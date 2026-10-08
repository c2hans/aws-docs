---
name: agentcore-harness
description: Bedrock AgentCore Harness family (CreateHarness/InvokeHarness/hooks/token-vault) live-test facts — all A1/A2/A3 REFUTED, cheap standup recipe, teardown cascade
metadata:
  type: reference
---

Bedrock AgentCore **Harness** family, live-tested run 2026-10-08-1 (see [[agentcore-env]], [[agentcore-test-methods]]). All hypotheses REFUTED; the family is well-guarded.

**Served & cheap (contradicts the old agent-sessions 401 preview-gate note):**
- `bedrock-agentcore-control` has full Harness surface in botocore 1.43.109: CreateHarness/Update/Get/Delete/+Endpoint, ListHarnesses/Versions. Data plane `bedrock-agentcore` has `InvokeHarness`. All **served, NOT preview-gated** in both accounts.
- **No ECR image needed** — bare `create_harness(harnessName, executionRoleArn)` reaches READY in ~105s with a default Bedrock model (`global.anthropic.claude-sonnet-4-6`, converse_stream) + managed memory + networkMode PUBLIC. Cheapest AgentCore compute to stand up.
- ExecutionRole must EXIST and its trust must allow `bedrock-agentcore.amazonaws.com` (else ValidationException "Role validation failed... verify the role exists and its trust policy allows assumption by this service").
- `InvokeHarness` requires `runtimeSessionId` (regex `[a-zA-Z0-9][a-zA-Z0-9-_]*`, **len 33-100**) + `messages=[{role,content:[{text}]}]`; returns `{stream}` EventStream (hookEvent/messageStart/contentBlockDelta/...). The agent loop runs AS the customer exec role: `assumed-role/<execrole>/BedrockAgentCore-<uuid>`.

**A1 — cross-account hook confused deputy: REFUTED.** Hooks (`hooks[].{beforeInvocation,afterInvocation,beforeToolCall,afterToolCall}.target.{lambda,sns,eventBridge}.arn`) accept arbitrary-account ARNs at config time (cosmetic). But the target is invoked **under the customer executionRole**, double-sided xacct auth: delivery into B needs BOTH (A-side) exec role holding `lambda:InvokeFunction` AND (B-side) target resource policy allowing that role ARN. Oracle used: B Lambda policy allowing ONLY `bedrock-agentcore.amazonaws.com` service principal (no condition) → NO delivery (log group never created) + hookEvent `reason:"Hook target invocation failed"`; allow exec-role + grant it invoke → delivery + `VH_HOOK_INVOKED` log; remove exec-role's own `lambda:InvokeFunction` → fails again (dispositive = role-based, not service-principal). No fleet identity, no un-settable SourceAccount. Hook event payload carries the full agent conversation (messages, trace headers) to the target — but single-owner harness, so no cross-tenant leak.

**A2 — token-vault cross-account secret resolution: REFUTED (config-time positive ownership check).** `HarnessSkillGitAuth.credentialArn` AND model `openAiModelConfig/geminiModelConfig/liteLlmModelConfig.apiKeyArn` all reject a foreign-account `token-vault/.../apikeycredentialprovider/...` ARN with **ValidationException "ARN account mismatch: '<arn>' belongs to account '<B>' but caller is in account '<A>'"**. Check is account-match NOT existence (a self-account non-existent provider ARN is accepted at create). Stronger than the gateway L6 shape (which accepted at config, blocked at data plane). `skills` is a **tagged union** — set exactly one of path/s3/git/awsSkills.

**A3 — PassRole: REFUTED (enforced).** CreateHarness does the `iam:PassRole` caller-authz check: scoped role (Allow CreateHarness, explicit Deny iam:PassRole) → AccessDeniedException "not authorized to perform: iam:PassRole ... explicit deny". Cross-account ExecutionRole (RoleArn pattern `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` has optional acct segment) → AccessDeniedException **"Cross-account pass role is not allowed."** Simulator quirk: `iam:SimulatePrincipalPolicy` reports `bedrock-agentcore:CreateHarness` as implicitDeny even for admin (simulator doesn't model the new action; live calls still succeed).

**Tenant isolation (clean):** cross-acct `GetHarness` → ResourceNotFoundException 404 (no existence leak); cross-acct `InvokeHarness` → AccessDeniedException 403 (resource-authz, victim granted nothing). No-authorizerConfiguration default = SigV4/IAM invoke, NOT anonymous fail-open. Full `customJWTAuthorizer` fail-open (alg:none/foreign aud) NOT tested — needs a hosted OIDC discoveryUrl; deferred.

**Teardown gotchas:** DeleteHarness cascades the managed memory — you CANNOT delete the memory directly ("Memory is managed automatically"); it disappears when the harness finishes DELETING. Harness deletion is SLOW (invoked ones ~5min; it tears down an agent runtime). A harness still CREATING can't be deleted (ConflictException) — wait for READY first. apikey credential provider delete also removes its managed secret `bedrock-agentcore-identity!default/apikey/...`.

**Deliberate non-test (rule 4 hard stop):** Harness microVM has shell+egress and `apiBase` is a free-form URL the runtime calls. Pointing apiBase at `169.254.169.254` to grab fleet IMDS creds = attack on AWS's multi-tenant fleet. NOT done; flag only for an authorized AWS-internal review.
</content>
