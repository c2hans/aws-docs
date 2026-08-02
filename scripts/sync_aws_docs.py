#!/usr/bin/env python3
"""
Sync AWS documentation (docs.aws.amazon.com) into a local, diffable Markdown
mirror under docs/, and commit any changes to git.

Strategy per page:
  1. Fetch the site's native Markdown export (<path>.md, Content-Type: text/markdown).
     Every public docs.aws.amazon.com page serves one; a page that doesn't is
     logged as an error rather than scraped from HTML.
  2. Normalize whitespace, so re-running the script against unchanged upstream
     content always reproduces byte-identical output (idempotent -> empty
     `git status`).

Discovery: AWS publishes a sitemap index (https://docs.aws.amazon.com/sitemap_index.xml)
listing ~10,900 per-guide sitemaps across 11 locales. By default only the
English (no locale prefix) guides are synced.

A local cache manifest (.cache/manifest.json, gitignored) stores each page's
ETag/Last-Modified/content hash so re-runs use conditional GETs and skip
reconverting unchanged pages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://docs.aws.amazon.com"
SITEMAP_INDEX = f"{BASE}/sitemap_index.xml"
USER_AGENT = "aws-docs-sync/1.0 (+offline markdown mirror; personal archival use)"

# Locale path prefixes AWS uses for translated docs. Anything NOT matching
# one of these is treated as English/default.
LOCALE_PREFIX_RE = re.compile(
    r"^/(ar|de_de|en_us|es_es|fr_fr|id_id|it_it|ja_jp|ko_kr|pt_br|zh_cn|zh_tw|ru_ru)/"
)

# Per-class/per-method language-SDK, CLI, CDK, and PowerShell references are
# mechanically generated from source code (one page per class/method/command)
# rather than hand-written product documentation. They dwarf everything else
# (~84% of all English pages) and their diffs mostly reflect SDK codegen, not
# product/doc changes. Excluded by default; --include-sdk-references disables
# this filter. Hand-written developer/user guides for the same SDKs (e.g.
# sdk-for-java/*/developer-guide, powershell/*/userguide) are NOT matched here
# and are always synced.
SDK_REFERENCE_PATTERNS = [
    r"/apidocs/",                              # sdkfornet (.NET) API docs
    r"/javadoc/",                              # AWSJavaSDK, xray-sdk-for-java
    r"sdk-for-ruby/[^/]+/api/",                # Ruby SDK + gem API docs
    r"aws-sdk-php/v[123]/",                    # PHP SDK site (guide + API docs, all versions)
    r"AWSJavaScriptSDK/",                      # JS SDK v2 API docs
    r"cdk/api/",                               # CDK construct library reference
    r"powershell/v\d+/reference/",             # PowerShell cmdlet reference
    r"^https://docs\.aws\.amazon\.com/cli/(latest|v\d+)/sitemap\.xml$",  # CLI command reference
]
SDK_REFERENCE_RE = re.compile("|".join(SDK_REFERENCE_PATTERNS))


def is_sdk_reference(url: str) -> bool:
    return bool(SDK_REFERENCE_RE.search(url))

XML_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
STATE_DIR = REPO_ROOT / ".cache"
MANIFEST_PATH = STATE_DIR / "manifest.json"


def make_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_maxsize=64, pool_connections=64)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    s.headers.update({"User-Agent": USER_AGENT})
    return s


_thread_local = threading.local()


def session() -> requests.Session:
    if not hasattr(_thread_local, "session"):
        _thread_local.session = make_session()
    return _thread_local.session


# --------------------------------------------------------------------------
# Discovery
# --------------------------------------------------------------------------

def is_english(url: str) -> bool:
    return not LOCALE_PREFIX_RE.match(urlparse(url).path)


def fetch_xml_locs(url: str, timeout: float) -> tuple[str, list[str]]:
    """Fetch a sitemap (index or urlset) and return (root_tag, locs)."""
    resp = session().get(url, timeout=timeout)
    resp.raise_for_status()
    root = ElementTree.fromstring(resp.content)
    tag = root.tag.replace(XML_NS, "")
    locs = [
        el.text.strip()
        for el in root.iter(f"{XML_NS}loc")
        if el.text and el.text.strip()
    ]
    return tag, locs


def discover_guide_sitemaps(
    timeout: float, english_only: bool, exclude_sdk_references: bool = True
) -> list[str]:
    tag, locs = fetch_xml_locs(SITEMAP_INDEX, timeout)
    assert tag == "sitemapindex", f"unexpected root tag {tag} for sitemap index"
    if english_only:
        locs = [l for l in locs if is_english(l)]
    if exclude_sdk_references:
        locs = [l for l in locs if not is_sdk_reference(l)]
    return sorted(set(locs))


def discover_pages(sitemap_url: str, timeout: float) -> list[str]:
    """A guide's sitemap.xml is normally a <urlset>. Handle nested indexes too."""
    tag, locs = fetch_xml_locs(sitemap_url, timeout)
    pages: list[str] = []
    if tag == "sitemapindex":
        for sub in locs:
            try:
                _, sub_locs = fetch_xml_locs(sub, timeout)
                pages.extend(sub_locs)
            except (requests.RequestException, ElementTree.ParseError):
                continue
    else:
        pages.extend(locs)
    base_host = urlparse(BASE).netloc
    return [
        p
        for p in pages
        if urlparse(p).path.endswith(".html") and urlparse(p).netloc == base_host
    ]


