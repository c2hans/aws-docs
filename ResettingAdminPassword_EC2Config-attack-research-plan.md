# Reset Windows admin password via EC2Config — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Config.html` (mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Config.md`) and the adjacent pages reconstructed below. Status: **documentation-derived hypotheses only; nothing tested against a live AWS account.** This plan completes the Windows password-reset set alongside the pre-existing `ResettingAdminPassword_EC2Launch-attack-research-plan.md` and `ResettingAdminPassword_EC2Launchv2-attack-research-plan.md` in this directory; many leads are shared across all three agents and are flagged where EC2Config-specific.

Evidence was gathered via three parallel documentation sweeps (EBS/KMS IAM scoping; password/key-pair/SSM-automation mechanism; AMI/snapshot/EIP lifecycle). Every lead cites the exact page/field.

---

## 0. How to use this document

- Each lead is written as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — in this workflow that means the EC2 infrastructure role `arn:aws:sts::<acct>:assumed-role/aws:ec2-infrastructure/<instance_id>`, the AWS-owned `AWSSupport-EC2Rescue-*` Lambda functions, the automation's temporary service VPC, or any `*.amazonaws.com` service principal — **stop, preserve evidence, flag for AWS-Security disclosure.** Do not escalate.
- **Scope reminder:** this is an *intra-account* workflow by design (volume detach/attach, key pairs, GetPasswordData are all account-scoped). The high-value findings are therefore (a) **intra-account privilege escalation / cross-workload reach** where a low-privilege IAM principal defeats the tag-based scoping, and (b) **cross-account escape** via AMI/snapshot sharing and EIP transfer. Pure single-tenant self-service (an owner resetting their own password) is the documented happy path and out of scope.

---

## 1. Pentest Objectives

Stated as concrete boundary-breach outcomes a hunter should try to achieve:

1. As an IAM principal that is **denied RDP/SSM/`GetPasswordData` on a target instance**, read or modify that instance's root-volume contents offline by detaching it and attaching it to an instance you control — i.e. defeat the tag-based attach/detach scoping.
2. Convert **offline write access to a root volume** into **LocalSystem code execution** on the victim instance's next boot (via `config.xml` plugin tampering: `Ec2SetPassword`, or `Ec2HandleUserData` + injected user data).
3. Make the **encrypted admin password decryptable by a key pair you control** (key-pair substitution via the "Create image → relaunch" fallback or SSM automation), recovering admin on an instance whose original key pair you never held.
4. Recover a **plaintext-equivalent admin credential without any key pair at all** via the SSM Run Command `ResetAccess` path and the predictable Parameter Store secret `/EC2Rescue/Password/<INSTANCE_ID>`.
5. Read a victim volume's data through a **non-`AttachVolume`** path (CreateSnapshot → `ebs:GetSnapshotBlock`; CreateImage → launch/share) and prove the `ebs:*` vs `ec2:*` authorization divergence.
6. Cause the reset-fallback AMI/snapshot (which captures a disk holding a known admin password + customer data) to **escape the account** — share to a foreign account/org/OU/public, then prove the data survives revocation.
7. Hijack the released/transferred **Elastic IP** or **reused key-pair name** to intercept traffic or retain access after the "fix."

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane (SigV4 IAM) via console/CLI/SDK: `StopInstances`, `DetachVolume`, `AttachVolume`, `StartInstances`, `CreateImage`, `RunInstances`, `GetPasswordData`, `GetConsoleOutput`, `CreateSnapshot`, `ModifyImageAttribute`, `ModifySnapshotAttribute`, key-pair APIs, EIP transfer APIs. Plus an **offline filesystem edit** of `config.xml` on a temporary instance (RDP/console). Plus two Systems Manager paths: the Automation runbook **`AWSSupport-ResetAccess`** and the Run Command document **`AWSSupport-RunEC2RescueForWindowsTool`**.

**Processes / hosts / runtimes.**
- **EC2Config service (`EC2Config.exe`)** — runs in the **LocalSystem** account on pre-Windows-Server-2016 AMIs; **end-of-support legacy agent** (`ec2config-service.md`: "EC2Config has reached the end of support"). Reads `C:\Program Files\Amazon\Ec2ConfigService\Settings\config.xml` on boot and executes enabled plugins as SYSTEM.
- **EC2Launch (v1)** / **EC2Launch v2** — the Server-2016/2019 and 2022+ equivalents (`LaunchConfig.json` / YAML `setAdminAccount` task gated by a `.run-once` state marker). Same ciphertext-via-key-pair outcome, different trigger mechanism.
- **EC2Rescue for Windows** — invoked by the SSM runbooks; enables password generation on the attached volume, or writes a new password to Parameter Store.
- **AWS-owned automation fleet** (service plane — HARD STOP): `AWSSupport-ResetAccess` spins up a **temporary VPC**, **`AWSSupport-EC2Rescue-*` Lambda functions**, and a **temporary SSM-enabled helper instance**.

