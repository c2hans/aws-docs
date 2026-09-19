---
name: agentcore-obo-findings
description: Run vh-obo-20260917 results — AgentCore Identity OBO token-exchange / OAuth2 cred-provider Account<->AWS seam. OBO-1 aud-injection primitive CONFIRMED-of-interest but NOT hard-stop (subject=caller's own principal); OBO-2 SSRF REFUTED (defense-in-depth set-time+fetch-time DNS/IP guard); OBO-3 strong claim REFUTED (auth-critical params blocked); OBO-4 issuer-agnosticism confirmed but intra-account/by-design (no finding). Zero confirmed vulnerabilities.
metadata:
  type: project
---

# Run vh-obo-20260917 (2026-09-17) — AgentCore Identity OBO Token-Exchange / OAuth2 Cred-Provider

Plan: `/work/aws-docs/AgentCore-OBO-ActorConfusion-attack-research-plan.md`. Follow-up to settled Consent-Portal/Gateway hunt (all cross-account REFUTED). This hunt targeted the **Account<->AWS seam**: OBO exchange + OAuth2 cred provider making AgentCore's OWN identity sign/fetch to caller-controlled targets. Account A=`default`=183174222929 (attacker/self), B=`awsbb2`=289531347876 (unused here — everything is caller-account-bound). All resources tagged `vh-run-id=vh-obo-20260917`. **Teardown verified clean.**

## Verdicts
- **OBO-1 (AWS_IAM_ID_TOKEN_JWT aud-injection oracle) — CONFIRMED-of-interest, NOT hard-stop → classified intended-behavior / informational disclosure.**
- **OBO-2 (SSRF via discoveryUrl/tokenEndpoint) — REFUTED (robust defense-in-depth).**
- **OBO-3 (customParameters RFC8693 injection) — strong claim REFUTED; only bounded non-critical param passthrough (by-design).**
- **OBO-4 (standalone-workload issuer/actor confusion) — issuer-agnosticism primitive CONFIRMED but intra-account/by-design; actor-confusion REFUTED. No finding.**
- **Zero confirmed vulnerabilities. Zero confirmed misconfigurations. One AWS-security informational disclosure note (claim minimization) preserved below.**

## Tooling that worked (reuse next time)
- **interactsh-client** (`/root/go/bin/interactsh-client`) is the request-capturing OOB collaborator — `raw-request` includes full HTTP POST bodies over valid-TLS `*.oast.pro/live/online` wildcard certs. Run: `interactsh-client -json -v -o out.json -sf sess -poll-interval 3 &`; payload host is on stderr/banner. This is what let us capture the actual outbound token-exchange bodies (env-tooling's "no inbound logs" note is about the github/cloudflare skills, NOT interactsh).
- **Self-hosted OIDC issuer on c2hans.github.io**: host `<path>/.well-known/openid-configuration` + `<path>/jwks.json`; REQUIRES a root `.nojekyll` file or Jekyll drops the `.well-known` dot-dir (404). RS256 self-signed JWT with `iss`=github.io path is accepted by GetWorkloadAccessTokenForJWT.
- botocore 1.43.95 has full `bedrock-agentcore` (data) + `bedrock-agentcore-control` OBO surface.

## OBO-4 primitive (CONFIRMED, but no finding) — standalone workload has NO issuer binding
`CreateWorkloadIdentity` takes only name + allowedResourceOauth2ReturnUrls (no issuer). `GetWorkloadAccessTokenForJWT(workloadName, userToken)` accepted an **arbitrary self-hosted-issuer** RS256 JWT (`iss=https://c2hans.github.io/vh-obo-20260917`, self-signed with my key, `sub=canary-user-A`) → 200, opaque KMS-envelope workload token (`AgV4...`, not a JWT). It does OIDC discovery on the JWT's own `iss`, fetches that issuer's JWKS, validates, and vends. The workload token is bound to the caller ACCOUNT, not to any cred provider or issuer — so any independently-valid JWT the caller can make discoverable works with any cred provider. **Intra-account / customer self-conflation → NOT a finding** (re-framed per plan). Actor is not forgeable downstream (see OBO-1/OBO-3).

## OBO-1 (highest value) — AWS_IAM_ID_TOKEN_JWT actor token, decoded
Setup: enabled `iam:EnableOutboundWebIdentityFederation` in A (was DISABLED pre-run; **GetOutboundWebIdentityFederationInfo → IssuerIdentifier=`https://a1971b17-666c-4821-8afb-7249a18a8bb2.tokens.sts.global.api.aws`, JwtVendingEnabled=true** — per-account STS global issuer). CustomOauth2 provider `vh-obo-20260917-p1` with `authorizationServerMetadata.tokenEndpoint=https://<interactsh>/...-token`, OBO `grantType=TOKEN_EXCHANGE, actorTokenContent=AWS_IAM_ID_TOKEN_JWT`. Minted workload token, called `GetResourceOauth2Token --oauth2-flow ON_BEHALF_OF_TOKEN_EXCHANGE`. Result: "Error parsing token exchange response" (interactsh returns non-OAuth) — but the outbound POST already left AWS from src IP **54.89.200.97** (AWS EC2 us-east-1), UA `Apache-HttpClient/UNAVAILABLE (Java/25.0.4.1)`.

**Captured actor_token (AWS-STS-signed sts:GetWebIdentityToken JWT), decoded — reproduced twice (fresh sessions):**
- header: `{"kid":"RSA_0","typ":"JWT","alg":"RS256"}`
- `aud`: `https://<interactsh-host>/vh-obo-20260917-p1-token` ← **attacker-chosen token endpoint, honored VERBATIM to off-AWS host** (per doc: aud = cred provider's token endpoint, by design)
- `sub`: `arn:aws:iam::183174222929:user/research-admin` ← **the CALLER's OWN account principal (NOT a fleet/service principal)** → hard-stop NOT triggered
- `iss`: `https://a1971b17-...tokens.sts.global.api.aws` (per-account STS global)
- `https://sts.amazonaws.com/` claim block: `invoked_by=bedrock-agentcore.amazonaws.com`, `org_id=o-pf2hyvtase`, `ou_path=[o-pf2hyvtase/r-ja5k/ou-ja5k-umgi471e/]`, `aws_account=183174222929`, `source_region`, `original_session_exp`, `principal_id`, `principal_tags={Purpose:aws-research-central-account}`
- subject_token = my inbound JWT forwarded verbatim (`sub=canary-user-A/B`, `subject_token_type=urn:ietf:params:oauth:token-type:jwt`).

**Analysis / classification = intended-behavior + informational disclosure (NOT a vuln, NOT hard-stop):** the token asserts the caller's OWN identity to a caller-CONFIGURED endpoint. No cross-tenant/cross-principal escalation (sub always = the API caller of GetResourceOauth2Token; a scoped principal would get sub=itself). The aud being the configured token endpoint is documented/by-design. Did NOT exercise the token against any RP (would be exploitation/hard-stop). **Disclosure-worthy nugget for AWS (routing: aws-security, claim minimization):** the brokered STS "outbound web identity" token embeds AWS **Organizations topology** (org_id + full OU path), principal tags, and the invoking service principal `bedrock-agentcore.amazonaws.com`, and is deliverable to ANY caller-specified public HTTPS endpoint — a customer pointing their OBO provider at an untrusted/compromised token endpoint leaks their org structure. Note also: the test accounts ARE inside AWS-internal org `o-pf2hyvtase` (contradicts "no org" brief — it's an AWS-internal research org).

## OBO-2 — SSRF via discoveryUrl / tokenEndpoint — REFUTED (defense-in-depth)
Set-time `CreateOauth2CredentialProvider` validation (all "TokenEndpoint/DiscoveryUrl is not a valid URL"):
- `http://` scheme REJECTED (https-only) → blocks HTTP-only IMDS structurally.
- IPv4 link-local literal `169.254.169.254` REJECTED; IPv6 `[fd00:ec2::254]` REJECTED; `localhost` REJECTED; IP-embedding hostname `169.254.169.254.nip.io` REJECTED.
- discoveryUrl must match regex `.+/\.well-known/(openid-configuration|oauth-authorization-server)`.
- Registrable public domain (`iam.amazonaws.com`, `x.example`, oast.pro, github.io) ACCEPTED.
**Decisive twin test:** two identical configs differing only by hostname — `vh-obo-pub.m1tz.de`→93.184.216.34 (public) **CREATED OK**; `vh-obo-ssrf.m1tz.de`→169.254.169.254 (link-local) **REJECTED**. So set-time validation RESOLVES DNS and blocks link-local/private IPs (defeats rebind at set-time).
**TOCTOU test:** created provider with `vh-obo-pub.m1tz.de` (public at set-time), then flipped that A record to 169.254.169.254 and ran OBO → **"Token endpoint is not a valid URL" (ValidationException, reqid 737abce1-...)**. Fetch-time ALSO re-resolves + blocks → TOCTOU-resistant defense-in-depth.
Residual: a fetch to a genuinely-public https host DOES happen server-side (AWS egress IP, UA Java HttpClient) but carries NO AWS creds/SigV4/fleet identity — just the OAuth body. That's by-design (fetching the customer's IdP). IMDS/fleet-SSRF branch fully refuted.

## OBO-3 — customParameters RFC 8693 injection — strong claim REFUTED
Server-side allowlist on `GetResourceOauth2Token.customParameters` (all "<x> cannot be present in customParameters for the specified OAuth2 Flow"):
- **BLOCKED (auth-critical):** `subject_token`, `actor_token`, `actor_token_type`, `client_id`, `client_secret`, `grant_type`, `scope`. Also collision-dedup: `resource` blocked when top-level `resources` set; `audience` blocked when top-level `audiences` set.
- **FORWARDED verbatim into the outbound RFC8693 body:** `audience`, `subject_token_type` (this one OVERRODE the default `urn:...:token-type:jwt` → became `urn:injected:sttype`), `requested_token_use`, and arbitrary custom keys (`vh_marker=canary-marker-123`).
So: cannot smuggle a different subject, cannot inject/override actor_token, cannot override client auth, cannot broaden scope via customParameters. Only bounded non-critical passthrough to the customer's OWN IdP, authenticated with the customer's OWN client creds → intended flexibility, not a boundary crossing. Note: API doc says customParameters "will not override" standard params, but `subject_token_type` IS overridable — cosmetic doc inaccuracy, not security-relevant.

## Teardown ledger (all destroyed + verified)
- IAM: `EnableOutboundWebIdentityFederation` (A) — re-DISABLED (pre-run state), verified FeatureDisabledException.
- bedrock-agentcore-control: workload identity `vh-obo-20260917-wl` DELETED; oauth2 providers `vh-obo-20260917-p1`, `-internalaws`, `-pubtwin` DELETED (list now []); managed Secrets Manager secrets auto-removed (residual scan []).
- Cloudflare m1tz.de: A records `vh-obo-ssrf` (id 1563d1b0...), `vh-obo-pub` (id 4382aadd...) DELETED (zone search []).
- github c2hans.github.io: `vh-obo-20260917/.well-known/openid-configuration`, `vh-obo-20260917/jwks.json`, and root `.nojekyll` (did NOT pre-exist) DELETED (all API 404). NOTE: git history retains prior versions (canary JWKS/config only — no secrets).
- interactsh-client process killed (none running).
No config changes to pre-existing resources beyond the IAM account setting (reverted).
