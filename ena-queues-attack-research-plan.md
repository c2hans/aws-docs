# EC2 ENA Queues (configurable ENA queue allocation) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-queues.html` (offline mirror `docs/AWSEC2/latest/UserGuide/ena-queues.md`), cross-read against `list_ec2.md` (IAM Service Authorization Reference), `API_ModifyNetworkInterfaceAttribute.md` / `API_NetworkInterfaceAttachmentChanges.md` / `API_AttachNetworkInterface.md` / `API_InstanceNetworkInterfaceSpecification.md`, `iam-policies-for-amazon-ec2.md`, `vpc-share-limitations.md`, `troubleshooting-ena.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.** Target page + all four API-reference pages + `list_ec2.md` + `iam-policies-for-amazon-ec2.md` re-verified **offline==online, zero drift, 2026-10-15**.

> **What this page is.** The feature page for **configurable ENA queue allocation** — letting a caller choose how many Elastic Network Adapter (ENA) hardware queues each ENI gets, within a per-ENI and per-instance cap that varies by instance type. It introduces **one net-new attribute** — `EnaQueueCount` (Integer) and its reset twin `DefaultEnaQueueCount` (Boolean) — exposed on **three** existing control-plane actions: `RunInstances`, `AttachNetworkInterface`, `ModifyNetworkInterfaceAttribute`. It introduces **no new API, no IAM policy JSON, no URL/upload/token/role field, no cross-account surface.**

> **Where this plan sits in the corpus.** This is a **page-level deep-dive child of the `enhanced-networking-ena` hub**, which lists `ena-queues.html` as one of its children but develops it only at summary level (its Area N4 "cannot be managed from the console" doc-contradiction, and it explicitly **out-of-scopes** queue self-DoS and treats the power-of-2 / ≤vCPU limits as "availability facts, not vulnerabilities"). This plan **owns the net-new `EnaQueueCount` surface the hub and every sibling left undeveloped**: its total IAM-unscopability across all three paths, the three-path authz/validation parity question, the `DefaultEnaQueueCount` reset twin, and the doc-vs-API / doc-vs-doc integrity gaps. It **cross-references, does not restate**:
> - `[[enhanced-networking-ena-attack-research-plan]]` — Area N4 console-contradiction; §7 self-DoS out-of-scope. (do not restate)
> - `[[modify-network-interface-attributes-attack-research-plan]]` — its Area 5.1 "API accepts 10 attributes, UG lists 5" table is now **stale**: `EnaQueueCount`/`DefaultEnaQueueCount` is an **11th** `Attachment`-nested parameter it never captured. This plan supplies that correction.
> - `[[network-interface-attachments-attack-research-plan]]` — the closest owning sibling (`AttachNetworkInterface`/`DetachNetworkInterface` pair); extend its Area 2 zero-hit condition-key list with `ec2:EnaQueueCount`.
> - `[[using-eni-attack-research-plan]]` — owns `AttachNetworkInterface`; extend its lead #3 value-level 0-hit key list with `ec2:EnaQueueCount`.
> - `[[scenarios-enis-attack-research-plan]]` — its S5-AA1 ENI-failover carried-attribute set does **not** include `EnaQueueCount` (open question: does queue count ride a failover re-attach?).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **This is a deliberately low-yield page.** The honest headline is a *capability gap in AWS-authored IAM* (no condition key can govern queue allocation) plus doc-integrity defects — not a cross-tenant breach. There is **no cross-account path** on this surface (foreclosed by `vpc-share-limitations.md`, see §7). Do not inflate the self-DoS angle; the hub already out-of-scoped it.
- The primary safe oracle throughout is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** (no resource touched). The handful of enforcement questions (reject-vs-clamp, three-path parity) are **documentation-silent** and can only be settled by a live call on a **single owned canary instance** — never against shared or foreign resources.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. a requester-managed ENI appears under an AWS-owned operator), stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives
Stated as concrete boundary-breach outcomes:
1. **Govern-the-value objective (primary):** demonstrate that **no IAM policy an admin can write** will cap, floor, allowlist, or forbid a specific `EnaQueueCount`, nor block a `DefaultEnaQueueCount=true` reset, on *any* of the three call sites — i.e. the documented per-ENI/per-instance maxima and power-of-2 rule are **unexpressible as an IAM control**. (Lens S/U; AWS-owned, Tier-2 reportable as a capability gap.)
2. **Parity objective:** determine whether the three call sites (`RunInstances`, `AttachNetworkInterface`, `ModifyNetworkInterfaceAttribute`) enforce the documented constraints (power-of-2, ≤vCPU, per-ENI/per-instance max, instance-stopped) **identically**, or whether one path accepts a value another rejects (Lens X).
3. **Enforcement objective:** determine whether a constraint violation is a synchronous reject (`ValidationException`) or a **silent clamp/ignore** (undocumented either way) — a silent clamp is a doc-vs-behavior defect; a silent over-allocation acceptance is a self-DoS footgun (Lens U).
4. **Doc-integrity objective:** file the API-reference-omits-all-constraints gap and the "instance must be stopped" blanket-wording inconsistency (Lens U). Confirm the hub's Area N4 console-contradiction still holds.
5. **Isolation objective (expected NULL):** confirm there is **no** cross-tenant queue-starvation path, and characterize the intra-instance sibling-ENI starvation doc-gap (single-tenant → out of scope, but worth a one-line canary observation).

