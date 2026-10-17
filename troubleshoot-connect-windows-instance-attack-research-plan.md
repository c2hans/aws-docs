# EC2 Windows RDP Troubleshooting Flows — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.html` (and `.md`), plus linked pages: `ResettingAdminPassword*.md` (offline mirror), `API_GetPasswordData.html`, and the AWS Systems Manager runbook/userguide pages `automation-awssupport-troubleshootrdp`, `automation-awssupport-executeec2rescue`, `automation-awssupport-startec2rescueworkflow`, `automation-ec2rescue`, `automation-ec2reset`, `automation-permissions`. IAM facts cross-checked against the offline Service Authorization Reference `docs/service-authorization/latest/reference/list_ec2.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.** Produced with the `security-questionbuilder` skill (lens catalog A–FF).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **Scope framing is the headline for this target.** This page is an *operational runbook*, not a service API surface. Almost every primitive it describes resolves to **customer-account IAM policy design** — i.e. a customer footgun, which the skill places **out of scope** when the customer authored the policy. The in-scope leads are the narrow set where **AWS ships the artifact verbatim** (the `automation-ec2reset` sample IAM policy with wildcard `Resource:"*"` + `iam:PassRole`), where **AWS owns a storage/KMS default** (the `/ec2rl/openssh/{instanceId}/key` SSM SecureString under the default managed key), or where a **documented guarantee lacks an enforcing mechanism**. Those are flagged **[IN-SCOPE / Tier 2]** below; everything else is flagged **[CUSTOMER-CONFIG]** and should be reported, if at all, as a hardening note, not a service bug.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (SSM/EC2/Lambda control-plane credentials, the EC2Rescue helper fleet identity), stop, preserve evidence, flag for AWS-Security disclosure. The subagent passes found **no** such reach — all mechanisms terminate inside the customer account.

---

## 1. Pentest Objectives
Stated as concrete breach outcomes a hunter would try to produce:
1. From a **low-privileged IAM principal** (support/ops-style grant, no RDP creds, no `ssm:SendCommand`), gain Administrator or disk-level access to a Windows instance the principal does not operationally own — via the password-reset runbook, the TroubleshootRDP firewall-disable, or an EBS root-volume detach/attach.
2. Retrieve another workload's **secret at rest** (reset SSH key in Parameter Store, GetPasswordData ciphertext, EC2Rescue OS logs) through a **storage service whose IAM/KMS is weaker than the originating EC2/RDP control**.
3. Prove a **documented security guarantee is advisory only** — e.g. "upload logs to a bucket *in your account*", "restore to the original instance" — by exercising the unconditioned path.
4. Confirm whether any runbook's EC2/EBS/S3 actions are scoped to a **specific target instance** or whether a single document-level grant reaches **every** instance in the account.

---

## 2. Components, Assets, and Design

**Customer-facing interface(s).**
- **RDP / TCP 3389** to the Windows instance (the thing being troubleshot). Default two concurrent sessions.
- **EC2 console + EC2 API** (`GetPasswordData`, `StopInstances`, `DetachVolume`, `AttachVolume`, `CreateImage`, `ModifyInstanceAttribute`, key-pair APIs).
- **SSM Automation API** (`ssm:StartAutomationExecution`) invoking the AWS-owned runbooks `AWSSupport-TroubleshootRDP`, `AWSSupport-ExecuteEC2Rescue`, `AWSSupport-ResetAccess` (ec2reset).

