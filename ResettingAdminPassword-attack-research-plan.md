# EC2 Windows Administrator Password Reset — Attack Research Plan

**Source of leads:** docs.aws.amazon.com + offline mirror `/work/aws-docs/docs/`. Primary pages:
`AWSEC2/latest/UserGuide/{ResettingAdminPassword, ResettingAdminPassword_EC2Launchv2, ResettingAdminPassword_EC2Launch, ResettingAdminPassword_EC2Config, ec2rw-ssm, ec2launch-v2, ec2launch-v2-settings, ec2launch-v2-task-definitions, ec2launch, ec2config-service, sysprep-using-ec2launchv2, user-data, ec2launchv2-troubleshooting, ec2-key-pairs, create-key-pairs, delete-key-pair, describe-keys, connecting_to_windows_instance, ec2-windows-passwords, ec2-serial-console, configure-access-to-serial-console}.md`;
`AWSEC2/latest/APIReference/API_{GetPasswordData,GetConsoleOutput,ModifyInstanceAttribute,AttachVolume,DetachVolume,StopInstances,StartInstances,CreateImage,CreateKeyPair,ImportKeyPair,DescribeKeyPairs}.md`;
`systems-manager/latest/userguide/automation-{ec2reset, ec2rescue, setup-iam, awssupport-resetaccess, awssupport-startec2rescueworkflow, awssupport-runec2rescueforwindowstool}.md`;
`service-authorization/latest/reference/{list_ec2, list_ssm, list_ec2-instance-connect}.md`;
AWS-published artifacts fetched live: `AWSSupport-EC2RescueRole.zip` (CFN template) and the `AmazonSSMAutomationRole` managed-policy JSON.

**Status:** documentation-derived hypotheses only; nothing has been tested against a live AWS account. This plan is written for a downstream hunter (e.g. `aws-vuln-hunter`) to execute against an account it is *authorized* to test, with synthetic/canary data only.

---

## 0. How to use this document

