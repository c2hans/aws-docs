# EC2 "Troubleshoot Linux instances with failed status checks" (Manual Volume-Recovery + Boot-Chain Modify) — Attack Research Plan

Source of leads:
- **Primary page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html (`.md` twin fetched live 2026-10-17). This is the **Linux failed-status-check** troubleshooting guide: review status checks, retrieve system logs, and ~20 system-log-error recovery runbooks (OOM, device I/O, kernel, filesystem, GRUB, SELinux, MAC, Xenbus).
- **Linked UserGuide pages:** `monitoring-system-instance-status-check.md`, `UsingAlarmActions.md` (CloudWatch stop/terminate/reboot/recover), `Stop_Start.md`, `terminating-instances.md`, `resize-limitations.md`, `instance-types.md`, `Using_ChangingAttributesWhileInstanceStopped.html` ("Modify a stopped instance"), `UserProvidedKernels.html` (PV-GRUB), EBS `ebs-attaching-volume` / `ebs-detaching-volume` / `EBSEncryption`.
- **API refs:** `API_ModifyInstanceAttribute.html`, `API_AttachVolume.html`, `API_DetachVolume.html`, `API_GetConsoleOutput.html`, `API_CreateImage.html`.
- **Authoritative IAM surface:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (read offline by targeted grep; rows cited by line below). `list_amazonec2.html` now 302-redirects to the reference index — use `list_ec2.html` online.

**Status: documentation-derived hypotheses only. Nothing has been tested against any live AWS account.** For a downstream authorized hunter (`aws-vuln-hunter`) to execute in a two-account / two-team canary lab.

---

## Scope / relationship to sibling plans (READ FIRST — avoids duplicated effort)

Two sibling plans already **own** adjacent surface. This plan **cross-references rather than restates** them, and OWNS the one mechanism distinctive to *this* page: the **manual "recovery instance" EBS volume workflow** and **boot-chain (kernel/ramdisk) attribute modification**.

- `[[ec2-instance-troubleshoot-attack-research-plan]]` — OWNS serial console, console-output/screenshot retrieval, Windows password reset, EC2 Instance Connect, diagnostic interrupts, EC2Rescue/SSM-automation recovery, **replace-root-volume**, boot-from-wrong-volume. **GetConsoleOutput** cross-tenant read and the serial-console gateway live there.
- `[[troubleshoot-unreachable-instance-attack-research-plan]]` — OWNS `GetConsoleOutput`/`GetConsoleScreenshot` confidentiality boundary, **CloudWatch recover** alarm action, Stop/Start lifecycle, the "instance ID is `i-`+17 hex, no checksum, blind enumeration infeasible" testability gate.
- `[[attach-iam-role-attack-research-plan]]` / `[[iam-roles-for-amazon-ec2-attack-research-plan]]` — OWN `iam:PassRole`, IMDS credential vending, and the canonical `ec2:ModifyInstanceAttribute(userData)` privesc. **This plan extends that primitive to the sibling boot-chain attributes `kernel`/`ramdisk`/`blockDeviceMapping` that THIS page legitimizes.**
- `[[ExamplePolicies_EC2-attack-research-plan]]` / `[[security-iam-awsmanpol-attack-research-plan]]` — OWN the Lens R AWS-managed/sample-policy audit.