## 2. Components, Assets, and Design

**Interface.** EC2 control-plane API (SigV4 IAM). Three documented workflows, all also exposed in Console (under each **Network interface**) and PowerShell:
- `RunInstances` → `NetworkInterfaces.N` → `InstanceNetworkInterfaceSpecification.EnaQueueCount` (Integer) — set queue count at launch.
- `AttachNetworkInterface` → `EnaQueueCount` (Integer, CLI `--ena-queue-count`) — set at attach time.
- `ModifyNetworkInterfaceAttribute` → `Attachment` (`NetworkInterfaceAttachmentChanges` object) → `EnaQueueCount` (Integer) **or** `DefaultEnaQueueCount` (Boolean) — change / reset on an existing attachment.
- Read: `DescribeInstances` → `Reservations[].Instances[].NetworkInterfaces[].Attachment.EnaQueueCount` (the documented read path); `DescribeNetworkInterfaces` exposes the same field structurally.

**Asset.** ENA hardware queues — a **finite, per-instance pool shared across that instance's ENIs**, consumed only by the single instance that owns them. Not an ARN'd resource; it is an **attribute of an ENI↔instance *attachment***. Identifier shape: the attachment is named by `AttachmentId` (`eni-attach-...`); the attribute has no independent identity.

**Constraints (UserGuide prose only — `ena-queues.md` L629–635):** instance must be **stopped**; value must be a **power of 2** (1,2,4,8,16,32…); per-ENI count **cannot exceed the instance's vCPU count**; per-ENI and per-instance maxima vary by instance type (per-ENI observed range 1–128; per-instance observed range 2–1536; the `*` footnote marks types that reach the per-instance max via **multiple network cards**).

**Identity / ownership.** Every call site requires the caller to own (or be the single account behind) **both** the instance and the ENI. There is no service-linked role, no PassRole, no server-side fetch, no credential vending on this surface — all three actions run under the **caller's own identity**.

