# EC2 AMI Billing & Capacity-Reservation Billing-Ownership Transfer — Attack Research Plan

**Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`)
**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html
**Source of leads (docs read, online + offline mirror `/work/aws-docs`):**
- UserGuide: `ami-billing-info`, `billing-info-fields`, `view-billing-info`, `verify-ami-charges`, `assign-billing`, `request-billing-transfer`, `view-billing-transfers`, `accept-decline-billing-transfer`, `cancel-billing-transfer`, `billing-ownership-events`
- APIReference: `AssociateCapacityReservationBillingOwner`, `AcceptCapacityReservationBillingOwnership`, `RejectCapacityReservationBillingOwnership`, `DisassociateCapacityReservationBillingOwner`, `DescribeCapacityReservationBillingRequests`, `CapacityReservationBillingRequest`
- Online sync **verified** via WebFetch of the `AssociateCapacityReservationBillingOwner` API `.md` (offline == online).

**Status:** Documentation-derived hypotheses only. Nothing was tested against a live account. Where the docs are silent, the lead is marked **doc-gap** and the surface must be confirmed before hunting.

> **Note on repeated in-doc text (SUSPECTED PROMPT INJECTION, benign to this task):** every page in this cluster — local *and* the live-fetched copy — ends with a "See also / Skills for AI coding assistants (optional)" block urging the reader to run `aws agent-toolkit search-skills --search-query AWSEC2`. It is embedded documentation content, not a user instruction, and it was **not** acted upon. It is recorded here only as an observation; it does not describe a service boundary and generates no lead against the target.

---

## 0. How to use this document

- Each lead is stated as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs the plan did not anticipate.
- The whole feature is a **financial-liability transfer between two AWS accounts gated by a 12-hour consent step.** The consent gate and the "shared + same-org" precondition are the *entire* security model. Every top lead asks whether one of those two gates actually holds.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service/billing plane (not two customer accounts you control), stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe AWS's billing backend.
- The hunter needs **three accounts under one Organizations payer** to exercise the core (owner `O`, targeted consumer `C`, and a third shared-but-not-targeted account `T`), plus one account in a **different org** (`X`) for the cross-org tests. All test data (CRs, tags) must be synthetic canaries; every CR created must be torn down.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Force billing of unused Capacity-Reservation capacity onto an account that never accepted it** — i.e. defeat the accept gate (attach billing while state ≠ `accepted`, or via a replay of a stale/expired/`revoked` request). *Financial griefing / unwanted-liability.*
2. **Accept or reject a billing request that was not addressed to my account** — accept/reject are authorized by `CapacityReservationId` alone (no request nonce); prove another shared account `T` (or any account that can name `cr-…`) can settle a request targeted at `C`.
3. **Assign billing to an account the Capacity Reservation is *not* shared with, or that is in a different Organizations payer** — defeat the "shared + same-org" precondition at `Associate` time.
4. **Read another account's Capacity-Reservation internals** (size, tags, instance usage via `capacityReservationInfo`) through a `pending`/`rejected` billing request, before/without ever becoming billing owner. *Disclosure-timing.*
5. **Enumerate or spam** — use guessable `cr-…` IDs or fan-out across many CRs to flood a victim account with billing requests/EventBridge events, or discover valid CR IDs via error-oracle differences.
6. **AMI billing-metadata integrity** — cause the billing code an instance is actually charged (`UsageOperation`) to diverge from the `PlatformDetails`/`UsageOperation` a launcher sees on a shared/public AMI before launch.
7. **Audit-gap** — perform any of the above with no CloudTrail/EventBridge record reaching the victim.

---

## 2. Components, Assets, and Design

### 2.1 What the target page actually is
`ami-billing-info.html` is a **read-only informational hub**. It documents two AMI metadata fields and points to a sibling cluster (the mutating surface):
- **`PlatformDetails`** — "The platform details associated with the billing code of the AMI" (e.g. `Red Hat Enterprise Linux`). (`billing-info-fields.html`)
- **`UsageOperation`** — "The operation of the Amazon EC2 instance and the billing code that is associated with the AMI" (e.g. `RunInstances:0010`); "corresponds to the `lineitem/Operation` column on your … (CUR)". (`billing-info-fields.html`)

Both are surfaced by `describe-images` / `describe-instances` (`view-billing-info.html`). They are **attacker-influenceable only by the AMI *publisher*** (the account that registers/shares the AMI sets the billing code); the *launcher* only reads them. This is the one trust seam inside the target page itself (→ Lead F1 / Lens I integrity).

### 2.2 The real mutating surface — Capacity-Reservation billing-ownership transfer
Reachable one hop away (`assign-billing.html` and children). Mechanism:

- **Actors:** a **Capacity Reservation owner** account and a **consumer** account. Both must sit under the **same AWS Organizations payer account**, and the CR must already be **shared** with the consumer.
- **The object:** *billing ownership of the unused/"available" capacity* of a shared CR. By default the owner is billed for unused capacity; the owner can **reassign** that liability to a consumer. "After billing is assigned to another account, that account becomes the *billing owner* of any available capacity" and "charges … are billed to the assigned account instead of the owner's account." (`assign-billing.html`)
- **Consent gate:** the target account "must either accept or reject it within 12 hours"; unaccepted requests `expire`. Only after `accepted` does liability move. (`assign-billing.html`, `request-billing-transfer.html`)
- **Privilege claim (an integrity boundary to test):** "The account to which billing is assigned does not get any additional privileges; they can't cancel, modify, or share the Capacity Reservation." (`assign-billing.html`)
- **Identity:** SigV4 IAM. Cross-account trust is carried by Organizations (same payer) + RAM/Organizations CR sharing — **not** by any per-request token.
- **Resource IDs:** `CapacityReservationId` = `cr-…` (opaque, ~17 hex). Account IDs = fixed `[0-9]{12}` (`AssociateCapacityReservationBillingOwner` request pattern). **A billing "request" has no independent request-ID that the caller must present** — accept/reject/settle operations are keyed on `CapacityReservationId` alone.

### 2.3 ASCII flow

```
 AMI publisher ──sets billing code──► [AMI: PlatformDetails / UsageOperation]  ──read──► launcher (describe-images)
                                                                                    │ (F1: displayed code vs charged code?)
 ┌───────────────────────────── same AWS Organizations payer ─────────────────────────────┐
 │                                                                                          │
 │  Owner account O                              Consumer account C (targeted)              │
 │  ├ owns CR cr-XXXX (shared w/ C, T, …)                                                   │
 │  │                                                                                       │
 │  ├─ Associate(cr-XXXX, C) ──── request(pending, 12h TTL) ──► EventBridge ─► C            │
 │  │        ▲ precondition: CR shared with C AND C in same org (checked when? P3)          │
 │  │        │                                                                              │
 │  │  Disassociate(cr-XXXX, C)  cancel(pending)/revoke(accepted)                           │
 │  │                                                                                       │
 │  │                          Accept(cr-XXXX)  / Reject(cr-XXXX)  ◄── C (or T? A1)         │
 │  │                              │  keyed on cr-ID only, no request nonce                 │
 │  ▼                              ▼                                                        │
 │  billing owner of UNUSED capacity flips O→C on 'accepted'  (liability = $$$)             │
 │                                                                                          │
 │  DescribeCapacityReservationBillingRequests(Role=odcr-owner | unused-…-owner)            │
 │     └─ returns CapacityReservationBillingRequest{ capacityReservationInfo,               │
 │           requestedBy, unusedReservationBillingOwnerId, status, statusMessage }  (A2)    │
 └──────────────────────────────────────────────────────────────────────────────────────────┘
   Cross-org account X  ─── should be REJECTED at Associate (P4)