**What THIS plan owns:** (1) the manual **Detach-foreign-volume → Attach-to-my-recovery-instance → mount → read/modify root filesystem** data-at-rest breach; (2) **boot-chain modification** (`kernel`/`ramdisk`/`blockDeviceMapping`) as a code-exec / tamper primitive and its coarse single-action IAM gate; (3) the documented **CreateImage reboot-without-RebootInstances** twin.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **Read-only settlement first.** Condition-key scoping / "which attributes a grant covers" / "does a condition key apply to this action" leads settle **read-only** via `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` — no resource touched. Ownership-vs-existence, cross-team resolution, encrypted-volume KMS consent, and mount-and-read leads are **live-only** → hand to `aws-vuln-hunter` with a synthetic **two-team / two-account** canary (dummy instances, canary secret files baked into the victim root volume and user-data).
- **DryRun is caller-IAM-only** — `ModifyInstanceAttribute`/`AttachVolume` accept `DryRun`, but it is evaluated **before resource resolution**, so a `DryRunOperation` pass proves only that the caller holds the action, NOT that the target instance/volume ownership check would pass. Do **not** treat DryRun as an IDOR/ownership oracle.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** — a mounted volume that turns out to belong to an AWS-managed/shared fleet host; an attached volume whose data decrypts under an AWS-owned KMS key you were never granted; a `blockDeviceMapping` change rejected with "attached to AWS-managed resources"; an IMDS cred (after a userData/kernel code-exec) that resolves to an AWS service role — **stop, preserve evidence, flag for AWS-Security disclosure.** Do not escalate.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Read another team's/account's data at rest** by attaching that owner's EBS **root volume** to a recovery instance you control, mounting it, and reading `/etc/shadow`, SSH host/user keys, app secrets, and baked-in credentials — the recovery workflow this page prescribes, turned against a volume the caller does not own. (Critical if cross-account; High cross-team.)
2. **Code execution under an instance's existing instance-profile role without `iam:PassRole`** by rewriting the instance's `userData` **or** `kernel`/`ramdisk` via `ec2:ModifyInstanceAttribute` and triggering a (re)boot — stealing that role's IMDS credentials. (High–Critical.)
3. **Over-broad single-action footprint:** demonstrate that one `ec2:ModifyInstanceAttribute` grant (no `ec2:Attribute` condition) lets the holder also flip `disableApiTermination`, replace `groupSet` (security groups), and set `instanceInitiatedShutdownBehavior=terminate` — capabilities that read like "fix the kernel." (High.)
4. **Mount an encrypted foreign volume** and determine whether KMS consent is actually required, or whether `AttachVolume` silently makes the data readable. (High.)
5. **Reboot/tamper a non-owned instance via a twin action** (`CreateImage` reboots without `ec2:RebootInstances`; `DetachVolume Force`) that bypasses the obvious permission. (Medium–High.)

---

## 2. Components, Assets, and Design

**Customer-facing interface:** EC2 console + EC2 Query/SDK API (SigV4 IAM). No service-specific wire protocol — every step is a standard EC2 control-plane action, plus **OS-level filesystem operations the operator performs inside the recovery instance** (mount, fsck, edit `/etc/fstab`, `etc/sysconfig/selinux`, GRUB `menu.lst`).

**Actions this page invokes (the attack surface):**
- `ec2:GetConsoleOutput` — "Actions → Monitor and troubleshoot → Get system log" (confidentiality; **owned by siblings**, cross-ref only).
- `ec2:RebootInstances` / `ec2:StopInstances` / `ec2:StartInstances` / `ec2:TerminateInstances` — lifecycle used in nearly every runbook.
- `ec2:DetachVolume` + `ec2:AttachVolume` — the **recovery-instance workflow** core: "Detach the root volume. Attach the root volume to a known working instance."
- `ec2:ModifyInstanceAttribute` — "Modify the kernel and ramdisk attributes to use a newer kernel"; also `blockDeviceMapping` (DeleteOnTermination), `instanceType`.
- `ec2:CreateImage` / `ec2:ModifyImageAttribute` / `ec2:RegisterImage` — "Modify the AMI … correcting the kernel."
- CloudWatch `cloudwatch:PutMetricAlarm` with `ec2:Recover|Stop|Terminate|Reboot` alarm actions (`UsingAlarmActions`), and Auto Scaling health-check replacement — **recover owned by sibling**, cross-ref.

**Assets:** the failed instance's **EBS root volume and every byte on it** (the crown jewel for this page); the live system-log/console buffer; the operator-controlled **recovery ("known working") instance**; the AMI; the kernel (`aki-*`) / ramdisk (`ari-*`) images; each instance's attached **instance-profile role** (reachable via IMDS once you get code-exec on the instance).

**Accounts / tenancy:** EBS volumes and EC2 instances are **account-local** — there is no documented cross-account `AttachVolume`, and no `ec2:ResourceAccount`-style ownership condition key exists (the only ownership-ish keys are `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:VolumeID`, `ec2:InstanceID`). **Consequence:** the realistic blast radius is **cross-TEAM within one account** via a wildcard (`Resource:"*"`) or tag-mis-scoped IAM policy, not cross-account. (True cross-account only if a shared snapshot/volume or RAM relationship bridges accounts — note and test separately.)

