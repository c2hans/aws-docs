---
name: agentcore-test-methods
description: Reusable techniques for live-testing Bedrock AgentCore — MCP SigV4 invoke, in-account collector, cross-tenant oracles
metadata:
  type: reference
---

Techniques validated on the AgentCore live run (see [[agentcore-env]]).

**MCP gateway invoke via SigV4 (confirms credential injection / tool exec):**
- Gateway URL: `https://<gwid>.gateway.bedrock-agentcore.<region>.amazonaws.com/mcp`.
- Sign POST with `botocore.auth.SigV4Auth(creds,'bedrock-agentcore',region)`; headers `Content-Type: application/json`, `Accept: application/json, text/event-stream`.
- JSON-RPC sequence: `initialize` -> `tools/list` -> `tools/call`. Tool names are `<targetName>___<operationId>`.

**In-account public HTTP collector (to observe what the service injects/sends):**
- API Gateway v2 HTTP API (`create_api` with `Target=<lambdaArn>`, ProtocolType HTTP) fronting a Lambda that does `print("COLLECTOR_HEADERS "+json.dumps(event["headers"]))`. Read via CloudWatch Logs `/aws/lambda/<fn>`. (Lambda Function URLs are SCP-blocked in these accounts.)
- Point a gateway target's openApiSchema `servers[0].url` at the collector; the gateway injects the configured credential (e.g. `x-api-key`) when the tool is called — the header value shows up in the collector log.

**Cross-tenant credential-resolution oracle (L6 shape):**
- Create apikey credential providers in both accounts; create a self-account gateway target whose `apiKeyCredentialProvider.providerArn` points at the FOREIGN account's token-vault ARN.
- Observed: control plane ACCEPTS the cross-account ARN and the target reaches READY, but at invoke the gateway returns "An internal error occurred. Please retry later." and no request reaches the backend — i.e. cross-tenant resolution is blocked at the data plane. Config-time acceptance alone is not a vuln.

**Gateway policy-engine (Cedar) enforcement oracle (L8 shape):**
- Attach engine to gateway via `UpdateGateway policyEngineConfiguration={'arn':PEARN,'mode':'ENFORCE'}`. Policies carry both `enforcementMode` (ACTIVE|LOG_ONLY) and `validationMode` (FAIL_ON_ANY_FINDINGS default | IGNORE_ALL_FINDINGS).
- A blanket `forbid(principal, action==..., resource==<gwArn>)` is flagged "Overly Restrictive" by the default validator and lands in **UPDATE_FAILED** (status reasons say it would deny every request) — it does NOT enforce, yet the API still echoes `enforcementMode=ACTIVE`. Must set `validationMode=IGNORE_ALL_FINDINGS` on CreatePolicy/UpdatePolicy to force it ACTIVE.
- Confirmed enforcement at MCP data plane: forbid ACTIVE -> `tools/call` returns JSON-RPC `error code -32002 "Tool Execution Denied ... [Policy evaluation denied due to <policyId>]"`. Demote same policy to LOG_ONLY -> `-32002 "No policy applies to the request (denied by default)"` (deny-by-default holds when >=1 policy present but none permits). So the engine enforces correctly; L8 bypass REFUTED. Operator caveat: blanket-forbid silently fails validation while enforcementMode reads ACTIVE.
- **Empty-engine fail-open REFUTED (run 2026-10-06-1b):** cleanly isolated 4 configs on one openApiSchema gateway target (tool `vh1btgt___canary`):
  (A) NO engine attached -> `tools/call` SUCCESS (pass-through; this is the only non-permit pass-through config);
  (B) ENFORCE engine with ZERO policies attached -> `tools/list` returns `[]` AND `tools/call` -> `-32002 "No policy applies to the request (denied by default)"` = FAIL-CLOSED, not fail-open;
  (C) ENFORCE engine with one ACTIVE non-permitting policy (real-gw-scoped permit + always-false `when{context has k && context.k=="never"}` condition) -> tool IS listed but `tools/call` -> same `-32002 denied by default`;
  (D) ENFORCE engine with one ACTIVE constrained PERMIT `permit(principal,action,resource==AgentCore::Gateway::"<gwArn>");` -> `tools/call` SUCCESS (proves engine genuinely evaluates; empty-engine deny is deliberate, not a broken/always-deny engine).
  So "empty attached ENFORCE engine = lockdown", NOT a footgun. Deny-by-default is the engine default whether 0 or >=1 non-permitting policies present.
- Cedar policy gotchas: wildcard resource rejected ("constrain the resource to a specific AgentCore::Gateway"); resource entity format that validates = `AgentCore::Gateway::"<full-gateway-ARN>"`; a permit referencing a NON-existent gateway ARN is rejected with `AccessDeniedException ... "Failed to confirm existence on AgentCore Gateway ... GetGateway"` (validator confirms the referenced gw exists). Engine must be `ACTIVE` before `UpdateGateway` can attach it (else ValidationException "must be in ACTIVE state"). HTTP-API quirk: path `/ping` is intercepted by a health-check layer returning "Healthy Connection" 200 — use any other path for the OpenAPI operation.

**Error-delta / IDOR oracle:** `ResourceNotFoundException` (authz passed, object absent/invisible) vs `AccessDeniedException` (authz failed) are different oracles — never collapse. Cross-account control-plane reads return NotFound = clean isolation.
