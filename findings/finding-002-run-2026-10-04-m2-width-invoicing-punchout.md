# Run 2026-10-04-m2 — WIDTH addendum results (invoicing PunchOut + DevOps-Agent triggers)

Hunter execution of `_change-analysis/plans/2026-10-04-sincelastpush/_MASTER-hunter-dispatch-m2-width.md`.
Continuation of `-m1` (findings 000/001 untouched). Teardown verified clean (8 created, 8 deleted,
re-enumeration shows A/B prefs=0 units=0 spaces=0). In-scope accounts A=183174222929 / B=289531347876,
us-east-1, both verified via `sts:GetCallerIdentity` before any mutation. No out-of-scope account touched.

## Verdict table

| Lead | Verdict | Evidence / metadata | Severity | Routing |
|---|---|---|---|---|
| W-A1 invoicing IAM artifact | **confirmed (artifact)** | `invoicing:*ProcurementPortal*` actions are action-level-only, non-resource-scopable (SimulateCustomPolicy `allowed` without ResourceArns; zero condition keys). IAM imposes no tenant scope. | Low (context) | account-operator |
| W-B1 cross-account preference read/write (CROWN) | **REFUTED** | A→B Get/Delete/Send/Verify/UpdateStatus all `AccessDeniedException` ("no resource-based policy allows"). Existent==non-existent B ARN (no enum oracle); same-acct-missing = `ResourceNotFoundException` 404. Service enforces ARN-embedded-account ownership server-side. | n/a | — |
| W-B2 foreign-InvoiceUnit egress + gate-skip | **REFUTED** | Selector naming B unit `arn:aws:invoicing::289531347876:invoice-unit/x5xd25ky` → `ValidationException`; A non-existent unit → 200 (ownership, not existence, enforced). `UpdateStatus→ACTIVE/VALIDATED` → "Transition can only be done by AWS". `Code=""` → `\S+` reject. | n/a | — |
| W-C1 `SendProcurementPortalValidation` SSRF / fetch identity | **boundary-dependent / partial** | Server-side fetch CONFIRMED: `POST /portal/cxml/invoices` from AWS egress `34.200.183.109`, UA `Jakarta Commons-HttpClient/3.0`, cXML body carrying only the customer's own `<SharedSecret>` — **no fleet SigV4/credential outbound** ⇒ service-plane hard-stop concern REFUTED. Create-time allowlist is **lexical**: https-only, blocks private/link-local IP literals + `localhost`, but accepts public IP literals + arbitrary hostnames incl `metadata.google.internal`. | Low–Med (filter) | account-operator (+ AWS awareness on rebinding) |
| W-A2 devops-agent shipped-sample weak default | **confirmed (artifact)** | Shipped Operator policy (`Resource:"*"`) → all 5 `aidevops:*Trigger` ALLOWED vs B agentspace ARN; tightened example (`aws:ResourceAccount==aws:PrincipalAccount`) → implicitDeny. AWS sample omits the account pin. | Low–Med | account-operator |
| W-B3 cross-account Agent-Space trigger | **REFUTED** | Bare `agentSpaceId` path param; account derived from caller SigV4. A→B real id: GetAgentSpace 404, ListTriggers 403, CreateTrigger 403 before body validation. Server-side account scoping. | n/a | — |
| Area 6 (left/right) shared-secret read-back | **confirmed-behavior, Low** | `GetProcurementPortalPreference` echoes `ProcurementPortalSharedSecret` in clear **intra-account** (len 21); List summary omits it. Critical only if chained with the refuted cross-account Get. | Low/info | account-operator |

## Headline
The two crown cross-tenant hypotheses (**W-B1, W-B2**) and the DevOps-Agent cross-account trigger (**W-B3**)
are **cleanly REFUTED** at the service layer with authz-first denials and ARN-embedded-account ownership
validation. The IAM layer's total absence of resource/condition scoping (W-A1, W-A2 — real AWS-authored
artifact weak-defaults) is **fully backstopped by service code**, so those remain least-privilege /
defense-in-depth fixes to the shipped policies, NOT exploitable boundary crossings.

## The one item worth an AWS-side look — W-C1
`SendProcurementPortalValidation` performs a server-side cXML `POST` to the caller-configured endpoint.
Good news first: the outbound carries **no AWS fleet credential** (only the customer's own SharedSecret),
so it is not a service-plane confused-deputy. The weakness is that the Create-time endpoint allowlist is
**purely lexical** — it rejects private/link-local **IP literals** and `localhost`, but accepts arbitrary
**hostnames** (including `metadata.google.internal`) and public IP literals.

- **Open question (NOT developed — hard-stop discipline):** is a hostname that resolves to a private/
  link-local IP re-validated at *fetch* time (DNS-rebinding)? Testing this means deliberately aiming the
  AWS validation fleet at link-local/metadata, which is the service-plane line, so it was stopped.
- **Recommendation for a human reviewer:** fetch-time DNS re-resolution + private/link-local range
  rejection on the invoicing validation fetch. Routed `account-operator` for the lexical-filter weakness;
  **flagged for AWS awareness** on the rebinding question because confirming it probes the fleet.

## Blocked / untestable
- **Area 5 open-redirect** (`MarketplacePunchOutPreference.ApprovalRequestRedirectUrl`, the net-new-in-window
  field): `blocked: SDK-absent` — not in botocore 1.43.95; host-match validator untestable without
  hand-crafted SigV4. Carry to a future window when the Preview API ships in the SDK.

## Resources created & destroyed (all torn down, re-enumerated gone)
A: 5 procurement-portal-preferences (`2fc92cd5…, 47d88a4b…, 9aa0bafc…, acb23767…, eb6d83d6…`).
B: 1 preference (`26a58ce3…`), 1 invoice-unit (`x5xd25ky`), 1 agentspace (`05ebba58…`).
Teardown COMPLETE — re-enumeration A/B prefs=0 units=0 spaces=0. interactsh-client stopped, temp files
removed. No pre-existing resource modified.