**ASCII pipeline (the recovery workflow this page prescribes):**
```
                        (1) StopInstances
   [ FAILED INSTANCE ] ------------------> stopped
          | root EBS vol  (2) DetachVolume
          v
   [ detached vol V ] --(3) AttachVolume to /dev/sdf--> [ RECOVERY INSTANCE  <-- attacker-controlled ]
                                                              |
                                                     (4) mount V; read/modify
                                                         /etc/shadow, SSH keys,
                                                         secrets, fstab, selinux, GRUB
                                                              |
   [ FAILED INSTANCE ] <--(6) AttachVolume as root <--(5) DetachVolume V
          | (7) StartInstances
          v
   boot with attacker-modified root FS / kernel / ramdisk
```
The security question is whether the authz on steps (2),(3),(5),(6) binds the **owner** of volume V and of the recovery instance, or merely their **existence / a tag the caller can set**.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller (team A) | Team B's EBS **root volume** V | `AttachVolume(volume=V, instance=my-recovery)` then OS mount | Recovery instance mounts & reads V's filesystem — **any byte of a volume the caller does not own = breach** (Critical x-account / High x-team) |
| Caller (team A) | Team B's **instance** | `ModifyInstanceAttribute` / `DetachVolume` / `GetConsoleOutput` naming its `i-…` id | The action succeeds (attribute changes / volume detaches / log returns) on an instance the caller does not own |
| Caller's IAM identity | Instance's **instance-profile role** | `ModifyInstanceAttribute(userData\|kernel\|ramdisk)` + reboot → code runs on instance → IMDS | Obtaining STS creds for a role the caller holds no `iam:PassRole` for |
| Caller | **KMS CMK** of an encrypted volume | `AttachVolume` of an encrypted foreign volume, then read | Plaintext of a volume encrypted under a key the caller was never granted `kms:Decrypt` on |
| Narrow-permission holder | Broad instance mutation | one coarse `ec2:ModifyInstanceAttribute` | Flipping `disableApiTermination`/`groupSet`/`shutdownBehavior` from a grant intended only for "kernel fix" |
| Any customer action | **EC2/EBS service plane** (shared fleet, AWS-managed resources) | mount / attach / modify hitting an AWS-owned resource | Any AWS-owned identity/key/host reached — **HARD STOP + disclose** |

---

## 4. API / Interface Inventory

| Name | Method (HTTP) | Mutating? | Ext-facing? | Functionality | Callable from Internet | Authorized callers | Notes (IAM: list_ec2.md) |
|---|---|---|---|---|---|---|---|
| `AttachVolume` | POST (Query) | **Mutating** | External | Attach EBS vol to instance at device name | Yes (ec2 endpoint) | IAM principals w/ `ec2:AttachVolume` | **Two required resources `instance*` + `volume*`**, each with own condition keys; keys incl. `ec2:VolumeID`,`ec2:Encrypted`,`ec2:ParentSnapshot`,`ec2:InstanceID`,`ec2:ResourceTag`. No account/owner key. (L4873) |
| `DetachVolume` | POST | **Mutating** | External | Detach EBS vol (optionally `Force`) | Yes | `ec2:DetachVolume` | `Force` can detach without OS unmount → data risk; parity with Attach |
| `ModifyInstanceAttribute` | POST | **Mutating** | External | Modify ONE attribute of an instance | Yes | `ec2:ModifyInstanceAttribute` | One action gates `kernel\|ramdisk\|userData\|groupSet\|blockDeviceMapping\|disableApiTermination\|disableApiStop\|instanceInitiatedShutdownBehavior\|instanceType\|...`. Per-attr only via opt-in `ec2:Attribute` / `ec2:Attribute/${AttributeName}`. "To modify some attributes, the instance must be stopped." (L8808) |
| `GetConsoleOutput` | POST | Non-mut (Read) | External | Return system/boot log buffer | Yes | `ec2:GetConsoleOutput` | instance* only; tag/`InstanceID` scoping. **Confidentiality boundary owned by siblings** — cross-ref |
| `CreateImage` | POST | **Mutating** | External | Create AMI from instance | Yes | `ec2:CreateImage` | IAM desc: *"This action can **reboot instances** as part of the image creation process, **even without RebootInstances permissions**. To prevent … use the NoReboot parameter"* (L5143) — **documented reboot twin** |
| `RebootInstances`/`Stop`/`Start`/`TerminateInstances` | POST | Mutating | External | Lifecycle | Yes | respective `ec2:*` | Availability actions; `TerminateInstances` gated separately from `disableApiTermination` flag |
| `ModifyImageAttribute`/`RegisterImage` | POST | Mutating | External | Set AMI kernel/launchPermission | Yes | `ec2:ModifyImageAttribute` etc. | AMI boot-chain path; cross-ref `[[ExamplePolicies_EC2-...]]` |
| CloudWatch `PutMetricAlarm` (alarm actions) | POST | Mutating | External | `recover/stop/terminate/reboot` on alarm | Yes | `cloudwatch:PutMetricAlarm` + SLR | Recover owned by sibling; cross-ref |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Foreign-volume mount: the recovery workflow as a cross-team data-at-rest read  [Lens A / S / U — PRIME]
**Background.** Every EBS-backed runbook on this page ends in: "Stop the instance, detach the root volume, attach the volume to a **known working instance**, … start the instance," or (SELinux) "Attach the root volume to another running Linux instance (a **recovery instance**) … mount the failed instance's root volume … disable SELinux in `/{mount_point}/etc/sysconfig/selinux`." The operator mounts a root filesystem and has unrestricted OS-level read/write to it.

