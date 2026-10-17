# EC2 Instance Troubleshooting — Attack Research Plan

Source of leads: hub `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html` and its ~20 child pages (online `.md` twins fetched live 2026-10-16; the `/work/aws-docs` mirror is missing most of these newer UserGuide pages, so pages were fetched online per project convention). Authoritative IAM surface: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` and `list_ec2-instance-connect.md` (read offline by targeted grep) plus `/tmp/list_ec2.md`. SSM runbook surface: `docs/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-*.md` (offline mirror).

Status: **documentation-derived hypotheses only. Nothing has been tested against a live AWS account.**

> **Scope / relationship to siblings.** This plan OWNS the **troubleshooting / direct-instance-access & recovery-tooling** surface of EC2: the serial console, console-output/screenshot retrieval, Windows admin-password retrieval & reset, EC2 Instance Connect (SSH key-push + EIC Endpoint), diagnostic interrupts, EC2Rescue/SSM-automation recovery, replace-root-volume, and boot-from-wrong-volume. It **cross-references** rather than restates:
> - `[[ec2-key-pairs-attack-research-plan]]` / `[[create-key-pairs-attack-research-plan]]` — key-pair lifecycle, which OWN the `GetPasswordData`→private-key decryption chain and key reuse; this plan develops the IAM-retrieval side only.
> - `[[attach-iam-role-attack-research-plan]]` / `[[iam-roles-for-amazon-ec2-attack-research-plan]]` — `iam:PassRole`, IMDS credential vending, and `ec2:ModifyInstanceAttribute(userData)` privesc, which this plan reuses for the SSM-automation/helper-instance role chain.
> - `[[security-iam-awsmanpol-attack-research-plan]]` — AWS-managed-policy audit, which OWNS Lens R; this plan points the AWSSupport-* automation role at it.
> - `[[ec2-security-iam-attack-research-plan]]` — the EC2 resource-level-permission model behind the "only the instance owner" guarantee.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity-if-true → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Policy-scoping / condition-key leads settle **read-only** via `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` (a condition key either applies to an action or it does not — no resource touched). Resolution/replay/ownership-vs-existence and interactive-session leads are **live-only** → hand to `aws-vuln-hunter` with a synthetic two-account / two-team canary (dummy instances, canary secrets in user-data).
- **DryRun is caller-IAM-only** (evaluated before resource resolution) — it is NOT an ownership/resolution oracle for the IDOR leads. Do not treat a DryRun pass as proof of cross-tenant reach.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — e.g. the serial-console SSH gateway returning another tenant's stream, an EC2Rescue helper assuming an AWS-fleet role, or an IMDS cred that resolves to an AWS service role — stop, preserve evidence, flag for AWS-Security disclosure. These are AWS-owned shared fleet hosts.

## 1. Pentest Objectives
Stated as concrete breach outcomes:
1. **Cross-tenant console read:** using only `ec2:GetConsoleOutput` / `ec2:GetConsoleScreenshot` on `Resource:"*"`, retrieve the boot log or screen framebuffer of an instance owned by a **different team or account** by naming its instance-id — and determine whether the gate is ownership (`UnauthorizedOperation`) or mere existence (`NotFound`), the latter also yielding an instance-id enumeration oracle. Chain to canary-secret leakage in cloud-init/user-data boot output.
2. **Serial-console reach beyond own instance:** prove whether `ec2-instance-connect:SendSerialConsoleSSHPublicKey` + the shared regional SSH gateway (`serial-console.ec2-instance-connect.<region>.aws`, username `<instance-id>.port0`) ever routes a session to an instance the caller does not own, or whether the 60-second pushed key is replayable/reusable.
3. **Narrow-action → root escalation:** demonstrate that `ec2-instance-connect:SendSerialConsoleSSHPublicKey` (or `SendSSHPublicKey` with `ec2:osuser=root`) grants full root/admin OS access from a permission that reads like "connect".
4. **Disk-access boundary bypass:** prove that `ec2:DetachVolume`+`ec2:AttachVolume`+`ec2:RunInstances` (the AWS-documented offline recovery / EC2Rescue path) grants full read/write of another instance's filesystem **without** the key pair or Windows password — i.e. that EBS-level IAM, not OS credentials, is the real authorization boundary.
5. **Automation IAM-artifact escalation & land-grab:** prove the AWS-authored `AWSSupport-StartEC2RescueWorkflow` required policy enables `CreateRole`+`AttachRolePolicy(AdministratorAccess)` self-escalation; sweep `awssupport-ssm.<region>` buckets for an unclaimed name (CFN/Lambda land-grab into the victim account); and read `/EC2Rescue/Password/<id>` admin passwords account-wide. Route AWS-authored artifacts to `aws-security` (Tier 2).
6. **Availability kill-switch:** prove `ec2:SendDiagnosticInterrupt` deterministically crashes a running instance from a single narrow IAM grant, independent of the serial-console account toggle.
7. **Boot-from-wrong-volume takeover:** attach a volume carrying a colliding `LABEL=/` / UUID and show the next reboot boots the attacker volume as root.

## 2. Components, Assets, and Design

**Customer-facing interfaces.**
- EC2 **control-plane API** (SigV4) / CLI / console for `GetConsoleOutput`, `GetConsoleScreenshot`, `GetPasswordData`, `SendDiagnosticInterrupt`, `EnableSerialConsoleAccess`/`DisableSerialConsoleAccess`/`GetSerialConsoleAccessStatus`, `CreateReplaceRootVolumeTask`, `RebootInstances`.
- **EC2 Instance Connect API** (`ec2-instance-connect:*`): `SendSSHPublicKey`, `SendSerialConsoleSSHPublicKey`, `OpenTunnel`.
- **Serial-console SSH gateway** — AWS-owned, per-region, **multi-tenant shared fleet**. Hostname `serial-console.ec2-instance-connect.<region>.aws` (older) / `ec2-serial-console.<region>.api.aws` (newer), port 22. SSH username embeds the instance id: `<instance-id>.port0`. **Explicitly outside the VPC** — "does not use the instance security group or the subnet network ACL to authorize traffic" (`configure-access-to-serial-console`). Browser proxy: `prod.<region>.oneclickv2-proxy.ec2.aws.dev:443`.
- **EC2 Instance Connect Endpoint (EIC Endpoint)** — AWS-managed identity-aware TCP proxy (an ENI in a chosen subnet) tunnelling SSH/RDP from an IAM caller into private-IP instances with no public IP / IGW.
- **SSM Automation** runbooks `AWSSupport-ExecuteEC2Rescue`, `AWSSupport-RunEC2RescueForWindowsTool`, `AWSSupport-StartEC2RescueWorkflow`, `AWSSupport-TroubleshootRDP` — orchestrate recovery.

**Processes / fleets behind the interfaces.**
- Per-instance **virtual serial port** (`ttyS0`/`COM1`), independent of networking.
- On-instance agents **EC2Launch / EC2Launch v2 / EC2Config** generate the random Windows Administrator password at first boot, encrypt it with the launch key pair's public key, and emit it to console output.
- **EC2Rescue** tool runs either in-OS or **offline on a helper instance**.
- **Nitro hypervisor** mediates console-screenshot/output capture and the diagnostic-interrupt NMI.

**Accounts / network ownership.**
- Serial-console SSH gateway and EIC Endpoint proxy are **AWS-service-account owned**, shared across tenants → the highest-value isolation zones.
- The EC2Rescue helper instance and its new VPC are created **in the customer's own account** (noisy-neighbour / in-account IDOR, not cross-tenant) unless the automation role is cross-account.

**Resource identifiers.** `instance-id` = `i-` + 17 hex (not secret; routinely leaked in logs/tickets/CI output → enumerable targets for the IDOR leads). `replace-root-volume-task/<id>`. The serial-console session is addressed purely by `<instance-id>.port0` in the SSH username.

**Identity / credentials.**
- Console/password/interrupt APIs: **SigV4 IAM only**.
- Serial console: IAM gates the *key push*; after push, "the SSH connection is **not** subject to the IAM policies" — a 60-second ephemeral key, then up to a ~1-hour session (1 active session/instance, 30s teardown).
- Windows password: ciphertext under the **key pair public key**; private key is the sole decryption secret.
- EC2Rescue SSM: `AutomationAssumeRole` ARN, or — **if omitted — the permissions of the user who starts the runbook** (`automation-awssupport-executeec2rescue`).

**Roles / privilege levels.** Account-wide serial-console toggle (`ec2:EnableSerialConsoleAccess`, no resource type); per-instance key push (`ec2-instance-connect:SendSerialConsoleSSHPublicKey`, instance-scoped); `ec2:osuser` string condition on `SendSSHPublicKey`; AWSSupport automation execution role.

**Pipeline (ASCII).**
```
                        ┌─────────────── EC2 control plane (SigV4 / IAM) ───────────────┐
