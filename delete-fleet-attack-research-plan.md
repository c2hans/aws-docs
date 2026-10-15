# Delete an EC2 Fleet (`DeleteFleets`) — Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-fleet.html` (markdown twin: append `.md`).
**Source of leads:** that page + its API/IAM neighborhood — `AWSEC2/latest/APIReference/API_DeleteFleets.html` (+ `API_DeleteFleetError`, `API_DeleteFleetSuccessItem`), `EC2-fleet-states.html`, `instant-fleet.html`, `fleet-quotas.html`, `tag-ec2-fleet.html`, `monitor-ec2-fleet-using-eventbridge.html`, `monitor-with-cloudtrail.html`, `how-ec2-instance-termination-works.html`, `ec2-fleet-prerequisites.html`, `spot-fleet-prerequisites.html`, `ExamplePolicies_EC2.html`, and the EC2 **Service Authorization Reference** (mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`). Offline mirror root: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/*.md`. Online `.md`/`.html` twins cross-checked (the target page and `API_DeleteFleets` were byte-identical online vs. local — no sync gap).
**Status:** Documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** This is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on `delete-fleet` + API/IAM references, plus 2 parallel deep-analysis subagents (DeleteFleets authorization & the TerminateInstances-check semantics; enumeration-oracle + orphaned-instance lifecycle + audit).
**Scope note:** This plan is **narrowed to the `DeleteFleets` operation**. It is a companion to:
- `/work/aws-docs/ec2-fleet-attack-research-plan.md` (parent — launch-template late-binding/PassRole, the AWS-authored sample IAM policy, the KMS grant, capacity-reservation sharing), and
- `/work/aws-docs/modify-ec2-fleet-attack-research-plan.md` (sibling — `ModifyFleet` as a launch/terminate primitive, console-hidden `LaunchTemplateConfig`).

Where a DeleteFleets lead feeds those, it is cross-referenced as **[parent §x]** / **[modify §x]**. A hunter should read §2–§4 here first, then the parent plan for the KMS/capacity-reservation and sample-policy context.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in the §5 priority order; look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Every IAM lead is confirmable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` and read-only `aws ec2 describe-fleets` / `iam:GetPolicyVersion` **before** any live resource is created or deleted. Any live confirmation uses only synthetic canary fleets/launch-templates/instances and tears them down immediately. **`DeleteFleets` is irreversible** — live confirmation of a *destructive* claim is performed only against a throwaway canary fleet whose instances hold no real data, never a real workload, and `DescribeFleets` (read-only, reversible) is always preferred over a live `DeleteFleets` probe.
- **HARD STOP:** DeleteFleets runs almost entirely *inside the caller's own account*. The one AWS-service-plane identity in scope is the service-linked role **`AWSServiceRoleForEC2Fleet`** — which performs the actual `TerminateInstances` on DeleteFleets' behalf. Treat it as **read-only** (`GetPolicyVersion`, `GetRole`). The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**
- **Why `DeleteFleets` specifically is worth a plan of its own:** it is the service's **destructive / data-destroying primitive** (the page's own `Warning`: *"Terminating an instance is permanent and irreversible … All attached Amazon EBS volumes … are also permanently deleted … All data stored on instance store volumes is permanently lost."*). Two things make it security-interesting beyond "it deletes a fleet": (a) **unlike `ModifyFleet`, DeleteFleets performs a documented secondary `ec2:TerminateInstances` authorization check on the caller** — the one API in this family that *does* gate termination — so the question becomes whether that gate is **scoped per-instance or coarse**, and whether its non-terminating sibling path routes around it; and (b) it is a **batch API** (up to 125 fleet IDs) with a **per-fleet partial-success/error model** (`SuccessfulFleetDeletions` / `UnsuccessfulFleetDeletions` with 7 distinct error codes) — an enumeration-oracle shape.

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. **Scoped-grant → out-of-scope destruction (the P0).** As a principal whose `ec2:TerminateInstances` is **tag/ID/AZ-scoped** (the exact pattern AWS's own `ExamplePolicies_EC2` recommends) plus unscoped `ec2:DeleteFleets`, call `DeleteFleets --terminate-instances` on a fleet containing instances **outside** that scope and show the SLR terminates them anyway — i.e. the documented `ec2:TerminateInstances` gate is a coarse "do you hold the action" check, not a per-instance one, and the SLR laundering lets a narrow grant destroy instances the caller could not `TerminateInstances` directly.
2. **Silent decommission without `TerminateInstances` (Lens X).** As a principal holding **only `ec2:DeleteFleets`** (explicitly **denied** `ec2:TerminateInstances`), delete a `maintain`/`request` fleet with `--no-terminate-instances`: cancel all its Spot requests and detach it from its self-healing logic, orphaning its running (billable) instances — availability/cost impact with none of the permission that nominally governs termination.
3. **Enumeration / ABAC existence-&-state leak.** Using the batch per-fleet error model, show that an under-privileged (tag-scoped) principal can distinguish `fleetIdDoesNotExist` vs `UnauthorizedOperation` vs `fleetNotInDeletableState` to learn the **existence and lifecycle state** of fleets its ABAC policy was meant to hide — and pin down the **check ordering** that bounds how much leaks.
4. **Orphan-strand governance bypass (Lens AA).** Delete a `maintain` fleet `--no-terminate-instances` and show its instances escape fleet-scoped automation/tagging/EventBridge while continuing to run, bill, and (per `fleet-quotas`) consume the per-Region fleet quota — with degraded post-`deleted` attribution.
5. **Audit blind spot (Lens O).** Confirm that deleting an `instant` fleet emits **no EventBridge event at all**, and resolve whether the CloudTrail `DeleteFleets` record carries the **terminated instance IDs** or only the fleet-state transition.
6. Resolve the load-bearing **doc-gaps** that gate the above (TerminateInstances-check granularity; error-code check-ordering; >1000-instance partial-state; CloudTrail record shape).

---

## 2. Components, Assets, and Design

**What DeleteFleets is.** `DeleteFleets` (`aws ec2 delete-fleets`, PowerShell `Remove-EC2Fleet`) is a **CLI/API-only, Write-level, mutating, batch** control-plane call that deletes one or more EC2 Fleet *requests* and optionally terminates their instances. Two **required** inputs: `FleetId.N` (array of fleet IDs) and `TerminateInstances` (boolean — `--terminate-instances` is the default; `--no-terminate-instances` is supported **only** for `maintain`/`request`, never `instant`). Optional `DryRun`.

**Behavioral facts (delete-fleet.html + API ref + EC2-fleet-states):**
- Delete → **all associated Spot requests are canceled** so no new Spot Instances launch (stated unconditionally, including for the `--no-terminate` path).
- `--terminate-instances` → fleet enters **`deleted_terminating`**; instances (On-Demand **and** Spot) terminate. **Permanent & irreversible** — EBS `DeleteOnTermination` volumes and all instance-store data are destroyed.
- `--no-terminate-instances` → fleet enters **`deleted_running`**; instances keep running until interrupted or **manually** terminated. `deleted_running` **does not apply to `instant` fleets.**
- Terminal **`deleted`** state is reached **two days after** instances terminate; the request object then ceases to be a live managed object.
- **`instant` fleets must terminate on delete.** For `instant` fleets with **>1000 instances** the deletion request **"might fail"**; guidance is to manually terminate down to ≤1000 first.

**Batch / restriction facts:** up to **25 `instant`**, up to **100 `maintain`/`request`**, up to **125 total** per request; **if you exceed, no fleets are deleted** (batch-atomic quota check). Results split into per-fleet `SuccessfulFleetDeletions` (`DeleteFleetSuccessItem`: `fleetId`, `currentFleetState`, `previousFleetState`) and `UnsuccessfulFleetDeletions` (`DeleteFleetErrorItem`: `fleetId`, `Error.{Code,Message}`).

**Error codes (delete-fleet troubleshooting + API ref):** `ExceededInstantFleetNumForDeletion`, `fleetIdDoesNotExist`, `fleetIdMalformed`, `fleetNotInDeletableState`, `NoTerminateInstancesNotSupported`, `UnauthorizedOperation`, `unexpectedError`. *(Note: `API_DeleteFleetError.md` lists only 4 of the 7 as valid values — a stale/incomplete enum; the troubleshooting examples show the other two returned in the same per-fleet `Error.Code` shape. → §8 doc-gap.)*

**Who actually acts.** The terminations DeleteFleets triggers are performed by the service-linked role **`AWSServiceRoleForEC2Fleet`** (documented grants include `ec2:TerminateInstances`, `ec2:RunInstances`, `ec2:CreateTags`, several `Describe*`) — **but**, uniquely in this API family, DeleteFleets first performs a **caller-side `ec2:TerminateInstances` authorization check** (see §5.1). The SLR identity is service plane — **read-only / hard stop.**

**Identity / assets.**
- Fleet ID — ARN `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}`; **account-scoped**; the `FleetId` is `fleet-` + a **canonical 128-bit UUID** (8-4-4-4-12 hex), high-entropy and non-fabricable (→ Lens A null, §8).
- Fleet type (`instant` / `request` / `maintain`) — governs both the batch cap bucket and whether `--no-terminate` is legal.
- The terminated instances' EBS volumes (`DeleteOnTermination`) and instance-store data — the destroyed assets.
- `AWSServiceRoleForEC2Fleet` — service plane (read-only, hard stop).

**IAM facts for `ec2:DeleteFleets` (Service Authorization Reference, mirror `list_ec2.md` line 5884):**
- Access level **Write**; required resource type **`fleet*`** (ARN `…:fleet/${FleetId}`).
- Condition keys: **only** `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Region`.
- **No `instance` resource type** → DeleteFleets' own IAM entry cannot natively express "this call touches these specific instance ARNs." The termination gate is therefore an *action-level* check layered on top (§5.1), not expressible via DeleteFleets' resource/condition surface.
- Contrast — `ec2:TerminateInstances`: required resource type **`instance*`**, with per-instance condition keys (`ec2:InstanceID`, `ec2:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, …). It is *designed* to be scoped per-instance; the open question is whether DeleteFleets honors that scoping.

