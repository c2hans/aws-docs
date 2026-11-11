---
name: aws-test-environment
description: Operational setup for the two authorized AWS test accounts (creds location, no CLI, boto3 usage, trail limits)
metadata:
  type: project
---

Two authorized in-scope AWS test accounts, both `user/research-admin` (AdministratorAccess — deliberately over-privileged testers): **A = 183174222929** (profile `default`), **B = 289531347876** (profile `awsbb2`). Default region us-east-1.

**Why:** these are the only in-scope sessions for every sweep; cross-account/tenant tests use B as the "foreign" side. Account `532876697804` is an out-of-scope IdC/management account (an org CloudTrail in A logs to it) — never touch it.

**How to apply:**
- No `aws` CLI binary is installed; use **boto3/botocore** (installed). Credentials live at `/work/.aws/credentials` + `/work/.aws/config` — export `AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials` and `AWS_CONFIG_FILE=/work/.aws/config`, or pass `profile_name=` to `boto3.Session`.
- Run throwaway Python with `python3 -I` heredocs from a scratch dir under `/work/analysis-*/`. `/work/aws-docs` is read-only (offline docs mirror).
- Account A sits at the **5-trail-per-region CloudTrail limit** (prior-run canary trails + 1 org trail) — you usually cannot create a new trail in us-east-1; confirm CloudTrail authorization non-destructively via a resource-existence oracle (AccessDenied vs TrailNotFoundException) instead.
- Many `vh-*` roles/buckets and `vh-run-id`-tagged resources are residue from prior/parallel hunts (the run-id is date-based `YYYY-MM-DD-N` and collides across concurrent runs). Verify your own teardown by **resource name**, not tag alone.
