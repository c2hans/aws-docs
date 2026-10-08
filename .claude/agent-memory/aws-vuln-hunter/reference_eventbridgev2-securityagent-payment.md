---
name: eventbridgev2-securityagent-payment
description: Adjacent-lead facts — eventbridgev2 cross-account bus isolation, securityagent CI/CD targetUrl SSRF (no server-side fetch), AgentCore payment-connector cross-account isolation
metadata:
  type: reference
---

Live run 2026-10-07 ([[env-sessions]]). Three adjacent leads, all REFUTED (clean isolation). All reachable in botocore 1.43.108.

**W-1 eventbridgev2 (api 2025-05-15) — REFUTED, clean cross-account:**
- Reachable: `CreateEventBus(Name, Tags=<dict map, NOT list>)` → arn:aws:events:...:event-busv2/<name>/<id>. StorageConfiguration default retention 1 day.
- Attacker (no resource policy) cross-account on victim bus: PutEvents/CreateSubscriber/DescribeEventBus/GetResourcePolicy/PutResourcePolicy ALL → `AccessDeniedException "Access denied."` — no cross-account access without an explicit bus resource policy.
- `PutResourcePolicy` has an always-on public guard: wildcard `Principal:"*"` → `PublicPolicyException "...could grant public access... Replace any wildcard principal with specific principals, or add a condition..."`. A specific foreign-account principal (arn:aws:iam::<other>:root) IS accepted (intended owner-initiated share).
- Resource-policy action scoping is PRECISE: granting foreign acct ONLY `events:PutEvents` lets it PutEvents but NOT CreateSubscriber/DescribeEventBus/PutResourcePolicy (all AccessDenied) — no action-wildcard leak ("match too loose" refuted).
- `CreateSubscriber.InvokeConfiguration.RoleArn` must belong to the CALLING (subscriber-creator's) account: a granted foreign caller passing the bus-OWNER's roleArn → `AccessDeniedException` (cross-account PassRole denied) = confused-deputy REFUTED. Passing its own-account role only hit a param-shape InvalidInputException (authz already passed). So an owner who grants CreateSubscriber lets the foreign acct deliver to ITS OWN target with ITS OWN role — no privilege borrowed. UniversalTargetParameters (arbitrary aws-sdk action) is bounded by that caller-account role.

**W-2 securityagent (api 2025-09-06) CI/CD connector SSRF — REFUTED:**
- `CreateIntegration(provider enum[GITHUB,GITLAB,BITBUCKET,CONFLUENCE,AZURE_DEVOPS], input{<provider>:{...targetUrl/siteUrl...}})` + `InitiateProviderRegistration(provider, targetUrl, organizationName, clientId, clientSecret)` → returns {redirectTo, csrfState}. `state` fields must be hex [0-9a-fA-F]+.
- InitiateProviderRegistration does NOT fetch targetUrl server-side (returns <0.7s for nonexistent/dead/localhost hosts); it only EMBEDS targetUrl into a browser `redirectTo` OAuth URL (`<targetUrl>/rest/oauth2/latest/authorize?...&redirect_uri=https://securityagent.us-east-1.api.aws/oauth2/provider/register/callback/...`). The AWS callback host is fixed.
- bitbucketDataCenter `targetUrl` SSRF guard: rejects IP literals AND localhost AND decimal-encoded IPs (`https://2130706433` → ValidationException "must use a hostname, not an IP address or localhost"); a hostname passes then requires clientId+clientSecret. Guard is syntactic (a hostname with a private-IP A record is not caught at validation), BUT the only server-side fetch (OAuth token exchange at CreateIntegration) requires a valid `code` bound to a prior registration csrfState that only a cooperating OAuth server at targetUrl can mint — so an attacker-chosen internal/metadata host can't produce the code → fetch to internal unreachable. No fleet-SSRF, no hard stop.
- Onboarding chain: CreateApplication(all args optional) → CreateAgentSpace(name, codeReviewSettings{controlsScanning,generalPurposeScanning}) → CreateMembership(applicationId, agentSpaceId, membershipId[hex-ish regex], memberType, config). GITHUB CreateIntegration gated with AccessDenied (GitHub App not installed); BITBUCKET progressed to ValidationException (needs input.bitbucket not bitbucketDataCenter under provider=BITBUCKET).

**W-3 bedrock-agentcore-control payment connector — REFUTED, clean cross-account (same AgentCore isolation as [[agentcore-env]]):**
- `CreatePaymentManager(name, authorizerType enum[CUSTOM_JWT,AWS_IAM], roleArn)` — use AWS_IAM to avoid JWT discoveryUrl. The execution role must grant `bedrock-agentcore:*` (first attempt errored "role missing bedrock-agentcore:TagResource on workload identity"). Creates a workload-identity side-resource auto-deleted with the manager. Service principal for the role trust = `bedrock-agentcore.amazonaws.com`.
- `RotatePaymentConnectorCredentials(paymentManagerId, paymentConnectorId[min len 12], credentialsToRotate{coinbaseCDP{secrets:[API_KEY|WALLET_SECRET]}})` — Coinbase CDP API_KEY/WALLET_SECRET are SERVICE-PLANE secrets; use AWS_IAM-only canary managers, never trigger a real rotation/read.
- Cross-account: victim `GetPaymentManager(my pmId)` → `ResourceNotFoundException "Payment manager not found"` (owner-scoped; no existence leak). Minor benign note: victim `ListPaymentConnectors(my pmId)` → OK empty list (account-scoped query, returns caller's own connectors, not NotFound) — no cross-tenant data. Rotation of another tenant's connector unreachable (manager not found).
