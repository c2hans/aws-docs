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
import fcntl
import hashlib
import json
import re
import subprocess
import sys
import threading
import time
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse, urlunparse
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
    r"^https://docs\.aws\.amazon\.com/cli/(latest|v\d+)/",  # CLI command reference
]
SDK_REFERENCE_RE = re.compile("|".join(SDK_REFERENCE_PATTERNS))


def is_sdk_reference(url: str) -> bool:
    return bool(SDK_REFERENCE_RE.search(url))

# Most sitemaps use the canonical http:// namespace, but a few (e.g.
# codeguru/detector-library) declare https://.
XML_NAMESPACES = (
    "{http://www.sitemaps.org/schemas/sitemap/0.9}",
    "{https://www.sitemaps.org/schemas/sitemap/0.9}",
)
MAX_REDIRECTS = 10
# Abort the page phase after this many 403s in a row: docs.aws.amazon.com is
# blocking this client, and continuing only prolongs the block.
MAX_CONSECUTIVE_BLOCKED = 50

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
STATE_DIR = REPO_ROOT / ".cache"
MANIFEST_PATH = STATE_DIR / "manifest.json"
LOCK_PATH = STATE_DIR / "sync.lock"


class SyncError(RuntimeError):
    pass


class RetiredSitemap(SyncError):
    """A sitemap AWS still lists but that no longer describes a live guide.

    The index keeps entries for guides that were retired or merged elsewhere:
    their sitemap.xml redirects off-site, to an HTML landing page, or to a
    404, or is an empty <urlset>. These are skipped rather than treated as
    discovery failures, which would otherwise block every full sync.
    """


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
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https" or parsed_url.netloc != urlparse(BASE).netloc:
        raise SyncError(f"unsupported sitemap URL: {url}")

    # Follow redirects by hand so we never fetch from outside docs.aws.amazon.com.
    # AWS's own chains sometimes bounce through http:// or an explicit :443.
    current = url
    redirected = False
    for _ in range(MAX_REDIRECTS + 1):
        resp = session().get(current, timeout=timeout, allow_redirects=False)
        if not resp.is_redirect:
            break
        target = urljoin(current, resp.headers["Location"])
        parsed_target = urlparse(target)
        if parsed_target.hostname != urlparse(BASE).hostname or parsed_target.port not in {
            None,
            443,
        }:
            raise RetiredSitemap(f"sitemap redirects off docs.aws.amazon.com: {target}")
        current = urlunparse(parsed_target._replace(scheme="https", netloc=urlparse(BASE).netloc))
        redirected = True
    else:
        raise SyncError(f"too many redirects for sitemap {url}")

    if resp.status_code in {404, 410} or (redirected and resp.status_code == 403):
        raise RetiredSitemap(f"sitemap {url} resolves to HTTP {resp.status_code} at {current}")
    resp.raise_for_status()

    if redirected and "xml" not in resp.headers.get("Content-Type", "").lower():
        # AWS's index occasionally retains a sitemap URL after a guide becomes a
        # single page. In that case the URL redirects directly to the HTML page.
        if urlparse(current).path.endswith(".html"):
            return "urlset", [current]
        raise RetiredSitemap(f"sitemap {url} redirects to a non-sitemap page: {current}")

    root = ElementTree.fromstring(resp.content)
    ns = next((n for n in XML_NAMESPACES if root.tag.startswith(n)), None)
    tag = root.tag[len(ns):] if ns else root.tag
    if tag not in {"sitemapindex", "urlset"}:
        raise SyncError(f"unexpected root tag {root.tag!r} for {url}")
    locs = [
        el.text.strip()
        for el in root.iter(f"{ns}loc")
        if el.text and el.text.strip()
    ]
    return tag, locs


def discover_guide_sitemaps(
    timeout: float, english_only: bool, exclude_sdk_references: bool = True
) -> list[str]:
    tag, locs = fetch_xml_locs(SITEMAP_INDEX, timeout)
    if tag != "sitemapindex" or not locs:
        raise SyncError(f"invalid or empty sitemap index at {SITEMAP_INDEX}")
    if english_only:
        locs = [l for l in locs if is_english(l)]
    if exclude_sdk_references:
        locs = [l for l in locs if not is_sdk_reference(l)]
    return sorted(set(locs))