**ASCII — DeleteFleets as a destructive primitive:**
```
 Caller (holds ec2:DeleteFleets on fleet/*; ec2:TerminateInstances = scoped? denied? ec2:*?)
     │
     │  DeleteFleets(FleetId.N = [up to 125],
     │     TerminateInstances = true  ──► documented secondary caller check: ec2:TerminateInstances
     │                                      (coarse "has action" OR per-instance scoped?  = DOC-GAP §5.1)
     │                        = false ──► NO terminate check; Spot requests still canceled; instances orphaned)
     ▼
 EC2 Fleet control plane ──(active → deleted_terminating | deleted_running → deleted[+2 days])
     │  assumes
     ▼
 AWSServiceRoleForEC2Fleet (SLR) ──TerminateInstances (UNCONDITIONED on the SLR side)──►  EC2 instances in caller's account
                                                                                   │
                                                                                   ├─ EBS (DeleteOnTermination) → PERMANENTLY DELETED
                                                                                   └─ instance-store data        → PERMANENTLY LOST
 (instant fleets: no EventBridge event emitted at all → audit blind spot §5.7)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Holder of `ec2:DeleteFleets` whose `ec2:TerminateInstances` is **tag/ID/AZ-scoped** | Fleet instances **outside** that scope (their EBS/instance-store data) | `DeleteFleets --terminate-instances` → SLR issues `TerminateInstances` **unconditioned** | Instances the caller could not `TerminateInstances` directly are terminated / their data destroyed (scoped grant laundered through the SLR) |
| Holder of `ec2:DeleteFleets`, **denied `ec2:TerminateInstances`** | A `maintain`/`request` fleet's running instances + all its Spot requests | `DeleteFleets --no-terminate-instances` (gate only fires on the *terminating* path) | Spot requests canceled + instances orphaned (`deleted_running`) with the caller holding **no** terminate permission |
| Under-privileged (ABAC-scoped) principal in the account | Existence + lifecycle state of fleets its tag condition should hide | Batch `DeleteFleets`/`DryRun` per-fleet error codes (`fleetIdDoesNotExist` vs `UnauthorizedOperation` vs `fleetNotInDeletableState`) | A differential error reveals a fleet exists / its state, where "denied" should look like "does not exist" |
| Holder of `ec2:DeleteFleets` on `Resource:"*"` | Every `maintain`/`request`/`instant` fleet in the account | DeleteFleets carries only `fleet*` + `aws:/ec2:ResourceTag` + `ec2:Region` | A DeleteFleets against a fleet the holder does not "own"/tag succeeds (account-wide destructive reach from a wildcard grant) |
| Operator choosing `--no-terminate` | Fleet-scoped governance (Capacity Rebalance, maintain-replenishment, EventBridge, tag-based control, quota) | Fleet request deleted while instances persist | Instances continue running/billing but are no longer governed/attributable to any fleet; still consume the per-Region fleet quota |
| Any caller deleting an `instant` fleet | The audit trail | `instant` fleets emit **no** EventBridge events; CloudTrail record shape for terminated instance IDs unconfirmed | A destructive termination with no fleet-level event record and (possibly) no instance-ID attribution in the DeleteFleets CloudTrail entry |

**Hard-stop boundary:** any customer surface ↔ AWS's own service plane (the SLR's live credentials). Read-only only (`GetPolicyVersion`, `GetRole`).

---

## 4. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `DeleteFleets` | yes (Write) | external | Delete ≤125 fleet requests; optionally terminate instances | yes (SigV4) | principal with `ec2:DeleteFleets` (+ `ec2:TerminateInstances` for the terminating path) | **Prime target.** `fleet*` resource type + `aws:/ec2:ResourceTag`,`ec2:Region` **only**; **no `instance` resource type**. Batch, per-fleet partial-success, 7 error codes. Irreversible. |
| `TerminateInstances` (caller check inside DeleteFleets) | — (authz check) | internal gate | Documented secondary check: caller must hold `ec2:TerminateInstances` to delete a fleet that **must** terminate | — | caller | **Granularity unknown** — coarse vs per-instance (§5.1, top doc-gap). delete-fleet.html promises "the following example" of the fix policy that **is missing from the page**. |
| SLR terminate (internal) | yes | internal | `TerminateInstances` the SLR performs on DeleteFleets' behalf | no | `ec2.amazonaws.com` only | Service plane — **read-only / hard stop.** Whether its own terminate is internally conditioned to fleet-owned instances is a doc-gap. |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeFleetHistory` | no | external | Read fleet state/instances/events — recon + the **safe** enumeration-oracle probe (§5.4) | yes | caller | Account-scoped. Post-`deleted` queryability unconfirmed (§8). |
| `ModifyFleet` | yes | external | Twin terminate path that routes **around** the `ec2:TerminateInstances` check | yes | caller | **[modify §5.1]** — the asymmetry that makes §5.1/§5.2 a parity question. |
| `CancelSpotInstanceRequests` (implied) | yes | internal | DeleteFleets cancels associated Spot requests | — | caller/SLR | Whether a caller-side `ec2:CancelSpotInstanceRequests` check fires on `--no-terminate` is a doc-gap (§5.2). |

