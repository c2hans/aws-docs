---
name: eventbridge-scheduler-hunt
description: EventBridge/Scheduler family hunt (run 2026-09-30-1) — confirmed connection-secret exfil via api-destination repoint, egress-guard behavior, PassRole boundary holds, eventsv2 SDK gap
metadata:
  type: project
---

EventBridge/Scheduler family hunt executed 2026-09-30 in account 289531347876 (`awsbb2` = research-admin AdministratorAccess). Second account 183174222929 (`root`) session was expired → cross-account leads blocked.

**Confirmed (reuse these):**
- **Connection-secret exfil bypassing a Secrets Manager `GetSecretValue` deny (HIGH).** A principal with `events:UpdateApiDestination`/`CreateApiDestination` on Resource `*` but explicitly denied `secretsmanager:GetSecretValue` can repoint an existing API destination (or bind any existing connection) to an attacker HTTPS endpoint; the ApiDestinations fleet replays the connection's injected auth header (UA `Amazon/EventBridge/ApiDestinations`) to that endpoint. No permission on the connection/secret is checked. The SM deny does not protect the connection secret. Routing: account-operator.
- **Shipped Scheduler sample policy grants `iam:PassRole` `role/*`** gated only by `iam:PassedToService=scheduler.amazonaws.com` — SimulatePrincipalPolicy allows passing any role (incl. pre-existing privileged roles). AWS-authored least-priv defect; enabling precondition for universal-target privesc.

**Refuted / boundaries that HELD (don't re-chase without new info):**
- Universal-target privesc thesis (Scheduler `CreateSchedule` + classic `PutTargets`): `iam:PassRole` IS enforced at create time (AccessDeniedException before target check). `PassedToService` condition enforced. Read/list/describe universal actions rejected at create (`ValidationException: <api> is not supported`). Doc confirms eventsv2 CreateSubscriber requires PassRole too.
- InputTransformer injection: EventBridge ESCAPES values substituted from Input Path into JSON string context (doc claim of "no escaping" does NOT reproduce).
- OAuth/api-destination SSRF egress guards: `http://` scheme rejected at validation (https-only), 3xx redirects NOT followed ("endpoint redirection messages are not allowed"), `https://169.254.169.254` accepted at create but fetch returns generic internal error with no data leak. `https` link-local host has NO allowlist at create but no exploitable leak channel. See [[route53-media-ssrf-egress-guards]].
- Confirmed egress fetchers leak the auth material to the configured host: API_KEY header (api-destination delivery) and OAuth `client_secret` in the token-fetch body (authorize time). UA for OAuth fetch = `Apache-HttpClient/UNAVAILABLE (Java/1.8.0_504)`.

**Env facts:** botocore 1.43.95 / CLI do NOT model `eventsv2` (CreateSubscriber/PutRawEvents/custom-bus-v2 universal targets). Endpoint `eventsv2.us-east-1.amazonaws.com` resolves but returns UnknownOperationException to guessed JSON1.1 targets — wire protocol not reproducible with this SDK. Pre-existing secret `mqhunt-victim-secret-2496` belongs to another engagement — do NOT touch.