- Each lead is stated as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs around each confirmed primitive.
- **HARD STOP / disclosure trigger:** the moment any evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane** (not the customer account), stop immediately, preserve evidence, and route to AWS-Security disclosure. This feature is overwhelmingly single-account by design, so a service-plane identity appearing anywhere is a strong signal and a hard stop.
- **Safe oracle first.** Every IAM-artifact lead below (Lens R/S/T/B) is settleable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` — **no resources touched**. Only escalate to a live scoped call with canary role names / canary instances / canary parameters, and tear everything down.
- **Scoped-role discipline:** every "a principal denied X can still do Y" claim must be proven under a **scoped role holding exactly the artifact / exactly the grant named**, never under the over-privileged tester identity. A `DryRunOperation` response is caller-IAM-only (evaluated before resource resolution) — **it is NOT an ownership oracle.**

---

## 1. Pentest Objectives

Concrete boundary-breach outcomes a hunter should try to achieve:

1. **Control-plane → OS-admin escalation.** Starting from EC2 control-plane IAM only (no OS credentials, no RDP, no key-pair private key), obtain SYSTEM / local-Administrator code execution on a Windows instance.
2. **IAM self-escalation via an AWS-authored artifact.** Starting from *exactly* the "least-privilege" IAM policy AWS tells customers to attach for this feature, reach account-level `AdministratorAccess`.
3. **Credential-wall bypass.** Recover the reset Windows admin password — or the RSA private key that decrypts it — through a channel gated by a *different* (often broader, unrelated) IAM permission than the one an operator believes protects it.
4. **Cross-instance (intra-account) IDOR.** Point any of the reset primitives (SSM automation, volume swap, userData mutation) at an instance the caller's intended scope never named.
5. **Negative / out-of-scope confirmation.** Prove the design is single-account (no cross-*account* reach) where the evidence says so, so the hunter stays off the shared-responsibility line.

---

## 2. Components, Assets, and Design

### The unifying mechanism
All reset paths converge on one primitive: **force the on-instance agent (EC2Launch v2 / EC2Launch / EC2Config) to generate a NEW admin password on next boot, then retrieve it.** Because the agent config lives on the root EBS volume and the agent runs as LocalSystem, controlling the *volume* or the *boot/userData* equals controlling the *password* — without ever authenticating at the OS layer.

### Three delivery variants (same primitive)
- **Manual offline volume swap (console-driven).** Stop instance → detach root volume → attach to an attacker/operator-controlled *temporary* instance (same AZ, *different* Windows version to avoid disk-signature collision) as secondary → edit the agent's reset trigger offline → re-attach → boot → retrieve password.
  - EC2Launch v2: delete `D:\ProgramData\Amazon\EC2Launch\state\.run-once` (forces all `once`-frequency tasks, incl. `setAdminAccount`, to rerun).
  - EC2Launch: run the EC2Rescue tool's "Reset Administrator Password".
  - EC2Config: flip the `Ec2SetPassword` plugin in `config.xml` from `Disabled` → `Enabled`.
- **SSM Automation (server-side).** `AWSSupport-ResetAccess` → nested `AWSSupport-StartEC2RescueWorkflow` performs the volume swap automatically using a launched **helper/EC2Rescue instance** in a **temporary CloudFormation-provisioned VPC**, all inside the **customer's own account**; writes the new secret to SSM Parameter Store; also produces persistent backup + password-enabled AMIs.
- **SSM Run Command (in-place).** `AWSSupport-RunEC2RescueForWindowsTool` — target already SSM-managed and online, no volume swap; can **re-enable a disabled local Administrator account**.
- **Boot/userData channel (adjacent, higher-yield).** `ec2:ModifyInstanceAttribute(--attribute userData)` + `StopInstances`/`StartInstances` plants attacker code the EC2Launch v2 UserData stage runs as `localSystem`/admin — a SYSTEM-code-exec primitive that doesn't even need the volume swap.

### Assets
- **Encrypted admin-password blob** (`passwordData`) — generated at boot, RSA-encrypted with the launch key pair's public key.
- **Key-pair private key** — normally never stored by AWS; **but CloudFormation-created key pairs persist it** in SSM Parameter Store at `/ec2/keypair/{key_pair_id}` as a `SecureString`.
- **Reset secret sinks (EC2Rescue):** SSM Parameter Store `/EC2Rescue/Password/<instance_id>` (Windows) and `/ec2rl/openssh/<instance_id>/key` (Linux SSH), encrypted under `alias/aws/ssm` (default) or a CMK.
- **On-disk agent config:** `agent-config.yml` / `LaunchConfig.json` / `config.xml` / `Sysprep.xml` — hold the password field in **clear text** during the window before Sysprep consumes/deletes it.
- **Persistent AMIs** produced by the SSM automation (backup + password-enabled), left in the account with default (private) permissions.

### Identity / trust split
EC2's backend has **no notion of "the caller holds the private key."** `GetPasswordData` is pure IAM-gated ciphertext retrieval; decryption happens entirely client-side. So two *independently configurable* gates stand between an attacker and the plaintext password — the ciphertext gate (`ec2:GetPasswordData` **or** `ec2:GetConsoleOutput` **or** offline disk read) and the key gate (private `.pem` file **or** `ssm:GetParameter` on the CFN key-pair path).

### ASCII pipeline
```
 Attacker with EC2 control-plane IAM (NO OS creds / NO key pair)
   │
   ├── Path 1: Boot/userData channel  (least privilege required)
   │     StopInstances → ModifyInstanceAttribute(userData=payload) → StartInstances
   │       → EC2Launch v2 UserData stage: executeScript/executeProgram runAs=localSystem
   │       → attacker code as SYSTEM / local Administrator
   │
   ├── Path 2: Offline volume swap (manual or via SSM AWSSupport-ResetAccess)
   │     StopInstances → DetachVolume(root) → AttachVolume(root → attacker temp instance)
   │       → edit .run-once / Ec2SetPassword / EC2Rescue offline (reads cleartext config too)
   │       → DetachVolume → AttachVolume(back) → StartInstances
   │       → new admin password generated on boot
   │
   └── Retrieve the secret (any ONE channel is enough):
         GetPasswordData (ciphertext)  ──decrypt──┐
         GetConsoleOutput (ciphertext) ──decrypt──┤── private .pem  OR
         offline agent-config.yml (cleartext)     │   ssm:GetParameter /ec2/keypair/{id}
         ssm:GetParameter /EC2Rescue/Password/{id}┘   (CFN-created pairs; no ec2:*KeyPair* needed)
                                                   → plaintext Windows Administrator password
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal w/ only `ec2:StopInstances`+`ModifyInstanceAttribute(userData)`+`StartInstances` (no OS creds) | Local SYSTEM / Administrator code exec | Plant userData → boot → EC2Launch v2 UserData-stage `executeScript runAs=localSystem` | Attacker code runs as SYSTEM on an instance never authenticated to at OS layer. **Documented design fact** (`user-data.md`). |
| Holder of *exactly* the documented "required IAM permissions" | Account-level `AdministratorAccess` | `AWSSupport-EC2RescueRole.json`: `iam:CreateRole`+`AttachRolePolicy`+`PassRole` scoped **only by role-name prefix**, no `iam:PolicyARN`/`PassedToService` condition | A non-admin creates `role/AWSSupport-EC2Rescue-admin`, attaches `AdministratorAccess`, passes it onward — proven by `SimulatePrincipalPolicy`. |
| Role built "to reset instance i-AAAA" | Any instance / any SSM parameter in the account | `AmazonSSMAutomationRole` grants `ec2:{Stop,Start,Terminate}Instances,CreateImage,…` + `ssm:*` on `Resource:"*"`, **no conditions** | The scoped role stops/terminates/images i-BBBB, or reads another job's `/EC2Rescue/Password/*`. |
| Any `ssm:GetParameter` holder (unrelated ops/config role) | Another instance's reset password / SSH key | Deterministic path `/EC2Rescue/Password/<id>`; **no SSM path-prefix condition key exists** | Principal with broad `ssm:GetParameter` + no EC2 reset perms reads a foreign instance's fresh admin password. |
| Broad `ssm:GetParameter` holder w/ **zero** `ec2:*KeyPair*` | Plaintext RSA private key (CFN-created pair) | `/ec2/keypair/{key_pair_id}` SecureString, gated by SSM IAM only; `key_pair_id` enumerable via unscopable `DescribeKeyPairs` | Principal denied all `ec2:*KeyPair*` retrieves the private key, decrypts `GetPasswordData`. |
| Any `ec2:GetConsoleOutput` holder | Password ciphertext (same asset `GetPasswordData` protects) | `SetPasswordAfterSysprep` / troubleshooting log echoes `<Password>…</Password>` to console | Policy denying `GetPasswordData` but allowing `GetConsoleOutput` still yields the ciphertext — twin-action parity break. |
| Temp-instance admin (holds a 2nd instance + attach/detach rights) | Original instance's "protected" agent-config directory | Offline-mount the detached root volume | NTFS ACL ("restricted … to prevent privilege escalation") is inert offline — the official reset procedure itself exploits this. |
| Any SSM automation in the account (not just this feature) | `AWSSupport-EC2Rescue-*` role | Trust policy `Principal: ssm.amazonaws.com`, **no `aws:SourceArn`/`SourceAccount`** | Confused-deputy: an unrelated automation assumes the role. |
| **Any customer surface** | **AWS's own service plane** | — | **HARD STOP.** Any AWS-fleet identity/ARN/account = disclosure, stop immediately. |