**Security Concern.** `ec2:AttachVolume` authorizes against **two independent required resources** — the `volume` and the target `instance` — each with its own condition-key list (`list_ec2.md` L4872–4873). The only ownership-binding keys are tags and resource IDs; there is **no account/owner condition key**. A policy that scopes the *recovery instance* (e.g. `ec2:ResourceTag/role: recovery`) but leaves the **volume** resource as `*` — or vice-versa — lets the caller attach **any volume in the account** to their recovery instance and read its entire filesystem. This is the "two ways to name one operation, only one side is checked" IDOR shape, specialized to EBS. **Confirmed structural fact:** there is **no condition key that cross-binds a `VolumeId` to an `InstanceId`** within one statement (no `ec2:AttachedInstanceOwner`/`ec2:VolumeOwner` equivalent) — IAM evaluates the two required-resource rows independently, so the instance-scope and volume-scope conditions are *independently satisfiable and never mutually constrained*. AWS's console-generated "recovery operator" policies commonly just use `"Resource":"*"`.

**High-level Test Scenarios (falsifiable):**
- **Claim:** With `ec2:AttachVolume`/`ec2:DetachVolume` on `Resource:"*"` (or volume-side wildcard), team A can detach team B's stopped root volume, attach it to A's recovery instance, mount it, and read B's `/etc/shadow` + SSH keys + app secrets. → **Mechanism:** L4873 volume-side keys are tag/ID/encryption only, no owner key; page text "Attach the root volume to a known working instance." → **Oracle:** in a 2-team lab, bake a canary file `/root/CANARY-<teamB>` into B's root volume; from A, `detach`→`attach`→`mount`→read the canary. Success on a volume A doesn't own = confirmed. Settle the IAM-scoping half read-only with `SimulatePrincipalPolicy` (does the policy's volume Resource match B's volume ARN?); the mount-and-read half is live-only. → **Severity:** High (cross-team); Critical if a shared snapshot/RAM path makes it cross-account.
- **Claim (ownership vs existence):** `DetachVolume`/`AttachVolume` validate the instance/volume **exists** but not that the caller **owns** it. → **Oracle:** distinct error (`UnauthorizedOperation` vs `InvalidVolume.NotFound`) on a foreign vs nonexistent id = ownership enforced; identical/`IncorrectState` = existence-only + enumeration oracle. **Do not use DryRun** (caller-IAM only).
- **Claim (self-tag widening — Lens S/I):** if isolation relies on `ec2:ResourceTag/team`, can A set that tag on B's volume (or on A's recovery instance) via `CreateTags` to satisfy the condition? → **Oracle:** `SimulatePrincipalPolicy` for `ec2:CreateTags` on the volume, then live tag + attach. Confirmed if A can self-tag the gating key.

**Doc evidence:** TroubleshootingInstances.html (SELinux, GRUB, General-mount, fsck runbooks); `list_ec2.md` L4870–4874. **Severity-if-true:** High–Critical. **Stop condition:** a mounted volume resolving to an AWS-managed/shared resource → HARD STOP.

