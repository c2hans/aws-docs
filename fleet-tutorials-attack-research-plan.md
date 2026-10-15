# EC2 Fleet Tutorials (Capacity Reservations + Instance Weighting) — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/fleet-tutorials.html` (hub) and its six child tutorials —
`ec2-fleet-instance-weighting-walkthrough`, `ec2-fleet-on-demand-walkthrough`,
`ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough`,
`ec2-fleet-launch-instances-capacity-blocks-walkthrough`,
`ec2-fleet-launch-instances-interruptible-cr-walkthrough`,
`ec2-fleet-launch-instances-multiple-cr-types-walkthrough` — plus the mechanism pages they link
(`ec2-fleet-instance-weighting`, `ec2-fleet-allocation-strategy`, `ec2-fleet-control-spending`,
`ec2-fleet-prerequisites`, `ec2-fleet-on-demand-capacity-reservations`,
`ec2-capacity-reservations`, `capacity-reservation-sharing`, `interruptible-capacity-reservations`,
`capacity-owner-procedures`, `capacity-consumer-procedures`, `monitor-interruptible-cr`,
`assign-billing`, `cr-groups`, `cr-groups-add`, `ec2-capacity-blocks`, `capacity-blocks-share`),
the AWS-managed policy `AWSEC2CapacityReservationFleetRolePolicy`, and the IAM Service Authorization
Reference `service-authorization/latest/reference/list_ec2.md`. Online `.md` twins cross-checked
against the offline mirror 2026-10-14.

Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note — what is NEW here vs. the 18 sibling fleet/spot-fleet plans.** The existing plans
> (`ec2-fleet-*`, `spot-fleet-*`, `modify-*`, `delete-fleet`, `cancel-spot-fleet`, scaling/monitoring
> families) are single-account/delegation-centric: SLR-launch guardrail bypass, PassRole, scaling
> control loops, cancel/terminate, metrics. **This plan is the first to cover the Capacity-Reservation
> (CR) consumption surface the tutorials introduce — the only genuine cross-account / cross-Organization
> trust boundary in the EC2 Fleet feature set** (shared ODCRs, Capacity Blocks for ML, cross-org
> *interruptible* CRs, and CR Resource Groups), plus instance-weighting capacity math. It deliberately
> defers SLR-launch condition-key non-propagation, PassRole/confused-deputy, cancel/terminate internals,
> and the auto-scaling loop to the siblings and cross-references them where they touch.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ordered). Look left and right for adjacent bugs.
- **In-scope / reportable (Tier 2):** weak defaults in **AWS-authored, copy-verbatim or uneditable artifacts** — the `AWSEC2CapacityReservationFleetRolePolicy` managed SLR policy (Area 1), the `ec2-fleet-prerequisites` sample user policy (Area 9). A true cross-account **consumption-without-a-share** enforcement gap (Area 2) would be Critical.
- **Out-of-scope / document-but-don't-report:** behaviors that require the *owner's own* RAM share first ("trust-abuse-after-share") and self-inflicted single-account cost footguns — these are documented design, not latent defects (see §7). Flag them so a hunter does not burn time proving AWS's own documented behavior.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane**, stop, preserve evidence, flag for AWS-Security disclosure. For CR work the realistic hard-stop trigger is any cross-account read/consume that reaches an account you were never shared into — treat as a boundary breach and preserve, do not escalate.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Consume reserved capacity you were never shared** — launch an EC2 Fleet / instance into a `CapacityReservationId` or CR-group ARN owned by an account that never RAM-shared it to you (cross-account capacity theft + billing shift onto the owner).
2. **Read another account's CR posture** — retrieve a foreign CR's instance type / AZ / total+available count / consumer list / billing-assignment requests with only the ID and no share relationship (capacity-planning info disclosure).
3. **Force-terminate a borrower's workload across the account boundary** — drive `UpdateInterruptibleCapacityReservationAllocation` (reclaim) or the org-leave path as a cross-account DoS with sub-2-minute or no notice.
4. **Escalate / overreach via the AWS-authored CR-Fleet SLR policy** — show a principal holding only `AWSEC2CapacityReservationFleetRolePolicy` (or the service acting under it) can Cancel/Modify a CR it should not, because the policy keys on tag *presence* (`crf-*`) not ownership.
5. **Shift cost onto a consented billing owner without re-consent** — after a billing-ownership accept, grow the CR's available capacity (or cancel a future-dated CR) so the assigned account's bill rises beyond what it agreed to.
6. **Prove the Org-scope / interruptible guarantees are unenforceable by EC2 IAM** — demonstrate no `aws:*OrgID` or `ec2:IsInterruptible` condition key is available on the consumer-side launch actions, so an admin cannot write the policy the docs imply.
7. **Amplify cost within one account** — instance-weighting rounding overshoot; MaxTotalPrice edge; CR-group priority/fallback drain.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SigV4 EC2 API + console. Relevant mutating actions: `CreateFleet`,
`RunInstances`; CR-management actions `CreateCapacityReservation`, `PurchaseCapacityBlock(/Extension)`,
`ModifyCapacityReservation`, `CancelCapacityReservation`, `CreateInterruptibleCapacityReservationAllocation`
**[NEW]**, `UpdateInterruptibleCapacityReservationAllocation` **[NEW]**,
`AssociateCapacityReservationBillingOwner` / `AcceptCapacityReservationBillingOwnership` **[billing transfer]**;
read actions `DescribeCapacityReservations`, `GetCapacityReservationUsage`,
`GetGroupsForCapacityReservation`, `DescribeCapacityReservationBillingRequests`; resource-group actions
via the AWS Resource Groups service (`resource-groups:GroupResources`); sharing via AWS RAM
(`ram:CreateResourceShare` / `ram:AssociateResourceShare`).