**Accounts / zones.** Single customer account for the core workflow. KMS trust set governs encrypted volumes. EBS KMS grants are issued to the per-target **instance identity-only role** `arn:aws:sts::<acct>:assumed-role/aws:ec2-infrastructure/<instance_id>` (`ebs-encryption-requirements.md`). SSM secret lands in Parameter Store `/EC2Rescue/Password/<INSTANCE_ID>`.

**Resource identifiers.** `i-...` instance IDs, `vol-...` volume IDs, `ami-...`, `snap-...`, EIP allocation IDs — all account-scoped resource ARNs. Note: `volume` and `instance` resource types expose **no `ec2:Owner` condition key** (only `image`/`snapshot` do).

**Identity / credential model.**
- Control plane: IAM SigV4, resource-level permissions gated by **tags only** for volume/instance (no per-principal ownership key).
- Admin password secrecy: purely **cryptographic** — AWS encrypts a random password with the launch **key pair's public key**; `GetPasswordData` returns only ciphertext; the **private key is the only decryption gate** and AWS keeps no copy (`ec2-key-pairs.md`). There is **no IAM condition key binding `GetPasswordData` to the key-pair holder.**
- SSM path: the key-pair gate is bypassed entirely — the new password is encrypted under a KMS key and stored in SSM Parameter Store, re-gated by `ssm:GetParameter` + `kms:Decrypt`.

**Untrusted-data → privileged-action transforms (injection seams).**
- `config.xml` plugin state (`Disabled`→`Enabled`) → on-boot SYSTEM action. `Ec2SetPassword` mints+encrypts a password; **`Ec2HandleUserData`** "Creates and runs scripts created by the user on the first launch" as SYSTEM; `SetPasswordAfterSysprep` "outputs the encrypted password to the console" (`ec2config-service.md`).
- **AMI inheritance:** "If you create an AMI from an instance after updating its settings, the new settings are applied to any instance that's launched from the new AMI" (`ec2config-service.md`) — a tampered `config.xml` propagates to every downstream launch.

### ASCII pipeline

```
                      [Original Windows instance]  (admin password lost; EC2Config = LocalSystem)
                                 | StopInstances
                                 v
                      [Original instance: stopped]
                                 | DetachVolume            <-- boundary: who may detach THIS volume?
                                 v
                       vol-xxxx  (state: available)
                                 | AttachVolume xvdf       <-- boundary: attach to WHICH instance? (temp = attacker-controllable)
                                 v
   [Temporary instance] <--- offline NTFS mount --->  \Program Files\Amazon\Ec2ConfigService\Settings\config.xml
   (different Win OS,        * Ec2SetPassword: Disabled -> Enabled   (intended)
    same AZ)                 * Ec2HandleUserData -> inject SYSTEM payload   (ABUSE)
                             * read SAM / DPAPI / app secrets offline       (ABUSE)
                                 | DetachVolume
                                 v
                       vol-xxxx  (state: available)
                                 | AttachVolume /dev/sda1
                                 v
                      [Original instance] --StartInstances--> EC2Config runs enabled plugins as SYSTEM
                                 |                                   |
                                 | GetPasswordData (ciphertext)      +--> injected user-data runs as SYSTEM (code exec)
                                 v
                      decrypt with key-pair PRIVATE KEY --> RDP as Administrator --> IMDS --> instance-profile role creds

   FALLBACK (lost private key):  CreateImage -> AMI (captures full disk) -> RunInstances w/ attacker key pair
                                 -> ModifyImageAttribute launchPermission (account/org/OU/public)  [data escape]
                                 -> transfer EIP to new/other-account instance                      [IP hijack]

   SSM AUTOMATION (AWS-owned, HARD STOP territory): AWSSupport-ResetAccess
                                 -> temp VPC + AWSSupport-EC2Rescue-* Lambdas + helper instance
                                 -> EC2Rescue enables password gen on attached root volume
                                 -> new password -> Parameter Store /EC2Rescue/Password/<INSTANCE_ID> (KMS)
```

---

## 3. API / Interface Inventory

