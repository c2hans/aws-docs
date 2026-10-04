---
name: aws-env-setup
description: How to reach the authorized AWS test env (venv, CLI, creds, two in-scope sessions) — no AWS tooling is on the default PATH
metadata:
  type: reference
---

The AWS tooling is NOT on the default PATH. To operate:

- Python + botocore/boto3: `/work/.venv/bin/python` (botocore 1.43.73). AWS CLI: `/work/.venv/bin/aws`.
- Export before any call: `AWS_CONFIG_FILE=/work/.aws/config` and `AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials`.
- Two in-scope sessions (profiles), both `user/research-admin`, region us-east-1:
  - profile `default` = account **183174222929** ("self"/A)
  - profile `awsbb2`  = account **289531347876** ("foreign"/B)
- `$PROXY_GATEWAY=http://host.docker.internal:1337` is set (enables github-page-hosting / cloudflare-dns-gateway skills). Sandbox egress to the public internet works directly (curl reaches AWS endpoints).
- Useful pattern: a boto3 helper with `Config(retries={'max_attempts':0})` that prints operation/status/error-code/RequestId/timestamp per call. See [[agent-registry-service-facts]].