caller ── GetConsoleOutput/Screenshot ─► instance* (IAM resource-ARN scope) ─► Nitro ─► buffered boot log / JPG framebuffer
caller ── GetPasswordData ────────────► instance* ─► ciphertext(adminpw, keypair.pub)   (decrypt needs private key — separate gate)
caller ── SendDiagnosticInterrupt ────► instance* ─► NMI ─► kernel panic / BSOD (crash+reboot)
caller ── EnableSerialConsoleAccess ──► ACCOUNT-WIDE toggle (no resource, ec2:Region only)

caller ── ec2-instance-connect:SendSerialConsoleSSHPublicKey(instance) ─┐  60s key TTL
                                                                        ▼
      ssh <instance-id>.port0 @ serial-console.ec2-instance-connect.<region>.aws  (AWS shared fleet, OUTSIDE VPC, no SG/NACL)
                                                                        ▼
                                                        root-capable serial shell (~1h, NOT IAM-mediated)

caller ── ec2-instance-connect:SendSSHPublicKey(instance, ec2:osuser) ─► 60s key in IMDS ─► sshd AuthorizedKeysCommand ─► OS login
caller ── ec2-instance-connect:OpenTunnel(EIC-Endpoint) ─► AWS-managed proxy ENI ─► private-IP instance in VPC

