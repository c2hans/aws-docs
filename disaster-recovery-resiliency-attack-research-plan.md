# Resilience in Amazon EC2 — Attack / Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disaster-recovery-resiliency.html
**Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/disaster-recovery-resiliency.md`
**Skill:** `security-questionbuilder` (boundary-first, documentation-derived, read-only)
**Date:** 2026-10-15
**Drift status:** target page verbatim offline==online. Subagent-verified live twins: `dlm-prerequisites.md`, `AWSDataLifecycleManagerSSMFullAccess.md` byte-identical as of 2026-10-15. `list_ec2.md` condition-key facts grepped offline (online WebFetch truncates before the condition-key tables).

---

## IMPORTANT — how to read this plan (it is a HUB plan)

`disaster-recovery-resiliency.html` is a **thin, template-driven hub page** (25 lines). It has **no API of its own**. It asserts two availability guarantees (AZ / Local-Zone isolation) and then enumerates **six** EC2 resiliency *features*, each owned by a different API surface and in several cases a different service. The real attack surface therefore lives in the children, not the hub.

This plan does three things:
1. **Owns the hub-level synthesis** — the AZ / Local-Zone Lens-U guarantee sentences, and the cross-Region **copy-path condition-key facts** that are common to AMI copy, EBS snapshot copy, and DLM (the `ec2:KmsKeyId` gap chain extending the `data-protection` plan's R2).
2. **Folds in three parallel deep-dive subagent syntheses** — (§5A) AMI cross-Region copy, (§5B) EBS snapshot cross-Region copy, (§5C) Amazon Data Lifecycle Manager. **DLM carries the single highest-severity finding on the page** (a documentation-sanctioned RCE kill chain, §5C-T1).
3. **Cross-references existing sibling plans** rather than re-deriving them, and treats **EC2 Auto Scaling** and **Elastic Load Balancing** as separate-service pointers / deferred doc-gaps (feature #5 and #6).

### Cross-referenced sibling plans (already in `/work/aws-docs/`)
- `using-regions-availability-zones-attack-research-plan.md` — AZ-name-vs-ZoneId residency SCP footgun, `ModifyAvailabilityZoneGroup` unscopable one-way opt-in, CreateVolume/Snapshot AZ asymmetry. **The AZ/Local-Zone Lens-U guarantees in this hub defer their mechanism analysis there.**
- `data-protection-attack-research-plan.md` — **R2 headline: `ec2:KmsKeyId` present on CreateVolume/CreateFleet but ABSENT from CopySnapshot/CopyVolumes/RunInstances-vol.** This hub's §4 copy-path facts are the direct extension of that finding onto the DR/resiliency copy surface.
- `ec2-instance-naming-attack-research-plan.md` — dangling-DNS / `.ip.aws` reuse (relevant if a failover re-IPs an instance).

---

## §0 — Pentest Objectives

Confirm or refute, from documentation only, that an attacker operating within one AWS account (or a lower-privileged principal inside it) can abuse the EC2 "resiliency" feature set to:

1. **Re-encrypt a copied snapshot/AMI under an attacker-chosen or unintended KMS key** because no copy-path IAM action carries an `ec2:KmsKeyId` condition key (§4, §5A-H, §5B-H).
2. **Leak or retain cross-account/cross-org access** to snapshots and AMIs past the point the owner believes access was revoked (§5A-AA, §5B-AA, §5C-AA).
3. **Read raw snapshot block data via the EBS direct-APIs** (`ebs:GetSnapshotBlock`) under an authorization grain that diverges from the `ec2:CopySnapshot` ownership grain (§5B-X — **Critical lead**).
4. **Achieve root/SYSTEM RCE on every SSM-managed EC2 instance in the account** by chaining DLM's caller-controlled pre/post-script handler with the unconditioned `AllowAllEC2Instances` SSM grant (§5C-T1 — **Critical, documentation-sanctioned**).
5. **Escalate via DLM's over-broad service roles** (`Resource:"*"`, no ownership/tag condition on `DeleteSnapshot` / `DeregisterImage` / `ModifyImageAttribute`) to delete or publicly share any snapshot/AMI in the account (§5C-R2/R3).
6. **Land-grab a predictable default role name** (`AWSDataLifecycleManagerDefaultRole`) so an admin's first console use adopts an attacker-planted, backdoored-trust role (§5C-EE1).

Each is phrased as a falsifiable claim with a Confirm/Refute oracle below. **Everything is a documentation-derived hypothesis; nothing has been executed against a live account.** The oracles are what a downstream `aws-vuln-hunter` runs.

---

## §1 — Components, Assets, and Design

The hub page names six features. Mapped to their real owning surfaces:

| # | Feature (hub wording) | Owning API / service | Deep-dive |
|---|---|---|---|
| 1 | Copying AMIs across Regions | `ec2:CopyImage` (+ auto `ec2:CopySnapshot`) | §5A |
| 2 | Copying EBS snapshots across Regions | `ec2:CopySnapshot`; EBS direct-APIs (`ebs:*`) | §5B |
| 3 | Automating EBS-backed AMIs via DLM | `dlm:*` + SSM + service roles | §5C |
| 4 | Automating EBS snapshots via DLM | `dlm:*` + service roles | §5C |
| 5 | Fleet health via EC2 Auto Scaling | `autoscaling:*` (**separate service**) | deferred — §7 |
| 6 | Traffic distribution via Elastic Load Balancing | `elasticloadbalancing:*` (**separate service**) | deferred — §7 |

**Assets at stake:** EBS snapshots (and their block data), AMIs (and their backing snapshots), the KMS keys that encrypt them, the IAM execution/service roles DLM assumes, and the SSM-managed instance fleet DLM can command.

**Identifier shapes:** snapshot IDs `snap-<17 hex>` and AMI IDs `ami-<17 hex>` are **high-entropy / non-enumerable** (closes Lens EE for the copy surface — see §5B-EE). DLM default **role names are predictable/fixed** (opens Lens EE for DLM — §5C-EE1).

**Guarantee sentences on the hub itself (Lens U seeds):**
- L8: *"...applications and databases that automatically fail over between zones without interruption"* and *"physically separated and isolated Availability Zones."*
- L10: *"Like all AWS Regions, AWS Local Zones are completely isolated from other AWS Zones."*

```
                         disaster-recovery-resiliency.html  (hub, no API)
                                        |
        +------------------+------------+------------+------------------+
        |                  |                         |                  |
   AZ / Local-Zone    cross-Region copy          DLM automation    AutoScaling / ELB
   isolation (U)      (ec2:CopyImage,            (dlm:* + SSM +     (separate services,
   [→ regions-AZ      ec2:CopySnapshot,          service roles)     §7 deferred)
    sibling plan]     ebs:* direct-APIs)              |
                           |                          |
                  KMS re-encryption gap        caller-script -> ssm:SendCommand
                  (no ec2:KmsKeyId on           -> RCE on all SSM-managed
                   any copy path) [§4]           instances [§5C-T1]