| Name | Mutating? | Internet-callable | Resource / scoping | Condition keys (notable) | Authorized callers | Notes / lead |
|---|---|---|---|---|---|---|
| `DetachVolume` | Mutating | Yes (control plane) | `instance`, `volume*` | tag keys, `ec2:Encrypted`, `ec2:ParentVolume`, `ec2:VolumeID`, `ec2:Region` — **no `ec2:Owner`** | any IAM principal allowed on the ARN | Core primitive. Only intra-account scoping is the (spoofable) tag. → **A/S** |
| `AttachVolume` | Mutating | Yes | `instance*`, `volume*` | same as Detach; **`ec2:KmsKeyId` NOT in per-action list** (only `ec2:Encrypted`) | ditto | Attach victim volume to attacker instance. Encrypted-volume attach also needs KMS grant success. → **A/S/H** |
| `GetPasswordData` | Non-mutating | Yes | `instance*` only | tag keys, instance-attribute keys — **no volume/encryption/owner key** | ditto | Returns ciphertext regardless of key-pair possession; secrecy = private key only. → **A/U** |
| `GetConsoleOutput` | Non-mutating | Yes | `instance*` | tag keys only (same family) | ditto | `SetPasswordAfterSysprep` "outputs the encrypted password to the console". → **M/U** |
| `CreateImage` | Mutating | Yes | `image*`, `instance*`, `snapshot*` | image carries **`ec2:Owner`**, `ec2:Public`, `ec2:ImageID` | principal allowed on instance ARN | Captures full disk incl. known admin pw + data; no documented sanitization step. → **Q/AA** |
| `RunInstances` | Mutating | Yes | `image*`(+`ec2:Owner`/`ec2:Public`), `instance*`, `key-pair`, ... | per-resource | principal | Relaunch with attacker key pair re-triggers pw gen → key substitution. → **EE** |
| `CreateSnapshot` | Mutating | Yes | `snapshot*`, `volume*` | tag keys, `ec2:ParentVolume`, size/type — **no owner key** | principal | Alternate offline-read entry → EBS direct APIs. → **X** |
| `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` / `ListChangedBlocks` | Non-mutating | Yes (EBS direct API) | `snapshot*` | `aws:ResourceTag`, `ebs:ParentSnapshot`, `ebs:VolumeSize` — **no owner key** | principal (separate `ebs:` family) | **AWS-documented divergence** from `ec2:*` scoping. → **X** |
| `ModifyImageAttribute` (launchPermission) | Mutating | Yes | `image` | `ec2:Owner`, `ec2:Public` | image owner | Share to account / **Org / OU / public**; org/OU target not membership-validated. → **AA** |
| `ModifySnapshotAttribute` (createVolumePermission) | Mutating | Yes | `snapshot` | tag keys | snapshot owner | Separate object from AMI; block-public-snapshots does NOT block public-AMI data access. → **AA** |
| `ModifyInstanceAttribute` (userData) | Mutating | Yes | `instance*`, `volume`, `security-group` | instance/volume key families | principal | Online analog of config tamper → SYSTEM exec at next boot. → **B/E** |
| `EnableAddressTransfer` / `AcceptAddressTransfer` | Mutating | Yes | EIP | — | source / transfer account | Cross-account EIP transfer, 7-day handshake, no AWS notification. → **AA** |
| SSM `AWSSupport-ResetAccess` (Automation, **Owned by Amazon**) | Mutating | Yes (SSM) | automation doc | — | caller or supplied `AssumeRole` | AWS-authored runbook; self-provisions IAM role; HARD STOP on its service-plane fleet. → **R/S** |
| SSM `AWSSupport-RunEC2RescueForWindowsTool` → `ResetAccess` | Mutating | Yes (SSM Run Command) | managed instance | SSM document/instance scoping | `ssm:SendCommand` holder | Re-enables disabled admin; writes pw to `/EC2Rescue/Password/<id>`. Bypasses key-pair gate. → **T/E** |

Doc-planted leads to keep verbatim:
- `ec2config-service.md`: EC2Config "runs in the **LocalSystem** account"; `Ec2HandleUserData` runs user scripts on first launch; AMI inheritance of settings.
- `API_GetPasswordData`: "the password is **not generated for rebundled AMIs unless `Ec2SetPassword` is enabled before bundling**" — EC2Config branch still live.
- `ebsapi-permissions.md` **Important**: granting `ebs:*` "might give access to a user who is denied access to the same resource through the Amazon EC2 APIs."

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (observation that proves it broke) |
|---|---|---|---|
| Low-priv IAM principal (same account) | Another workload's **root EBS volume** | `DetachVolume`+`AttachVolume` to an attacker-controlled instance, scoping is tag-only | Attacker mounts and reads/modifies a volume whose instance it is denied RDP/SSM/`GetPasswordData` on — **cross-workload disk access via spoofable tag**. |
| Offline-mounted volume | Running-OS access control | NTFS mount on temp instance | Any file the live Windows ACL would protect (SAM, DPAPI, `config.xml`, app secrets) is read/written offline — **OS access control bypassed by design**. |
| `config.xml` (data) | **LocalSystem** action on boot | enable `Ec2SetPassword` / `Ec2HandleUserData` plugin | Attacker-chosen plugin or injected user data executes as SYSTEM on next boot — **data→SYSTEM-exec**. |
| Key-pair holder | Encrypted admin password | `Ec2SetPassword` encrypts to launch key's public key; relaunch substitutes the key pair | Attacker's key pair decrypts the admin password of an instance whose original key it never held — **credential-vending via key substitution**. |
| `ssm:SendCommand` caller | Disabled admin account + Parameter Store secret | `AWSSupport-RunEC2RescueForWindowsTool` `ResetAccess` | Admin re-enabled and new password readable at `/EC2Rescue/Password/<id>` with `ssm:GetParameter`+`kms:Decrypt` — **key-pair gate bypassed**. |
| EBS IAM layer | KMS trust set (CMK) | attach encrypted volume → `CreateGrant` to instance identity-only role | Attach of a victim's CMK volume **completes** for a principal who should be walled off (default key policy trusts account IAM) — reads succeed. |
| `ec2:*` snapshot/volume authz | `ebs:*` direct-API authz (same snapshot) | `CreateSnapshot` then `ebs:GetSnapshotBlock` | Principal denied `ec2:CreateVolume`/`CopySnapshot` reads raw blocks via `ebs:*` — **parity gap AWS itself warns about**. |
| AMI/snapshot owner | Foreign account / org / OU / public | `ModifyImageAttribute` / `ModifySnapshotAttribute` | A reset-fallback image capturing a known admin pw + data is launched/copied by a foreign principal; **data survives revocation**. |
| Source account | EIP transfer account | `Enable`/`AcceptAddressTransfer` | A foreign account accepts the instance's EIP (only a 12-digit ID gates it, no AWS notification) → **IP/traffic carryover**. |
| **Any customer surface** | **AWS service plane** (EC2 infra role, `AWSSupport-EC2Rescue-*` Lambdas, temp VPC) | SSM automation internals | **HARD STOP** — any AWS-owned identity/credential/ARN observed → preserve + disclose. |

