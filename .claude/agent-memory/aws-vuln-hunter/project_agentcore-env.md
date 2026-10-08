---
name: agentcore-env
description: In-scope accounts, tooling quirks, and Bedrock AgentCore service/resource facts observed during live runs
metadata:
  type: project
---

Amazon Bedrock AgentCore live-test environment (observed 2026-10-06).

**Accounts (both `user/research-admin`, both AdministratorAccess):**
- `[default]` 183174222929 — self / attacker tenant
- `[awsbb2]` 289531347876 — foreign / victim tenant

Both users are over-privileged (AdministratorAccess), so every privilege-dependent result must be re-run under a scoped-down principal before being called a finding.

**Why:** these are the fixed in-scope sandbox accounts; any other account ID is out of scope.
**How to apply:** use `[default]` as attacker, `[awsbb2]` as the cross-tenant victim. Never touch a third account.

**Tooling quirks:**
- No `aws` CLI installed; no boto3 preinstalled. Install boto3 with `pip3 install --break-system-packages boto3` (PEP668 blocks plain pip).
- Creds at `/work/.aws/{credentials,config}`; use `AWS_SHARED_CREDENTIALS_FILE`+`AWS_CONFIG_FILE` env vars with `boto3.Session(profile_name=...)`.
- botocore 1.43.x already knows the full AgentCore surface: services `bedrock-agentcore`, `bedrock-agentcore-control`, `agent-registry`, `agent-registry-control`.
- Account **blocks public Lambda Function URLs** (AuthType NONE returns Forbidden even with correct public resource policy) — use an API Gateway v2 HTTP API as a public in-account HTTP collector instead.

**AgentCore facts observed:**
- Control-plane tenant isolation is clean: cross-account `Get*/Update*` on another account's resource id returns `ResourceNotFoundException` (identical to a bogus id in your own account) — no existence leak, no cross-account mutation.
- Cheapest resources to stand up (no container/role): `CreatePolicyEngine` (name regex `^[A-Za-z][A-Za-z0-9_]*$`), `CreateApiKeyCredentialProvider`, `CreateMemory`.
- `CreateAgentRuntime` requires an ECR container image (heavy standup). **CreateHarness does NOT** — a bare `create_harness(harnessName, executionRoleArn)` with a service-trusting role reaches READY in ~105s with a default Bedrock model + managed memory (cheapest AgentCore compute; see [[agentcore-harness]]).
- Gateway (`CreateGateway`, authorizerType AWS_IAM) + `CreateGatewayTarget` (openApiSchema needs HTTPS `servers` URL) is a cheaper invoke-path substrate; gateway MCP endpoint is SigV4-signable with service name `bedrock-agentcore`.
- api-key / oauth credential providers store secret in service-managed Secrets Manager (`bedrock-agentcore-identity!default/apikey/...`) — do NOT read that secret material (service plane). Provide synthetic canary values on create instead.
