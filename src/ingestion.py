import os
import glob
import time
import json
import feedparser
from datetime import datetime, timezone, timedelta

class RSSIngestionEngine:
    def __init__(self, digests_dir: str = "digests"):
        self.digests_dir = digests_dir
        self.gap_days = 0  # Track gap for naming purposes

    def get_last_digest_date(self) -> tuple:
        """
        Scans the persistence directory for historical briefs to extract
        the latest PREVIOUS digest (excluding today) and calculate the dynamic gap.

        Returns: (last_previous_digest_date, gap_days)
        """
        search_path = os.path.join(self.digests_dir, "*_daily_brief*.md")
        existing_briefs = glob.glob(search_path)
        today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        if not existing_briefs:
            print("⚠️ No historical digests found. Defaulting scan window to T-1.")
            today = datetime.now(timezone.utc)
            default_date = today - timedelta(days=1)
            return default_date, 1

        dates = []
        for file_path in existing_briefs:
            filename = os.path.basename(file_path)
            date_str = filename.split("_")[0] # Extracts 'YYYY-MM-DD'
            try:
                parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
                parsed_date = parsed_date.replace(tzinfo=timezone.utc)

                # Exclude today's digests - we want the last PREVIOUS digest
                if date_str != today_str:
                    dates.append(parsed_date)
            except ValueError:
                continue

        if not dates:
            print("⚠️ No previous digests found. Defaulting scan window to T-1.")
            today = datetime.now(timezone.utc)
            default_date = today - timedelta(days=1)
            return default_date, 1

        # Calculate dynamic gap from last PREVIOUS digest to today
        last_previous_digest_date = max(dates)
        today = datetime.now(timezone.utc)
        gap_days = (today - last_previous_digest_date).days

        print(f"📊 Gap Analysis: Last previous digest on {last_previous_digest_date.strftime('%Y-%m-%d')}, gap = T-{gap_days} days")

        return last_previous_digest_date, gap_days

    def scrape_feeds(self, sources: list) -> str:
        """
        Iterates over target feed URLs and harvests posts published
        strictly within the calculated execution tracking window.
        """
        # 1. Fetch our dynamic historical watermark date boundary
        last_digest_date, gap_days = self.get_last_digest_date()
        self.gap_days = gap_days  # Store for pipeline to use for naming
        now_utc = datetime.now(timezone.utc)

        print(f"⏱️ Scan Window Baseline: Ingesting articles published between {last_digest_date} and {now_utc} (T-{gap_days} days)")
        
        scraped_payload = []

        # 2. Iterate through each platform source target mapped in sources.json
        for source in sources:
            feed_url = source.get("url")
            source_name = source.get("name", "Unknown Source")
            
            print(f"📡 Querying endpoint: {source_name}")
            parsed_feed = feedparser.parse(feed_url)
            
            for entry in parsed_feed.entries:
                # Fallback guard in case an RSS feed lacks parsed time metadata
                if not getattr(entry, "published_parsed", None):
                    continue
                
                # --- YOUR DATE MATH INJECTED HERE ---
                # Convert the raw RSS feed time tuple to a timezone-aware datetime object
                post_time = datetime.fromtimestamp(time.mktime(entry.published_parsed), tz=timezone.utc)
                
                # Clean, safe evaluation boundary loop tracking the gap window
                if last_digest_date < post_time <= now_utc:
                    scraped_payload.append({
                        "source": source_name,
                        "title": entry.title,
                        "link": entry.link,
                        "summary": getattr(entry, 'summary', 'No summary provided.')
                    })

        # 3. Serialize gathered items into a JSON payload for the LLM Editor
        if not scraped_payload:
            return json.dumps([])

        return json.dumps(scraped_payload)