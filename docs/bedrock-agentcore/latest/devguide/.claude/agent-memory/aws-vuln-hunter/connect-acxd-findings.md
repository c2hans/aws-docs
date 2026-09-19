---
name: connect-acxd-findings
description: Connect ACXD (Agentic CX Designer) front door is LIVE and fully characterized; first acxd_live_ key is strictly console-gated with no IAM path. Phase 1 isolation/privesc BLOCKED pending a supplied key. (run vh-acxd-20260917, 2026-09-17)
metadata:
  type: project
---

Run `vh-acxd-20260917` (2026-09-17), accounts A=183174222929 (default/attacker), B=289531347876 (awsbb2/victim). Executed `/work/aws-docs/Connect-ACXD-Bootstrap-and-Hunt-plan.md`. **Corrects the prior "surface-unconfirmed / NXDOMAIN everywhere" dead end (see [[acxd-sagemaker-hyperpod-facts]]) — that was a WRONG-HOSTNAME false negative.**

## DECISIVE OUTCOME: front door LIVE, first key console-gated => Phase 1 BLOCKED (honest stop, not fabricated)

### The real ACXD front door (extracted from npm pkg `amazon-connect-acxd-sdk@0.1.0`, published, Smithy-generated)
- **Endpoint template:** `https://api.acxd.connect.{Region}.amazonaws.com` (in runtimeConfig/endpointResolver). Prior hunts guessed `acxd.*`, `api.acxd.<region>`, `acxd.connect.<region>` — all NXDOMAIN; the real form inserts BOTH `api.acxd.connect`. This is why prior runs concluded NXDOMAIN.
- **RESOLVES LIVE** (checked via socket + curl): us-east-1 (44.207.238.61), us-west-2, eu-central-1, ap-southeast-1, ap-northeast-1, ap-southeast-2, ca-central-1. NXDOMAIN in eu-west-1. Fronted by **API Gateway** (`x-amz-apigw-id` on every response).
- **Auth:** `smithy.api#httpApiKeyAuth`, header **`x-api-key`** = `acxd_live_<20charPrefix>.<secret>`. `HttpApiKeyAuthSigner` (no SigV4). apiVersion `2025-01-01`, protocol AwsRestJson, `defaultSigningName=agenticcxdesignerservice`, serviceTarget `AgenticCXDesignerService`, namespace `com.amazon.connect.acxd.sdk`.
- **workspaceId transport:** header **`x-workspace-id`** (added by SDK `addWorkspaceHeader` build step). Workspace-scoped ops send it; account-level ops (workspaces, programmatic-users) omit it.
- **TLS:** cert SAN = ONLY `api.acxd.connect.us-east-1.amazonaws.com`, issuer Amazon RSA 2048 M04 (public ACM). **No internal-hostname leakage.**

### REST path map (from SDK schemas_0.js) — ready for Phase 1 once a key exists
`GET/POST /sdk/secrets`, `GET/PUT/DELETE /sdk/secrets/{secretIdentifier}`; `GET/POST /sdk/programmatic-users`, `/sdk/programmatic-users/{userId}`, `POST /sdk/programmatic-users/{userId}/api-tokens`, `.../api-tokens/{keyPrefix}`; `/sdk/workspaces` (account-level); `/sdk/data-requests`, `/sdk/context-variables`, `/sdk/conversations`, `/sdk/knowledge-bases/...`, `/sdk/roles`, `/sdk/guardrails`, `/sdk/trails/query`, `/sdk/logs/query`, `/sdk/team`, `/sdk/users`.

