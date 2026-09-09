---
name: env-setup
description: How to reach the two in-scope AWS test sessions and tooling quirks in this environment
metadata:
  type: reference
---

Two authorized in-scope AWS sessions for hunting (both `user/research-admin`, both **AdministratorAccess**):
- Account A (attacker/self): `183174222929`, profile `default`
- Account B (victim/canary): `289531347876`, profile `awsbb2`

Setup (nothing is on PATH by default):
```
export AWS_CONFIG_FILE=/work/.aws/config
export AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials
export PATH="/work/.venv/bin:$PATH"   # aws CLI (v1) + botocore/boto3 live in this venv
export AWS_DEFAULT_REGION=us-east-1
```
Quirks:
- No `aws` or `botocore` on the system PATH; both are in `/work/.venv`.
- No `zip` binary — build Lambda zips with python `zipfile`.
- AWS CLI shorthand `--parameters k=v` cannot carry JSON values (commas break parsing); use botocore/boto3 with a dict for anything holding JSON (e.g. Athena `connection-properties`).
- Both principals are full admin → any direct test trivially succeeds. Privilege/confused-deputy findings MUST be re-run under a scoped-down assumed role modelling the real low-priv actor. See [[athena-federation-isolation]].
