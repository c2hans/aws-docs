# EC2 "Instance Booting From Wrong Volume" (Linux root-volume election by filesystem LABEL/UUID) — Attack Research Plan

**Source of leads:**
- Primary target: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.html (`.md` form fetched; also mirrored at `/work/aws-docs/docs/AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.md`)
- Supporting EC2/EBS docs: `block-device-mapping-concepts.html`, `device_naming.html`, `ebs/latest/userguide/nvme-ebs-volumes.html`, `ebs/latest/userguide/identify-nvme-ebs-device.html`, `ebs/latest/userguide/ebs-using-volumes.html`, `ebs-creating-volume.html`, `ebs-creating-snapshot.html`, `ebs-modifying-snapshot-permissions.html`, `view-shared-snapshot.html`, `share-kms-key.html`, `sharing-amis.html`, `usingsharedamis-confirm.html`, `replace-root.html`
- API reference: `API_AttachVolume.html`, `API_ModifySnapshotAttribute.html`, `API_EbsBlockDevice.html`, `API_RunInstances.html`, `API_CreateReplaceRootVolumeTask.html`, `API_DescribeImages.html`
- IAM: EC2 Service Authorization Reference (offline mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`) — resource/condition-key data for `ec2:AttachVolume`, `ec2:CreateVolume`, `ec2:ModifySnapshotAttribute`, `ec2:RunInstances`, `ec2:CreateReplaceRootVolumeTask`

**Status:** Documentation-derived hypotheses only. Nothing tested against a live account. This is the plan a hunter (`aws-vuln-hunter`) executes later, against an authorized test environment only.

---

## 0. How to use this document
- Each lead is written as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **This is a shared-responsibility boundary case.** The core mechanism is an *OS/Linux* behavior (initramfs root election), not an AWS API bug. The in-scope AWS question is narrower and precise: **does any AWS-level control (block-device mapping, IAM condition keys, snapshot-sharing gates, "root device" semantics) prevent an actor from getting an attacker-influenced filesystem elected as another instance's root `/`, and are AWS's own documented mitigations (UUID in fstab) actually sound?** Keep the hunt on the AWS-controllable seams; do not report "Linux picks root by LABEL" as an AWS defect on its own.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g., a fleet-owned snapshot, a service-account volume, Nitro/host-manager internals), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate.
- **Read-only / non-destructive only.** Use synthetic canary accounts and canary snapshots you own on both sides. Never attach to, relabel, or reboot a volume/instance you do not own in the test environment. Confirm *existence of the boundary gap*, not weaponized impact.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. **Cross-trust root-filesystem substitution.** Demonstrate that a filesystem an actor controls (via a shared/lineage-colliding EBS snapshot) can be elected as the root `/` of an instance it should not control — i.e., the initramfs LABEL/UUID election resolves to the *attacker-derived* volume rather than the AMI-designated root device. Breach = the "wrong" (attacker-influenced) volume is mounted as `/`.
2. **IAM cannot scope the attack away.** Show that no `ec2:AttachVolume` / `ec2:CreateVolume` / `ec2:RunInstances` condition key binds the **owner account or authenticity** of the source-snapshot lineage of a volume being placed into an instance — so a least-privilege author *cannot* write a policy that says "only attach volumes derived from snapshots I own."
3. **Snapshot-share grantee / revocation integrity.** Show whether `ModifySnapshotAttribute createVolumePermission` validates the grantee account (nonexistent/foreign) at share time, and whether un-sharing actually severs volumes already derived from the snapshot (it does not — the derived volume is independent).
4. **AWS mitigation soundness.** Prove or refute AWS's own documented fix: that specifying a UUID in `/etc/fstab` resolves the ambiguity. The target page concedes it does **not** when volumes share snapshot lineage — quantify the residual gap and whether any AWS-level control closes it.
5. **Availability / self-DoS.** Show that the documented remediation (relabel away from `/`) renders the source instance unbootable if the volume is later returned as a root volume without reverting the label — a durable, AWS-exposed footgun.

---

## 2. Components, Assets, and Design

### 2.1 What the mechanism actually is (reconstructed from docs)
A Linux EC2 instance has **two independent "root" decisions** that AWS's docs confirm are decoupled:

- **AWS block-device layer ("root device").** At launch, the AMI's `RootDeviceName` (`/dev/sda1` or `/dev/xvda`, per `device_naming.html`/`DescribeImages`) tells the hypervisor which EBS volume occupies the designated root *slot*. `block-device-mapping-concepts.html`: *"The device names specified in the block device mapping are mapped to their corresponding block devices when the instance first boots… The block device driver for the instance determines which devices are used when the volumes are formatted and mounted."* AWS enforces AZ-locality and IAM on the ARNs — **nothing about filesystem identity.**
- **OS/initramfs layer ("root filesystem `/`").** Target page: *"This is due to how the initial ramdisk in Linux works. It chooses the volume defined as `/` in the `/etc/fstab`, and in some distributions, this is determined by the label attached to the volume partition."* The example shows two attached volumes **both** carrying `LABEL="/"` and the **identical** `UUID=73947a77-…`, and either can win.

**The security-relevant seam is the gap between these two layers.** AWS's "root device" is metadata describing a slot; the *actual* `/` is elected later by the kernel from filesystem LABEL/UUID, over **all** attached volumes, with **no owner/authenticity pinning and no AWS-level uniqueness enforcement**.

### 2.2 Assets
- **Instance identity & its IMDS role credentials.** If an attacker-controlled filesystem boots as `/`, attacker-planted userspace (`/etc/passwd`, authorized_keys, systemd units, cron) runs in the victim instance context and can read the instance profile credentials from IMDS. **This is the real prize** and sets the severity ceiling.
- **Data on the real root volume** (confidentiality) and **bootability** of the instance (availability).
- **EBS snapshots** as a cross-account *delivery* object (publicly or privately shareable).

### 2.3 Identifier shapes (the collidable namespace — key to Lens EE)
- **Filesystem LABEL** — free-form string; the "boot by label" distros resolve `/` to whatever volume has `LABEL=/`. Attacker-settable before snapshotting.
- **Filesystem UUID** — 128-bit, normally unique, **but** `ebs-creating-volume.html`: *"If you create a volume from a snapshot, the volume begins as an exact replica of the volume that was used to create that snapshot."* → a volume from the same snapshot lineage carries the **same** UUID. The target page states this explicitly as a named failure mode.
- Both identifiers are **owner-blind**: the kernel resolver has no concept of which AWS account owns the volume.

### 2.4 ASCII pipeline (how an attacker-influenced filesystem reaches an instance's `/`)
```
Attacker account A                         Victim/target account B
-----------------                          -----------------------
root vol (LABEL="/",                        instance I (AMI RootDeviceName=/dev/xvda,
  UUID=X)                                      real root vol R: LABEL="/", UUID=X')
   |                                                |
   | CreateSnapshot                                 |
   v                                                |
 snap S (block-for-block copy; LABEL/UUID baked in) |
   |                                                |
   | ModifySnapshotAttribute                        |
   | createVolumePermission add (userId=B | group=all)
   v                                                |
 S shared ----------> [B creates volume V from S] --+--> AttachVolume(V -> I, any device name)
                       CreateVolume / RunInstances        (AWS checks: AZ match + IAM on ARNs.
                       BlockDeviceMapping.Ebs.SnapshotId=S  NO filesystem-identity / owner check)
                                                          |
                                                          v
                                           Reboot I -> initramfs elects "/" by LABEL/UUID
                                           over {R, V}. If V wins -> attacker-controlled
                                           filesystem is the running root. IMDS role creds,
                                           persistence, data all follow.
```
**Precondition that bounds realism (state loudly):** step "B attaches V to I" requires either (a) the victim to be socially/operationally induced to create+attach a volume from the shared snapshot (supply-chain / shared-catalog / "latest snapshot" automation), or (b) an actor who *already* holds `ec2:AttachVolume` on instance I (intra-account privilege/role confusion, or a compromised-but-scoped automation role). There is **no** documented path for an unsolicited cross-account actor to attach a volume to a stranger's instance. The hunt's cross-account value therefore concentrates on **(1) the shared-snapshot supply-chain / name-resolution variant** and **(2) the intra-account "scoped role cannot be prevented from doing this" IAM-gap variant.**

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Attacker account A | Victim account B's instance root `/` | Shared snapshot → volume → attach → initramfs LABEL/UUID election | A filesystem whose LABEL/UUID attacker set is mounted as `/` on B's instance → attacker userspace executes in B's instance context (IMDS creds reachable). **Breach.** |
| Attacker account A | Any account (public) | `ModifySnapshotAttribute createVolumePermission group=all` | A snapshot carrying `LABEL=/` + a chosen UUID is world-createable → delivery object exists. Corroborating, not itself a breach. |
| Scoped IAM role R (intra-account) | Instance it should not fully control | `ec2:AttachVolume` at `/dev/xvda`/any name + reboot | A role granted only "attach volumes" flips an instance's running root with no condition key able to prevent it → privilege/integrity beyond intent. **Breach (IAM-gap).** |
| Automation that resolves "a snapshot" by name/tag/"latest" without owner filter | The instance it builds | `CreateVolume`/`RunInstances BlockDeviceMapping.SnapshotId` resolving to an attacker-published snapshot | The pipeline attaches an attacker-owned snapshot's filesystem (whoAMI-shaped) → root election can flip. **Breach (authenticity-omission).** |
| Volume owner (relabel remediation) | Source instance bootability | `e2label`/`xfs_admin` changes LABEL away from `/` | Returning the relabeled volume as a root volume elsewhere → that instance will not boot (ramdisk can't find `LABEL=/`). **Availability breach / documented footgun.** |
| Any customer surface | **AWS service plane** | A fleet-owned snapshot / service volume appearing in resolution | **HARD STOP** — any AWS-owned snapshot/volume/account identity is out of scope; preserve evidence, flag for disclosure. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internet-callable | Authorized callers | Notes (routing to lenses) |
|---|---|---|---|---|---|---|
| `AttachVolume` | EC2 API | Existing | Mutating | Yes (SigV4) | IAM on `instance*` **and** `volume*` ARNs | Volume-resource condition keys: `ec2:ParentSnapshot`, `ec2:ParentVolume`, `ec2:Encrypted`, `ec2:VolumeID/Type/Size`, `aws:ResourceTag`. **No `ec2:Owner` on the volume resource.** Caller freely chooses the device-name string. → **S, X, EE** |
| `CreateVolume` | EC2 API | Existing | Mutating | Yes | IAM on `volume` | Takes `SnapshotId` (owned or shared-with-you). Keys include `ec2:ParentSnapshot`, `ec2:Encrypted`, `ec2:KmsKeyId`. No ownership filter on the source snapshot's account. → **S, EE, H** |
| `RunInstances` | EC2 API | Existing | Mutating | Yes | IAM | `BlockDeviceMapping.Ebs.SnapshotId` ("Required: No", any accessible snapshot). Wires a snapshot straight into a launch spec as an attached device. → **X, EE** |
| `ModifySnapshotAttribute` | EC2 API | Existing | Mutating (permissions mgmt) | Yes | IAM on `snapshot*` | `createVolumePermission`: `group=all` (public) or `userId=<acct>` (private). Condition keys: `ec2:Add/userId`, `ec2:Add/group`, `ec2:Remove/userId`, `ec2:Remove/group`, `ec2:Owner`, `ec2:SnapshotID`. **These let a customer *restrict* sharing — test whether they're used/usable.** → **AA, S** |
| `CopySnapshot` / `CreateSnapshot` | EC2 API | Existing | Mutating | Yes | IAM | Produces the delivery object preserving filesystem LABEL/UUID. → **EE** |
| `CreateReplaceRootVolumeTask` | EC2 API | Existing | Mutating | Yes | IAM on instance/volume | Validates AZ, available state, not-attached, encryption-compat — **no filesystem-identity concept.** Cannot fix a LABEL/UUID collision; swaps the AWS slot only. → **X, U** |
| `DescribeImages` | EC2 API | Existing | Non-mutating | Yes | IAM | Returns `RootDeviceName`/`RootDeviceType` — the *AWS* notion of root, which ≠ OS `/`. → **U** |
| initramfs root election | OS internal | Existing | n/a | No | n/a (runs in guest) | Resolves `/` by LABEL then UUID over all attached volumes; **owner-blind, no AWS enforcement.** The core seam. → **EE, U, L** |

**Undocumented/hidden-knob sweep:** `AttachVolume`'s `Device` parameter accepts any device-name string including the AMI's root slot name with no API-level validation tying it to root semantics (per API ref). `BlockDeviceMapping.Ebs.SnapshotId` is documented "Required: No" with no owner constraint. No console surface warns that attaching a second `LABEL=/` volume can hijack boot — the only warning lives on the troubleshooting page itself.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### AREA 1 — Owner-blind root-filesystem resolution (Lens EE: predictable-name / shadow-resource selection) — **PRIORITY 1**
**Background.** The initramfs elects `/` by filesystem LABEL (`=/`) or UUID over *all* attached volumes. LABEL is an attacker-chosen string; UUID is replicated block-for-block into any volume created from the same snapshot lineage (`ebs-creating-volume.html`: "exact replica"; target page: same-snapshot volumes "share a UUID"). This is structurally identical to the **whoAMI** / `resolve:ssm` class the catalog flags under the *authenticity-filter-omission → attacker-resource selection* variant: a resolver matches a **name/identifier** with **no owner pinning**.
**Security Concern.** If an actor can place a volume carrying `LABEL=/` (or the victim-root UUID) onto a target instance, the kernel may elect it as `/` — booting attacker-controlled userspace with the victim instance's identity (IMDS role creds). AWS enforces nothing about filesystem-identity uniqueness across attached volumes (block-device-mapping docs confirm AWS only maps slots; it does not dedupe LABEL/UUID).
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A canary volume whose ext4 LABEL is set to `/` and whose UUID matches the instance's real root, attached alongside the real root and rebooted, can win the `/` election on a boot-by-label distro (e.g., older Amazon Linux). → **Mechanism:** target page example (`e2label /dev/xvdf1` → `/`, both volumes `UUID=…840778`). → **Oracle:** after reboot, `findmnt /` / `blkid` of the live `/` resolves to the canary volume's device, not the AMI root slot. → **Preconditions:** two canary volumes in one test instance you own; distro that resolves root by LABEL. → **Cost:** low. → **Severity-if-true:** High (intra-account integrity); **Critical** if demonstrated reachable via a cross-account shared snapshot with no victim collusion beyond "used a shared snapshot."
- **Claim:** An automation that resolves a snapshot by *name/tag/"latest"* without an `--owners`/owner-ARN filter can be steered to an attacker-published snapshot (whoAMI-for-snapshots). → **Mechanism:** `CreateVolume`/`RunInstances` accept any accessible `SnapshotId`; sharing is public via `group=all`. → **Oracle:** the pipeline creates a volume from the attacker snapshot id. → **Severity:** High–Critical depending on whether that volume lands at/with a colliding root LABEL.
**Doc evidence:** target page; `ebs-creating-volume.html`; `block-device-mapping-concepts.html`. **Severity-if-true:** High–Critical.
**Stop condition:** root election confirmed to resolve to the non-AMI volume once. Do not weaponize IMDS creds; do not touch any non-canary instance.

### AREA 2 — AWS-level controls cannot scope the attack (Lens S + Lens U: condition-key semantics vs documented guarantee) — **PRIORITY 2**
**Background.** `ec2:AttachVolume`'s **volume** resource exposes `ec2:ParentSnapshot`, `ec2:ParentVolume`, `ec2:Encrypted`, `ec2:VolumeID/Type/Size`, `aws:ResourceTag` — but **not** `ec2:Owner`. `CreateVolume` likewise keys on `ec2:ParentSnapshot` (an id the actor supplies) but not on the *owner account* of that snapshot.
**Security Concern.** A least-privilege policy author **cannot** express "only allow attaching/creating volumes whose source snapshot I own" — the only lineage key (`ec2:ParentSnapshot`) binds a snapshot *id*, which an attacker's shared snapshot also has. The documented AWS mitigation (UUID in fstab) is conceded by AWS to fail on shared lineage. So *both* the IAM control and the fstab guidance have a documented hole.
**High-level Test Scenarios:**
- **Claim:** No `AttachVolume`/`CreateVolume` IAM condition can deny a volume derived from a *foreign-owned* snapshot while allowing one from an owned snapshot, given only the volume being named. → **Mechanism:** `list_ec2.md` AttachVolume volume-resource key set lacks `ec2:Owner`; `ec2:ParentSnapshot` = id only. → **Oracle:** `iam:SimulateCustomPolicy` — construct the tightest possible deny and show a foreign-lineage volume still passes (or that the policy cannot even be expressed). → **Cost:** zero (Simulate, no resources). → **Severity:** Medium–High (it is an AWS-owned condition-key coverage gap; report as least-privilege-expressibility gap). 
- **Claim:** AWS's documented UUID remediation is advisory only — nothing re-checks or enforces UUID uniqueness across attached volumes. → **Mechanism:** target page: "if both volumes come from the same snapshot… they share a UUID." → **Oracle:** attach two same-lineage volumes; confirm no AWS API rejects or warns. → **Severity:** Low–Medium (doc-vs-enforcement; AWS-owned).
**Doc evidence:** `list_ec2.md` (AttachVolume/CreateVolume condition keys); target page UUID paragraph. **Severity-if-true:** Medium–High. **Stop:** once the expressibility gap is shown via Simulate.

### AREA 3 — Snapshot-share grantee validation & revocation completeness (Lens AA) — **PRIORITY 3**
**Background.** `ModifySnapshotAttribute createVolumePermission` shares a snapshot publicly (`group=all`) or to a specific `userId`. Owner-side doc warns "share only with people you trust with ALL your snapshot data," but there is **no consumer-side trust warning** on `view-shared-snapshot.html` (the subagent confirmed the AMI-sharing pages carry a due-diligence warning; the snapshot-consumption page does not).
**Security Concern.** (a) Is the grantee `userId` validated to be a real/eligible account at share time, or can a nonexistent/typo'd account be added (grant pre-registration)? (b) After `Remove/userId` (un-share), does a volume the grantee **already created** from the snapshot get severed? Per "exact replica," the derived volume is independent — un-sharing does **not** retract already-created volumes.
**High-level Test Scenarios:**
- **Claim:** Un-sharing a snapshot does not invalidate volumes already created from it. → **Oracle:** share → grantee `CreateVolume` → owner `Remove/userId` → grantee volume still usable. → **Severity:** Medium (revocation-completeness gap; mostly expected behavior — report as hardening/doc-gap, not a bug unless docs promise otherwise).
- **Claim:** `ec2:Add/group`/`ec2:Add/userId` condition keys can be used by a customer to *deny* public sharing (`Add/group=all`) org-wide — verify they actually gate it. → **Oracle:** `SimulateCustomPolicy` with a deny on `ec2:Add/group=all`. → **Severity:** Informational (confirms a usable guardrail exists; its *absence by default* is the footgun).
**Doc evidence:** `ebs-modifying-snapshot-permissions.html`; `view-shared-snapshot.html` (no consumer warning); `list_ec2.md` ModifySnapshotAttribute keys. **Severity-if-true:** Medium. **Stop:** once grantee/revoke behavior observed with canary accounts.

### AREA 4 — Action-family parity: every path that places a filesystem into an instance (Lens X) — **PRIORITY 4**
**Background.** Multiple AWS paths put an EBS volume into an instance: `AttachVolume`, `RunInstances BlockDeviceMappings`, `CreateReplaceRootVolumeTask`, and `CreateVolume`+attach. Each validates different things (AZ, availability, encryption-compat) and **none** validate filesystem LABEL/UUID or source-snapshot ownership.
**Security Concern.** A control or warning present on one path but absent on a sibling is the classic parity gap. `ReplaceRootVolume` explicitly "updates the block device mapping to the replacement volume id" but has no filesystem-identity concept — so it can install a volume whose `/` LABEL collides, and cannot be used to *fix* a collision either.
**High-level Test Scenarios:**
- **Claim:** `RunInstances` with a `BlockDeviceMapping` pointing at a foreign/shared snapshot as a *non-root* device, plus a root AMI, yields two `LABEL=/` filesystems at first boot. → **Oracle:** launch a canary instance with such a mapping; `blkid` shows duplicate `LABEL=/`. → **Severity:** High (pre-wired collision at launch, no attach step needed).
- **Claim:** No path emits a warning/validation when a second `LABEL=/` or duplicate-UUID volume is introduced. → **Oracle:** exercise all four paths; record which (if any) warn. → **Severity:** Low–Medium (parity/doc).
**Doc evidence:** `API_RunInstances.html`/`API_EbsBlockDevice.html`; `replace-root.html`/`API_CreateReplaceRootVolumeTask.html`; `API_AttachVolume.html`. **Severity-if-true:** High. **Stop:** once duplicate-LABEL state is reproduced on a canary.

### AREA 5 — Encrypted-lineage variant (Lens H: CMK / encryption-context) — **PRIORITY 5**
**Background.** Encrypted snapshots require CMK sharing (`share-kms-key.html`: grantee needs `kms:Decrypt`, `GenerateDataKey`, etc.); default-KMS-key snapshots cannot be shared; encrypted snapshots cannot be made public.
**Security Concern.** Encryption raises the bar (explicit CMK grant) but does not change the LABEL/UUID election. Question: does a *copy* of a shared encrypted snapshot re-encrypted under the grantee's own key still preserve the filesystem UUID (it should — re-encryption is block-level, not filesystem-level)?
**High-level Test Scenarios:**
- **Claim:** Re-encrypting a shared snapshot under a new CMK preserves the filesystem UUID/LABEL, so the collision survives the encryption boundary. → **Oracle:** `CopySnapshot` with a new KMS key → `CreateVolume` → `blkid` shows the original UUID/LABEL. → **Severity:** Medium (confirms encryption is not a mitigation for the collision).
**Doc evidence:** `share-kms-key.html`; `ebs-modifying-snapshot-permissions.html`. **Severity-if-true:** Medium. **Stop:** once UUID preservation across copy+re-encrypt is confirmed.

### AREA 6 — Availability / self-DoS via remediation (Lens L) — **PRIORITY 6**
**Background.** Target page "Important": after relabeling the attached volume away from `/`, *"If you intend to detach the volume with the new label and return it to another instance to use as the root volume, you must perform the above procedure again and change the volume label back… Otherwise, the other instance does not boot because the ramdisk is unable to find the volume with the label `/`."*
**Security Concern.** The AWS-sanctioned fix creates a durable bricking footgun: a volume legitimately used as a root elsewhere becomes unbootable if returned without reverting the label. In an automation/role context, an actor with relabel-capable access to a volume could render a *future* root-boot of that volume impossible.
**High-level Test Scenarios:**
- **Claim:** A volume whose `/` LABEL was removed will not boot as a root volume on another instance. → **Oracle:** relabel a canary root volume, move it to a fresh canary instance as root, observe boot failure. → **Severity:** Medium (single-tenant availability; High only if it crosses a tenant boundary in the test env — it should not; keep intra-account).
**Doc evidence:** target page Important block. **Severity-if-true:** Medium (single-tenant → largely out-of-scope self-DoS; include for completeness). **Stop:** once boot-failure reproduced once on a canary.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attacker-influenced filesystem elected as `/` | initramfs LABEL/UUID resolver | AWS "root device" slot metadata (`RootDeviceName`) — **does not govern OS `/`**; prove the decoupling |
| Cross-account delivery of a colliding filesystem | `ModifySnapshotAttribute createVolumePermission` + `CreateVolume`/`RunInstances SnapshotId` | Owner-side "share only with trusted" warning; **no consumer-side warning**, no owner-pinning condition key — prove the gap |
| Least-privilege policy cannot prevent foreign-lineage volume attach | `ec2:AttachVolume`/`ec2:CreateVolume` condition keys | `ec2:ParentSnapshot` (id only); **absent `ec2:Owner` on the volume resource** — prove inexpressibility via `SimulateCustomPolicy` |
| UUID-in-fstab mitigation is unsound on shared lineage | fstab / initramfs | AWS's documented UUID remedy — prove residual collision when volumes share a snapshot |
| Relabel remediation bricks future root boot | `e2label`/`xfs_admin` guidance | Target page "Important" note — prove the availability footgun |
| Snapshot-share revocation does not retract derived volumes | `ModifySnapshotAttribute Remove` | "original snapshot remains unaffected" / derived volume is an "exact replica" — prove independence |
| Encryption does not stop the collision | `CopySnapshot` + CMK | CMK-share requirement — prove UUID/LABEL survives re-encrypt |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **"Linux elects root by LABEL" as a standalone Linux/distro behavior** — not an AWS defect on its own; only the AWS-controllable seams (IAM condition-key coverage, snapshot-share gates, block-device semantics, AWS's own mitigation guidance) are in scope.
- **Unsolicited cross-account attach.** There is no documented path for an external actor to attach a volume to a stranger's instance without the victim creating/attaching attacker-derived storage (supply chain) or the actor already holding `ec2:AttachVolume` on the instance. Do not claim remote cross-account RCE without one of those preconditions.
- **IMDS/role-credential weaponization.** Confirming the root flips is the PoC; do **not** harvest or use the instance-profile credentials.
- **AWS service-plane / fleet-owned snapshots or volumes** — HARD STOP + disclosure.
- **Single-tenant self-DoS** (Area 6) — included for completeness; largely a customer footgun, low priority.
- **Shared EBS backend / Nitro host internals / hypervisor** — out of scope.
- **Windows instances** — the LABEL/UUID election mechanism described is Linux-specific; Windows boot-disk selection is a separate, un-analyzed surface (doc-gap).

## 8. Null hypotheses / doc gaps (lenses checked that did not fire)
- **Lens B/C (PassRole / credential vending) — N/A.** Read `API_AttachVolume`, `API_RunInstances`, `replace-root.html`; no role-ARN-as-input or STS session-scoping surface on this feature. (The *consequence* of a flipped root is IMDS role-cred exposure, but that is downstream impact, not a vending bug here.)
- **Lens G (SSRF) — N/A.** No field on these pages is a URL/host the service dereferences server-side. (Checked block-device-mapping, snapshot-sharing, attach, replace-root.)
- **Lens D/V (network segmentation) — N/A at this layer.** No ENI/control-plane reachability surface on the volume/snapshot APIs.
- **Lens F (translation/injection) — doc-gap, low.** The only parsing seams are ext4/xfs LABEL and `/etc/fstab`; whether a crafted LABEL (e.g., containing whitespace/quotes) could confuse `e2label`/`blkid`/initramfs parsing is unexamined and OS-level — mark "doc-gap — confirm surface first," low priority.
- **Lens J/K/M/N/P/Q/T/W/Y/BB/CC/DD/FF — N/A.** No OAuth/3P linking, LLM/agent, session-id, namespace-migration, identity-proofing, upload-validation (snapshot content is handled under EE/AA, not as a classic upload-parse surface), secret-storage, attestation, transport/TLS, HTTP-edge-parser, upstream-context, caching, or JWT surface on the target or its immediate supporting pages.
- **Lens R (AWS-authored IAM artifact) — N/A for this page.** No AWS-managed policy / sample policy / CFN / runbook ships specifically for this troubleshooting feature. (If an EBS sample policy page is later found to grant `AttachVolume` on `volume/*` unconditioned, route it back to Lens R/S.)
- **Lens I (tagging/ABAC) — minor.** `aws:ResourceTag` is available on AttachVolume/volume; ABAC is not the access-control mechanism for root election, so not load-bearing.
- **Lens O (audit) — Informational.** Whether CloudTrail distinctly records "a second LABEL=/ volume was attached" or the boot-time root flip is unexamined; the root election happens in-guest and is unlikely to produce a control-plane event — note as a detection-gap enabler.

---

### Appendix — Severity framing recap for this feature
- **Critical:** attacker-controlled filesystem elected as another **account's** instance root with no collusion beyond consuming a shared/public snapshot (supply-chain), yielding that instance's IMDS role identity.
- **High:** intra-account integrity flip via a scoped role that IAM cannot be configured to prevent; duplicate-`LABEL=/` pre-wired at `RunInstances`.
- **Medium:** condition-key coverage gap (no `ec2:Owner` on AttachVolume volume resource); encryption-does-not-mitigate; revocation-incompleteness.
- **Low / Informational:** UUID-mitigation doc-vs-enforcement gap; single-tenant relabel self-DoS; audit/detection gap.

*Plan ends. The hunter should begin at Area 1 on a canary instance it owns, confirm the root-election flip once, then validate Areas 2–3 primarily with `iam:SimulateCustomPolicy` (no live resources), and stop at the first AWS-service-plane signal.*
