# EC2 Windows Troubleshooting (win-ts-common-issues) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-ts-common-issues.html`
(offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/win-ts-common-issues.md`), plus the pages it links and the IAM references it implicates:
`ec2-windows-passwords.md`, `ResettingAdminPassword*.md`, `ec2launch.md`, `ec2launch-config.md`, `configure-launch-agents.md`, `launch-agents-service-admin.md`, `Upgrading_PV_drivers.md`, `Windows-Server-EC2Rescue.md`, `API_GetConsoleOutput.md`, `API_GetPasswordData.md`, `service-authorization/.../list_ec2.md`, `list_ebs.md`, `list_ssm.md`, `ebs/latest/userguide/{how-ebs-encryption-works,ebs-encryption-requirements,ebsapi-permissions,ebs-modifying-snapshot-permissions,share-volume}.md`.

**Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.** Online and offline copies of the target page were confirmed identical on 2026-10-17.

---

## 0. How to use this document

- Each lead is stated as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5); look left and right for adjacent bugs.
- This is an **operational troubleshooting page**, not an API surface page. Its security value is that it documents, in step-by-step form, two primitives AWS's own runbooks normalize: (a) **detach a root volume and mount it on a second instance** (offline-disk access), and (b) **retrieve console/password/screenshot data and re-establish an SSM admin session**. The plan treats those normalized workflows as attacker playbooks and asks whether the IAM/KMS/transport controls that *should* bound them actually do.
- Most leads here are **IAM/KMS policy-composition and transport-integrity** issues whose owner-to-fix is often the *customer's policy author* (least-privilege footgun → out of scope / informational) **unless** the weak default ships in an AWS-authored artifact or the control simply does not exist in the API — those are in scope. Each lead marks which side of that line it sits on.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane** (the Nitro/host layer, the EC2 control plane's own fleet identity, a storage-plane ENI), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate beyond existence.
- **Scope discipline:** HTTP/application + IAM/API layer only. Read-only probes with synthetic canary data. Never read another real tenant's bytes beyond the minimum signal that proves the boundary broke; never mutate another workload's state.

---

## 1. Pentest Objectives

Stated as concrete boundary-breach outcomes a hunter would try to produce:

1. **Cross-workload offline disk read** — using only a "scoped-looking" EBS/instance IAM policy, attach *another workload's* root volume to an instance the tester controls and read its filesystem (the DSRM-offline workflow, performed adversarially).
2. **Encryption-bypass confirmation** — show that EBS-encryption-at-rest with the **default `aws/ebs` managed key** provides *no* barrier to objective 1 for any in-account principal.
3. **Guardrail-blind block read** — pull raw snapshot bytes via `ebs:GetSnapshotBlock`/`ListSnapshotBlocks` against a snapshot that an `ec2:*`-only SCP/guardrail believes is protected.
4. **Cross-account exfil via share** — convert an intra-account disk-read primitive into permanent cross-account data egress via `ec2:ModifySnapshotAttribute createVolumePermission`, and show revoke does not undo an already-made copy.
5. **Out-of-scope credential retrieval** — call `ec2:GetPasswordData` / `ec2:GetConsoleOutput` / `ec2:GetConsoleScreenshot` against an instance outside the principal's intended scope and receive a non-empty response (credential/recon disclosure).
6. **SSM default-admin foothold** — start an `ssm:StartSession` on a Windows node and confirm the shell runs as a local-Administrators-group account (`ssm-user`), bypassing the entire RDP-password / console-ownership model; and test whether session scoping holds across instances.
7. **On-host privilege escalation via launch-agent artifacts** — show that a non-admin local user can influence a SYSTEM-level EC2Launch v1 scheduled-task script or read a cleartext password left in `LaunchConfig.json`.
8. **Driver supply-chain compromise** — show the documented PV-driver download path (S3 zip → MSI run as admin) lacks integrity verification and/or can be downgraded in transport.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces referenced by the page**
- **EC2 control-plane APIs:** `StopInstances`, `RunInstances`, `AttachVolume`, `DetachVolume`, `GetConsoleOutput`, `GetPasswordData`, `GetConsoleScreenshot`, `ModifySnapshotAttribute`, `CreateSnapshot`, `CreateImage` (console + CLI + PowerShell `Get-EC2ConsoleOutput`).
- **EBS direct (data-plane) APIs:** `ebs:GetSnapshotBlock`, `ebs:ListSnapshotBlocks`, `ebs:ListChangedBlocks` — block-level reads of snapshot bytes, **`ebs:` prefix but ec2-namespaced snapshot ARN**.
- **AWS Systems Manager:** `ssm:StartSession` (Session Manager), the SSM Agent (`AmazonSSMAgent` service) + SSM Distributor (PV-driver package install), SSM Automation `AWS-CreateImage` runbook.
- **On-instance (OS) surface:** RDP; the Windows registry (`RealTimeIsUniversal`, Boot Manager `11000001`/`Element`); DiskPart; `bcdedit` / BCD store; EC2Launch v1 PowerShell scripts + JSON config under `C:\ProgramData\Amazon\EC2-Windows\Launch\`; EC2Launch v2 / EC2Config services; EC2Rescue for Windows.

**Processes / runtimes behind the interface**
- **EC2Launch v1** = a *set of PowerShell scripts* run via a **Windows Scheduled Task as SYSTEM** (`ec2launch.md`, `launch-agents-service-admin.md`: "EC2Launch v1 is a set of PowerShell scripts that is managed through a scheduled task"). Config in `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\*.json`; scripts in `...\Launch\Scripts\*.ps1`; can be scheduled `-Schedule` / `-SchedulePerBoot`.
- **EC2Launch v2 / EC2Config** = Windows Services. All three generate the **default Administrator password** at boot and encrypt it with the launch key pair's public key.
- **SSM Agent** on the node; a default local user **`ssm-user`** added to the **Administrators group**, which is the default OS user for a Session Manager session.
- **KMS** for EBS data-key decryption: EC2 sends `kms:CreateGrant` to an *instance identity-only role* on attach of an encrypted volume.

**Accounts / trust zones**
- Customer account/region (all the above live here).
- AWS service plane (Nitro host, EC2 control plane, storage plane) — **hard-stop zone**, not a target.
- A *second AWS account* enters the picture only via snapshot/volume sharing (objective 4).

**Assets**
- EBS volume/snapshot **bytes** (the crown jewels — any other workload's root volume).
- The **default Administrator password** (RSA-encrypted blob from `GetPasswordData`; cleartext transiently in `LaunchConfig.json`).
- Console output / screenshots (recon + possible legacy credential leakage).
- The PV-driver MSI (kernel-level code executed as admin).

**Identifier shapes**
- `i-…` instance IDs, `vol-…` volume IDs, `snap-…` snapshot IDs (used directly in IAM `ec2:InstanceID` / `ec2:VolumeID` condition keys and in ARNs). Snapshot ARN is ec2-namespaced even for `ebs:` actions: `arn:${Partition}:ec2:${Region}::snapshot/${SnapshotId}`.

```
ASCII pipeline — the "offline disk" primitive the page documents

  [affected instance] --StopInstances--> stopped
          |  root volume (vol-AAA)
          v
     DetachVolume(vol-AAA)
          |
          v
  AttachVolume(vol-AAA -> i-TEMP, same AZ)        <-- i-TEMP is attacker-launchable
          |
          v
  [temp instance i-TEMP] mounts vol-AAA as data disk
          |  (bcdedit /store D:\Boot\BCD ... ; or read ANY file)
          v
  DetachVolume + reattach to /dev/sda1 (intended)   OR   CreateSnapshot(vol-AAA)
                                                              |
                                                              v
                                            ebs:GetSnapshotBlock  (guardrail-blind read)
                                                              |
                                                              v
                                   ModifySnapshotAttribute(createVolumePermission, acct-B)
                                                              |
                                                              v
                                            [account B] CopySnapshot  (cross-account exfil)

KMS gate (should stop the mount read):  attach of encrypted vol -> kms:CreateGrant/Decrypt.
   If vol encrypted with default aws/ebs key => every in-account principal can decrypt => no gate.
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal with broad/mis-scoped EBS rights | Another workload's root-volume **bytes** | `AttachVolume(vol-X → i-attacker)` then OS-level read | Tester reads a canary file planted on victim volume after attaching it to an instance the policy "should not" have paired with that volume |
| Same | Decryption of an encrypted victim volume | `kms:CreateGrant`/`Decrypt` via default `aws/ebs` key | Mounted encrypted volume is readable in cleartext with **no CMK key-policy grant** to the tester |
| IAM principal denied `ec2:*` snapshot actions | Snapshot **blocks** | `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` | Raw block data returned for a snapshot the `ec2:`-scoped guardrail reports as protected |
| Customer account | **Second AWS account** | `ModifySnapshotAttribute createVolumePermission` + `CopySnapshot` | Account B creates a volume/copy from the shared snapshot; copy survives a later `remove`/unshare |
| IAM principal scoped to instance A | Credentials/recon of instance B | `GetPasswordData` / `GetConsoleOutput` / `GetConsoleScreenshot` on `i-B` | Non-empty, instance-B response returned to a principal whose policy names only `i-A` / a different tag |
| Any `ssm:StartSession`-capable principal | Local **Administrator**-equivalent shell on the node | Session Manager default `ssm-user` in Administrators group | `whoami /groups` in the session shows Administrators; session starts on an instance outside the policy's intended scope |
| Non-admin **local OS user** | SYSTEM code execution | Writable EC2Launch v1 `*.ps1` script / scheduled task running as SYSTEM at boot | A tester-modified script executes as SYSTEM on next boot/schedule |
| Network MITM / transport | Driver MSI (kernel code) run as admin | Unverified S3 zip download + MSI execute | A substituted/downgraded driver package is installed because no signature/checksum is verified |
| Any customer surface | **AWS service plane** (Nitro/control/storage) | — | Any AWS-owned identity/ARN/account observed → **HARD STOP + disclose** |

---

## 4. API / Interface Inventory

| Name | Method | Mutating? | Internet-callable | Authorized callers (doc) | Notes / lead |
|---|---|---|---|---|---|
| `ec2:AttachVolume` | API | Mutating | Yes | IAM, scoped to **both** `instance*` + `volume*` | **No "owner" condition key**; two independent resource clauses → split-scoping footgun (Lead A1) |
| `ec2:DetachVolume` | API | Mutating | Yes | IAM, `instance` + `volume*` | pairs with AttachVolume |
| `ec2:CreateSnapshot` / `CreateImage` | API | Mutating | Yes | IAM, `snapshot*`+`volume*` / `image*`+`instance*`+`snapshot*` | feeds the snapshot-exfil chain |
| `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` / `ListChangedBlocks` | API | Non-mutating (read) | Yes | IAM, `snapshot*` only, tag keys | **Twin path** bypassing `ec2:`-only guardrails (Lead X1). AWS's own docs warn about this (`ebsapi-permissions.md` L12-13) |
| `ec2:ModifySnapshotAttribute` | API | Mutating | Yes | IAM; `ec2:Add/Remove/userId`,`/group` | Cross-account share + one-way revoke (Lead AA1) |
| `ec2:GetPasswordData` | API | Non-mutating | Yes | IAM, `instance*`, tag/ID keys | Returns RSA-encrypted admin password; **resource-scopable** (Lead A2) |
| `ec2:GetConsoleOutput` (`--latest` Nitro-only) | API | Non-mutating | Yes | "Only the instance owner can access" + IAM `instance*` | Content today = "last three system event log errors" for Windows; legacy sensitive-boot-output hypothesis (Lead U2) |
| `ec2:GetConsoleScreenshot` | API | Non-mutating | Yes | IAM, `instance*` | Visual recon of login/error state (Lead A3) |
| `ssm:StartSession` | API | Mutating (session) | Yes | IAM, `document` and/or `instance`/`managed-instance`, `ssm:SessionDocumentAccessCheck` | Default shell = `ssm-user` in **Administrators** (Lead CC1 / E1) |
| SSM Distributor / `AWS-CreateImage` runbook | API/runbook | Mutating | Yes | IAM | Alt driver-install + AMI-create path; audit runbook permissions |
| On-host: EC2Launch v1 scripts, registry, DiskPart, bcdedit | OS | Mutating | No (local) | Local admin (per docs) | SYSTEM scheduled-task scripts; cleartext password in `LaunchConfig.json` (Leads R1/T1) |

**Undocumented/hidden-knob note:** `GetConsoleOutput`'s `Latest=true` is "only supported on Nitro-based instances" — a capability delta worth diffing against `DescribeInstanceTypes` (Lens U). No console-hidden auth-weakening enum was found on this surface.

---

## 5. Recommended Areas of Focus

Priority order: cross-account/cross-workload data reach first, then credential retrieval, then the SSM foothold, then on-host and supply-chain.

### Area 1 — EBS detach/attach as an account-wide offline-read primitive  *(Lens A / S / U)*  — **TOP PRIORITY**
**Background.** The page's "boot an offline instance into DSRM" runbook instructs the operator to launch a *temporary instance in the same AZ*, detach the affected root volume, attach it to the temp instance, mount it, then reattach. This is the canonical offline-disk access pattern — and nothing in it is specific to DSRM.
**Security Concern.** `ec2:AttachVolume` requires grants on **two independent resource types** (`instance*` AND `volume*`) and offers **no condition key meaning "a resource I own"** — scoping is only via `ec2:ResourceTag`/`aws:ResourceTag` or explicit `ec2:VolumeID`/`ec2:InstanceID` lists (`list_ec2.md` L4870-4874). IAM evaluates each resource clause independently, so a policy that tightly tags the *instance* clause but leaves the *volume* clause `"*"` (or vice-versa) lets a principal attach **any** volume in the region to a throwaway instance they launch.
**High-level Test Scenarios.**
- *Claim:* a principal holding a "backup/EBS-operator"-style policy can attach a foreign-workload volume to a tester-controlled instance and read its filesystem. *Oracle:* canary file planted on a victim volume is read from the temp instance; prove the policy's two clauses are asymmetrically scoped. *Severity-if-true:* **Critical** (account-wide data read) — but owner-to-fix is the customer policy author ⇒ treat a plain mis-scope as a least-privilege footgun (informational/out-of-scope) **unless** the mis-scoped policy is an **AWS-authored/managed/sample** policy (then in scope, Area 7).
- *Claim (Lens S):* `ec2:Encrypted` / `ec2:AvailabilityZone` condition keys do **not** bind ownership; a Deny intended to stop foreign attach is inert if written against the wrong key. *Oracle:* an attach allowed despite a Deny that the author believed was scoping ownership.
**Doc evidence.** `win-ts-common-issues.md` "To boot an offline instance into DSRM"; `list_ec2.md` AttachVolume/DetachVolume entries.

### Area 2 — Encryption-at-rest is a no-op against Area 1 under the default key  *(Lens H / U)*
**Background.** Auditors routinely close "is data encrypted at rest?" as soon as EBS encryption is on.
**Security Concern.** `ebsapi-permissions.md` L224: *"By default, all principals in the account have access to the default AWS managed KMS key for Amazon EBS encryption, and they can use it for encryption and decryption."* On attach, EC2 issues `kms:CreateGrant`/`Decrypt` automatically (`how-ebs-encryption-works.md` L29/48; `ebs-encryption-requirements.md` L71).
**High-level Test Scenarios.**
- *Claim:* a volume encrypted with `aws/ebs` mounts in cleartext on the temp instance with **no CMK grant** to the tester. *Oracle:* successful cleartext read of an encrypted victim volume by a principal absent from any CMK key policy. *Severity-if-true:* **High** (defeats a control widely assumed sufficient).
- *Claim (Lens U):* `EnableEbsEncryptionByDefault` is documented as protective but enforces nothing against an in-account lateral read unless paired with a **scoped CMK key policy**. *Oracle:* doc-vs-mechanism gap confirmed; file as informational if purely advisory.
**Doc evidence.** quoted lines above.

### Area 3 — `ebs:GetSnapshotBlock` twin path bypasses `ec2:`-only guardrails  *(Lens X)*
**Background.** Most SCP/guardrail examples constrain only `ec2:CreateSnapshot`/`CopySnapshot`/`CreateVolume`.
**Security Concern.** `ebs:GetSnapshotBlock`/`ListSnapshotBlocks`/`ListChangedBlocks` reach the **same snapshot bytes** with only a `snapshot*` resource + tag keys, under the **`ebs:` prefix**. AWS states the gap explicitly: `ebsapi-permissions.md` L12-13 *"you might give access to a user who is denied access to the same resource through the Amazon EC2 APIs, such as CopySnapshot or CreateVolume."*
**High-level Test Scenarios.**
- *Claim:* a principal Denied all `ec2:*` snapshot actions still reads snapshot blocks via `ebs:GetSnapshotBlock`. *Oracle:* raw block returned where the `ec2:` path returns AccessDenied. *Severity-if-true:* **High** (guardrail-blind data read). Owner-to-fix is shared: AWS documents the gap; the customer must add `ebs:` to the guardrail. A doc that failed to warn would be AWS-owned — **it does warn**, so this is a hunter-education lead, not an AWS defect.
**Doc evidence.** `list_ebs.md`; `ebsapi-permissions.md`.

### Area 4 — Cross-account snapshot share + one-way revoke  *(Lens AA)*
**Background.** `ec2:ModifySnapshotAttribute createVolumePermission --user-ids <acct>` shares a snapshot cross-account; `--group-names all` makes it public.
**Security Concern.** Revoke (`--operation-type remove`, keys `ec2:Remove/userId`,`/group`) does **not** retroactively invalidate volumes/copies the consuming account already created (`ebs-modifying-snapshot-permissions.md` L8) — classic one-way share. CMK-encrypted snapshots *can* be shared (L28), so the share path is viable precisely when data is "encrypted."
**High-level Test Scenarios.**
- *Claim:* after chaining Area 1 → `CreateSnapshot` → share to a tester-owned account B → `CopySnapshot`, a later unshare leaves account B's copy intact. *Oracle:* account B reads the data post-revoke; `SharedSnapshotCopyInitiated` is the only documented detection point (L121-124). *Severity-if-true:* **Critical** (permanent cross-account exfil), bounded only by detection speed. Owner-to-fix shared (AWS provides block-public-access-for-snapshots, snapshot-lock, Recycle Bin; customer must enable).
**Doc evidence.** `ebs-modifying-snapshot-permissions.md`, `share-volume.md`, `share-kms-key.md`.

### Area 5 — Out-of-scope credential / recon retrieval via Get* APIs  *(Lens A / FF-adjacent)*
**Background.** The page's "Unable to get console output" step teaches `get-console-output`/`Get-EC2ConsoleOutput`; the Windows-password workflow uses `GetPasswordData`.
**Security Concern.** `GetConsoleOutput`, `GetPasswordData`, `GetConsoleScreenshot` are all **resource-scopable to a single `instance*`** (`list_ec2.md` L8252/8498/8258) with identical tag/ID condition keys — so the *only* barrier to reading every Windows instance's credential blob is whether the policy author actually scoped it. `GetPasswordData` returns the **RSA-encrypted** admin password; ciphertext is useless without the private key, **but** key-pair reuse across many instances collapses that second layer.
**High-level Test Scenarios.**
- *Claim:* a principal whose policy names only `i-A` (or tag `env:dev`) successfully calls `GetPasswordData`/`GetConsoleOutput` on `i-B`. *Oracle:* non-empty instance-B response. *Severity-if-true:* **Critical** for `GetPasswordData` (path to RDP admin if the shared/default key pair is recoverable), **High** for console output/screenshot. Mis-scope by a customer policy = footgun/informational; an AWS-managed policy granting these at `Resource:"*"` = in scope (Area 7).
- *Claim (key reuse):* the same private key decrypts `passwordData` for many instances. *Oracle:* one key file yields working plaintext for ≥2 instances. *Severity:* Critical.
**Doc evidence.** `API_GetPasswordData.md`, `API_GetConsoleOutput.md`, `ec2-windows-passwords.md`, `ResettingAdminPassword.md`, `list_ec2.md`.

### Area 6 — SSM Session Manager default `ssm-user` = local Administrator  *(Lens E / CC)*
**Background.** The page's first remediation restarts `AmazonSSMAgent` so **Session Manager connects** to the Windows node.
**Security Concern.** `session-manager-getting-started-ssm-user-permissions.md`: the agent creates local user **`ssm-user`** and adds it to the **Administrators group (Windows)**; it is the **default OS user** for a session. So anyone who can `ssm:StartSession` on the node gets an admin-equivalent shell — **no RDP password, no `GetPasswordData`, no key pair** — bypassing the entire console-ownership/encryption model. `ssm:StartSession` *is* resource-scopable (`document` + `instance`/`managed-instance`, `ssm:SessionDocumentAccessCheck`).
**High-level Test Scenarios.**
- *Claim:* `ssm:StartSession` scoped to instance A also starts on instance B (document-only scoping, no instance condition). *Oracle:* session opens on `i-B`. *Severity:* **Critical**.
- *Claim:* any permitted session yields Administrators membership by default. *Oracle:* `whoami /groups` shows Administrators. *Severity:* **Critical** (design-level; owner-to-fix shared — customer can restrict `ssm-user`, AWS ships the admin default).
**Doc evidence.** `win-ts-common-issues.md` (SSM Agent restart step), `list_ssm.md` L1764-1770, `session-manager-getting-started-ssm-user-permissions.md`.

### Area 7 — On-host privilege escalation via EC2Launch v1 artifacts  *(Lens R / T — on-host)*
**Background.** The EBS-init remediation edits `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\DriveLetterMappingConfig.json` and runs `...\Scripts\InitializeDisks.ps1 -Schedule`.
**Security Concern.** EC2Launch v1 is **PowerShell scripts run by a Scheduled Task as SYSTEM** (`launch-agents-service-admin.md`, `ec2launch.md`). If the ACLs on `...\EC2-Windows\Launch\Scripts\*.ps1` or `...\Config\*.json` permit write by a non-admin local user, that user gains SYSTEM at next boot/schedule. Separately, `ec2launch-config.md` L57: *the admin password "is stored in `LaunchConfig.json` as clear text and is deleted after Sysprep sets the administrator password."* — a transient cleartext-credential-at-rest window (and a hazard if baked into an AMI/snapshot before deletion).
**High-level Test Scenarios.**
- *Claim:* a non-admin user can write a Launch script that the SYSTEM scheduled task executes. *Oracle:* tester-authored script runs as SYSTEM. *Severity:* High (local privesc). **Doc-gap:** the page prescribes editing these files but documents **no ACL-hardening guidance** → AWS-owned documentation gap, file as informational + verify actual default ACLs on an instance.
- *Claim:* `LaunchConfig.json` with a cleartext `adminPassword` survives in a captured AMI/snapshot. *Oracle:* cleartext password recovered from a snapshot of a freshly-configured (pre-Sysprep) instance — chains into Area 1/3. *Severity:* High.
**Doc evidence.** `ec2launch-config.md` L36/L57, `launch-agents-service-admin.md`, `ec2launch.md`.

### Area 8 — PV-driver download supply-chain / transport integrity  *(Lens Y / Q)*
**Background.** `Upgrading_PV_drivers.md` instructs downloading the driver package and running the MSI: `Download https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip` (also via `Invoke-WebRequest`), extract, run MSI (installs a **kernel driver**, auto-reboot).
**Security Concern.** No **signature/checksum verification** of the zip/MSI is documented. A TLS note (L125) says Windows Server 2016/earlier "might need TLS 1.2 enabled" for the PowerShell session — implying the default session may negotiate a weaker/older TLS, a downgrade window. The package is a **path-style `s3.amazonaws.com`** URL; the content is executed with admin rights.
**High-level Test Scenarios.**
- *Claim:* the documented flow performs no integrity check, so a transport-position or cache-position attacker can substitute the kernel driver. *Oracle:* doc confirms no hash/sig step; on a lab instance, a modified zip installs without warning. *Severity:* High (kernel code exec) — **AWS-owned** if the doc omits an integrity step it should prescribe; verify whether the MSI is Authenticode-signed (Windows would enforce that independently).
- *Claim (Lens Y):* the driver fetch can be forced below the documented TLS floor on legacy OS. *Oracle:* download succeeds over <TLS1.2. *Severity:* Medium–High.
- *Note (Lens EE):* the bucket `ec2-windows-drivers-downloads` is AWS-owned → name-squat/land-grab **N/A**; do not probe the bucket.
**Doc evidence.** `Upgrading_PV_drivers.md` L117-125, L178, L232 (Citrix package).

### Area 9 — Registry / BCD / console-output integrity (lower)  *(Lens O / U)*
- `RealTimeIsUniversal` and the Boot-Manager `11000001`/`Element` edits are **local-admin OS operations**; their only cross-boundary relevance is that misuse of `bcdedit /store D:\Boot\BCD` against an *attached foreign* volume (Area 1) is how the offline primitive is actioned — the registry/BCD steps themselves are not a remote boundary.
- *Lens U/O:* `GetConsoleOutput` for Windows is scoped by docs to "the last three system event log errors" and "only the instance owner can access" — a **legacy hypothesis** that older EC2Config AMIs leaked boot-time password material to the console is *unconfirmed by current docs*; test only against a lab legacy AMI, treat as info-leak if reproduced.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attach foreign root volume to tester instance → read bytes | `ec2:AttachVolume` two-clause scoping | tag/ID condition keys (`ec2:ResourceTag`/`VolumeID`/`InstanceID`) — no owner key |
| Mount encrypted foreign volume in cleartext | KMS default `aws/ebs` key | CMK key policy scoping `kms:Decrypt`/`CreateGrant` to specific principals |
| Read snapshot blocks past an `ec2:`-only guardrail | `ebs:GetSnapshotBlock` | guardrail must include `ebs:` prefix (AWS warns in `ebsapi-permissions.md`) |
| Cross-account exfil via share; copy survives revoke | `ec2:ModifySnapshotAttribute createVolumePermission` | block-public-access-for-snapshots, snapshot lock, CloudTrail `SharedSnapshotCopyInitiated` |
| Retrieve out-of-scope admin password / console | `GetPasswordData`/`GetConsoleOutput`/`GetConsoleScreenshot` | per-instance IAM resource scoping + private-key custody (no key reuse) |
| Admin shell with no password via SSM | `ssm:StartSession` + default `ssm-user` | `ssm:SessionDocumentAccessCheck` + instance-scoped policy; restrict `ssm-user` group |
| Local non-admin → SYSTEM via Launch script | EC2Launch v1 SYSTEM scheduled task | default ACLs on `...\Launch\Scripts`/`Config` (not documented — verify) |
| Kernel-driver substitution/downgrade | PV-driver zip/MSI download | MSI Authenticode signature (doc prescribes none); TLS 1.2 floor |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Customer-authored least-privilege mistakes.** A customer writing an over-broad `AttachVolume`/`GetPasswordData`/`StartSession` policy is a footgun the customer owns — **informational, not an AWS defect**. It flips **in scope only** when the weak grant ships in an **AWS-managed or AWS-published sample/CFN/runbook** policy (then Tier-2, route `aws-security`).
- **IMDS on these fully-managed Windows hosts** — out of scope as a service-plane target.
- **The AWS service plane** (Nitro, EC2 control plane, storage ENIs) — HARD STOP + disclose; never a target.
- **Pure on-host Windows administration** (registry, DiskPart, bcdedit, `net user`, msconfig) performed by a legitimate local admin — these are OS operations, not service boundaries, except where they action a cross-workload primitive (Area 1).
- **Single-tenant self-DoS** (e.g., a user corrupting their own BCD) — out of scope.
- **Third-party components** (Citrix PV drivers, Microsoft registry/AD behavior) — out of scope except for AWS's *download/distribution* integrity (Area 8).
- **Shared EBS/storage backend infrastructure** — out of scope; only the customer-facing API/IAM behavior is in scope.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens G (SSRF):** N/A. Read the troubleshooting page, `ec2launch-config.md`, `configure-launch-agents.md`, `Upgrading_PV_drivers.md` — no field the service dereferences server-side on the customer's behalf (the only fetch is the *instance* pulling a driver zip, covered under Area 8 transport, not service-side SSRF).
- **Lens K (prompt injection):** N/A — no LLM/agent in this surface.
- **Lens J / FF (OAuth / JWT):** N/A — no 3P linking or token validation on these pages.
- **Lens BB / DD (parser-differential / cache):** N/A — no multi-parser request path or caching layer documented here.
- **Lens W (attestation):** N/A — no Nitro-enclave attestation gate on this surface.
- **Lens EE (name land-grab):** checked — the only predictable global name is the AWS-owned driver S3 bucket; **not** attacker-claimable → N/A (do not probe).
- **Doc gaps to confirm against a lab instance first:**
  1. **Actual default ACLs** on `C:\ProgramData\Amazon\EC2-Windows\Launch\{Scripts,Config}` — the page prescribes editing these but never documents who may write them (Area 7).
  2. Whether the **PV-driver MSI is Authenticode-signed** (the doc prescribes no verification; Windows may still enforce signing) (Area 8).
  3. Whether any **current** Windows AMI's console output can still contain boot-time credential material (Area 9 legacy hypothesis).
- **Owner-to-fix reminder:** most data-reach leads here are *policy-composition* risks whose fix the customer owns; the hunter's job is to distinguish those (informational) from (a) AWS-managed/sample-policy weak defaults and (b) controls that simply do not exist in the API (both in scope).

---

### Appendix — grep crib for the hunter
- `AttachVolume`/`DetachVolume`/`CreateSnapshot`/`CreateImage`/`RunInstances` → `service-authorization/latest/reference/list_ec2.md`
- `GetSnapshotBlock`/`ListSnapshotBlocks`/`ListChangedBlocks` → `list_ebs.md` (prefix `ebs`, ec2-namespaced snapshot ARN)
- `GetConsoleOutput` L8252 · `GetPasswordData` L8498 · `GetConsoleScreenshot` L8258 → `list_ec2.md`
- `StartSession` L1764-1770 → `list_ssm.md`; default-admin `ssm-user` → `session-manager-getting-started-ssm-user-permissions.md`
- cleartext password note → `ec2launch-config.md` L57; default-key-decrypt note → `ebs/latest/userguide/ebsapi-permissions.md` L224
- driver download → `Upgrading_PV_drivers.md` L117-125