**Doc-planted leads kept verbatim:**
- delete-fleet.html: *"If you do not have permission to terminate instances, you get the `UnauthorizedOperation` error when deleting a fleet **that must terminate its instances** … you must add the `ec2:TerminateInstances` action to the IAM policy, **as shown in the following example.**"* — **the example does not exist on the page** (confirmed online + offline). AWS points at the gate but never shows its intended scope.
- `monitor-ec2-fleet-using-eventbridge.html`: *"Only fleets of type `maintain` and `request` emit events. Fleets of type `instant` do not emit events."*
- `fleet-quotas.html`: fleets in `deleted_running` still count against the per-Region `maintain`/`request` fleet quota; `deleted_terminating` does not.

---

## 5. Recommended Areas of Focus (priority order)

Priority = (SLR-laundered destruction of out-of-scope instances) > (silent decommission without terminate right) > (RunInstances/terminate-control parity vs ModifyFleet) > (enumeration/ABAC leak) > (orphan-strand governance) > (DoS / audit / sample-policy).

### 5.1 Does the `ec2:TerminateInstances` gate scope per-instance, or coarsely? — SLR-laundered out-of-scope destruction — **P0 (top doc-gap)**
**Background:** DeleteFleets is the one API in this family that performs a documented caller-side `ec2:TerminateInstances` check (delete-fleet.html `UnauthorizedOperation` troubleshooting). But DeleteFleets' own IAM entry has **no `instance` resource type**, and the actual terminate is issued by the SLR, which holds `ec2:TerminateInstances` **unconditioned**. `ExamplePolicies_EC2.html` ships AWS's canonical **tag-scoped** `TerminateInstances` pattern (`Resource: instance/*`, `Condition: aws:ResourceTag/purpose = test`) as a recommended real-world shape.
**Security Concern (Lens S / U / X — doc-vs-enforcement):** If DeleteFleets' gate is a **coarse** "does this principal hold `ec2:TerminateInstances` at all" check (not evaluated against the specific instance ARNs/tags in the fleet), then a caller whose `TerminateInstances` is tag/ID/AZ-scoped to only *their* instances can trigger termination — **permanent EBS/instance-store destruction** — of fleet instances **outside** that scope, laundered through the SLR. The missing "following example" on delete-fleet.html means AWS never states the intended Resource/Condition shape of the gate, so operators cannot even tell what they granted.
**High-level Test Scenarios:**
- Safe: `SimulateCustomPolicy` — grant `ec2:TerminateInstances` with `Condition {StringEquals: ec2:ResourceTag/owner = team-a}` + unscoped `ec2:DeleteFleets` on `fleet*`. Simulate `ec2:TerminateInstances` in a context where `ec2:ResourceTag/owner = team-b` → expect `implicitDeny`. This proves only the *standalone* IAM evaluation, **not** DeleteFleets' server-side behavior.
- Canary (synthetic, disposable instances only): one `maintain` fleet whose instances carry **mixed** tags (`owner=team-a` and `owner=team-b`); test principal's `TerminateInstances` scoped to `owner=team-a`; call `DeleteFleets --terminate-instances`; **diff which instances actually terminate vs. the grant's tag scope.** team-b instances dying = breach (coarse gate). Stop the instant a non-synthetic/out-of-scope instance would be destroyed.
**Doc evidence:** delete-fleet.html `UnauthorizedOperation` section (+ missing example); `list_ec2.md` (DeleteFleets `fleet*`-only vs TerminateInstances `instance*` per-instance keys); `ExamplePolicies_EC2.html` tag-scoped terminate; `ec2-fleet-prerequisites.html` (SLR holds unconditioned `TerminateInstances`). **Severity-if-true:** **High** (irreversible destruction of instances the caller has no direct IAM authorization to terminate; data loss). Drops to informational if the gate *does* re-check per instance (plausible but nowhere stated). **Stop condition:** canary/synthetic only; read-only `SimulateCustomPolicy` first; stop before any out-of-scope instance is actually terminated.