```

### 2.4 Mandatory coverage sweep (pages checked → lens relevance)
- **Server-side-dereferenced location fields (→G SSRF):** none. Read every page above; the only fields are billing codes, account IDs, CR IDs, an EventBridge event body, and CUR line-item names. **No URL/URI/host/webhook/logo field exists.** → Lens G null (evidence-backed).
- **Uploaded blobs / pointers (→Q):** none in this cluster. → Lens Q null.
- **Gates before a privileged state change (→P):** the 12-hour **accept/reject** gate; the **shared + same-org** precondition; the **"only owner can cancel/revoke"** rule; auto-revoke on leaving org / un-sharing. → Lens P is the primary firing lens.
- **"Revealed only after <step>" statements (→A disclosure-timing):** `capacityReservationInfo` returned inside a billing *request*; account IDs (`requestedBy`, `unusedReservationBillingOwnerId`) exposed in the request and in EventBridge events. → Lens A disclosure-timing fires.

---

## 3. API / Interface Inventory

| Name | Method (query action) | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers (per docs) | Notes / lead |
|---|---|---|---|---|---|---|---|---|
| `AssociateCapacityReservationBillingOwner` | POST (Query) | Existing (2024) | **Mutating** | External | Owner initiates billing-transfer request | Yes (SigV4) | CR owner; target must be shared + same org | Body: `CapacityReservationId`, `UnusedReservationBillingOwnerId=[0-9]{12}`. **Precondition-enforcement timing unclear** → P3/P4 |
| `AcceptCapacityReservationBillingOwnership` | POST (Query) | Existing | **Mutating** (moves $ liability) | External | Consumer accepts | Yes | "your account" (the targeted consumer) | **Only param = `CapacityReservationId`; no request nonce** → A1 authorization-by-CR-ID |
| `RejectCapacityReservationBillingOwnership` | POST (Query) | Existing | Mutating | External | Consumer rejects | Yes | targeted consumer | Same shape as Accept → A1 |
| `DisassociateCapacityReservationBillingOwner` | POST (Query) | Existing | Mutating | External | Owner cancels (pending) / revokes (accepted) | Yes | "Only the Capacity Reservation owner" | Body: `CapacityReservationId`, `UnusedReservationBillingOwnerId` → E/A (owner-only enforced?) |
| `DescribeCapacityReservationBillingRequests` | POST (Query) | Existing | Non-mutating | External | List requests by role | Yes | `Role=odcr-owner` (as owner) or `unused-reservation-billing-owner` (as consumer) | Returns `capacityReservationInfo` → **A2 disclosure**. Filters: `status`, `requested-by`, `unused-reservation-billing-owner` |
| `DescribeImages` | GET/Query | Existing | Non-mutating | External | Read AMI incl. `PlatformDetails`/`UsageOperation` | Yes | any account with image visibility | F1 metadata integrity |
| `DescribeInstances` | GET/Query | Existing | Non-mutating | External | Read instance incl. billing fields | Yes | instance owner | F1 |

**Object leaked by Describe (`CapacityReservationBillingRequest`):** `capacityReservationId`, **`capacityReservationInfo` (full CR info object)**, `lastUpdateTime`, `requestedBy` (initiator account), `status`, `statusMessage`, `unusedReservationBillingOwnerId`. → A2.

**Doc inconsistency lead (Lens N):** `DescribeCapacityReservationBillingRequests` links to a UserGuide page `transfer-billing.html`, while the live UserGuide topic is `assign-billing.html`/`view-billing-transfers.html`. Possible renamed/legacy endpoint or doc drift — confirm no dual-endpoint/legacy naming exists for the same data. Low, but check.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (observation that proves it broke) |
|---|---|---|---|
| Owner account O | Consumer account C's **bill** | `Associate` → `Accept` moves unused-capacity liability | **Charges land on an account that is not in state `accepted`** (attached without consent, or after `expired`/`rejected`/`revoked`) = breach |
| Third shared account T | A request targeted at C | `Accept`/`Reject` keyed on `cr-ID` only | **T settling (accept/reject) a request whose `unusedReservationBillingOwnerId` = C** = cross-tenant authz breach |
| Owner O | An account X in a **different org** / not shared | `Associate(cr, X)` | **`Associate` succeeds (or billing later attaches) for X outside the org / without CR sharing** = precondition bypass |
| Consumer C | Owner O's CR internals | `capacityReservationInfo` in a billing request | **C reads CR size/tags/usage from a `pending` or `rejected` request** (data before/without the gating `accepted`) = disclosure breach |
| Any caller | Owner O's CR existence | `cr-…` ID space + error responses | **Distinct not-found vs access-denied vs already-requested errors form a CR-ID enumeration oracle** |
| AMI publisher | Launcher's bill | billing code baked into shared/public AMI | **Charged `lineitem/Operation` ≠ the `UsageOperation` the launcher saw pre-launch** = billing-integrity breach |
| Any customer | **AWS's own billing/service plane** | — | **Any AWS-owned identity/credential/ARN/account, or influence over AWS's billing backend** = HARD STOP, preserve + disclose |

---

## 5. Recommended Areas of Focus (priority-ordered; one block per firing lens)

### AF-1 — Consent-gate integrity & accept/reject authorization  *(Lens P + Lens A — HIGHEST)*
**Background.** Moving unused-capacity billing from O to C is gated by a 12-hour accept step, and `Accept`/`Reject` take **only** `CapacityReservationId` — there is no request token, no `requestedBy`, no consumer-ID parameter that the caller must present. The "request" is identified purely by the `(CR, targeted-consumer)` pair server-side.

**Security Concern.** If authorization for `Accept`/`Reject` is derived from "caller is a consumer the CR is shared with" rather than "caller == `unusedReservationBillingOwnerId` of *this* request," then a **different** shared account can settle a request meant for another; and if state transitions are not strictly checked, a stale/expired/revoked request may be re-accepted (TOCTOU/replay), attaching liability with no valid live consent. **Why this gate is load-bearing (IAM sub-analysis):** there is **no IAM condition key that lets a consumer refuse being targeted** (no account-scoping key exists) and **no resource policy** on CRs — so a targeted account's *only* protection against unwanted financial liability is (a) the "shared + same-org" precondition and (b) this accept gate. Break either and there is no residual IAM defense to fall back on.

**High-level Test Scenarios (falsifiable claims):**
- **Claim P1 (replay/expiry TOCTOU):** `Accept(cr)` succeeds *after* the 12-hour window has elapsed (request should be `expired`). → **Oracle:** billing owner flips to caller though `status` was `expired`. Precond: owner `Associate`, wait >12h, then consumer `Accept`. Cost: low. **Severity if true: High** (consent bypass → forced liability). Stop when billing attaches post-expiry.
- **Claim P2 (revoke/accept race):** simultaneous owner `Disassociate`(revoke) and consumer `Accept` on the same `cr` leaves billing `accepted` (or attaches then isn't billed-back). → **Oracle:** final `status`=`accepted` with liability on C after a completed revoke. **Severity: Medium–High.**
- **Claim A1 (accept-by-wrong-account):** account **T** (CR shared with T, but request targeted at **C**) calls `Accept(cr)` and *T* becomes billing owner, or the request for C is consumed/rejected by T. → **Oracle:** `unusedReservationBillingOwnerId` in the resulting state = T, or C's pending request disappears via T's action. **Severity: High** (cross-tenant authz on a financial object). This is the single highest-value test — it directly probes the "keyed on cr-ID only" shape.
- **Claim P3 (idempotent re-attach):** after a `revoked` request, a fresh `Accept(cr)` (no new `Associate`) re-attaches billing. → **Oracle:** billing owner = C without a new owner-initiated request. **Severity: Medium–High.**

**Doc evidence:** `AcceptCapacityReservationBillingOwnership` / `RejectCapacityReservationBillingOwnership` request params (only `CapacityReservationId`); `assign-billing.html` ("must either accept or reject it within 12 hours"); `view-billing-transfers.html` state table.
**Severity-if-true:** High.

### AF-2 — Cross-org / not-shared precondition & the sharing↔billing asymmetry  *(Lens P + Lens B)*
**Background.** Docs state billing "can be assigned only to an account with which the Capacity Reservation is shared and that is consolidated under the same AWS Organizations payer account," and this is documented as **server-side and continuously enforced** (the request auto-`revoked` if the CR is un-shared or the consumer leaves the org). **Confirmed asymmetry (IAM sub-analysis):** CR *sharing* via RAM can target **any AWS account, including out-of-org** (`ram/.../shareable.md`), but billing *assignment* requires **same payer**. So a CR can legitimately be shared with an out-of-org account that launches instances, yet that account may never become billing owner.

**Security Concern.** The `Associate` body is just `cr-ID` + a raw 12-digit account number, and — per the IAM sub-analysis — **no IAM condition key scopes the counterparty account** (there is no `ec2:UnusedReservationBillingOwnerId` key; `UnusedReservationBillingOwnerId` is a request param but not conditionable). The "same-payer + shared" rule is therefore enforced **only by service business logic**, with no IAM backstop and no documented action-specific error code. The interesting cases are the boundary of that business logic: the **out-of-org-but-shared** target (whose failure mode is undocumented — doc-gap), and any TOCTOU gap in the "continuous" re-check.

**High-level Test Scenarios:**
- **Claim P4 (out-of-org shared target):** `Associate(cr, X)` where X is **shared** with the CR via RAM but sits in a **different** payer org. Docs imply this must fail the same-payer rule, but the failure mode is undocumented. → **Oracle:** X receives a `pending` request (EventBridge to X) or billing attaches → precondition bypass; or a clean documented rejection → refuted. **Severity if bypassed: High** (unsolicited request / liability to an external account). Stop at request delivery to X.
- **Claim P5 (unshare TOCTOU):** `Associate(cr, C)`, then owner **un-shares** the CR from C (or C is removed from a RAM OU) *before* C `Accept`s; does `Accept` still attach billing despite the "no longer shared → revoked" rule? → **Oracle:** billing attaches to a now-unshared account. **Severity: Medium–High.**
- **Claim P6 (leave-org settlement gap):** consumer leaves the org while `accepted`; billing "is automatically revoked" — is there a settlement window where charges still land on C (or on nobody)? → **Oracle:** CUR line items for the gap period. **Severity: Medium** (billing-integrity edge).

**Doc evidence:** `request-billing-transfer.html` (precondition); `assign-billing.html` Considerations ("automatically revoked … if they leave the organization … or … no longer shared"); `ram/.../shareable.md` line 172 (CR shareable with any AWS account, RAM customer-managed permissions **No**); IAM sub-analysis Q1/Q4 (no account-scoping condition key; no documented error code).
**Severity-if-true:** High (out-of-org bypass) / Medium (TOCTOU & settlement gaps).

### AF-3 — Disclosure via billing request (DOWNGRADED after IAM sub-analysis)  *(Lens A disclosure-timing)*
**Background.** `DescribeCapacityReservationBillingRequests` returns a `CapacityReservationBillingRequest` containing `capacityReservationInfo`, `requestedBy` (owner account ID), `lastUpdateTime`, and `status`. **Correction from the IAM sub-analysis:** the embedded `CapacityReservationInfo` object holds **only** `availabilityZone`, `availabilityZoneId`, `instanceType`, `tenancy` — **not** capacity size/count, tags, or occupant-instance data. Sharing already grants the consumer "total capacity and available capacity," so the marginal leak is small.

**Security Concern (narrowed).** The residual concern is not "CR posture harvest" (the object is too thin) but **unsolicited-request recon**: being *targeted* by an `Associate` reveals to the targeted account the owner's account ID (`requestedBy`) plus the CR's AZ/instance-type/tenancy, **before** any acceptance and without the target having asked. If P4 (out-of-org / arbitrary target) holds, this becomes a low-grade recon primitive: send a request to an account to leak that a CR exists in a given AZ/type owned by `requestedBy`. Data also remains readable for 24h after a terminal state.

**High-level Test Scenarios:**
- **Claim A2:** a targeted account reads `requestedBy` + `capacityReservationInfo` (AZ/AZ-id/instanceType/tenancy) from a **`pending`** request it never accepted. → **Oracle:** successful `Describe…(Role=unused-reservation-billing-owner)` returning those fields for a request in `pending`. **Severity: Low** (thin info; Low–Medium only if chained with P4 to hit arbitrary/out-of-org accounts).
- **Claim A2b:** the same fields remain readable in the "24 hours after `cancelled`/`expired`/`revoked`" window — data readable after the relationship ended. → **Oracle:** successful read post-`revoked`. **Severity: Low.**

**Doc evidence:** `API_CapacityReservationInfo` (fields = AZ/AZ-id/instanceType/tenancy only — IAM sub-analysis Q5); `capacity-reservation-sharing.html` ("Consumers can only view the total capacity and available capacity"); `view-billing-transfers.html` (24h post-terminal viewing).
**Severity-if-true:** Low (Low–Medium if chained with AF-2/P4).

### AF-4 — Cross-tenant financial DoS / request flooding  *(Lens L + Lens P)*
**Background.** Every `Associate` sends an EventBridge event to the targeted account and (per `view-billing-transfers.html`) an owner "can view only the **most recent** request" per CR — implying one live request per `(owner, CR)`.

**Security Concern.** An owner controls how many CRs exist; each CR can carry a live request to the same victim. Fan-out across N CRs → N unsolicited `pending` requests + N EventBridge events to one account = notification/eventing flood and repeated "review requests" banners. Combined with P4 (cross-org), the victim need not even be in the attacker's org. Also: does an owner rapidly `Associate`/`Disassociate`/`Associate` on one CR bypass the "one live request" cap to spam?

**High-level Test Scenarios:**
- **Claim L1:** owner creates M CRs and issues M concurrent billing requests to one consumer → M EventBridge events / banners; no per-target rate limit. → **Oracle:** M `pending` requests visible to the victim. **Severity: Medium** (cross-tenant nuisance; High only if it degrades a shared control).
- **Claim L2:** repeated `Associate`→`Disassociate` churn on a single CR generates unthrottled event spam. → **Oracle:** event count ≫ documented "most recent" single-request model. **Severity: Low–Medium.**

**Doc evidence:** `billing-ownership-events.html` (events on every state change); `view-billing-transfers.html` ("view only the most recent … request").
**Severity-if-true:** Medium.

### AF-5 — AMI billing-metadata integrity (the target page's own surface)  *(Lens I / integrity)*
**Background.** `PlatformDetails`/`UsageOperation` are "associated with the billing code of the AMI" and set by the AMI publisher; `verify-ami-charges.html` tells launchers the displayed `UsageOperation` "should match" the CUR `lineitem/Operation`.

**Security Concern.** For a **shared or public** AMI, the launcher reads these fields to predict cost *before* launch. If a publisher can present one billing code via `describe-images` while the launched instance is actually charged a different (higher, or Marketplace) operation, the "verify before you launch" guidance fails and launchers incur unplanned charges — an integrity/trust gap between displayed and charged billing codes.

**High-level Test Scenarios:**
- **Claim F1:** an AMI shared by publisher P shows `UsageOperation=RunInstances` (free) via `describe-images`, but an instance launched from it is billed a different `lineitem/Operation` (e.g. a Marketplace/paid code). → **Oracle:** CUR `lineitem/Operation` for the launched instance ≠ the AMI's advertised `UsageOperation`. Precond: two accounts, a shared AMI. **Severity: Medium** (financial mis-prediction; not cross-tenant data). Note: this likely reflects an AWS product-design property, not a customer-fixable bug — verify before rating higher, and HARD STOP if it implicates AWS's billing plane.

**Doc evidence:** `billing-info-fields.html`; `verify-ami-charges.html`.
**Severity-if-true:** Medium (frequently an out-of-scope product property — confirm first).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attach billing without a live `accepted` state (post-expiry / replay) | Accept/Reject state machine | "must accept or reject within 12 hours"; state table `pending→accepted/expired` |
| Settle a request addressed to another account (A1) | Accept/Reject authz (cr-ID-only keying) | Implicit "your account" wording — **no documented per-request nonce** |
| Assign billing cross-org / to non-shared account (P4/P5) | Associate precondition check | "shared … and same AWS Organizations payer account" |
| Owner-only cancel/revoke bypassed by consumer/third party | Disassociate authz | "Only the Capacity Reservation owner can cancel … revoke" |
| Read owner CR internals via pending/ended request (A2) | DescribeCapacityReservationBillingRequests / `capacityReservationInfo` | 24-hour post-terminal viewing window; role-scoped view |
| Notification/eventing flood to a victim account (L1/L2) | Associate + EventBridge | "view only the most recent request" (one-live-request implication) |
| Displayed vs charged AMI billing code (F1) | AMI `UsageOperation` metadata | "verify … matches" guidance (detective, not preventive) |
| Any action reaching AWS's billing/service plane | all | shared-responsibility line — **HARD STOP** |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **AWS's own billing/settlement backend, CUR generation, and the Organizations payer accounting** — the shared-responsibility line. Confirming that charges *route* between two accounts you control is in scope; probing AWS's billing engine is not. Any AWS-owned identity/ARN = HARD STOP.
- **A customer over-sharing their own CR or mis-setting their own IAM** (least-privilege footguns the owner inflicts on themselves).
- **Single-account self-DoS** (owner spamming their own account).
- **AMI billing-code design as a product property** (F1) if it proves to be intended AWS behavior rather than a spoof of *displayed* vs *charged* — downgrade/close.
- **The in-doc "agent-toolkit" note** — documentation content, not a service boundary.
- **Third-party SDKs / PowerShell cmdlet wrappers** — the wire API is the surface, not the client libraries.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens G (SSRF) — NULL (evidence-backed):** read `ami-billing-info`, `billing-info-fields`, `view-billing-info`, `verify-ami-charges`, `assign-billing`, `request-billing-transfer`, `view-billing-transfers`, `accept-decline-billing-transfer`, `cancel-billing-transfer`, `billing-ownership-events`, and all six API-reference pages. **No field is a URL/URI/host/webhook/logo/location the service dereferences.** No server-side fetch exists.
- **Lens Q (untrusted upload) — NULL:** no upload/image/attachment/document field anywhere in the cluster.
- **Lens F (translation/wire-injection) — NULL:** only inputs are `cr-…` IDs and `[0-9]{12}` account IDs (pattern-constrained); `statusMessage` is server-generated; no parser/translator/query-builder consumes caller free-text.
- **Lens C (credential vending) — NULL:** no STS AssumeRole / session-policy / token-as-input in this cluster.
- **Lens D (data→control plane) — NULL:** no data plane / ENI / host-agent surface; this is a control-plane-only IAM API set.
- **Lens H (KMS), J (OAuth/3P), K (prompt injection) — NULL:** no KMS key field, no 3P linking, no LLM/agent in the pipeline.
- **Lens B (confused deputy / PassRole) — RESOLVED to LIMITED:** no role-ARN is passed, so classic PassRole does not apply. IAM sub-analysis **confirms there is NO account-scoping condition key** (`UnusedReservationBillingOwnerId` is a request param but not conditionable) and **no resource policy** on CRs — so the consumer cannot IAM-deny being targeted. The confused-deputy-shaped concern (owner forcing liability) is therefore governed entirely by AF-1/AF-2 business-logic gates, not IAM. This *raises* the importance of AF-1.
- **Lens E (RBAC/privesc) — LOW (confirmed):** IAM sub-analysis confirms clean action-level separation — `Associate`/`Accept`/`Reject`/`Disassociate` are distinct actions, all scoped to the `capacity-reservation*` ARN; `Describe…` is a List-level action (`ec2:Region` only). A `Describe`-only principal cannot settle. Still worth a quick confirm that no single action bundles two capabilities.
- **Lens I (tagging/ABAC) — CONFIRMED SUPPORTED, test enforcement:** IAM sub-analysis confirms the 4 mutating actions **do** honor `aws:ResourceTag/${TagKey}` and `ec2:ResourceTag/${TagKey}` on the CR. So ABAC *can* gate which CR a principal acts on — test whether it is actually enforced (e.g. `Accept` on a CR whose tag should deny). Note ABAC scopes the **CR**, never the counterparty **account** (no account-scoping key).
- **Lens M (shared-identifier interception) — LOW:** the request has no interceptable token (keyed on cr-ID); folded into A1.
- **Lens N (namespace/endpoint drift) — LOW LEAD:** `DescribeCapacityReservationBillingRequests` doc links to `transfer-billing.html` while the live topic is `assign-billing.html` — verify there is no legacy/renamed endpoint exposing the same data under weaker authz. Also: a `#identifying-shared-cr` anchor referenced from `capacity-reservation-sharing.html` appears stale in the mirror (confirm live).
- **Lens O (audit-log evasion) — INFORMATIONAL/doc-gap:** EventBridge events are documented per state change, but **CloudTrail coverage of `Associate`/`Accept`/`Reject`/`Disassociate` is not stated**, and **no action-specific error codes are documented** for any of the 5 APIs (IAM sub-analysis Q4). Confirm each mutating call emits a CloudTrail record to the victim's trail; a silent settle would raise the severity of AF-1/AF-2. Undocumented error codes also mean error-response differences must be probed empirically as a possible CR-ID **enumeration oracle** (see boundary map).

