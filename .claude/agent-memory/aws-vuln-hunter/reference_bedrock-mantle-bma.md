---
name: bedrock-mantle-bma
description: BMA / bedrock-mantle (OpenAI-on-Bedrock managed agents) live-test facts — SigV4 technique, preview-gate, inference/bearer IAM enforcement
metadata:
  type: reference
---

Bedrock Managed Agents (BMA) / service `bedrock-mantle`, OpenAI-on-Bedrock. Observed 2026-10-06 (run 20261006-bma). See [[agentcore-env]] for accounts/tooling.

**SDK gap + SigV4 technique:** boto3/botocore 1.43.108 has NO `bedrock-mantle` service model. Hit it with raw HTTPS signed by `botocore.auth.SigV4Auth(creds,'bedrock-mantle','us-east-1')` against `https://bedrock-mantle.<region>.api.aws`. Helper pattern lives in /work/findings/bma_sig.py when a run is active. RequestIds are `req_...` (not x-amzn-RequestId header on the OpenAI-compat routes — read from response).

**Preview gate (CRITICAL precondition):** the agent-session surface `/openai/v1/agents/sessions*` returns **401 "Bedrock Managed Agents is not available for this account."** in BOTH in-scope accounts, ALL THREE regions (us-east-1/2, us-west-2). It is an allow-listed preview neither account holds. So L1 (session IDOR headline), L2 (PassRole), L3 (injection->exec), L4 (env attach), L5 (AgentCore invoke) are all BLOCKED on precondition — not testable until an account is enabled. Re-check this 401 first on any future BMA sweep; don't rebuild the whole rig until it clears.
**Why:** these are the only in-scope sandbox accounts and BMA isn't provisioned in them.
**How to apply:** if the 401 persists, report L1-L5 blocked and spend budget only on the reachable inference plane.

**Reachable surface = inference only:** `GET /v1/models` 200 (first-party catalog: anthropic.claude-*, openai.gpt-oss-20b, openai.gpt-oss-safeguard-120b, qwen.*, mistral.*, deepseek.*, zai.*, nvidia.*; `openai.gpt-6.1-sol` from the model card is NOT present). Inference routes: `/openai/v1/chat/completions`, `/openai/v1/responses`. gpt-oss-20b isn't supported on either route (400 validation) but that 400 comes AFTER authz — perfect for authz-only oracles without burning tokens. Control plane (projects/reservations/data-retention) is 404 on this host — different endpoint/protocol, not in SDK -> L7/L8/L9 blocked.

**L10 Model-condition — REFUTED/clean:** IAM `bedrock-mantle:CreateInference` + StringEquals `bedrock-mantle:Model` is enforced server-side, CASE/alias/geo-prefix SENSITIVE, fail-closed. Exact match -> 400 (authz pass); uppercase, `us.`-prefix, other model -> 403. 403 names customer resource `arn:aws:bedrock-mantle:<region>:<acct>:project/default` (not service plane).

**L6 Bearer token — REFUTED (no bypass) + doc-gap:** Bedrock long-term API key = IAM service-specific credential ServiceName `bedrock.amazonaws.com` (secret in `ServiceCredentialSecret`, ~136 chars, prefix `ABSK...`). Used as `Authorization: Bearer <key>`. It resolves to the CREATING IAM principal and is FULLY IAM-evaluated: respects that user's Model condition (qwen->403 CreateInference denied via bearer) AND requires a second grant `bedrock-mantle:CallWithBearerToken`. No scope bypass. Bearer is a CUSTOMER credential (denials name customer ARNs) — not a HARD STOP.
  - `bedrock-mantle:BearerTokenType` enforced value is **`LONG_TERM`** (and `SHORT_TERM`) — NOT the doc prose "Long-term". StringEquals is case-sensitive, so a Deny written "long-term"/"Long-term" is silently FAIL-OPEN; only `LONG_TERM` binds. Docs (list_bedrock-mantle.md) give prose only, no value, no example. Classify as doc-gap/operator-footgun, not an AWS service vuln (key populates & binds with the correct value).

**Teardown note:** everything was IAM in [default] (user+inline policy+access key+service-specific cred). awsbb2 was read-only. Delete service-specific cred and access key BEFORE the user. Verify get_user->NoSuchEntity + tag sweep list_user_tags for vh-run-id.