```
                 caller identity (SigV4 IAM) — same account owns instance + ENI
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                           ▼
   RunInstances            AttachNetworkInterface     ModifyNetworkInterfaceAttribute
   NetworkInterfaces.N      --ena-queue-count          --attachment ...,EnaQueueCount=N
   .EnaQueueCount                                       | ...,DefaultEnaQueueCount=true
          │                         │                           │
          └─────────────┬───────────┴───────────────────────────┘
                        ▼
        attachment attribute: EnaQueueCount   (NetworkInterfaceAttachmentChanges)
                        │
                        ▼
   ENA queue pool  ──  FINITE, PER-INSTANCE, shared across THIS instance's ENIs only
   (per-ENI cap ≤ vCPUs & ≤ type max;  per-instance cap = type max)
                        │
                        ▼
   read-back:  DescribeInstances → ...Attachment.EnaQueueCount   (unscopable; ec2:Region only)
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller identity | Own instance's ENA queue pool | `EnaQueueCount` on Run/Attach/Modify | **No boundary crossed** — same-account, same-owner. The only "boundary" is the IAM policy's *ability to express a value limit*, which does not exist (§5 Area 1). |
| IAM admin (intended governor) | A principal's queue-allocation choice | an intended `Deny` on `EnaQueueCount`/attribute | **Breach-of-intent oracle:** a `Deny` keyed on the queue value is **silently inert** — the governed principal still sets any queue count. Prove via `SimulateCustomPolicy` showing the key is never populated. |
| One ENI's attachment | A sibling ENI on the same instance | contending for the shared per-instance queue pool | **Intra-instance only** — self-DoS; not a tenant boundary. Oracle (canary): sequential attach/modify; does the 2nd call reject, or silently reduce the 1st ENI's count? (doc-gap, §5 Area 4) |
| Account A | Account B's ENI / instance queue pool | **FORECLOSED** — `vpc-share-limitations.md`: participants/owners cannot attach/detach/modify each other's ENIs | **No cross-tenant path exists** (§7). Any observation to the contrary = report (would contradict a published isolation guarantee). |
| Any customer surface | AWS service plane (requester-managed ENI) | Modify/Attach on a service-owned ENI | Modify/Attach are blocked on requester-managed ENIs by the existing hard-stop guardrail (`using-eni` lead #4). **Any success = HARD STOP + disclose.** |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `RunInstances` (`InstanceNetworkInterfaceSpecification.EnaQueueCount`) | SDK/CLI | **existing action, NEW field** | yes | external | set queue count at launch | yes (SigV4) | owner of instance+ENI | field not documented in API ref with any constraint (Lens U) |
| `AttachNetworkInterface` (`EnaQueueCount` / `--ena-queue-count`) | SDK/CLI | **existing action, NEW field** | yes | external | set queue count at attach | yes | owner | `network-interface*` row has **no `ec2:Attribute` key** (list_ec2 L4861) |
| `ModifyNetworkInterfaceAttribute` (`Attachment.EnaQueueCount` / `Attachment.DefaultEnaQueueCount`) | SDK/CLI | **existing action, NEW field** | yes | external | change / reset queue count | yes | owner | only path with `ec2:Attribute`/`ec2:Attribute/${AttributeName}` (L8969) — but see Area 1: cannot reach this value |
| `DescribeInstances` | SDK/CLI | existing | no | external | read current `Attachment.EnaQueueCount` | yes | any (per policy) | **unscopable** — blank resource type, `ec2:Region` only (L6996) |
| `DescribeNetworkInterfaces` | SDK/CLI | existing | no | external | read same field structurally | yes | any (per policy) | **unscopable** — blank resource type, `ec2:Region` only (L7218) |

Console-hidden / under-documented knob tells: `EnaQueueCount`/`DefaultEnaQueueCount` are **documented in the API reference with Type + Required:No and literally no constraint text** — the power-of-2, vCPU, maxima, and stopped-instance rules exist **only in UserGuide prose**. That delta is itself a Lens-U lead (§5 Area 3).

## 5. Recommended Areas of Focus

### Area 1 — `EnaQueueCount` / `DefaultEnaQueueCount` is IAM-unscopable on all three paths [Lens S / U — HEADLINE, AWS-owned, Tier-2 reportable]
**Background.** The feature's entire security-relevant surface is "which principal may set what queue count on which ENI." AWS documents per-ENI (≤vCPU, ≤type max) and per-instance maxima and a power-of-2 rule, framing them as governance of a finite resource.
**Security Concern.** None of that is expressible as an IAM control:
- Whole-of-`list_ec2.md` grep (10,190 lines): `EnaQueue` / `QueueCount` / `DefaultEnaQueueCount` / bare `queue` = **0 hits**; `ec2:Ena*` matches only unrelated `ec2:Enable*` **action** names. **No dedicated condition key exists.**
- `RunInstances` `network-interface*` row (L9595) and `AttachNetworkInterface` `network-interface*` row (L4861) **do not carry `ec2:Attribute` at all** → no value-scoping mechanism whatsoever.
- `ModifyNetworkInterfaceAttribute` `network-interface*` row (L8969) **does** carry `ec2:Attribute` and `ec2:Attribute/${AttributeName}` — but per AWS's own documented restriction (`iam-policies-for-amazon-ec2.md`, attribute-key section): the key *"supports only properties that are of a primitive data type … or complex AttributeValue objects that contain only a Value property … [not] complex objects that contain multiple properties, such as the LaunchPermission object."* `EnaQueueCount`/`DefaultEnaQueueCount` live inside the **multi-property `NetworkInterfaceAttachmentChanges` object** (4 properties: `AttachmentId`, `DeleteOnTermination`, `DefaultEnaQueueCount`, `EnaQueueCount`) — structurally the *disallowed* `LaunchPermission` shape, not the single-`Value` shape that `Description`/`SourceDestCheck` use. ⇒ `ec2:Attribute/${AttributeName}` **cannot reach the queue value even on the one action that has the key.**
**High-level Test Scenarios.**
- *Claim:* an admin cannot author any policy that forbids `EnaQueueCount=128` (or any value), nor one that blocks `DefaultEnaQueueCount=true`, on Run/Attach/Modify. → *Oracle:* `iam:SimulateCustomPolicy` with `ActionNames=["ec2:ModifyNetworkInterfaceAttribute"]`, `ResourceArns=["arn:aws:ec2:<region>:<acct>:network-interface/*"]`, `ContextEntries=[{ec2:Attribute/EnaQueueCount:"16"}]` against a `Deny` using that key; the decision does not change with the value because the service never populates the key for this field. Repeat for `ec2:Attribute/DefaultEnaQueueCount`. No resource touched.
- *Claim (adjacent):* the only live levers on these rows are ENI/subnet/SG identity, region, and tag — never the attribute value. → *Oracle:* enumerate each row's condition keys in `list_ec2.md` (done: §4 Notes).
**Doc evidence.** `list_ec2.md` L4861 / L9595 / L8969; `iam-policies-for-amazon-ec2.md` attribute-key restriction; `API_NetworkInterfaceAttachmentChanges.md` (4-property object). **Severity-if-true:** **Low–Medium** — a capability gap in AWS-authored IAM (no customer footgun; the customer *cannot* write the control at all). Reportable as Lens-S/U because it is AWS-owned and uneditable, **Tier 2**, routed `aws-security`. Not a data-access or privilege-escalation bug.
**Cross-ref:** extends `[[network-interface-attachments-attack-research-plan]]` Area 2 and `[[using-eni-attack-research-plan]]` lead #3 zero-hit key lists with `ec2:EnaQueueCount`; corrects `[[modify-network-interface-attributes-attack-research-plan]]` Area 5.1 attribute count (11th attribute).

### Area 2 — Three-call-site constraint-enforcement parity is documentation-silent [Lens X]
**Background.** One attribute, three setters (Run / Attach / Modify). Lens X asks whether a control enforced on one variant of a capability is enforced identically on its siblings.
**Security Concern.** The three parameter definitions (`InstanceNetworkInterfaceSpecification.EnaQueueCount`, `AttachNetworkInterface.EnaQueueCount`, `NetworkInterfaceAttachmentChanges.EnaQueueCount`) are **textually identical** in the API reference ("The number of ENA queues…", Integer, Required: No) with **zero** constraint or error text on any of them. The documentation therefore provides **no basis to prove or disprove** that all three enforce power-of-2 / ≤vCPU / per-ENI-max / per-instance-max / stopped-instance the same way.
**High-level Test Scenarios.**
- *Claim:* at least one path accepts a value (e.g. a non-power-of-2, or a value > per-ENI max, or on a *running* instance via Attach/Run) that another path rejects. → *Oracle:* on a single owned canary instance, submit the same out-of-range `EnaQueueCount` via each of Run / Attach / Modify and compare accept/reject + resulting `DescribeInstances.Attachment.EnaQueueCount`. **Live-only** (docs are silent); single owned instance; no shared/foreign resource.
- *Claim:* the "instance must be stopped" rule is enforced only for the Modify path (where it is written) and is moot/unenforced for Run (instance doesn't exist yet) and possibly for Attach-to-running. → *Oracle:* attempt Attach `--ena-queue-count` to a *running* owned instance; observe reject vs accept.
**Doc evidence.** `API_*` pages (no constraints/errors documented); `ena-queues.md` L633 (stopped rule written as a blanket under a heading covering all three tabs). **Severity-if-true:** Low (self-affecting parity/validation inconsistency; no tenant boundary). Flag as **doc-gap**, not a confirmed hole.

### Area 3 — Documented constraints absent from the API reference; violation behavior undocumented [Lens U]
**Background.** Lens U: trace every promised constraint to the mechanism that enforces it.
**Security Concern.** (a) **API-reference omission:** power-of-2, ≤vCPU, per-ENI/per-instance maxima, and the stopped-instance precondition appear **only** in `ena-queues.html` prose — **none** of the four API-reference pages carry them, and both relevant Errors sections name no `EnaQueueCount`-specific exception. A tool/SDK author working from the API reference has no machine-readable constraint. (b) **Violation behavior unspecified:** no doc (offline or online) states whether an out-of-range / non-power-of-2 / over-cap value is a synchronous `ValidationException` (**reject**) or a **silent clamp/ignore**. A silent clamp is a doc-vs-behavior defect (the caller believes they set N, got M); a silent over-allocation acceptance is a self-DoS footgun. (c) **Blanket-wording inconsistency:** "Your instance must be stopped before you configure the number of ENA queues" is written universally but is logically moot for `RunInstances` (set at launch).
**High-level Test Scenarios.**
- *Claim:* submitting `EnaQueueCount=7` (non-power-of-2) or a value above the per-ENI max is silently clamped rather than rejected. → *Oracle:* set it on an owned canary, read back `Attachment.EnaQueueCount`; a value ≠ submitted = silent clamp. **Live-only; single owned instance.**
- *Claim:* the API reference will accept and the SDK model will serialize a constraint-violating value with no client-side guard. → *Oracle:* inspect the SDK/botocore model + API-ref Errors (documentation only).
**Doc evidence.** All four `API_*.md` (no constraints/errors); `ena-queues.md` L629–635. **Severity-if-true:** Informational–Low (AWS-owned doc/enforcement-transparency gap). Reportable as a documentation defect; a confirmed silent-clamp would be a Low behavior bug.

### Area 4 — Intra-instance sibling-ENI queue starvation [Lens L — single-tenant, mostly out of scope]
**Background.** `ena-queues.md`: the pool is "shared across its ENIs… The total per ENI and per instance is still capped." Setting one ENI to its per-ENI max consumes from the shared per-instance budget (e.g. `m8a.8xlarge`: per-instance 128, per-ENI 32 — one ENI at 32 leaves 96 for all others combined).
**Security Concern.** The docs never state whether a second attach/modify that would exceed the remaining budget is **rejected atomically** or whether queues are **stolen from an already-attached ENI** (degrading its throughput silently). This is **single-tenant** (only the instance's own ENIs compete; cross-account attach is foreclosed, §7), so it is **self-DoS → out of scope** per the hub's §7, with one caveat worth a single canary observation: if a sibling ENI could ever be requester-managed/service-attached on a mixed-ownership instance, starving it would approach the service plane — but Modify/Attach on requester-managed ENIs is already blocked by the hard-stop guardrail, so the chain does **not** reach the service plane from documentation.
**High-level Test Scenarios.**
- *Claim:* allocating max queues to ENI-A silently reduces ENI-B's already-set count rather than erroring. → *Oracle:* on an owned 2-ENI canary, set ENI-A high, then read ENI-B's `Attachment.EnaQueueCount`; a drop = silent steal. **Live-only; single owned instance; stop at observation.**
**Doc evidence.** `ena-queues.md` (shared-pool sentences); `vpc-share-limitations.md` (cross-account foreclosed). **Severity-if-true:** Low / out-of-scope (single-tenant self-DoS). Documented here only to close the lens honestly.

### Area 5 — Console-manageability contradiction + change-observability gap [Lens U / O — cross-ref, do not restate]
**Background / Security Concern.** The hub (`[[enhanced-networking-ena-attack-research-plan]]` Area N4) already owns the direct textual contradiction: `enhanced-networking-ena.md` L55 says enhanced networking "cannot be managed from the console" while `ena-queues.md` L629 says the queue count **is** console-managed "under each Network interface." This plan **confirms it still holds (offline==online 2026-10-15)** and does not restate it. **Observability (Lens O):** a queue-count change emits **no EventBridge event** (no EC2 detail-type for it in the mirror's event catalog) and has **no dedicated CloudWatch metric** (the ENA driver metrics in `monitoring-network-performance-ena.md` are bandwidth/pps-allowance counters, unrelated to the configured count); the only read-back is the **unscopable** `DescribeInstances`/`DescribeNetworkInterfaces` field (`ec2:Region` only). `ModifyNetworkInterfaceAttribute` is a CloudTrail management event (logged by default), so the *setup* stays auditable even though no push signal exists.
**Severity-if-true:** Informational (AWS-owned doc inconsistency + observability gap). Owned by the hub; cited here for completeness.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| IAM cannot cap/forbid a queue value | Run/Attach/Modify `network-interface*` rows | "per-ENI/per-instance maxima" (prose) — **no IAM mechanism**; test the inert `ec2:Attribute` key (Area 1) |
| One path accepts what another rejects | 3 call sites | identical, constraint-free API-ref definitions — test parity live (Area 2) |
| Out-of-range value silently clamped/accepted | all paths | power-of-2 / ≤vCPU / caps (prose only) — test reject-vs-clamp (Area 3) |
| Sibling-ENI queue starvation | shared per-instance pool | "total per instance is still capped" — test atomic-reject vs silent-steal (Area 4, self-DoS) |
| Cross-account queue starvation | shared VPC | `vpc-share-limitations.md` ENI attach/modify prohibition — **expected to hold** (Area/§7) |
| Service-plane reach via requester-managed ENI | Modify/Attach guardrail | requester-managed ENI modify/attach block — **HARD STOP if it fails** |

## 7. Out-of-Scope Risk Categories
- **Cross-tenant queue starvation — FORECLOSED, not merely out of scope.** `vpc-share-limitations.md` (Network interfaces section) states participants cannot attach/detach/modify ENIs created by owners and vice-versa; `EnaQueueCount` is only settable via Run/Attach/Modify, all of which require single-account ownership of both instance and ENI. There is **no** cross-account path on this surface. (Matches `[[using-eni-attack-research-plan]]` §6 and resolves `[[network-interface-attachments-attack-research-plan]]` open doc-gap #4.)
- **Single-tenant self-DoS** — exhausting / mis-allocating your *own* instance's queue pool, bricking your own driver with a pathological count. Product behavior; already out-of-scoped by the hub.
- **Power-of-2 / ≤vCPU / maxima as availability facts** — these are capacity/availability limits, not security controls (hub §7). In scope here *only* as "is there an IAM key to express them" (Area 1) and "what happens on violation" (Area 3), not as limits per se.
- **Requester-managed / service-attached ENIs** — AWS service plane; modify/attach already blocked. HARD STOP on any success.
- **ENA driver internals / in-guest `ethtool` queue stats** — guest-OS surface, not control-plane.

## 8. Null hypotheses / doc gaps
- **Lens A (IDOR), B/C (PassRole/vending/STS), D (control-plane escape), G (SSRF), F (injection), H (KMS), K (prompt), M (session), N (namespace), J (OAuth), P (proofing), Q (upload), R (sample IAM policy), T (secret storage), V (segmentation beyond the foreclosed cross-account), W (attestation), Y (transport/sig), AA (share/revoke), BB/CC/DD (edge/parser/cache/upstream-context), EE (predictable-name), FF (JWT): NULL.** Pages read: `ena-queues.md` (full), all four `API_*.md`, `list_ec2.md` (grep), `iam-policies-for-amazon-ec2.md`, `vpc-share-limitations.md`, `troubleshooting-ena.md`. This surface is a single integer attribute on three same-account mutating actions — no role ARN, no URL the service dereferences, no upload, no token, no cross-account share, no printed IAM artifact, no new ARN/namespace, no edge/parser chain.
- **Doc-gaps carried for the hunter (all live-only, single owned canary):** (1) reject-vs-silent-clamp on constraint violation (Area 3) — highest value; (2) three-path validation parity (Area 2); (3) stopped-instance enforcement on Attach-to-running / Run (Area 2); (4) atomic-reject vs silent-steal on sibling-ENI over-allocation (Area 4); (5) does `EnaQueueCount` ride an ENI failover re-attach — `[[scenarios-enis-attack-research-plan]]` S5-AA1's carried-attribute set omits it.
- **Flaggable prior-corpus contradiction to re-verify (do NOT assert the old claim as fact):** the `[[modify-network-interface-attributes-attack-research-plan]]` corpus note asserts `ec2:Attribute` is **case-sensitive / fail-open**. The live UserGuide (`iam-policies-for-amazon-ec2.md`, keys section) states **"Condition keys are not case-sensitive."** This is a direct contradiction; the case-sensitivity premise should be re-verified empirically (SimulateCustomPolicy) before any downstream plan relies on it. (Immaterial to Area 1's conclusion, which rests on the *multi-property-object* restriction, not on casing.)
- **Drift:** target page + `API_ModifyNetworkInterfaceAttribute.md` + `API_NetworkInterfaceAttachmentChanges.md` + `API_AttachNetworkInterface.md` + `API_InstanceNetworkInterfaceSpecification.md` + `list_ec2.md` + `iam-policies-for-amazon-ec2.md` all re-verified **offline==online byte-identical 2026-10-15**.

See [[reference-aws-iam-service-auth-ref-url]].
