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

1. Fetch AWS's native Markdown export at `<path>.md` (`Content-Type: text/markdown`).
   Used as-is.
2. Run it through `normalize_markdown()`: LF line endings, no trailing whitespace, no
   runs of 3+ blank lines, exactly one trailing newline.

Every public `docs.aws.amazon.com` page serves a `.md` export — verified across a random
sample spanning all guide trees, including the SDK/CLI/CDK/PowerShell reference trees
excluded by default (see Scope below). The lone counterexample found wasn't real AWS
content: a meta-refresh redirect stub (in `embedded-csdk`'s doxygen-generated tree)
pointing off-site to `aws.github.io`, empty even as HTML. There's no HTML-scraping
fallback; a page whose `.md` isn't a 200 is logged as an error and skipped, not
downgraded to a scraped conversion.

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
~10,900 per-guide sitemaps. Two filters are applied by default:

1. **Locale.** About 71% of guides are translated (`ja_jp`, `zh_cn`, `ko_kr`, `es_es`,
   `pt_br`, `fr_fr`, `zh_tw`, `de_de`, `it_it`, `id_id`, `ar`). Only the English/default
   guides (~3,150) are synced. Pass `--all-locales` to include translations too.
2. **SDK/CLI/CDK/PowerShell references.** A handful of trees are one page per
   class/method/command, mechanically generated from SDK source code on every release
   (`sdkfornet` .NET API docs, `AWSJavaSDK` javadoc, `sdk-for-ruby/*/api`, `aws-sdk-php`,
   `AWSJavaScriptSDK`, `cdk/api`, `powershell/*/reference`, `cli/*`). Together these are
   **~910,000 of the ~1.09M English pages (84%)** — their diffs mostly reflect SDK codegen,
   not product changes, so they're excluded by default (see `SDK_REFERENCE_PATTERNS` in
   the script). Hand-written SDK developer/user guides (e.g. `sdk-for-java/*/developer-guide`,
   `powershell/*/userguide`) are prose, not generated references, and are always synced.
   Pass `--include-sdk-references` to include the excluded trees too.

The index also keeps entries for guides AWS has retired or merged elsewhere: their
`sitemap.xml` redirects off-site, to an HTML landing page, or to a 404, or is an empty
`<urlset>` (~140 of them, e.g. old `powertools/*` versions and many `whitepapers/*`).
These are logged as `WARN: skipping retired guide` and skipped. Any other discovery
failure (timeouts, 5xx, malformed XML at the sitemap's own URL) still aborts the run
before anything is written, so stale-page cleanup never acts on a partial page list.

With both default filters, the sync covers **~3,127 guides / ~172,000 pages**: user guides,
developer guides, each product's own API reference (EC2, S3, Bedrock, SageMaker, etc.),
whitepapers, prescriptive guidance, and release notes.

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
python3 scripts/sync_aws_docs.py --include-sdk-references                 # also sync SDK/CLI/CDK/PowerShell refs
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