### Area 2 — `ModifyInstanceAttribute(kernel|ramdisk|userData)` → code-exec under the instance role without PassRole  [Lens B / E — PRIME]
**Background.** The runbooks say "**Modify the kernel and ramdisk attributes** to use a newer kernel" (KernelLoop, KernelOld). `API_ModifyInstanceAttribute` accepts `Attribute ∈ {…, kernel, ramdisk, userData, blockDeviceMapping, groupSet, disableApiTermination, instanceInitiatedShutdownBehavior, …}`, "specify only one attribute at a time," "to modify some attributes, the instance must be stopped."

**Security Concern.** The confirmed corpus exemplar is `ModifyInstanceAttribute(userData)`: an attacker who **cannot** `iam:PassRole` still gains code-exec under the instance's *already-attached* instance-profile role by rewriting user-data and rebooting, then reading the role's creds from IMDS — a PassRole bypass. **This page legitimizes the sibling attributes `kernel` and `ramdisk`** (and `blockDeviceMapping`), which are equally boot-influencing: a chosen `aki-*`/`ari-*` or an altered root-device boot path changes what executes at boot, under the same role. The IAM gate is a single coarse `ec2:ModifyInstanceAttribute` (L8808) — per-attribute restriction requires the policy author to opt into `ec2:Attribute`/`ec2:Attribute/${AttributeName}`, which "fix the kernel" runbooks will not do.

**High-level Test Scenarios:**
- **Claim:** `ec2:ModifyInstanceAttribute` on an instance that already carries instance-profile role R, with no `ec2:Attribute` condition, yields code-exec as R (via `userData` **or** a `kernel`/`ramdisk` swap + reboot) without the caller holding `iam:PassRole` or `iam:PassedToService` for R. → **Mechanism:** L8808 single-action gate; API valid-values list; `[[iam-roles-for-amazon-ec2-...]]` IMDS vending. → **Oracle:** 2-identity lab — identity with `ec2:ModifyInstanceAttribute` + `ec2:StartInstances` but **no** `iam:PassRole`; set `userData` to a boto/IMDS exfil, start, observe R's STS creds appear. Confirmed = privesc. → **Severity:** High (Critical if R is broadly privileged).
- **Claim (coarse-action blast radius — Lens E):** the same grant also flips `disableApiTermination=true` (anti-cleanup / anti-IR), replaces `groupSet` with a permissive SG (network exposure), and sets `instanceInitiatedShutdownBehavior=terminate` (data-destruction trap). → **Oracle:** `SimulatePrincipalPolicy` shows all these attributes allowed under one `ec2:ModifyInstanceAttribute` with no `ec2:Attribute` condition (read-only, definitive). → **Severity:** High.
- **Claim (Lens S — `ec2:Attribute` case-sensitivity fail-open):** a defensive `Deny` written `ec2:Attribute: "userData"` (lowercase) is **inert** if the request/key populates the PascalCase/`groupSet` form, or if the attribute name casing differs — the Deny silently does not match. → **Oracle:** `SimulateCustomPolicy` with a Deny on one casing and an Allow, request the other casing; allow-through confirms. → **Severity:** Medium–High (defeats the only per-attribute guardrail).

**Doc evidence:** TroubleshootingInstances.html (KernelLoop/KernelOld "Modify the kernel and ramdisk attributes"); `API_ModifyInstanceAttribute.html`; `list_ec2.md` L8808. **Stop condition:** an IMDS cred resolving to an AWS service role → HARD STOP + disclose.

### Area 3 — Encrypted foreign-volume mount: the KMS grant is issued to the *instance*, not the caller — caller needs zero `kms:*`  [Lens H — CRITICAL]
**Background.** Most root volumes are KMS-encrypted. The expected control is **two-factor**: the caller needs the EC2 IAM action **and** `kms:Decrypt` (or a grant) on the volume's CMK. The recovery workflow attaches an encrypted foreign volume to an instance the caller controls, then mounts it.

