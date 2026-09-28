import unittest
import json
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone, timedelta
from src.ingestion import RSSIngestionEngine


class TestRSSIngestionEngine(unittest.TestCase):
    """Unit tests for RSS feed ingestion and validation."""

    def setUp(self):
        self.engine = RSSIngestionEngine(digests_dir="test_digests")

    def test_get_last_digest_date_no_files(self):
        """Test fallback to T-1 when no historical digests exist."""
        with patch('glob.glob', return_value=[]):
            result = self.engine.get_last_digest_date()
            expected = datetime.now(timezone.utc) - timedelta(days=1)
            # Allow 1 second tolerance
            self.assertLess((result - expected).total_seconds(), 2)

    def test_scrape_feeds_returns_json(self):
        """Test that scrape_feeds returns valid JSON."""
        mock_feed = MagicMock()
        mock_entry = MagicMock()
        mock_entry.title = "Test Article"
        mock_entry.link = "https://example.com/article"
        mock_entry.summary = "Test summary"
        mock_entry.published_parsed = (2026, 9, 28, 12, 0, 0, 0, 0, 0)

        mock_feed.entries = [mock_entry]

        sources = [{"name": "Test Source", "url": "https://example.com/feed.xml"}]

        with patch('feedparser.parse', return_value=mock_feed):
            with patch.object(self.engine, 'get_last_digest_date') as mock_date:
                mock_date.return_value = datetime(2026, 9, 27, 0, 0, 0, tzinfo=timezone.utc)
                result = self.engine.scrape_feeds(sources)

        # Verify it returns valid JSON
        parsed = json.loads(result)
        self.assertIsInstance(parsed, list)

    def test_scrape_feeds_empty_feeds(self):
        """Test handling of empty feed results."""
        mock_feed = MagicMock()
        mock_feed.entries = []

        sources = [{"name": "Test Source", "url": "https://example.com/feed.xml"}]

        with patch('feedparser.parse', return_value=mock_feed):
            with patch.object(self.engine, 'get_last_digest_date'):
                result = self.engine.scrape_feeds(sources)

        # Should return empty JSON array
        self.assertEqual(result, "[]")

    def test_getattr_fallback_for_missing_summary(self):
        """Test that missing summary fields are handled gracefully."""
        mock_feed = MagicMock()
        mock_entry = MagicMock(spec=['title', 'link', 'published_parsed'])
        mock_entry.title = "Test Article"
        mock_entry.link = "https://example.com/article"
        mock_entry.published_parsed = (2026, 9, 28, 12, 0, 0, 0, 0, 0)
        # Don't set summary attribute

        mock_feed.entries = [mock_entry]
        sources = [{"name": "Test Source", "url": "https://example.com/feed.xml"}]

        with patch('feedparser.parse', return_value=mock_feed):
            with patch.object(self.engine, 'get_last_digest_date') as mock_date:
                mock_date.return_value = datetime(2026, 9, 27, 0, 0, 0, tzinfo=timezone.utc)
                result = self.engine.scrape_feeds(sources)

        parsed = json.loads(result)
        # Should use default summary
        self.assertEqual(parsed[0]['summary'], 'No summary provided.')


class TestConfigLoader(unittest.TestCase):
    """Unit tests for configuration loading."""

    def test_config_format(self):
        """Test that config is in expected format: {"sources": [...]]}."""
        from src.config_loader import ConfigLoader
        loader = ConfigLoader("config/sources.json")
        config = loader.load_sources()

        self.assertIn("sources", config)
        self.assertIsInstance(config["sources"], list)
        self.assertGreater(len(config["sources"]), 0)

        # Each source should have name and url
        for source in config["sources"]:
            self.assertIn("name", source)
            self.assertIn("url", source)


if __name__ == '__main__':
    unittest.main()