```

---

## §2 — Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Account A principal | Account B snapshot/AMI | `ModifySnapshotAttribute` / `ModifyImageAttribute` share; DLM cross-account copy policy | B retains read after A believes it revoked; B is a non-member of A's org/OU yet share succeeds |
| Lower-priv principal in Account A | All snapshots/AMIs in A | DLM service roles `Resource:"*"` no condition | Delete/deregister/share a resource **not** created by DLM |
| Lower-priv principal in A (holds DLM sample policy only) | Every SSM-managed instance in A | `ExecutionHandler` free text → `ssm:SendCommand` (unconditioned) | Command executes as root/SYSTEM on a non-DLM instance |
| Caller supplying copy params | KMS key used to re-encrypt copy | copy path with no `ec2:KmsKeyId` condition | Copy completes under a key an `ec2:KmsKeyId` Deny was meant to forbid |
| EBS direct-API caller | Raw snapshot blocks | `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` | Block read authorized where `ec2:CopySnapshot` ownership would deny |
| Attacker with `iam:CreateRole` in A | Admin's first DLM console use | Predictable role-name collision + documented "reuse existing" remedy | Admin adopts attacker-planted role with backdoored trust policy |
| AZ ↔ AZ; Local Zone ↔ other Zones | — | hub Lens-U guarantee | **Deferred to `using-regions-availability-zones` sibling** — physical-isolation claims are shared-responsibility, not customer-testable here |

---

## §3 — API / Interface Inventory

| Name | Mutating | Facing | Copy/KMS key? | Notes |
|---|---|---|---|---|
| `ec2:CopyImage` | yes | external | **no `ec2:KmsKeyId`, no `ec2:Encrypted`** | L4990-4994 list_ec2; image* + snapshot* keys are tag/ID/Region only |
| `ec2:CopySnapshot` | yes | external | **no `ec2:KmsKeyId`** (has `ec2:Encrypted`) | L4996-5000 list_ec2; auto-granted alongside CopyImage |
| `ec2:CreateVolume` | yes | external | **has `ec2:KmsKeyId`** (L5122) | the *only* path with the key — asymmetry anchor |
| `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` / `ListChangedBlocks` | no (read) | external | n/a | **no `ebs:Owner` key in list_ebs.md** — §5B-X |
| `ec2:ModifySnapshotAttribute` | yes | external | n/a | has `ec2:Add/group`, `ec2:Add/userId` (L10047-48) — snapshots only |
| `ec2:ModifyImageAttribute` | yes | external | n/a | **no `ec2:Add/*` condition key for images** — §5A-AA |
| `dlm:CreateLifecyclePolicy` / `UpdateLifecyclePolicy` | yes | external | n/a | **no required Resource type**; `ExecutionHandler` free text — §5C-T1/S1 |
| `autoscaling:*`, `elasticloadbalancing:*` | — | — | — | separate services, §7 deferred |

Doc-flagged leads kept verbatim: copy-ami-permissions.md L60 ("Users need `ec2:CopySnapshot` ... automatically") ; ebsapi-permissions.md L12-13 (EBS direct-API vs EC2 permission divergence); automate-app-consistent-backups.md ("If you decide to not include that condition key, then you do not need to tag your SSM documents").

---

## §4 — HUB-LEVEL FINDING: the cross-Region copy KMS re-encryption gap (Lens H / X)

**Claim:** No cross-Region copy action on this page can be scoped to a specific KMS key via IAM, so an `ec2:KmsKeyId`-based Deny (the natural guardrail a security team would write) **fails open** on every copy path, while the same key *does* gate `CreateVolume`.

**Mechanism (offline-grep-verified in `list_ec2.md`):**
- `CopyImage` (L4990-4994): image keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:ImageID`, `ec2:Owner`, `ec2:Region`; snapshot keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:Region`. **No `ec2:KmsKeyId`, no `ec2:Encrypted`.**
- `CopySnapshot` (L4996-5000): has `ec2:Encrypted` but **no `ec2:KmsKeyId`**.
- `CreateVolume` (L5122): **has `ec2:KmsKeyId`** — the lone create path that does.

**Why it matters:** the copy path is exactly where re-encryption key choice happens (`ebs-copy-snapshot.md` L67-76 confirms a copy may select a new/different key). A `Deny unless ec2:KmsKeyId == <approved>` guardrail silently does nothing on CopySnapshot/CopyImage. This is the DR-surface extension of `data-protection` plan **R2**.

**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` for `ec2:CopySnapshot` and `ec2:CopyImage` with a context entry `ec2:KmsKeyId` set — predict the key is simply ignored (no matchable condition) → policy evaluates ALLOW regardless. Compare against `ec2:CreateVolume` where the same context key is honored.

**Severity:** High (guardrail-evasion / unexpected-key re-encryption). Not a cross-tenant breach by itself.

---

## §5 — Recommended Areas of Focus (one block per firing lens, grouped by deep-dive)

### §5A — AMI cross-Region copy (subagent: "Deep-dive AMI cross-Region copy", completed)

- **§5A-H (High) — CopyImage has no KMS/Encrypted condition key.** See §4. CopyImage is strictly weaker than CopySnapshot (which at least carries `ec2:Encrypted`).
- **§5A-X (Medium) — action-family asymmetry + silent auto-grant.** CopySnapshot carries `ec2:Encrypted`; CopyImage does not (§4). Separately, `copy-ami-permissions.md` L60: granting `ec2:CopyImage` **auto-requires** `ec2:CopySnapshot`, so an operator scoping only CopyImage silently also enables the backing snapshot copy. *Oracle:* SimulateCustomPolicy on both actions under a CopyImage-only intent policy.
- **§5A-AA (High) — share/revoke lifecycle is doc-admitted leaky.**
  - `share-amis-with-organizations-and-OUs.md` L27: an AMI can be shared with an org/OU the sharer is **not a member of** (no membership gate).
  - `share-amis-org-ou-manage.md` L163: `Remove-UserId` / unshare **returns success but the AMI remains shared** in the doc-described case = High.
  - **No `ec2:Add/*` condition key exists for images** (snapshots have `ec2:Add/group` + `ec2:Add/userId` at L10047-48) — so image sharing cannot be scoped by grantee in IAM. *Oracle:* two-account canary — share AMI with non-member OU, confirm; unshare, confirm residual access.
- **§5A-EE (Medium) — "whoAMI"-style name confusion.** `ec2-allowed-amis.md` L290: Allowed-AMIs criteria match on `ImageNames` with OR-logic — a permissive allow-list entry can admit an attacker-published AMI whose name matches. *Oracle:* review the account's Allowed-AMIs config for OR-wildcarding.
- **§5A-U (Medium) — BPA-to-AMIs scope.** `block-public-access-to-amis` blocks only **public** sharing, not org/OU sharing — so §5A-AA's org/OU leak is **not** mitigated by enabling AMI BPA. No HARD-STOPs; no drift observed in this child.

### §5B — EBS snapshot cross-Region copy (subagent: "Deep-dive EBS snapshot copy", completed)

- **§5B-X (CRITICAL lead) — EBS direct-API vs CopySnapshot ownership divergence.** `ebsapi-permissions.md` L12-13 **admits** that the EBS direct-APIs (`ebs:GetSnapshotBlock`, `ebs:ListSnapshotBlocks`, `ebs:ListChangedBlocks`) use `ebs:*` permissions distinct from the `ec2:*` snapshot permissions. **`list_ebs.md` has NO `ebs:Owner` condition key** — so the block-read grain cannot be scoped to owned snapshots the way CopySnapshot can. **Open question (the live lead):** do the block-read APIs consult `createVolumePermission` (the share list) at all, or only `ebs:*` IAM? If the former, a shared snapshot's raw blocks are readable by the grantee; if neither gates ownership, this is a cross-account raw-data read. *Oracle:* **two-account canary** — share snapshot from A to B, then from B attempt `ebs:GetSnapshotBlock`; and separately attempt block-read of an **unshared** A snapshot from B holding only `ebs:*`. This is the highest-value refutable claim on the EBS surface.
- **§5B-H (High) — CopySnapshot no `ec2:KmsKeyId`.** See §4. `ebs-copy-snapshot.md` L67-76: copy chooses a (possibly new) encryption key, ungated by IAM.
- **§5B-AA (High, by-design) — copy-then-revoke survival.** `ebs-copy-snapshot.md` L76: once another account copies a shared snapshot, revoking the original share does **not** reach the copy (by design, doc-stated). Snapshots support only `all` / specific-account targets — **no org/OU keys**. *Oracle:* two-account canary — share, copy from B, revoke from A, confirm B's copy survives.
- **§5B-U (Medium ×4) — Block-Public-Access gaps.**
  1. BPA for snapshots is **not default-on** (contrast: AMI BPA became default Oct 2023 — `DocumentHistory.md` L123).
  2. `block-public-access-snapshots.md` L24: snapshot BPA does **not** block an **EBS-backed AMI** from being shared publicly (the AMI carries the snapshot).
  3. L22: no **org-level** BPA for snapshots.
  4. L25: snapshot BPA **not available on Outposts**.
- **§5B-R/U (Medium, Tier-2 drift) — snapshot-lock sample-policy key drift.** `snapshot-lock-iam.md` ships a sample IAM policy that conditions on **`ec2:SnapshotTime`**, but the real cooling-off key is **`ec2:SnapshotCoolOffPeriod`** (`list_ec2.md` L10154 / L8708). A customer copy-pasting the AWS sample gets a WORM-lock guardrail that **does not bind the cooling-off window**. AWS-authored artifact defect. *Oracle:* SimulateCustomPolicy with the sample vs the correct key.
- **§5B-EE (N/A).** Snapshot IDs are `snap-<17 hex>` random — not enumerable. Null hypothesis, pages checked: snapshot-id docs + list_ec2 ID pattern.

### §5C — Amazon Data Lifecycle Manager (subagent: "Deep-dive Data Lifecycle Manager", completed — RICHEST SURFACE)

> Live-twin drift check: `dlm-prerequisites.md` and `AWSDataLifecycleManagerSSMFullAccess.md` byte-identical online as of 2026-10-15.

- **§5C-T1 (CRITICAL — documentation-sanctioned RCE kill chain, every component AWS-authored).** `ExecutionHandler` on `CreateLifecyclePolicy`/`UpdateLifecyclePolicy` is **caller-controlled free text** (`automate-app-consistent-backups.md`, `script-other-use-cases.md`). Chained with **R1** (below), a principal holding only the `dlm-prerequisites.md` **minimal-permissions sample** (`dlm:*` + PassRole scoped to the default role) can self-author/self-tag an SSM document and drive `ssm:SendCommand`-based **RCE as root/SYSTEM on every SSM-managed EC2 instance in the account.** *Oracle:* two chained `SimulateCustomPolicy` calls — (1) PassRole + CreateLifecyclePolicy under the sample; (2) SendCommand under the SSM policy. Live trigger confirmation is explicitly a vuln-hunter phase, out of scope here.
- **§5C-R1 (Critical, Tier-2) — `AllowAllEC2Instances` is unconditioned.** `AWSDataLifecycleManagerSSMFullAccess` (managed-policies.md L202-211, cross-confirmed in the aws-managed-policy reference + live twin): `ssm:SendCommand` on `arn:aws:ec2:*:*:instance/*` with **no Condition at all**. The tag condition gates only *which document*, never *which instance*. *Oracle:* SimulateCustomPolicy for `ssm:SendCommand` on an arbitrary instance ARN under a role holding only this policy → predict ALLOW.
- **§5C-R2 (High, Tier-2) — service roles `Resource:"*"` no condition.** `AWSDataLifecycleManagerServiceRole` / `...ForAMIManagement` (managed-policies.md L36-54, 92-141): `ec2:DeleteSnapshot`, `ec2:ModifySnapshotAttribute`, `ec2:DeregisterImage`, `ec2:ModifyImageAttribute` all on `Resource:"*"` with no ownership/tag condition — blast radius is **every** snapshot/AMI in the account, not just DLM-created ones. *Oracle:* SimulateCustomPolicy against a non-DLM-tagged resource → predict ALLOW.
- **§5C-R3 (High) — ModifyImageAttribute = sharing/exfil primitive.** Same unconditioned grant lets the AMI-management role add `launchPermission` to **any** AMI in the account (not just DLM's) — an exfil primitive if PassRole to this role is reachable from a lower-trust caller.
- **§5C-S2 (High, unresolved — vacuous-truth candidate).** `service-role.md` custom-role SSM sample uses `StringNotLike: {aws:ResourceTag/DLMScriptsAccess: "false"}` on `ssm:SendCommand` against `instance/*`. Negated string operators evaluate **true when the key is absent** (standard IAM semantics, not stated on the page) → the sample likely allows `SendCommand` on any **untagged** instance by default. Shipped as a copy-paste "customize this role" sample (Tier-2). *Oracle:* SimulateCustomPolicy for `ssm:SendCommand` on an untagged instance ARN under this statement alone.
- **§5C-T2 (High, Tier-2) — AWS frames the weaker path as sanctioned.** `automate-app-consistent-backups.md` verbatim: the `aws:ResourceTag` condition is *optional*: *"If you decide to not include that condition key, then you do not need to tag your SSM documents."* AWS's own doc presents the fully-unconditioned variant with no security callout.
- **§5C-B1 (Medium, Tier-2) — PassRole sample missing `iam:PassedToService`.** `dlm-prerequisites.md`'s required-permissions sample scopes `iam:PassRole` by Resource ARN but with **no `iam:PassedToService=dlm.amazonaws.com`** — the exact key `list_dlm.md` documents as recommended for this call. AWS recommends a hardening its own sample omits. *Oracle:* SimulateCustomPolicy for PassRole with `iam:PassedToService` set to a non-DLM service → ALLOW confirms the sample doesn't bind the role to DLM.
- **§5C-B2 (Medium, Tier-2) — default trust policy has no SourceAccount/SourceArn.** `service-role.md`: both default roles trust `dlm.amazonaws.com` + `sts:AssumeRole` with **no Condition by default**; `aws:SourceAccount`/`aws:SourceArn` is only an optional "recommend" add-on.
- **§5C-S1 (Medium, Tier-2) — no DLM-native role-scoping.** DLM condition keys are limited to `aws:RequestTag`/`aws:ResourceTag`/`aws:TagKeys` on the `policy` resource only; `CreateLifecyclePolicy` has **no required Resource type** (`list_dlm.md`, blank Resource cell). There is no DLM-native way to scope *which execution role* a caller references in `policyDetails` — PassRole ARN scoping (§5C-B1) is the only control point.
- **§5C-AA1 (Medium-High) — cross-account snapshot sharing accepts arbitrary account IDs.** `snapshot-ami-policy.md`: cross-account share accepts any 12-digit target with no documented org/membership validation. *Oracle:* two-account canary, A targets non-member B, confirm no secondary gate.
- **§5C-AA2 (Medium) — shared-until-deleted, not default.** `snapshot-ami-policy.md` verbatim: *"If you do not enable automatic unsharing, the snapshot is shared until it is deleted."* Removing a target from config going forward does not retroactively revoke already-shared snapshots (silent in `modify.md`). *Oracle:* two-account canary — remove target, check persistence.
- **§5C-AA3 (Medium) — cross-account COPY event policy KMS tip is optional.** `event-policy.md`: encrypted cross-account copy needs KMS sharing; `kms:GrantIsForAWSResource` hardening is an optional "Tip," not in the default sample.
- **§5C-EE1 (Medium, mixed Tier-2/footgun) — predictable default-role name land-grab.** `dlm-troubleshooting.md`: console- and CLI-created default roles **collide on name** (same name, different path) → documented remedy is to **adopt the existing same-named role with no audit of its trust/permissions**. An attacker with `iam:CreateRole` pre-plants `AWSDataLifecycleManagerDefaultRole` (path `/`) with a backdoored trust policy; the admin's first console DLM use is guided to adopt it. Fixed role name = AWS design (Tier-2); broad `iam:CreateRole` = customer footgun. **Not cross-account** (role names are account-scoped). *Oracle:* review account for a pre-existing role of that exact name with unexpected trust.
- **§5C-U1 (root-cause synthesis).** R1 + S2 + T2 all trade the *same* dimension — instance/tag-level scoping on `ssm:SendCommand` — for convenience, and the docs frame tightening it as optional, never recommended. This is the structural "why" behind the T1 RCE chain.
- **§5C nulls (named):** No DLM cross-account surface for its own `policy` resource (account-scoped, no sharing API — checked `list_dlm.md` in full). No **false absolute** security guarantee found; the unshare-period≤retention-period constraint in `snapshot-ami-policy.md` **is** actually enforced as stated (checked `snapshot-ami-policy.md`, `dlm-elements.md`, `default-policies.md`).

### §5D — Hub-level Lens U (AZ / Local-Zone isolation guarantees)

- **§5D-U1 (deferred — shared-responsibility, not customer-testable here).** Hub L8/L10 assert AZs are "physically separated and isolated" and fail over "without interruption," and Local Zones are "completely isolated from other AWS Zones." These are **AWS-infrastructure guarantees** — their mechanism analysis belongs to `using-regions-availability-zones-attack-research-plan.md` (AZ-name-vs-ZoneId residency SCP footgun; `ModifyAvailabilityZoneGroup` one-way opt-in). **HARD STOP** if any live probe would test physical isolation of AWS's own fabric — that is AWS service-plane, out of scope. The one customer-testable thread: the hub points at `describe-availability-zones` for parent-zone lookup during Local-Zone failover — a **read-only** oracle, already covered in the regions-AZ sibling.

---

## §6 — Threat Model Test Objectives (priority order for a hunter)

1. **§5C-T1 (Critical)** — DLM `ExecutionHandler` + `AllowAllEC2Instances` RCE chain. Two chained SimulateCustomPolicy calls; defer live trigger.
2. **§5B-X (Critical lead)** — EBS direct-API block-read vs CopySnapshot ownership divergence. Two-account canary; the clearest potential cross-account raw-data read.
3. **§5C-R2 / R3 (High)** — DLM service-role `Resource:"*"` delete/share-any primitive.
4. **§5C-S2 (High)** — vacuous-truth `StringNotLike` on untagged instances.
5. **§4 / §5A-H / §5B-H (High)** — copy-path `ec2:KmsKeyId` guardrail-evasion.
6. **§5A-AA / §5B-AA / §5C-AA1/AA2 (High/Medium)** — share-revoke survival + cross-account/org share without membership gate.
7. **§5B-R/U (Medium, Tier-2)** — snapshot-lock sample-policy `ec2:SnapshotTime` vs `ec2:SnapshotCoolOffPeriod` drift.
8. **§5C-B1/B2/EE1 (Medium)** — PassRole/trust-policy hardening gaps; predictable default-role land-grab.

**Standing oracle note:** every lead here is confirmable with **`iam:SimulateCustomPolicy`** (policy-grain claims) or a **two-account synthetic canary** (share/revoke/block-read claims). No lead requires a destructive or state-mutating probe to *confirm existence*; stop at existence.

---

## §7 — Out of Scope / Deferred

- **EC2 Auto Scaling (feature #5)** and **Elastic Load Balancing (feature #6)** are **separate services** (`autoscaling:*`, `elasticloadbalancing:*`) with their own doc trees and IAM references. The hub only *points* at them for resiliency. **Doc-gap — confirm surface first** in a dedicated Auto Scaling / ELB plan; not analyzed here beyond noting their existence.
- **Physical AZ / Local-Zone isolation** (§5D) — AWS infrastructure / shared-responsibility. **HARD STOP** on any probe of AWS's own fabric.
- **Live execution of any oracle** — this plan is documentation-derived; execution is the `aws-vuln-hunter` phase against an authorized, in-scope account with synthetic canary data only.
- **DLM doc-gaps not fetched** (low priority, flagged for completeness): `dlm-stacksets.md` CloudFormation sample templates (possible additional Lens-R CFN artifact surface); `ami-policy.md`, `aws-resource-dlm-lifecyclepolicy.md` (likely duplicative of already-covered `dlm-elements.md`/`service-role.md`).

---

## §8 — Null Hypotheses & Doc Gaps (named, per skill discipline)

- **Lens EE on the copy surface — NULL.** Snapshot (`snap-<17hex>`) and AMI (`ami-<17hex>`) IDs are high-entropy, non-enumerable (checked list_ec2 ID patterns). EE fires only for DLM's **predictable role name** (§5C-EE1), not for resource IDs.
- **No cross-tenant HARD-STOP breach found in copy or DLM surfaces** — the AMI and EBS copy children surfaced no AWS-service-plane escape; the only HARD-STOP is the AZ physical-isolation guarantee (§5D), which is correctly deferred.
- **No false absolute guarantee in DLM docs** (§5C null) — the one checked guarantee (unshare≤retention) is enforced as stated.
- **DLM cross-account surface for its own `policy` resource — NULL** (account-scoped, no sharing API).
- **`list_ec2.md` online truncation** — condition-key tables are only reliable via offline grep; all §3/§4 key facts were grepped offline with line numbers.
- **Zero EC2 org-condition keys** (grep count 0 in list_ec2) — this is *why* §5A-AA / §5B-AA org/OU sharing cannot be IAM-scoped by grantee.
- **EBS direct-API ownership question (§5B-X) is genuinely unresolved from docs** — requires the two-account canary to settle; do not assert either way until run.

---

*Produced by the `security-questionbuilder` skill, documentation-derived and read-only. Three parallel subagent deep-dives (AMI copy, EBS snapshot copy, DLM) folded into a hub plan over `disaster-recovery-resiliency.html`. No live AWS account was contacted. All leads are falsifiable hypotheses with confirm/refute oracles for a downstream `aws-vuln-hunter`.*
