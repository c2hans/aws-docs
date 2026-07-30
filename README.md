# aws-docs

An offline, diffable Markdown mirror of [docs.aws.amazon.com](https://docs.aws.amazon.com),
synced by [`scripts/sync_aws_docs.py`](scripts/sync_aws_docs.py). The point of this repo is
to turn AWS's documentation into `git log` / `git diff` history, so product and doc changes
show up as normal commits.

## Layout

```
docs/<guide-path>.md   -- mirrors the URL path, e.g.
                          https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
                          -> docs/AWSEC2/latest/UserGuide/concepts.md
scripts/sync_aws_docs.py
.cache/manifest.json   -- gitignored; per-URL ETag/Last-Modified/hash cache
```

Each file starts with a small front-matter block recording its source URL:

```
---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
---
```

## How a page is fetched

1. Try AWS's native Markdown export at `<path>.md` (AWS serves nearly every doc page
   this way now, `Content-Type: text/markdown`). Used as-is.
2. If that isn't available, fetch `<path>.html`, extract the `#main-col-body` content
   region (BeautifulSoup), strip `<script>`/`<style>`/`awsdocs-*` custom elements (these
   are empty client-side widgets in the static HTML — banners, feedback buttons, TOC),
   absolutize relative links/images, and convert to Markdown via `markdownify` with fixed
   settings (ATX headings, `-` bullets, no autolinks, no wrapping).
3. Both paths are run through the same `normalize_markdown()`: LF line endings, no
   trailing whitespace, no runs of 3+ blank lines, exactly one trailing newline.

In practice essentially every page currently uses path 1. Path 2 exists as a fallback so
the script doesn't error out if AWS stops serving `.md` for some corner of the site.

## Determinism / idempotency

- Conversion is a pure function of the fetched bytes: same input -> byte-identical output.
- A run only *writes* a file if its content actually differs from what's on disk, and
  file writes are atomic (write to `*.tmp`, then rename).
- A local cache (`.cache/manifest.json`, gitignored) records each URL's ETag/Last-Modified
  and the sha256 of the content last written. Re-runs send conditional GETs; AWS's `304`
  responses are cheap and skip reconversion entirely.
- Before trusting the cache for a URL, the script checks the local file still exists *and*
  its hash still matches what the manifest recorded — if a file was deleted or corrupted
  (e.g. a previous run got killed mid-write) the cache is ignored and the page is fully
  refetched, which self-heals the mirror.
- Net effect: running the script twice back-to-back with no upstream changes produces an
  empty `git status`. Running it after AWS changes a page produces a normal, readable diff
  on exactly that file.
- Commit messages are derived from `git diff --cached --name-only -- docs` (the actual
  staged file count), not from in-run counters, so they stay accurate even on a resumed
  or repaired run. If nothing changed, no commit is made (no empty commits).

## Scope

AWS publishes a sitemap index (`https://docs.aws.amazon.com/sitemap_index.xml`) listing
~10,900 per-guide sitemaps. About 71% of those are translated locales (`ja_jp`, `zh_cn`,
`ko_kr`, `es_es`, `pt_br`, `fr_fr`, `zh_tw`, `de_de`, `it_it`, `id_id`, `ar`). By default
this script only syncs the English/default guides (~3,150 of them, an estimated ~84,000
pages). Pass `--all-locales` to include translations too (roughly 3.5x the volume).

## Usage

```bash
pip install -r requirements.txt

# Full sync (English guides), commits changes, does not push:
python3 scripts/sync_aws_docs.py

# Useful flags:
python3 scripts/sync_aws_docs.py --guide-filter 'AWSEC2/latest/UserGuide'  # one guide
python3 scripts/sync_aws_docs.py --max-sitemaps 20                        # first N guides
python3 scripts/sync_aws_docs.py --limit 50                               # first N pages
python3 scripts/sync_aws_docs.py --dry-run                                # fetch/convert only
python3 scripts/sync_aws_docs.py --no-cache                               # ignore manifest cache
python3 scripts/sync_aws_docs.py --workers 24                             # concurrency
python3 scripts/sync_aws_docs.py --no-commit                              # leave changes unstaged
python3 scripts/sync_aws_docs.py --push                                   # also push to origin
```

Re-run it any time (e.g. from cron/CI) to pick up AWS's changes as new commits.

## Pushing to GitHub over SSH

This sandbox currently has no SSH client, no SSH key, and no `origin` remote configured,
so `--push` is a no-op until that's set up. To wire it up:

```bash
# 1. Install an SSH client (if not already present) and generate a deploy key:
sudo apt-get install -y openssh-client
ssh-keygen -t ed25519 -C "aws-docs-sync" -f ~/.ssh/aws_docs_ed25519 -N ""

# 2. Add ~/.ssh/aws_docs_ed25519.pub as a Deploy Key (with write access) on the
#    aws-docs GitHub repo, or as a key on the account that owns it.

# 3. Make sure github.com's host key is trusted and the deploy key is used:
mkdir -p ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts
cat >> ~/.ssh/config <<'EOF'
Host github.com
  IdentityFile ~/.ssh/aws_docs_ed25519
  IdentitiesOnly yes
EOF

# 4. Point this repo's origin at the GitHub repo and push:
git remote add origin git@github.com:<owner>/aws-docs.git
git push -u origin HEAD
```

Once `origin` exists, `--push` (or a scheduled run with `--push`) will push new commits
after each sync.