# --------------------------------------------------------------------------
# Fetch + convert
# --------------------------------------------------------------------------

@dataclass
class FetchResult:
    url: str
    local_path: Path
    markdown: str | None
    source: str  # "md" | "cached" | "error"
    etag: str | None = None
    last_modified: str | None = None
    error: str | None = None


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip("\n")
    return text + "\n"


def front_matter(source_url: str) -> str:
    return f"---\nsource_url: {source_url}\n---\n\n"


def url_to_local_path(url: str) -> Path:
    path = urlparse(url).path.lstrip("/")
    if path.endswith(".html"):
        path = path[: -len(".html")] + ".md"
    return DOCS_DIR / path


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_page(url: str, timeout: float, cache_entry: dict | None) -> FetchResult:
    local_path = url_to_local_path(url)
    # Plain suffix swap, not urljoin: some sitemap URLs (e.g. the /solutions/
    # tree) contain a doubled slash right after the domain, and urljoin()
    # treats a path starting with "//" as a protocol-relative reference,
    # silently discarding the real host in favor of the first path segment.
    md_url = url[: -len(".html")] + ".md"

    headers = {}
    if cache_entry:
        if cache_entry.get("etag"):
            headers["If-None-Match"] = cache_entry["etag"]
        if cache_entry.get("last_modified"):
            headers["If-Modified-Since"] = cache_entry["last_modified"]

    try:
        resp = session().get(md_url, timeout=timeout, headers=headers)
    except requests.RequestException as e:
        return FetchResult(url, local_path, None, "error", error=str(e))

    if resp.status_code == 304:
        return FetchResult(
            url,
            local_path,
            None,
            "cached",
            etag=cache_entry.get("etag"),
            last_modified=cache_entry.get("last_modified"),
        )

    if resp.status_code == 200 and "markdown" in resp.headers.get("Content-Type", ""):
        body = normalize_markdown(front_matter(url) + resp.text)
        return FetchResult(
            url,
            local_path,
            body,
            "md",
            etag=resp.headers.get("ETag"),
            last_modified=resp.headers.get("Last-Modified"),
        )

    return FetchResult(
        url,
        local_path,
        None,
        "error",
        error=f"no markdown export at {md_url} (status {resp.status_code}, "
        f"content-type {resp.headers.get('Content-Type')!r})",
    )


# --------------------------------------------------------------------------
# Manifest cache
# --------------------------------------------------------------------------