**Security Concern (upgraded by EBS deep-dive).** EBS encryption documents that **Amazon EC2 — not the caller — sends the `CreateGrant`/decrypt request to KMS, scoped to the attaching instance's auto-generated "identity-only role" `arn:…:assumed-role/aws:ec2-infrastructure/{instance_id}`** (`ebs/latest/userguide/how-ebs-encryption-works.md` L29–54; `ebs-encryption-requirements.md` L68–71: *"a KMS key grant is issued to the instance's identity-only role … they have no policies associated with them"*). And for the **default `aws/ebs` managed key**, *"all principals in the account have access to the default AWS managed KMS key for Amazon EBS encryption"* (`ebsapi-permissions.md` L223–224). **Net effect:** an operator with only `ec2:AttachVolume`/`StopInstances`/`DetachVolume` and **no KMS permissions whatsoever** can attach a default-key-encrypted foreign volume to their recovery instance and read plaintext — the decrypt is authorized against the instance's infrastructure role, outside the caller's own policy evaluation. The expected two-factor control collapses to a single EC2 IAM allow for the common default-key case. For a customer CMK, the chain still succeeds automatically **unless** the key policy / an SCP explicitly denies the `aws:ec2-infrastructure/*` principal.

**High-level Test Scenarios:**
- **Claim:** A recovery-instance role/user with `ec2:*Volume*` and **zero `kms:*`** mounts team B's `aws/ebs`-encrypted root volume and reads a canary file in plaintext. → **Mechanism:** the CreateGrant-to-identity-only-role chain above + default-key openness. → **Oracle:** **live-only** (by design `iam:SimulatePrincipalPolicy` CANNOT see this — the grant is issued by the EC2 service principal, not the caller, so Simulate against the caller's policy misleadingly shows "no KMS allow"). In a 2-team lab, give the recovery identity no `kms:*`, attach the encrypted foreign volume, mount, read canary; in CloudTrail confirm KMS logs the `Decrypt` caller as `aws:ec2-infrastructure/{recovery-instance-id}`, not the operator. → **Severity:** **Critical** — collapses expected IAM+KMS two-factor to IAM-only for default-key encrypted-at-rest data.
- **Claim (CMK variant):** a customer-CMK-encrypted volume is equally readable unless the key policy explicitly denies `aws:ec2-infrastructure/*`. → **Oracle:** repeat with a CMK whose policy grants only the owning team; attach from the other team's recovery instance; decrypt succeeding = confirmed. → **Severity:** High.

**Doc evidence:** `how-ebs-encryption-works.md` L29–68; `ebs-encryption-requirements.md` L68–92; `ebsapi-permissions.md` L223–224. **Stop condition:** a volume that decrypts under an **AWS-owned** key you were never granted → HARD STOP + disclose.

### Area 3b — `ebs:GetSnapshotBlock` raw-block read bypasses the entire mount/fsck/SELinux path  [Lens X / S]
**Background.** The recovery workflow assumes the only way to read a failed volume's data is attach → mount → (fsck) → read, gated by SELinux/filesystem ACLs inside the guest.
**Security Concern.** The **EBS direct APIs** (`ebs:GetSnapshotBlock` / `ListSnapshotBlocks` / `ListChangedBlocks`, resource type `snapshot*`) return **raw disk blocks** — a full filesystem image, including unallocated/deleted data — with **no condition key for owner/creator** (`list_ebs.md` L72–87; keys are tag/`ebs:ParentSnapshot`/`ebs:VolumeSize` only). AWS's **own published sample policy** scopes these purely by a single tag: `"Resource":"arn:aws:ec2:*::snapshot/*","Condition":{"StringEqualsIgnoreCase":{"aws:ResourceTag/<Key>":"<Value>"}}` (`ebsapi-permissions.md` L27–47) — copied verbatim into recovery/forensics tooling, it authorizes any snapshot bearing that tag regardless of which team made it, and bypasses mount/fsck/SELinux entirely.
**Test Scenarios:**
- **Claim:** a principal holding only the AWS-sample `ebs:GetSnapshotBlock` tag-scoped policy can reconstruct a foreign team's root-volume snapshot block-by-block. → **Oracle:** read-only confirm the sample omits an owner condition (done, by quotation); live, enumerate deployed `ebs:GetSnapshotBlock` policies via `SimulatePrincipalPolicy` and attempt a block read of a snapshot tagged to match but owned by another team. → **Severity:** High (full data exfil + an alternate path to Area 1's secrets without ever stopping/attaching a volume). **Lens-R note:** the insecure default ships in an **AWS-published sample policy** → in-scope/reportable if the omission causes a real cross-team read.