def discover_pages(sitemap_url: str, timeout: float) -> list[str]:
    """Recursively read a guide sitemap, failing if any branch is incomplete."""
    pages: list[str] = []
    seen: set[str] = set()

    def walk(url: str, depth: int = 0) -> None:
        if depth > 10:
            raise SyncError(f"sitemap nesting exceeds 10 levels at {url}")
        if url in seen:
            raise SyncError(f"sitemap cycle detected at {url}")
        seen.add(url)
        try:
            tag, locs = fetch_xml_locs(url, timeout)
        except RetiredSitemap as e:
            if depth == 0:
                raise
            print(f"WARN: skipping retired child sitemap: {e}", file=sys.stderr)
            return
        if tag == "sitemapindex":
            for sub in locs:
                walk(sub, depth + 1)
        else:
            pages.extend(locs)

    walk(sitemap_url)
    if not pages:
        raise RetiredSitemap(f"sitemap contains no pages: {sitemap_url}")
    base_host = urlparse(BASE).netloc
    return [
        p
        for p in pages
        if urlparse(p).path.endswith(".html")
        and urlparse(p).scheme == "https"
        and urlparse(p).netloc == base_host
    ]


# --------------------------------------------------------------------------
# Fetch + convert
# --------------------------------------------------------------------------

@dataclass
class FetchResult:
    url: str
    local_path: Path
    markdown: str | None
    source: str  # "md" | "cached" | "error" | "blocked"
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
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != urlparse(BASE).netloc:
        raise SyncError(f"unsupported documentation URL: {url}")
    if parsed.query or parsed.fragment:
        raise SyncError(f"documentation URL has query or fragment: {url}")
    decoded_path = unquote(parsed.path)
    if "\\" in decoded_path or "\x00" in decoded_path:
        raise SyncError(f"unsafe documentation path: {url}")
    parts = Path(decoded_path).parts
    if ".." in parts:
        raise SyncError(f"documentation path escapes docs directory: {url}")
    path = decoded_path.lstrip("/")
    if path.endswith(".html"):
        path = path[: -len(".html")] + ".md"
    else:
        raise SyncError(f"documentation URL does not end in .html: {url}")
    local_path = DOCS_DIR / path
    try:
        local_path.resolve().relative_to(DOCS_DIR.resolve())
    except ValueError as e:
        raise SyncError(f"documentation path escapes docs directory: {url}") from e
    return local_path


def markdown_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.path.endswith(".html"):
        raise SyncError(f"documentation URL does not end in .html: {url}")
    return urlunparse(parsed._replace(path=parsed.path[:-5] + ".md"))


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_page(url: str, timeout: float, cache_entry: dict | None) -> FetchResult:
    local_path = url_to_local_path(url)
    md_url = markdown_url(url)

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

    final_url = urlparse(resp.url)
    if final_url.scheme != "https" or final_url.netloc != urlparse(BASE).netloc:
        return FetchResult(
            url, local_path, None, "error", error=f"redirected off docs.aws.amazon.com: {resp.url}"
        )

    if resp.status_code == 304 and cache_entry:
        return FetchResult(
            url,
            local_path,
            None,
            "cached",
            etag=cache_entry.get("etag"),
            last_modified=cache_entry.get("last_modified"),
        )

    if resp.status_code == 200 and "markdown" in resp.headers.get("Content-Type", "").lower():
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
        # CloudFront answers every path with 403 once it starts rate-limiting us.
        "blocked" if resp.status_code == 403 else "error",
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
                if not isinstance(self.data, dict):
                    self.data = {}
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

    def remove(self, url: str) -> None:
        with self.lock:
            if self.data.pop(url, None) is not None:
                self._dirty_count += 1

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