**Principals / trust zones.**
- **Fleet caller** — the identity invoking `CreateFleet`. Instances are launched by the **EC2 Fleet
  service-linked role `AWSServiceRoleForEC2Fleet`**, not re-authenticated per instance as the caller
  (established by sibling plans; the tutorials show no per-launch caller check, only attribute/existence
  matching — `cr-groups.md`: "EC2 matches the instances with any Capacity Reservation in the group that
  has matching attributes and available capacity").
- **CR owner** — the single account in the CR ARN `arn:${Partition}:ec2:${Region}:${Account}:capacity-reservation/${CapacityReservationId}`. Owns, manages, cancels, reclaims.
- **CR consumer** — an account the CR was RAM-shared to; "can only view the total capacity and available
  capacity" and manage its own instances (`capacity-reservation-sharing.md`).
- **Billing owner** — a consumer account that accepted a billing-ownership transfer; pays for unused
  capacity but "does not get any additional privileges" (`assign-billing.md`).
- **CR-Fleet SLR** — `AWSServiceRoleForEC2Fleet`-adjacent CR-Fleet role carrying the AWS-managed
  `AWSEC2CapacityReservationFleetRolePolicy`.
- **AWS service plane** — hard stop.

**Assets.** Reserved compute (ODCR / Capacity Block / interruptible allocation); the owner's On-Demand
instance **service quota** (shared-CR usage counts against it — see Area 7); billing attribution
(CUR line items `Reservation`/`UnusedBox`/`BoxUsage`); CR attributes (instance type, AZ-ID, counts) as
capacity-planning intelligence.

**Identifiers.** CR id `cr-` + 17 hex (high entropy, not enumerable — realistic disclosure is CloudTrail
/ tags / shared config / group listings, not brute force). CR-Fleet id `crf-`. CR-group ARN
`arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName}` (a **Resource Groups**
service resource, **not** an EC2 resource). AZ identity is **per-account-remapped**: only the AZ **ID**
(`use1-az1`) is stable across accounts; AZ **names** (`us-east-1a`) are not.

```
                        AWS RAM resource share (accounts / OU / whole Org)
   CR OWNER acct ──────────────────────────────────────────────► CONSUMER acct(s)
     │ owns cr-xxxx (ODCR / CapacityBlock / interruptible)          │
     │                                                              │ CreateFleet / RunInstances
     │ CreateInterruptibleCapacityReservationAllocation (carve)     │   target: CapacityReservationId
     │ UpdateInterruptible...Allocation (RECLAIM → 2-min kill)──────┼─► consumer instances TERMINATED
     │ AssociateCapacityReservationBillingOwner ──(12h accept)────► │   billing owner (pays UnusedBox)
     │                                                              │
     ▼ launched by EC2 Fleet SLR (not caller) ◄── no per-launch caller re-auth shown in docs
   CR Resource Group (owned + shared CRs mixed) ── priority list ReservationTypes + On-Demand fallback
```

---

## 3. API / Interface Inventory (CR + weighting surface)

| Name | Mut? | New? | Int/Ext | Authorized callers | `list_ec2` resource type / condition keys | Notes / lead |
|---|---|---|---|---|---|---|
| `CreateFleet` | Mut | existing | Ext | fleet callers | `capacity-reservation` (**non-required**) keys `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag`; `fleet*` req. | **No `ec2:CapacityReservationId`/`IsInterruptible` key** → can't IAM-pin which CR a fleet targets except by tag/literal-ARN. Area 2/6 |
| `RunInstances` | Mut | existing | Ext | all | `capacity-reservation` (non-req) keys `aws:ResourceTag`,`ec2:IsLaunchTemplateResource`,`ec2:LaunchTemplate`,`ec2:Region` | same gap; interruptible keys absent here too. Area 2/6 |
| `CreateInterruptibleCapacityReservationAllocation` | Mut | **NEW** | Ext | CR owner | `capacity-reservation*` + `ec2:IsInterruptible`,`ec2:InterruptibleCapacityReservationId`,`ec2:SourceCapacityReservationId`,`ec2:TargetInstanceCount` … | Carve interruptible allocation (≤1000, one per source). Area 3 |
| `UpdateInterruptibleCapacityReservationAllocation` | Mut | **NEW** | Ext | CR owner | `capacity-reservation*` + same interruptible keys | **Reclaim primitive** — "add more capacity or **reclaim** capacity"; lower target → kill borrowers. Area 3 |
| `AssociateCapacityReservationBillingOwner` | Mut | billing | Ext | CR owner | `capacity-reservation*` + rich keys, no org key | "assign billing of unused capacity to a consumer account". Area 5 |
| `AcceptCapacityReservationBillingOwnership` | Mut | billing | Ext | target consumer | `capacity-reservation*` + rich keys | 12h accept window. Area 5 |
| `DescribeCapacityReservationBillingRequests` | Non | billing | Ext | all | **blank resource type**, only `ec2:Region` | Unscopable read oracle of billing requests. Area 6 |
| `DescribeCapacityReservations` | Non | existing | Ext | all | **blank resource type**, only `ec2:Region` | Unscopable account-wide CR read oracle. Area 6 |
| `GetCapacityReservationUsage` | Non | existing | Ext | owner/consumer | `capacity-reservation*`, keys `aws:ResourceTag`,`ec2:CapacityReservationFleet`,`ec2:Region` | Lists consumer accounts using a CR. Area 6 |
| `GetGroupsForCapacityReservation` | Non | existing | Ext | owner/consumer | `capacity-reservation*`, same keys | Enumerate groups a CR is in. Area 6 |
| `ModifyCapacityReservation` | Mut | existing | Ext | CR owner | `capacity-reservation*` + `ec2:Attribute`,`ec2:Attribute/${AttributeName}`,`ec2:CapacityReservationFleet`,`ec2:Region` | `ec2:Attribute` case-sensitivity fail-open class (see modify-spot-fleet). EndDate/release-condition change. Area 3/8 |
| `PurchaseCapacityBlock` / `…Extension` | Mut | existing | Ext | buyer | `capacity-reservation*` | Prepaid GPU block; FCFS-after-share. Area 4 |
| `resource-groups:GroupResources` | Mut | existing | Ext | group owner | `group` resource type has **zero condition keys** | Add owned+shared CRs to a group. Area 7 |
| `CreateCapacityReservationFleet` / `Modify…` / `Cancel…` | Mut | existing | Ext | CRF owner | `capacity-reservation-fleet*` | Separate from EC2 Fleet; CRF SLR = Area 1 |

**Doc-flagged leads to keep verbatim:** `capacity-blocks-share.md`: Capacity Blocks are "first-come,
first-served basis for all accounts, **regardless of ownership status**." `capacity-reservation-sharing.md`:
"All Capacity Reservation usage counts toward the **Capacity Reservation owner's On-Demand Instance limits**."
`interruptible-capacity-reservations.md`: "there is **no fallback** to On-Demand or Spot" and instances
"**will be terminated when the owner reclaims capacity**." `capacity-owner-procedures.md`: org-leave →
instances "**eventually terminated**" (no notice guarantee stated).

**Doc-vs-doc contradiction flagged:** `interruptible-capacity-reservations.md` ("Capacity consumers")
says "**You can't add interruptible Capacity Reservations to capacity reservation groups**," while
`cr-groups.md`/`cr-groups-add.md`/`cr-groups-launch.md` and tutorial #6 treat interruptible CRs as a
first-class, priority-ordered group member (`ReservationTypes` includes `interruptible-capacity-reservation`).
Resolve first (Area 7) — it decides whether the interruptible tier even participates in group arbitration.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Consumer / arbitrary caller | Owner's CR capacity | `CreateFleet`/`RunInstances` targeting `cr-xxxx` or group ARN | **Launching into a CR never RAM-shared to the caller = breach** (Area 2). Expected clean result: `UnauthorizedOperation`/`…NotFound`. |
| Arbitrary caller (knows id) | Owner's CR attributes/usage/billing-requests | `DescribeCapacityReservations`/`GetCapacityReservationUsage`/`DescribeCapacityReservationBillingRequests` | **Returning foreign-owned CR attributes to a non-shared account = read breach** (Area 6). |
| CR owner (or compromised owner principal) | Consumer's running instances | `UpdateInterruptibleCapacityReservationAllocation` reclaim / org-leave | **Terminating a borrower's workload with <2-min or no notice = cross-account availability breach** (Area 3). Documented ≥ this; test for *missing* safeguards. |
| Principal holding only CR-Fleet SLR policy | Any `capacity-reservation` tagged with any `crf-*` | `Cancel/ModifyCapacityReservation` under `ArnLike ec2:CapacityReservationFleet=crf-*` | **Cancel/Modify a CR not belonging to the holder's own CR-Fleet = authz-by-presence breach** (Area 1). |
| CR owner | Consented billing owner | Post-accept capacity growth / future-dated cancel | **Raising the assigned account's bill beyond consented amount with no re-consent = integrity/billing breach** (Area 5). |
| Fleet caller | Owner's On-Demand service quota | Consumer instances count against **owner's** limit | **Exhausting the owner's On-Demand quota via shared-CR usage = cross-account resource-exhaustion** (Area 7). |
| Any customer surface | AWS service plane | — | **Any AWS-owned identity/ARN/account reached = HARD STOP.** |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — AWS-authored CR-Fleet SLR policy: Cancel/Modify-any-CR by tag *presence*  [Lens R / S] — Tier-2 reportable
**Background.** `AWSEC2CapacityReservationFleetRolePolicy` (SLR policy, ARN `arn:aws:iam::aws:policy/aws-service-role/AWSEC2CapacityReservationFleetRolePolicy`, v2, edited 2025-03-03) is attached to a service-linked role, **uneditable and copy-verbatim** — a weak default is AWS's defect, not a customer footgun.
**Security Concern.** The actual JSON:
- Statement 1: `ec2:DescribeCapacityReservations` + `ec2:DescribeInstances` on `Resource:"*"`, **no Condition** → the role can enumerate *every* CR and instance in the account.
- Statement 2: `ec2:CreateCapacityReservation` + `ec2:CancelCapacityReservation` + `ec2:ModifyCapacityReservation` on `arn:aws:ec2:*:*:capacity-reservation/*` gated **only** by `"ArnLike": {"ec2:CapacityReservationFleet": "arn:aws:ec2:*:*:capacity-reservation-fleet/crf-*"}`. The condition binds **membership in *some* CR Fleet (`crf-*` wildcard), not ownership of the caller's own CR Fleet** — the classic presence-not-ownership shape (cf. the Spot-Fleet terminate primitive keyed on `aws:ec2spot:fleet-request-id:"*"`).
**High-level Test Scenarios.**
- *Claim:* a CR carrying any `crf-*` association can be Cancelled/Modified under this policy regardless of which CR Fleet created it → **Mechanism:** `ArnLike … crf-*` wildcard. → **Oracle:** under a scoped principal holding exactly this policy (or `iam:SimulatePrincipalPolicy` as the safe first pass), attempt `ModifyCapacityReservation`/`CancelCapacityReservation` on a `capacity-reservation` associated with a *different* CR Fleet; `Allow` = confirmed over-grant. → **Severity:** Medium–High (destroy/alter a CR outside the intended fleet; cancelling a CR releases reserved capacity).
- *Claim:* Statement 1's unconditioned `Describe*:"*"` lets the SLR read all CRs/instances account-wide → trace whether any customer-reachable path can borrow the SLR's view (chains to Area 6).
**Doc evidence:** `aws-managed-policy/.../AWSEC2CapacityReservationFleetRolePolicy` JSON. **Severity-if-true:** Medium–High, **in scope** (AWS-authored uneditable artifact).
**Stop condition:** once Simulate/scoped-call shows Allow on a non-owned-fleet CR, record and stop — do not actually cancel foreign CRs.

### Area 2 — Can a fleet consume a CR it was never shared? (cross-account enforcement has no IAM backstop)  [Lens A / U / X]
**Background.** CR consumption authorization is not expressed in the caller's IAM policy: on `CreateFleet` and `RunInstances` the `capacity-reservation` resource type is **non-required** and carries only `aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag` (+`ec2:LaunchTemplate` on RunInstances). There is **no `ec2:CapacityReservationId` / `ec2:InstanceMatchCriteria` condition key** for these actions. Therefore the entire cross-account consumption boundary rests on the EC2 service's server-side RAM-share lookup — there is **no IAM resource-level safety net behind it.**
**Security Concern.** If that single server-side check has any gap (missing on one code path — group indirection, a specific launch shape, a late-binding `$Latest` launch-template, a race during share/unshare), a caller consumes reserved capacity owned by an account that never shared it, shifting the unused-capacity bill onto the owner and denying the owner its reservation.
**High-level Test Scenarios.**
- *Claim:* `CreateFleet`/`RunInstances` targeting a foreign `CapacityReservationId` never RAM-shared to the caller is rejected by the service, not silently honored. → **Oracle:** from account C (broad `ec2:CreateFleet`/`RunInstances`, no RAM share), target a known-but-unshared `cr-xxxx`. Clean result = `UnauthorizedOperation`/`InvalidCapacityReservationId.NotFound`; **200 + instance placed in the reserved capacity = Critical cross-account breach (HARD STOP, preserve).**
- *Claim (validator divergence):* the group-ARN path (`CapacityReservationResourceGroupArn`) and the direct-ID path enforce the share check with equal strictness. → **Oracle:** repeat the above via a group ARN that resolves to the foreign CR (ties to Area 7).
- *Claim (error-class oracle):* even when denied, the distinction `NotFound` vs `AccessDenied` vs silent on-demand fallback forms an existence oracle for foreign CR IDs. → **Oracle:** compare responses for a fabricated id, a real-but-unshared id, and a real-shared id.
**Doc evidence:** `list_ec2` CreateFleet (line ~5115) & RunInstances (line ~9586) rows; `ec2-fleet-on-demand-capacity-reservations` "must specifically target it". **Preconditions:** a foreign CR id (CloudTrail/tags/config leak; not brute-forceable at 17-hex entropy). **Severity-if-true:** Critical if consume-without-share holds; otherwise Low (confirms the boundary is server-side-only, informing Area 7's chain).
**Stop condition:** any successful foreign consume = stop + preserve + disclose.

### Area 3 — Interruptible-CR reclaim as a cross-account forced-termination primitive  [Lens AA / L / O]
**Background.** `interruptible-capacity-reservations`: an owner carves unused capacity into an interruptible allocation (`CreateInterruptibleCapacityReservationAllocation`, ≤1000, one per source), optionally RAM-shares it **within the Org only**, and reclaims "**at any time**" via `UpdateInterruptibleCapacityReservationAllocation --target-instance-count` lower; running borrower instances get a **2-minute** EventBridge warning (`EC2 Capacity Reservation Instance Interruption Warning`, `source: aws.ec2`) then terminate — "**no fallback to On-Demand or Spot**."
**Security Concern.** This is a legitimate owner capability, but it is a clean, repeatable **cross-account availability weapon** against borrowers, and the docs expose two sharp edges:
1. **No documented consumer veto, cooldown, minimum-hold, or rate limit** on reclaim.
2. **Org-leave path diverges:** when a consumer leaves the Org the allocation auto-unshares and instances are "**eventually terminated**" — `monitor-interruptible-cr` documents **no** event and **no** 2-minute guarantee for this path (only the two reclaim events exist). An Org admin evicting a member may kill its workloads with less/no notice.
**High-level Test Scenarios.**
- *Claim:* rapid `Update…Allocation` cycling (drop to 0 / raise) force-terminates borrower instances each cycle with no throttle. → **Oracle:** owner cycles target count while a borrower runs; observe repeated terminations + warning timing. **Severity:** High (cross-account DoS of borrower).
- *Claim:* the org-leave termination fires with less than the 2-minute warning (or none). → **Oracle:** share org-wide, launch in account B, remove B from Org, measure whether `Instance Interruption Warning` fires and the actual grace period. **Severity:** Medium–High (uncontrolled termination + stranded-consumption billing gap).
- *Claim:* the 2-minute warning rides the same `source:aws.ec2` channel as Spot interruption and is as suppressible/forgeable (cross-ref `fleet-monitor` EventBridge findings) → detection-evasion angle.
**Doc evidence:** `interruptible-capacity-reservations`, `capacity-owner-procedures` (Reclamation; "eventually terminated"), `monitor-interruptible-cr`. **Severity-if-true:** High (availability), but see §7 — reclaim itself is **documented design** requiring the owner's own share; the *reportable* residue is a missing-safeguard or missing-notice gap, not the reclaim capability.

### Area 4 — Capacity Block for ML: first-come-first-served "regardless of ownership"  [Lens L / U]
**Background.** `capacity-blocks-share`: "Capacity Blocks operate on a **first-come, first-served basis for all accounts, regardless of ownership status**. When you share a Capacity Block, if a consumer launches instances before the owner, those instances occupy the capacity until the consumer terminates … or until 30 minutes before the Capacity Block expires." UltraServer Capacity Blocks are explicitly not shareable.
**Security Concern.** The paying owner's intuition ("I bought it, I get priority") is false: a shared-to consumer can **race the owner and occupy the entire prepaid GPU block**, denying the owner the capacity it paid for for the block's life (minus a 30-min pre-expiry eviction window). Also contrasts with ODCR unshare (Area 2/7): Capacity Block "stop sharing" lets running consumer instances continue to 30-min-pre-expiry.
**High-level Test Scenarios.**
- *Claim:* a shared consumer filling the block the instant it goes `active` returns `InsufficientCapacityException` to the owner's own later launches. → **Oracle:** race `CreateFleet`/`RunInstances` from the consumer at block activation; confirm owner starvation.
- *Claim:* the "30 minutes before expiry" eviction is the only mechanism returning the block to the owner → verify no owner-initiated pre-emption of a consumer exists.
**Doc evidence:** `capacity-blocks-share` (FCFS sentence), `ec2-capacity-blocks` Considerations. **Severity-if-true:** documented design (owner-side capacity DoS after a share) — **catalogue, do not report** unless an *unshared* account can consume (that would be Area 2). Value: correct any trust model assuming ownership ⇒ launch priority.

### Area 5 — Billing-ownership transfer: cross-account cost-shift + post-consent amplification  [Lens P / A / U]
**Background.** `assign-billing`: owner may `AssociateCapacityReservationBillingOwner` to assign billing of a CR's *available (unused)* capacity to a consumer; the consumer must `Accept…` within **12 hours** (mutual consent; reject/expire → stays with owner). Billing is auto-revoked if the consumer leaves the Org or the CR is unshared (clean revocation — good). The assigned account "**does not get any additional privileges**."
**Security Concern.** Three edges:
1. **Post-accept unilateral growth.** "The available capacity … can change over time … For example, available capacity can increase if the Capacity Reservation owner increases the size of the Capacity Reservation" → after a consumer consents, the owner can `ModifyCapacityReservation` to grow the CR and **raise the assigned account's bill with no re-consent**.
2. **Future-dated cancel charge.** "If the owner cancels a future-dated Capacity Reservation that has billing assigned to another account, the **assigned billing owner pays the cancellation charges**." A consent to pay for *usage* becomes liability for a *cancellation fee* the owner triggers.
3. **Consent-gate integrity.** `DescribeCapacityReservationBillingRequests` has a **blank resource type / only `ec2:Region`** — an unscopable read of pending billing requests (recon for which transfers are in flight). Verify the accept side truly fails closed on expiry and cannot be forced without the target's accept.
**High-level Test Scenarios.**
- *Claim:* owner grows CR size after accept → assigned account's `UnusedBox` CUR line rises without a new consent event. → **Oracle:** accept a small assignment, owner `ModifyCapacityReservation` larger, inspect assigned account CUR / Service Quotas. **Severity:** Medium (billing integrity).
- *Claim:* a transfer can be driven to "accepted" without the target's explicit accept (replay/forge the accept, or default-accept on timeout). → **Oracle:** attempt `Associate…` then verify no state change until a genuine `Accept…`; confirm 12h expiry defaults to owner-billed. **Severity:** High if accept is bypassable.
**Doc evidence:** `assign-billing` (How it works, Considerations). **Severity-if-true:** Medium; High only if the accept gate is bypassable (that would be a real Lens-P break).

### Area 6 — Unscopable CR read oracles (attributes, usage, billing requests)  [Lens A / U / X] (read-side twin of `manage-spot-fleet`)
**Background.** `DescribeCapacityReservations` and `DescribeCapacityReservationBillingRequests` have **blank resource-type cells and only `ec2:Region`** in `list_ec2` — identical inert-ABAC asymmetry to `DescribeSpotFleetRequests` (see `manage-spot-fleet` plan). `GetCapacityReservationUsage` ("get usage information about a Capacity Reservation") and `GetGroupsForCapacityReservation` require `capacity-reservation*` but gain only `aws:ResourceTag`/`ec2:CapacityReservationFleet`/`ec2:Region`.
**Security Concern.** The richest reads can't be ABAC/tag-restricted, so an admin cannot pen a Deny that scopes CR visibility by tag/ARN. Within an account this is intra-account over-exposure (Lens S inert-Deny). The sharp question is cross-account: `capacity-reservation-sharing` promises "**Consumers can only view the total capacity and available capacity**" and "cannot view … instances owned by other consumers or the owner" — a guarantee to trace. `GetCapacityReservationUsage` returning the *list of consumer accounts* using a CR is consumer-identity disclosure.
**High-level Test Scenarios.**
- *Claim:* `DescribeCapacityReservations --capacity-reservation-ids cr-<foreign>` from a non-shared account returns attributes rather than `NotFound`. → **Oracle:** direct call; attributes returned = cross-account read breach (HARD STOP).
- *Claim:* a consumer can read more than "total + available" (e.g. other consumers' counts, owner tags, instance ids) via `GetCapacityReservationUsage`. → **Oracle:** compare a consumer's `GetCapacityReservationUsage` output to the documented "total + available only" promise (Lens U enforcement-vs-guarantee).
- *Claim:* `DescribeCapacityReservationBillingRequests` leaks pending transfer requests account-wide / across the share set.
**Doc evidence:** `list_ec2` rows; `capacity-reservation-sharing` consumer-permissions prose. **Severity-if-true:** Medium (capacity-planning / consumer-identity disclosure), High if it crosses to a non-shared account.

### Area 7 — CR Resource Groups: cross-ownership mixing, zero group condition keys, priority/fallback & owner-quota drain  [Lens A / S / L]
**Background.** A CR Resource Group (`arn:…:resource-groups:…:group/${GroupName}`) "can include Capacity Reservations that you own … **and** Capacity Reservations that are shared with you by other AWS accounts" (`cr-groups`). Targeting the group lets a fleet consume *any* member opportunistically. The `group` resource type carries **zero condition keys** in `list_ec2`; group membership is managed by the Resource Groups API (`resource-groups:GroupResources`) with the share check inherited from RAM, never restated EC2-side. Tutorial #6 adds priority arbitration: `ReservedCapacityOptions.ReservationTypes` (ordered: `on-demand-capacity-reservation` → `capacity-block` → `interruptible-capacity-reservation`), each **fully exhausted before the next**, with `ReservedCapacityFallbackOptions.MarketTypes=["on-demand"]` for the remainder.
**Security Concern.** (a) The group is an **indirection layer that mixes ownership boundaries** with no EC2-expressible authz on the group ARN itself — if any path lets a principal add a CR it only has *view* access to, or resolve a group to a CR the fleet isn't actually shared, that is the Area-2 breach reached transitively. (b) **Cross-account On-Demand quota drain:** "All Capacity Reservation usage counts toward the **owner's** On-Demand Instance limits … including usage by instances owned by consumers" — a consumer filling a shared CR consumes the *owner's* account-wide quota (bounded by CR size). (c) Caller-controlled priority/fallback = cost/starvation shaping. (d) **Resolve the doc contradiction** on whether interruptible CRs may join a group at all.
**High-level Test Scenarios.**
- *Claim:* `resource-groups:GroupResources` accepts a CR ARN not shared to the caller. → **Oracle:** add a non-shared foreign CR ARN to your group; `AccessDenied`/`NotFound` = boundary holds, accept = breach. 
- *Claim:* launching into a group ARN resolves to a member CR the fleet isn't shared (validator divergence vs direct-ID path). → **Oracle:** Area-2 test via group ARN.
- *Claim:* a consumer filling a shared CR reduces the **owner's** `DescribeAccountAttributes`/Service-Quotas On-Demand headroom. → **Oracle:** fill a shared CR from the consumer; inspect owner quota. **Severity:** Low–Medium (bounded cross-account exhaustion).
- *Claim:* interruptible CRs cannot actually be grouped (per `interruptible-capacity-reservations`) → **Oracle:** attempt tutorial-#6's `group-resources` with an interruptible CR ARN; rejection resolves the contradiction and collapses the interruptible branch of the priority lens.
**Doc evidence:** `cr-groups`, `cr-groups-add`, `capacity-reservation-sharing` (owner-limit prose), tutorial #6, `list_ec2` `group` row (empty keys). **Severity-if-true:** High if group indirection yields unshared consumption; else Low–Medium.

### Area 8 — Interruptible / consumer-side condition keys exist but are wired to the wrong actions (unenforceable guardrails)  [Lens S / U]
**Background.** EC2 defines `ec2:IsInterruptible` (Bool), `ec2:InterruptibleCapacityReservationId`, `ec2:SourceCapacityReservationId`, `ec2:TargetInstanceCount` — but **only on the owner-side allocation actions** (`Create/UpdateInterruptibleCapacityReservationAllocation`) and on the `capacity-reservation` *resource* row. They are **absent from `CreateFleet` and `RunInstances`.** Separately, **no AWS Organizations condition key exists anywhere in EC2** (`aws:PrincipalOrgID`/`aws:ResourceOrgID`/`…OrgPaths` return **zero** matches across `list_ec2`).
**Security Concern.** Two guardrails the docs imply a customer could build are **not expressible in an identity policy on the launch path:**
1. "My fleets may only launch into **non-interruptible** (non-terminable) capacity" / "only into interruptible CR X" — impossible, because `ec2:IsInterruptible`/`ec2:InterruptibleCapacityReservationId` aren't available on `RunInstances`/`CreateFleet`. A fleet can be steered into terminable borrowed capacity with no IAM means to forbid it.
2. "Only consume CRs **within my Org**" — impossible via EC2 IAM (no `aws:*OrgID` key); enforcement is 100% RAM-share state + SCP, never a resource-level EC2 condition. The interruptible "within your AWS organization" guarantee has **no EC2 IAM enforcement mechanism** (Lens U: guarantee traced to orchestration/RAM, not IAM).
**High-level Test Scenarios.**
- *Claim:* an admin cannot author an identity policy that denies a fleet from launching into interruptible capacity. → **Oracle:** attempt a Deny using `ec2:IsInterruptible` on `RunInstances`/`CreateFleet` via `iam:SimulateCustomPolicy`; the key is not evaluated (inert) = confirmed (same class as the `ec2:InterfaceType`-doesn't-exist / case-sensitivity fail-opens catalogued for modify-spot-fleet).
- *Claim:* no `aws:ResourceOrgID` Deny can scope CR consumption. → **Oracle:** grep + Simulate; confirm inert.
**Doc evidence:** `list_ec2` CreateFleet/RunInstances rows vs the interruptible-allocation rows; zero-match Org-key grep. **Severity-if-true:** Medium (guardrail-expressibility gap; AWS-owned — a customer building a compliance control on "we can't touch interruptible capacity" would be relying on a non-enforceable claim).

### Area 9 — `ec2-fleet-prerequisites` sample user policy & instance-weighting cost math  [Lens R / L / business-logic]
**Background & Concern (sample policy, Tier-2).** The AWS-published "Permissions for EC2 Fleet users" policy prints `{"Effect":"Allow","Action":["ec2:*"],"Resource":"*"}` plus `iam:PassRole` scoped by a **role-name wildcard** `arn:aws:iam::123456789012:role/DevTeam*` — a name-prefix, not an `iam:PassedToService` condition. An org copying it verbatim that later creates any `DevTeam*`-named role (e.g. `DevTeamBreakGlassAdmin`) lets a fleet user pass that unrelated role into a launch template. **Oracle:** attach the policy verbatim to a scoped test principal; `CreateFleet` with a launch template referencing a coincidentally-prefixed high-priv role; success = the AWS-modeled pattern enforces only name-prefix, not intent. (Distinct from the SLR-side `Resource:"*"` PassRole fact owned by the prerequisites/create-spot-fleet siblings.) **Severity:** Medium, in scope (AWS-authored sample).
**Background & Concern (weighting, self-inflicted).** `ec2-fleet-instance-weighting`: "If the result isn't an integer, the fleet **rounds it up** … the fleet can select any pool … **even if the capacity of the instances launched exceeds the requested target capacity**." No stated ceiling on the overshoot ratio. `MaxTotalPrice` (`ec2-fleet-control-spending`) is only demonstrated on *unweighted* examples; its interaction with weight-rounding is undocumented. The `Priority` override field is **shared** across Spot and On-Demand selection ("the same priority is also applied to your On-Demand Instances if the On-Demand allocation strategy is set to `prioritized`").
**High-level Test Scenarios.** (i) small `TotalTargetCapacity` + large mutually-prime `WeightedCapacity` under `diversified` → overshoot ratio ≫1 while spec-compliant (Oracle: `DescribeFleetInstances` unit sum vs target). (ii) weight-rounding batch that exceeds `MaxTotalPrice` in a single launch — does the cap block, overshoot once, or error? (iii) a `Priority` set for Spot silently reorders On-Demand. **Severity:** Low–Medium, **self-inflicted single-account cost footgun → §7 out-of-scope** unless a lower-priv user sets weight under a budget/SCP sized on a 1:1 capacity-to-instance assumption.
**Doc evidence:** `ec2-fleet-prerequisites`, `ec2-fleet-instance-weighting`, `ec2-fleet-control-spending`, `ec2-fleet-allocation-strategy`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Consume a CR never shared to caller | `CreateFleet`/`RunInstances` + CR | Server-side RAM-share check (no IAM resource-level backstop — Area 2/8) |
| Cancel/Modify a CR outside caller's own CR Fleet | CR-Fleet SLR policy | `ArnLike ec2:CapacityReservationFleet=crf-*` (presence-not-ownership — Area 1) |
| Read foreign CR attributes/usage with only the ID | Describe/Get CR actions | "Consumers can only view total+available"; unscopable Describe (Area 6) |
| Force-terminate borrower across accounts | `Update…Allocation` reclaim / org-leave | 2-min EventBridge warning (reclaim); "eventually terminated" (org-leave, no notice — Area 3) |
| Shift/grow cost onto a consented billing owner | `Associate/AcceptCapacityReservationBillingOwner` | 12h mutual-consent accept; auto-revoke on org-leave/unshare (Area 5) |
| Transitive consume via CR group indirection | `resource-groups:GroupResources` + group-target launch | RAM share of members; group ARN has no EC2 condition keys (Area 7) |
| Exhaust owner's On-Demand quota via shared-CR usage | Service Quotas | Usage counts to owner's limit (documented coupling — Area 7) |
| Guardrail "no interruptible / only my Org" | `CreateFleet`/`RunInstances` IAM | Keys absent on launch actions; no `aws:*OrgID` in EC2 (Area 8) |
| Pass an unintended `DevTeam*` role | sample user policy | role-name-prefix wildcard, not `iam:PassedToService` (Area 9) |
| Weighting overshoot / MaxTotalPrice bypass | instance weighting | round-up by design; cap only demoed unweighted (Area 9) |

---

## 7. Out-of-Scope Risk Categories (state confidently to keep the hunter off documented design)
- **Any behavior that requires the owner's own RAM share first** ("trust-abuse-after-share"): Capacity-Block FCFS owner starvation (Area 4), interruptible reclaim as such (Area 3 base capability), owner-quota coupling (Area 7) — these are **documented design**. Report only a *missing safeguard* (missing reclaim notice on org-leave, bypassable billing accept, consume-*without*-a-share).
- **Self-inflicted single-account cost footguns:** instance-weighting overshoot, MaxTotalPrice edge, shared-`Priority` coupling (Area 9) — in scope only if a lower-privileged principal can trigger them under a budget/SCP/quota the operator sized on a false 1:1 assumption.
- **Customer-authored IAM** (the operator's own fleet policy) — only AWS-authored artifacts (Areas 1, 9-sample) are reportable.
- **CR brute-force / ID enumeration** at 17-hex entropy — not feasible; assume IDs leak via CloudTrail/tags/config, don't model guessing.
- **Shared tenancy / dedicated-host / Outposts / Local-Zone CR variants**, UltraServer Capacity Blocks (non-shareable), and the Spot-Fleet twin surface — deferred to their own pages.
- **IMDS on fleet-launched instances, SLR launch condition-key non-propagation, PassRole/confused-deputy, cancel/terminate internals, the auto-scaling loop** — owned by the sibling plans (`ec2-fleet`, `spot-fleet-prerequisites`, `create-spot-fleet`, `delete-fleet`, `modify-*`, scaling family).
- **AWS service plane** — hard stop, not a target.

## 8. Null hypotheses / doc gaps (lenses checked, pages named)
- **No `aws:PrincipalOrgID`/`aws:ResourceOrgID`/`…OrgPaths` anywhere in EC2** — grepped full `list_ec2.md`, zero matches. Org-scope is RAM/SCP-only, never a resource-level EC2 condition (Area 8). *Confirmed, not a gap — it's the finding.*
- **No `ec2:CapacityReservationId`/`InstanceMatchCriteria`/`IsInterruptible` key on `CreateFleet`/`RunInstances`** — confirmed from the detailed per-action rows (CreateFleet ~5115, RunInstances ~9586). *Confirmed.*
- **Re-validation cadence of the RAM-share check at launch (create-time-only vs continuous)** — doc gap; `capacity-reservation-sharing` has no unshare/running-instance section (only Capacity Block documents the "running instances continue to 30-min-pre-expiry" behavior). Area 2/7 need a live test to settle.
- **Error class on targeting an unrelated CR** (`AccessDenied` vs `…NotFound` vs silent on-demand fallback) — unspecified in the two walkthroughs; settles Area 2's existence-oracle.
- **Org-leave termination event + timing** — `monitor-interruptible-cr` documents only two events; the org-leave "eventually terminated" path has no documented event/notice (Area 3).
- **Billing-accept fail-closed behavior & whether post-accept capacity growth re-consents** — `assign-billing` implies no re-consent; confirm live (Area 5).
- **Doc-vs-doc:** interruptible-CRs-in-groups contradiction (Area 7) — must be resolved before investing in the interruptible branch of the priority lens.
- **Lenses that did not fire (pages read):** SSRF/G (no server-side-fetch field in any tutorial, prereq, allocation, sharing, or group page); Q upload (none); K prompt-injection (no LLM/agent); W attestation, Y transport, FF/token, DD cache, CC upstream-context, BB canonicalization (no HTTP router/authorizer/parser surface in these doc pages) — all N/A for this documentation set, re-open if a console/API path with those shapes is found.

---
*Companion to the 18 existing fleet/spot-fleet plans in this directory. Owns the Capacity-Reservation
consumption + instance-weighting surface of `fleet-tutorials.html`; cross-references siblings for SLR
launch, PassRole, cancel/terminate, scaling, and monitoring depth it deliberately does not restate.*
