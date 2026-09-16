# EC2Launch v2 agent — Attack Research Plan

Source of leads: `ec2launch-v2.html` (main) + its five child pages — `ec2launch-v2-install.html`, `ec2launch-v2-settings.html`, `ec2launch-v2-task-definitions.html`, `ec2launchv2-troubleshooting.html`, `ec2launchv2-versions.html`. Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`, cross-checked against live `docs.aws.amazon.com` `.md` on **2026-09-12** (main + task-definitions live byte-consistent with offline; **no** "See also"/agent-toolkit injection block on these pages — cf. `[[aws-docs-see-also-injection]]`).
Status: documentation-derived hypotheses only; nothing tested against a live account.

Skill: `security-questionbuilder`. This page is a **member page** of the Windows launch-agents family. It is scoped as the EC2Launch v2 *agent-internals* slice and cross-references the family/hub plans rather than re-deriving their crown jewels:
- `[[project_configure-launch-agents-plan]]` — launch-agents FAMILY hub (config-dir ACL lead originated here).
- `[[project_ec2-windows-instances-plan]]` — Windows config hub; carries the two headline crown jewels this plan defers to: **Sysprep first-boot blank-password/RDP window** and **EC2FastLaunchServiceRolePolicy `PassRole Resource:"*"`**.
- `[[project_ec2-security-iam-plan]]`, `[[project_sysprep-ami-plan]]`, `[[project_connect-windows-rdp-plan]]`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This is an **in-guest, single-account, customer-owned** agent. The dominant boundary is **non-admin/prior-tenant in-guest identity → SYSTEM-executing launch agent**, plus **IAM-holder → SYSTEM code-exec** and **instance → AWS control/telemetry plane**. There is **no multi-tenant shared service fleet** here; the only AWS-owned shared surfaces are the KMS activation servers, the EC2 telemetry ingestion endpoint, and the EC2 console message channel ("Windows is ready", RDP cert thumbprint).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (telemetry ingest, KMS activation fleet, the S3 bucket `amazon-ec2launch-v2` write plane), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** attempt to write to the S3 distribution bucket or the telemetry endpoint.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Local privilege escalation to SYSTEM** by a non-administrator in-guest principal, via any agent-consumed file whose directory is *not* the one the docs say is ACL-restricted (`state`, `sysprep`, `wallpaper`, `log`, or the config **file** vs the config **dir**).
2. **Prior-tenant / AMI-author → subsequent-instance code exec or credential capture**, via content baked into `agent-config.yml`, the `sysprep` dir, the wallpaper `.lnk`, or a static admin password left in the config.
3. **IAM-holder → SYSTEM code execution without `iam:PassRole`**, via `executeScript`/`executeProgram` delivered through user data (`ec2:ModifyInstanceAttribute` / `RunInstances`).
4. **Cleartext-secret recovery**: read the local-administrator password (or any secret) from `agent-config.yml` / snapshots / `get-agent-config` output, bypassing the intended "encrypted with the user's key" wall.
5. **Supply-chain compromise** of the agent binary via the S3/MSI/SSM-Distributor/Image-Builder install paths.
6. **Defense evasion / audit blind-spot**: use the agent's own `reset`/`sysprep`/`clean` to wipe state and logs, or suppress `startSsm`, from an in-guest script.
7. **Data destruction** of an attacker-influenced or Linux-formatted secondary volume via `initializeVolume` empty-detection bypass.

---

## 2. Components, Assets, and Design

### 2.1 What it is
EC2Launch v2 (`EC2Launch.exe`) is the Windows first-boot/every-boot provisioning agent, preinstalled on AWS Windows Server 2016–2025 AMIs. It runs as a **Windows service** (`EC2LaunchService.exe`) and as an on-demand CLI. It executes a pipeline of **tasks** grouped into **stages** (`Boot → Network → PreReady → [Windows is ready] → PostReady/UserData`), driven by two config sources: the on-disk `agent-config.yml` and instance **user data**.

### 2.2 Execution identity (the核心 of the threat model)
- `executeProgram` — **`runAs` (Required) MUST be `localSystem`.**
- `executeScript` — **`runAs` (Required) is `admin` OR `localSystem`**; `content` is arbitrary `batch`/`powershell`; if no `arguments`, the agent injects **`-ExecutionPolicy Unrestricted`** by default.
- Default tasks (`activateWindows`, `setDnsSuffix`, `setAdminAccount`, `setWallpaper`, `startSsm`, `extendRootPartition`) all run under the service (SYSTEM).
→ Anything that controls task **content** or **input files** controls SYSTEM-level execution on the instance.

### 2.3 Assets / identifiers
| Asset | Location | Owner | Sensitivity |
|---|---|---|---|
| `agent-config.yml` | `%ProgramData%\Amazon\EC2Launch\config\` | admin-restricted **dir** (doc-asserted) | drives every SYSTEM task; may hold **cleartext** admin pw (static type) |
| `state.json` / `previous-state.json` / `.run-once` | `%ProgramData%\Amazon\EC2Launch\state\` | **no ACL guarantee in docs** | decides which `once` tasks re-run |
| `sysprep` dir files (`unattend.xml`, etc.) | `%ProgramData%\Amazon\EC2Launch\sysprep\` | **no ACL guarantee in docs** | determines Sysprep operations → baked into next AMI |
| `wallpaper` image + `setwallpaper.lnk` | `wallpaper\` dir + **every user's** Startup folder | **no ACL guarantee in docs** | `.lnk` auto-runs at each user's first logon; **survives task removal** |
| `agent.log` / `telemetry.log` | `log\` dir | **no ACL guarantee in docs** | forensic record; auto-rotated, **only one backup kept** |
| Local Administrator credential | generated by `setAdminAccount`; encrypted "with the user's key" (random) OR **cleartext in `agent-config.yml`** (static, until Sysprep) | mixed | Critical |
| Agent MSI | `https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi` | AWS (service plane) | supply-chain root of trust |
| `EC2LAUNCH_TELEMETRY` env var | machine system env | admin | telemetry on/off |

### 2.4 ASCII pipeline
```
 IAM caller (RunInstances / ModifyInstanceAttribute userData)
        │  user data (YAML v1.1/v1.0 or XML <powershell>)
        ▼
 IMDS user-data ──► EC2Launch v2 service (SYSTEM) ──► executeScript/Program (SYSTEM/admin)
        ▲                    │  reads                         │
 agent-config.yml ──────────┘                                 ├─► setAdminAccount ─► local Admin pw (enc | cleartext-in-yml)
 (config dir: admin-only*)                                    ├─► setDnsSuffix    ─► registry SearchList  (see launch-agents-set-dns)
 state/ sysprep/ wallpaper/ log/  (no doc ACL guarantee) ─────┤─► setWallpaper    ─► .lnk in EVERY user Startup (persist)
                                                              ├─► initializeVolume─► formats attached volumes
                                                              └─► startSsm        ─► SSM Agent (manageability)
                                                 outbound: KMS activation fleet | telemetry ingest | EC2 console ("ready", RDP thumbprint)
 install source: S3 MSI / SSM Distributor (acct or ORG-wide) / Image Builder component / preinstalled AMI
 (*"Permission to create files in this directory is restricted to the administrator account to prevent privilege escalation." — config dir ONLY)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Non-admin in-guest user | SYSTEM launch agent | write to an agent-consumed file whose dir has no ACL guarantee (`state`, `sysprep`, `wallpaper`, `log`) | a file a non-admin can write is later read/executed by the SYSTEM service → SYSTEM code exec or task-rerun control = **privilege escalation** |