def require_clean_auto_commit(repo_dir: Path, manifest: Manifest) -> list[Path]:
    """Check docs/ only has changes left by an earlier, uncommitted sync.

    Returns those leftover paths so this run commits them too: their manifest
    entries are current, so this run would otherwise see them as cached and
    never stage them.
    """
    staged = run_git(["diff", "--cached", "--quiet"], repo_dir)
    if staged.returncode not in {0, 1}:
        raise SyncError(staged.stderr.strip() or "failed to inspect git index")
    docs_status = run_git(
        ["status", "--porcelain", "-z", "--untracked-files=all", "--", "docs"], repo_dir
    )
    if docs_status.returncode != 0:
        raise SyncError(docs_status.stderr.strip() or "failed to inspect docs worktree")
    if staged.returncode == 1:
        raise SyncError("auto-commit requires an empty git index")
    entries_by_path = {
        entry.get("local_path"): entry for entry in manifest.data.values()
    }
    leftovers: list[Path] = []
    for line in filter(None, docs_status.stdout.split("\0")):
        relative_path = line[3:]
        path = repo_dir / relative_path
        entry = entries_by_path.get(relative_path)
        if (
            not entry
            or not path.is_file()
            or entry.get("sha256") != sha256(path.read_text())
        ):
            raise SyncError(
                "docs/ has changes not produced by a recoverable previous sync: "
                f"{relative_path}"
            )
        leftovers.append(path)
    return leftovers


def git_stage_and_count(repo_dir: Path, paths: list[Path]) -> int:
    relative_paths = sorted({str(p.relative_to(repo_dir)) for p in paths})
    for start in range(0, len(relative_paths), 500):
        r = run_git(["add", "--", *relative_paths[start : start + 500]], repo_dir)
        if r.returncode != 0:
            raise SyncError(r.stderr.strip() or "git add failed")
    r = run_git(["diff", "--cached", "--name-only"], repo_dir)
    if r.returncode != 0:
        raise SyncError(r.stderr.strip() or "git diff failed")
    staged_paths = {line for line in r.stdout.splitlines() if line.strip()}
    unexpected = staged_paths - set(relative_paths)
    if unexpected:
        raise SyncError(
            "refusing to commit unrelated staged paths: " + ", ".join(sorted(unexpected))
        )
    return len(staged_paths)


def git_commit(repo_dir: Path, message: str) -> bool:
    r = run_git(["commit", "-m", message], repo_dir)
    if r.returncode != 0:
        print(f"git commit failed: {r.stdout}\n{r.stderr}", file=sys.stderr)
        return False
    return True


def git_push(repo_dir: Path) -> bool:
    r = run_git(["remote"], repo_dir)
    if r.returncode != 0:
        print(f"git remote failed: {r.stderr}", file=sys.stderr)
        return False
    if "origin" not in r.stdout.split():
        print("No 'origin' remote configured; cannot push.", file=sys.stderr)
        return False
    r = run_git(["push", "origin", "HEAD"], repo_dir)
    if r.returncode != 0:
        print(f"git push failed: {r.stdout}\n{r.stderr}", file=sys.stderr)
        return False
    else:
        print("Pushed to origin.")
        return True


@contextmanager
def process_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as lock_file:
        try:
            fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as e:
            raise SyncError("another AWS docs sync is already running") from e
        yield


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


def process_url(
    url: str, timeout: float, manifest: Manifest, dry_run: bool, no_cache: bool
) -> tuple[str, str]:
    cache_entry = None if no_cache else manifest.get(url)
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

    if result.source in {"error", "blocked"}:
        return result.source, f"{url}: {result.error}"

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

    if not dry_run:
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


