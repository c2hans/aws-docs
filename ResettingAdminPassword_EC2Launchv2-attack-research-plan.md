# EC2Launch v2 — Reset Windows Admin Password — Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Launchv2.html`
(mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Launchv2.md`)

**Source of leads:** the target page plus the mechanism/IAM pages it depends on —
`AWSEC2/latest/UserGuide/{ec2launch-v2, ec2launch-v2-settings, ec2launch-v2-task-definitions, ec2launchv2-troubleshooting, ResettingAdminPassword, ResettingAdminPassword_EC2Launch, ResettingAdminPassword_EC2Config, ec2rw-ssm, ec2-windows-passwords, Windows-Server-EC2Rescue, user-data}.md`;
`service-authorization/latest/reference/list_ec2.md`;
`systems-manager/latest/userguide/automation-ec2reset.html` (the `AWSSupport-ResetAccess` runbook + its AWS-published sample IAM policy).

**Status:** documentation-derived hypotheses only — **nothing has been tested against a live AWS account.** Written for a downstream hunter (`aws-vuln-hunter`) to execute against an account it is *authorized* to test, with synthetic/canary data only. A companion, broader plan already exists for the parent topic at `/work/aws-docs/ResettingAdminPassword-attack-research-plan.md`; this plan is scoped to the **EC2Launch v2 variant** and the `.run-once` mechanism specifically, and is self-contained.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the §5 priority order; look left and right for adjacent bugs around every confirmed primitive.
- **HARD STOP / disclosure trigger:** this feature is single-account by design. The moment any evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane**, stop immediately, preserve evidence, route to AWS-Security. Do not escalate beyond existence.
- **Safe oracle first.** Every IAM-artifact lead (Lens R/S/T/B) is settleable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` — **no resources touched.** Escalate to a live scoped call only with canary role names / canary instances / canary parameters, then tear everything down.
- **Scoped-role discipline:** every "a principal denied X can still do Y" claim must be proven under a **scoped role holding exactly the artifact/grant named**, never under the over-privileged tester. A `DryRunOperation` result is caller-IAM-only (evaluated before resource resolution) — **it is NOT an ownership oracle.** Many EC2 resource IDs carry an embedded checksum, so a *fabricated* foreign ID that returns `InvalidID` is a genuine null, not an access check.

---

## 1. Pentest Objectives

Concrete boundary-breach outcomes, stated as goals:

1. **Control-plane → OS-SYSTEM escalation.** Starting from EC2 control-plane IAM only (no OS creds, no RDP, no `.pem`), obtain **local-Administrator / SYSTEM code execution** on a running Windows instance — not merely a reset password.
2. **IAM self-escalation via an AWS-authored artifact.** Starting from *exactly* the "least-privilege" IAM policy AWS tells customers to attach for the `AWSSupport-ResetAccess` runbook, reach account-level `AdministratorAccess`.
3. **Credential-wall bypass.** Recover the reset admin password — or the RSA key that decrypts it, or the EC2Rescue secret — through an IAM gate *different from and broader than* the one the operator believes protects it.
4. **Cross-instance (intra-account) IDOR.** Point any reset primitive (volume swap, `ModifyInstanceAttribute(userData)`, the SSM automation) at an instance the caller's intended scope never named, and prove whether IAM conditions can actually scope it.
5. **Negative / out-of-scope confirmation.** Prove the design is single-account (no cross-*account* reach) where the evidence says so, keeping the hunter off the shared-responsibility line.

---

## 2. Components, Assets, and Design

### The unifying mechanism
Every variant converges on one primitive: **force the on-instance EC2Launch v2 agent to run its `once`-frequency tasks again on next boot, so `setAdminAccount` regenerates the admin password — then retrieve it.** The agent runs as **LocalSystem**, reads its config and *trusts* it with no integrity check, and takes its "have I already run?" decision from a **plain file on the root EBS volume**. Therefore **whoever controls the volume (or the boot/userData channel) controls the agent — and the agent controls the OS**, with no OS-layer authentication ever required.

### The EC2Launch v2 state machine (the heart of the target page)
- **Config:** `C:\ProgramData\Amazon\EC2Launch\config\agent-config.yml` (plain YAML). The docs state the `config` directory's write permission "is restricted to the administrator account **to prevent privilege escalation**" (`ec2launch-v2.md`, directory-structure section) — an *online NTFS-ACL* control.
- **State:** `C:\ProgramData\Amazon\EC2Launch\state\` holds **`.run-once`** ("indicates whether the service has already run after Sysprep, so tasks with a frequency of `once` will be skipped on the next run"), plus `state.json` / `previous-state.json` (per-task status). (`ec2launch-v2.md`.)
- **Frequencies:** `once` = run only on first boot after Sysprep; `always` = every agent run (start/restart/`EC2Launch.exe run`). Only `executeScript` lets the *user* choose the frequency. (`ec2launch-v2.md`.)
- **Default `once` tasks:** `extendRootPartition` (Boot) → `activateWindows`, `setDnsSuffix`, **`setAdminAccount`**, `setWallpaper` (PreReady) → `startSsm` (PostReady). (`ec2launch-v2.md`.)
- **The target-page trigger:** deleting `state\.run-once` makes the agent believe it has never run → it re-executes **all `once` tasks**, including `setAdminAccount`. The page's own **"Important: Any scripts set to run once will be triggered by this action"** confirms the blast radius is *every* `once` task, not just the password reset.
- **`setAdminAccount` password types** (`ec2launch-v2-settings.md`): `Random` (agent generates, RSA-encrypts under the launch key pair's public key, then disables the setting so it persists across reboots), `Specify` (plaintext in `agent-config.yml` until Sysprep consumes it), `Do not set`.
- **`executeScript`** (`ec2launch-v2-task-definitions.md`): `runAs` is **required** and must be **`admin`** or **`localSystem`**; runs in `PreReady`, `PostReady`, or `UserData` stages; content is arbitrary PowerShell/batch. **This is the SYSTEM-code-execution sink.**

### Three delivery variants (same primitive)
1. **Manual offline volume swap** (the target page). `StopInstances` → `DetachVolume` (victim root) → `AttachVolume` to an attacker/operator **temporary instance** (same AZ; *different* Windows version to dodge disk-signature collision) as a secondary volume → edit the offline disk → reattach as `/dev/sda1` → `StartInstances` → `GetPasswordData`.
2. **SSM Automation** (`AWSSupport-ResetAccess`, server-side). Spins up a **temporary CFN VPC + SSM-enabled helper instance** *in the customer's own account*, attaches the victim's root volume to the helper, runs **EC2Rescue** to re-enable password generation, stores the Linux SSH key in **Parameter Store** (`/ec2rl/openssh/{instanceID}/key`), and leaves behind a **backup AMI** and a **password-enabled AMI**.
3. **SSM Run Command / in-place EC2Rescue** (`ec2rw-ssm`). Target already SSM-managed and online; no volume swap. Can **re-enable a disabled local Administrator account** and reset it.
4. **Adjacent boot channel (higher-yield, no volume swap):** `ec2:ModifyInstanceAttribute --attribute userData` + `StopInstances`/`StartInstances` plants an `executeScript`/`localSystem` user-data task the agent runs at next boot.

### Assets
- **Encrypted admin-password blob** (`passwordData`) — RSA-encrypted with the launch key pair's public key; decryption is 100% client-side (EC2 has **no notion of "the caller holds the private key"**).
- **Key-pair private key** — normally never stored by AWS, **but CloudFormation-created key pairs persist it** in SSM Parameter Store (`/ec2/keypair/{key_pair_id}`, `SecureString`).
- **EC2Rescue secret sinks** — Parameter Store `/EC2Rescue/Password/{instance_id}` (Windows) and `/ec2rl/openssh/{instance_id}/key` (Linux), encrypted under `alias/aws/ssm` (default) or a CMK.
- **On-disk config** `agent-config.yml` — holds a `Specify` password in **clear text** in the pre-Sysprep window; fully readable/writable when mounted offline.
- **Persistent AMIs** from the SSM automation (`AWSSupport-EC2Rescue:{InstanceID}` backup + "Password-enabled AMI from {InstanceID}"), left in the account with default (private) permissions.

### ASCII pipeline
```
 Caller (EC2 control-plane IAM only — no OS creds, no .pem)
    │
    │ Variant 1: StopInstances → DetachVolume(victim root) → AttachVolume(attacker temp inst)
    │ Variant 4: ModifyInstanceAttribute(userData) ───────────────┐
    ▼                                                             │
 Offline root EBS volume  ── mount on attacker instance ──►  write agent-config.yml
 (agent-config.yml, state\.run-once)                           + delete state\.run-once
    │  reattach /dev/sda1                                         │
    ▼                                                             ▼
 StartInstances ──► EC2Launch v2 (runs as LocalSystem) reads config, sees no .run-once
    │                         │
    │  re-runs ALL `once` tasks: setAdminAccount (new pwd) + ANY injected executeScript(localSystem)
    ▼                         ▼
 GetPasswordData ◄── new encrypted admin pwd        arbitrary SYSTEM code on victim OS
 (+ client-side decrypt with a key the caller controls)
```

---

## 3. API / Interface Inventory

| Name | Access level | Resource type(s) (required) | Scoping condition keys (selected) | Role in the attack | Notes |
|---|---|---|---|---|---|
| `ec2:StopInstances` | Write | instance* | `ec2:ResourceTag`, `ec2:InstanceID`, … | Quiesce victim before detach | Reboot/stop side effects |
| `ec2:DetachVolume` | Write | **instance** + **volume\*** | per-resource: instance side `ec2:InstanceID`/tag; volume side `ec2:VolumeID`/`ec2:ParentVolume`/tag | Remove root vol from victim | **No key links the volume to its instance** |
| `ec2:AttachVolume` | Write | **instance\*** + **volume\*** | instance: `ec2:InstanceID`,`ec2:InstanceProfile`,tag; volume: `ec2:VolumeID`,`ec2:ParentSnapshot`,`ec2:ParentVolume`,tag | Mount victim vol on attacker temp instance | **No cross-reference condition** (see Lens U/S) |
| `ec2:StartInstances` | Write | instance* | tag/`InstanceID` | Boot → agent re-runs `once` tasks | — |
| `ec2:GetPasswordData` | **Read** | instance* | tag/`InstanceID` | Retrieve encrypted admin pwd | Ciphertext only; decrypt is client-side |
| `ec2:ModifyInstanceAttribute` | Write | instance* (also security-group, volume) | **`ec2:Attribute`**, **`ec2:Attribute/${AttributeName}`**, tag | `userData` rewrite → SYSTEM exec; also `disableApiStop` | One action spanning many attributes |
| `ec2:CreateImage` | Write | image* + instance* | image: `aws:RequestTag`,`ec2:Owner`; instance: tag | "lost key pair" sub-flow; leftover AMIs | **Reboots even without `RebootInstances`** |
| `ec2:RunInstances` | Write | many (instance, image, volume, …) | `ec2:InstanceType`,`ec2:LaunchTemplate`,tag | Launch temp instance / relaunch from pwd-enabled AMI | — |
| `ec2:CreateKeyPair` / `ec2:DeleteKeyPair` | Write | key-pair* | `aws:RequestTag`,`ec2:KeyPairName` | Replace lost key pair (Step 2 sub-flow) | Delete-then-recreate same name |
| `ec2:GetConsoleOutput` | Read | instance* | tag/`InstanceID` | **Alternate password-blob channel** (Lens X) | Twin of GetPasswordData for the blob |
| `ssm:StartAutomationExecution` (`AWSSupport-ResetAccess`) | — | automation-definition | — | Server-side full reset | Needs the AWS-published IAM policy → Lens R/S |
| `ssm:SendCommand` (`AWSSupport-RunEC2RescueForWindowsTool`) | — | instance/document | tag | In-place reset / re-enable admin | No volume swap |
| `ssm:GetParameter` on `/ec2rl/*`, `/EC2Rescue/*`, `/ec2/keypair/*` | Read | parameter | path/tag | Recover reset secrets / private keys | Lens T/EE |

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller w/ EC2 control-plane IAM | Victim Windows OS (Administrator/SYSTEM) | Detach→attach→offline edit→boot, or `ModifyInstanceAttribute(userData)` | **SYSTEM code execution or a usable admin password on an instance the caller holds no OS credential for** |
| Attacker's temp instance (owner-controlled) | Victim's root EBS volume | `AttachVolume` with attacker-chosen target instance | **Victim root volume mounts read/write on an instance the attacker fully administers** |
| Low-priv principal holding the `AWSSupport-ResetAccess` sample policy | Account-wide `AdministratorAccess` | `CreateRole`+`AttachRolePolicy`+`PassRole`+`lambda:CreateFunction` within the `AWSSupport-EC2Rescue-*` name prefix | **A principal holding only the sample policy performs an action the policy's description implies it cannot (admin-level)** |
| Principal with `ssm:GetParameter` but denied EC2 key/password actions | Reset secret / SSH private key | Read `/ec2rl/openssh/{id}/key`, `/EC2Rescue/Password/{id}`, `/ec2/keypair/{id}` | **Cleartext credential retrieved via the storage service's read action, bypassing the EC2-side gate** |
| Caller | AWS service plane | (none expected — single-account design) | **ANY AWS-owned identity/ARN appearing = hard stop + disclosure** |

---

## 5. Recommended Areas of Focus

Priority order: (1) control-plane→SYSTEM escalation, (2) AWS-authored IAM-artifact self-escalation, (3) IAM-scoping reality of the volume swap, (4) cross-service secret reach, (5) persistence/leftover artifacts, (6) audit-trail gaps, (7) variant parity.

### Area 1 — Offline config injection → SYSTEM code execution (beyond password reset)  [Lens F / K / U / E]
**Background.** The target page edits the offline root volume to delete `state\.run-once`. But the *same* offline access gives full read/write to `config\agent-config.yml`, which the LocalSystem agent re-reads and trusts on boot. `executeScript` tasks run `runAs: localSystem|admin` with arbitrary script content.
**Security Concern.** The docs assert the `config` directory is "restricted to the administrator account **to prevent privilege escalation**" — but that NTFS ACL is an *online* control; it is meaningless once the volume is mounted on a temporary instance the attacker administers. There is **no documented integrity/signature/ownership check** on `agent-config.yml` or the state files before the agent executes them.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** An attacker who can mount the volume offline can add an `executeScript`/`localSystem` task to `agent-config.yml` (PreReady stage) that runs on the next boot *as SYSTEM* — a strictly stronger outcome than the documented password reset. → **Mechanism:** `ec2launch-v2-task-definitions.md` (`runAs` required, `localSystem` allowed); `ec2launch-v2.md` (config is plain YAML; agent runs as LocalSystem). → **Oracle:** the injected script executes on boot (e.g. writes a canary file / makes an outbound canary callback) with SYSTEM token. → **Preconditions:** the Area-3 volume-swap capability. → **Severity:** High (OS-admin takeover of a single instance within the account).
- **Claim:** Deleting `.run-once` *also* re-triggers any pre-existing `once` `executeScript` already in the customer's config (the page's own "Important" warning), so the recovery procedure can have unintended destructive/again-run side effects. → **Oracle:** a customer `once` task fires a second time after the documented procedure. → **Severity:** Low–Medium (integrity/availability, customer-owned config).
- **Claim:** No config integrity check exists — the agent will execute a wholly attacker-authored `agent-config.yml`. → **Oracle:** replace the config entirely offline; confirm the agent honors it on boot with no validation error attributable to tampering (vs schema error). → **Severity:** High (enables the first claim).

### Area 2 — `AWSSupport-ResetAccess` AWS-published IAM policy: non-admin → **account admin** self-escalation  [Lens R / S / B]  — **Critical**
**Background.** `automation-ec2reset.html` prints an **IAM policy AWS tells customers to attach verbatim** (inline or as a managed policy) to run the reset runbook, and the *same policy is byte-for-byte identical* inside the official CloudFormation template `AWSSupport-EC2RescueRole.json` (its description literally reads "Creates an IAM role with least privilege to run AWSSupport-ExecuteEC2Rescue"). The customer cannot edit it meaningfully, so a weak default is **AWS's defect → in scope, reportable, route `aws-security`.** This same policy is also what the runbook's `AutomationAssumeRole` carries when Automation runs "in the context of the user who ran the automation."
**Security Concern.** One statement grants, scoped only to the **name prefix** `role/AWSSupport-EC2Rescue-*` and `instance-profile/AWSSupport-EC2Rescue-*`, with **no `Condition` at all**:
`iam:CreateRole, iam:PutRolePolicy, iam:AttachRolePolicy, iam:PassRole, iam:CreateInstanceProfile, iam:AddRoleToInstanceProfile` (+ delete variants). Separate statements grant `lambda:CreateFunction` on `Resource: "*"` and `lambda:InvokeFunction` on `function:AWSSupport-EC2Rescue-*`. The name prefix provides **zero isolation** — the holder types the role/function name themselves. Two independent sinks:
1. `iam:AttachRolePolicy` carries **no `iam:PolicyARN` condition** → attach `arn:aws:iam::aws:policy/AdministratorAccess`.
2. `iam:PutRolePolicy` has **no mechanism to constrain inline-policy content** (IAM has no condition key for inline JSON) → write a hand-authored inline `{"Action":"*","Resource":"*"}`. **This second path means even allow-listing `PolicyARN` on `AttachRolePolicy` would be insufficient** — the *only* complete fix is a mandatory **permissions boundary** (`iam:PermissionsBoundary` condition on `CreateRole`/`PutRolePolicy`/`AttachRolePolicy`).
**High-level Test Scenarios:**
- **Claim:** A principal holding *only* this policy reaches full account admin. → **Walk (each step uses a grant present verbatim):** `CreateRole AWSSupport-EC2Rescue-pwn` with trust policy `{Principal:{Service:"lambda.amazonaws.com"},Action:"sts:AssumeRole"}` (trust content unconstrained) → `AttachRolePolicy …/AdministratorAccess` *or* `PutRolePolicy {"Action":"*","Resource":"*"}` → `lambda:CreateFunction` (Resource `*`, no `PassedToService` tying it) with `Role=…/AWSSupport-EC2Rescue-pwn` via `iam:PassRole` → `lambda:InvokeFunction` (name under the prefix) → code runs as admin; mint an IAM user/access key. → **Mechanism:** the exact statements above (doc + CFN template). → **Oracle (safe first):** `iam:SimulatePrincipalPolicy` for the scoped principal on `iam:AttachRolePolicy{PolicyArn=…/AdministratorAccess}`, `iam:PutRolePolicy`, `lambda:CreateFunction`, `iam:PassRole`, `lambda:InvokeFunction` — all must return `allowed`. Escalate to a live run only with a canary role + canary Lambda, then delete. → **Refuting control (absent):** a permissions boundary on the role-creation statements. → **Severity:** **Critical** (non-admin → account admin via an AWS-authored, copy-verbatim artifact; also reachable by anyone who can invoke the runbook under this `AutomationAssumeRole`).

### Area 2b — `AWSSupport-StartEC2RescueWorkflow` `OfflineScript`: arbitrary code against the mounted victim volume  [Lens K / E]
**Background.** The lower-level runbook `AWSSupport-StartEC2RescueWorkflow` (which `AWSSupport-ResetAccess` wraps) takes a **required, caller-supplied, base64-encoded Bash/PowerShell `OfflineScript`** that executes **on the helper instance with the victim's root volume mounted**.
**Security Concern.** Anyone who can invoke that document *directly* (rather than only via the narrower `AWSSupport-ResetAccess` wrapper) controls exactly what code touches the mounted victim disk — a documented, by-design arbitrary-code-execution primitive over another instance's offline disk, in-account.
**High-level Test Scenarios:**
- **Claim:** A principal with `ssm:StartAutomationExecution` on `AWSSupport-StartEC2RescueWorkflow` can run an attacker `OfflineScript` that reads/writes the victim volume (exfiltrate SAM hashes, plant the Area-1 `agent-config.yml` payload). → **Oracle:** supply a canary `OfflineScript` that drops a marker into the mounted volume; confirm execution. → **Severity:** High (offline disk RCE on a chosen instance).

### Area 3 — Can IAM actually scope the volume swap? (the unconditioned capability)  [Lens U / S / A]
**Background.** The whole recovery relies on `DetachVolume`(victim)→`AttachVolume`(attacker instance). The thesis: holding `Stop/Detach/Attach/Start/GetPasswordData` on Windows instances ≈ "Administrator on every Windows instance in the account," and IAM **cannot** cleanly prevent it.
**Security Concern.** From `list_ec2.md`: `AttachVolume` requires **both** `instance*` and `volume*` resource types, each with its *own independent* condition keys (instance: `ec2:InstanceID`,`ec2:InstanceProfile`,`ec2:ResourceTag`; volume: `ec2:VolumeID`,`ec2:ParentSnapshot`,`ec2:ParentVolume`,`ec2:ResourceTag`). A grep of the **full ~145-entry EC2 condition-key catalogue** (`list_ec2.md` lines 10036–10190) confirms **there is no key that binds a volume to its origin/owning instance** — no `ec2:SourceInstance`/`ec2:AttachedInstance`/`ec2:PreviousOwner`. `ec2:ParentVolume`/`ec2:ParentSnapshot` track EBS *creation* lineage, not attachment history; `ec2:SourceInstanceARN` is STS session provenance, not volume lineage. IAM evaluates the instance-side and volume-side conditions **independently** (not a join), so a matching tag on both just means "attacker needs a same-tagged instance," which a broad EC2-write role can create for itself (`RunInstances`+`CreateTags`).
**High-level Test Scenarios:**
- **Claim:** No IAM policy can express "this root volume may be re-attached only to the instance it was detached from," so any principal who can attach volumes to *their own* temp instance can mount *any* taggable victim volume. → **Oracle:** attempt to author a policy that allows legitimate maintenance but denies attaching a tagged "production root volume" to a freshly created attacker instance; show it is not expressible (the attacker tags their own temp instance to satisfy the instance-side condition; the volume-side condition only matches the volume, not the pairing). Pinning explicit `ec2:VolumeID`/`ec2:InstanceID` *lists* out-of-band is the only option and is operationally brittle (breaks resize/AZ-migration/ordinary maintenance). Use `SimulateCustomPolicy` to demonstrate the gap. → **Severity:** Informational→High *as an enforcement-gap enabler* (precondition for Areas 1, 2b & 4; the underlying takeover is High).
- **Claim (case-sensitivity fail-open, Lens S variant — confirmed-plausible):** The `InstanceAttributeName` API enum is **camelCase** (`userData`, `disableApiTermination`). A Deny written PascalCase — `"StringEquals":{"ec2:Attribute":"UserData"}` — is **inert**, because IAM key *names* are case-insensitive but compared *values* are case-sensitive (`iam-policies-for-amazon-ec2.md` line 155 says only the *name* is case-insensitive). The Deny silently fails to match a real `Attribute=userData` call and any broad Allow proceeds. → **Oracle:** author a PascalCase `ec2:Attribute` Deny, confirm a `userData` rewrite still succeeds under it. → **Severity:** High (userData-rewrite Deny bypass → SYSTEM exec via Area 4).
- **Claim (non-existent condition key fail-open, Lens S variant):** `ec2:InterfaceType` returns **zero hits** in the entire `list_ec2.md` — it is not a real IAM key (only an API *response field*). A Deny conditioned on it never fires (the context key is never present). Audit the feature's recommended policies for Denies keyed on non-existent keys, and for `…IfExists`/`Null` fail-open shapes (`iam-policies-for-amazon-ec2.md` line 196). → **Oracle:** confirm a Deny keyed on `ec2:InterfaceType` (or any absent key) is inert. → **Severity:** Medium–High depending on what the inert Deny was meant to block.
- **Claim (IDOR, intra-account):** Each of `Stop/Detach/Attach/Start/GetPasswordData/ModifyInstanceAttribute` authorizes per-resource on existence + whatever tag/ID condition is present — point them at an instance outside the operator's intended team scope. → **Oracle:** perform the reset against a canary instance the scoped role was never meant to touch. → **Severity:** intra-account cross-team = Medium–High (cross-**account** is out of scope / hard stop).

### Area 4 — `ModifyInstanceAttribute(userData)` → SYSTEM exec without the volume swap  [Lens B-variant / E / U]
**Background.** EC2Launch v2 runs user data as an `executeScript` task (`localSystem`/`admin`) during the UserData stage on every boot where it is marked to persist (`<persist>true</persist>` / `frequency: always`).
**Security Concern.** `ec2:ModifyInstanceAttribute` is a **single action spanning many attributes**; the sub-attribute `userData` can be scoped with `ec2:Attribute/${AttributeName}`, but if a policy grants `ModifyInstanceAttribute` for any benign attribute *without* that condition, it also grants `userData` rewrite. This is a **non-`PassRole` action that reaches code execution as SYSTEM** (the confirmed-exemplar shape in the corpus).
**High-level Test Scenarios:**
- **Claim:** A principal with unscoped `ec2:ModifyInstanceAttribute` + `Stop/Start` on a Windows instance gets SYSTEM code exec on next boot by writing a persistent `executeScript`/`localSystem` user-data payload. → **Mechanism:** `ec2launch-v2-settings.md` (user data = `executeScript`, `runAs: localSystem`, `<persist>`); `list_ec2.md` ModifyInstanceAttribute. → **Oracle:** canary user-data payload executes as SYSTEM after a stop/start cycle. → **Severity:** High. **This avoids the volume swap entirely** — flag whether orgs that locked down `DetachVolume` left `ModifyInstanceAttribute` open.

### Area 5 — EC2Rescue / SSM secret sinks reachable via a different IAM gate  [Lens T / EE]
**Background.** The automated paths write generated secrets to Parameter Store at **deterministic, public-ID-derived paths**: `/ec2rl/openssh/{instanceID}/key` (Linux SSH, "encrypted"), `/EC2Rescue/Password/{instance_id}` (Windows), and CFN key pairs at `/ec2/keypair/{key_pair_id}`.
**Security Concern.** A secret created under an EC2/SSM-automation gate comes to rest under SSM Parameter Store's *own* IAM + KMS reachability. A principal **denied** the EC2 password/key actions may still read the cleartext via `ssm:GetParameter`.
**High-level Test Scenarios:**
- **Claim:** A principal with `ssm:GetParameter` on `/ec2rl/*` (or `/EC2Rescue/*`, `/ec2/keypair/*`) but no `ec2:GetPasswordData`/no `.pem` can recover SSH private keys / reset passwords for instances reset this way. → **Oracle:** under a scoped role proving the EC2-side **deny** and the SSM-side **allow** in one run, read a canary parameter. → **Preconditions:** the path is derivable from the public instance ID (enumerable). → **Severity:** Medium–High (credential-wall bypass).
- **Claim (KMS, Lens T):** The `AWSSupport-ResetAccess` / `AWSSupport-StartEC2RescueWorkflow` parameter list exposes **no KMS-key parameter** (unlike the Run-Command path, which lets the caller supply a CMK). So `/ec2rl/openssh/*` is a `SecureString` encrypted under the **default managed key `alias/aws/ssm`** — an account-shared key whose policy commonly delegates via `kms:ViaService`, so `kms:Decrypt` can succeed without the caller holding it explicitly. → **Oracle:** confirm decrypt succeeds for a role lacking `kms:Decrypt` in its identity policy. → **Severity:** Medium–High.
- **Claim (lifecycle):** The runbook's "How it works" enumerates cleanup (temp instance, temp VPC, Lambdas) but says **nothing about deleting `/ec2rl/openssh/{id}/key`** — and, unlike the leftover AMIs, the customer is **not even warned** it lingers. The secret persists indefinitely by default. → **Oracle:** confirm the parameter survives automation completion. → **Severity:** Medium (stale-credential recovery window is unbounded).

### Area 6 — Persistent leftover AMIs (predictable name land-grab / stale access)  [Lens EE / AA]
**Background.** `AWSSupport-ResetAccess` deliberately leaves two AMIs: `AWSSupport-EC2Rescue:{InstanceID}` (backup) and "Password-enabled AMI from {InstanceID}" — **predictable names, left in the account.**
**Security Concern.** A **password-enabled AMI** launched by anyone who can `RunInstances` from it (with a key pair *they* control) yields an admin password *they* can decrypt — a clone of the victim's disk with attacker-retrievable admin.
**High-level Test Scenarios:**
- **Claim:** An intra-account principal who can `DescribeImages`+`RunInstances` from the leftover password-enabled AMI obtains an admin-accessible clone of the victim's data. → **Oracle:** launch from the leftover AMI with an attacker key pair; `GetPasswordData`; decrypt. → **Severity:** Medium–High (data clone + admin).
- **Claim (AA):** If the backup/password-enabled AMI is ever shared (`launchPermission`), does revocation sever all derived copies? → **Oracle:** standard launch-permission revoke-completeness test. → **Severity:** Medium (only if sharing is in play).

### Area 7 — Variant / twin parity and alternate password-blob channel  [Lens X]
**Background.** Three agent families reset the same way (EC2Launch v2 `.run-once`; EC2Launch via EC2Rescue; EC2Config `Ec2SetPassword` plugin in `config.xml`), and two APIs expose the encrypted password blob.
**High-level Test Scenarios:**
- **Claim:** `ec2:GetConsoleOutput` is an alternate retrieval channel for the encrypted-password blob — an org that denies `GetPasswordData` but allows `GetConsoleOutput` has an unguarded twin. → **Oracle:** retrieve the blob via console output where `GetPasswordData` is denied. → **Severity:** Medium (credential-channel parity gap).
- **Claim:** The EC2Config variant (`ResettingAdminPassword_EC2Config.md`) flips `Ec2SetPassword` in `config.xml` offline — same offline-trust primitive on older AMIs; confirm the same no-integrity-check property. → **Severity:** High (same as Area 1 on legacy fleet).

### Area 8 — Audit-trail visibility of the reset  [Lens O]
**Background.** The decisive act in Variant 1 — deleting `state\.run-once` and editing `agent-config.yml` — happens **inside a mounted volume on a helper instance**, invisible to CloudTrail; only the EC2 control-plane calls (`DetachVolume`/`AttachVolume`/`Start`) are logged.
**High-level Test Scenarios:**
- **Claim:** There is no AWS-side audit record that distinguishes a legitimate password recovery from a volume-swap takeover; the OS-level file edit produces no CloudTrail event. → **Oracle:** confirm which of the steps appear in CloudTrail vs none for the offline edit. → **Severity:** Low–Informational (detection-gap enabler; raises severity of Areas 1/3).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Offline config injection → SYSTEM exec | `agent-config.yml` / EC2Launch v2 LocalSystem | "config dir restricted to administrator to prevent privilege escalation" (NTFS ACL) — defeated offline |
| Non-admin → account admin | `AWSSupport-ResetAccess` sample IAM policy | the policy's own name-prefix scoping on IAM write actions (no `PolicyArn` condition) |
| Volume re-attach to foreign instance | `AttachVolume` authz | per-resource `ec2:VolumeID`/`ec2:InstanceID`/tag conditions (no volume↔instance binding) |
| `userData` rewrite → SYSTEM exec | `ModifyInstanceAttribute` | `ec2:Attribute/${AttributeName}` condition (test case-sensitivity / presence) |
| Secret recovery via storage gate | Parameter Store `/ec2rl/*`,`/EC2Rescue/*`,`/ec2/keypair/*` | SSM parameter path IAM + KMS key policy / `kms:ViaService` |
| Password blob via alternate channel | `GetConsoleOutput` vs `GetPasswordData` | separate IAM actions for the same ciphertext |
| Leftover password-enabled AMI clone | `CreateImage` output AMIs | default-private AMI permissions |
| Reset undetectable | CloudTrail vs offline file edit | control-plane logging only |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account reach.** This feature is single-account by design; all reset paths operate within the customer account. Any AWS-service-plane identity/ARN is a **hard stop + disclosure**, never a finding to pursue.
- **IMDS on the managed hosts**, shared EBS/Nitro storage-plane internals — AWS-owned, out of scope.
- **Customer-authored** least-privilege mistakes (a customer writing their own over-broad policy) — footgun, out of scope. *Carve-out:* the **AWS-published** `AWSSupport-ResetAccess` policy / CFN template / runbook (Area 2) **is in scope** precisely because the customer copies it verbatim.
- **Physical EBS attack / disk-signature-collision** as a reliability note — the "different Windows version" instruction is an availability guard, not a security control; not a vuln by itself.
- **A legitimate account admin resetting their own instance** — the design intent; only the *privilege-escalation* and *cross-scope* variants are in scope.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, did not fire)

- **Lens G (SSRF):** N/A — read `ResettingAdminPassword_EC2Launchv2`, `ec2launch-v2`, `ec2launch-v2-settings`, `ec2launch-v2-task-definitions`. The only URL/path fields (`setWallpaper` image path, `copyFiles`/`writeFiles` destinations, `--path`) are **local filesystem paths**, not server-side-dereferenced URLs. No field the service fetches on the customer's behalf. (`setWallpaper` image path → see Lens Q note below, not SSRF.)
- **Lens Q (upload/parse):** Thin fire — the `setWallpaper` `.jpg` and `executeScript`/`copyFiles` content are *locally* parsed on the instance the attacker already controls via Area 1; no cross-tenant render surface. Marked **low/absorbed into Area 1**. Confirm no path-traversal in `writeFiles`/`copyFiles destination` as an adjacent check.
- **Lens F (wire-protocol/translation injection):** N/A — no customer-input-to-backend-language translator on this surface; `agent-config.yml` is parsed and executed locally (covered by Area 1, not a cross-boundary injection).
- **Lens H/W (KMS/attestation):** N/A for the agent itself; KMS appears only indirectly for the Parameter Store SecureString (handled in Area 5, Lens T).
- **Lens J / FF (OAuth / JWT):** N/A — no 3P linking or bearer-token validation on these pages.
- **Lens V / D (network segmentation / data→control-plane):** N/A — no customer-reachable multi-ENI service process here; the "control plane" touched is the public EC2 API, gated by IAM (covered by Areas 2–4).
- **Lens BB / CC / DD (parser-differential / upstream-context / cache):** N/A — no multi-parser request path, no asserted-identity header chain, no caching layer on this documentation surface.
- **Lens Y (transport/sig):** N/A at the agent layer; EC2/SSM API SigV4 transport is generic AWS surface, not specific to this feature.
- **Doc gap:** the docs do **not** state whether `agent-config.yml` / state files carry any integrity or signature verification. This is **assumed absent** (Area 1 Claim 3) and must be confirmed empirically — mark Area 1 "doc-gap — confirm no config integrity check first." Likewise the exact KMS key and `SecureString` status of `/ec2rl/openssh/*` and `/EC2Rescue/Password/*` are not fully specified on these pages — confirm the key and parameter type before relying on the Area 5 Lens-T claim.

---

### Kill-chain summary (rate at the end of the chain)
1. **IAM-only → SYSTEM:** scoped EC2 perms (Area 3, unconditioned attach, no volume↔instance key) → offline config injection (Area 1, `executeScript localSystem`) *or* `OfflineScript` (Area 2b) → **SYSTEM on the victim instance** — *High*, no OS credential ever used.
2. **Sample-policy → account admin:** hold `AWSSupport-ResetAccess` policy (Area 2) → `CreateRole`+(`AttachRolePolicy AdministratorAccess` **or** `PutRolePolicy *:*`)+`PassRole`+`lambda:CreateFunction`+`InvokeFunction` → **account `AdministratorAccess`** — ***Critical***, AWS-authored copy-verbatim artifact; only a permissions boundary refutes it.
3. **Storage-gate credential recovery:** `ssm:GetParameter /ec2rl/*` on the default `alias/aws/ssm` key (Area 5) → SSH key / reset password for instances with no EC2-side grant, from a never-deleted, instance-ID-derived path — *Medium–High*.
4. **Bonus reboot-bypass:** `ec2:CreateImage` "can reboot instances as part of image creation **even without `RebootInstances` permissions**" (`list_ec2.md` line 5143) — an implicit state-change side effect to flag in any policy review; `ec2:DeleteKeyPair`'s resource is **not required**, enabling the Step-2 delete-then-recreate-same-name key-pair sub-flow with optional scoping.
