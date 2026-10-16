---
name: test-environment
description: The two in-scope AWS test accounts, how creds are wired, the pre-staged scenario, and stale prior-run artifacts to distrust
metadata:
  type: project
---

The authorized hunt environment (docs-diff exercise driven by `/work/research-plans/`).

**Why:** this is a seeded red-team exercise against a live-but-synthetic AWS environment with custom botocore service models; knowing the fixtures avoids re-deriving them each run.

**How to apply:** use these as starting facts, but always re-verify live state (prior runs mutate/tear down fixtures).

- Creds: `source /work/vh-scripts/env.sh` → PATH=/work/.venv-aws/bin, AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials, AWS_CONFIG_FILE=/work/.aws/config, region us-east-1. No `aws`/botocore on the default PATH.
- Two in-scope sessions, both `user/research-admin` with AdministratorAccess (deliberately over-privileged → every cross-boundary claim must be re-proven under a scoped role):
  - profile `default` = account A **183174222929**
  - profile `awsbb2` = account B **289531347876**
- Custom botocore (436 svcs) includes seeded/new models: bedrock-agentcore(+control), agent-registry(+control), securityagent, network-security-manager, lambda-web. Endpoints are LIVE and respond. `iam:SimulatePrincipalPolicy` does NOT validate action names (admin matches `*`) — it is not an existence oracle; use real calls.
- Pre-staged scenario in account A: a "manufacturing / mfg-ukg" tenant — Cognito pool `mfg-ukg-users`, AgentCore MCP gateway `mfg-ukg-registry-gateway` (AWS_IAM, Lambda target over a DynamoDB "system registry"), agent runtimes `mfg_ukg_discovery`/`mfg_ukg_explorer`, memories `mfg_ukg_memory`/`mfg_ukg_discovery_memory`, many `registry-*` workload identities. Account B starts empty.
- `/work/.aws/_vh_ids.json` is STALE prior-run state (Cognito pools, agentcore canaries) — mostly torn down; do not trust it as live. Expect prior-run residue (e.g. a leftover `pocF13Probe2` gateway with authorizerType=NONE + PASSTHROUGH targets `rfc5737`/`k8s*`, role `vh-f13-probe-exec`) that this run did not create — flag as residual, don't claim as own.
- Tag every created resource `vh-run-id=<today>-N`; keep a teardown ledger (I use `/work/vh-scripts/ledger.jsonl`) and a reusable harness `/work/vh-scripts/vh.py` (vh.call/vh.pr, retries pinned 0). See [[agentcore-authz]].