### 8.1 IAM authorization model — resolved findings (from sub-analysis of `service-authorization/.../list_ec2` + RAM docs)
1. **Resource-level permissions supported:** all 4 mutating actions require the `capacity-reservation*` resource type (ARN `arn:aws:ec2:${Region}:${Account}:capacity-reservation/${CapacityReservationId}`) and honor tag/attribute condition keys (`aws:ResourceTag`, `ec2:InstanceType`, `ec2:AvailabilityZone`, `ec2:Tenancy`, dates, etc.). `Describe…` is List-level (`ec2:Region` only).
2. **No counterparty-account condition key exists** — IAM cannot restrict *which account* billing is assigned to/from; the same-payer/shared rule is pure service business logic. **→ makes AF-1/AF-2 the only real controls; no IAM backstop.**
3. **No resource-based policy** on CRs; RAM "customer managed permissions" is **explicitly No** for `ec2:CapacityReservation` (`ram/.../shareable.md`).
4. **Sharing↔billing asymmetry:** RAM can share a CR with **any** AWS account (incl. out-of-org); billing assignment requires **same payer**. Failure mode for an out-of-org-but-shared target is undocumented → **AF-2/P4**.
5. **Preconditions enforced server-side & continuously:** un-share or leave-org auto-`revokes` — test the TOCTOU seam (**AF-2/P5, P6**).
6. **`CapacityReservationInfo` is thin** (AZ/AZ-id/instanceType/tenancy only) → **AF-3 downgraded to Low**.
7. **Doc-gaps to treat as leads:** no action-specific error codes documented; EC2's central `security-iam` guide has **zero** mention of this cross-account financial-transfer feature.
