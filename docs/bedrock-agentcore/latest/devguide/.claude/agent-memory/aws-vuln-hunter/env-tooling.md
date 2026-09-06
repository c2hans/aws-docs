---
name: env-tooling
description: AWS vuln-hunt test environment — in-scope accounts, credential location, tooling quirks, and canary skills
metadata:
  type: reference
---

Live AWS vuln-hunt environment layout (verify still current before relying on it):

- **Sessions/accounts** (both authorized, in-scope): `default` profile = user/research-admin in account **183174222929** (the "self"/attacker). `awsbb2` profile = user/research-admin in account **289531347876** (the "foreign"/victim). Both are over-privileged admins — always re-frame findings against the *intended* scoped principal.
- **Credentials** live at `/work/.aws/credentials` + `/work/.aws/config`. Export `AWS_SHARED_CREDENTIALS_FILE` and `AWS_CONFIG_FILE` to point at them. Default region us-east-1.
- **`aws` CLI is NOT on PATH** and system python has no botocore. Use **`/work/.venv/bin/python`** (boto3/botocore 1.43.73 installed there) as the primary interface. There is an `aws` binary at `/work/.venv/bin/aws` if needed.
- **Canary/callback skills** via `$PROXY_GATEWAY` (e.g. http://host.docker.internal:1337): `github-page-hosting` publishes to **c2hans/c2hans.github.io** (public URL `https://c2hans.github.io/<path>`); `cloudflare-dns-gateway` manages zone **m1tz.de** (create unproxied A records for SSRF/DNS-rebind, e.g. point a hostname at 169.254.169.254). Sandbox has direct outbound egress to the public internet (can curl github.io). Neither skill gives inbound request logs, so SSRF is observed via **server-side status/error oracles**, not captured headers.
- See [[agent-registry-findings]] for service-specific results.
