---
name: env-setup
description: How to reach AWS CLI/botocore and the two in-scope AWS sessions in this container (paths, account IDs, region)
metadata:
  type: reference
---

AWS tooling is NOT on the default PATH. To use it:

```bash
export PATH="/work/.venv/bin:$PATH"          # aws-cli 1.46, botocore 1.43.62, python3.12
export AWS_CONFIG_FILE=/work/.aws/config
export AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials
```

Profiles / in-scope accounts (both `user/research-admin`, region us-east-1):
- `default`  = Account A (attacker/self)  = **183174222929**, key AKIASVJQI2RIXUUEC2GA
- `awsbb2`   = Account B (victim/canary)  = **289531347876**, key AKIAUG2LJYOSLX563BEN
- (`root` / `awsbb2-root` profiles also exist in config.)

`PROXY_GATEWAY=http://host.docker.internal:1337` is available for custom skills.
Only these two accounts are in scope — any other account ID is out of scope (rule 1).
