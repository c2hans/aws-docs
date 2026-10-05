import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import sync_aws_docs as sync


class UrlMappingTests(unittest.TestCase):
    def test_maps_html_url_to_markdown_path(self):
        path = sync.url_to_local_path(
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html"
        )
        self.assertEqual(
            path,
            sync.DOCS_DIR / "AWSEC2/latest/UserGuide/concepts.md",
        )

    def test_rejects_traversal_and_query_collisions(self):
        unsafe = [
            "https://docs.aws.amazon.com/%2e%2e/scripts/x.html",
            "https://docs.aws.amazon.com/AWSEC2/page.html?version=1",
            "http://docs.aws.amazon.com/AWSEC2/page.html",
            "https://example.com/AWSEC2/page.html",
        ]
        for url in unsafe:
            with self.subTest(url=url), self.assertRaises(sync.SyncError):
                sync.url_to_local_path(url)


class DiscoveryTests(unittest.TestCase):
    def test_recursively_walks_nested_sitemap_indexes(self):
        responses = {
            "https://docs.aws.amazon.com/root.xml": (
                "sitemapindex",
                ["https://docs.aws.amazon.com/child.xml"],
            ),
            "https://docs.aws.amazon.com/child.xml": (
                "sitemapindex",
                ["https://docs.aws.amazon.com/pages.xml"],
            ),
            "https://docs.aws.amazon.com/pages.xml": (
                "urlset",
                ["https://docs.aws.amazon.com/guide/page.html"],
            ),
        }
        with mock.patch.object(sync, "fetch_xml_locs", side_effect=lambda u, _: responses[u]):
            pages = sync.discover_pages("https://docs.aws.amazon.com/root.xml", 1)
        self.assertEqual(pages, ["https://docs.aws.amazon.com/guide/page.html"])

    def test_rejects_sitemap_cycles(self):
        response = ("sitemapindex", ["https://docs.aws.amazon.com/root.xml"])
        with mock.patch.object(sync, "fetch_xml_locs", return_value=response):
            with self.assertRaises(sync.SyncError):
                sync.discover_pages("https://docs.aws.amazon.com/root.xml", 1)


class ManifestTests(unittest.TestCase):
    def test_non_object_manifest_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            path.write_text("[]")
            self.assertEqual(sync.Manifest(path).data, {})

    def test_dry_run_does_not_write_file_or_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            manifest = sync.Manifest(root / "manifest.json")
            url = "https://docs.aws.amazon.com/guide/page.html"
            result = sync.FetchResult(
                url,
                docs / "guide/page.md",
                "new content\n",
                "md",
                etag="etag",
            )
            with (
                mock.patch.object(sync, "DOCS_DIR", docs),
                mock.patch.object(sync, "REPO_ROOT", root),
                mock.patch.object(sync, "fetch_page", return_value=result),
            ):
                kind, _ = sync.process_url(url, 1, manifest, True, False)
            self.assertEqual(kind, "written")
            self.assertFalse(result.local_path.exists())
            self.assertEqual(manifest.data, {})

    def test_no_cache_ignores_validator_without_clearing_other_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            manifest = sync.Manifest(root / "manifest.json")
            manifest.data["https://docs.aws.amazon.com/other.html"] = {"etag": "keep"}
            url = "https://docs.aws.amazon.com/guide/page.html"
            result = sync.FetchResult(
                url,
                docs / "guide/page.md",
                "content\n",
                "md",
                etag="new",
            )
            with (
                mock.patch.object(sync, "DOCS_DIR", docs),
                mock.patch.object(sync, "REPO_ROOT", root),
                mock.patch.object(sync, "fetch_page", return_value=result) as fetch,
            ):
                sync.process_url(url, 1, manifest, False, True)
            fetch.assert_called_once_with(url, 1, None)
            self.assertIn("https://docs.aws.amazon.com/other.html", manifest.data)

    def test_stale_cleanup_preserves_locally_modified_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            path = docs / "guide/page.md"
            path.parent.mkdir(parents=True)
            path.write_text("locally modified\n")
            url = "https://docs.aws.amazon.com/guide/page.html"
            manifest = sync.Manifest(root / "manifest.json")
            manifest.data[url] = {"sha256": sync.sha256("old content\n")}
            failed_git = mock.Mock(returncode=1, stdout="", stderr="")
            with (
                mock.patch.object(sync, "DOCS_DIR", docs),
                mock.patch.object(sync, "REPO_ROOT", root),
                mock.patch.object(sync, "run_git", return_value=failed_git),
            ):
                removed, errors = sync.remove_stale_pages(
                    manifest, set(), False, lambda _: True
                )
            self.assertEqual(removed, [])
            self.assertEqual(len(errors), 1)
            self.assertTrue(path.exists())
            self.assertIn(url, manifest.data)

    def test_stale_cleanup_deletes_manifest_verified_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            path = docs / "guide/page.md"
            path.parent.mkdir(parents=True)
            path.write_text("old content\n")
            url = "https://docs.aws.amazon.com/guide/page.html"
            manifest = sync.Manifest(root / "manifest.json")
            manifest.data[url] = {"sha256": sync.sha256(path.read_text())}
            with (
                mock.patch.object(sync, "DOCS_DIR", docs),
                mock.patch.object(sync, "REPO_ROOT", root),
            ):
                removed, errors = sync.remove_stale_pages(
                    manifest, set(), False, lambda _: True
                )
            self.assertEqual(removed, [path])
            self.assertEqual(errors, [])
            self.assertFalse(path.exists())
            self.assertNotIn(url, manifest.data)


if __name__ == "__main__":
    unittest.main()
