---
name: invoicing-devopsagent-facts
description: Live behavior of AWS invoicing procurement-portal API + devops-agent (aidevops) trigger/agentspace isolation; WIDTH -m2 run 2026-10-04
metadata:
  type: project
---

Run 2026-10-04-m2 (WIDTH addendum). invoicing procurement-portal + devops-agent triggers. All cross-tenant hypotheses REFUTED; two AWS-authored artifact weak-defaults + one SSRF-filter note.

**invoicing (API invoicing-2024-12-01, signing name `invoicing`, SDK-modeled in botocore 1.43.95).** ProcurementPortal CRUD + Send/Verify/UpdateStatus all SDK-present. Both A/B can call (not read-allowlist-gated); Create/Delete work (not mutation-allowlist-gated either — NOT preview-blocked).
- **W-A1 IAM artifact:** `invoicing:*ProcurementPortal*` actions are action-level only — NOT resource-scopable (SimulateCustomPolicy with any ResourceArn => implicitDeny matched=0; without ResourceArns => allowed) and have ZERO condition keys. IAM imposes no tenant scope; isolation rests entirely on service code.
- **W-B1 cross-account IDOR REFUTED:** A Get/Put/Delete/Send/Verify/UpdateStatus on B's `arn:aws:invoicing::289531347876:procurement-portal-preference/<id>` => `AccessDeniedException` http400 "because no resource-based policy allows". Authz-FIRST: existent vs non-existent B ARN give IDENTICAL AccessDenied (NO enumeration oracle); same-account-missing gives `ResourceNotFoundException` http404. Service resolves ARN's embedded account and enforces ownership server-side. Pref id = UUIDv4 (enumeration refuted).
- **W-B2 foreign-InvoiceUnit egress REFUTED:** Create with `Selector.InvoiceUnitArns` naming B's unit => `ValidationException`; naming an A-account unit ARN that DOESN'T EXIST => 200 (ownership checked at ACCOUNT level, not unit existence). Gate-skip REFUTED: `UpdateProcurementPortalPreferenceStatus`→ACTIVE/VALIDATED/SUSPENDED => ValidationException "Transition ... can only be done by AWS"; Verify Code="" rejected by `\S+`; Verify needs an in-progress validation.
- **W-C1 SSRF/fetch-identity:** server-side fetch CONFIRMED. `SendProcurementPortalValidation` does `POST <endpoint>/cxml/invoices` from AWS us-east-1 egress IP (e.g. 34.200.183.109), `User-Agent: Jakarta Commons-HttpClient/3.0`, cXML InvoiceDetailRequest body. **NO AWS SigV4/fleet credential on outbound — only the customer's own `<SharedSecret>`** => hard-stop concern (fleet identity) REFUTED. OTP (6-digit) delivered INSIDE the cXML body = legit endpoint-ownership proof. 15-min Send cooldown (ThrottlingException) = anti-brute. Create-time endpoint allowlist is **LEXICAL**: https-only; rejects private/link-local IP literals + `localhost` ("not a valid https delivery endpoint"); but ACCEPTS public IP literals AND arbitrary hostnames incl `metadata.google.internal`. DNS-rebinding (hostname→private IP) fetch-time re-validation = UNDETERMINED by design (probing aims fleet at link-local = hard stop, NOT developed).
- **Area 6:** `GetProcurementPortalPreference` echoes `ProcurementPortalSharedSecret` in CLEAR (intra-account); List summary omits it. Low alone (Critical only if chained w/ the refuted cross-account Get).
- MarketplacePunchOut / `ApprovalRequestRedirectUrl` (net-new-in-window Area 5) NOT in botocore 1.43.95 model — host-match open-redirect untested (SDK-absent; needs hand-crafted SigV4).

**devops-agent (signing name `aidevops`, SDK-modeled; CreateAgentSpace/CreateTrigger/ListTriggers/etc).**
- **W-A2 artifact CONFIRMED:** shipped Operator sample (`Resource:"*"`) => all 5 `aidevops:*Trigger` actions ALLOWED against a B agentspace ARN (Simulate matched=1); tightened sample (`aws:ResourceAccount==aws:PrincipalAccount`) => implicitDeny. Sample omits the account pin = Lens R/U weak default, but server-side pin present (see W-B3) => defense-in-depth/Low-Med only.
- **W-B3 cross-account trigger IDOR REFUTED:** CreateTrigger/ListTriggers take BARE `agentSpaceId` path param (not ARN) — account derived from caller SigV4. From A against B's real space id: GetAgentSpace => 404 "not found" (identical to nonexistent id, no oracle); ListTriggers => 403; CreateTrigger => 403 BEFORE body validation. Service scopes lookup to caller account.

Resources all created+deleted (5 A prefs, 1 B pref, 1 B invoice-unit x5xd25ky, 1 B agentspace); teardown verified clean. interactsh-client (oast.site) used as OOB SSRF collector.
