# Detach and Delete an EFA — Attack Research Plan

Source of leads: online + offline mirror page `docs/AWSEC2/latest/UserGuide/detach-efa.md` (`detach-efa.html`), **confirmed byte-for-byte identical offline↔online 2026-10-15**; the two procedure pages it defers to (`network-interface-attachments.md#detach_eni`, `delete_eni.md`); the EFA overview/changelog (`efa.md`, `efa-changelog.md`); and the authoritative IAM reference `docs/service-authorization/latest/reference/list_ec2.md` (trusted over User-Guide prose on conflict — see memory `reference-aws-iam-service-auth-ref-url`). Status: **documentation-derived falsifiable hypotheses only; nothing tested against a live account.** No claim below asserts a confirmed bug.

> **This is the teardown/lifecycle page of the EFA cluster.** It is a 15-line *pointer* page: it asserts EFA detach/delete work "in the same way as any other elastic network interface," adds one EFA-specific precondition ("you must first **stop** the instance"), and the lifecycle ordering (stop → detach → delete). It introduces **no new API, no role, no URL, no upload, no parser**. Accordingly this plan is deliberately **thin and complement-only**: it OWNS exactly three net-new things that live on *this* page and defers everything else, with explicit cross-references, to the siblings that already own it.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. you can address another tenant's QP/memory-region or the Nitro fabric control plane after a teardown), stop, preserve evidence, flag for AWS-Security disclosure.
- **Precedence:** this is documentation only. If the docs are thin on a surface, the lead is marked "doc-gap — confirm surface first," never silently closed.

### What this plan OWNS (net-new to detach-efa.html)
1. **The "same as any other ENI" equivalence claim** applied to a teardown that must also tear down OS-bypass RDMA/SRD/QP/MR/AH state a plain ENI never carries — a Lens-U guarantee-vs-mechanism gap *at the detach/delete boundary specifically* (Area 1).
2. **The EFA-only "must stop the instance first" precondition** and its IAM-unexpressibility — a lifecycle-ordering gate enforced by orchestration alone, with no `ec2:InstanceState` condition key and the detach/delete actions `InterfaceType`-blind (Area 2).
3. **The stop → detach → delete ordering state-machine** as a race/completeness surface (Area 3).

### What this plan DEFERS (do not re-run here)
- **Generic `DetachNetworkInterface` mechanics** — force-detach, device-index pin, cross-service-managed detach-refusal, no-EventBridge, the instance↔ENI join being IAM-unexpressible → **`network-interface-attachments-attack-research-plan.md`**.
- **Generic `DeleteNetworkInterface` collateral** — the UG-only EIP-disassociate + private-IP-release "whole-ENI unscopable address-strip," no-EventBridge → **`delete-eni-attack-research-plan.md`**.
- **EFA-specific teardown doc-gap, SG-does-not-filter-SRD, and the changelog QP/CQ-destroy correctness bugs** → **`efa-attack-research-plan.md` Area 7** (already owns these; this plan cross-refs, does not restate).
- **Detach/reattach residual MR/QP relocation + "SG-revoke does not sever a live RDMA session"** → **`efa-start-attack-research-plan.md` Area F**.
- **Root cause that `InterfaceType` is not an IAM-scopable grain** → **`efa-attack-research-plan.md` Area 1**.
- **The SRD/EFA AZ-VPC fabric confinement enforcement mechanism** → `efa-attack-research-plan.md` Area 4 / `efa-start` Area C (service-plane adjacent; HARD STOP on cross-tenant reach).

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce from the EFA teardown path:
- **O1.** Demonstrate that EFA detach/delete leaves **residual, addressable fabric or host-memory state** (queue pairs, memory regions, address handles, SRD flow state) that a plain-ENI teardown would not — i.e. the "same as any other ENI" guarantee is false in a security-relevant way. (If this state is reachable from another tenant → service-plane HARD STOP.)
- **O2.** Show that an operator **cannot author an IAM policy** that governs EFA detach/delete differently from an ordinary ENI, nor that enforces the "stopped instance" precondition — so an identity granted broad `ec2:DetachNetworkInterface`/`ec2:DeleteNetworkInterface` on tagged ENIs silently also tears down EFAs.
- **O3.** Break the **stop → detach → delete ordering** (race a detach against a running/rebooting/replacing instance, or delete a still-logically-attached EFA) and observe inconsistent fabric teardown.

