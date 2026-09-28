import os
import glob
from datetime import datetime
from src.config_loader import ConfigLoader
from src.ingestion import RSSIngestionEngine
from src.editor import AIEditorialEngine

class DigestPipeline:
    def __init__(self, output_dir: str = "digests"):
        self.output_dir = output_dir
        self.config_loader = ConfigLoader()
        self.ingestion_engine = RSSIngestionEngine(digests_dir=output_dir)
        self.editorial_engine = AIEditorialEngine() # Instantiated as editorial_engine

    def _get_next_version(self, today_str: str) -> int:
        """Find the next available version number for today's digest."""
        search_pattern = os.path.join(self.output_dir, f"{today_str}_daily_brief_v*.md")
        existing_files = glob.glob(search_pattern)

        if not existing_files:
            return 1

        versions = []
        for file_path in existing_files:
            filename = os.path.basename(file_path)
            # Extract version number from "YYYY-MM-DD_daily_brief_vX.md"
            try:
                version_str = filename.split("_v")[-1].replace(".md", "")
                versions.append(int(version_str))
            except (ValueError, IndexError):
                continue

        return max(versions) + 1 if versions else 1

    def _persist_to_disk(self, content: str) -> str:
        """Internal helper handling file persistence with versioning."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        today_str = datetime.now().strftime("%Y-%m-%d")
        version = self._get_next_version(today_str)
        file_path = os.path.join(self.output_dir, f"{today_str}_daily_brief_v{version}.md")
        meta_header = f"# Daily AI Research Digest\n*Generated on: {datetime.now().strftime('%B %d, %Y at %H:%M')}*\n\n"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(meta_header + content)
        return file_path

    def run(self):
        """Orchestrates the ingestion, processing, and output generation."""
        print("📁 Loading news source channels from JSON config...")
        config_data = self.config_loader.load_sources()
        sources = config_data.get("sources", [])

        if not sources:
            raise ValueError("No sources found in configuration file. Check config/sources.json.")

        print("📡 Triggering self-healing adaptive gap scan...")
        raw_data = self.ingestion_engine.scrape_feeds(sources)

        if not raw_data or raw_data == "[]":
            print("📅 No new articles found within the gap scan window today. Exiting smoothly.")
            return "No updates."

        print("🤖 Forwarding collected data delta to AI Editorial Engine...")
        digest_content = self.editorial_engine.generate_digest(raw_data)

        print("💾 Persisting generated markdown intelligence brief to disk...")
        saved_path = self._persist_to_disk(digest_content)

        print(f"✅ Success! Daily brief compiled cleanly at: {saved_path}")
        return "Pipeline run executed successfully."