### Area 4 — Twin / parity actions that bypass the obvious permission  [Lens X]
**Background/Concern.** Availability actions have siblings with divergent authz:
- **Claim:** `ec2:CreateImage` **reboots the instance even without `ec2:RebootInstances`** (documented, `list_ec2.md` L5143). A caller denied `RebootInstances` can still force a reboot (availability impact; also triggers the userData/kernel changes from Area 2 to take effect) via `CreateImage` without `NoReboot`. → **Oracle:** identity with `ec2:CreateImage` but explicit `Deny ec2:RebootInstances`; call `CreateImage` (NoReboot=false); observe the instance reboot. Definitive from the documented behavior; confirm live. → **Severity:** Medium (High when chained to Area 2 to apply attacker boot-chain changes while "lacking" reboot).
- **Claim:** `DetachVolume Force=true` detaches without OS unmount — a cross-team actor could force-detach a victim's in-use root volume (availability + FS corruption). → **Oracle:** parity check of DetachVolume authz vs AttachVolume; live force-detach of a foreign volume in the 2-team lab. → **Severity:** Medium–High (cross-team DoS/corruption).

### Area 5 — AMI / kernel-image modification path  [Lens E / EE — secondary]
**Background.** "Modify the AMI … correcting the kernel"; older instance-store relaunch "specifying `-kernel` and `-ramdisk`."
**Concern.** `ModifyImageAttribute`/`RegisterImage` can set the AMI's kernel and `launchPermission`; a predictable `aki-*`/`ari-*` (user-provided-kernels / PV-GRUB) namespace *might* be pre-registrable (Lens EE land-grab) so a victim recovery workflow selects an attacker kernel. **Doc-gap:** the AKI/ARI resolution/ownership model is not described on this page — confirm via `UserProvidedKernels.html` and route AMI-sharing/launchPermission authz to `[[ExamplePolicies_EC2-attack-research-plan]]`. **Severity:** Medium if a cross-account kernel/AMI selection is confirmed; otherwise Low.

### Area 6 — System-log confidentiality (cross-reference only)  [Lens A / O]
"Get system log" = `ec2:GetConsoleOutput`, instance* + tag/`InstanceID` scoping (`list_ec2.md` L8252). Cross-tenant console read, ownership-vs-existence, and secret-leakage-in-boot-output are **fully developed in `[[troubleshoot-unreachable-instance-attack-research-plan]]` and `[[ec2-instance-troubleshoot-attack-research-plan]]`** — do not restate; pick them up there. One adjacency to add: the recovery workflow (Area 1) is an **alternate, stronger disclosure path** to the same secrets GetConsoleOutput leaks, and is not rate-limited the same way.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attach foreign root volume to own recovery instance → read FS | `AttachVolume` (volume + instance resources) | Resource-level perms on **both** required resources + tag/ID condition keys (no owner key) |
| Code-exec as instance role w/o PassRole via `userData`/`kernel`/`ramdisk` | `ModifyInstanceAttribute` | `ec2:Attribute`/`ec2:Attribute/${AttributeName}` opt-in condition; instance-level resource perms |
| One grant mutates SG/termination-protection/shutdown-behavior | `ModifyInstanceAttribute` coarse action | Per-attribute `ec2:Attribute` conditions (only if authored) |
| `ec2:Attribute` Deny defeated by casing | IAM policy eval | Case-exact condition authoring |
| Decrypt encrypted foreign volume with **zero caller `kms:*`** (grant issued to `aws:ec2-infrastructure/{instance}`) | `AttachVolume` + KMS auto-grant | CMK key-policy explicit deny of `aws:ec2-infrastructure/*`; default `aws/ebs` key is open to all account principals |
| Raw block read bypassing mount/fsck/SELinux | `ebs:GetSnapshotBlock` | Owner/account condition on snapshot (AWS sample omits it — tag-only) |
| Reboot w/o `RebootInstances` | `CreateImage` (NoReboot) | `NoReboot=true`; separate `CreateImage` scoping |
| Force-detach victim root volume | `DetachVolume Force` | Resource-level perms + ownership |
| Cross-tenant system-log read | `GetConsoleOutput` | Instance ownership check *(owned by siblings)* |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **OS-level log interpretation itself** (OOM, fsck, GRUB, Xenbus errors) — these are customer-workload failures, not AWS boundary defects. In scope only where a *runbook step* invokes an AWS action with a boundary (Areas 1–5).
- **Cross-ACCOUNT `AttachVolume`** — not possible per the model (volumes/instances account-local, no owner condition key); test only if a shared snapshot / RAM / cross-account launchPermission bridges accounts.
- **IMDS on a managed host / the customer steering their own instance** — out of scope; the privesc in Area 2 is in scope *only* because it crosses an IAM identity boundary (no PassRole → role creds).
- **Single-tenant self-DoS** (you terminate/corrupt your own instance) — out of scope; cross-team force-detach (Area 4) is in scope.
- **Shared EBS/EC2 fleet internals, the console/serial service backend** — HARD STOP + disclose, not a lead to pursue.
- **AWS-managed/sample IAM policy audit** — owned by `[[ExamplePolicies_EC2-attack-research-plan]]` / `[[security-iam-awsmanpol-attack-research-plan]]`.