| Non-admin in-guest user | config `agent-config.yml` | the doc guarantee is on the **dir** ("create files"); test **modify/replace/rename** of the existing file and ACL on the file itself | non-admin can alter the file the SYSTEM service parses next boot |
| AMI author / prior tenant | subsequent instance (new owner) | content baked into `agent-config.yml` / `sysprep` dir / wallpaper `.lnk` / static pw remanence, then AMI shared/published | booted instance runs attacker task as SYSTEM, or a stale credential is recoverable |
| IAM principal (no PassRole) | SYSTEM on the instance | `ec2:ModifyInstanceAttribute(userData)` or `RunInstances(user-data)` → `executeScript runAs localSystem` | SYSTEM command runs though caller holds no `iam:PassRole` / no admin on the box |
| Any admin/process on box | local Administrator secret | `get-agent-config` prints `agent-config.yml`; static pw stored cleartext until Sysprep | cleartext password recovered from config or CLI output |
| Instance | AWS KMS activation fleet | `activateWindows` static routes + KMS servers | (AWS-owned) reaching/abusing the activation plane = HARD STOP |
| Instance | AWS telemetry ingest | `EC2AgentTelemetry` upload (all AWS-owned AMIs, default on) | (AWS-owned) egress content / spoofing another agentId into ingest = HARD STOP |
| S3 MSI / Distributor source | instance binaries | download-and-run install (TOFU) | a substituted/foreign MSI executes as installer/SYSTEM |
| In-guest script | audit/state record | `reset` / `sysprep -c` / `collect-logs` delete state & logs; single log backup | a security-relevant run leaves no durable log |
| **customer surface** | **AWS service plane** | any of the AWS-owned rows above | **HARD STOP — preserve evidence, disclose.** |

