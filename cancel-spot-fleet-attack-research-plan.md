# EC2 Spot Fleet — Cancel (`CancelSpotFleetRequests`) Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-spot-fleet.html` ("Cancel (delete) a Spot Fleet request"; markdown twin: append `.md`).
**Source of leads:** that page + its API/IAM neighborhood — `AWSEC2/latest/APIReference/API_CancelSpotFleetRequests.html` (+ `API_CancelSpotFleetRequestsSuccessItem`, `API_CancelSpotFleetRequestsErrorItem`), `delete-fleet.html` (the EC2-Fleet twin, for the gate asymmetry), `spot-fleet-states.html`, `work-with-spot-fleets.html`, `spot-fleet-prerequisites.html`, `ExamplePolicies_EC2.html`, `how-ec2-instance-termination-works.html`, the EC2 **Service Authorization Reference** (`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`), and the AWS-managed policy `AWSEC2SpotFleetServiceRolePolicy`. Offline mirror root: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/*.md`.
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on `cancel-spot-fleet` + API/IAM references, plus one parallel documentation-only deep-analysis subagent (terminate-authorization asymmetry vs `DeleteFleets`; On-Demand termination + SLR condition; sample-policy terminate coverage). **Subagent confirmations folded in:** (1) the caller-side `ec2:TerminateInstances` gate is **absent across the entire Spot Fleet doc neighborhood** (not merely unstated on one page); (2) the SLR terminate statement JSON (`Resource:"*"`, `StringLike aws:ec2spot:fleet-request-id:"*"`) verbatim; (3) `list_ec2.md` CancelSpotFleetRequests = `spot-fleet-request*` only, no `instance` type; (4) AWS's operator sample policy grants `ec2:CancelSpotFleetRequests` on `*` but **omits `ec2:TerminateInstances`** → the recommended-default principal already has the §5.1 shape. The one thing docs cannot settle (so it's a live test, not a confirmed finding): whether the service enforces a caller terminate check at runtime despite documenting none.
**Online twins cross-checked:** the local mirror did **not** contain `cancel-spot-fleet.md` (local-sync gap); the target page and `API_CancelSpotFleetRequests` were read from the **online** `.md`/`.html` twins. `list_ec2.md` read offline and used as authoritative over User-Guide prose.

> **Relationship to the sibling plans (this plan COMPLEMENTS, does not duplicate).**
> - `spot-fleet-states-attack-research-plan.md` owns the **lifecycle/state-machine** surface — `cancelled_running`/`cancelled_terminating` orphan completeness (SF-9/SF-10), KMS-grant survival (SF-8), 48-h forensic decay (SF-11/SF-12), cross-team cancel *reach* via the `Resource:"*"` sample policy (SF-2), the per-ID cancel response as a state oracle (SF-15), and the modify/cancel TOCTOU (SF-13). **Those are cross-referenced here as [states SF-x] and not re-derived.**
> - `delete-fleet-attack-research-plan.md` owns the **EC2 Fleet** (`DeleteFleets`) twin, including its **documented caller-side `ec2:TerminateInstances` gate** and that gate's granularity question. Cross-referenced as [delete §x].
> - `spot-fleet-prerequisites-attack-research-plan.md`/`spot-fleet-attack-research-plan.md` own the **PassRole / confused-deputy / IAM-artifact privesc** depth.
>
> **What THIS plan uniquely owns:** the **cancel-with-terminate operation as the Spot Fleet family's irreversible data-destruction primitive**, and specifically the **authorization asymmetry** between `CancelSpotFleetRequests` (whose target page documents **no** caller-side `ec2:TerminateInstances` requirement) and `DeleteFleets` (whose page explicitly documents one). The headline question — *can a holder of only `ec2:CancelSpotFleetRequests` irreversibly terminate every instance in a fleet, including On-Demand instances, with no termination permission?* — is this plan's reason to exist.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the §5 priority order; look left and right for adjacent bugs.
- **Prefer the safe oracle first.** The authorization leads are confirmable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`, read-only `iam:GetPolicyVersion` / `iam:GetRole`, and read-only `ec2 describe-spot-fleet-*` **before** any live resource is created or cancelled.
- **`CancelSpotFleetRequests --terminate-instances` is IRREVERSIBLE** (target page `Warning`: *"Terminating an instance is permanent and irreversible … All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted … All data stored on instance store volumes is permanently lost."*). Any **live** confirmation of a *destructive* claim is performed **only against a throwaway canary Spot Fleet** whose instances hold no real data, and is torn down immediately. Prefer `--dry-run` (IAM-only) and `SimulatePrincipalPolicy` first — but note the **DryRun caveat** below.
- **DryRun caveat (confirmed from the API ref):** `DryRun` on `CancelSpotFleetRequests` checks **IAM permission only** (`DryRunOperation` vs `UnauthorizedOperation`) — it is evaluated **before** resource resolution and **cannot** surface a state/ownership/termination-gate result. So DryRun is *not* an ownership oracle and *cannot* refute the §5.1 terminate-gate question; that one requires a real call against a synthetic canary fleet (the call does not mutate if the service rejects it).
- **HARD STOP:** this service runs entirely inside the caller's own account. The only AWS-service-plane identity in scope is the service-linked role **`AWSServiceRoleForEC2SpotFleet`** (service principal `spotfleet.amazonaws.com`), which performs the actual `TerminateInstances` on the cancel's behalf. Treat it **read-only** (`GetPolicyVersion`, `GetRole`). The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. **Terminate-without-terminate-permission (the P0).** As a principal holding **only `ec2:CancelSpotFleetRequests`** (scoped to a fleet, and provably **not holding** `ec2:TerminateInstances`), call `CancelSpotFleetRequests --terminate-instances` and show that **all** of the fleet's instances — **On-Demand and Spot** — are irreversibly terminated (EBS `DeleteOnTermination` volumes + instance-store data destroyed) with the attacker never holding `ec2:TerminateInstances`. **This is not a contrived principal:** AWS's own published operator sample policy (`spot-fleet-prerequisites.html`) grants `ec2:CancelSpotFleetRequests` on `Resource:"*"` and **never grants `ec2:TerminateInstances`** (confirmed), so the *recommended default* Spot-Fleet operator already holds exactly this combination. The cancel-spot-fleet page — and the entire Spot Fleet doc neighborhood — documents **no** caller-side terminate check (contrast `delete-fleet.html`, which explicitly requires and troubleshoots one) → the question is whether that gate is **absent** at runtime.
2. **Twin-path parity break.** Demonstrate that the Spot Fleet family offers **≥3 doors to terminate a fleet's instances** with **different gates**: direct `ec2:TerminateInstances` (per-instance scoped), `ModifySpotFleetRequest(ExcessCapacityTerminationPolicy=default, ↓TargetCapacity)` ([states SF-5] / [modify-spot-fleet §], no caller terminate check), and `CancelSpotFleetRequests --terminate-instances`. An org that locked down `ec2:TerminateInstances` has not locked down termination.
3. **On-Demand destruction via a "Spot" cancel.** Confirm the SLR's tag-presence termination condition (`aws:ec2spot:fleet-request-id`) covers the **On-Demand** instances the fleet launched, so a cancel-with-terminate destroys On-Demand workloads too — surprising to an operator who thinks "Spot Fleet = Spot only."
4. **Batch cancel-and-destroy across teams.** Using the ≤100-ID batch and the per-ID success/unsuccess split, show a holder of AWS's `Resource:"*"` operator sample policy can cancel-and-terminate **multiple other teams'** production fleets in one call, and read the per-ID state transitions as an existence/state oracle ([states SF-2]/[states SF-15], extended here to the *destructive* consequence).
5. **Default-to-terminate footgun.** Confirm that `TerminateInstances` — though `Required: Yes` in the API — **defaults to terminate** in the User-Guide/CLI framing, so an omitted/mis-defaulted client silently destroys instances; map how SDKs surface this.
6. Resolve the load-bearing **doc-gaps** that gate the above (presence/absence of the caller terminate check; On-Demand tag coverage; per-ID error check-ordering; CloudTrail record shape for the terminated instance IDs).

---

## 2. Components, Assets, and Design

**What `CancelSpotFleetRequests` is.** A console-supported, CLI/API, **Write-level, mutating, batch** control-plane call (`aws ec2 cancel-spot-fleet-requests`, PowerShell `Stop-EC2SpotFleetRequest`) that cancels (deletes) one or more Spot Fleet **requests** and — governed by a **required** boolean — optionally terminates every instance each fleet launched. It is part of a *legacy* API family ("Spot Fleet uses a legacy API with no planned investment … use EC2 Fleet or an Auto Scaling group instead").

**Inputs (API ref, verbatim):**
- `SpotFleetRequestId.N` — **Required**, array of strings, **up to 100 IDs** per call.
- `TerminateInstances` — **Required: Yes**, Boolean. *"Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances. To let the instances continue to run after the Spot Fleet request is canceled, specify `no-terminate-instances`."* (CLI surfaces this as `--terminate-instances` / `--no-terminate-instances`.)
- `DryRun` — Optional, Boolean (IAM-only check; see §0 caveat).
- **No** `Context`/reserved field on this action (that lives on `RequestSpotFleet`/`ModifySpotFleetRequest`).

**Behavioral facts (cancel-spot-fleet.html + API ref + spot-fleet-states):**
- Cancel → **all Spot requests associated with the fleet are canceled**, so no new Spot Instances launch (stated unconditionally, including the no-terminate path).
- `--terminate-instances` (the default) → request enters **`cancelled_terminating`**; **both On-Demand and Spot** instances terminate. **Permanent & irreversible** — EBS `DeleteOnTermination` volumes and all instance-store data destroyed.
- `--no-terminate-instances` → request enters **`cancelled_running`**; instances **continue to run** until interrupted or **manually** terminated (orphan surface — owned by [states SF-9/SF-10]).
- Terminal **`cancelled`** state: the request is **deleted two days (48 h) after its instances are terminated** (forensic-decay surface — owned by [states SF-11/SF-12]).
- **Restriction:** up to **100 fleets per request**; *"If you exceed the specified number, no fleets are canceled."* (batch-atomic count check precedes per-fleet processing).

**Outputs (API ref):** per-fleet split — `successfulFleetRequestSet` (`CancelSpotFleetRequestsSuccessItem`: `spotFleetRequestId`, `currentSpotFleetRequestState`, `previousSpotFleetRequestState`) and `unsuccessfulFleetRequestSet` (`CancelSpotFleetRequestsErrorItem`). Plus `requestId`. Example success transition: `previous=active → current=cancelled_terminating`.

**Who actually terminates.** The terminations are performed by the service-linked role **`AWSServiceRoleForEC2SpotFleet`** (AWS-managed policy `AWSEC2SpotFleetServiceRolePolicy`). Its terminate statement, **confirmed verbatim** from the managed-policy reference:
```json
{
  "Effect": "Allow",
  "Action": [ "ec2:TerminateInstances" ],
  "Resource": "*",
  "Condition": { "StringLike": { "ec2:ResourceTag/aws:ec2spot:fleet-request-id": "*" } }
}
```
i.e. `Resource:"*"` gated **only** by *presence* of the `aws:ec2spot:fleet-request-id` tag (any value matches — tag-**key presence**, value-agnostic; [states SF-9]). The SLR is **service plane — read-only / hard stop.** The open question (§5.1) is whether `CancelSpotFleetRequests` layers a **caller-side `ec2:TerminateInstances` check** on top (as `DeleteFleets` documents) or **not** — the subagent found no such check documented anywhere in the Spot Fleet doc tree.

**Identity / assets.**
- Spot Fleet request ID `sfr-` + 8-4-4-4-12 hex (UUIDv4-shaped, ~122-bit, non-enumerable → Lens A cross-account null, §8); ARN `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}`; **account-scoped**.
- The terminated instances' EBS `DeleteOnTermination` volumes + instance-store data — the destroyed assets. On-Demand **and** Spot.
- `AWSServiceRoleForEC2SpotFleet` — service plane (read-only, hard stop).

**IAM facts for `ec2:CancelSpotFleetRequests` (Service Authorization Reference, `list_ec2.md` line ~4966–4970 — authoritative):**
- Access level **Write**; required resource type **`spot-fleet-request*`** (ARN `…:spot-fleet-request/${SpotFleetRequestId}`).
- Condition keys: **only** `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Region`.
- **No `instance` resource type** → the `ec2:CancelSpotFleetRequests` IAM entry **cannot natively express** "this call may terminate only these specific instance ARNs/tags." Any per-instance termination scoping would have to come from a *separate* action-level `ec2:TerminateInstances` check layered on top — which the cancel page never mentions (§5.1).
- Contrast `ec2:TerminateInstances` (`list_ec2.md` line ~4525): required resource type **`instance*`** with per-instance condition keys (`ec2:InstanceID`, `ec2:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:InstanceType`, …). It is *designed* to be scoped per-instance; the question is whether the cancel path honors any of it.

**ASCII — CancelSpotFleetRequests as a destructive primitive:**
```
 Caller (holds ec2:CancelSpotFleetRequests on spot-fleet-request/*;
         ec2:TerminateInstances = DENIED / not held ??? )
     │
     │  CancelSpotFleetRequests(SpotFleetRequestId.N = [≤100],
     │     TerminateInstances = true  ──►  is there ANY caller-side ec2:TerminateInstances check?
     │                                      cancel-spot-fleet.html = SILENT (contrast delete-fleet.html, which REQUIRES it)
     │                                      = DOC-GAP / headline §5.1
     │                        = false ──►  cancelled_running; Spot reqs canceled; instances orphaned [states SF-9/10])
     ▼
 Spot Fleet control plane ──(active → cancelled_terminating | cancelled_running → cancelled ──48h──► DELETED [states SF-11])
     │  assumes
     ▼
 AWSServiceRoleForEC2SpotFleet (SLR) ──TerminateInstances on Resource:"*",
     │                                   Condition StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id : "*"
     │                                   (tag-key PRESENCE, value-agnostic — [states SF-9])
     ▼
 EC2 instances in caller's account  —— BOTH On-Demand AND Spot ("These include both …") ——►
                                      ├─ EBS (DeleteOnTermination) → PERMANENTLY DELETED
                                      └─ instance-store data        → PERMANENTLY LOST
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Holder of `ec2:CancelSpotFleetRequests`, **denied/lacking `ec2:TerminateInstances`** | A fleet's instances (On-Demand + Spot) + their EBS/instance-store data | `CancelSpotFleetRequests --terminate-instances` → SLR issues `TerminateInstances` **unconditioned on the caller's instance scope** | Instances the caller could **not** `TerminateInstances` directly are terminated / their data destroyed — terminate laundered through the SLR with **no** terminate permission (§5.1) |
| Holder whose `ec2:TerminateInstances` is **tag/ID/AZ-scoped** | Fleet instances **outside** that scope | same cancel-with-terminate path | Out-of-scope instances die anyway (coarse or absent gate — §5.1 variant) |
| Operator with AWS `Resource:"*"` sample policy (team A) | Team B's `sfr-` fleets' running instances (same account) | batch `CancelSpotFleetRequests --terminate-instances` naming ≤100 foreign fleet IDs | Multiple other teams' fleets reach `cancelled_terminating`; their instances/data destroyed in one call (§5.4; reach confirmed by [states SF-2]) |
| Any caller who thinks "Spot Fleet = Spot" | The fleet's **On-Demand** instances | the SLR's tag-presence terminate condition applied to On-Demand instances too | On-Demand (non-interruptible, often stateful) instances terminated by a "Spot Fleet" cancel (§5.3) |
| Under-privileged (ABAC/tag-scoped) principal | Existence + state of fleets its tag condition should hide | per-ID `successful`/`unsuccessful` split + state transitions in the cancel response | A differential per-ID result reveals a fleet exists / its prior state where "denied" should look like "not found" ([states SF-15]; destructive-batch variant §5.4) |
| Any caller canceling with `--terminate` | The audit trail | SLR-attributed `TerminateInstances`; cancel response carries no instance-ID list | Destructive termination whose terminated-instance IDs are not in the `CancelSpotFleetRequests` CloudTrail record (§5.6) |

**Hard-stop boundary:** any customer surface ↔ AWS's own service plane (the SLR's live credentials). Read-only only (`GetPolicyVersion`, `GetRole`).

---

## 4. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `CancelSpotFleetRequests` | yes (Write) | external | Cancel ≤100 Spot Fleet requests; **required** `TerminateInstances` boolean (default = terminate) | yes (SigV4) | principal with `ec2:CancelSpotFleetRequests` on `spot-fleet-request*` | **Prime target.** `spot-fleet-request*` + `aws:/ec2:ResourceTag`,`ec2:Region` **only**; **no `instance` resource type**. Page documents **no** caller-side `ec2:TerminateInstances` requirement (§5.1). Batch, per-fleet partial-success. Irreversible. |
| caller `ec2:TerminateInstances` check (hypothesized) | — (authz gate) | internal | Does cancel-with-terminate require the caller to hold `ec2:TerminateInstances`? | — | caller | **Documented for `DeleteFleets`, NOT for `CancelSpotFleetRequests`.** Presence/absence = top doc-gap §5.1. |
| SLR terminate (internal) | yes | internal | `TerminateInstances` the SLR performs on the cancel's behalf | no | `spotfleet.amazonaws.com` only | Service plane — **read-only / hard stop.** Condition keys on tag-key *presence*, value-agnostic ([states SF-9]). |
| `ModifySpotFleetRequest` | yes | external | Twin terminate path (`ExcessCapacityTerminationPolicy=default`, ↓capacity) that routes **around** any terminate check | yes | caller | [states SF-5] / [modify-spot-fleet §] — the asymmetry that makes §5.2 a parity question. |
| `DescribeSpotFleetRequests` / `…Instances` / `…RequestHistory` | no | external | Read fleet config/instances/events — recon + the **safe** oracle (§5.4) | yes | caller | Account-scoped; `DescribeSpotFleetRequests` is **unscopable** by resource/tag ([states SF-1]). |

**Doc-planted leads kept verbatim:**
- cancel-spot-fleet.html: *"When you cancel a Spot Fleet request, you must also specify if you want to terminate all of its instances. **These include both On-Demand Instances and Spot Instances.**"* → §5.3.
- cancel-spot-fleet.html / API ref: *"The default is to terminate the instances."* (with `TerminateInstances` nonetheless `Required: Yes`) → §5.5.
- cancel-spot-fleet.html: *"you can cancel up to 100 fleets in a single request. If you exceed the specified number, no fleets are canceled."* → batch-atomic (§5.4).
- **Absence worth citing:** cancel-spot-fleet.html + API_CancelSpotFleetRequests have **no** `UnauthorizedOperation`/`ec2:TerminateInstances` troubleshooting note — unlike delete-fleet.html, which explicitly does. The *absence* is the §5.1 lead.

---

## 5. Recommended Areas of Focus (priority order)

Priority = (terminate-without-terminate-permission, §5.1) > (twin-path parity, §5.2) > (On-Demand destruction, §5.3) > (batch cross-team destroy + oracle, §5.4) > (default-to-terminate footgun, §5.5) > (audit coverage, §5.6).

### 5.1 Does `CancelSpotFleetRequests --terminate-instances` require the caller to hold `ec2:TerminateInstances`? — **P0 (headline doc-gap)**
**Background:** `DeleteFleets` (the EC2 Fleet twin) **documents** a caller-side `ec2:TerminateInstances` check — delete-fleet.html returns `UnauthorizedOperation` and tells you to add `ec2:TerminateInstances` when deleting a fleet that *must* terminate ([delete §5.1]). The Spot Fleet cancel path documents **no such requirement anywhere** — confirmed by sweeping `cancel-spot-fleet.html`, `API_CancelSpotFleetRequests`, `work-with-spot-fleets.html`, `spot-fleet-prerequisites.html`, and `ExamplePolicies_EC2.html` (online twins verbatim-matched): `ec2:TerminateInstances` is **never** listed as a caller permission for cancel, and the API ref carries only the generic `DryRun`/`UnauthorizedOperation` boilerplate every EC2 action has. Yet the operation is explicitly irreversible and destroys On-Demand + Spot instances. The `ec2:CancelSpotFleetRequests` IAM entry has **only** `spot-fleet-request*` + `aws:/ec2:ResourceTag` + `ec2:Region` condition keys (confirmed `list_ec2.md`) — **no `instance` resource type** — so it structurally **cannot** carry per-instance scoping; the actual terminate is issued by the SLR, which holds `ec2:TerminateInstances` on `Resource:"*"` gated only by tag-key *presence* (confirmed JSON in §2; [states SF-9]). **Crucially, AWS's own operator sample policy grants `ec2:CancelSpotFleetRequests` on `Resource:"*"` and omits `ec2:TerminateInstances` entirely** — so the recommended-default principal has the exact "cancel-anything, terminate-nothing-directly" shape this lead exploits; a verbatim copy of AWS's guidance does **not** mute the lead, it *creates* the vulnerable principal.
**Security Concern (Lens X / S / U — twin-path authorization parity + doc-vs-enforcement):** If the cancel path performs **no** caller-side `ec2:TerminateInstances` check, then a principal holding **only `ec2:CancelSpotFleetRequests`** — even one **explicitly denied** `ec2:TerminateInstances` — can trigger **permanent, irreversible termination** (EBS `DeleteOnTermination` + instance-store destruction) of **every** instance in the fleet via the SLR. The one permission that nominally governs instance destruction is bypassed entirely. This is the Spot Fleet analogue of [delete §5.1], but *worse*: DeleteFleets at least documents a gate (granularity-questionable); CancelSpotFleetRequests appears to document **none**.
**High-level Test Scenarios:**
- Safe first: `SimulatePrincipalPolicy`/`SimulateCustomPolicy` — construct a principal with `Allow ec2:CancelSpotFleetRequests` on a fleet ARN and an **explicit `Deny ec2:TerminateInstances`** on `*`. This proves the *standalone* IAM evaluation only; it **cannot** reveal whether the service layers its own check (DryRun won't either — §0 caveat).
- Canary (synthetic, disposable instances only, in an account you are authorized to test): one `maintain` or `request` Spot Fleet with throwaway instances holding no real data; test principal as above (`CancelSpotFleetRequests` allowed, `TerminateInstances` **denied**); call `cancel-spot-fleet-requests --terminate-instances`; **observe whether the instances actually terminate.** Instances dying = **gate absent → breach confirmed**. `UnauthorizedOperation`/instances surviving = gate present (refuted). Stop the instant a non-synthetic instance would be destroyed.
- Variant: repeat with `ec2:TerminateInstances` **tag-scoped** to a tag the fleet's instances lack → do they still die? (coarse-gate variant, mirrors [delete §5.1]).
**Doc evidence:** cancel-spot-fleet.html (Warning + "must also specify if you want to terminate"; **no** terminate-permission note); `API_CancelSpotFleetRequests` (only generic `DryRun`/`UnauthorizedOperation` boilerplate, no `ec2:TerminateInstances` requirement); `spot-fleet-prerequisites.html` sample policy (grants `ec2:CancelSpotFleetRequests` on `*`, omits `ec2:TerminateInstances` — confirmed); `list_ec2.md` (CancelSpotFleetRequests `spot-fleet-request*`-only, no `instance` type; TerminateInstances `instance*` per-instance keys); `AWSEC2SpotFleetServiceRolePolicy` (SLR terminate on `*`, tag-presence condition — confirmed JSON §2); delete-fleet.html (the twin that **does** document the gate). **Severity-if-true:** **High** (irreversible destruction of instances/data the caller has no IAM authorization to terminate; the governing permission bypassed, by a principal AWS's own sample policy produces). Drops to Informational only if a caller-side check *is* enforced at runtime (nowhere documented → the single remaining thing to test). The documentation/sample-policy half is **AWS-authored and copy-verbatim** → in scope per the Lens R/S carve-out regardless; route `aws-security`. **Stop condition:** `SimulateCustomPolicy` first; canary/synthetic instances only; stop before any out-of-scope/real instance is terminated.

### 5.2 Terminate-path parity across `CancelSpotFleetRequests`, `ModifySpotFleetRequest`, and direct `TerminateInstances` — **P1 (Lens X)**
**Background:** Three doors can terminate a Spot Fleet's instances with potentially three different gates: (1) direct `ec2:TerminateInstances` (per-instance scoped by design), (2) `ModifySpotFleetRequest(ExcessCapacityTerminationPolicy=default, ↓TargetCapacity or →0)` — no documented caller terminate check ([states SF-5], [modify-spot-fleet §]), (3) `CancelSpotFleetRequests --terminate-instances` (§5.1). This is the classic twin-path parity surface, now spanning the Spot Fleet lifecycle.
**Security Concern:** An org that believes it has locked down termination by scoping/denying `ec2:TerminateInstances` has **three** doors with **three** gates; the weakest wins. Modify ignores the check; Cancel may too (§5.1). Document the full matrix so a defender's "I denied `TerminateInstances`" assumption is tested against every door, including the Spot-request-cancel side effect (every door also cancels the fleet's Spot requests, preventing relaunch).
**High-level Test Scenarios:** For a principal denied/scoped on `ec2:TerminateInstances`, attempt the same instance termination via (1) direct `TerminateInstances` (expect Deny), (2) `ModifySpotFleetRequest(→0, default)`, (3) `CancelSpotFleetRequests --terminate-instances`. Any door succeeding where (1) fails is a parity breach. Record which permission each door *actually* requires. Canary instances only.
**Doc evidence:** cancel-spot-fleet.html; [states SF-5]; [modify-spot-fleet §]; `list_ec2.md` (neither Modify nor Cancel carries an `instance` resource type). **Severity-if-true:** **High** (non-uniform control over the account's most destructive EC2 operation across equivalent paths). **Stop condition:** canary instances only.

### 5.3 "Spot Fleet" cancel terminates **On-Demand** instances — SLR tag-presence condition coverage — **P1 (Lens S / U)**
**Background:** cancel-spot-fleet.html states plainly that cancel-with-terminate terminates *"both On-Demand Instances and Spot Instances."* The SLR performs the terminate under `Condition: StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id : "*"` — a tag-**key-presence** gate ([states SF-9]). For this to reach On-Demand instances, those instances must also carry the `aws:ec2spot:fleet-request-id` tag.
**Security Concern:** (a) **Scope surprise** — an operator who reasons "it's a *Spot* Fleet, cancel only kills interruptible Spot capacity" is wrong; stateful On-Demand workloads in the same fleet are destroyed too, compounding §5.1's missing gate. (b) **Condition semantics** — because the SLR condition is value-agnostic (matches *any* `aws:ec2spot:fleet-request-id` value), the "who may terminate these" authority does **not** depend on the owning fleet still existing; any instance ever launched by *any* Spot Fleet carries a terminable marker (links to the [states SF-9] persistence/tag-inheritance lead and the reserved-tag-settability question).
**High-level Test Scenarios:** Read-only — resolve `AWSEC2SpotFleetServiceRolePolicy` via `iam:GetPolicyVersion`; confirm the `TerminateInstances` statement's `Resource` and value-agnostic condition. On a canary fleet mixing On-Demand + Spot, `describe-tags` to confirm **On-Demand** instances carry `aws:ec2spot:fleet-request-id`; then (chained to §5.1 canary) confirm a cancel-with-terminate destroys the On-Demand ones. Probe whether a *user* can set the reserved `aws:`-prefixed tag on an arbitrary instance (expect denied/ignored for reserved prefix — if not, a victim-instance-marking primitive, [states SF-9]).
**Doc evidence:** cancel-spot-fleet.html ("both On-Demand Instances and Spot Instances"); `AWSEC2SpotFleetServiceRolePolicy`; EC2 `id_tags`/tag-your-resources pages (On-Demand tagging). **Severity-if-true:** **Medium–High** (destruction of non-interruptible/stateful On-Demand workloads via a path the operator under-estimates; condition is value-agnostic). **Stop condition:** read-only policy/tag inspection; canary only for the destructive confirmation.

### 5.4 Batch cross-team cancel-and-destroy + per-ID state oracle — **P2 (Lens A / X)**
**Background:** `CancelSpotFleetRequests` takes up to **100** fleet IDs and returns a **per-ID** `successful`/`unsuccessful` split with `current`/`previousSpotFleetRequestState`. [states SF-2] already confirms AWS's `Resource:"*"` operator sample policy lets any operator cancel **any** fleet in the account; [states SF-15] already flags the per-ID response as a low-severity state oracle. **This plan's distinct extension:** the *destructive* consequence of combining the two — a single batch call can **cancel-and-terminate dozens of other teams' production fleets at once**, and the `previousSpotFleetRequestState` returned per ID is a confirmed existence/prior-state disclosure for fleets an ABAC policy meant to hide.
**Security Concern:** Under AWS's account-wide sample policy, the batch turns "I can cancel one fleet" into "I can irreversibly destroy the running capacity of up to 100 fleets across every team in the account in one API call," with the response doubling as a reconnaissance oracle (which IDs were real/active). The "exceed → none canceled" rule is **batch-atomic** (count check precedes per-fleet authz), so it is not itself a count-overflow oracle, but the per-ID `previousSpotFleetRequestState` is a state oracle.
**High-level Test Scenarios:** Safe first — read-only `DescribeSpotFleetRequests` (unscopable, [states SF-1]) to enumerate account fleet IDs + states; `SimulatePrincipalPolicy` to confirm the sample policy allows `CancelSpotFleetRequests` against foreign fleet ARNs. For the oracle: a `--dry-run` mixed batch tests only the auth branch; a real per-ID split (canary IDs only) reveals whether `unsuccessful` codes distinguish *not-found* vs *unauthorized* vs *wrong-state*. **Do not** cancel a real foreign fleet. **Cross-account = genuine null:** `sfr-` IDs are ~122-bit UUIDs, account-scoped resolution (§8).
**Doc evidence:** cancel-spot-fleet.html batch restriction; `API_CancelSpotFleetRequests` per-ID response shape; [states SF-2]/[states SF-15]; `list_ec2.md`. **Severity-if-true:** **High** for the destructive cross-team batch (intra-account, mass irreversible capacity loss); **Low–Medium** for the enumeration oracle alone. **Stop condition:** `DescribeSpotFleetRequests` recon + simulate only; no live cancel against non-owned IDs.

### 5.5 Default-to-terminate footgun — required-but-defaulted `TerminateInstances` — **P3 (Lens U — doc-vs-SDK)**
**Background:** The API marks `TerminateInstances` **`Required: Yes`**, but the User-Guide and CLI framing say *"The default is to terminate the instances."* The CLI exposes `--terminate-instances` / `--no-terminate-instances`; the console pre-selects the "Terminate instances" checkbox.
**Security Concern:** A "required" field whose documented default is the **destructive** choice is a safety footgun: an operator or automation that omits/mis-handles the flag (or an SDK that defaults it) destroys instances when they meant to merely cancel the request and keep the instances running. The destructive outcome is the path of least resistance / the default UI state. (Owner-to-fix is largely API/SDK/UX design; flagged as a hygiene/anti-footgun observation, not a boundary breach.)
**High-level Test Scenarios:** Read-only — diff how each SDK (Boto3 `terminate_instances`, Java, Go v2, .NET) treats the "required" boolean when the caller omits it (SDK validation error vs implicit default), and confirm the console's default checkbox state. No live cancel needed to characterize the footgun.
**Doc evidence:** cancel-spot-fleet.html (console checkbox default + CLI examples); `API_CancelSpotFleetRequests` (`Required: Yes` + "default is to terminate"). **Severity-if-true:** **Low / Informational** (destructive-default UX; amplifies §5.1/§5.3 impact when the gate is weak). **Owner-to-fix:** AWS (API/SDK/console UX).

### 5.6 Audit coverage of the terminated instance IDs — **P3 (Lens O — enabler)**
**Background:** The `CancelSpotFleetRequests` **response** (`CancelSpotFleetRequestsSuccessItem`) contains only `spotFleetRequestId` + the fleet-state transition — **no terminated-instance-ID list**. The actual terminate is issued by the SLR via `spotfleet.amazonaws.com`. CloudTrail logs the `CancelSpotFleetRequests` **call** as a management event, but whether its `responseElements`/`requestParameters` carry the destroyed instance IDs (vs requiring a correlated SLR-attributed `TerminateInstances` event, joined only by `spotFleetRequestId`) is undocumented — and [states SF-11] shows the `sfr-id` join key purges at 48 h.
**Security Concern:** A destructive cancel-with-terminate may leave the specific destroyed instances **unattributed** in the primary CloudTrail record; combined with [states SF-11/SF-12]'s 48-h request+history purge, EC2-native reconstruction of "which instances did this cancel destroy, and who launched them" decays on the attacker's clock. Raises the severity of §5.1–§5.4 as an evasion enabler.
**High-level Test Scenarios:** Canary — cancel a canary fleet `--terminate-instances`; inspect the CloudTrail `CancelSpotFleetRequests` `responseElements` for instance IDs; check for a correlated `TerminateInstances` event with `userIdentity.invokedBy = spotfleet.amazonaws.com` carrying them; confirm the `spotFleetRequestId` join key persists only until the 48-h purge. Read-only on the logs.
**Doc evidence:** `API_CancelSpotFleetRequestsSuccessItem`; `monitor-with-cloudtrail` (service-principal attribution); [states SF-11/SF-12]. **Severity-if-true:** **Low / Informational** standalone; **Medium** as a §5.1–§5.4 enabler (destructive action with decaying attribution).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Irreversibly terminate a fleet's instances holding **only** `ec2:CancelSpotFleetRequests` (no terminate perm) | cancel terminate path vs SLR terminate | **None documented** — unlike `DeleteFleets`, the cancel page states no caller `ec2:TerminateInstances` requirement (§5.1) |
| Non-uniform terminate control across Cancel / ModifySpotFleetRequest / direct TerminateInstances | twin-path parity | Per-instance `ec2:TerminateInstances` on the direct path only; absent on Modify; undocumented on Cancel |
| Destroy **On-Demand** workloads via a "Spot" cancel | SLR tag-presence terminate condition | Value-agnostic `aws:ec2spot:fleet-request-id` presence; "both On-Demand and Spot" stated but under-appreciated |
| Mass cross-team destruction + state oracle in one batch | ≤100-ID batch + per-ID state split | AWS `Resource:"*"` sample policy ([states SF-2]); batch-atomic count check; `sfr-` scoping available but unused |
| Cross-account fleet-ID enumeration | `SpotFleetRequestId.N` | ~122-bit UUID + account-scoped resolution (**genuine null**) |
| Destructive-default footgun | required-but-defaulted `TerminateInstances` | API `Required: Yes` but "default is to terminate"; console pre-checks terminate |
| Destructive action with decaying instance-ID attribution | cancel response + SLR attribution + 48-h purge | CloudTrail (customer-configured); join key purges at 48 h ([states SF-11]) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant / cross-account IDOR on fleets or instances** — N/A: a fleet, its instances, and the SLR all live in the caller's own account; `SpotFleetRequestId.N` resolves only in the caller's account; `sfr-` IDs are ~122-bit UUIDs (non-fabricable). All leads here are **intra-account cross-team**.
- **AWS service-plane / SLR live credentials** — hard stop; read-only (`GetPolicyVersion`, `GetRole`) only. The SLR performs the actual terminate; do not exercise it.
- **The `cancelled_running` orphan surface** (instances still running / still tagged / still load-balanced after `--no-terminate`), the **KMS-grant survival**, and the **48-h forensic decay** — owned by `spot-fleet-states-attack-research-plan.md` ([states SF-8/SF-9/SF-10/SF-11/SF-12]); cross-referenced, not re-derived here. This plan is the **cancel-WITH-terminate / destruction** companion; the states plan is the **cancel-WITHOUT-terminate / orphan** companion.
- **IAM-artifact privilege escalation, PassRole/confused-deputy, scaling-guardrail bypass, CloudWatch-alarm tampering, quota-exhaustion DoS** — owned by the prerequisites/states/broad Spot Fleet plans; not re-scoped here.
- **Single-tenant self-DoS** a caller inflicts on *their own* fully-owned fleet with blanket perms — out of scope, **except** where a principal that provably **lacks or is scoped out of** `ec2:TerminateInstances` achieves destruction (§5.1/§5.2/§5.3) or across-team destruction (§5.4).
- **Customer-authored** over-broad policies — a footgun. The **AWS-published operator sample policy** and the **AWS-managed SLR policy** are copy-verbatim / uneditable → in scope per the Lens R carve-out.
- **SSRF, wire-protocol/translation injection, prompt injection, attestation gating, canonicalization/parser-differential, cache-key divergence, trusted-header injection, JWT/token validation, KMS encryption-context confusion, predictable-name land-grab** — N/A for this SigV4 control-plane cancel API (see §8).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, pages checked)

- **Lens A (cross-account IDOR / enumeration):** cross-account = **GENUINE NULL** — `sfr-` IDs are `sfr-`+~122-bit UUID, no account qualifier, resolved in the caller's own account (checked `cancel-spot-fleet.md`, `API_CancelSpotFleetRequests.md`, [states SF-1/§8]). The *intra-account* per-ID state oracle **does** fire → §5.4. `DryRun` is caller-IAM-only, **not** an ownership oracle (§0).
- **Lens C (credential vending / STS session scope):** null — no session-policy/ProvidedContext/per-tenant role vending on the cancel path; the only role is the SLR. Pages: `API_CancelSpotFleetRequests`, `spot-fleet-prerequisites`.
- **Lens D / V (data-plane→control-plane / network segmentation):** null — no service-owned fleet, no control/storage ENI, no multi-tenant subnet. Pages: `work-with-spot-fleets`, `cancel-spot-fleet`.
- **Lens F (translation/wire-protocol injection):** N/A — cancel inputs are an array of opaque IDs + a boolean + optional boolean; no free-text/query language or parser. Pages: `API_CancelSpotFleetRequests`, CLI reference.
- **Lens G (SSRF):** N/A — no URL/URI/webhook/callback field the cancel path dereferences. Pages: `cancel-spot-fleet.md`, `API_CancelSpotFleetRequests.md`.
- **Lens H (KMS / encryption-context):** not reachable *through cancel* — any CMK interaction is on the launch side; the grant-survival lead on cancel lives in [states SF-8].
- **Lens EE (predictable-name land-grab):** N/A — `sfr-` IDs are opaque UUIDs, account-scoped; no global/predictable namespace.
- **Lenses K / W / BB / CC / DD / FF (prompt-injection / attestation / canonicalization / trusted-header / cache-key / token-validation):** N/A — no LLM/agent, no enclave/`kms:RecipientAttestation`, no authorizer/WAF/CDN/cache layer, no JWT/OIDC in front of this SigV4 control-plane API.
- **Lens M (shared-identifier interception):** null — `sfr-` always paired with SigV4; no presigned/one-time token. Pages: `API_CancelSpotFleetRequests`.
- **Lens O (audit):** **fires** — the cancel response carries no instance-ID list + SLR attribution + 48-h purge → §5.6.
- **Lens AA (revocation completeness):** the *cancel-without-terminate* orphan/revocation surface **fires but is owned by [states SF-9/SF-10]**; cross-referenced, not re-derived.

**Load-bearing doc-gaps to resolve before calling anything confirmed:**
1. **(Blocks §5.1 — top priority)** Does `CancelSpotFleetRequests --terminate-instances` perform **any** caller-side `ec2:TerminateInstances` authorization check? The cancel page + API ref document **none** (contrast delete-fleet.html, which does). Must be tested against a synthetic canary fleet (DryRun is IAM-only and cannot answer this).
2. **(Blocks §5.3)** Do **On-Demand** instances launched by a Spot Fleet carry the `aws:ec2spot:fleet-request-id` tag, so the SLR's tag-presence terminate condition covers them? And is that reserved tag user-settable on arbitrary instances?
3. **(Blocks §5.4)** The per-ID `unsuccessfulFleetRequestSet` error-code set and check ordering for `CancelSpotFleetRequests` (not enumerated in the API ref — only `successful`/`unsuccessful` shapes are) — determines the oracle's leak size.
4. **(Blocks §5.6)** CloudTrail `CancelSpotFleetRequests` record shape — does it carry the terminated instance IDs, or only the fleet-state transition (requiring a correlated SLR `TerminateInstances` event joined by `spotFleetRequestId`)?
5. **(Service-plane / read-only)** Confirm the exact `AWSEC2SpotFleetServiceRolePolicy` `TerminateInstances` statement (Resource + value-agnostic condition) via `iam:GetPolicyVersion`; **do not** exercise the SLR.

---

### Kill-chain candidates (rate at the end of the chain)
- **§5.4 (hold AWS `Resource:"*"` operator sample policy)** → **§5.1** (cancel-with-terminate needs no `ec2:TerminateInstances`) → **§5.3** (On-Demand + Spot both destroyed) → **§5.6** (terminated-instance IDs decay from EC2-native audit at 48 h) = **mass, irreversible, cross-team destruction of running capacity and data with no termination permission and decaying attribution.** **End severity: High** (account-wide destruction + evasion; capped below Critical only because it is intra-account, not cross-tenant).
- **Recon** (`DescribeSpotFleetRequests`, unscopable — [states SF-1]) → map every team's fleets + instance tags → **§5.1/§5.4** targeted cancel-with-terminate of the highest-value fleets. **End severity: High.**

---

*End of plan. Downstream hunter (`aws-vuln-hunter`): start with §5.1 — the single question "does cancel-with-terminate require `ec2:TerminateInstances`?" is the headline, confirmable first with `SimulateCustomPolicy` (standalone IAM) and `GetPolicyVersion` (SLR policy), then with ONE synthetic canary fleet (DryRun cannot answer it). Read `spot-fleet-states-attack-research-plan.md` for the orphan/KMS/forensic siblings and `delete-fleet-attack-research-plan.md` for the EC2-Fleet twin's documented gate. Use `list_ec2.md` (not `list_amazonec2.html`) for the IAM reference.*