## 2. Components, Assets, and Design
- **Customer-facing interface:** EC2 control-plane APIs only — `ec2:DetachNetworkInterface`, `ec2:DeleteNetworkInterface` (plus `ec2:StopInstances` as the mandatory precursor). The page exposes no EFA-specific API; an EFA *is* an ENI with `InterfaceType=efa` or `efa-only`.
- **Asset under teardown:** an elastic network interface that additionally fronts the **EFA OS-bypass device** (libfabric/SRD endpoint, queue pairs, protection domains, memory regions pinned in guest RAM, address handles). A plain ENI has none of this; the page nonetheless asserts the teardown is identical.
- **Accounts/zones:** single customer account/VPC on the API side. The *fabric* side (SRD/RDMA, Nitro-enforced AZ/VPC confinement) is a shared-substrate, service-plane-adjacent zone — reaching another tenant's QP/MR after teardown is the top-severity outcome and a HARD STOP.
- **Identity:** SigV4 IAM. No role is passed, no credential vended on this path.
- **State machine (the page's core content):**

```
  [running]  --(cannot detach EFA here)-->  X
      |  ec2:StopInstances
      v
  [stopped]  --ec2:DetachNetworkInterface-->  [EFA detached, ENI exists]
                                                   |  ec2:DeleteNetworkInterface
                                                   v
                                              [EFA deleted]
   (open question: at WHICH edge is SRD/QP/MR/AH state actually torn down —
    at power-off, at detach, at delete, or never fully? = Area 1/3 doc-gap)
```

## 3. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller identity w/ broad ENI detach/delete | A specific EFA ENI (`InterfaceType=efa`) | `ec2:DetachNetworkInterface`/`DeleteNetworkInterface`; **no `ec2:InterfaceType` key exists** to carve EFA out | A policy intended to allow plain-ENI teardown but forbid EFA teardown **cannot be written** → EFA torn down under an EFA-blind grant (Area 2) |
| Caller (any state) | The "stopped-instance" precondition | Orchestration only; **no `ec2:InstanceState` condition key** in `list_ec2` | The precondition cannot be IAM-enforced or IAM-relaxed; only API orchestration gates it (Area 2) |
| A detached/deleted EFA's residual fabric state | Another tenant / the SRD fabric | SRD/QP/MR teardown semantics are **undocumented** on this page | Any addressable QP/MR/AH or in-flight SRD flow surviving teardown and reachable cross-tenant = **service-plane HARD STOP** (Area 1, cross-ref hub Area 7 / efa-start Area F) |

## 4. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:DetachNetworkInterface` | API | Existing | **Yes** | External | Detach the EFA ENI from a **stopped** instance | Yes (SigV4) | Any principal granted it on the ENI | `list_ec2` L2672: **Access level Write; blank condition-key cell in the summary row**. Resource-level scoping to `network-interface*` + `aws:ResourceTag` is owned by the attachments sibling. **No `InterfaceType` grain.** |
| `ec2:DeleteNetworkInterface` | API | Existing | **Yes** | External | Delete the detached EFA ENI | Yes (SigV4) | Any principal granted it on the ENI | `list_ec2` L1142: **Access level Write; blank condition-key summary cell.** UG-only collateral (EIP disassociate + private-IP release) owned by `delete-eni` plan. **No `InterfaceType` grain.** |
| `ec2:StopInstances` | API | Existing | Yes | External | Mandatory precursor to EFA detach | Yes | — | `list_ec2` L4513. The *only* documented enforcement of the "stop first" rule is this ordering; no state condition key (Area 2). |

Confirmed from `list_ec2.md` 2026-10-15: `ec2:InterfaceType` = **0 hits (not a real IAM condition key)**; `ec2:InstanceState`/`InstanceStateName` = **0 hits (no such key)**; only `ec2:StopInstances` exists as an action.

---

## 5. Recommended Areas of Focus

### Area 1 — "Detach/delete an EFA the same way as any other ENI": the equivalence guarantee vs the extra RDMA/SRD teardown (Lens U, headline)
**Background.** The page's opening sentence is a security-relevant *guarantee*: *"You can detach an EFA from an Amazon EC2 instance and delete it in the same way as any other elastic network interface in Amazon EC2."* Both sub-sections repeat the equivalence ("in the same way that you detach/delete an elastic network interface"). But an EFA is **not** the same as a plain ENI at teardown: it fronts an OS-bypass libfabric/SRD device with queue pairs, protection domains, **memory regions pinned in guest RAM**, and address handles — none of which a plain ENI has. The page says **nothing** about tearing that state down.

**Security Concern.** Trace the "same way" guarantee to a mechanism. A plain-ENI detach/delete tears down IP/MAC/route/SG association. An EFA detach/delete must *additionally* retire SRD/QP/MR/AH and un-pin host memory. If that extra teardown is **not performed, is performed lazily, or is performed only at instance power-off** (not at the detach/delete API), then:
- (a) a **residual, still-addressable** QP/MR/AH could survive the ENI's logical teardown — a stale fabric handle; if it is reachable by a subsequently-attached workload or (worse) another tenant on the shared SRD substrate, that is a cross-tenant/service-plane breach (HARD STOP);
- (b) the operator's mental model ("I deleted the interface, so the fabric endpoint is gone") is wrong — a Lens-U documented-guarantee-vs-enforcement defect that AWS owns (the guarantee is in an AWS page).

**High-level Test Scenarios.**
- *Claim:* EFA detach/delete does not perform SRD/QP/MR teardown at the API; teardown happens only at power-off, leaving a window where a detached-but-not-powered-cycled interface's fabric state persists. → *Oracle:* on a stopped instance, detach the EFA, then inspect (from inside a freshly re-attached workload on the same host/instance) whether prior QP/MR/AH handles are still valid/pollable; the changelog's QP-destroy/CQ-poll correctness history (cross-ref hub Area 7) is the hint that this teardown has been buggy. → *Severity:* residual same-tenant handle = Medium; cross-tenant addressable = **Critical + HARD STOP**.
- *Claim:* the "same as any ENI" guarantee is false — EFA teardown has an extra, undocumented step with its own failure mode. → *Oracle:* diff the observable post-detach device state (`fi_info`, `/sys/class/infiniband`, rdma resources) of an EFA vs a plain ENI after an identical detach sequence; any EFA-only residual = guarantee violated. → *Severity:* Low–Medium (doc-vs-enforcement) unless (a) escalates it.

**Changelog corroboration (with a precise caveat).** `efa-changelog.md` shows QP/CQ/MR/AH destroy-ordering has been a historically fragile area of the EFA stack — e.g. 1.44.0 *"Fix CQ poll after QP destroy"*; 1.48.0 *"Fix use-after-free bugs in DC packet completion, CQ drain, AH unit test, and MR logging"* and *"Add null check for base_ep in CQ polling to handle destroyed QPs"*; 1.47.0 *"Fix double-free in … RTM packet processing"* and *"Unlink RX packet entries before releasing during endpoint cleanup."* **Caveat (do not over-attribute):** these are **host-side libfabric/rdma-core/EFA-driver lifecycle bugs in the user-space RDMA stack**, not changes to the EC2 `DetachNetworkInterface`/`StopInstances` control-plane path. They establish that fabric-object teardown is fragile *in the guest*; whether the EC2 teardown API triggers an analogous residual-state window is the Area-1 doc-gap to confirm live, not something the changelog proves.

**Doc evidence:** `detach-efa.md` L8 ("in the same way as any other elastic network interface"), L13, L15, L22; `efa.md` (teardown silence — no SRD/QP/MR/AH/detach/delete/stop/teardown prose, confirmed 2026-10-15); `efa-changelog.md` (1.44.0/1.47.0/1.48.0 lifecycle fixes above). **Defer** full changelog ownership and the SG-doesn't-filter-SRD angle to `efa-attack-research-plan.md` Area 7; defer the detach/reattach residual-MR relocation + "SG-revoke doesn't sever a live RDMA session" to `efa-start-attack-research-plan.md` Area F. **Severity-if-true:** Low–Medium baseline; **Critical + HARD STOP** if residual fabric state is cross-tenant addressable.

### Area 2 — The EFA-only "stop the instance first" precondition is IAM-unexpressible, and detach/delete cannot be scoped to EFA interfaces (Lens S / X / U)
**Background.** The page adds one rule a plain secondary ENI does **not** have: *"To detach an EFA from an instance, you must first stop the instance. You cannot detach an EFA from an instance that is in the running state."* The very procedure page it defers to contradicts this for ordinary ENIs — `network-interface-attachments.md` states (Considerations) *"You can detach secondary network interfaces when the instance is **running or stopped**"* and the detach section opens *"You can detach a secondary network interface that is attached to an EC2 instance **at any time**."* So EFA detach is a **strictly stricter** lifecycle than the generic ENI procedure the page simultaneously claims parity with — a confirmed **internal contradiction inside the "same way" guarantee** (the equivalence prose and the stop-first rule cannot both be fully true). The stricter rule almost certainly exists *because* the EFA fronts fabric/memory-region state that must quiesce at power-off (Area 1), but the docs never say so — the rationale is a doc-gap.

**Security Concern.** Two IAM-expressibility gaps confirmed against `list_ec2.md`:
1. **No `ec2:InstanceState` / `InstanceStateName` condition key exists** (0 hits). The "must be stopped" rule is therefore **pure API orchestration** — an operator can neither *tighten* it (e.g. "only allow detach when instance carries tag X and is stopped") nor rely on IAM to express it. The precondition is invisible to policy evaluation and to `iam:SimulatePrincipalPolicy`.
2. **`ec2:InterfaceType` is not a real IAM condition key** (0 hits — reconfirms `efa-attack-research-plan.md` Area 1). Both `ec2:DetachNetworkInterface` and `ec2:DeleteNetworkInterface` carry a **blank condition-key cell** in their `list_ec2` summary rows and are scopable only by the `network-interface*` resource ARN + `aws:ResourceTag` (owned by the siblings). There is **no way to write a policy that permits tearing down ordinary ENIs but forbids tearing down the account's EFAs** (or vice-versa). An EFA is distinguished only by a field (`InterfaceType=efa`/`efa-only`) that IAM cannot see.

**Consequence (Lens X asymmetry):** a principal granted broad ENI detach/delete on tag-matched interfaces will silently also tear down EFAs it was never meant to touch — and because EFA teardown may carry the extra fabric-state semantics of Area 1, an EFA-blind grant is strictly more dangerous than the operator believes. This is a least-privilege-*unexpressibility* defect in the EC2 authz model, not a customer footgun (the customer cannot fix it with any policy).

**High-level Test Scenarios.**
- *Claim:* no condition key can single out EFA interfaces at detach/delete. → *Oracle:* `iam:SimulateCustomPolicy` with a Deny keyed on `ec2:InterfaceType` / `ec2:InstanceState` on `ec2:DetachNetworkInterface` — the keys are inert (ignored), so the Deny never bites; the detach of an `efa` ENI is still Allowed. No resource touched. → *Severity:* Low–Medium (expressibility gap; AWS-owned, Lens U/S).
- *Claim:* the "stopped" precondition is orchestration-only and so is relaxable by an API path or raceable (see Area 3). → *Oracle:* attempt `DetachNetworkInterface` on an `efa` ENI of a `running` instance and confirm it is the *API* (not IAM) that refuses; then probe transitional states (stopping/pending/rebooting). → *Severity:* see Area 3.

**Doc evidence:** `detach-efa.md` L13 (stop-first rule, EFA-only); `list_ec2.md` L2672/L1142 (blank condition cells), 0-hit greps for `ec2:InterfaceType` and `ec2:InstanceState`. **Severity-if-true:** Low–Medium (Lens U/S/X expressibility defect, AWS-owned, reportable Tier-2 flavor as a model gap, not a bug).

### Area 3 — stop → detach → delete ordering as a race / completeness surface (Lens P state-gate / Lens AA revocation-completeness)
**Background.** The page defines a strict ordering with two "must reach state before action" gates: *"To detach an EFA … you must first stop the instance"* and *"To delete an EFA, you must first detach it from the instance. You cannot delete an EFA while it is attached."* Each gate is a Lens-P precondition; the EFA fabric teardown presumably happens somewhere along this chain.

**Security Concern.** Because the gates are orchestration-enforced (Area 2) and the fabric-teardown edge is undocumented (Area 1), the ordering is a candidate for **transition-state races and incomplete teardown**:
- Does `DetachNetworkInterface` succeed against an instance in a *transitional* state (stopping / pending / rebooting / under instance-replacement by an Auto Scaling or Spot-maintain controller) where the guest RDMA stack has not cleanly quiesced? A detach that lands mid-quiesce could orphan QP/MR state (chains to Area 1).
- Is there a path to `DeleteNetworkInterface` an EFA that is still *logically* attached at the fabric layer even though the control plane marks it detached (control-plane vs fabric-plane view divergence)? If delete returns success but the SRD endpoint lingers, the "delete requires detach" guarantee is a control-plane-only check (Lens AA revocation-incompleteness — the revoke doesn't sever the derived fabric state).
- **Force-detach already documents a control-plane-vs-reality divergence** (confirmed, generic): `network-interface-attachments.md` warns that force detachment *"can prevent you from attaching a different network interface on the same index until you restart the instance. It can also prevent the instance metadata from reflecting that the network interface was detached until you restart the instance."* So a forced detach leaves the control-plane/metadata view **out of sync with the actual attachment state until a restart** — exactly the divergence class Area 3 attacks, and a strong hint that a force-detached EFA could leave fabric/MR state in an undefined window. Does a forced detach of an *EFA* skip the clean SRD/MR teardown that a graceful detach would do?

**High-level Test Scenarios.**
- *Claim:* detach during a transitional/replacement window leaves residual QP/MR. → *Oracle:* script a `StopInstances`→immediate `DetachNetworkInterface` race and inspect fabric residue (as Area 1); repeat under a `maintain`-fleet instance replacement. → *Severity:* Medium same-tenant; **Critical + HARD STOP** if cross-tenant addressable.
- *Claim:* control-plane "deleted" ≠ fabric "torn down." → *Oracle:* after delete, probe for any surviving SRD endpoint/address handle keyed to the old ENI MAC/ID. → *Severity:* as above.

**Doc evidence:** `detach-efa.md` L13, L20–L22. **Defer** the generic force-detach + cross-service-managed-detach-refusal mechanics to `network-interface-attachments-attack-research-plan.md`; **defer** the detach/reattach residual-MR relocation primitive to `efa-start` Area F. **Severity-if-true:** Medium baseline; escalates to Critical/HARD-STOP on cross-tenant fabric residue.

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| EFA teardown leaves residual addressable QP/MR/AH (Area 1) | SRD/libfabric device behind the EFA ENI | "same way as any other ENI" equivalence claim (prose only; no documented fabric teardown) |
| EFA-blind detach/delete grant tears down an EFA an operator meant to protect (Area 2) | IAM authz on `ec2:DetachNetworkInterface`/`DeleteNetworkInterface` | none — `ec2:InterfaceType` is not a real key; only `network-interface*`+`aws:ResourceTag` scoping |
| "Must stop first" precondition relaxed/raced (Area 2/3) | API orchestration of the stop→detach gate | prose rule only; no `ec2:InstanceState` condition key to enforce or audit it |
| Control-plane "deleted" ≠ fabric torn down (Area 3) | detach→delete ordering gate | "you cannot delete while attached" (control-plane check; fabric view undocumented) |

## 7. Out-of-Scope Risk Categories
- **Generic ENI detach/delete authz and collateral** (force-detach, index pin, EIP-disassociate + private-IP-release address-strip, no-EventBridge) — owned by `network-interface-attachments-attack-research-plan.md` and `delete-eni-attack-research-plan.md`. Do not re-derive here.
- **EFA installer supply chain, self-referencing SG construction, OS-bypass InterfaceType root cause, SRD AZ/VPC fabric confinement mechanism** — owned by `efa-attack-research-plan.md` (Areas 1/2/4/7) and `efa-start`/`efa-start-nccl`/`efa-start-nixl`/`efa-installer-containers` plans.
- **Single-tenant self-DoS** (leaking your own QP/MR until a per-instance cap) — out of scope unless it crosses a tenant boundary.
- **IMDS on managed/metal hosts, product-parity gaps.**
- **Shared Nitro/SRD substrate internals** — service-plane; HARD STOP and disclose on any cross-tenant reach, do not probe AWS infrastructure.

## 8. Null hypotheses / doc gaps
Lenses checked against `detach-efa.md` (+ the two referenced procedure pages) and found non-firing, with the pages read:
- **Lens A (cross-tenant IDOR):** N/A on this page — it exposes no resource-by-ID API of its own; the ENI id lives in the generic detach/delete actions owned by siblings. No tenant-id-in-body shape. (Residual-handle *reachability* is captured as the Area 1/3 fabric doc-gap, not an API IDOR.)
- **Lens B / C (PassRole / credential vending):** N/A — no role ARN, no session, no credential on detach/delete. Pages read: `detach-efa.md`.
- **Lens F / G / K / Q (injection / SSRF / prompt / upload):** N/A — a teardown pointer page has no parser, no server-side-dereferenced field, no LLM, no upload. Pages read: `detach-efa.md`, `network-interface-attachments.md`, `delete_eni.md`.
- **Lens H / T (KMS / secret reachability):** N/A — no key, no generated/persisted secret on this path.
- **Lens I (tagging/ABAC):** only indirectly — tag-based scoping of the detach/delete actions is the sibling-owned mechanism; this page adds no tag surface. The *inability* to ABAC-scope by `InterfaceType` is folded into Area 2 (Lens S/X).
- **Lens W / Y / BB / CC / DD / EE / FF:** N/A for a 15-line lifecycle page — no attestation gate, no transport/TLS surface, no multi-parser request path, no upstream-context header, no cache layer, no predictable-name resolution, no token validation.
- **Lens L (resource exhaustion):** marked **doc-gap** — residual QP/MR leak as a self-DoS is possible but single-tenant (out of scope) unless it exhausts a *shared* fabric resource (then → Area 1 cross-tenant, HARD STOP). Confirm fabric-residue behavior first.
- **Lens O (audit):** marked **doc-gap** — whether an EFA detach/delete emits a CloudTrail signal distinguishable from a plain-ENI teardown (it almost certainly does not, since the action is literally the same `ec2:DetachNetworkInterface`). Low/Informational; an enabler for Area 1/3 stealth if confirmed.

**Open doc-gaps to confirm before investing (ranked):**
1. **At which lifecycle edge is SRD/QP/MR/AH state actually torn down** — power-off, detach, delete, or never fully? (Area 1/3; the load-bearing unknown — DryRun/SimulatePolicy cannot answer it; needs a synthetic EFA-enabled canary instance.)
2. **Is any residual fabric state cross-tenant addressable** on the shared SRD substrate? (Area 1; HARD STOP if yes.)
3. **Does the control-plane "deleted/detached" state ever diverge from the fabric view** (delete succeeds while SRD endpoint lingers)? (Area 3.)
4. **Does a forced / transitional-state detach skip graceful SRD/MR teardown?** (Area 3.)

---
*Cross-references:* `efa-attack-research-plan.md` (hub; Areas 1/2/4/7), `efa-start-attack-research-plan.md` (Area F detach/reattach residual MR/QP + SG-revoke-doesn't-sever-live-RDMA), `network-interface-attachments-attack-research-plan.md` (generic detach), `delete-eni-attack-research-plan.md` (generic delete collateral). IAM ground truth: `service-authorization/latest/reference/list_ec2.md`.