caller ── ssm:StartAutomationExecution(AWSSupport-ExecuteEC2Rescue) ─► stop target ─► snapshot/AMI ─► DETACH root vol
                                                                        ▼
                              ATTACH target root vol as data vol to NEW helper instance (new VPC, same AZ)
                                                                        ▼
                   full R/W of target filesystem w/o key pair or password; logs ─► LogDestination S3 bucket
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller w/ `ec2:GetConsole*` on `Resource:"*"` | Another team/account's instance screen & boot log | name foreign `instance-id` | Returned JPG/boot-text for an instance the caller doesn't own = **cross-tenant IDOR**. `NotFound` vs `UnauthorizedOperation` divergence = existence-enumeration oracle. The doc's "**Only the instance owner can access the console output**" guarantee is the thing to break. |
| Caller w/ `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | A serial shell on an instance it doesn't own | push key for foreign `instance-id`; connect via shared gateway `<instance-id>.port0` | A serial stream from a foreign instance, OR routing confusion on the shared gateway = **Critical cross-tenant OS access**. Gateway is AWS-owned → HARD STOP if another account's stream appears. |
| Holder of the narrow "send key" action | root/admin OS of the instance | serial console / `ec2:osuser=root` | Interactive root shell obtained from an IAM grant that names only a "connect"/"send-key" action = **privilege under-approximation**. |
| Caller w/ `ec2:AttachVolume`+`DetachVolume`+`RunInstances` (NOT the OS user) | Full filesystem of a target instance | AWS-documented offline recovery: detach root vol → attach to helper → mount/edit | Reading/writing the target's disk (another team's secrets, `authorized_keys`, registry hive) without ever holding the key pair or password = **the real disk-access boundary is EBS IAM, not OS creds**. |
| Caller w/ only `ec2:SendDiagnosticInterrupt` | Availability of a running instance | NMI → kernel panic | Instance crashes/reboots from one narrow grant, independent of serial-console toggle = availability kill-switch (intra-account cross-team if `Resource:"*"`). |
| Principal holding only the AWSSupport automation role | Resources/accounts beyond the one instance | `AutomationAssumeRole` default = caller's perms; wildcard PassRole/resource; `LogDestination` S3 | Helper assumes a role / writes logs to a bucket the artifact's description implies it cannot = Lens R/B/T escalation (route `aws-security` if AWS-authored & uneditable). |
| Attacker-controlled data volume | Root of a victim instance | colliding `LABEL=/` / UUID resolved by initramfs at reboot | Foreign volume mounts as `/` on reboot = root takeover before real OS init. |
| Account-level `SerialConsoleAccessEnabled=false` | A live serial session | IAM key-push while flag false | Session established while account flag is `false` = account toggle is non-enforcing (defence-in-depth collapses to the single IAM gate). |
| Any customer surface | AWS service plane | serial-console gateway / EIC proxy / automation fleet identity | **HARD STOP** — preserve, disclose. |

## 4. API / Interface Inventory

| Name | Namespace / method | Mutating | Internet-callable | Resource binding (IAM) | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `GetConsoleOutput` | `ec2` / SigV4,CLI | No (Read) | Yes | **`instance*`** + `aws:ResourceTag`/`ec2:ResourceTag` + many `ec2:*` keys | holders of `ec2:GetConsoleOutput` on the instance | returns buffered boot/serial log; `--latest` on Nitro; **"Only the instance owner can access the console output"** (UserGuide) — mechanism unspecified |
| `GetConsoleScreenshot` | `ec2` / SigV4,CLI | No (Read) | Yes | **`instance*`** + tags + **`ec2:NewInstanceProfile`** (spurious) | holders of `ec2:GetConsoleScreenshot` | **JPG ≤100KB**, base64; works running or crashed; `WakeUp=true` injects a keystroke; **no owner-only sentence in its API ref** (asymmetry vs Output). Condition-key set carries `ec2:NewInstanceProfile`, irrelevant to a read → inert-Deny trap (Lens S) |
| `GetPasswordData` | `ec2` / SigV4,CLI | No (Read) | Yes | **`instance*`** + tags | holders of `ec2:GetPasswordData` | returns ciphertext(adminpw) under keypair.pub; retrieval gate ≠ decryption gate |
| `SendDiagnosticInterrupt` | `ec2` / SigV4,CLI | **Yes (Write)** | Yes | **`instance*`** + tags | holders of `ec2:SendDiagnosticInterrupt` | NMI → panic/BSOD, "could lead to the loss of data"; Nitro Intel/AMD (not Graviton); no documented rate-limit/approval |
| `EnableSerialConsoleAccess` | `ec2` / SigV4,CLI | **Yes (Write)** | Yes | **none (account-wide)** — only `ec2:Region` | holders of the action | flips serial console for **all** instances in the account/region; no tag/resource scoping |
| `DisableSerialConsoleAccess` | `ec2` | **Yes** | Yes | none / `ec2:Region` | holders of the action | account-wide |
| `GetSerialConsoleAccessStatus` | `ec2` | No | Yes | none / `ec2:Region` | holders of the action | account-wide read |
| `SendSerialConsoleSSHPublicKey` | **`ec2-instance-connect`** / SigV4,CLI | **Yes** | Yes | **`instance*`** + `aws:ResourceTag`/`ec2:ResourceTag` (**no `ec2:osuser`**) | holders of the action on the instance | pushes 60s key; post-push session **not IAM-mediated**; "= admin-level privileges on the instance" (Windows). **No `ec2:osuser` key** — cannot restrict which serial login |
| `SendSSHPublicKey` | **`ec2-instance-connect`** | **Yes** | Yes | **`instance*`** + **`ec2:osuser`** + tags | holders of the action | 60s key in IMDS; `ec2:osuser` is a free-form string (can be `root` on RHEL/SUSE) |
| `OpenTunnel` | **`ec2-instance-connect`** | **Yes** | Yes | **EIC-Endpoint ARN** + `ec2-instance-connect:remotePort`/`privateIpAddress`/`maxTunnelDuration`, `aws:SourceIp` | holders of the action on the endpoint | tunnels into private subnet; instance scoping is only via optional `privateIpAddress` condition |
| `CreateReplaceRootVolumeTask` | `ec2` | **Yes** | Yes | **`instance*`,`image`,`snapshot`,`volume`,`replace-root-volume-task*`** | holders of the action + resource perms on AMI/snapshot/volume | swaps root EBS in place (reboots); existing-volume path requires `available` + same-AZ + encryption-compat, **no explicit owner check on the volume beyond state** |
| `AWSSupport-ExecuteEC2Rescue` (SSM) | `ssm` automation | **Yes** | Yes (API) | automation doc + `AutomationAssumeRole` | `ssm:StartAutomationExecution` holder | top-level entry; delegates to `StartEC2RescueWorkflow`; stops target, snapshots/AMIs it; `AutomationAssumeRole` defaults to **caller's perms**; `LogDestination` = caller-named S3 bucket |
| `AWSSupport-StartEC2RescueWorkflow` (SSM) | `ssm` automation | **Yes** | Yes (API) | required policy: `iam:CreateRole`/**`AttachRolePolicy` (no PolicyArn cond)**/`PassRole`/`CreateInstanceProfile` on `AWSSupport-EC2Rescue-*`; `s3:GetObject` on **`awssupport-ssm.*/*.template|*.zip`** (name-only); `ec2:*VPC/Subnet/Route*`, `lambda:*` on `*` | holder of the required policy (+ recommended `AmazonSSMAutomationRole`) | **the real offline mechanism**: builds CFN stack + Lambda + IAM role, launches helper in **customer account**, detaches target root vol, attaches to helper, runs base64 `OfflineScript`. Lens R/S/EE epicentre |
| `AWSSupport-RunEC2RescueForWindowsTool` (SSM) | `ssm` automation/Distributor | **Yes** | Yes (API) | AWS **Example Policy = `Resource:"*"`** for `ssm:PutParameter`,`s3:PutObject`,`kms:Encrypt` | holder | in-OS `ResetAccess`/`CollectLogs`/`FixAll`; writes reset admin pw to SSM param |
| SSM Parameter `/EC2Rescue/Password/<instance-id>` | `ssm` | n/a (store) | Yes | `ssm:GetParameter`/`PutParameter` + `kms:Decrypt`; path enumerable | holders of the param read + KMS decrypt | KMS-encrypted local-Administrator password; predictable path → account-wide harvest if scoped `*`/`/EC2Rescue/Password/*` |
| KDNET debug channel | guest `bcdedit` + UDP 50000–50039 | n/a (OS) | network | SG-reachable UDP range; auth = shared `key:` only | anyone who reaches the port + knows the key | full kernel R/W; key in cleartext BCD store (offline-recoverable) |
| SAC `SAC>` commands | serial console | **Yes** (OS-level) | via serial console | gated only by serial-console IAM | serial-console caller | `i`/`k`/`l`/`m`/`r`/`crashdump`/`shutdown`/`restart`/`d` "do not require you to sign in" |

## 5. Recommended Areas of Focus

### 5A — Cross-tenant / cross-team console disclosure (Lens A, U, X)  — **PRIORITY 1**
**Background.** `GetConsoleOutput` and `GetConsoleScreenshot` return the literal boot log and screen framebuffer of an instance, named only by `instance-id`. Both bind the `instance*` resource type, so IAM *can* scope them by ARN/tag — but legacy/broad policies routinely grant `Resource:"*"`. Instance-ids are not secret.
**Security Concern.** The UserGuide asserts "**Only the instance owner can access the console output**" but neither the UserGuide nor the API reference describes the *mechanism*; `GetConsoleScreenshot`'s API ref carries **no** owner-only sentence at all (doc asymmetry). Boot output routinely contains cloud-init/user-data secrets; a screenshot can show a logged-in desktop or a password prompt.
**High-level Test Scenarios.**
- *Claim:* a principal with `ec2:GetConsoleOutput`/`GetConsoleScreenshot` on `Resource:"*"` retrieves a **cross-account** instance's output/screenshot by supplying its id. → *Oracle:* data returned = **Critical IDOR**; `UnauthorizedOperation` = ownership enforced; `InvalidInstanceID.NotFound` on a known-live foreign id = existence-only check + enumeration oracle. → *Cost:* 2 accounts, 1 call. → *Severity:* **Critical** (cross-tenant secret disclosure).
- *Claim:* within one account, a team-A-scoped principal (tagged ABAC) reads team-B's screen because the policy wildcards the resource. → *Oracle:* B's JPG returned. → *Severity:* **High**.
- *Claim:* `GetConsoleOutput` buffered boot text contains a canary secret planted in verbose user-data. → *Oracle:* canary appears in `--latest` output → confirms the IDOR→credential-theft chain. → *Severity:* **Critical** when chained.
- *Claim (Lens X parity):* `GetConsoleScreenshot` and `GetConsoleOutput` enforce ownership with different strictness / error taxonomy (only Output documents owner-only). → *Oracle:* divergent error codes or one returns data where the other denies. → *Severity:* Medium–High.
- *Claim (Lens S):* a Deny keyed on `ec2:NewInstanceProfile` (present only on `GetConsoleScreenshot`'s key set, semantically a RunInstances/Associate key) is **inert** against a screenshot read. → *Oracle:* `SimulateCustomPolicy` shows the Deny never matches `GetConsoleScreenshot`. → *Severity:* Informational (AWS-owned IAM-model inconsistency).
**Doc evidence:** `troubleshoot-unreachable-instance` (owner-only sentence; JPG ≤100KB; `WakeUp`); `list_ec2.md` action detail (resource `instance*`; `ec2:NewInstanceProfile` only on Screenshot). **Severity-if-true:** Critical (cross-account) / High (cross-team).

### 5B — Serial console: shared-gateway isolation & narrow-action→root (Lens A, V, E, U)  — **PRIORITY 1**
**Background.** Serial console access is off by default; an org enables it account-wide (`EnableSerialConsoleAccess`, no resource scope) and grants `ec2-instance-connect:SendSerialConsoleSSHPublicKey` per instance. Connection is to an **AWS-owned, per-region, multi-tenant SSH gateway**, addressed by `<instance-id>.port0`, **outside the VPC** (no SG/NACL). After the 60-second key push the live session is **not IAM-mediated**.
**Security Concern.** Routing to the right instance depends on the username + pushed-key handshake, not network isolation. The gating IAM action is named like "send a key" but "= admin-level privileges on the instance". `SendSerialConsoleSSHPublicKey` has **no `ec2:osuser`** condition key — nothing restricts which login the serial session reaches.
**High-level Test Scenarios.**
- *Claim:* pushing a key for owned instance A then `ssh <B-id>.port0` (B foreign) against the same regional gateway with A's key routes to or leaks B's serial stream. → *Oracle:* any B stream / routing or error-timing divergence. **Gateway is AWS-owned → HARD STOP** if a foreign stream appears. → *Severity:* **Critical**.
- *Claim:* the 60-second TTL is enforced server-side and the key is single-use. → *Oracle:* connect >60s later, or reconnect after teardown without re-push → auth failure confirms; success = replayable-key weakness. → *Severity:* Medium.
- *Claim:* `ec2-instance-connect:SendSerialConsoleSSHPublicKey` scoped to one instance, with no other EC2/SSM/compute permission, yields an interactive root-capable shell. → *Oracle:* root serial shell obtained. → *Severity:* **High** (privilege under-approximation / least-privilege-review blind spot).
- *Claim (Lens U):* `SendSerialConsoleSSHPublicKey` succeeds while account `SerialConsoleAccessEnabled=false`. → *Oracle:* session established with flag false → account toggle non-enforcing. → *Severity:* Medium (defence-in-depth collapse).
**Doc evidence:** `configure-access-to-serial-console` ("outside of the VPC … does not use the instance security group"; "admin-level privileges"); `connect-to-serial-console` (`<instance-id>.port0`, gateway hostnames, 60s, 1-session); `list_ec2-instance-connect.md` (no `ec2:osuser` on serial action). **Severity-if-true:** Critical (gateway isolation) / High (privesc).

### 5C — EBS offline-recovery: the real disk-access boundary (Lens A, R, B)  — **PRIORITY 1**
**Background.** Every AWS-documented offline recovery path (lost SSH key, reset Windows password, fix RDP/firewall, DSRM) and the `AWSSupport-ExecuteEC2Rescue` runbook work by **detaching the target's root volume and attaching it as a data volume to a separate/helper instance**, then editing `authorized_keys` or the registry hive.
**Security Concern.** This silently shifts the authorization boundary from "OS credential / key pair" to "`ec2:AttachVolume`+`ec2:DetachVolume` IAM on the volume." Anyone holding those actions — even a principal that could never SSH/RDP in — gets full read/write of the instance's filesystem, defeating the key pair and the Windows password entirely. `AWSSupport-ExecuteEC2Rescue` additionally defaults `AutomationAssumeRole` to the **caller's own permissions** and launches the helper in a new VPC.
**High-level Test Scenarios.**
- *Claim:* a principal with `ec2:DetachVolume`/`AttachVolume`/`RunInstances` but no OS access reads a target's secrets by attaching its root volume to a helper. → *Oracle:* canary file / shadow / registry hive read from the helper. → *Severity:* **Critical** (by design; IDOR-shaped privesc — audit whether these grants are scoped as tightly as `GetPasswordData`/`SendSSHPublicKey`).
- *Claim (Lens R/S):* the AWSSupport automation's AWS-authored role / policy pairs `iam:PassRole` or `ec2:RunInstances`/`AttachVolume` with wildcard resource and no ownership condition → self-escalation. → *Oracle:* `SimulatePrincipalPolicy` under a role holding exactly the artifact performs an action its description implies it cannot. **Route `aws-security` if the policy is AWS-managed/uneditable (Tier 2); customer-authored → footgun/out-of-scope.** → *Severity:* High (non-admin→admin) / Medium–High (cross-workload reach).
- *Claim (Lens B):* omitting `AutomationAssumeRole` runs the runbook with the starting user's perms, broadening what the helper can touch (confused-deputy on the recovery path). → *Oracle:* helper performs an action the automation doc scopes away. → *Severity:* Medium–High.
**Doc evidence:** `TroubleshootingInstancesConnecting` (lost-key offline procedure); `troubleshoot-connect-windows-instance` / `win-ts-common-issues` (registry hive edit, DSRM); `automation-awssupport-executeec2rescue` (`AutomationAssumeRole` default = caller perms; new VPC/helper; stop+AMI). **Severity-if-true:** Critical.

### 5D — EC2 Instance Connect: `ec2:osuser`, 60s race, EIC-Endpoint lateral reach (Lens E, C/M, V)  — PRIORITY 2
**Background.** `SendSSHPublicKey` pushes a 60-second key into IMDS; `ec2:osuser` string condition names the OS login; the EIC Endpoint is an AWS-managed proxy ENI tunnelling into private subnets.
**Security Concern.** `ec2:osuser` is a free-form string, not an OS-privilege check — it can be `root` (RHEL/SUSE default). The 60s key is readable by any IMDS reader during the window (SSRF/IMDSv1 chain). `OpenTunnel` scoping to a specific instance is only via the optional `privateIpAddress`/`remotePort` conditions; omitted, the endpoint can reach any routable private IP.
**High-level Test Scenarios.**
- *Claim:* a policy with `ec2:osuser=root` + `SendSSHPublicKey` grants root SSH — an apparently-narrow condition equals granting root. → *Oracle:* root login succeeds. → *Severity:* High (doc gives no warning against privileged `osuser`).
- *Claim:* an SSRF/IMDSv1 read on the target captures the pushed key within 60s and hijacks the session; or two overlapping `SendSSHPublicKey` callers race (overwrite vs multi-key — undocumented). → *Oracle:* second party authenticates with the pushed key. → *Severity:* Low–Medium (needs an IMDS-read primitive).
- *Claim:* an `OpenTunnel` policy with the endpoint ARN but no `privateIpAddress` condition reaches arbitrary private IPs in the VPC. → *Oracle:* tunnel completes to an instance other than the intended one. → *Severity:* High (lateral movement).
**Doc evidence:** `ec2-instance-connect-configure-IAM-role` (`ec2:osuser`, default-user table incl. `root`); `connect-linux-inst-eic`/`permissions-for-ec2-instance-connect-endpoint` (OpenTunnel conditions, 60s). **Severity-if-true:** High.

### 5E — Diagnostic interrupt as availability kill-switch (Lens L)  — PRIORITY 2
**Background.** `SendDiagnosticInterrupt` sends an unknown NMI to a Nitro Intel/AMD instance.
**Security Concern.** A single IAM-gated, no-confirmation Write action deterministically crashes a running instance ("could lead to the loss of data"); no documented rate limit, approval, or dependency on the serial-console toggle. `instance*`-scoped, so a `Resource:"*"` grant is account-wide.
**High-level Test Scenarios.**
- *Claim:* a principal with only `ec2:SendDiagnosticInterrupt` on `Resource:"*"` crashes any (incl. another team's) running instance. → *Oracle:* target panics/reboots; `StatusCheckFailed`. → *Severity:* High (intra-account cross-team DoS); single-tenant self-DoS = out-of-scope.
**Doc evidence:** `diagnostic-interrupt` (crash/reboot warning); `list_ec2.md` (`instance*`, Write). **Severity-if-true:** High (cross-team) / out-of-scope (self).

### 5F — Boot-from-wrong-volume via label/UUID collision (Lens BB)  — PRIORITY 2
**Background.** Linux initramfs selects root by `/etc/fstab` `LABEL=/` or UUID (resolved by `blkid`/`e2label`) — AWS does not validate this. Any snapshot/clone of a root volume shares its UUID.
**Security Concern.** Attaching a secondary volume with a colliding `LABEL=/` or UUID can cause the next reboot to boot the foreign volume as root, giving its init first code execution.
**High-level Test Scenarios.**
- *Claim:* a data volume built from a shared/public snapshot with `LABEL=/` becomes `/` on reboot. → *Oracle:* `mount` / canary shows the foreign volume mounted as root. → *Preconditions:* victim attaches a crafted/foreign volume (malicious shared snapshot or marketplace-AMI companion volume) + a reboot. → *Severity:* High (root takeover; supply-chain vector via shared snapshots/AMIs).
- *Claim:* `CreateReplaceRootVolumeTask`'s existing-volume path accepts a volume without an owner check beyond state/AZ/encryption. → *Oracle:* replace with an attacker-prepared volume the policy didn't intend. → *Severity:* Medium–High.
**Doc evidence:** `instance-booting-from-wrong-volume` (label/UUID collision); `list_ec2.md` `CreateReplaceRootVolumeTask` resource set. **Severity-if-true:** High.

### 5G — EC2Rescue / SSM-automation IAM-artifact audit & land-grab (Lens R, S, B, EE, T, U)  — **PRIORITY 1**
**Background.** The real offline mechanism is `AWSSupport-StartEC2RescueWorkflow` (called by `AWSSupport-ExecuteEC2Rescue`): it builds a CloudFormation stack (VPC, Lambda `AWSSupport-EC2Rescue-*`, IAM role+instance-profile `AWSSupport-EC2Rescue-*`), launches a helper instance **in the customer's account**, detaches the target root volume, attaches it to the helper, runs a base64 `OfflineScript`, then unwinds. The CFN template + Lambda zip are fetched from AWS-owned `awssupport-ssm.*` S3 buckets. `AWSSupport-RunEC2RescueForWindowsTool` (in-OS path) stores the reset local-Administrator password in SSM Parameter `/EC2Rescue/Password/<instance-id>` (KMS-encrypted).
**Security Concern.** The **AWS-authored "required IAM permissions"** for `StartEC2RescueWorkflow` pair `iam:CreateRole` + `iam:AttachRolePolicy` (scoped only to the resource-name prefix `AWSSupport-EC2Rescue-*`, **with no `PolicyArn` condition**) + `iam:PassRole` + `iam:CreateInstanceProfile`/`AddRoleToInstanceProfile`, and recommend attaching the broad `AmazonSSMAutomationRole` alongside. The S3 source ARN `arn:aws:s3:::awssupport-ssm.*/*.template|*.zip` trusts the bucket **name only** (S3 ARNs carry no account id). The Windows runbook's own **"Example Policy" uses `Resource:"*"`** for `ssm:PutParameter`, `s3:PutObject`, `kms:Encrypt`, while a sibling page scopes `PutParameter` to the per-instance path. These are AWS-authored, copy-verbatim artifacts → **in scope, Tier 2, route `aws-security`.**
**High-level Test Scenarios.**
- *Claim (Lens R/S — Critical):* a principal holding **only** the documented `StartEC2RescueWorkflow` policy + `AmazonSSMAutomationRole` self-escalates: `CreateRole AWSSupport-EC2Rescue-x` → `AttachRolePolicy AdministratorAccess` (unconstrained PolicyArn) → `CreateInstanceProfile`/`AddRoleToInstanceProfile` → launch/associate an instance with that profile → harvest admin IMDS creds. → *Oracle:* `SimulatePrincipalPolicy` shows `AttachRolePolicy` accepts `AdministratorAccess`; live confirm under a role holding exactly the artifact. → *Severity:* **Critical** (non-admin→admin privesc from a "just run EC2Rescue" grant).
- *Claim (Lens EE — Critical):* an `awssupport-ssm.<region>` bucket is unclaimed in some (newer/opt-in) region; pre-registering it serves an attacker CloudFormation template / Lambda zip that the automation fetches and executes in the victim account. → *Oracle:* unauthenticated bucket-existence/`GetBucketLocation` sweep across all regions; any unclaimed name is the land-grab target. → *Severity:* **Critical** (arbitrary CFN/Lambda exec in victim account). *Doc-gap:* exact region→bucket-name construction not public — confirm first.
- *Claim (Lens U/T — High):* following the Windows runbook's `Resource:"*"` Example Policy verbatim lets the role `PutParameter` on arbitrary SSM paths and `PutObject` to arbitrary buckets, far beyond the EC2Rescue naming convention. → *Oracle:* attach the example policy to a scoped role; `SimulateCustomPolicy` confirms writes outside `/EC2Rescue/*`. → *Severity:* High (over-permissioning + doc-vs-doc inconsistency; AWS-owned).
- *Claim (Lens T — High):* `/EC2Rescue/Password/<instance-id>` is enumerable; a principal with `ssm:GetParameter`+`kms:Decrypt` scoped `/EC2Rescue/Password/*` (or `*`, per the Example Policy) reads **every** rescued instance's local-admin password. → *Oracle:* enumerate instance-ids, `GetParameter --with-decryption` each path. → *Severity:* High (lateral credential harvesting).
- *Claim (Lens B):* omitting `AutomationAssumeRole` runs the workflow with the starting user's own perms (confused deputy on recovery). → *Oracle:* helper performs an action the automation doc scopes away. → *Severity:* Medium–High.
- *Claim (Lens Q — High/low-likelihood):* `ec2rl` tarball + `.sha256` + `.sig` + GPG key all fetch from the same AWS host over `curl` and GPG verification is labelled "(Optional)" → tampered tool if that bucket is ever compromised. → *Oracle:* not customer-testable; supply-chain note. → *Severity:* High-impact / low-likelihood.
- *Claim (footgun, note only):* `LogDestination`/`S3BucketName` is "in your account" with only a prose bucket-policy warning → collected logs (`/collect:all`) can land in a misconfigured/public bucket. → **customer-configuration risk**, flagged not as an AWS-side bug.
**Doc evidence:** `automation-awssupport-startec2rescueworkflow` (CreateRole/AttachRolePolicy no-PolicyArn, `awssupport-ssm.*/*.template|*.zip`, helper/CFN); `automation-awssupport-runec2rescueforwindowstool` (`Resource:"*"` Example Policy) vs `ec2rw-ssm` (scoped `/EC2Rescue/Passwords/{instanceid}`); `ec2rl_install` (optional GPG); `automation-awssupport-executeec2rescue` (`LogDestination`). **Severity-if-true:** Critical (privesc / land-grab) / High (secret harvest).

### 5H — KDNET kernel-debug channel: shared-key weakness & offline key recovery (Lens Y, A, T)  — PRIORITY 2
**Background.** `troubleshoot-windows-with-kdnet` configures a UDP 50000–50039 kernel-debug channel between a debug host and target via `bcdedit /dbgsettings net hostip:… port:… key:…`. The only authentication for full kernel read/write is the shared `key:` + network reachability.
**Security Concern.** The doc prints a literal example key; the key is stored in cleartext in the on-disk BCD store (recoverable via the EC2Rescue offline-volume primitive, 5C); cleanup (`/debug off`) is manual/optional.
**High-level Test Scenarios.**
- *Claim:* an operator left the doc's example key (`1kdnet2keys3.4kdnet5keys6.7kdnet8keys9.10kdnet11ke`) or a weak key, and UDP 50000–50039 is reachable from a co-SG instance → WinDbg attach = full kernel R/W. → *Oracle:* connect with the example/recovered key. → *Severity:* Critical (total compromise, bypasses OS auth) **if reachable + key recoverable**.
- *Claim:* the BCD `key:` is recoverable from an offline-attached volume (chains 5C). → *Oracle:* `bcdedit /enum` / BCD hive grep yields the key. → *Severity:* High (enabler).
**Doc evidence:** `troubleshoot-windows-with-kdnet`. **Severity-if-true:** Critical (contingent on reachability + key).

### 5I — SAC unauthenticated command set over serial console (Lens U, L)  — PRIORITY 2
**Background.** Windows Special Administration Console (SAC) is reached over the EC2 serial console (`troubleshoot-windows-sac`). The built-in `SAC>` commands table states these "do not require you to sign in."
**Security Concern.** Once the serial-console perimeter is crossed (IAM key-push, 5B), `i` (set IP), `k`/`l`/`m`/`r` (process control), `crashdump`, `shutdown`, `restart`, `d` (kernel log) execute with **no Windows credential** — only `cmd`-channel creation asks for admin creds.
**High-level Test Scenarios.**
- *Claim:* a caller with only serial-console IAM (no Windows login) can `crashdump` / `shutdown` / set IP / kill processes / dump the kernel log. → *Oracle:* run `crashdump`/`i`/`k <pid>` at `SAC>` with no OS login. → *Severity:* Medium–High (pre-auth DoS, network reconfig, forced dump; integrity/availability without OS creds). Chains with 5B's narrow-action→serial access.
**Doc evidence:** `troubleshoot-windows-sac` (built-in commands "do not require you to sign in"). **Severity-if-true:** Medium–High.

### 5J — Audit-log coverage of troubleshooting actions (Lens O)  — PRIORITY 3 (enabler)
**Background.** `RebootInstances` is explicitly stated to be CloudTrail-logged; no fetched page states the same for `GetConsoleOutput`/`GetConsoleScreenshot`/`GetPasswordData`/`SendSerialConsoleSSHPublicKey`/`SendDiagnosticInterrupt`/the serial-console toggle, and the in-session serial keystroke stream is a raw virtual-serial-port stream (not an API).
**Security Concern.** If console reads / key pushes / the diagnostic NMI are unlogged, an IDOR (5A) or crash (5E) is unauditable to the victim — a severity multiplier.
**High-level Test Scenarios.**
- *Claim:* one or more of the above produces no CloudTrail management event. → *Oracle:* call each, inspect `LookupEvents`. → *Severity:* Low–Informational alone; multiplies 5A/5B/5E.
**Doc evidence:** `ec2-instance-reboot` (CloudTrail stated) vs silence elsewhere. **Severity-if-true:** Informational (enabler).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant console read | `GetConsoleOutput`/`Screenshot` | "Only the instance owner can access the console output" + IAM resource-ARN scoping (mechanism unstated) |
| Cross-tenant serial shell | serial-console SSH gateway | per-instance IAM on `SendSerialConsoleSSHPublicKey` + gateway routing by `<instance-id>.port0` |
| Narrow action → root | `SendSerialConsoleSSHPublicKey` / `ec2:osuser` | IAM action naming; `ec2:osuser` condition (SendSSHPublicKey only) |
| Disk access without OS creds | EBS AttachVolume/DetachVolume + helper | `ec2:AttachVolume`/`DetachVolume` resource-ARN scoping (same AZ/account) |
| Automation role self-escalation | `AWSSupport-StartEC2RescueWorkflow` policy | resource-name prefix `AWSSupport-EC2Rescue-*` on CreateRole/AttachRolePolicy (no PolicyArn cond) |
| CFN/Lambda source land-grab | `awssupport-ssm.*` S3 ARN | bucket-name-only trust (S3 ARN has no account id) |
| Admin-password harvest | `/EC2Rescue/Password/<id>` SSM param | per-instance path + KMS; weakened by `Resource:"*"` Example Policy |
| KDNET kernel takeover | `bcdedit` net debug | shared `key:` + SG-scoped UDP 50000–50039 |
| SAC pre-auth commands | serial-console SAC | serial-console IAM only ("do not require you to sign in") |
| Availability kill-switch | `SendDiagnosticInterrupt` | IAM `instance*` scoping; no approval/rate-limit documented |
| Boot-from-wrong-volume | initramfs label/UUID | none from AWS (guest-side `/etc/fstab`); replace-root-volume resource perms |
| Account toggle bypass | `SerialConsoleAccessEnabled` | account/region flag + Org SCP / declarative policy |
| Unaudited action | CloudTrail | only `RebootInstances` documented as logged |

## 7. Out-of-Scope Risk Categories
- Single-tenant **self-DoS** (crashing your own instance via diagnostic interrupt / zip-bomb). Out of scope.
- **Customer-authored** IAM least-privilege footguns (e.g. a customer writing `Resource:"*"` on `GetConsole*` or `AttachVolume`) — the misconfig is in scope to *demonstrate the shape*, but the fix is the customer's; only an **AWS-authored/uneditable** policy or sample is Tier-2 reportable.
- IMDS on fully-managed hosts; DNS rebinding against private-only endpoints.
- A user steering the OS of **their own** instance (serial/SSH to one's own box is intended).
- Guest-OS bugs reached via a legitimate serial/SSH session (that's the customer's OS, not AWS's plane).
- Shared EBS/Nitro backplane internals — treat as AWS service plane: **HARD STOP**, do not probe.

## 8. Null Hypotheses / Doc Gaps
- **Lens K (prompt injection), F (translation/wire-protocol), H/W (KMS/attestation), N (ARN migration), J/FF (OAuth/JWT), DD (cache-key), P (identity proofing):** no triggers on the troubleshooting pages read (`ec2-instance-troubleshoot`, `troubleshoot-unreachable-instance`, serial-console set, `ResettingAdminPassword`, Instance-Connect set, EC2Rescue set, `instance-booting-from-wrong-volume`). Declared **N/A** on the basis of those pages — re-open if a troubleshooting feature adds an LLM, a parser, a KMS-gated recovery secret, or a token flow.
- **Ownership mechanism** behind "only the instance owner can access the console output" is undocumented (IAM resource-ARN scoping vs a hardcoded account comparison) — the crux of 5A; confirm against `ec2-security-iam` / EC2 resource-level-permission reference or by test.
- **GetConsoleScreenshot** API ref carries no owner-only sentence (asymmetry with Output) — confirm whether a true enforcement gap or incidental omission.
- **`WakeUp=true`** on `GetConsoleScreenshot` — unconfirmed whether it has a distinct permission gate beyond `ec2:GetConsoleScreenshot`.
- **CloudTrail** coverage of all console/serial/password/interrupt actions is undocumented (5H).
- **`SendSerialConsoleSSHPublicKey` lacks `ec2:osuser`** — confirmed in IAM reference; whether the serial login can be restricted at all is a doc gap.
- **60-second key** overwrite / multi-key semantics within the window are undocumented (5D).
- **`LogDestination` S3 bucket** ownership/account/region validation on `AWSSupport-ExecuteEC2Rescue` is undocumented (5G).
- **`instance-console.md`** 404s on the current UserGuide tree; content reconstructed from `troubleshoot-unreachable-instance` + API refs — verify canonical URL before citing.
- **EC2Rescue download integrity** — `ec2rl` GPG verification is explicitly "(Optional)" and all artifacts come from one AWS host over `curl` (5G); the Windows SSM Distributor package `AWSSupport-EC2Rescue` says "Downloads and verifies" without describing how.
- **`awssupport-ssm.*` region→bucket-name construction** is not public — needed to fully confirm the land-grab (5G Lead); confirm whether the region is baked into the fetched bucket name and whether every region's name is pre-claimed by AWS.
- **Helper/target ownership checks** beyond "same Availability Zone" for `UnreachableInstanceId`/`InstanceId` are undocumented (5G).
- **`AWSSupport-RunEC2RescueForWindowsTool`** appears as both a Run Command and an Automation document of the same name; the full parameter schema was not rendered — reconcile before building IAM test policies.

> **Lenses that FIRED (do not treat as null):** A, V, E/B, C/M, U, L, BB, R, S, T, EE, Y, O. **Null / N/A** (named pages checked, no trigger): K (prompt-injection), F (translation/wire-protocol — the serial stream is raw, not parsed into another language), H/W (KMS/attestation — no recovery secret under a customer CMK or attestation gate on these pages), N (ARN migration), J/FF (OAuth/JWT), DD (cache-key), P (identity proofing), I (tagging-as-access-control), G (SSRF — no field these pages dereference server-side; EC2Rescue's `OfflineScript`/`LogDestination` are account-local, not fetched URLs). Re-open any null lens if a troubleshooting feature later adds an LLM, a parser, a KMS-gated recovery secret, a token flow, or a server-side fetch.

---
*Generated by the `security-questionbuilder` skill (6-step boundary-first method), documentation-only. Hand confirmed-ownership / routing / replay leads to `aws-vuln-hunter` with a synthetic two-account canary; settle condition-key leads read-only via IAM policy simulation.*
