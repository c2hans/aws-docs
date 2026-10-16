---
name: agentcore-authz
description: bedrock-agentcore authorization is consistently well-enforced in the test account — leads that reliably refute, with the discriminating tests
metadata:
  type: project
---

In account A (183174222929), bedrock-agentcore's authz held up under scoped-role testing on every surface probed in run 2026-10-15-1.

**Why:** avoids re-litigating refuted AgentCore leads; points future runs at the discriminating experiment instead.

**How to apply:** treat these as refuted unless a doc change reopens them; reuse the test shapes.

- `GetWorkloadAccessTokenForUserId` (lead #5): the `bedrock-agentcore:userid` condition key IS enforced. Scoped role pinned to `userid=alice` → allow alice, deny bob (AccessDeniedException). Cross-user needs an unscoped grant = customer footgun.
- Memory namespace isolation (`ListMemoryRecords`/`RetrieveMemoryRecords`/`GetMemoryRecord`): defense in depth. The `bedrock-agentcore:namespace` key IS emitted by `GetMemoryRecord` despite the service-authorization doc omitting it (doc bug, not authz gap). A role scoped to `/users/alice/*` cannot read another actor's record by: omitting namespace (IAM deny), claiming the victim namespace (IAM deny), or spoofing own namespace with the victim record id (service returns 404 — independent record↔namespace membership check).
- Cross-account MCP gateway invoke: account B SigV4 to account A's gateway `/mcp` URL → HTTP 403 AccessDeniedException (MCP -32002). Account-isolated.
- Workload access tokens are account-bound: account B replaying account A's `workloadAccessToken` → 403 "Invalid workload access token". So payment/OAuth provider leads (#8) can't cross accounts by token replay; provider names resolve account-locally.
- Legacy `bedrock-agentcore:...Registry...` control actions (CreateRegistry/ListRegistries/GetRegistry/ListRegistryRecords) are DENIED even under AdministratorAccess (SCP/service gate). The `agent-registry` discoverable namespace IS authorized but needs a 12-16 char registryId (not obtainable via a listable API here). Self-approval supply-chain path (#17) blocked.
- `billing` model lacks `TransferCredit`/`SplitCredit` entirely (#21 refuted at surface). `lambda-web` exposes only `GetWebAccountSettings` — Web Functions CRUD/endpoint/resource-policy surface (#12/#13) absent from reachable API.

See [[test-environment]].