### 5.2 Silent decommission: orphan + Spot-cancel with **no** `ec2:TerminateInstances` — **P1**
**Background:** The `UnauthorizedOperation`/`ec2:TerminateInstances` gate fires **only** "when deleting a fleet **that must terminate its instances**." The `--no-terminate-instances` path on a `maintain`/`request` fleet is therefore **not** gated by it, yet it still (per delete-fleet.html, unconditionally) **cancels all the fleet's Spot requests** and deletes the fleet request, leaving instances in `deleted_running`.
**Security Concern (Lens X / E — privilege-granularity gap):** A principal holding **only `ec2:DeleteFleets`** (explicitly denied `ec2:TerminateInstances`) can unilaterally (a) cancel all pending Spot capacity and (b) detach the fleet from its self-healing `maintain` logic — a "silent decommission" / availability-and-cost-abuse primitive that bypasses the one authorization control AWS documents for this API. Mirror of **[modify §5.1]** (ModifyFleet triggers terminate with no caller `TerminateInstances`) but via the *delete* door and the Spot-cancel side effect.
**High-level Test Scenarios:** `SimulatePrincipalPolicy` → confirm principal is `ALLOW ec2:DeleteFleets` on the fleet ARN, `DENY ec2:TerminateInstances`. Canary `maintain` fleet with a live Spot request → as that principal, `DeleteFleets --no-terminate-instances` → confirm the fleet reaches `deleted_running`, the Spot request is canceled, and the instances keep running. **Resolve the doc-gap:** does a caller-side `ec2:CancelSpotInstanceRequests` check fire on this path (it is not documented)? If absent, the Spot-cancel is a second un-gated destructive side effect.
**Doc evidence:** delete-fleet.html (Spot cancel unconditional; `UnauthorizedOperation` scoped to must-terminate); `EC2-fleet-states.html` `deleted_running`. **Severity-if-true:** **Medium** (availability/cost; no data destruction, but a confused-deputy-adjacent decommission with a permission that doesn't look like a terminate/cancel permission). **Stop condition:** one canary fleet; never a real workload.

### 5.3 `RunInstances`/terminate-control parity between DeleteFleets, ModifyFleet, and direct calls — **P1**
**Background:** Three paths can terminate a fleet's instances: direct `ec2:TerminateInstances` (fully gated, per-instance), `ModifyFleet(↓capacity, termination)` (**no** caller terminate check — [modify §5.1]), and `DeleteFleets --terminate-instances` (coarse caller terminate check — §5.1). This is a classic twin-path parity surface.
**Security Concern (Lens X):** An org that believes it has locked down instance termination by scoping/denying `ec2:TerminateInstances` has **three** doors with **three different gates**. The weakest wins: `ModifyFleet` ignores the check entirely, and DeleteFleets' check may be coarse (§5.1). Document the full matrix so a defender's "I denied TerminateInstances" assumption is tested against every door.
**High-level Test Scenarios:** For a principal denied/scoped on `ec2:TerminateInstances`, attempt the same instance termination via (1) direct `TerminateInstances` (expect Deny), (2) `ModifyFleet(↓,termination)`, (3) `DeleteFleets --terminate-instances`. Any door that succeeds where (1) fails is a parity breach. Compare with the `--no-terminate` orphan door (§5.2).
**Doc evidence:** delete-fleet.html; [modify §5.1]; `list_ec2.md` (neither ModifyFleet nor DeleteFleets carries an `instance` resource type). **Severity-if-true:** **High** (governance control over the account's most destructive EC2 operation is non-uniform across equivalent paths). **Stop condition:** canary instances only.

### 5.4 Batch per-fleet error model → intra-account existence/state enumeration oracle — **P2**
**Background:** DeleteFleets returns **per-fleet** results. The 7 error codes are *differently triggered*: `fleetIdMalformed` (syntactic, pre-lookup), `fleetIdDoesNotExist` (well-formed, not in caller's account/region), `fleetNotInDeletableState` (real, visible/authorized fleet in a non-deletable state), `UnauthorizedOperation` (real, deletable fleet the caller lacks terminate rights for). The `ExceededInstantFleetNumForDeletion` "no fleets deleted" rule is **batch-atomic** (count/type-classify precedes per-fleet authz); the other codes appear to be evaluated per-fleet.
**Security Concern (Lens A — differential-error oracle, intra-account):** Where an org scopes `ec2:DeleteFleets`/`ec2:TerminateInstances` by **tag (ABAC)**, an under-privileged principal can distinguish *doesn't exist* from *exists-but-unauthorized* from *exists-wrong-state* — leaking the **existence and lifecycle state** of fleets its policy was meant to hide ("deny should look like not-found"). The leak size depends entirely on **check ordering** (does the state check fire before or after the authz check?) — undocumented.
**Cross-account = GENUINE NULL:** fleet IDs are `fleet-` + a **128-bit UUID** (non-fabricable), the ID carries no account qualifier, and EC2 resolves IDs against the **caller's own account** — a foreign/guessed ID returns `fleetIdDoesNotExist`, never a cross-account signal. Same null class the parent plan recorded for `cr-` IDs, with even higher entropy. `DryRun` is a **caller-IAM-only** check (returns `DryRunOperation`/`UnauthorizedOperation` before resource resolution) → **not** an ownership/existence oracle.
**High-level Test Scenarios:** **Safe first** — use read-only `DescribeFleets` on a batch mixing an owned ID, a wrong-state fleet, and a syntactically-valid-but-absent ID; compare per-ID visibility/codes. Then two ABAC principals (tag matches / doesn't) against the same fleet ID → does the non-matching principal get `UnauthorizedOperation` (existence proof) vs `fleetIdDoesNotExist`? Determine the check order (malformed → exists → state → authz?).
**Doc evidence:** delete-fleet.html troubleshooting; `API_DeleteFleetError.md` (+ its **incomplete** 4-of-7 enum, §8); `tag-ec2-fleet.html`; `API_DeleteFleets.md` DryRun. **Severity-if-true:** **Low–Medium** (intra-account confidentiality leak of resource existence/state across tag-isolated principals; no direct delete/terminate without the tag). **Stop condition:** `DescribeFleets` recon only; no live `DeleteFleets` against non-owned IDs.

### 5.5 Orphan-strand governance loss via `--no-terminate-instances` — **P2 (Lens AA — revocation completeness)**
**Background:** `--no-terminate` deletes the fleet request but leaves instances running (`deleted_running`) and cancels Spot requests. Fleet-scoped mechanisms (Capacity Rebalance, maintain-replenishment, EventBridge fleet events, fleet-tag-based IAM control) are tied to the now-deleted request. `tag-ec2-fleet.html`: fleet-request tags are **not** auto-propagated to instances — so unless the launch template explicitly tagged them, orphaned instances carry **no breadcrumb** back to the deleted fleet. `fleet-quotas.html`: `deleted_running` fleets still consume the per-Region fleet quota.
**Security Concern:** Deleting a fleet `--no-terminate` is a way to **strand instances outside fleet governance** while they keep running and billing: they dodge fleet-tag-scoped controls, lose automated rebalancing/replenishment, and (after the 2-day `deleted` cleanup) may lose queryable fleet attribution entirely (`DescribeFleetInstances`/`History` post-`deleted` retention is undocumented — §8). An insider could use this to detach workload from monitoring/control that keys on the fleet.
**High-level Test Scenarios:** Canary `maintain` fleet with no fleet-ID-referencing launch-template tags → `DeleteFleets --no-terminate` → (a) can `DescribeFleetInstances`/`History` still resolve the fleet after `deleted`? (b) do the orphaned instances carry any fleet reference? (c) do fleet-tag-scoped IAM controls still reach them? Confirm continued billing via Cost Explorer attribution.
**Doc evidence:** `EC2-fleet-states.html`; `tag-ec2-fleet.html`; `fleet-quotas.html`; `describe-ec2-fleet.html`. **Severity-if-true:** **Medium** (self-contained governance/operational-hygiene drift; single-account, no cross-tenant exposure).

### 5.6 `instant`-fleet >1000-instance deletion partial/undefined state — **P3 (Lens L — self-DoS)**
**Background:** For `instant` fleets with >1000 instances the deletion "might fail." No doc states whether the failure is atomic or leaves a **partial state** (some instances terminated, request stuck), nor which error code is returned (`unexpectedError` inferred, unconfirmed). `deleted_running` explicitly does **not** apply to `instant` fleets, so a partially-failed delete could leave the fleet in a state the documented state machine does not describe.
**Security Concern:** A self-inflicted availability/consistency bug — resources that can neither be cleanly deleted nor cleanly identified as active. Single-account, so rated as self-DoS / operational drift, not a boundary breach.
**High-level Test Scenarios:** (expensive — >1000 synthetic instances) delete and inspect `UnsuccessfulFleetDeletions.Error.Code`, whether `SuccessfulFleetDeletions` is simultaneously populated for the same ID (partial processing), and idempotency of the ≤1000-then-retry remediation.
**Doc evidence:** delete-fleet.html / `API_DeleteFleets.md` ">1000 instances" paragraph; `EC2-fleet-states.html`; `instant-fleet.html`. **Severity-if-true:** **Medium** (self-DoS / undefined-state) — provisioning cost makes this low-ROI; prioritize behind the authz leads. **Stop condition:** do not provision production-scale fleets; synthetic micro-instances only, or defer.

### 5.7 Audit blind spot: `instant` delete emits no EventBridge event; CloudTrail instance-ID coverage unconfirmed — **P3 (Lens O — enabler)**
**Background:** `monitor-ec2-fleet-using-eventbridge.html`: *"Only fleets of type `maintain` and `request` emit events. Fleets of type `instant` do not emit events."* (unconditional — applies to the delete/terminate path). Even `maintain`/`request` events are "best effort." `monitor-with-cloudtrail.html` logs all EC2 API actions as management events, so the `DeleteFleets` **call** is captured — but the DeleteFleets **response** shape (`DeleteFleetSuccessItem`) contains only `fleetId`+state transition, **no terminated-instance-ID list**. So the specific instances destroyed may **not** appear in the DeleteFleets CloudTrail record.
**Security Concern:** Deleting an `instant` fleet (the only fleet-driven path to terminate its instances) leaves **no fleet-level event** and (pending the CloudTrail-shape doc-gap) possibly no instance-ID attribution — a destructive action with a weak audit trail. Raises the severity of §5.1/§5.3 as an evasion enabler. `instant` is also what EMR/Auto Scaling use internally (parent plan).
**High-level Test Scenarios:** delete a canary `instant` fleet → confirm **zero** `aws.ec2fleet` EventBridge events. Delete a canary `maintain` fleet `--terminate-instances` → inspect the CloudTrail `DeleteFleets` `responseElements` for instance IDs; check whether a correlated `TerminateInstances` event (with `invokedBy`/`calledVia` = the fleet service) carries them.
**Doc evidence:** `monitor-ec2-fleet-using-eventbridge.html`; `monitor-with-cloudtrail.html`; `API_DeleteFleetSuccessItem.md`. **Severity-if-true:** **Medium** (confirmed EventBridge blind spot) → **Low/Informational** as a standalone issue, higher as a §5.1/§5.3 enabler.

### 5.8 AWS-authored sample-policy audit — `ec2:*`/`*` bundles DeleteFleets + TerminateInstances — **P3 (Lens R — root cause)**
**Background:** `ec2-fleet-prerequisites.html` "Permissions for EC2 Fleet users" ships `{"Effect":"Allow","Action":["ec2:*"],"Resource":"*"}` with only a soft prose caveat and **no narrowed EC2-Fleet example** (contrast `spot-fleet-prerequisites.html`, which enumerates a minimal, properly-scoped action list). Copy-verbatim, uneditable-pattern artifact → **in scope per the Lens R carve-out** (parent §5.2).
**Security Concern:** An org that copies the EC2 Fleet sample verbatim grants unconditioned `ec2:DeleteFleets` **and** `ec2:TerminateInstances` **and** everything else — which both (a) makes §5.1/§5.2/§5.3 moot by over-granting (the principal already holds blanket terminate), and (b) is itself the most likely real-world instantiation of the destructive primitive in unexpected hands. The sample's missing TerminateInstances-scoping example (§5.1) compounds this.
**High-level Test Scenarios:** read-only — resolve the printed JSON and confirm `ec2:*`/`*` includes `DeleteFleets`+`TerminateInstances` with no condition; for prevalence, `iam:GetAccountAuthorizationDetails` / Access Analyzer scan for the `{"Action":["ec2:*"],"Resource":"*"}` pattern on Fleet-using principals.
**Doc evidence:** `ec2-fleet-prerequisites.html`; `spot-fleet-prerequisites.html`; `ExamplePolicies_EC2.html`. **Severity-if-true:** **Informational / root-cause** (AWS-authored over-broad quick-start; route `aws-security` Tier-2 per the carve-out, consistent with parent §5.2).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Destroy out-of-scope instances via a tag-scoped TerminateInstances grant | DeleteFleets terminate-gate vs SLR terminate | `UnauthorizedOperation` requires `ec2:TerminateInstances`; **granularity undocumented** (missing example) |
| Silent decommission (orphan + Spot-cancel) with no TerminateInstances | DeleteFleets `--no-terminate` path | Gate fires only on the *must-terminate* path; Spot-cancel is unconditional |
| Non-uniform terminate control across DeleteFleets / ModifyFleet / direct | Twin-path parity | Per-instance `ec2:TerminateInstances` on the direct path only; absent on ModifyFleet; coarse? on DeleteFleets |
| Existence/state leak across ABAC-isolated principals | Batch per-fleet error codes | Tag-condition scoping of `ec2:DeleteFleets`; "deny ≈ not-found" assumption (check-order undocumented) |
| Cross-account fleet-ID enumeration | `FleetId.N` | 128-bit UUID + account-scoped resolution (**genuine null**) |
| Strand instances outside fleet governance | `deleted_running` lifecycle | None — fleet tags don't propagate; governance tied to the deleted request; quota still consumed |
| Partial/undefined state on >1000-instance instant delete | instant-fleet deletion | Prose "might fail; terminate manually first"; no error-code mapping |
| Destructive action with no audit record | EventBridge (instant blind spot) + CloudTrail record shape | "instant fleets do not emit events"; CloudTrail logs the call but maybe not instance IDs |
| Over-broad sample policy bundling delete+terminate | AWS-authored "EC2 Fleet users" policy | Prose caveat only; no scoped EC2-Fleet example shipped |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant / cross-account IDOR on fleets or instances** — N/A: a fleet, its instances, and the SLR all live in the caller's own account; `FleetId.N` resolves only in the caller's account; fleet IDs are 128-bit UUIDs (non-fabricable). (Cross-account trust lives in the KMS grant and shared Capacity Reservation surfaces — parent §5.5/§5.6 — not reachable through DeleteFleets.)
- **AWS service-plane / SLR live credentials** — hard stop; read-only (`GetPolicyVersion`, `GetRole`) only. The SLR performs the actual terminate; do not exercise it.
- **Single-tenant self-DoS / cost footguns** a caller inflicts on *their own* fleet (deleting a fleet they fully own with blanket perms) — out of scope, **except** where a principal that provably **lacks or is scoped out of** `ec2:TerminateInstances` achieves destruction/orphaning (§5.1/§5.2/§5.3), or where an ABAC-isolated principal learns hidden state (§5.4).
- **Customer-authored** least-privilege mistakes (an over-broad `ec2:DeleteFleets` the customer wrote) — a footgun, lower priority. The **AWS-authored** `ec2:*` sample policy and the missing TerminateInstances-scoping example are **in scope** per the Lens R carve-out (§5.8).
- **SSRF, wire-protocol/translation injection, prompt injection, attestation gating, canonicalization/parser-differential, cache-key divergence, trusted-header injection, JWT/token validation, KMS encryption-context, predictable-name land-grab** — N/A for this surface (see §8).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, pages checked)

- **Lens A (cross-account IDOR / enumeration):** cross-account = **GENUINE NULL** — fleet IDs are `fleet-`+128-bit UUID, no account qualifier, resolved in the caller's own account (checked `delete-fleet.md`, `API_DeleteFleets.md`, EventBridge ARN examples; `grep -ril checksum` on the mirror found no predictable structure). The *intra-account* ABAC existence/state leak **does** fire → §5.4. `DryRun` is caller-IAM-only, not an ownership oracle.
- **Lens F (injection/translation):** N/A — DeleteFleets inputs are an array of opaque IDs + a boolean + optional boolean; no free-text/query language or parser. Checked `API_DeleteFleets.md` + CLI reference.
- **Lens G (SSRF):** N/A — no URL/URI/webhook/callback field the service dereferences. Checked `delete-fleet.md`, `API_DeleteFleets.md`, CLI reference.
- **Lens H (KMS / encryption-context):** not reachable *through DeleteFleets* — any CMK interaction is on the *launch* side; the grant-over-scope lead lives in parent §5.5.
- **Lens EE (predictable-name land-grab):** N/A — fleet IDs are opaque UUIDs, account-scoped; no global/predictable namespace in play.
- **Lenses K / W / BB / CC / DD / FF (prompt-injection / attestation / canonicalization / trusted-header / cache-key / token-validation):** N/A — no LLM/agent, no enclave/`kms:RecipientAttestation`, no authorizer/WAF/CDN/cache layer, no JWT/OIDC in front of this SigV4 control-plane API.
- **Lens O (audit):** **fires** — the `instant`-fleet EventBridge blind spot and CloudTrail instance-ID question → §5.7.

**Load-bearing doc-gaps to resolve before calling anything confirmed:**
1. **(Blocks §5.1 — top priority)** Is DeleteFleets' internal `ec2:TerminateInstances` check evaluated **per-instance** (honoring the caller's tag/ID/AZ conditions) or **coarsely** ("holds the action")? Nowhere stated; delete-fleet.html's promised fix-policy example is **missing from the page** (confirmed online + offline — not a sync artifact).
2. **(Blocks §5.2)** Does any caller-side check (`ec2:CancelSpotInstanceRequests`) fire on the `--no-terminate` Spot-cancel path, or is it entirely un-gated? Not addressed in any mirrored page.
3. **(Blocks §5.4)** What is the **error-code check ordering** (malformed → exists → state → authz, or other)? Determines how much the ABAC leak exposes. `API_DeleteFleetError.md`'s valid-value enum is **incomplete** (lists 4 of 7 — omits `ExceededInstantFleetNumForDeletion`, `NoTerminateInstancesNotSupported`), so confirm the full code set and ordering against a sandbox.
4. **(Blocks §5.6)** No error code is documented for the >1000-instance instant-fleet failure (`unexpectedError` inferred); is the failure atomic or partial?
5. **(Blocks §5.7)** CloudTrail `DeleteFleets` record shape — does `responseElements` carry the terminated instance IDs, or only the fleet-state transition (requiring a correlated `TerminateInstances` event)?
6. **(Blocks §5.5)** Post-`deleted`-state queryability — do `DescribeFleetInstances`/`DescribeFleetHistory` still resolve a fleet two days after termination? Not stated in `describe-ec2-fleet.md`.
7. **(Service-plane / read-only)** Is the SLR's own `TerminateInstances` internally conditioned to fleet-owned instances? Resolve with read-only `iam:GetPolicyVersion` on `AWSEC2FleetServiceRolePolicy`; **do not** exercise the SLR.

---

### Kill-chain candidates (rate at the end of the chain)
- **§5.8 over-broad sample policy** (principal holds `ec2:*`) → **§5.1/§5.3** destructive terminate of *any* instance via the fleet path with **§5.7** weak audit trail → mass irreversible data destruction across the account with degraded attribution. **End severity: High** (account-wide destruction + evasion).
- **Recon** (`DescribeFleets`/`DescribeFleetInstances` → map fleets + their instances' tags) → **§5.1** (tag-scoped `TerminateInstances` holder calls `DeleteFleets --terminate` to destroy out-of-scope instances via the SLR) → **irreversible EBS/instance-store loss** on instances the caller could not terminate directly. **End severity: High** (SLR-laundered destruction of data outside the caller's grant).
- **§5.4 ABAC existence/state leak** (map hidden fleets by error-code differential) → feeds target selection for **§5.2 silent decommission** (orphan + Spot-cancel) against those fleets with only `ec2:DeleteFleets`. **End severity: Medium** (reconnaissance → availability impact without a terminate permission).