---

## 5. Recommended Areas of Focus

> Ordered by priority. Each block is Background / Security Concern / High-level Test Scenarios / Doc evidence / Severity-if-true / Stop condition.

### Area 1 — Volume detach/attach scoping: cross-workload disk access as an unprivileged primitive  (Lens A / S / U)
**Background.** The entire reset workflow rests on detaching a stopped instance's root volume and attaching it to a *temporary* instance, then mounting it offline. The only documented constraints on the temporary instance are technical (same AZ; different Windows OS to avoid disk-signature collision) — **none are IAM/ownership-related**. Within an account there is no per-principal volume ownership: `volume` and `instance` resource types expose **no `ec2:Owner` condition key**; AWS's own canonical attach/detach policy (`security_iam_id-based-policy-examples.md`, "Attach and detach volumes") scopes by a **mutable tag** (`volume_user=${aws:username}`).

**Security Concern.** A low-privilege principal with `ec2:DetachVolume`/`ec2:AttachVolume` (and `StopInstances`) but **no** RDP/SSM/`GetPasswordData` on a target can mount that target's root volume offline on an instance it controls and read/modify everything — defeating the live-OS access control. Worse, if the tag-based scoping is the intended control, any principal holding generic `ec2:CreateTags` can **set the `volume_user` (or equivalent) tag value** to satisfy the attach policy, unless a separate `ec2:CreateTags` statement locks it (`ec2:CreateAction=CreateVolume`).

**High-level Test Scenarios (falsifiable claims).**
- *Claim:* With attach/detach scoped by tag `volume_user=${aws:username}`, a principal with `ec2:CreateTags` can retag a victim volume to its own username and then attach it. → *Oracle:* `CreateTags` succeeds on the foreign volume, then `AttachVolume` to the attacker instance returns `attached` → **confirmed**; `AttachVolume` returns `AccessDenied` (tag immutable / CreateTags locked) → refuted.
- *Claim:* No condition key can constrain attach/detach to "same owner" — only tags. → *Oracle:* attempt to author a Deny on `AttachVolume` keyed on anything but a tag; confirm `ec2:Owner` is rejected/not evaluated for `volume`.
- *Claim:* `StopInstances` + detach of a *running* production root volume is not blocked beyond tags → availability + offline-read in one.

**Doc evidence.** `list_ec2.md` AttachVolume/DetachVolume (no `ec2:Owner`); `security_iam_id-based-policy-examples.md` tag-scoped example; `ResettingAdminPassword_EC2Config.md` Steps 2–3 (only AZ/OS constraints). **Severity-if-true:** cross-workload disk + credential read within an account = **High** (customer-controllable, but the scoping footgun is subtle and the primitive is AWS-documented). **Stop condition:** one foreign volume mounted read-only with canary proof; do not read real customer data.

### Area 2 — Offline `config.xml` tampering → LocalSystem code execution + persistence  (Lens B / E / Q)
**Background.** EC2Config runs as **LocalSystem** and executes `config.xml` plugins on boot. Step 4 of the workflow has the operator flip `Ec2SetPassword` `Disabled`→`Enabled` offline. But the same offline write can enable **`Ec2HandleUserData`** ("Creates and runs scripts created by the user on the first launch … Commands wrapped in script tags are saved to a batch file, and … PowerShell tags … to a .ps1 file") and plant attacker user data, or alter any plugin.

**Security Concern.** Offline write access to a root volume (obtained via Area 1) converts to **SYSTEM-level code execution** on the victim instance's next boot — a privilege escalation that needs no RDP, no password, no SSM. Because EC2Config settings are **inherited into any AMI** created from the instance, a tamper also becomes a **persistence/supply-chain** vector that propagates to every downstream launch and, if the AMI is shared, across accounts (chains to Area 6).

**High-level Test Scenarios.**
- *Claim:* Enabling `Ec2HandleUserData` + writing a benign canary user-data script offline causes that script to run as SYSTEM on next boot. → *Oracle:* canary artifact (e.g. a timestamped file / outbound beacon to an attacker-owned sink) appears after `StartInstances` → confirmed.
- *Claim:* The online analog `ModifyInstanceAttribute(userData)` on a stopped instance achieves the same SYSTEM exec without touching the volume. → *Oracle:* user-data re-execution on next boot. (Known EC2 privesc exemplar — verify EC2Config honors it.)
- *Claim:* Offline mount exposes the SAM/DPAPI and lets the attacker extract/replace local credentials independent of the Ec2SetPassword flow.