---

## 4. API / Interface Inventory

| Name | Mutating? | Resource-level IAM scoping (per `list_ec2.md`) | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:ModifyInstanceAttribute(userData)` | Yes (Write) | `instance`; condition keys incl. `ec2:Attribute`, `ec2:Attribute/${AttributeName}` | Yes (SigV4) | any grantee | **Primary privesc primitive.** `ec2:Attribute/${AttributeName}` is the *only* key that could scope-deny `userData` specifically; broad grants cover it implicitly. No userData signing/allow-list documented. |
| `ec2:StopInstances` / `StartInstances` | Yes | `instance`, `ec2:InstanceID`, `aws:ResourceTag` | Yes | any grantee | Required to mutate userData / do volume swap. No condition key separates benign stop from weaponized stop. |
| `ec2:GetPasswordData` | No (Read) | `instance*` (**resource-level supported**); long condition-key list incl. `ec2:InstanceID`, `ec2:ResourceTag/*` | Yes | any grantee | Returns ciphertext only; private-key possession never checked by EC2. Row shows no *action-level* condition key (keys attach at resource type). |
| `ec2:GetConsoleOutput` | No (Read) | `instance` | Yes | any grantee | **Twin of GetPasswordData** — same asset, disjoint IAM gate. Also leaks RDP cert thumbprint. |
| `ec2:AttachVolume` / `DetachVolume` | Yes | `volume`/`instance`, `ec2:InstanceID`/`ec2:VolumeID`/`aws:ResourceTag` | Yes | any grantee | Enables offline-mount of the "protected" config dir. The official remediation path == the attack path. |
| `ec2:CreateImage` | Yes | `instance` | Yes | any grantee | Captures in-flight cleartext config files permanently into an AMI; also the "lost key pair" relaunch path. Follow-up lead. |
| `ec2:CreateKeyPair` | Yes | `key-pair*`; `aws:RequestTag`, `ec2:KeyPairType` (**no `ec2:KeyPairName`**) | Yes | any grantee | Returns private key once in response. |
| `ec2:ImportKeyPair` | Yes | `key-pair*` | Yes | any grantee | Public-key only — **SSM-parameter persistence (Lens T) applies only to EC2-*created*, not imported, pairs.** |
| `ec2:DescribeKeyPairs` | No (List) | **None** — blank resource type, `Resource:"*"` mandatory | Yes | any grantee | **Cannot be IAM-scoped per key pair.** Enumerates every `key_pair_id` (precursor to the SSM key-read chain). `--include-public-key` discloses public keys account-wide. |
| `ec2:DeleteKeyPair` | Yes | `key-pair`, `ec2:KeyPairName` | Yes | any grantee | Deletes EC2 public key only; "does not delete the matching private key." Direct-API delete on a CFN pair may orphan the SSM parameter (doc-gap). |
| `ssm:GetParameter`/`GetParameters` on `/ec2/keypair/*`, `/EC2Rescue/Password/*`, `/ec2rl/openssh/*` | No | SSM parameter condition keys are `aws:ResourceTag`/`ssm:resourceTag` only — **no path/prefix key** | Yes | whoever SSM policy allows | The cross-service secret-reachability seam; scoping must come from the literal `Resource` ARN string, which ops roles often wildcard. |
| `ssm:StartAutomationExecution` (`AWSSupport-ResetAccess`) | Yes | automation-document ARN | Yes | caller + optional `AutomationAssumeRole` (defaults to caller creds) | Entry point; `InstanceId`/`SubnetId` are unconstrained `String` params. |
| `ssm:StartAutomationExecution` (`AWSSupport-StartEC2RescueWorkflow`, nested) | Yes | document ARN | Yes | same | **Directly invokable, not only via ResetAccess.** Accepts raw base64 `OfflineScript` executed against the attached offline volume — a generic "run my script against any volume" primitive. |
| `ssm:SendCommand` (`AWSSupport-RunEC2RescueForWindowsTool`) | Yes | document ARN | Yes | caller | In-place variant; **re-enables a disabled local Administrator**. |
| `iam:CreateRole`/`CreateInstanceProfile`/`AttachRolePolicy`/`PutRolePolicy`/`PassRole` | Yes | `role/AWSSupport-EC2Rescue-*` **name-prefix only**, no further condition | — | holder of the documented policy | **Self-escalation engine** (Lens R). |
| `lambda:CreateFunction` | Yes | `Resource:"*"` — **no name restriction** (unlike sibling `Invoke/Delete/GetFunction` scoped to `AWSSupport-EC2Rescue-*`) | — | holder of the documented policy | Second escalation vector: admin-policy role → new Lambda → code exec. |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | Yes | `instance*`, `aws:ResourceTag/*` | Yes | grantee + account serial-console toggle (default **off**) | Alternate admin path; docs: "equivalent to granting admin-level privileges on the instance." |

**Verbatim doc pointers worth keeping:** no literal `[NEW]` markers anywhere in this surface. AWS's own fallback for an under-permissioned caller: *"If you have Administrator-level permissions … you might be able to run the automation without configuring permissions"* (`automation-ec2reset.md`) — a tacit admission the granular policy is hard to get right.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### [P1] Lens R/S/U — IAM self-escalation via the AWS-authored "least-privilege" EC2Rescue artifact
**Background.** `automation-ec2reset.md` links a CloudFormation template (`AWSSupport-EC2RescueRole.json`) whose own `Description` is *"Creates an IAM role with least privilege to run AWSSupport-ExecuteEC2Rescue."* The identical inline policy is printed copy-paste in `automation-ec2reset.md`, `automation-ec2rescue.md`, and `automation-awssupport-startec2rescueworkflow.md`.
**Security Concern.** Its statement grants `iam:CreateRole, CreateInstanceProfile, PutRolePolicy, AttachRolePolicy, PassRole, AddRoleToInstanceProfile` scoped to `role/AWSSupport-EC2Rescue-*` / `instance-profile/AWSSupport-EC2Rescue-*` **by name prefix with NO `Condition`** — no `iam:PolicyARN` on `AttachRolePolicy`, no `iam:PassedToService` on `PassRole`. The same statement block grants `lambda:CreateFunction` on `Resource:"*"`. The companion AWS-managed `AmazonSSMAutomationRole` (which the docs instruct customers to attach) grants `ssm:*` and `ec2:{Stop,Start,Terminate}Instances,CreateImage,CopyImage,DeregisterImage,DeleteSnapshot,RunInstances}` on `Resource:"*"` with no conditions — despite `list_ec2.md` showing every one of those actions supports `ec2:InstanceID`/`ResourceTag` scoping.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A principal holding exactly this documented policy can self-escalate to `AdministratorAccess`. → **Oracle:** `iam:SimulatePrincipalPolicy` for `CreateRole(RoleName=AWSSupport-EC2Rescue-canary)` → `AttachRolePolicy(…, PolicyArn=arn:aws:iam::aws:policy/AdministratorAccess)` → `PassRole`/`lambda:CreateFunction`. All `allowed` = confirmed. Live confirmation only with a canary role name, deleted immediately. **Severity: High** (non-admin → admin; Tier 2 reportable AWS-authored artifact, NOT a customer footgun).
- **Claim:** The role built "to reset i-AAAA" can terminate/image any instance and read any SSM parameter. → **Oracle:** `SimulatePrincipalPolicy` for `ec2:TerminateInstances`/`CreateImage` and `ssm:GetParameter` against a *different* instance ID / arbitrary parameter path under the scoped role. **Severity: Medium-High** (intra-account blast radius; chains to Lens T).
- **Claim:** The role trust policy allows confused-deputy assumption. → **Oracle:** confirm `AssumeRolePolicyDocument` = `Principal: ssm.amazonaws.com` with **no** `aws:SourceArn`/`SourceAccount` (contradicting `automation-setup-iam.md`'s own recommendation). **Severity: Medium** (hardening/doc-vs-practice gap).
**Doc evidence:** `AWSSupport-EC2RescueRole.json`; `automation-ec2reset.md`; `automation-awssupport-startec2rescueworkflow.md`; `automation-setup-iam.md`; `AmazonSSMAutomationRole` v9 JSON; `list_ec2.md` condition-key tables.
**Stop condition:** once the simulation returns `allowed` for the admin-attach chain, the finding is established — do not actually attach AdministratorAccess beyond a canary throwaway you delete.

### [P2] Lens T — Cross-service secret reachability (two independent chains)
**Background.** The feature generates secrets that come to rest in SSM Parameter Store under deterministic, instance/key-ID-keyed paths, governed by SSM's IAM — not by the EC2/automation permission that created them. SSM parameters have **no path-prefix condition key**, so scoping depends entirely on the reader's own `Resource` ARN string.
**Security Concern.**
- **Chain A (reset password):** EC2Rescue writes the Windows admin password to `/EC2Rescue/Password/<instance_id>` (`ec2rw-ssm.md`). A principal with a broad `ssm:GetParameter` grant (`parameter/*`, common for config-reading roles) and **none** of the EC2/automation reset permissions reads another instance's fresh admin password.
- **Chain B (private key):** For **CloudFormation-created** key pairs, AWS persists the RSA private key at `/ec2/keypair/{key_pair_id}` as a `SecureString` (`aws-resource-ec2-keypair.md`). `create-key-pairs.md`'s "Required IAM permissions" lists only `ssm:PutParameter`/`DeleteParameter` — **never `ssm:GetParameter`** — so the read path is outside EC2's `ec2:*KeyPair*` surface entirely. `key_pair_id` is enumerable via the unscopable `DescribeKeyPairs`.
**High-level Test Scenarios:**
- **Claim (A):** Principal denied every EC2/automation reset action but holding `ssm:GetParameter` on `parameter/*` reads `/EC2Rescue/Password/<id>`. → **Oracle:** `SimulatePrincipalPolicy` for `ssm:GetParameter` on that ARN under the scoped-deny role; then (canary) run the reset on a canary instance and read the parameter. **Severity: Medium-High.**
- **Claim (B):** Principal with explicit Deny on `ec2:CreateKeyPair`/`ImportKeyPair`/`DescribeKeyPairs`/`DeleteKeyPair` + broad `ssm:GetParameter` retrieves the plaintext PEM at `/ec2/keypair/<id>` and decrypts a `GetPasswordData` ciphertext. → **Oracle:** `aws ssm get-parameter --name /ec2/keypair/<id> --with-decryption` succeeds under the scoped role; plaintext PEM returned = confirmed. **Severity: High** (full admin-credential-chain recovery bypassing the entire EC2 key-pair access model).
- **Sub-claim (KMS, Lens H):** decrypt succeeds for a principal with **zero** `kms:*` permissions → confirms `alias/aws/ssm` `kms:ViaService` delegation is doing the authorizing, widening the population. The CFN `AWS::EC2::KeyPair` resource exposes **no `KmsKeyId` property** → a customer cannot require a CMK for this secret class.
- **Sub-claim (lifecycle):** direct `ec2:DeleteKeyPair` (not via CloudFormation stack delete) leaves `/ec2/keypair/<id>` live → stale private key survives. → **Oracle:** delete via `ec2 delete-key-pair`, then `ssm get-parameter` still returns the PEM.
**Doc evidence:** `ec2rw-ssm.md`; `aws-resource-ec2-keypair.md`; `create-key-pairs.md`; `delete-key-pair.md`; `list_ssm.md`; `list_ec2.md` (`DescribeKeyPairs` blank resource type).
**Stop condition:** retrieving one canary secret proves the chain — do not enumerate real fleet secrets.

### [P3] Lens F — userData task primitives as SYSTEM-level code exec (control-plane → OS root)
**Background.** EC2Launch v2's `executeScript`/`executeProgram`/`writeFile` tasks are invokable from the `UserData` stage with `runAs: localSystem|admin` (`ec2launch-v2-task-definitions.md`). `user-data.md`: *"User data scripts are run from the local administrator account when a random password is generated. Otherwise … from the System account."* No signing or allow-list on userData content is documented.
**Security Concern.** A principal with `ec2:StopInstances` + `ec2:ModifyInstanceAttribute(userData)` + `ec2:StartInstances` — and **no OS credential, no RDP, no key pair, no IAM role-passing** — plants a payload that runs as SYSTEM/Administrator on next boot. This needs *less* privilege than most PassRole escalations.
**High-level Test Scenarios:**
- **Claim:** The above three-API sequence yields SYSTEM code execution. → **Oracle (canary instance):** set `userData` to an `executeProgram, runAs: localSystem` block that writes a benign marker file / phones a canary beacon; confirm execution post-boot. The *mechanism* is already a documented design fact; the live test confirms no undocumented gate (signature/allow-list) intervenes. **Severity: Critical** (OS-admin from control-plane IAM alone).
- **Adjacent:** `writeFile` (PostReady/UserData) as arbitrary-file-write-as-SYSTEM — test writing into a service binary path / startup location.
- **Chain:** combine with Lens T to then read the generated password, or with the volume-swap path when userData is disabled.
**Doc evidence:** `ec2launch-v2-task-definitions.md`; `user-data.md`; `list_ec2.md` (`ec2:Attribute/${AttributeName}` is the only scoping key for userData).
**Stop condition:** a single benign-marker execution confirms the primitive.

### [P4] Lens Q — Offline-mounted config directory defeats the "anti-privesc" NTFS ACL
**Background.** `ec2launch-v2.md`: the agent-config directory's create permission is *"restricted to the administrator account to prevent privilege escalation."* The official reset procedures (`ResettingAdminPassword_EC2Launchv2.md` Steps 2-4; `ResettingAdminPassword_EC2Config.md` Steps 3-4) detach the root volume and mount it on a *temporary* instance to edit exactly that directory.
**Security Concern.** The ACL is an online-OS NTFS control; it is inert once the volume is offline-mounted. Anyone holding `ec2:DetachVolume`/`AttachVolume` + a second instance can read/write `agent-config.yml` / `LaunchConfig.json` / `config.xml` / `Sysprep.xml` — forcing `Ec2SetPassword: Enabled`, `setAdminAccount: Specify <attacker password>`, or reading the transient cleartext password field (Lens T channel 3).
**High-level Test Scenarios:**
- **Claim:** The "protected" directory is fully read/writable offline. → **Oracle (canary):** detach a canary instance's root volume, attach to a temp instance, read/modify `agent-config.yml`; reattach and confirm the agent honors the attacker-set `Specify` password on boot. **Severity: High.**
- **Note:** only EBS volume-level encryption would be orthogonal protection — neither reset procedure checks for it; the SSM automation explicitly **fails closed on encrypted root volumes** (`aws:assertAwsResourceProperty - Check the root volume is not encrypted`).
**Doc evidence:** `ec2launch-v2.md`; the two reset procedure pages; `ec2launch-v2-settings.md` / `ec2launch-sysprep.md` (cleartext-until-Sysprep window).

### [P5] Lens X — `GetConsoleOutput` vs `GetPasswordData` twin-action parity
**Background.** EC2Config's `SetPasswordAfterSysprep` *"outputs the encrypted password to the console"* (`ec2config-service.md`); EC2Launch v2 troubleshooting logs echo `<Password>{encrypted password}</Password>` (`ec2launchv2-troubleshooting.md`). Both are retrievable via `ec2:GetConsoleOutput`, a different action from `ec2:GetPasswordData` with a disjoint condition-key set.
**Security Concern.** An operator who scopes down / denies `GetPasswordData` believing the password is protected has not denied `GetConsoleOutput`, which yields the same ciphertext.
**High-level Test Scenarios:**
- **Claim:** `Deny GetPasswordData` + `Allow GetConsoleOutput` still exposes the password ciphertext. → **Oracle:** static — `SimulatePrincipalPolicy` shows the combination is non-contradictory and GetConsoleOutput remains allowed; on an instance where SetPasswordAfterSysprep/troubleshooting fired, the log contains the ciphertext. **Severity: Medium-High** (concrete IAM-authoring footgun around the password asset).
**Doc evidence:** `ec2config-service.md`; `ec2launchv2-troubleshooting.md`; `ec2-windows-passwords.md` (*"The console can only retrieve the default password"* — a narrower guarantee than it reads; Lens U).

### [P6] Lens E — Sysprep Administrator re-activation + protocol-scoped blank-password window
**Background.** `sysprep-using-ec2launchv2.md` Specialize phase runs, as synchronous command **order 1**, unconditionally: `net user Administrator /ACTIVE:YES /LOGONPASSWORDCHG:NO /EXPIRES:NEVER /PASSWORDREQ:YES`. It also documents *"during the first boot session after Windows Sysprep has run, there is a short period of time where RDP allows connections and the Administrator password is blank,"* mitigated by `BeforeSysprep.cmd` setting `fDenyTSConnections=1` (an **RDP-only** registry key).
**Security Concern.**
- The unconditional `/ACTIVE:YES` re-enables an Administrator account an operator may have intentionally disabled ("Do not set" password type) — a documented-guarantee-vs-enforcement gap.
- The blank-password-window mitigation blocks RDP (3389) but **not** SMB (445) or WinRM (5985/5986); if the SG permits those inbound, the blank admin password is reachable during the window the docs claim is shut off.
**High-level Test Scenarios:**
- **Claim:** A disabled Administrator is re-enabled on every generalize/specialize cycle. → **Oracle:** trigger a Sysprep cycle on a canary instance with Administrator pre-disabled; confirm it is active afterward. **Severity: Medium-High.**
- **Claim:** SMB/WinRM reach the blank-password account during the post-Sysprep window. → **Oracle (canary, live):** with SG allowing 445/5985, race the first boot after an AMI-creation/`.run-once`-triggered Sysprep and authenticate with a blank Administrator password over SMB/WinRM. **Severity: Medium** (narrow timing window; mitigation is protocol-specific, not credential-specific).
**Doc evidence:** `sysprep-using-ec2launchv2.md`; `ec2launch-v2-settings.md`.

### [P7] Lens A — Cross-instance IDOR and existence-enumeration oracles (intra-account)
**Background.** `AWSSupport-ResetAccess`/`StartEC2RescueWorkflow` take unconstrained `InstanceId`/`SubnetId` String params; `GetPasswordData` takes `InstanceId`. Ownership is only as strong as the caller's IAM `Condition` — which the AWS-authored artifacts omit (Lens R/S).
**Security Concern / Scenarios:**
- **Claim (intra-account IDOR):** With the documented (unconditioned) automation role, point the reset at an instance outside the caller's intended target. → **Oracle:** `SimulatePrincipalPolicy` for the automation's `ec2:*`/`ssm:*` actions against a *different* instance ID succeeds. **Severity: High intra-account.**
- **Claim (enumeration oracle):** `GetPasswordData` against a nonexistent vs existing-but-foreign-account instance ID returns distinguishable errors (per Variant-coverage: 500 vs 400 vs 200-empty). → **Oracle:** compare response/latency classes. **Severity: Low-Medium** (existence leak only). **Caveat:** `DryRunOperation`/`UnauthorizedOperation` is caller-IAM-only, **not** an ownership oracle.
- **Refuted-by-default (confirm the refutation):** cross-**account** `GetPasswordData`/reset — EC2/SSM ARNs are account-scoped; expect `AuthFailure`/`InvalidInstanceID.NotFound`. If it ever returns data → HARD STOP.
**Doc evidence:** `automation-awssupport-resetaccess.md`; `API_GetPasswordData.md`; `list_ec2.md`.

### [P8] Serial-console alternate admin path (adjacent, Lens A/U)
**Claim:** `ec2-instance-connect:SendSerialConsoleSSHPublicKey` grants admin-equivalent access to any instance the (often wildcarded) IAM policy names, once the account-level serial-console toggle is on. → **Oracle:** push a key to an instance outside the principal's intended scope. **Severity: High** if per-instance scoping is absent. Docs: *"Granting serial console permissions is equivalent to granting admin-level privileges"* and the account toggle defaults off (`configure-access-to-serial-console.md`, `ec2-serial-console.md`).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack | Lens | Priority |
|---|---|---|---|---|
| Non-admin self-escalates to account admin | `AWSSupport-EC2RescueRole.json` + inline policy text | Role-name-prefix scope only; no `iam:PolicyARN`/`PassedToService` condition | R/S/U | P1 |
| Reset-one-instance role controls all instances + all SSM params | `AmazonSSMAutomationRole` | None — `Resource:"*"`, no conditions | R/S | P1 |
| Read another instance's reset password w/o EC2 perms | SSM `/EC2Rescue/Password/<id>` | None at SSM condition-key level (no path key) | T | P2 |
| Recover CFN key-pair private key w/o `ec2:*KeyPair*` | SSM `/ec2/keypair/{id}` | None — read path outside EC2 IAM; `DescribeKeyPairs` unscopable | T/H | P2 |
| Control-plane IAM → SYSTEM code exec, no OS creds | `ModifyInstanceAttribute(userData)` + EC2Launch v2 UserData stage | No userData signing/allow-list; `ec2:Attribute/${…}` the only scope key | F | P3 |
| Read/write "protected" agent config offline | Detach/Attach volume + agent-config dir | NTFS ACL (inert offline); EBS encryption (unchecked) | Q | P4 |
| `GetConsoleOutput` yields password despite `GetPasswordData` deny | `SetPasswordAfterSysprep` / troubleshooting log | None — disjoint IAM actions, same asset | X | P5 |
| Intentionally-disabled Administrator re-enabled by Sysprep | `sysprep-using-ec2launchv2.md` Specialize order 1 | None — unconditional `net user /ACTIVE:YES` | E/U | P6 |
| Blank admin password over SMB/WinRM post-Sysprep | `BeforeSysprep.cmd` `fDenyTSConnections` | RDP-only; SMB/WinRM not addressed | E | P6 |
| Cross-instance (intra-account) reset/IDOR | Automation `InstanceId` param | Caller IAM condition (omitted in AWS artifacts) | A | P7 |
| Admin-equiv access via serial console | `SendSerialConsoleSSHPublicKey` | Account toggle (off) + optional per-instance IAM | A/U | P8 |

---

## 7. Out-of-Scope Risk Categories (state these confidently — keep the hunter off the shared-responsibility line)

- **Cross-ACCOUNT reach — not present.** Every artifact examined constructs ARNs with the caller's own account ID (`AWS::AccountId`); AWS resource-level IAM evaluation prevents naming another account's resource. If a cross-account identity ever appears → **HARD STOP + disclosure**, do not pursue as an in-scope lead.
- **Shared multi-tenant fleet — not present.** The EC2Rescue helper instance, temp VPC, Lambdas, and CFN stack are all created **in the customer's own account** ("How it works", `automation-ec2reset.md`). No control-ENI / control-VPC / shared-subnet construct → Lens D/V null here.
- **Customer-authored overly-broad IAM policies** (e.g. an ops role with `ssm:GetParameter` on `parameter/*`, or `ec2:GetPasswordData` on `Resource:"*"`) — the *composition* is the customer's footgun. The in-scope defect is only where the weak default ships in an **AWS-authored** artifact (Lens R/S/T/U). Keep that line sharp.
- **IMDS public-key retrieval** — returns the *public* key only (non-secret, by design). Not a breach.
- **Memory-safety / parser bugs inside EC2Launch/EC2Config/EC2Rescue binaries** — requires binary analysis, out of a documentation-only pass; flag for a separate effort.
- **Generic SigV4/TLS transport weaknesses** common to all EC2 Query-API actions (not specific to this feature) — Lens Y null here.
- **The SSH session content** once a serial-console session is established — in scope only up to "does the API authorize against the right instance."
- **Single-tenant self-DoS** (stopping your own instance) — not a finding.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did NOT fire, with pages named)

- **Lens B/PassRole — null for the three on-instance agents** (no API in `ec2launch-v2-task-definitions.md`, `ec2launch.md`, `ec2config-service.md`, or the three reset pages accepts a role ARN). **Fires** in the SSM-automation sub-surface (P1, confused-deputy trust policy).
- **Lens CC (metadata-as-identity) — null.** `ec2launch-v2.md`, `ec2launch-v2-settings.md`, `ec2launch-v2-task-definitions.md`, `user-data.md`, `ec2launch.md`, `ec2config-service.md`, `sysprep-using-ec2launchv2.md` — no agent treats IMDS/tags/network values as an authorization identity; trust model is "run whatever is in my local config/state."
- **Lens G (SSRF) — null.** Checked every EC2Launch v2 task type and all four automation runbook parameter lists; no field is dereferenced server-side as a URL/host (`OfflineScript` is inline base64; `S3BucketName`/`LogDestination` are upload destinations, not fetched). Key-pair pages: no fetched-URL field.
- **Lens D/V (data-plane↔control-plane, network segmentation) — null.** Single-instance, single-account; `automation-ec2reset.md`/`startec2rescueworkflow.md` explicit about account placement.
- **Lens M (shared-identifier interception) — null.** No session ID / JWT / MagicLink / presigned URL in key-pair creation, password retrieval, or decryption (checked `ec2-key-pairs.md`, `create-key-pairs.md`, `describe-keys.md`, `delete-key-pair.md`, `API_GetPasswordData.md`, `API_CreateKeyPair.md`, `API_ImportKeyPair.md`).
- **Lens Y (transport/signature) — mostly null.** No cleartext-HTTP / SigV2 / presigned variant for `GetPasswordData`/key-pair actions. One note: `GetPasswordData` returns ciphertext in the response body — CloudTrail *data-event* capture of responses (if enabled) would itself become a secret-at-rest concern; docs don't address this.
- **Lens K/W/FF/BB/DD (prompt injection, attestation, JWT/OIDC, routing/canonicalization, cache) — null.** No LLM, attestation-gated KMS, token validation, HTTP router/CDN/cache layer anywhere in this pipeline.
- **Lens AA (share/revoke) — null.** No RAM share / launch-permission / KMS-grant-on-toggle in this feature (the password-enabled/backup AMIs are left private; their persistence is a shared-responsibility note, §Lens U, not a revoke-lifecycle bug).
- **Lens X on `AttachVolume`/`DetachVolume` — null (no asymmetry); no `ebs:*` lower-level cousin** appears in this feature's documented permissions, so the direct-block-read bypass is not reachable via documented inputs. (The firing X case is `GetConsoleOutput`/`GetPasswordData`, P5.)

### Doc gaps — confirm surface before scoring
1. **Nested CFN/S3 template that provisions the helper-instance execution role** — referenced only as `arn:aws:s3:::awssupport-ssm.*/*.template`; content not published. The helper instance's *runtime* IAM role (distinct from the customer `AutomationAssumeRole`) is opaque to documentation. **Confirm what role runs the `OfflineScript` on the helper instance** — this is the one place internal AWS artifact is unreadable from docs and could itself be over-scoped.
2. **Which KMS key protects `/ec2/keypair/{id}` and `/EC2Rescue/Password/<id>`** — unstated. If default `alias/aws/ssm`, `kms:ViaService` delegation widens the reader population (Lens T sub-claim).
3. **SSM parameter cleanup on direct (non-CloudFormation) `ec2:DeleteKeyPair`** — only the CFN-managed delete path is documented as cleaning up the parameter.
4. **`/EC2Rescue/Password` vs `/EC2Rescue/Passwords`** path inconsistency between `ec2rw-ssm.md` prose (singular) and its own sample IAM policy (plural) — if the real path is singular, the printed least-privilege policy fails closed, pushing customers to widen `Resource` to `parameter/*` and amplifying Lens T.
5. **EC2Launch/EC2Config internal password-generation/encryption mechanism** (whether ciphertext transits the console/system log before `GetPasswordData` serves it) — partially evidenced via `SetPasswordAfterSysprep`; confirm the full flow before asserting.

---

## 9. Kill-chain summary (compose primitives — rate at the END of the chain)

- **Chain 1 (Critical, lowest privilege):** `ec2:StopInstances`+`ModifyInstanceAttribute(userData)`+`StartInstances` → SYSTEM code exec [P3] → from there, native OS admin, read any on-disk secret, pivot via the instance profile's role.
- **Chain 2 (High, read-only, highest confidence):** `ec2:DescribeKeyPairs` (unscopable) → enumerate `key_pair_id` → `ssm:GetParameter --with-decryption /ec2/keypair/{id}` [P2-B] → plaintext PEM → decrypt `GetPasswordData` ciphertext → Windows Administrator password — **all while every `ec2:*KeyPair*` action is denied.**
- **Chain 3 (High, AWS-artifact defect):** attach the documented "least-privilege" EC2Rescue policy → `CreateRole`+`AttachRolePolicy(AdministratorAccess)`+`PassRole`/`lambda:CreateFunction` [P1] → account admin.
- **Chain 4 (High):** `AWSSupport-ResetAccess`/offline volume swap [P4] → force `setAdminAccount: Specify <attacker pw>` or `Ec2SetPassword: Enabled` on the offline config → boot → known admin password → RDP.
- **Chain 5 (Medium-High):** scope down `GetPasswordData`, forget `GetConsoleOutput` [P5] → ciphertext still leaks via the console log.

**First move for the hunter:** P1 and P2 are both settleable with `iam:SimulatePrincipalPolicy` / a single read-only `ssm:GetParameter` and have documented root causes — start there (cheapest, highest confidence, no mutation). Then P3 on a canary instance.

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
