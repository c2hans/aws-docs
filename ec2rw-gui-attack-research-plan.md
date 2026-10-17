# EC2Rescue for Windows Server — Attack Research Plan

Source of leads: AWS EC2 User Guide pages `ec2rw-gui.html` (primary target), `ec2rw-cli.html`, `ec2rw-ssm.html`, `Windows-Server-EC2Rescue.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`); SSM Automation runbook pages `automation-awssupport-executeec2rescue.html`, `automation-awssupport-startec2rescueworkflow.html`, `systems-manager/latest/userguide/automation-ec2rescue.html`; AWS managed policy `AmazonSSMAutomationRole`; SSM & EC2 Service Authorization References (`list_ssm.md`, `list_ec2.md`). **Status: documentation-derived hypotheses only; nothing has been tested against a live account.**

> ⚠️ This plan analyzes a **customer-run operational tool** and its SSM automation wrappers, not a classic multi-tenant AWS service. The boundaries here are **intra-account privilege / trust-zone** crossings (SSM-caller → host-Administrator; compromised-volume → clean rescue host; instance-role → Parameter-Store/S3 credential sink; non-admin IAM principal → account admin via an AWS-authored policy) plus **cross-account** reach on the S3-log/OfflineScript egress and KMS-key input paths. The classic AWS **service-plane hard stop** still applies: the moment evidence shows an AWS-owned fleet identity/credential (e.g. the EC2Rescue S3 distribution bucket's backing identity, or an AWS-managed Support role acting outside its documented scope), stop, preserve evidence, and disclose.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity → Stop condition.** Work in priority order (Section 5 is ordered, highest-impact first). Look left and right for adjacent bugs the plan did not anticipate.
- **Safe-first oracles:** prefer `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` (touches no resources) to settle the IAM-artifact leads before any live call. For live confirmation use a **scoped role holding exactly the artifact under test**, never an over-privileged tester, and synthetic/canary data only.
- **HARD STOP:** any identity/credential/ARN/account belonging to AWS's own service plane → stop, preserve, route AWS-Security.
- **Owner-to-fix governs scope:** a weak default in an **AWS-authored, copy-verbatim IAM policy / managed policy / SSM document** is in scope and reportable (Tier 2, `aws-security`). A least-privilege mistake the *customer* authors in their own policy is out of scope.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. As a non-admin principal holding **only the AWS-published "least-privilege" EC2Rescue IAM policy** (`automation-ec2rescue.html`), escalate to **full account admin** via its `iam:CreateRole`+`iam:PutRolePolicy`+`iam:PassRole`+`lambda:CreateFunction/InvokeFunction` grants.
2. Supply a crafted **`OfflineScript`** to `AWSSupport-StartEC2RescueWorkflow` that reads the mounted offline **SAM/SYSTEM/SECURITY** hives (`EC2RESCUE_OFFLINE_REGISTRY_DIR`) of a **victim instance you targeted by id** and exfiltrates them to **your own S3 bucket** — SYSTEM-level credential theft from any instance's root volume.
3. From **`ssm:SendCommand`** on `AWSSupport-RunEC2RescueForWindowsTool` + a parameter read, reset and read the local-Administrator password → interactive host admin on an instance you had no OS rights to.
4. Read **another instance's** generated Administrator password from Parameter Store at `/EC2Rescue/Password[s]/<INSTANCE_ID>` holding only `ssm:GetParametersByPath` on `/EC2Rescue/*` and **no** `kms:Decrypt` (ViaService wall bypass); confirm it survives instance termination (stale secret).
5. Direct **credential-bearing collected logs** (memory dumps + registry hives) to an **attacker/cross-account S3 bucket** via the caller-supplied bucket name (confused deputy).
6. Start the automation against an **instance you do not own** (no tag/ownership check) and mount its root volume to a helper you control.
7. Achieve **code execution / file write on a clean rescue host** via EC2Rescue's offline parser or a `regback` **reparse-point escape** that writes onto the helper's own `C:\` — lateral movement from a compromised instance to the healthy helper.
8. Recover a full disk image from the **persistent, unencrypted, predictably-named backup AMI** (`AWSSupport-EC2Rescue:<InstanceId>`) left behind by the automation.
9. Pass a role you don't own / omit `AutomationAssumeRole`; audit the AWS-recommended `AmazonSSMAutomationRole` (`ssm:*` on `*`) blast radius.

---

## 2. Components, Assets, and Design

**What it is.** EC2Rescue for Windows Server is a downloadable Windows tool (`EC2RescueCmd.exe` + GUI) that diagnoses/repairs Windows Server EC2 instances. **Data-collector module** + **analyzer module** ("parses the data collected against a series of predefined rules" — `Windows-Server-EC2Rescue.html`). Two modes (`ec2rw-cli.html`):
- **`/online`** — acts on the instance EC2Rescue runs on (collect logs; reset admin pw).
- **`/offline:<device_id>`** — acts on an EBS **root volume detached from an impaired instance and re-attached to a separate healthy Windows instance**.

**Four invocation surfaces (increasing AWS exposure):**
1. **Local GUI / CLI** — operator runs it directly.
2. **SSM Run Command** doc `AWSSupport-RunEC2RescueForWindowsTool` — runs under the **target instance's role**. Commands `ResetAccess` / `CollectLogs` / `FixAll` (`ec2rw-ssm.html`).
3. **SSM Automation** `AWSSupport-ExecuteEC2Rescue` — orchestrates stop → create backup AMI → detach root → attach-to-helper → offline rescue → reattach, under an **AutomationAssumeRole**.
4. **SSM Automation** `AWSSupport-StartEC2RescueWorkflow` — the lower-level runbook `ExecuteEC2Rescue` defers to; **runs a caller-provided base64 Bash/PowerShell `OfflineScript`** on a helper with the victim's root volume mounted, exposing env vars `EC2RESCUE_OFFLINE_REGISTRY_DIR` (e.g. `D:\Windows\System32\config` → SAM/SYSTEM/SECURITY/SOFTWARE) and `EC2RESCUE_OFFLINE_CURRENT_CONTROL_SET`.

**Distribution / supply chain.** GUI/CLI fetch from `https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip?x-download-source=docs` over plain `s3.amazonaws.com`, **no documented checksum/signature** (contrast the Linux sibling `ec2rl_install.html`, which documents `sha256sum -c` + GnuPG signature verification, and `ec2rw-ssm.html` which says the Run Command doc "Downloads and **verifies**"). A note says TLS 1.2 may need manual enabling on Server 2016- → default negotiated TLS floor on that path can be < 1.2. The filename `EC2Rescue_latest.zip` is unversioned, so no fixed hash can ever be pinned.

**Sensitive assets.**
- **Generated local-Administrator password** → **SSM Parameter Store** `/EC2Rescue/Password/<INSTANCE_ID>` (prose) / `parameter/EC2Rescue/Passwords/<instanceid>` (IAM sample — **note the singular/plural mismatch**). Deterministic path keyed on the public instance-id. Encrypted with default `alias/aws/ssm` or a caller-supplied key.
- **Collected logs** → ZIP of **SYSTEM/SOFTWARE/BCD registry hives, `HKLM\BCD00000000`, memory-dump files, SSM-agent/Patch logs** (= LSA secrets, cached creds, DPAPI). Uploaded (`CollectLogs` / `S3BucketName`) to a **caller-supplied bucket**.
- **Offline mounted hives** reachable to `OfflineScript` incl. **SAM** (local password hashes).
- **Backup AMI** `AWSSupport-EC2Rescue:<UnreachableInstanceId>` — "remains in your account", **unencrypted** (automation hard-asserts the root volume is not encrypted), predictably named, never auto-deleted.
- **The impaired EBS volume** itself — untrusted content parsed by a tool running as admin/SYSTEM on a *clean* host.

**Identity.** No service-specific identity; everything runs under existing IAM: instance profile (Run Command), AutomationAssumeRole (runbooks; **defaults to the caller's own identity if omitted**), or operator console/CLI.

```
 operator / SSM caller ─ssm:SendCommand─▶ AWSSupport-RunEC2RescueForWindowsTool  (runs as TARGET instance role)
   ├─ ResetAccess ─▶ reset local Admin pw ─ssm:PutParameter▶ /EC2Rescue/Password/<id>  (KMS alias/aws/ssm)  ──read via GetParametersByPath + ViaService──▶ cleartext pw
   ├─ CollectLogs ─▶ /collect:all ─▶ S3 bucket (CALLER-SUPPLIED name)   [ZIP = registry hives + memory dumps = CREDS]
   └─ FixAll     ─▶ /rescue:all on device (CALLER-SUPPLIED)

 StartAutomationExecution ─▶ AWSSupport-ExecuteEC2Rescue ─▶ AWSSupport-StartEC2RescueWorkflow  (AutomationAssumeRole, or CALLER identity if omitted)
   stop(UnreachableInstanceId) ─▶ CreateImage (backup AMI, UNENCRYPTED, persists) ─▶ detach root vol ─▶ attach to HELPER (caller-influenced VPC)
       ─▶ run CALLER-SUPPLIED OfflineScript  [env EC2RESCUE_OFFLINE_REGISTRY_DIR → SAM/SYSTEM/SECURITY]  ─▶ upload to S3BucketName
   analyzer parses attacker-controlled registry/BCD/eventlog/memory-dump;  disk-signature OVERWRITE from BCD (default, even /check-only)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Non-admin holding the AWS-published EC2Rescue "least-privilege" policy | Full account admin | `iam:CreateRole`+`PutRolePolicy`+`PassRole`+`lambda:*` on `AWSSupport-EC2Rescue-*` | A principal with only that policy performs an admin-only action → privesc = breach of the artifact's own "scoped" claim |
| Automation caller | Victim instance's **SAM/SYSTEM/SECURITY** hives | caller-supplied `OfflineScript` runs on helper with victim root vol mounted + `EC2RESCUE_OFFLINE_REGISTRY_DIR` | Hashes/LSA secrets of an instance the caller had no OS access to land in attacker egress = SYSTEM credential theft |
| SSM caller holding only `ssm:SendCommand` | Local Windows **Administrator** on the target | `ResetAccess` resets pw, caller reads the parameter | Caller with no OS/RDP rights obtains the Administrator password → admin logon |
| Principal with `ssm:GetParametersByPath` on `/EC2Rescue/*`, not the reset right | Another instance's Admin password | deterministic path + `alias/aws/ssm` decrypts via `kms:ViaService` | Cleartext pw read for an instance-id you don't control, with no `kms:Decrypt` in your policy |
| Target instance role / automation role | Caller-supplied S3 bucket (cross-account) | `CollectLogs` / `S3BucketName` upload of hives+dumps | Credential-bearing logs landing in a non-owner bucket = exfil / confused deputy |
| Automation caller | Any instance / any EBS root volume | runbook stops instance, detaches/attaches by supplied id, no tag/ownership check documented | Stopping/mounting an instance's root volume the caller otherwise can't touch |
| Compromised/attacker-owned impaired volume | Clean rescue/helper host (admin/SYSTEM) | offline parser/analyzer; `regback` restore from a path on that volume | Code exec, OOB/UAF, or a write landing on the helper's own `C:\` = lateral movement |
| Attacker-controlled BCD disk signature | Rescue host disk subsystem | signature overwrite from BCD, default even under `/check-only` | A write under `/check-only`, or a signature collision affecting the helper's boot disk |
| Any customer surface | **AWS service plane** (EC2Rescue S3 bucket backing identity; AWS-managed Support role) | tool download; AWS-owned automation | **Any AWS-owned fleet identity/credential = HARD STOP, preserve + disclose** |

---

## 4. API / Interface Inventory

| Name | New/Existing | Mutating? | Internal/External | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `EC2RescueCmd /offline:<dev> /collect` | Existing | sets vol offline | Local | Collect from untrusted vol | No | Local admin on helper | Parses untrusted volume |
| `EC2RescueCmd /offline:<dev> /rescue:<grp>` | Existing | **Yes** | Local | Fix firewall/RDP/EC2Config/pw | No | Local admin | `/check-only` still fixes disk sig |
| `EC2RescueCmd /offline:<dev> /restore:regback` | Existing | **Yes** | Local | Restore registry from `\Windows\System32\config\RegBack` on untrusted vol | No | Local admin | reparse-point escape target |
| `rescue ec2config.Ec2HandleUserData` | Existing | **Yes** | Local | Arm user-data script on next boot | No | Local admin | persistence primitive |
| `rescue …Ec2SetPassword` / `ec2launch Reset Admin Pw` | Existing | **Yes** | Local | Generate Admin pw on target vol | No | Local admin | local path documents no secure storage |
| `ssm:SendCommand → AWSSupport-RunEC2RescueForWindowsTool ResetAccess` | Existing | **Yes** | External (SSM) | Reset Admin pw, store in Param Store | Yes | anyone w/ SendCommand on doc+instance | scopable by `document`/`instance`+`ssm:resourceTag`, default-broad |
| `…CollectLogs` | Existing | Yes (S3) | External | `/collect:all` ZIP → caller bucket | Yes | SendCommand holders | bucket name = caller input |
| `…FixAll` | Existing | **Yes** | External | `/rescue:all` on caller device | Yes | SendCommand holders | |
| `AWSSupport-ExecuteEC2Rescue` | Existing | **Yes** | External | Orchestrated offline rescue + backup AMI | Yes | automation caller + AutomationAssumeRole | defers perms to StartEC2RescueWorkflow |
| `AWSSupport-StartEC2RescueWorkflow` | Existing | **Yes** | External | Runs **caller `OfflineScript`** on helper w/ victim vol mounted | Yes | automation caller | `S3BucketName`, `OfflineScript`, backup-AMI params; env → SAM hive |
| `ssm:GetParameter(sByPath) /EC2Rescue/*` | Existing | No | External | Read stored Admin pw | Yes | any parameter-read holder | secret-wall-bypass target; `ssm:Recursive` optional |
| `ec2:DescribeImages Name=AWSSupport-EC2Rescue:*` | Existing | No | External | Enumerate persistent backup AMIs | Yes | any `Describe*` holder | unencrypted full-disk image |

**Undocumented/under-surfaced knobs:** pull the JSON of both SSM documents (`ssm:GetDocument` / console Content tab) and enumerate every parameter beyond the prose-documented `Command`/`Parameters`/`OfflineScript`/`S3BucketName` — look for helper instance type/subnet/VPC, arbitrary volume id, KMS key id, bucket prefix, and anything that weakens isolation. The prose understates the real parameter model.

---

## 5. Recommended Areas of Focus

> Priority (highest impact first): A1 OfflineScript credential theft → A2 AWS-authored IAM privesc chain → A3 SSM→host-admin → A4 Param-Store secret-wall → A5 CollectLogs/S3 exfil → A6 arbitrary-instance targeting + `AmazonSSMAutomationRole` over-grant → A7 persistent unencrypted backup AMI → A8 sample PutParameter policy + unconditioned `kms:Encrypt` → A9 offline-volume parser / regback escape → A10 `/check-only` disk-sig write & BCD collision → A11 supply-chain download → A12 misc (EC2-check spoof, Ec2HandleUserData persistence, local pw asymmetry).

### A1 — `OfflineScript`: SYSTEM credential theft from any instance's root volume (Lens K-adjacent / F / A) — **Critical**
**Background.** `AWSSupport-StartEC2RescueWorkflow` "runs the provided base64 encoded script (Bash or Powershell) on a helper instance created to rescue your instance. The root volume of your instance is attached and mounted"; it exposes `EC2RESCUE_OFFLINE_REGISTRY_DIR` ("Offline Windows registry directory path", e.g. `D:\Windows\System32\config`) and `EC2RESCUE_OFFLINE_CURRENT_CONTROL_SET` (`automation-awssupport-startec2rescueworkflow.html`). `ExecuteEC2Rescue` defers to this runbook.
**Security Concern.** The runbook's core primitive is "run my arbitrary script with SYSTEM-equivalent access to a root volume + a documented path to its SAM/SYSTEM/SECURITY hives." Combined with a caller-chosen target instance (A6) and a caller-chosen `S3BucketName` (A5), this is a structural, documented path to dump local password hashes, LSA secrets, cached domain credentials, and DPAPI master keys from a volume the caller otherwise cannot read.
**Test Scenarios.**
- Claim: an `OfflineScript` can copy `$env:EC2RESCUE_OFFLINE_REGISTRY_DIR\SAM`,`SYSTEM`,`SECURITY` and exfiltrate via `S3BucketName`, with no content/destination control blocking it. → Oracle: run with such a script; the hives arrive in the attacker bucket; confirm no DLP/destination check exists.
- Claim: the helper VPC/subnet is caller-influenced, giving arbitrary egress for exfil. → Oracle: helper reaches a non-allowlisted internet host.
**Doc evidence.** `automation-awssupport-startec2rescueworkflow.html` OfflineScript + env var descriptions. **Severity:** Critical (operationalizes credential material to attacker-chosen output using AWS's own mechanism). *Chains with A6 (arbitrary target) → cross-boundary; and A5 (bucket) → cross-account egress.*

### A2 — AWS-published "least-privilege" EC2Rescue IAM policy = privesc chain (Lens R / S / B) — **Critical**
**Background.** `automation-ec2rescue.html` ("IAM Policy for AWSSupport-EC2Rescue") grants, on `role/AWSSupport-EC2Rescue-*`: `iam:CreateRole`, `iam:CreateInstanceProfile`, `iam:PutRolePolicy`, `iam:AttachRolePolicy`, `iam:PassRole`, `iam:AddRoleToInstanceProfile`, plus `lambda:CreateFunction`/`lambda:InvokeFunction` on `function:AWSSupport-EC2Rescue-*`, and EC2 networking on `Resource:*`. The page also says you "must also attach the **`AmazonSSMAutomationRole`**" managed policy, whose JSON (`AmazonSSMAutomationRole.md`) contains `{"Action":["ssm:*"],"Resource":["*"]}` plus `ec2:Stop/Start/Run/TerminateInstances`,`CreateImage` on `*`.
**Security Concern.** The document AWS presents as the *scoped, non-admin* alternative is a textbook privilege-escalation primitive, and the required companion managed policy is SSM-wide admin. Both are AWS-authored, copy-verbatim artifacts (in scope, Tier 2).
**Test Scenarios.**
- Claim: a principal with **only** the published EC2Rescue policy can reach account admin: `CreateRole AWSSupport-EC2Rescue-x` (lambda trust) → `PutRolePolicy` admin perms → `CreateFunction` with `PassRole` of that role → `InvokeFunction` to run arbitrary API calls as admin. → Oracle: each step succeeds under a scoped role holding only the policy; prefer `iam:SimulatePrincipalPolicy` first, then a canary role.
- Claim: `AmazonSSMAutomationRole` lets the holder `SendCommand`/`PutParameter`/`GetParameter` on unrelated instances/paths. → Oracle: a call unrelated to EC2Rescue succeeds under only that managed policy.
**Doc evidence.** `automation-ec2rescue.html` policy JSON; `AmazonSSMAutomationRole.md` `ssm:*` on `*`. **Severity:** Critical (non-admin → admin via an AWS-authored "least-privilege" policy). Report `aws-security`.

### A3 — SSM command access → local-Administrator escalation (Lens E / X) — **High→Critical**
**Background.** `ResetAccess` "Resets the local Administrator password … stored in Parameter Store as `/EC2Rescue/Password/<INSTANCE_ID>`"; the example notes the retrieved password is used to "RDP … as the local Administrator" (`ec2rw-ssm.html`). Runs under the instance role; caller needs only `ssm:SendCommand` (scopable by `instance`/`document` + `ssm:resourceTag` — `list_ssm.md` ~914-915 — but not enforced).
**Security Concern.** Broad `ssm:SendCommand` (common ops grant) + a parameter read turns "can run commands" into interactive host admin on any SSM-managed Windows instance.
**Test Scenarios.**
- Claim: a role with only `ssm:SendCommand` on this document (+ `instance/*`) and `ssm:GetParameter` on the path obtains Administrator on an instance it has no OS rights to. → Oracle: ResetAccess + retrieved pw authenticates an RDP/WinRM admin logon. Confirm minimal end-to-end IAM (does `ssm:GetCommandInvocation` ever surface the pw without GetParameter?).
- Claim: SendCommand is invokable against a foreign-team instance-id because it isn't tag-scoped. → Oracle: SendCommand returns a CommandId and the parameter is written.
**Doc evidence.** `ec2rw-ssm.html` ResetAccess. **Severity:** High (Critical on domain controllers / credential-rich hosts).

### A4 — Parameter-Store secret-wall bypass + stale secret (Lens T / A / EE) — **High**
**Background.** Password at a path **deterministic from the public instance-id**, default key `alias/aws/ssm` (`ec2rw-ssm.html`). `ssm:GetParametersByPath` resource type `parameter` has an **optional** `ssm:Recursive` condition (`list_ssm.md`), so a grant on `parameter/EC2Rescue/*` with no `ssm:Recursive=false` can walk the whole namespace. No read-side least-privilege policy is published anywhere (feeds over-broad grants).
**Security Concern.** Origin (PutParameter) and read (GetParameter) sit behind different IAM. A principal denied the reset path but holding `ssm:GetParametersByPath` on `/EC2Rescue/*` reads every stored Administrator password; because the default key is managed `alias/aws/ssm`, decrypt succeeds via the key policy's `kms:ViaService` **without `kms:Decrypt` in the caller's identity policy** — defeating the mitigation an operator would reach for.
**Test Scenarios.**
- Claim: `get-parameters-by-path --path /EC2Rescue/Password/ --recursive --with-decryption` returns plaintext for instance-ids the caller cannot `SendCommand`. → Oracle: cleartext returned under a role with only that read.
- Claim: decrypt succeeds with `kms:Decrypt` omitted/denied in the identity policy. → Oracle: WithDecryption still returns plaintext.
- Claim: the password **outlives** the instance (no cascade delete, no TTL). → Oracle: `get-parameter --name /EC2Rescue/Password/i-<terminated>` still returns.
- Adjacent: `ParameterNotFound` vs `AccessDenied` as a cross-team instance-existence oracle.
**Doc evidence.** `ec2rw-ssm.html` storage + default-key sentences. **Severity:** High (fleet-wide host-admin credential disclosure from read-only SSM access). *Chains with A3: A3 writes the secret, A4 reads it — the full chain is **High trending Critical**.*

### A5 — CollectLogs / `S3BucketName` → credential-log exfil to caller/cross-account bucket (Lens B / EE / Q) — **High→Critical**
**Background.** `CollectLogs`: "`Parameters` must include an Amazon S3 bucket name to upload the logs to" (`ec2rw-ssm.html`); `/collect:all` includes `registry` (SYSTEM/SOFTWARE/BCD) + `memory-dump` (`ec2rw-cli.html`). `StartEC2RescueWorkflow`'s `S3BucketName` warning is advisory only: "Make sure the bucket policy does not grant unnecessary read/write permissions …" — a customer-responsibility note, **no** `s3:ResourceAccount`/expected-bucket-owner check documented.
**Security Concern.** Upload uses the instance/automation role identity but writes to a caller-chosen bucket name with no owner pinning → memory dumps + registry hives land in an attacker-controlled or cross-account bucket (confused deputy / Lens EE predictable-name land-grab).
**Test Scenarios.**
- Claim: a role with broad `s3:PutObject` uploads to a different-account bucket; no owner validation occurs. → Oracle: ZIP appears in the attacker bucket (owner mismatch / `bucket-owner-full-control`).
- Adjacent (Q output side): quantify who can `s3:GetObject` the credential-bearing ZIP once landed.
**Doc evidence.** `ec2rw-ssm.html` CollectLogs; `automation-awssupport-startec2rescueworkflow.html` `S3BucketName`. **Severity:** High → Critical if cross-account.

### A6 — Arbitrary-instance/volume targeting + no-role fallthrough (Lens A / B / V) — **High→Critical**
**Background.** `ExecuteEC2Rescue` param `UnreachableInstanceId` "(Required) ID of your unreachable EC2 instance … Automation stops this instance, and creates an AMI." `StartEC2RescueWorkflow` steps: stop instance → detach root → attach to helper. `AutomationAssumeRole` "(Optional) … If no role is specified, Systems Manager Automation uses the permissions of the **user that starts this runbook**." Policies carry no `aws:ResourceTag`/`ec2:ResourceTag` condition; `AmazonSSMAutomationRole` grants the EC2 actions on `Resource:*`.
**Security Concern.** Any caller who can start the runbook can stop and mount the root volume of **any instance id they supply** in-account; omitting the role runs the whole chain under the caller's own identity (bigger blast radius than the "service acts on your behalf" model implies).
**Test Scenarios.**
- Claim: start the automation against a foreign-team instance-id → it stops it and mounts its root volume on a caller-controlled helper, no extra authz. → Oracle: automation succeeds; attacker helper has the foreign device.
- Claim: with no `AutomationAssumeRole`, CloudTrail attributes stop/detach/OfflineScript to the caller's principal. → Oracle: CloudTrail shows caller identity.
**Doc evidence.** `automation-awssupport-executeec2rescue.html`, `automation-awssupport-startec2rescueworkflow.html`. **Severity:** High–Critical (combined with A1/A5 = cross-boundary credential theft).

### A7 — Persistent, unencrypted, predictably-named backup AMI (Lens A / EE / U) — **High**
**Background.** `automation-ec2rescue.html`: "The runbook creates a backup AMI … All other resources … are automatically deleted, but **this AMI remains in your account**", named `AWSSupport-EC2Rescue:<UnreachableInstanceId>`. A hard precondition step asserts the **root volume is not encrypted**, so the backup is guaranteed unencrypted. `StartEC2RescueWorkflow` `Create*EC2RescueBackup`: "The AMI will persist … It is your responsibility to secure access … or to delete it."
**Security Concern.** Each rescue leaves a standing, enumerable, unencrypted full-disk image (all registry/credential material) that nothing cleans up, discoverable by any principal with `ec2:DescribeImages` (the EC2Rescue policy itself grants `ec2:Describe*` on `*`).
**Test Scenarios.**
- Claim: `DescribeImages Name=AWSSupport-EC2Rescue:*` enumerates the AMIs; backing snapshot `Encrypted:false`; no step deletes them. → Oracle: AMI listed, unencrypted, persists post-run.
**Doc evidence.** `automation-ec2rescue.html` backup-AMI sentences. **Severity:** High (standing unencrypted disk copy, predictable name).

### A8 — AWS-authored write-side sample policy: path mismatch + unconditioned `kms:Encrypt` (Lens R / S / U) — **Medium–High**
**Background.** `ec2rw-ssm.html` prints two sample policies for the instance role. (a) `ssm:PutParameter` on `parameter/EC2Rescue/Passwords/<instanceid>` (**plural**) while prose writes `/EC2Rescue/Password/<id>` (**singular**). (b) adds `kms:Encrypt` on the custom key with **no `Condition`**.
**Security Concern.** (1) If the runtime path is singular, the sample grants PutParameter on a path the tool never writes → `ResetAccess` fails closed → operators broaden to `parameter/EC2Rescue/*` (widening A4's blast radius). (2) Unconditioned `kms:Encrypt` lets the role encrypt arbitrary data under the CMK outside EC2Rescue (no `kms:ViaService`/`EncryptionContext`/`SourceArn`).
**Test Scenarios.**
- Claim: a principal with exactly sample (a) is denied `ssm:PutParameter` on the singular runtime path. → Oracle: `iam:SimulatePrincipalPolicy` → implicitDeny on singular, allow on plural; or CloudTrail `AccessDenied` on a live ResetAccess.
- Claim: sample (b) `kms:Encrypt` is unconditioned → direct `kms:Encrypt(KeyId,…)` outside SSM succeeds. → Oracle: read the JSON (no Condition); live Encrypt succeeds under only that policy.
**Doc evidence.** `ec2rw-ssm.html` two JSON blocks + storage prose. **Severity:** Medium–High; AWS-authored, reportable (Tier 2).

### A9 — Offline-volume parser → clean-host lateral movement; `regback` reparse escape (Lens F / Q / V) — **High→Critical**
**Background.** Offline mode attaches an impaired root volume to a **separate healthy helper**; the **analyzer parses** SYSTEM/SOFTWARE/`BCD00000000` hives, event logs, memory dumps from that volume (`Windows-Server-EC2Rescue.html`, `ec2rw-cli.html`). `restore:regback` restores from `\Windows\System32\config\RegBack` — a path **on the attacker-controlled NTFS**.
**Security Concern.** Untrusted content fed to a privileged parser on a clean multi-purpose host = compromised-instance → rescue-host lateral movement. Parser memory-safety bugs (crafted hive/BCD/EVTX/minidump: bad cell/chunk/stream lengths, deep nesting, bogus offsets) → crash/OOB/UAF as SYSTEM. Path-handling: an NTFS junction/reparse point at `…\config\RegBack` on the mounted volume could redirect the restore source/target **onto the helper's own `C:\`**, overwriting its live registry. Also `/output:<path>` / collected filenames → zip-slip / temp-write outside intended dir.
**Test Scenarios.**
- Claim: a fuzzed SYSTEM/BCD/EVTX/minidump processed offline crashes or corrupts `EC2RescueCmd.exe` running as SYSTEM. → Oracle: crash/OOB under Application Verifier on a crafted volume.
- Claim (highest value): a reparse point at `RegBack` makes `/restore:regback` read/write the **helper's own** registry/system drive. → Oracle: canary-file / timestamp diff shows I/O outside the mounted volume.
**Doc evidence.** `Windows-Server-EC2Rescue.html` analyzer; `ec2rw-cli.html` `restore:regback`, `/output`. **Severity:** High (code exec/lateral movement); **Critical** if the reparse escape overwrites the helper's live registry. *Doc-gap: parser internals & the privilege level EC2RescueCmd runs at offline are undocumented — confirm empirically.*

### A10 — `/check-only` disk-signature write & BCD-driven collision (Lens U / F) — **Medium**
**Background.** "`/check-only` … generates a report but makes no modifications to the offline volume." immediately followed by: it "corrects the signature … **by default, even when you use `/check-only`**. You must use `/no-fix-signature` …" and "attempts to overwrite the disk signature with the signature on BCD" (`ec2rw-cli.html`, `ec2rw-gui.html`).
**Security Concern.** `/check-only` still **writes** — a documented-guarantee-vs-enforcement gap misleading forensic/chain-of-custody users. The written value derives from the **attacker-controlled BCD**; a crafted signature could collide with the **rescue host's own** boot-disk signature (MBR 4-byte sigs are low-entropy, often sequential in cloned AMIs), disrupting the helper's drive-letter assignment/bootability.
**Test Scenarios.**
- Claim: `/rescue:all /check-only` (no `/no-fix-signature`) changes the signature sector. → Oracle: block-level before/after diff; confirm `/no-fix-signature` suppresses it.
- Claim: a BCD signature equal to the helper's own disk signature induces a collision affecting the helper. → Oracle: helper mount/boot anomaly after the run.
**Doc evidence.** `ec2rw-cli.html` `/check-only` + `/no-fix-signature`. **Severity:** Medium (surprising write / single-host DoS).

### A11 — Supply-chain / transport integrity of the download (Lens Y / EE) — **Medium–High**
**Background.** GUI/CLI fetch from `https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip` with a TLS-1.2-manual-enable note on Server 2016- and **no documented checksum/signature** — unlike the Linux sibling's `sha256sum -c` + GnuPG chain (`ec2rl_install.html`) and unlike the SSM path's "Downloads and verifies" (`ec2rw-ssm.html`). Unversioned filename = no pinnable hash.
**Security Concern.** An operator on a possibly-sub-1.2-TLS session with no post-download integrity check is exposed to downgrade/MITM/substituted ZIP, run as admin.
**Test Scenarios.**
- Claim: no runtime integrity verification on the manual path (no sidecar hash, confirm whether the EXE is Authenticode-signed). → Oracle: inspect bucket for a hash file; check Authenticode on the EXE.
- Claim: the `ec2rescue` bucket is AWS-owned / not claimable (rule out Lens EE). → Oracle: confirm ownership; **if any response implicates an AWS-owned backing identity, HARD STOP + disclose.**
**Doc evidence.** download URL + TLS note; "Downloads and verifies"; `ec2rl_install.html` contrast. **Severity:** Medium–High (local admin code exec via tampered tool). *Runtime reality not doc-derivable — flag unconfirmed.*

### A12 — Misc leads (Lens U / chained) — **Low–Medium**
- **EC2-instance check spoofability (Lens U):** "When the tool starts, it checks whether it is running on an Amazon EC2 instance" (`Windows-Server-EC2Rescue.html`) — mechanism undocumented. If it relies on a spoofable signal (IMDS/BIOS asset-tag), the "trusted helper is a genuine EC2 instance" assumption behind A9/A10 weakens. Oracle: identify the check, test spoofing on a non-EC2 host. Low standalone; widens other preconditions.
- **`Ec2HandleUserData` persistence (chained):** `rescue:ec2config.'Ec2HandleUserData'` arms "run a user data script on the next boot" on the target volume. If an attacker independently controls that instance's user-data, this becomes unattended code exec on next boot. Oracle: determine whether it stages an operator script or re-enables the instance's own user-data path. Medium (contingent).
- **Local `Ec2SetPassword` disclosure asymmetry:** the GUI/CLI reset documents no secure storage for the generated password (contrast the SSM path's KMS-encrypted Parameter Store). Oracle: trace where the local plaintext surfaces (console/history/zip/written-back-to-volume) and whether it persists for later volume-read recovery. Medium (doc-asymmetry).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin → account admin via published policy | `automation-ec2rescue.html` IAM policy + `AmazonSSMAutomationRole` | the ARN-prefix scoping / managed-policy claim itself (under test) |
| OfflineScript dumps SAM/SYSTEM/SECURITY to attacker S3 | `AWSSupport-StartEC2RescueWorkflow` | advisory `S3BucketName` warning only |
| SSM caller resets+reads Admin pw of a no-OS-rights instance | `AWSSupport-RunEC2RescueForWindowsTool` ResetAccess | optional `ssm:SendCommand` tag-scoping |
| Read others' Admin pw via `/EC2Rescue/*`, no reset rights | Parameter Store + `alias/aws/ssm` | path-scoped ARN; managed-key `kms:ViaService` (the weakness) |
| Memory dumps/hives exfil to foreign bucket | CollectLogs / `S3BucketName` → S3 | bucket-owner / SourceAccount check (confirm absence) |
| Stop/mount any instance's root volume | `UnreachableInstanceId` targeting | tag/ownership condition (absent in docs) |
| Persistent unencrypted backup AMI harvested | backup AMI `AWSSupport-EC2Rescue:*` | "your responsibility to delete" disclaimer |
| Sample policy fails closed / over-grants kms:Encrypt | AWS-authored JSON `ec2rw-ssm.html` | the ARN/condition scoping (under test) |
| Crafted hive/BCD/dump exploits analyzer; regback reparse escape | offline analyzer / `restore:regback` | "checks it runs on EC2" (not a parser mitigation) |
| `/check-only` writes disk signature | offline rescue | `/no-fix-signature` opt-out (default writes) |
| Tampered tool via no-verify download | GUI/CLI S3 download | TLS floor; SSM path's verify (absent on manual path) |

---

## 7. Out-of-Scope Risk Categories

- **Customer-authored** least-privilege mistakes in the customer's *own* policies — *except* the AWS-authored artifacts in `ec2rw-ssm.html` / `automation-ec2rescue.html` / `AmazonSSMAutomationRole`, which **are** in scope (A2, A8).
- IMDS on these fully-managed/customer-managed Windows hosts.
- A customer running EC2Rescue against their **own** healthy volume (no boundary crossed) — unless it crosses to another instance/account.
- Linux EC2Rescue (`ec2rl`, `Linux-Server-EC2Rescue.html`) and its module-dev surface — sibling tool, worth a **separate plan** (the `ec2rl_moduledev` custom-module path is its own code-exec concern).
- Generic Windows OS / registry / RDP vulnerabilities not introduced by EC2Rescue.
- Single-tenant self-DoS from stopping one's own instance — note but low priority; unless it strands another party's volume.
- Shared SSM/KMS/EC2 backend infrastructure internals (AWS-operated).

---

## 8. Null Hypotheses / Doc Gaps

**Lenses that did not fire (pages checked):**
- **Lens FF (JWT/OIDC/Cognito):** N/A — read all four EC2Rescue pages + both runbook pages; no token verification layer. Null.
- **Lens J (OAuth/3P):** N/A — no third-party OAuth linking. Null.
- **Lens CC / DD / BB (upstream-context, cache-key, canonicalization):** N/A — no authorizer/CDN/edge/caching/HTTP-routing layer; the surface is SSM-API- and host-driven. Null.
- **Lens W (attestation):** N/A — no Nitro/enclave/PCR gating. Null.
- **Lens N (namespace migration):** N/A — no dual-ARN/migration window. Null.
- **Lens Y transport (beyond download):** mostly N/A — no custom `http://` service endpoint; the only transport lead is the tool download (A11).

**Doc gaps — confirm surface before/with testing:**
1. No AWS **read-side** (`GetParameter`) sample/managed policy for `/EC2Rescue/Password/*` exists in the mirror — only the write side is published (drives A4/A8 over-broad reads).
2. `alias/aws/ssm` key-policy text is not reproduced here — A4's `kms:ViaService` claim rests on general managed-key behavior; verify against the live key policy.
3. `AutomationAssumeRole` **trust-policy** requirements (which principal may assume it) are not shown for either runbook.
4. **Cross-account/disabled/pending-deletion KMS key** behavior for the ResetAccess custom-key input is undocumented (silent) — Lens H untested territory; confirm whether a cross-account or disabled key is rejected.
5. No **lifecycle/TTL** statement for `/EC2Rescue/Password/<id>` after instance termination (A4 stale-secret inferred from absence).
6. `AWSSupport-ExecuteEC2Rescue` defers its "Required IAM permissions" to `StartEC2RescueWorkflow` — the two share one permission surface; no tighter `ExecuteEC2Rescue`-layer scoping exists.
7. EC2Rescue **native binary internals**, the privilege level it runs at offline, the parser implementation (custom vs OS-API passthrough), and whether the manual download is integrity-verified at runtime — not in docs; mark "confirm empirically," do not assume.
8. The full **document JSON** parameter models (`ssm:GetDocument`) for both SSM documents — enumerate undocumented knobs (helper type/subnet/VPC, arbitrary volume id, bucket prefix) before testing.
9. Multi-candidate-disk behavior if two attached disks both look like the "offline root volume" — undocumented, adjacent.

---

*Priority kill-chains to run first:*
- **A6 → A1 → A5:** target a foreign instance (`UnreachableInstanceId`), run an `OfflineScript` that reads its mounted `SAM/SYSTEM/SECURITY` hives, exfiltrate to an attacker/cross-account `S3BucketName` → **cross-boundary SYSTEM credential theft; Critical.**
- **A3 → A4:** broad `ssm:SendCommand` resets the Administrator password, broad `/EC2Rescue/*` read + `alias/aws/ssm` ViaService decrypt reads it → fleet-wide Windows-Administrator access from ordinary ops IAM; **High trending Critical** on credential-rich hosts.
- **A2 standalone:** attach only the AWS-published "least-privilege" policy → `CreateRole`/`PutRolePolicy`/`PassRole`/Lambda → **account admin; Critical.**