**Doc evidence.** `ec2config-service.md` (LocalSystem; `Ec2HandleUserData`; AMI inheritance); `ResettingAdminPassword_EC2Config.md` Step 4. **Severity-if-true:** SYSTEM exec on a victim workload = **High**; cross-account if the tampered AMI is shared = **Critical**. **Stop condition:** canary-only payload; no lateral movement.

### Area 3 — Key-pair substitution: recovering admin on an instance whose key you never held  (Lens U / EE / C)
**Background.** The admin password's only secrecy gate is the launch key pair's private key; `GetPasswordData` returns ciphertext to **any** principal with the IAM permission on the instance ARN (no key-pair binding). The "lost private key" fallback explicitly tells the operator to **Create image → relaunch with a new key pair → retrieve the password with the new private key** — i.e. the ciphertext is re-encrypted to whichever key pair is present at the next generation event.

**Security Concern.** An attacker who can `CreateImage` + `RunInstances` (Area 1/2 reach) can relaunch a victim's disk under an **attacker-owned key pair** and read the admin password — the key pair is not bound to the original owner in any way that survives the workflow. Separately, `GetPasswordData` + `GetConsoleOutput` have **no owner condition key**, so the ciphertext (and, per `SetPasswordAfterSysprep`, the console-echoed encrypted password) is readable intra-account by anyone who can reach the instance resource; only the private key stands between them and plaintext.

**High-level Test Scenarios.**
- *Claim:* Relaunching from a CreateImage AMI with an attacker key pair and re-enabling `Ec2SetPassword` yields an admin password the attacker can decrypt. → *Oracle:* `GetPasswordData` ciphertext decrypts with the attacker private key → confirmed.
- *Claim:* `GetPasswordData` returns the ciphertext for an instance the caller cannot RDP to (no key-pair binding in IAM). → *Oracle:* non-empty `passwordData` for a principal lacking the private key.
- *Claim:* `whoAMI`-style — the fallback's "Launch instance from AMI" (and automation's AMI creation) resolve an image by **name without `--owners`**, letting an attacker-published AMI of the same name be selected. → *Oracle:* a `describe-images --filters Name=name,...` with no owner constraint returns an attacker image. **Doc gap:** `finding-an-ami.md` never warns against name-only resolution.

**Doc evidence.** `ec2-key-pairs.md`; `API_GetPasswordData.md`; `list_ec2.md` GetPasswordData/GetConsoleOutput (no owner key); `ResettingAdminPassword_EC2Config.md` fallback; `ec2config-service.md` `SetPasswordAfterSysprep`; `finding-an-ami.md`. **Severity-if-true:** admin recovery without the owner's key = **High**; whoAMI name-squat = **High** (end executes attacker code/credential). **Stop condition:** prove decryptability with a canary key pair; don't pivot into the recovered admin session.

### Area 4 — SSM `ResetAccess`: key-pair-less credential recovery + predictable Parameter Store secret  (Lens T / E / R)
**Background.** `AWSSupport-RunEC2RescueForWindowsTool`'s `ResetAccess` action "Resets the local Administrator password … stored in Parameter Store as `/EC2Rescue/Password/<INSTANCE_ID>` … encrypted automatically with the default KMS key." `ResettingAdminPassword.md` adds that this can **re-enable a disabled local administrator account**. The instance role needs only `ssm:PutParameter` on that path (+`kms:Encrypt` if custom key).

**Security Concern.** This path **bypasses the key-pair cryptographic gate entirely.** A principal with `ssm:SendCommand` against the target can re-enable a deliberately-disabled admin and mint a fresh credential; the secret lands at a **deterministic, enumerable path** (`/EC2Rescue/Password/<INSTANCE_ID>`) retrievable by anyone with `ssm:GetParameter` + `kms:Decrypt` on that parameter/key — a different and often broader IAM reachability than `GetPasswordData`. No documented check confirms the admin account was *intentionally* disabled before re-enabling it.

**High-level Test Scenarios.**
- *Claim:* `ssm:GetParameter` on `/EC2Rescue/Password/<id>` + `kms:Decrypt` on the **default** key succeeds for a principal denied `ec2:GetPasswordData` on the instance (cross-service secret reachability). → *Oracle:* cleartext password returned via SSM while `GetPasswordData` is denied — prove both in one run under a scoped role.
- *Claim:* The path is enumerable from a public instance ID → an attacker who learns `i-...` can target the exact parameter.
- *Claim:* The secret **outlives** the operation (no cascade delete) → a stale admin credential lingers in Parameter Store.
- *Claim (Lens R/S, in scope — AWS-authored):* the `AWSSupport-ResetAccess` CFN role pairs `iam:CreateRole`+`iam:AttachRolePolicy`+`iam:PassRole` scoped only to the **name prefix `AWSSupport-EC2Rescue-*`** with broad `ec2:*`/`lambda:*`/`Resource:*` statements. → audit via `iam:SimulatePrincipalPolicy`: can a principal holding exactly this policy self-escalate by creating/attaching to an `AWSSupport-EC2Rescue-*`-named role? Does `AmazonSSMAutomationRole` widen it further?