### Unauthenticated / bogus-key probe results (all us-east-1, 2026-09-17 ~13:33Z)
- `GET /` no auth => **403 `MissingAuthenticationTokenException`** (API GW default, unknown route).
- `GET /sdk/secrets` no key => **401 `UnauthorizedException`**, body `{"message":"Unauthorized"}` (26 bytes). req 60d627ef-...
- `GET /sdk/secrets` bogus well-formed key + bogus `x-workspace-id` => **identical 401**, 26-byte body. req 8d07b922-...
- `GET /sdk/workspaces` bogus key => identical 401. `GET /sdk/programmatic-users` bogus key => identical 401.
- **=> Auth is fail-closed at a custom authorizer.** No echo of workspaceId/Authorization; NO 401-vs-403-vs-404 discriminator between bad-prefix / bad-secret / unknown-workspace. **No enumeration oracle.** `acxd_live_` prefix keyspace base62^20 ~ 10^35 and the secret is separate => non-guessable, confirmed an identifier not a guess target.

### Bootstrap gate = CONSOLE ONLY, no IAM/SigV4 path (confirmed both from docs and live)
- `connect list-instances` EMPTY in A and B (200). Doc `enable-nextgeneration-amazonconnect.md`: **"All new instances are Connect Customer instances"** (ACXD-capable by default); pre-existing instances enable via console `Connect Customer > Enable` (no API).
- **Attempted `connect:CreateInstance`** (CONNECT_MANAGED, calls disabled, alias `vh-acxd-20260917-canary`, tagged): 200, instance `53a2fc7a-0b1b-47a6-810a-b5cc019879f6`, became ACTIVE. Attributes CONTACT_LENS/MPC/ENHANCED_MONITORING=true. **Deleted + verified** (ResourceNotFound on re-describe, list empty).
- The connect (SigV4) model has **NO** acxd token/apikey/programmatic-user op — only `GetFederationToken` (classic agent-app SSO session, NOT an acxd_live_ minter). The connect-model `CreateWorkspace/AssociateWorkspace/...` ops are the classic **Agent-Workspace UI** feature (views->pages->users/routing-profiles), NOT ACXD workspaces — different product, still need an InstanceId.
- The only key-minting op (`CreateApiToken` = `POST /sdk/programmatic-users/{userId}/api-tokens`) lives on the ACXD endpoint and itself needs an existing `acxd_live_` key (returns 401 without). **Bootstrap is circular from IAM creds.** Docs `acxd-getting-started.md`: first programmatic user + first key are minted ONLY via Admin Hub console ("Create Programmatic User" -> "Generate API Key", shown once, max 2 keys/user).

### EXACT UNBLOCK RECIPE (hand this to a hunter to run Phase 1 unattended)
In an ACXD-enabled Connect Customer instance's **Admin Hub > Programmatic Users**: (1) Create a programmatic user with `roleConfig.accountRole=administrator`; Generate API Key -> copy `acxd_live_...`. (2) Create TWO workspaces (or note two workspace UUIDs) in that account, AND repeat in account B for cross-account tests. (3) Also mint a NON-admin (developer/read-only or workspace-scoped) key for the A2 privesc test. Hand hunter: admin key + non-admin key + >=2 workspace UUIDs (+ B-account key/UUID for cross-account). Then A1/A2/A3/A6 are standalone-testable against `https://api.acxd.connect.us-east-1.amazonaws.com` with headers `x-api-key`, `x-workspace-id`.
- **A1 cross-workspace IDOR:** workspace-A key, set `x-workspace-id: <B-uuid>`, `GET /sdk/secrets`, `/sdk/context-variables`, `/sdk/conversations`. Cross-ws data = CONFIRMED.
- **A2 privesc:** non-admin key -> `POST /sdk/programmatic-users {roleConfig:{accountRole:administrator}}` -> `POST .../api-tokens` -> account-level read. 200 = privesc.
- **A3 data-request webhook SSRF + `{{secrets.*}}` relay:** `POST /sdk/data-requests` webhook url -> canary collaborator, header `{{secrets.<name>}}`. HARD STOP if fetch reaches IMDS/fleet identity.
- **A6 token IDOR:** `POST/DELETE /sdk/programmatic-users/{userId}/api-tokens` keyed only on caller-supplied `userId` — mint/delete a token for another tenant's admin user. 200 = takeover/DoS.

### Teardown: COMPLETE. 1 Connect instance created + deleted + verified (tag sweep + list empty). npm tarball only in /tmp (no AWS resource).
