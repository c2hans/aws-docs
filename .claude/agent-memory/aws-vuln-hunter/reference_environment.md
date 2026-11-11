---
name: reference-environment
description: AWS test-session credential location and account A/B mapping for the two in-scope sessions
metadata:
  type: reference
---

The AWS CLI binary is NOT on PATH in this environment; use boto3 directly. Credentials live at `/work/.aws/credentials` (not `~/.aws`). Point boto3 at them with `AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials` and `AWS_CONFIG_FILE=/work/.aws/config`.

Profiles and account mapping (both resolve to `user/research-admin`, over-privileged test users):
- profile `default` = account A `183174222929` (key `AKIASVJQI2RIXUUEC2GA`) — "self" tenant
- profile `awsbb2` = account B `289531347876` (key `AKIAUG2LJYOSLX563BEN`) — "foreign" tenant

Default region us-east-1. Run untrusted-dir Python with `-I`.