**Doc evidence.** `ec2rw-ssm.md` (ResetAccess, PutParameter policy, path); `automation-ec2reset.md` (Owned by Amazon; CFN IAM policy block; Lambda/VPC/helper fleet); `ResettingAdminPassword.md` (re-enable disabled admin). **Severity-if-true:** key-pair-less admin recovery / cross-service secret reach = **Medium–High**; AWS-authored-artifact self-escalation = **High** (reportable Tier 2, routed `aws-security`). **Stop condition:** HARD STOP if any `AWSSupport-EC2Rescue-*` / EC2-infra identity is observed in the automation internals.

### Area 5 — Offline-read action-family parity: `AttachVolume` vs `CreateSnapshot`+`ebs:GetSnapshotBlock` vs `CreateImage`  (Lens X)
**Background.** The same "read a victim disk offline" outcome has three IAM-distinct paths. AWS's own `ebsapi-permissions.md` opens with an **Important** warning that granting the `ebs:*` direct-API family "might give access to a user who is denied access to the same resource through the Amazon EC2 APIs, such as `CopySnapshot` or `CreateVolume`."

**Security Concern.** A principal walled off from one path may reach the identical bytes through a sibling with different (or absent) condition-key coverage. All three — `ec2:AttachVolume`, `ec2:CreateSnapshot`→`ebs:GetSnapshotBlock`/`ListSnapshotBlocks`/`ListChangedBlocks`, `ec2:CreateImage` — are **tag-only scoped with no owner key** (except `image` which uniquely carries `ec2:Owner`/`ec2:Public`).