def remove_stale_pages(
    manifest: Manifest,
    discovered: set[str],
    dry_run: bool,
    eligible,
) -> tuple[list[Path], list[str]]:
    candidates: dict[str, tuple[Path, dict | None]] = {}
    errors: list[str] = []
    discovered_paths = {url_to_local_path(url) for url in discovered}
    for url, entry in list(manifest.data.items()):
        if not eligible(url):
            continue
        try:
            path = url_to_local_path(url)
            if path in discovered_paths:
                if url not in discovered and not dry_run:
                    manifest.remove(url)
                continue
            candidates[url] = (path, entry)
        except (OSError, UnicodeError, SyncError) as e:
            errors.append(f"failed to remove stale page for {url}: {e}")

    # The manifest is local and gitignored, so a fresh clone needs the tracked
    # tree as a second source of managed stale-page candidates.
    for path in DOCS_DIR.rglob("*.md"):
        relative = path.relative_to(DOCS_DIR).as_posix()
        url = f"{BASE}/{relative[:-3]}.html"
        if path not in discovered_paths and eligible(url):
            candidates.setdefault(url, (path, manifest.get(url)))

    for url, (path, entry) in candidates.items():
        if not path.exists():
            continue
        expected_hash = entry.get("sha256") if entry else None
        hash_matches = (
            isinstance(expected_hash, str)
            and len(expected_hash) == 64
            and sha256(path.read_text()) == expected_hash
        )
        if not hash_matches:
            relative = str(path.relative_to(REPO_ROOT))
            tracked = run_git(["ls-files", "--error-unmatch", "--", relative], REPO_ROOT)
            clean = run_git(["diff", "--quiet", "--", relative], REPO_ROOT)
            staged_clean = run_git(
                ["diff", "--cached", "--quiet", "--", relative], REPO_ROOT
            )
            if (
                tracked.returncode != 0
                or clean.returncode != 0
                or staged_clean.returncode != 0
            ):
                errors.append(f"refusing to delete unverified stale page {path}")

    if errors:
        return [], errors

    removed: list[Path] = []
    for url, (path, _) in candidates.items():
        if path.exists():
            if not dry_run:
                path.unlink()
            removed.append(path)
        if not dry_run:
            manifest.remove(url)
    return removed, errors


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

    if args.workers < 1:
        ap.error("--workers must be positive")
    if args.timeout <= 0:
        ap.error("--timeout must be positive")

    for name in ("limit", "max_sitemaps"):
        value = getattr(args, name)
        if value is not None and value < 0:
            ap.error(f"--{name.replace('_', '-')} must be nonnegative")

    try:
        if args.dry_run:
            return run_sync(args)
        with process_lock(LOCK_PATH):
            return run_sync(args)
    except SyncError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