## 8. Null hypotheses / doc gaps (lens didn't fire — pages checked)
- **Lens G (SSRF):** null — read the full TroubleshootingInstances page + `ModifyInstanceAttribute`/`AttachVolume` API refs; no field the service **dereferences server-side** on behalf of the caller (kernel/ramdisk are opaque image IDs, not fetched URLs). Re-open if `UserProvidedKernels.html` describes a URL-based kernel source.
- **Lens D/V (network segmentation):** null — this page performs no network/ENI operation; `groupSet` SG replacement is covered under Area 2 (Lens E), not as a network-reach breach.
- **Lens F (translation/injection):** null for AWS layer — the only parsing is OS-side (`/etc/fstab`, GRUB, SELinux) inside the customer's own recovery instance; no AWS translator consumes the log text. (Minor adjacency: if the console renders `GetConsoleOutput` with attacker-controlled boot strings in a web UI → stored-XSS — Low, cross-ref sibling.)
- **Lens K (prompt injection):** null — no LLM/agent in this page's flow.
- **Lens J / M / N / W / Y / AA / BB / CC / DD / FF:** did not fire — no OAuth/3P linking, shared session id, namespace migration, attestation gate, transport/TLS claim, revocable share, multi-parser edge, upstream-context header, cache layer, or JWT in this page's mechanisms. `UsingAlarmActions` CloudWatch-recover SLR (a thin Lens B/AA adjacency) is **owned by `[[troubleshoot-unreachable-instance-attack-research-plan]]`** — pick up there.
- **Lens AA (revocation completeness):** thin — `DetachVolume` purges the plaintext data key from the Nitro card (`how-ebs-encryption-works.md` L65–68), but the docs **do not state** whether EC2 calls `kms:RevokeGrant` on the identity-only role at detach. **Doc-gap:** live-check via `kms:ListGrants` after a detach cycle whether the `aws:ec2-infrastructure/{instance_id}` grant lingers (read-only; narrow TOCTOU value only, Low–Medium — grant is bound to that instance's own role, not reusable by other callers).
- **Doc-gaps to confirm before hunting:** (a) whether `DetachVolume` triggers `kms:RevokeGrant` (above); (b) whether `AttachVolume` enforces same-AZ/same-account only (ARN is account-scoped by construction → cross-account structurally impossible, confirmed via `ebs-modifying-snapshot-permissions.md`: the only cross-account EBS path is share-snapshot → recipient creates a *new* volume in their own account; verify the live error is `InvalidVolume.NotFound`); (c) AKI/ARI ownership/resolution model for Area 5; (d) exact CMK-policy behavior for `aws:ec2-infrastructure/*` principal (Area 3 CMK variant).

---

## Priority kill-chain (compose across lenses)
**Highest-impact chain:** Area 1 (mount foreign root volume) → recover its **instance-profile/SSH/app credentials at rest** → use those to reach the workloads the victim instance could reach. **Alternative chain:** Area 2 (`ModifyInstanceAttribute userData/kernel`, no PassRole) → IMDS role creds → lateral movement; apply the boot-chain change even while "lacking" `RebootInstances` via Area 4's `CreateImage` reboot twin. Rate each chain at the **end** severity (role/credential compromise), not the entry action.