---

## 4. API / Interface Inventory

The public control-plane API surface that reaches this agent is **thin and belongs to EC2 core**, not to a dedicated EC2Launch API. Enumerate:

| Name | Method | Mut? | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:RunInstances` (user-data) | AWS API | mut | ext | supplies user-data tasks run as SYSTEM | yes | IAM principals | **no `iam:PassRole` needed to get SYSTEM exec** (Lens B/E variant) |
| `ec2:ModifyInstanceAttribute` (`userData`) | AWS API | mut | ext | rewrites user data → SYSTEM exec on next boot | yes | IAM principals w/ this action | key privesc-adjacent action; check condition-key coverage (defer to `[[project_ec2-windows-instances-plan]]` L4) |
| `ec2:GetPasswordData` | AWS API | non-mut | ext | retrieve encrypted Admin pw set by `setAdminAccount` | yes | IAM principals | scoping ownership-vs-existence → defer to `[[project_connect-windows-rdp-plan]]` |
| SSM Distributor `AWSEC2Launch-Agent` / Quick Setup | AWS API/console | mut | ext | install/auto-update agent, **account OR AWS-Organization-wide** | yes | SSM/Org admins | org-wide push = blast-radius amplifier for a bad package |
| EC2 Image Builder `ec2launch-v2-windows` component | AWS API | mut | ext | bakes agent into custom image | yes | Image Builder callers | supply-chain node |
| `EC2Launch.exe` CLI (`run`,`reset`,`sysprep`,`validate`,`get-agent-config`,`collect-logs`,`list-volumes`,`status`,`version`,`wallpaper`) | local exec | mixed | **in-guest only** | agent control; `get-agent-config` dumps config incl. secrets | no | local user (admin path assumed but **not asserted per-command**) | **not an AWS API** — no IAM gate; gate is NTFS/OS ACL only |
| Telemetry upload | agent→AWS | mut(remote) | egress | uploads usage/errors/callstacks | n/a | agent (fleet) | AWS-owned ingest; toggled by `EC2LAUNCH_TELEMETRY` |

**Undocumented/hidden-knob sweep:** the `setAdminAccount` `password.type` enum diverges between two pages — task-definitions says **`static` / `random` / `doNothing`**; the settings-dialog page says **`Random` / `Specify` / `Do not set`**. Confirm which string the YAML parser actually accepts and whether an unknown/empty `type` **fails open** (e.g. silently leaves the account blank-password/enabled). No IAM condition key governs any EC2Launch task selection — task authorization is entirely "can you write user data / the config file."

---

## 5. Recommended Areas of Focus

### Area 1 — Config/state/sysprep/wallpaper directory ACL: guarantee vs enforcement (Lens U, Lens Q, in-guest privesc) — **TOP PRIORITY**
**Background.** The directory-structure section makes exactly **one** security promise: for the `config` dir, *"Permission to create files in this directory is restricted to the administrator account to prevent privilege escalation."* Every other SYSTEM-consumed directory — `state`, `sysprep`, `wallpaper`, `log` — carries **no** such statement, yet each holds content the SYSTEM service reads or acts on.
**Security Concern.** A local non-administrator who can write `state.json`/`previous-state.json`/`.run-once` controls which `once`-frequency tasks (incl. `executeScript runAs localSystem`) re-run; who can write the `sysprep` dir controls the operations baked into the next AMI; who can drop/modify `setwallpaper.lnk` in a user Startup folder gets code at that user's logon. The single promised ACL may also be scoped to *create* only — **modify/replace/rename/delete** of the existing `agent-config.yml`, or ACL on the file itself, may be unguarded.
**High-level Test Scenarios (falsifiable):**
- **Claim:** a non-admin can write `%ProgramData%\Amazon\EC2Launch\state\state.json` (or delete `.run-once`) to force a `once` SYSTEM task to re-execute. → **Oracle:** as a standard user, alter state, trigger `EC2Launch.exe run` / reboot, observe a `once` task run again → **SYSTEM privesc**. Doc evidence: `state` dir description; `.run-once` semantics. Severity: **High**.
- **Claim:** the config guarantee covers create but not modify — a non-admin can replace/edit the existing `agent-config.yml`. → **Oracle:** inspect the actual NTFS DACL on the dir *and file*; attempt non-admin modify. Doc evidence: "restricted to the administrator account" (verb = *create files*). Severity: **High** if modify/replace succeeds.
- **Claim:** a non-admin can drop `setwallpaper.lnk` into another user's Startup folder (or the agent creates it world-writable). → **Oracle:** ACL of the `.lnk` and of the Startup path the agent writes into. Severity: **Medium–High** (per-user code exec + persistence — the `.lnk` **survives task removal**, troubleshooting §).
- **Doc-gap:** the actual DACLs on all five dirs, the service binary (`%ProgramFiles%\Amazon\EC2Launch\*.exe`), and the service `ImagePath`/registration are **not in the docs** → mark "doc-gap — confirm surface first." If any AWS-installer-set ACL is missing, the enforcement gap is **AWS's defect (Tier-2 reportable)**, not a customer footgun.
**Stop condition:** confirmed non-admin→SYSTEM write path, or all dirs proven admin/SYSTEM-only.

### Area 2 — SYSTEM code execution as a first-class primitive; user-data delivery without PassRole (Lens B/E variant, Lens K delivery)
**Background.** `executeProgram` (must `runAs localSystem`) and `executeScript` (`runAs admin|localSystem`) run arbitrary operator-supplied content. Delivery vectors: on-disk `agent-config.yml`, and **user data** (YAML v1.1/v1.0 or legacy XML `<powershell>`), with `<persist>true</persist>` making it recur every boot.
**Security Concern.** SYSTEM execution is reachable by anyone who can set user data — which is an **EC2 API grant (`ec2:ModifyInstanceAttribute` on `userData`, or `RunInstances`), NOT `iam:PassRole` and NOT in-guest admin.** This is the confirmed "non-PassRole action reaching effective root on the box" shape (`[[project_ec2-windows-instances-plan]]` L4).
**High-level Test Scenarios:**
- **Claim:** a principal holding only `ec2:ModifyInstanceAttribute` (userData) can achieve SYSTEM command execution on a stopped instance it can start, with no PassRole and no OS credentials. → **Oracle:** set user data to `executeScript runAs localSystem` writing a canary, start the instance, observe canary written by `NT AUTHORITY\SYSTEM`. → **Confirm/refute condition-key coverage on `ModifyInstanceAttribute(userData)` in the IAM reference (defer detailed condition-key audit to `[[project_ec2-windows-instances-plan]]`).** Severity: **High** (effective root via a non-obvious action).
- **Claim:** legacy YAML v1.0 / XML user data changes the run ordering relative to `startSsm` and can run **more than once** (troubleshooting: "Service runs user data more than once"), enabling repeated SYSTEM exec / a boot loop. → **Oracle:** submit v1.0 + reboot-inducing script, count executions. Severity: Medium.
- **Chain:** shared/published AMI with a malicious `executeScript` baked into `agent-config.yml` → every launcher runs it as SYSTEM (supply chain into Area 4 / `[[project_sharing-amis-plan]]`). Severity: **High**.
**Doc evidence:** executeProgram/executeScript `runAs`; user-data change-log table; `<persist>`/`<detach>` tags.

### Area 3 — Local-administrator credential handling & secret remanence (Lens T, Lens U)
**Background.** `setAdminAccount` sets the local Administrator password. Settings-dialog page: **`Specify`** ⇒ *"The password is stored in `agent-config.yml` as clear text and is deleted after Sysprep sets the administrator password"*; **`Random`** ⇒ encrypted "using the user's key"; **`Do not set`** ⇒ uses `unattend.xml`, and *"If you don't specify a password in unattend.xml, the administrator account is disabled."* Task-definitions calls the same field `static`/`random`/`doNothing` with `data` holding the static value.
**Security Concern.** A cleartext admin password lands in a config file (and therefore in **any snapshot/AMI/backup taken before Sysprep**, and in the output of `EC2Launch.exe get-agent-config`). The "encrypted with the user's key" claim for `random` and the "account disabled" claim for `doNothing` are guarantees to trace to enforcement.
**High-level Test Scenarios:**
- **Claim:** `password.type: static/Specify` leaves the Administrator password recoverable in cleartext from `agent-config.yml`, an EBS snapshot, or `get-agent-config` output, before Sysprep runs. → **Oracle:** set static pw, snapshot the volume / run `get-agent-config -f json`, grep for the plaintext. Severity: **High** (credential exposure; bypasses `GetPasswordData` encryption model). Route storage-remanence framing to `[[project_sysprep-ami-plan]]`.
- **Claim (Lens U doc-vs-behavior):** the `password.type` enum divergence (`static/random/doNothing` vs `Random/Specify/Do not set`) hides a **fail-open** — an unknown/empty/misspelled `type` value silently yields a blank-password or enabled-but-unset Administrator account. → **Oracle:** feed each spelling + an invalid value; observe account state. Severity: **Medium–High** (unauth network foothold if it composes with the RDP-enable window). Composes with the **Sysprep first-boot blank-password/RDP window** crown jewel in `[[project_ec2-windows-instances-plan]]` / `[[project_sysprep-ami-plan]]` — do **not** re-derive; test the composition only.
- **Claim:** `get-agent-config` and `collect-logs` are not restricted to admins, letting a lower-privileged local process read the config (and any static secret) or harvest logs. → **Oracle:** run each CLI as a standard user. Severity: Medium.

### Area 4 — Install / update supply chain (Lens Y transport, supply-chain, Lens AA org-share)
**Background.** Four install paths: (1) PowerShell `Invoke-WebRequest` from `https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi` then `msiexec`; (2) SSM Distributor `AWSEC2Launch-Agent`, incl. **Quick Setup across an entire AWS Organization**; (3) Image Builder component; (4) preinstalled AMI. The MSI *"uninstalls previous versions"* and can `ADDLOCAL="Basic,Clean,Telemetry"`.
**Security Concern.** The documented PowerShell flow is **trust-on-first-use**: it publishes **no hash, no signature-verification step, and no code-signing check** for the downloaded MSI, and for Server 2016 instructs the operator to **manually enable TLS 1.2** (implying the default may negotiate lower — a downgrade window). An org-wide Distributor Quick Setup turns one poisoned package into fleet-wide SYSTEM install.
**High-level Test Scenarios:**
- **Claim:** the doc's install procedure will run any MSI served at the operator-set `$Url`/download location without integrity verification (MITM on a pre-TLS1.2 Server-2016 session, or a typo-squatted `{{Amazon S3 URL}}`). → **Oracle:** documentation confirms absence of hash/sig check; the `latest/` path has no version pinning. Severity: **High** (SYSTEM install) — but the S3 bucket itself is **AWS-owned: do not probe it for write/takeover → HARD STOP** if the bucket namespace looks claimable.
- **Claim:** SSM Distributor Quick Setup applied to an AWS Organization pushes agent updates to member accounts on a schedule, so a compromised package version or a malicious co-admin reaches every member's SYSTEM. → **Oracle:** doc "can include instances within an AWS Organization"; audit who can create/modify the Association (`AWS-QuickSetup-Distributor-EC2Launch-Agent-` prefix). Severity: **High** (blast radius), scope-limited to org-admin trust.
**Doc-gap:** whether the MSI is Authenticode-signed and whether `msiexec` enforces it is not stated → confirm.

### Area 5 — In-guest defense evasion & audit blind spots (Lens O)
**Background.** From inside an `executeScript`, a script can issue `reset` (*"deletes all of the agent state data"*, optionally logs with `-c`) or `sysprep` (resets state, updates `unattend.xml`, **disables RDP**, runs Sysprep). `collect-logs` zips logs. `agent.log` rotates at 1 MB and **only one backup is kept**.
**Security Concern.** An attacker with SYSTEM (via Area 1/2) can (a) wipe agent state/logs to erase evidence of the task that ran, (b) suppress `startSsm` (inline reset/sysprep short-circuits the pipeline so *"the Systems Manager service never starts"*) to evade fleet management/EDR, and (c) rely on the single-backup log rotation to flush a prior malicious entry by generating 1 MB of noise.
**High-level Test Scenarios:**
- **Claim:** an inline `executeScript` issuing `sysprep`/`reset` prevents `startSsm` and clears state, leaving no durable agent record of the malicious task. → **Oracle:** run such a script; confirm SSM never starts and `state.json`/`previous-state.json` are gone (agent `status` = 5). Severity: Low–Medium (enabler; raises severity of Areas 1–2).
- **Claim:** log rotation (1 MB, one backup) lets an attacker roll a malicious `agent.log` entry off disk by emitting >2 MB of benign log. → **Oracle:** confirm rotation drops the older backup. Severity: Informational.

### Area 6 — initializeVolume empty-detection bypass → data destruction (Lens F/L data-integrity)
**Background.** `initializeVolume` (`initialize: all`) formats volumes it deems empty; *"A volume is considered empty if the first 4 KiB of the volume are empty, or if the volume doesn't have a Windows-recognizable drive layout."* Troubleshooting explicitly warns a **Linux-formatted (MBR/GPT-less-to-Windows) volume is treated as empty and initialized** — i.e. wiped.
**Security Concern.** An attacker who can attach a volume, or who supplies an AMI/config with `initialize: all`, can cause **silent destruction** of a victim's non-Windows or first-4-KiB-zeroed data volume on boot. `letter` is applied regardless of initialization state.
**High-level Test Scenarios:**
- **Claim:** attaching a Linux-formatted data volume to an instance whose `agent-config.yml` has `initializeVolume initialize: all` destroys the data on next boot. → **Oracle:** attach such a volume, boot, confirm reformat. Severity: **Medium** (single-tenant data loss; **High** if the config is baked into a shared AMI so it destroys *launchers'* attached volumes).
**Doc evidence:** initializeVolume empty-detection; troubleshooting note.

### Area 7 — setDnsSuffix search-list poisoning & persistence (Lens G-adjacent / network) — defer detail
**Background.** `setDnsSuffix` (`frequency: always`, PreReady) adds suffixes to the DNS search list with `$REGION`/`$AZ` substitution; *"Only suffixes that do not already exist are added"* and (per family plan) stale entries are **not automatically removed**.
**Security Concern.** A baked/config-controlled malicious suffix causes unqualified name resolution to attacker-controlled domains (NTLM-relay / credential-interception), and the no-auto-remove behavior makes it persistent.
**Scenario (defer):** route the full analysis to `[[project_configure-launch-agents-plan]]` (Area 2, `launch-agents-set-dns`). Page-local test: confirm `$REGION`/`$AZ` are sourced from IMDS (not attacker-settable) and that a config suffix persists across agent runs. Severity: Medium (persistence + relay enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin writes `state`/`sysprep`/`wallpaper`/`log` → SYSTEM exec | dir ACLs | *only* the config dir is doc-asserted admin-restricted (Area 1) |
| Config guarantee is create-only; modify/replace unguarded | `agent-config.yml` file ACL | "restricted to the administrator account **to create files**" |
| SYSTEM exec via user data without PassRole | `executeScript`/`ModifyInstanceAttribute` | none in-guest; relies on EC2 IAM scoping of `userData` |
| Cleartext admin pw in config/snapshot/CLI | `setAdminAccount` static; `get-agent-config` | "deleted after Sysprep"; "encrypted using the user's key" (random only) |
| Unknown `password.type` fails open (blank pw) | YAML parser | enum divergence across pages; "account is disabled" claim (doNothing) |
| Unverified MSI download / org-wide push | install paths | none documented (no hash/sig); TLS 1.2 manual on 2016 |
| Evidence/SSM suppression via reset/sysprep | agent state & log | single log backup; inline reset short-circuits `startSsm` |
| Linux-volume treated as empty → wiped | `initializeVolume` | 4 KiB / drive-layout empty check (bypassable) |
| DNS suffix poisoning + persistence | `setDnsSuffix` | "only new suffixes added"; no auto-removal |

---

## 7. Out-of-Scope Risk Categories
- **AWS-owned service plane — HARD STOP, do not probe:** the KMS Windows-activation fleet (`activateWindows`), the EC2 telemetry ingestion endpoint (`EC2AgentTelemetry`, on by default for all AWS-owned AMIs), the EC2 console message channel ("Windows is ready", RDP thumbprint), and the S3 distribution bucket `amazon-ec2launch-v2`. Reaching, spoofing, or writing any of these = disclose, don't exploit.
- **A customer steering their own SYSTEM agent** on an instance they fully own (setting their own user data to run their own script as SYSTEM) is expected behavior, not a finding — the finding is only when a *lower-privileged* principal or a *prior tenant* reaches it.
- **Customer-authored `agent-config.yml` least-privilege footguns** (their own weak scripts) — out of scope unless the weak default ships in AWS's preinstalled AMI config.
- **IMDS on managed hosts**, generic Windows/Sysprep OS bugs, and the Fast Launch t3 provisioning fleet (crown jewel lives in `[[project_ec2-windows-instances-plan]]`; provisioning-fleet IMDS = HARD STOP).
- Single-tenant self-DoS (reboot loops via mis-`exit 3010` scripts) — informational.

---

## 8. Null hypotheses / doc gaps (pages checked)

- **Lens A (cross-tenant IDOR):** NULL — read all six EC2Launch v2 pages; the agent is a single-instance in-guest component with no resource-by-ID API and no shared multi-tenant fleet. No tenant identifier appears in any request the agent makes on behalf of a caller.
- **Lens C (credential vending / session scope):** NULL — no STS/session-policy/AssumeRole surface on these pages (SSM Agent, once started, has its own; out of scope here).
- **Lens D/V (data→control-plane / network segmentation):** NULL for the agent itself — read main + settings + task-definitions; only outbound static routes to IMDS/KMS are mentioned, no control-ENI/multi-ENI model. `setDnsSuffix` network abuse tracked in Area 7.
- **Lens H/W (KMS encryption-context / attestation):** NULL — `activateWindows` uses AWS KMS *activation* servers (not customer CMKs); no `kms:RecipientAttestation`/PCR/encryption-context surface on these pages.
- **Lens I/S (tagging/ABAC, condition-key semantics):** NULL on this page set — no `TagResource`/ABAC and no in-scope IAM policy JSON is printed here. The relevant condition-key gap (`ec2:ModifyInstanceAttribute(userData)`) is owned by `[[project_ec2-windows-instances-plan]]`.
- **Lens R (AWS-authored IAM-artifact audit):** NULL for *policy JSON* — none printed on these pages. **But** the AWS-published *sample behavior* injects **`-ExecutionPolicy Unrestricted`** by default for `executeScript` when no arguments are given (Lens R "insecure sample default" variant) — noted; low severity, AWS-authored, worth filing if it composes.
- **Lens J/M/P (OAuth / shared-id / registration-proofing):** NULL — read all pages; no 3P linking, session tokens, or identity-proofing workflow.
- **Lens N (namespace migration):** NULL — v1↔v2 is an agent-generation change, not a dual-live ARN namespace; the MSI *uninstalls* v1, so no dual-authorization window.
- **Lens U doc integrity findings (open, non-null):** (a) `setAdminAccount` `password.type` enum spelled two different ways across pages; (b) config-dir ACL promise is verb-scoped to "create files"; (c) install docs assert TLS-1.2 requirement but provide no integrity check for the MSI. All three carried as leads in Areas 1/3/4.

### Priority order for a hunter
1. **Area 1** (non-admin→SYSTEM via unguarded dirs) — highest, in-guest privesc with a doc-asserted enforcement asymmetry.
2. **Area 2** (SYSTEM exec via `ModifyInstanceAttribute(userData)` without PassRole).
3. **Area 3** (cleartext admin-pw remanence + fail-open `password.type`; composes with the blank-pw/RDP crown jewel).
4. **Area 4** (MSI TOFU / org-wide Distributor) — mind the AWS-owned S3 HARD STOP.
5. **Area 6, 5, 7** (volume wipe; audit evasion; DNS poisoning).

**Doc-gaps to close first (all require in-guest inspection, not more docs):** actual NTFS DACLs on all five `%ProgramData%\Amazon\EC2Launch\*` dirs **and** on `agent-config.yml` itself; DACL/`ImagePath` on the service binary + `EC2LaunchService.exe`; whether these ACLs are AWS-installer-set (enforcement gap = **Tier-2 AWS defect**) vs customer-owned; whether the MSI is Authenticode-signed and enforced; the real string set the YAML parser accepts for `password.type` and its behavior on an invalid value.