def run_sync(args: argparse.Namespace) -> int:
    if not args.dry_run:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = Manifest(MANIFEST_PATH)
    leftover_paths: list[Path] = []
    if args.commit and not args.dry_run:
        leftover_paths = require_clean_auto_commit(REPO_ROOT, manifest)

    print("Discovering guide sitemaps...", file=sys.stderr)
    guide_sitemaps = discover_guide_sitemaps(
        args.timeout,
        english_only=not args.all_locales,
        exclude_sdk_references=not args.include_sdk_references,
    )
    if args.guide_filter:
        pat = re.compile(args.guide_filter)
        guide_sitemaps = [g for g in guide_sitemaps if pat.search(g)]
        if not guide_sitemaps:
            raise SyncError(f"guide filter matched no sitemaps: {args.guide_filter}")
    if args.max_sitemaps is not None:
        guide_sitemaps = guide_sitemaps[: args.max_sitemaps]
    print(f"{len(guide_sitemaps)} guide sitemap(s) selected.", file=sys.stderr)

    all_pages: list[str] = []
    discovery_errors = 0
    retired_sitemaps = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(discover_pages, gs, args.timeout): gs for gs in guide_sitemaps}
        i = 0
        for fut in as_completed(futures):
            gs = futures[fut]
            try:
                pages = fut.result()
            except RetiredSitemap as e:
                print(f"WARN: skipping retired guide: {e}", file=sys.stderr)
                retired_sitemaps += 1
                continue
            except (requests.RequestException, ElementTree.ParseError, SyncError) as e:
                print(f"WARN: failed to read {gs}: {e}", file=sys.stderr)
                discovery_errors += 1
                continue
            finally:
                i += 1
            all_pages.extend(pages)
            if i % 200 == 0 or i == len(guide_sitemaps):
                print(f"  scanned {i}/{len(guide_sitemaps)} sitemaps, {len(all_pages)} pages so far", file=sys.stderr)

    all_pages = sorted(set(all_pages))
    if retired_sitemaps:
        print(f"Skipped {retired_sitemaps} retired guide sitemap(s).", file=sys.stderr)
    if discovery_errors:
        print(
            f"ERROR: discovery failed for {discovery_errors} sitemap(s); aborting sync",
            file=sys.stderr,
        )
        return 1
    try:
        destinations = [url_to_local_path(url) for url in all_pages]
    except SyncError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    if len(set(destinations)) != len(destinations):
        print("ERROR: multiple documentation URLs map to the same local path", file=sys.stderr)
        return 1
    if args.limit is not None:
        all_pages = all_pages[: args.limit]
    print(f"{len(all_pages)} page(s) to sync.", file=sys.stderr)

    stats = Stats(total=len(all_pages))
    changed_urls: list[str] = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(
                process_url, url, args.timeout, manifest, args.dry_run, args.no_cache
            ): url
            for url in all_pages
        }
        done = 0
        consecutive_blocked = 0
        for fut in as_completed(futures):
            try:
                kind, info = fut.result()
            except Exception as e:
                stats.bump(errors=1)
                print(f"ERROR {futures[fut]}: {e}", file=sys.stderr)
                done += 1
                continue
            consecutive_blocked = consecutive_blocked + 1 if kind == "blocked" else 0
            if kind in {"error", "blocked"}:
                stats.bump(errors=1)
                print(f"ERROR {info}", file=sys.stderr)
                if consecutive_blocked >= MAX_CONSECUTIVE_BLOCKED:
                    print(
                        f"ERROR: {consecutive_blocked} consecutive HTTP 403s; "
                        "docs.aws.amazon.com appears to be rate-limiting this client. "
                        "Aborting; retry later, with fewer --workers.",
                        file=sys.stderr,
                    )
                    pool.shutdown(wait=True, cancel_futures=True)
                    break
            elif kind == "written":
                stats.bump(written=1)
                changed_urls.append(info)
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

    changed_paths = [url_to_local_path(url) for url in changed_urls]

    complete_full_run = (
        not args.guide_filter
        and args.max_sitemaps is None
        and args.limit is None
        and not args.all_locales
        and not args.include_sdk_references
        and discovery_errors == 0
        and stats.errors == 0
    )
    removed_paths: list[Path] = []
    if complete_full_run:
        removed_paths, stale_errors = remove_stale_pages(
            manifest,
            set(all_pages),
            args.dry_run,
            lambda url: is_english(url) and not is_sdk_reference(url),
        )
        for error in stale_errors:
            print(f"ERROR {error}", file=sys.stderr)
            stats.bump(errors=1)

    if not args.dry_run:
        manifest.flush()

    print(
        f"\nDone. total={stats.total} written={stats.written} "
        f"unchanged={stats.unchanged} cached_skip={stats.cached_skip} "
        f"errors={stats.errors} elapsed={time.time()-t0:.0f}s",
        file=sys.stderr,
    )

    if discovery_errors or stats.errors:
        print(
            f"Sync incomplete: discovery_errors={discovery_errors}, "
            f"page_errors={stats.errors}; skipping commit.",
            file=sys.stderr,
        )
        return 1

    if args.commit and not args.dry_run:
        # Only stage files this run may have updated, plus verified stale removals.
        n = git_stage_and_count(REPO_ROOT, changed_paths + removed_paths + leftover_paths)
        if n:
            msg = f"Sync AWS docs: {n} page(s) changed ({time.strftime('%Y-%m-%d')})"
            if git_commit(REPO_ROOT, msg):
                print(f"Committed: {msg}")
                if args.push and not git_push(REPO_ROOT):
                    return 1
            else:
                print("Commit failed; see errors above.", file=sys.stderr)
                return 1
        else:
            print("No changes to commit.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