class Manifest:
    def __init__(self, path: Path):
        self.path = path
        self.lock = threading.Lock()
        self.data: dict[str, dict] = {}
        if path.exists():
            try:
                self.data = json.loads(path.read_text())
            except (json.JSONDecodeError, OSError):
                self.data = {}
        self._dirty_count = 0

    def get(self, url: str) -> dict | None:
        return self.data.get(url)

    def update(self, url: str, entry: dict, flush_every: int = 100) -> None:
        with self.lock:
            self.data[url] = entry
            self._dirty_count += 1
            if self._dirty_count >= flush_every:
                self._flush_locked()

    def flush(self) -> None:
        with self.lock:
            self._flush_locked()

    def _flush_locked(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=0, sort_keys=True))
        tmp.replace(self.path)
        self._dirty_count = 0


# --------------------------------------------------------------------------
# Git
# --------------------------------------------------------------------------

def run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=False
    )


def git_stage_and_count(repo_dir: Path) -> int:
    run_git(["add", "--", "docs"], repo_dir)
    r = run_git(["diff", "--cached", "--name-only", "--", "docs"], repo_dir)
    return len([l for l in r.stdout.splitlines() if l.strip()])


def git_commit(repo_dir: Path, message: str) -> bool:
    r = run_git(["commit", "-m", message], repo_dir)
    if r.returncode != 0:
        print(f"git commit failed: {r.stdout}\n{r.stderr}", file=sys.stderr)
        return False
    return True


def git_push(repo_dir: Path) -> None:
    r = run_git(["remote"], repo_dir)
    if "origin" not in r.stdout.split():
        print("No 'origin' remote configured; skipping push.", file=sys.stderr)
        return
    r = run_git(["push", "origin", "HEAD"], repo_dir)
    if r.returncode != 0:
        print(f"git push failed: {r.stdout}\n{r.stderr}", file=sys.stderr)
    else:
        print("Pushed to origin.")


# --------------------------------------------------------------------------
# Main sync
# --------------------------------------------------------------------------

@dataclass
class Stats:
    total: int = 0
    written: int = 0
    unchanged: int = 0
    cached_skip: int = 0
    errors: int = 0
    lock: threading.Lock = field(default_factory=threading.Lock)

    def bump(self, **kw):
        with self.lock:
            for k, v in kw.items():
                setattr(self, k, getattr(self, k) + v)


