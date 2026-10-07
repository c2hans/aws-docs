---
name: env-sessions
description: In-scope AWS accounts, credential setup, and session profiles for the vuln-hunter test environment
metadata:
  type: reference
---

Two in-scope test accounts, both principal `user/research-admin` with `AdministratorAccess`:
- `[default]` profile = account **183174222929** (self / attacker session)
- `[awsbb2]` profile = account **289531347876** (foreign tenant / victim session)

Setup facts:
- Credentials at `/work/.aws/credentials` + `/work/.aws/config`. Export `AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials` and `AWS_CONFIG_FILE=/work/.aws/config` before boto3 calls.
- **No `aws` CLI installed** — use boto3 (botocore 1.43.108) exclusively.
- Default region us-east-1.
- Because research-admin is AdministratorAccess (deliberately over-privileged), any control-plane finding must be re-judged against the real actor (end-user vs pool-admin). The scoped run is the finding.

**Why:** avoids re-discovering the harness each run.
**How to apply:** reuse this setup for any future AWS hunt; confirm both accounts with sts:GetCallerIdentity before mutating.