**High-level Test Scenarios.**
- *Claim:* A role **denied `ec2:CreateVolume`/`ec2:CopySnapshot`** on a snapshot can still `ebs:GetSnapshotBlock` it and reconstruct the disk. → *Oracle:* raw block data returned where the EC2-API path returns `AccessDenied` → confirmed (matches AWS's own warning).
- *Claim:* `CreateSnapshot` on a victim volume is gated only by tags, so Area-1 tag spoofing extends to the snapshot path.
- *Claim:* Validator divergence — the three paths return different error shapes (`AccessDenied` vs `NotFound` vs 500) forming an enumeration oracle for foreign resource IDs.

**Doc evidence.** `ebsapi-permissions.md` Important; `list_ebs.md` (ebs:* condition keys, no owner); `list_ec2.md` CreateSnapshot/CreateImage. **Severity-if-true:** EC2-layer restriction bypassed via `ebs:*` = **High** (cross-workload data). **Stop condition:** canary snapshot only.

### Area 6 — AMI/snapshot share + revocation incompleteness: the reset image escapes the account  (Lens AA / Q)
**Background.** The fallback runs **Create image** on a disk that (per the workflow) now holds a **known admin password + customer data**, with **no documented sanitization/sysprep step** before imaging — in contrast to the explicit sanitization checklist AWS gives for intentionally-shared AMIs (`building-shared-amis.md`). The resulting AMI/snapshot can be shared to an account, **Org/OU, or public**.

**Security Concern.** (a) A recipient of `launchPermission` can **launch then re-AMI** the disk ("after they have launched an instance using your AMI, they can then create an AMI from the instance they launched") — a one-way escape of the owner's control. (b) **Revocation is incomplete**: removing an account's launch permission when it is covered by an **org/OU grant returns a success message but access persists**. (c) **Control gap**: "Block public access for snapshots does not prevent the public sharing of EBS-backed AMIs" — the same disk data stays reachable via the AMI launch path. (d) **Unvalidated grantee**: "The AMI owner can share an AMI with any organization or OU, including organizations and OUs that they're not a member of" — no membership/existence check documented.

**High-level Test Scenarios.**
- *Claim:* An AMI created by the reset fallback and shared to a foreign account lets that account launch, read the disk (incl. the known admin password), and re-AMI it — surviving later unshare. → *Oracle:* foreign-account launch succeeds post-revocation / a derived AMI persists.
- *Claim:* `ModifyImageAttribute` accepts a **nonexistent / non-member OrganizationArn/OU** without error.
- *Claim:* With "Block public access for snapshots" enabled, publicly sharing the **AMI** still exposes the snapshot data via `CreateVolume` from the launched instance.
- *Claim:* The reset AMI contains the admin password in `Sysprep.xml` / `LaunchConfig.json` (clear text until Sysprep) if `RemoveCredentialsfromSyspreponStartup`/post-Sysprep cleanup didn't run — credential baked into the shared image.

**Doc evidence.** `sharingamis-explicit.md`, `sharingamis-intro.md`, `share-amis-with-organizations-and-OUs.md`, `share-amis-org-ou-manage.md` (success-but-persists), `block-public-access-snapshots.md`, `ebs-modifying-snapshot-permissions.md`, `building-shared-amis.md`, `ec2config-service.md` (`SetPasswordAfterSysprep`, `RemoveCredentialsfromSyspreponStartup`). **Severity-if-true:** cross-account disclosure of admin credential + data = **Critical**; revocation false-confidence = **High**. **Stop condition:** share only between two accounts you own, with canary data.

### Area 7 — Elastic IP transfer & key-pair name reuse: post-"fix" hijack  (Lens AA / EE)
**Background.** The fallback instructs transferring the EIP to the new instance and reusing the old key-pair *name* (after deleting the key-pair object). EIP transfer is a cross-account 7-day handshake gated only by a 12-digit account ID, with **no AWS notification** to the recipient. Deleting a key pair does **not** invalidate a private key someone already holds, and public-key material is **copied into AMIs**.

**Security Concern.** (a) A mistyped/socially-engineered `transfer-account-id` lets an attacker **accept the instance's EIP** (blocked at accept-time only if still associated or carrying a reverse-DNS PTR; **IP reputation/forward-DNS/pinned-TLS carryover is never addressed**). (b) Reusing a deleted key pair's name does nothing to revoke a leaked old private key; if that key's public material was on disk at Create-Image time it is inherited by the new AMI/instance — the "fix" fails to lock out the prior holder.

**High-level Test Scenarios.**
- *Claim:* `AcceptAddressTransfer` succeeds for an attacker account given only the account ID, with no secondary ownership proof. → *Oracle:* transfer completes to a second account you own.
- *Claim:* After the "reset," an actor holding the **old** private key still connects because the public key was carried into the relaunched AMI. → *Oracle:* old key authenticates to the new instance.

**Doc evidence.** `transfer-EIPs-intro-ec2.md`; `delete-key-pair.md`; `replacing-key-pair.md`. **Severity-if-true:** EIP/traffic hijack or retained access after remediation = **High**. **Stop condition:** two-account test with your own accounts; no real EIP reputation abuse.

### Area 8 — Audit-log evasion of the offline tamper  (Lens O, enabler)
**Background.** CloudTrail records `StopInstances`, `DetachVolume`, `AttachVolume`, `StartInstances`, `CreateImage` — but the **content change to `config.xml` on the mounted volume is a filesystem write inside the temporary instance and produces no AWS-API event.**
**Security Concern.** The actual malicious act (plugin/user-data tamper, SAM read) is invisible to CloudTrail; only the volume-shuffle verbs are logged, and those are indistinguishable from the legitimate reset runbook.
**Test Scenario.** *Claim:* No durable AWS-side signal distinguishes a legitimate password reset from a malicious offline tamper. → *Oracle:* review whether any event captures the config delta. **Severity:** Low/Informational (raises severity of Areas 1–3 as an enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Low-priv principal mounts foreign root volume offline | `AttachVolume`/`DetachVolume` | Tag-based IAM scoping (no `ec2:Owner`); AZ/OS-collision constraints only |
| Tag spoofing to satisfy attach policy | `CreateTags` + attach policy | Separate `ec2:CreateTags` lock (`ec2:CreateAction`) — often omitted |
| Offline `config.xml` → SYSTEM exec on boot | EC2Config LocalSystem plugins | None documented; relies on volume-attach control holding |
| Key-pair substitution to read admin password | `CreateImage`+`RunInstances`+`Ec2SetPassword` | Private-key possession is the *only* gate; `GetPasswordData` has no owner key |
| whoAMI name-resolution of relaunch image | `RunInstances` / `describe-images` | `--owners`/`ImageOwnerAlias` best practice; **no enforced constraint, no doc warning** |
| Key-pair-less recovery via SSM | `ResetAccess` + Parameter Store | `ssm:SendCommand` + `ssm:PutParameter` scoping; default KMS key |
| `ebs:*` vs `ec2:*` parity bypass | EBS direct APIs | AWS **Important** warning only; no technical unification |
| Reset AMI/snapshot escapes account | `ModifyImageAttribute`/`ModifySnapshotAttribute` | launchPermission/createVolumePermission; block-public-access (per-object, non-overlapping) |
| Revocation leaves access live | org/OU launch permission | Documented as returning success while access persists |
| EIP transfer hijack | `Accept/EnableAddressTransfer` | 7-day handshake; accept-time checks (association, reverse DNS) only |
| AWS automation service-plane reach | `AWSSupport-ResetAccess` fleet | **HARD STOP** — shared-responsibility line |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **A customer resetting their own instance's password** via this documented runbook — the happy path.
- **Single-tenant self-DoS** — disk-signature collision from attaching two same-OS volumes; stopping your own instance; losing instance-store data on stop (AWS warns of all three). Operational, not a boundary breach.
- **IMDS on the managed Windows host** itself (169.254.169.254 route added by EC2Config `ShouldAddRoutes`) — IMDS reachability on a host you already control as admin is out of scope; only interesting as the *post-exploitation* pivot in Area 2's chain, not a standalone bug.
- **Customer-authored least-privilege footguns** — a customer who writes a loose attach/detach policy owns that risk. **Carve-out:** the AWS-authored `AWSSupport-ResetAccess` CFN role, `AmazonSSMAutomationRole`, and the EC2Rescue instance-profile policy are **in scope** (Area 4, Lens R/S).
- **Shared EBS/KMS backend infrastructure**, Nitro/host isolation — AWS service-plane, HARD STOP.
- **Decrypting someone's password without their private key via RSA attacks** — cryptographic brute force, not a documentation-derived boundary.

---

## 8. Null Hypotheses / Doc Gaps

Lenses examined and **not** fired (pages read named, per discipline):

- **Lens G (SSRF).** N/A — read `ResettingAdminPassword_EC2Config.md`, `ec2config-service.md`, `ec2-windows-passwords.md`, `ec2-key-pairs.md`: no field the service dereferences server-side on the customer's behalf. The only link-local reference is EC2Config adding a host-local route to `169.254.169.254` for IMDS (a guest-side route, not a server-side fetch). *Doc-gap caveat:* `ActivationSettings.xml` `ReadFromUserData`/`DiscoverFromZone`/`TargetKMSServer` point the KMS-activation client at an operator-supplied host — worth a glance if a hunter can influence those offline, but it is a guest→KMS-activation DNS lookup, not a service-plane fetch. Low priority.
- **Lens F (translation/injection).** N/A — no query/protocol translation layer in this workflow (XML config is parsed by the guest agent, not a multi-tenant service).
- **Lens K (prompt injection).** N/A — no LLM/agent.
- **Lens D / V (network segmentation).** N/A for the customer workflow (managed single host). The SSM automation's temporary VPC is **service-plane** → HARD STOP, not a test target.
- **Lens W (attestation).** N/A — no Nitro Enclave / PCR gating in password reset.
- **Lens Y (transport/signature).** Minimal — control plane is standard SigV4 over TLS; no service-specific endpoint documented here. Note only: `GetPasswordData` ciphertext in transit is already asymmetric-encrypted, so TLS interception alone doesn't yield plaintext.
- **Lens J / P / FF (OAuth / registration / JWT).** N/A — no 3P linking, no identity-proofing workflow, no bearer-token validation. (Key-pair "name reuse" touches a registration-uniqueness shape and is captured in Area 7.)
- **Lens BB / CC / DD (parser-differential / asserted-identity / cache).** N/A — no multi-parser request path, authorizer context, or caching layer in this console/CLI workflow.
- **Lens I (tagging).** Folded into **Lens S / Area 1** — here tagging *is* the access-control mechanism, so it is treated as high-value, not a standalone null.

**Doc gaps to confirm against a live account before weighting:**
1. Whether `ec2:CreateTags` is realistically lockable in customer environments (Area 1 hinges on this).
2. Whether `GetConsoleOutput` still surfaces the `SetPasswordAfterSysprep` encrypted-password echo on current EC2Config builds (Area 3 / Lens M).
3. Whether the SSM `/EC2Rescue/Password/<id>` parameter is deleted after the runbook completes or lingers (Area 4 persistence).
4. `finding-an-ami.md` carries **no warning** against name-only AMI resolution — confirm whether the console "Launch instance from AMI" / the automation's AMI step pin an owner (Area 3 whoAMI).

---

### Appendix — Primary source index

| Topic | Mirror path |
|---|---|
| Reset via EC2Config (target) | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Config.md` |
| Reset overview / EC2Rescue+SSM note | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ResettingAdminPassword.md` |
| EC2Config service & plugins (LocalSystem, config.xml) | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2config-service.md` |
| Windows passwords / agent mapping | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-windows-passwords.md` |
| GetPasswordData API | `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_GetPasswordData.md` |
| Key pairs | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-key-pairs.md`, `delete-key-pair.md`, `replacing-key-pair.md` |
| EC2 IAM reference | `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` |
| EBS direct-API IAM reference | `/work/aws-docs/docs/service-authorization/latest/reference/list_ebs.md` |
| EBS attach/detach policy examples | `/work/aws-docs/docs/ebs/latest/userguide/security_iam_id-based-policy-examples.md` |
| EBS encryption / KMS | `/work/aws-docs/docs/ebs/latest/userguide/ebs-encryption-requirements.md`, `how-ebs-encryption-works.md`, `encryption-examples.md` |
| EBS direct-API permission warning | `/work/aws-docs/docs/ebs/latest/userguide/ebsapi-permissions.md` |
| SSM `AWSSupport-ResetAccess` | `/work/aws-docs/docs/systems-manager/latest/userguide/automation-ec2reset.md` |
| EC2Rescue + Run Command | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2rw-ssm.md` |
| AMI sharing | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/sharingamis-explicit.md`, `sharingamis-intro.md`, `share-amis-with-organizations-and-OUs.md`, `share-amis-org-ou-manage.md`, `building-shared-amis.md`, `cancel-sharing-an-AMI.md`, `finding-an-ami.md` |
| Snapshot sharing / block-public-access | `/work/aws-docs/docs/ebs/latest/userguide/ebs-modifying-snapshot-permissions.md`, `block-public-access-snapshots.md` |
| EIP transfer | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/transfer-EIPs-intro-ec2.md` |
| EC2Launch v1 / v2 (parity) | `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2launch-config.md`, `ec2launch-v2-task-definitions.md` |