def process_url(url: str, timeout: float, manifest: Manifest, dry_run: bool) -> tuple[str, str]:
    cache_entry = manifest.get(url)
    local_path = url_to_local_path(url)
    if cache_entry:
        # Local mirror must still exist and match what the manifest recorded,
        # otherwise the cache (and any conditional-GET 304) can't be trusted.
        if not local_path.exists():
            cache_entry = None
        else:
            on_disk_hash = sha256(local_path.read_text())
            if on_disk_hash != cache_entry.get("sha256"):
                cache_entry = None
    result = fetch_page(url, timeout, cache_entry)

    if result.source == "error":
        return "error", f"{url}: {result.error}"

    if result.source == "cached":
        return "cached_skip", url

    local_path = result.local_path
    existing = local_path.read_text() if local_path.exists() else None
    changed = existing != result.markdown

    if changed and not dry_run:
        local_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = local_path.with_suffix(local_path.suffix + ".tmp")
        tmp_path.write_text(result.markdown)
        tmp_path.replace(local_path)

    manifest.update(
        url,
        {
            "etag": result.etag,
            "last_modified": result.last_modified,
            "sha256": sha256(result.markdown),
            "local_path": str(local_path.relative_to(REPO_ROOT)),
        },
    )

    return ("written" if changed else "unchanged"), url


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--timeout", type=float, default=20.0)
    ap.add_argument("--limit", type=int, default=None, help="max pages to process (testing)")
    ap.add_argument("--max-sitemaps", type=int, default=None, help="max guide sitemaps to scan (testing)")
    ap.add_argument("--guide-filter", default=None, help="regex; only sync guide sitemaps whose URL matches")
    ap.add_argument("--all-locales", action="store_true", help="include translated docs (default: English only)")
    ap.add_argument(
        "--include-sdk-references",
        action="store_true",
        help="include per-class/per-method language SDK, CLI, CDK, and PowerShell "
        "references (default: excluded, see SDK_REFERENCE_PATTERNS)",
    )
    ap.add_argument("--no-cache", action="store_true", help="ignore manifest, force full refetch")
    ap.add_argument("--dry-run", action="store_true", help="fetch/convert only, do not write files")
    ap.add_argument("--commit", dest="commit", action="store_true", default=True)
    ap.add_argument("--no-commit", dest="commit", action="store_false")
    ap.add_argument("--push", action="store_true", default=False)
    args = ap.parse_args()

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = Manifest(MANIFEST_PATH)
    if args.no_cache:
        manifest.data = {}

    print("Discovering guide sitemaps...", file=sys.stderr)
    guide_sitemaps = discover_guide_sitemaps(
        args.timeout,
        english_only=not args.all_locales,
        exclude_sdk_references=not args.include_sdk_references,
    )
    if args.guide_filter:
        pat = re.compile(args.guide_filter)
        guide_sitemaps = [g for g in guide_sitemaps if pat.search(g)]
    if args.max_sitemaps:
        guide_sitemaps = guide_sitemaps[: args.max_sitemaps]
    print(f"{len(guide_sitemaps)} guide sitemap(s) selected.", file=sys.stderr)

    all_pages: list[str] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(discover_pages, gs, args.timeout): gs for gs in guide_sitemaps}
        i = 0
        for fut in as_completed(futures):
            gs = futures[fut]
            try:
                pages = fut.result()
            except (requests.RequestException, ElementTree.ParseError) as e:
                print(f"WARN: failed to read {gs}: {e}", file=sys.stderr)
                continue
            finally:
                i += 1
            all_pages.extend(pages)
            if i % 200 == 0 or i == len(guide_sitemaps):
                print(f"  scanned {i}/{len(guide_sitemaps)} sitemaps, {len(all_pages)} pages so far", file=sys.stderr)

    all_pages = sorted(set(all_pages))
    if args.limit:
        all_pages = all_pages[: args.limit]
    print(f"{len(all_pages)} page(s) to sync.", file=sys.stderr)

    stats = Stats(total=len(all_pages))
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(process_url, url, args.timeout, manifest, args.dry_run): url
            for url in all_pages
        }
        done = 0
        for fut in as_completed(futures):
            kind, info = fut.result()
            if kind == "error":
                stats.bump(errors=1)
                print(f"ERROR {info}", file=sys.stderr)
            elif kind == "written":
                stats.bump(written=1)
            elif kind == "unchanged":
                stats.bump(unchanged=1)
            elif kind == "cached_skip":
                stats.bump(cached_skip=1)
            done += 1
            if done % 200 == 0 or done == len(all_pages):
                elapsed = time.time() - t0
                print(
                    f"  {done}/{len(all_pages)} done "
                    f"(written={stats.written} unchanged={stats.unchanged} "
                    f"cached={stats.cached_skip} errors={stats.errors}) "
                    f"[{elapsed:.0f}s]",
                    file=sys.stderr,
                )

    manifest.flush()

    print(
        f"\nDone. total={stats.total} written={stats.written} "
        f"unchanged={stats.unchanged} cached_skip={stats.cached_skip} "
        f"errors={stats.errors} elapsed={time.time()-t0:.0f}s",
        file=sys.stderr,
    )

    if args.commit and not args.dry_run:
        n = git_stage_and_count(REPO_ROOT)
        if n:
            msg = f"Sync AWS docs: {n} page(s) changed ({time.strftime('%Y-%m-%d')})"
            if git_commit(REPO_ROOT, msg):
                print(f"Committed: {msg}")
                if args.push:
                    git_push(REPO_ROOT)
            else:
                print("Commit failed; see errors above.", file=sys.stderr)
                return 1
        else:
            print("No changes to commit.")

    return 0 if stats.errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