**Processes / fleets behind it.**
- **EC2Launch v2 / EC2Launch / EC2Config** agent on the Windows instance (generates and encrypts the Administrator password at first boot; regenerates it on reset).
- **SSM Automation engine** (runs the runbook steps under an **AutomationAssumeRole** — optional; defaults to the *caller's* identity).
- **EC2Rescue "helper" instance** — an SSM-managed instance the automation **creates in the customer account** to perform offline volume surgery on an unreachable/unmanaged target. (This is the mechanism behind "works on instances not enabled for Systems Manager".)
- **Windows registry hive** on the target's root EBS volume (`fDenyTSConnections`, `EnableFirewall`) — mutated either online (RunPowerShell via agent) or offline (detach/attach to helper).

**Accounts / isolation model.** Everything here is **single customer account, single region**. SSM Automation and the EC2/EBS/S3 actions are all account-scoped; there is **no documented cross-account instance-targeting** path. The only "shared" surface is **cross-team within one account** (an over-broad ops role reaching instances other teams own). No multi-tenant AWS fleet is exposed to the customer in these flows.

**Resources & identifier shapes.** `InstanceId` / `UnreachableInstanceId` (`i-0123…`, **not secret, enumerable**); EBS `VolumeId`; AMI `ImageId` (orphaned backup AMI named `AWSSupport-EC2Rescue:{instanceId}`); SSM parameter path `/ec2rl/openssh/{instanceId}/key` (**deterministic from a public id**); the RSA key-pair (public key held by EC2, private key held only by the customer).

**Identity / credentials.** IAM SigV4 for all API/automation calls. The Administrator password is **RSA-encrypted to the key pair's public key** and decrypted **client-side** with the private key — AWS holds no secondary secret, so possession of the private key alone decrypts any captured ciphertext, forever, with no server-side revocation.

**Where untrusted / sensitive data comes to rest (injection/exfil seams).**
- Administrator password **ciphertext** → `GetPasswordData` response, CloudTrail event body, CLI/SDK logs.
- Reset **SSH private key** (Linux targets of the same runbook) → **SSM Parameter Store SecureString** `/ec2rl/openssh/{instanceId}/key`.
- Instance **OS logs** (event logs, memory dumps) → customer-named **S3 bucket** via `LogDestination`.
- Full **root-volume contents** (SAM hive, DPAPI blobs) → readable by whoever can attach the volume to an instance they control.

```
                 ┌─────────────────────────────────────────────────────────┐
                 │                 Customer AWS account                     │
  IAM caller ───►│  ssm:StartAutomationExecution                            │
  (support/ops)  │        │                                                 │
                 │        ▼  AutomationAssumeRole (or caller identity)       │
                 │  ┌──────────────┐   online (agent) ┌──────────────────┐  │
                 │  │ AWSSupport-*  │─────────────────►│ Target Windows   │  │
                 │  │  runbook      │  RunPowerShell   │ instance (RDP)   │  │
                 │  └──────┬───────┘                   └──────────────────┘  │
                 │         │ offline (unreachable / not SSM-managed)         │
                 │         ▼  Stop → DetachVolume → AttachVolume             │
                 │  ┌──────────────┐   xvdf  ┌──────────────────┐            │
                 │  │ EC2Rescue    │◄────────│ target ROOT EBS  │            │
                 │  │ helper inst. │ mount   │ volume (offline) │            │
                 │  └──────┬───────┘         └──────────────────┘            │
                 │         ├──► S3 LogDestination (OS logs)                  │
                 │         ├──► SSM Param /ec2rl/openssh/{id}/key (SSH key)  │
                 │         └──► orphaned backup AMI (persists)               │
                 └─────────────────────────────────────────────────────────┘
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (what proves it broke) |
|---|---|---|---|
| Low-priv IAM caller | Target instance Administrator session | `ssm:StartAutomationExecution` on `AWSSupport-ResetAccess`/`TroubleshootRDP` | Caller gains admin / disables firewall+NLA on an instance it holds **no** `ssm:SendCommand` or RDP creds for → **boundary = "only an instance admin changes OS security controls" broke** |
| IAM caller (no `GetPasswordData` need-to-know) | Admin password ciphertext | `ec2:GetPasswordData` scoped only by instance ARN | Ciphertext retrieved for an instance the caller doesn't operate → sets up offline decrypt if a private key leaks |
| AutomationAssumeRole | S3 bucket outside the account | `LogDestination` / `S3BucketName` `s3:PutObject` with no documented same-account assertion | OS logs of instance A written to a bucket in a **different account** the caller controls → **"upload to a bucket in your account" guarantee is advisory** |
| Principal denied EC2/RDP on instance | Reset SSH key for that instance | `ssm:GetParameter` + default-KMS `kms:Decrypt` on `/ec2rl/openssh/{id}/key` | Reading another instance's SSH key via SSM when the origin EC2 path denies you → **storage-service IAM weaker than origin** |
| Caller with EBS actions only | Full disk of another team's instance | `StopInstances`+`DetachVolume`+`AttachVolume` to a caller-owned instance | SAM hive / DPAPI read offline without ever touching RDP/SSM/GetPasswordData → **EBS lateral-movement primitive** |
| **Any customer surface** | **AWS service plane** | EC2Rescue helper fleet identity, SSM/EC2 control plane | **HARD STOP** — none found in docs; any such hit = disclosure |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internet-callable | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:GetPasswordData` | API | Existing | No (Read) | Yes | Return RSA-encrypted admin password | any IAM principal w/ action on instance ARN | **No condition keys in list_ec2.md** (Read-level). Ciphertext never re-encrypted/expired server-side |
| `ssm:StartAutomationExecution` (`AWSSupport-TroubleshootRDP`) | API | Existing | Yes | Yes | Read/modify RDP port, NLA, firewall, RDP service | principals w/ action on the document ARN | `Action=FixAll` disables firewall + enables RDP + disables NLA in one call. Works on **non-SSM-managed** instances via offline helper |
| `ssm:StartAutomationExecution` (`AWSSupport-ExecuteEC2Rescue`) | API | Existing | Yes | Yes | Stop instance, offline volume surgery, create AMI, upload logs to S3 | same | `LogDestination` = caller-chosen S3 bucket; creates **persistent** backup AMI |
| `ssm:StartAutomationExecution` (`AWSSupport-ResetAccess` / ec2reset) | API | Existing | Yes | Yes | Reset local admin password / regenerate SSH key | same | **AWS-published sample IAM policy** uses `Resource:"*"` + `iam:PassRole` → see Lead R1 |
| `ec2:StopInstances` / `DetachVolume` / `AttachVolume` | API | Existing | Yes | Yes | Manual detach-root-volume → attach-to-temp-instance | principal w/ action on instance+volume | Underpins both the registry-edit and password-reset manual runbooks |
| `ec2:CreateImage` | API | Existing | Yes | Yes | Backup AMI | principal w/ action | Orphaned AMI retains another instance's disk |
| `ec2:ModifyInstanceAttribute` | API | Existing | Yes | Yes | (adjacent) edit userData/launch spec | principal w/ action | Noted as a PassRole-adjacent primitive (Variant coverage B/E) — not on this page but in the same instance-admin blast radius |
| Manual registry edit (`regedit` on mounted hive) | OS | Existing | Yes | No (operator) | Set `fDenyTSConnections=0`, `EnableFirewall=0` | operator w/ EBS access | Security **downgrade**; done offline, no SSM/RDP needed |

Non-SDK / under-tested knob to probe: whether `ssm:StartAutomationExecution` honours **resource-level conditions on the target `InstanceId`** (vs. only on the document ARN). If not, document-level scope = account-wide instance reach.

---

## 5. Recommended Areas of Focus
Ordered: (1) AWS-authored artifact defects (in-scope Tier 2) → (2) AWS-owned storage/KMS defaults → (3) documented-guarantee gaps → (4) customer-config footguns (hardening notes).

### Area 1 — AWS-published sample IAM policy for AWSSupport-ResetAccess  **[IN-SCOPE / Tier 2]**  — Lens R/S
**Background.** `automation-ec2reset` ships a copy-verbatim sample IAM policy for the reset-password runbook. Subagent review reports it grants `iam:PassRole` scoped to `arn:aws:iam::{account}:role/AWSSupport-EC2Rescue-*` **plus** EC2 VPC/network-build and `ec2:Describe*`/`Create*`/`Delete*` actions on **`Resource:"*"`**, with **no per-instance resource constraint**.
**Security Concern.** A customer who attaches the sample as-is gives every holder the ability to run the reset runbook against **any instance id in the account** — i.e. seize Administrator on every Windows instance — and, via the `iam:PassRole` + role-name-prefix pairing, a classic PassRole self-escalation path if the `AWSSupport-EC2Rescue-*` role is over-scoped. Because the weak default is **AWS-authored and copied verbatim**, it is AWS's defect, not a customer footgun (skill carve-out).
**High-level Test Scenarios (falsifiable):**
- *Claim:* the sample policy authorizes reset of an instance the holder does not own → *Oracle:* `iam:SimulateCustomPolicy` with the printed JSON against `ssm:StartAutomationExecution` on a foreign `InstanceId` returns **allow** (no `Resource`/`Condition` denies it). Confirm no instance-ARN/tag scoping in the printed statements.
- *Claim:* a holder of only this policy escalates to the EC2Rescue role's permissions → *Oracle:* `iam:SimulatePrincipalPolicy` shows `iam:PassRole` succeeds and the target role's attached policy exceeds the holder's.
**Doc evidence:** `automation-ec2reset` IAM policy block (`iam:PassRole` on `AWSSupport-EC2Rescue-*`, `Resource:"*"` for EC2 actions). **Severity-if-true:** non-admin→admin / account-wide instance seizure = **High**. **Stop:** once the simulate shows allow-on-foreign-resource, the artifact defect is established; do not run a live reset.

### Area 2 — Reset SSH key at a predictable Parameter Store path under default KMS  **[IN-SCOPE — shared owner-to-fix]**  — Lens T
**Background.** For Linux targets of the ec2reset runbook, the regenerated SSH **private key** is stored, encrypted, at **`/ec2rl/openssh/{instanceId}/key`** (SecureString). The path is deterministic from a public instance id and the parameter **persists** after the run.
**Security Concern.** If the SecureString uses the **default `alias/aws/ssm` managed key** (AWS-owned default) rather than a per-run CMK, any principal with `ssm:GetParameter` on `/ec2rl/openssh/*` + `kms:Decrypt` on the default key can retrieve **any** instance's SSH key by enumerating instance ids — bypassing the EC2 instance-ownership wall. Unlike the Windows path (ciphertext + separate private key split), here Parameter Store holds the **whole** secret.
**High-level Test Scenarios:**
- *Claim:* the parameter is encrypted under the shared default SSM key, not a scoped CMK → *Oracle:* read the runbook/parameter KMS config; confirm KeyId resolves to `alias/aws/ssm`. (doc-gap — confirm surface first.)
- *Claim:* a principal denied EC2 on instance B still reads B's key via SSM → *Oracle:* under a scoped role (deny `ec2:*` on B, allow `ssm:GetParameter`+default-key decrypt), `GetParameter /ec2rl/openssh/{B}/key` returns cleartext.
- *Claim:* the key outlives the run (no cleanup) → *Oracle:* parameter still present after automation `Success`.
**Doc evidence:** `automation-ec2reset` — "the new SSH private key … is saved, encrypted, in Parameter Store. The parameter name is `/ec2rl/openssh/{{instance ID}}/key`." **Severity-if-true:** **Critical** (direct SSH credential disclosure across an IAM wall). **Stop:** one cross-role read with canary data proves it; do not enumerate real keys.

### Area 3 — "Upload logs to a bucket in your account" is advisory, not enforced  **[IN-SCOPE — guarantee gap]**  — Lens U/B/T
**Background.** `AWSSupport-ExecuteEC2Rescue` `LogDestination` (and nested `S3BucketName`) uploads instance OS logs via `s3:PutObject` under the AutomationAssumeRole. Docs say "an S3 bucket **in your account**" and warn the customer to set a tight bucket policy — a prose instruction, not a service check.
**Security Concern.** No documented step (`aws:assertAwsResourceProperty` only checks instance/volume properties) asserts the bucket is same-account. If the assume-role's `s3:PutObject` isn't bucket-pinned, the automation becomes a **conduit to move another instance's OS logs (event logs, memory dumps) to an attacker-chosen cross-account bucket**, or to redirect logs away from the owner's visibility.
**High-level Test Scenarios:**
- *Claim:* `LogDestination` accepts a cross-account bucket → *Oracle:* run with a canary bucket in a second account whose policy allows the role ARN; a `PutObject` lands there and the runbook does not reject the ARN on a same-account assertion.
- *Claim:* the guarantee has no enforcing mechanism → *Oracle:* grep the runbook step list for any `aws:ResourceAccount` / same-account check on the bucket — absence = advisory-only.
**Doc evidence:** `automation-ec2rescue` `LogDestination` description + bucket-policy warning. **Severity-if-true:** **High** when chained with Area 5 (broad `StartAutomationExecution`): a "help a stuck instance" grant becomes an OS-log exfil primitive. **Stop:** one canary PutObject to a controlled cross-account bucket proves the gap.

### Area 4 — GetPasswordData ciphertext: broad exposure + no server-side expiry  — Lens A/C/M/T  **[CUSTOMER-CONFIG, with a Tier-2 logging sub-lead]**
**Background.** `ec2:GetPasswordData` is **Read-level with no condition keys** (confirmed in `list_ec2.md`). It returns the admin password ciphertext for a running instance. Decryption is purely client-side with the private key; AWS keeps no secondary secret and never re-encrypts or expires the ciphertext.
**Security Concern.** (a) The action is often bundled into broad read-only/power-user policies on the assumption "it's just encrypted," letting a non-owning in-account principal pull ciphertext (need-to-know break, enumeration via non-secret instance ids). (b) **Stale-ciphertext-never-dies:** a ciphertext captured months ago (CLI history, CloudTrail event body, build log) + any retained copy of the original private key = a live admin credential, even after the customer *believes* they rotated. (c) **Logging sub-lead [Tier-2 candidate]:** docs are silent on whether `passwordData` is redacted in CloudTrail (contrast Secrets Manager's documented masking) — if unredacted by default, a CloudTrail-bucket compromise becomes an admin-credential path.
**High-level Test Scenarios:**
- *Claim:* GetPasswordData has no ownership/need-to-know gate beyond the instance-ARN action → *Oracle:* IAM reference shows no condition keys (confirmed); a scoped role with only `ec2:GetPasswordData` on `*` returns ciphertext for a foreign-team instance.
- *Claim:* replacing the key pair does not re-encrypt old ciphertext → *Oracle:* `ResettingAdminPassword_EC2Launchv2` wording on password-vs-key regeneration; old blob still decrypts with original key.
- *Claim:* `passwordData` appears unredacted in CloudTrail → *Oracle:* CloudTrail ec2 event reference search for redaction language; absence ⇒ doc-gap, confirm against a real event body.
**Doc evidence:** `API_GetPasswordData`; `list_ec2.md` GetPasswordData (Read, no condition keys); `ResettingAdminPassword`. **Severity-if-true:** ciphertext exposure alone = **Medium**; the CloudTrail-redaction gap, if AWS-side, = **High** and reportable.

### Area 5 — SSM Automation document as a privilege-escalation vector (firewall/NLA/RDP downgrade; account-wide reach)  — Lens E/A  **[CUSTOMER-CONFIG]**
**Background.** `AWSSupport-TroubleshootRDP Action=FixAll` disables all Windows Firewall profiles, disables NLA, force-enables RDP (`fDenyTSConnections→0`), and resets the port to 3389 — in one call. The OS-level `ssm:SendCommand`/RunPowerShell may execute under the **AutomationAssumeRole**, not the caller.
**Security Concern.** A principal with only `ssm:StartAutomationExecution` on the *document* (no `ssm:SendCommand`, no RDP creds) could weaken an instance's OS security posture it otherwise can't touch — and, if `StartAutomationExecution` is scoped only to the document ARN with no `InstanceId` condition, do so against **every** instance in the account.
**High-level Test Scenarios:**
- *Claim:* document-level grant alone (no instance-level SendCommand) achieves firewall-off/RDP-on → *Oracle:* under a role with `ssm:StartAutomationExecution` on only the TroubleshootRDP document ARN, `FixAll` succeeds and the target's firewall/NLA/RDP state changes.
- *Claim:* no per-instance scoping ⇒ account-wide → *Oracle:* confirm SSM supports (and the sample omits) a `Resource`/`Condition` on target `InstanceId` for the start action.
**Doc evidence:** `automation-awssupport-troubleshootrdp` `Action=FixAll`; "Required IAM permissions" list with no resource/condition scoping. **Severity-if-true:** **High** (narrow grant → broad OS security-control change). **Note:** in-scope *only* if the enabling policy is an AWS-published sample; otherwise a customer-config hardening note.

### Area 6 — EBS root-volume detach/attach as an offline data-at-rest primitive  — Lens A/T  **[CUSTOMER-CONFIG]**
**Background.** Both the registry-enable-RDP workflow and the password-reset workflow instruct: **stop the instance, detach its root volume, attach it to another ("reachable"/"temporary") instance**, then read/modify the filesystem and registry (`EnableFirewall=0`, `fDenyTSConnections=0`, delete `.run-once`).
**Security Concern.** This is a documented, legitimate operator primitive that is *also* a lateral-movement path: a principal holding only `ec2:StopInstances`+`DetachVolume`+`AttachVolume` on a victim's instance/volume can mount the **entire disk** (SAM hive → offline hash crack, DPAPI secrets, stored creds) on an instance it controls — **without** RDP, SSM, or `GetPasswordData`. Account-scoped, so cross-team-within-account, not cross-account.
**High-level Test Scenarios:**
- *Claim:* AttachVolume/DetachVolume are not jointly ownership-conditioned so a caller can move a foreign volume onto its own instance → *Oracle:* `list_ec2.md` shows AttachVolume/DetachVolume support resource-level perms on both volume and instance; confirm a policy granting them on `*` (or on the attacker's instance + victim's volume) is accepted.
- *Claim:* offline registry edit disables the firewall with no audit on the (stopped) target → *Oracle:* the mutation happens on the helper instance; the target produces no OS log of the change (overlaps Lens O).
**Doc evidence:** target page "Enable Remote Desktop … with remote registry" + `ResettingAdminPassword_EC2Launchv2` steps 2–3. **Severity-if-true:** **High** intra-account lateral movement; this is the sharpest *customer-config* footgun on the page.

### Area 7 — Orphaned backup AMI retains another workload's disk  — Lens L/AA  **[CUSTOMER-CONFIG]**
**Background.** ExecuteEC2Rescue/StartEC2RescueWorkflow create a backup AMI (`AWSSupport-EC2Rescue:{instanceId}`) that is **not auto-cleaned** ("this AMI remains in your account … your responsibility to secure or delete it").
**Security Concern.** A non-owning caller who can trigger the runbook (Area 5) can leave a persistent, discoverable (`ec2:DescribeImages`) full-disk image of another team's instance in the shared account, with no lifecycle control. No cross-account vector in docs.
**Oracle:** confirm no deregister/expiry step in the runbook step list; confirm the naming convention makes it enumerable. **Severity-if-true:** **Medium** (within-account durable disk copy).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Account-wide instance seizure via copied sample reset policy | ec2reset sample IAM policy | "sample policy" prose; `iam:PassRole` scoped to role-name prefix only, EC2 on `Resource:"*"` |
| Cross-IAM SSH-key read from Parameter Store | `/ec2rl/openssh/{id}/key` SecureString | "saved, encrypted, in Parameter Store" — relies on KMS key policy + `ssm:GetParameter` scoping |
| Cross-account OS-log exfil via LogDestination | ExecuteEC2Rescue S3 upload | prose "a bucket in your account" + bucket-policy warning (no service assertion) |
| Admin-credential path from stale ciphertext + leaked key | GetPasswordData | client-side decryption; no server-side expiry/rotation of ciphertext |
| Firewall/NLA/RDP downgrade from a document-only grant | TroubleshootRDP `FixAll` | "Required IAM permissions" list (no instance-level scoping shown) |
| Offline SAM/DPAPI read via volume detach/attach | EBS root volume | AttachVolume/DetachVolume resource-level IAM (customer-authored) |
| Durable foreign-disk AMI left in account | EC2Rescue backup AMI | "your responsibility to secure or delete it" |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Customer-authored IAM over-grants** (broad `ssm:StartAutomationExecution`, un-pinned AttachVolume/DetachVolume, bundling `GetPasswordData` into power-user) — a footgun the customer inflicts on themselves; **report as hardening, not a bug.** Exception: the **AWS-published** ec2reset sample policy (Area 1) and any AWS-managed policy are **in scope**.
- **Cross-account instance targeting** — SSM Automation and EC2/EBS are account+region scoped; no documented cross-account path. Do not chase one.
- **IMDS on these managed Windows hosts** — out of scope per skill.
- **Single-tenant self-DoS** (stopping your own instance, instance-store data loss on EC2Rescue, public-IP change) — product behaviour, not a security boundary.
- **AWS service-plane / EC2Rescue helper-fleet identity** — **HARD STOP + disclosure**, never exploit. No reach to it found in docs.
- **The RDP client / Windows OS internals** (NLA, TermService, Microsoft RDP app, mstsc `/admin`) — third-party/OS surface, not AWS's.

---

## 8. Null hypotheses / doc gaps
- **Lens F/K (injection / LLM):** N/A — read the full target page + reset pages + runbook pages; no translation layer, parser, or LLM/agent in these flows. Null hypothesis.
- **Lens G (SSRF):** N/A for the *target page* — no field the service dereferences from a URL. Checked target + reset pages. (`LogDestination` is an S3 bucket name, not a fetched URL → routed to Lens T/B instead.)
- **Lens V/D (network segmentation / control-plane):** N/A — all offline-volume work happens inside the customer VPC on a customer-owned helper instance; no control-ENI/storage-ENI exposure documented.
- **Lens W/H (attestation / KMS context):** N/A on this page; KMS appears only via the default-key question in Area 2 (routed to Lens T).
- **Doc-gaps to confirm *surface first* before hunting:**
  1. Does `ssm:StartAutomationExecution` support a resource-level condition on the **target InstanceId** (Areas 1, 5)? — decides "account-wide" vs "scoped".
  2. KMS key for `/ec2rl/openssh/{id}/key` — default `alias/aws/ssm` or per-run CMK (Area 2)?
  3. CloudTrail redaction of `passwordData` (Area 4c)?
  4. Does the AutomationAssumeRole's `s3:PutObject` get bucket-pinned, and is there any same-account assertion on `LogDestination` (Area 3)?
  5. EC2Launch v2/EC2Config password-generation entropy (Lens EE) — undocumented at public-doc level; confirm via agent source before treating predictability as a lead.

---
*Generated with the `security-questionbuilder` skill. Documentation-only; no live account was contacted. All leads terminate inside the customer account — no AWS service-plane reach was identified in the source docs.*
