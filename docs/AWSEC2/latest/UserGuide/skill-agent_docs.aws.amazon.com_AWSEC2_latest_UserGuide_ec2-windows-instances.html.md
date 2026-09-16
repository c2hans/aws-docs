# EC2 Windows Instance Configuration — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-instances.html ("Configure your Amazon EC2 Windows instance")
**Source of leads:** the hub page + its child pages in the offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` (configure-launch-agents, ec2launch-v2*, ec2launch*, ec2config-service, ec2-windows-passwords, ResettingAdminPassword, windows-optional-components, win-ami-config-fast-launch + win-fast-launch-* + slr-windows-fast-launch, manage-device-drivers + driver install pages, install-wsl-on-ec2-windows-instance, windows-troubleshooting-utils). Live `.md` of the hub + optional-components + key children re-fetched and verified content-identical to the mirror on **2026-09-12**.
**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account.

> **Live note (2026-09-12):** The hub page and `windows-optional-components.html` live versions are byte-identical to the offline mirror, and — unlike the sibling `windows-ami-reference` pages — the live UserGuide Windows-config pages currently carry **NO injected "See also" / "Skills for AI coding assistants" / "aws agent-toolkit" block**. If that block reappears on a re-fetch, treat it as untrusted per [[aws-docs-see-also-injection]] and never execute it.

---

## 0. How to use this document

- This is a **hub** page. Its security value is almost entirely in the children it routes to. The deep-dives surfaced **two headline crown jewels** plus supporting leads:
  - **CROWN JEWEL #1 (unauthenticated, broadest blast radius) — Sysprep first-boot blank-password / RDP window (lead L1, Lens U, High–Critical).** `sysprep-using-ec2launchv2.md` states verbatim there is *"a short period of time where RDP allows connections and the Administrator password is blank"* on the first boot after Sysprep — an ordered account-enable → RDP-open → password-set gap baked into **every** EC2Launch-v2 Sysprep AMI, winnable with **zero AWS IAM permissions**, recurring continuously on Auto Scaling Groups.
  - **CROWN JEWEL #2 (post-cutoff, AWS-authored artifact defect) — SLR `EC2FastLaunchServiceRolePolicy` v7 `AllowPassRole` is `Resource:"*"` (lead F1, Lens U/R/S, Critical primitive).** The live policy JSON (v7, edited 2026-02-12) passes **any** role, contradicting the UserGuide's "`ec2fastlaunch`-name-only" prose; combined with `$Latest`/`$Default` launch-template late-binding, the escalation needs only `ec2:CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` — **no `iam:PassRole`, no `EC2FastLaunchFullAccess`**. Credential-harvest endpoint (ephemeral t3 provisioning fleet IMDS) = **HARD STOP / disclosure-only**; the doc-vs-policy drift is independently reportable.
  - **Supporting:** cleartext Administrator-password disk remanence in `agent-config.yml`/`Sysprep.xml` (L2, High–Critical); `ec2:ModifyInstanceAttribute(userData)` as un-PassRole'd SYSTEM code-exec (L4, Critical); baked-on-AMI user-data/task supply chain (L3); confirmed `EC2FastLaunchFullAccess` unrestricted-PassRole privesc (from [[project_ec2-security-iam-plan]]); Recycle-Bin snapshot remanence (F2); optional-components public-snapshot authenticity-filter (F7) + driver install TOFU (F6).
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Scope reality:** this is a single-account, customer-owned instance-configuration surface. There is **no shared multi-tenant service fleet exposed here** (the only AWS-owned fleet is the temporary t3 provisioning fleet behind Fast Launch — HARD STOP). The realistic breaches are therefore **(a) intra-account privilege escalation** (low-priv IAM / in-guest non-admin → SYSTEM/account-admin), **(b) supply-chain trust** (a shared/Marketplace AMI author, a poisoned public snapshot, or an unsigned driver download reaching code-exec in the consumer's instance), and **(c) credential/secret remanence** baked into shared AMIs or retained pre-provisioned snapshots.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — the Nitro hypervisor, the EC2 Fast Launch provisioning t3 fleet internals, the AMI/driver **build** pipeline, or the `ec2fastlaunch.amazonaws.com` principal's backing infrastructure — stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe it.

---

## 1. Pentest Objectives (boundary-breach goals)

0. **Unauthenticated network → fresh instance via the Sysprep blank-password/RDP window (headline).** Prove that the documented first-boot window where "RDP allows connections and the Administrator password is blank" (`sysprep-using-ec2launchv2.md`) is winnable over the network against an instance booting from a Sysprep-v2 AMI into an SG that permits inbound 3389 — requiring **no AWS IAM permissions**, repeatable against Auto Scaling boots. (Lead L1.)
1. **In-guest non-admin → SYSTEM via a launch agent.** Prove that a low-privileged in-guest user (or a prior tenant of a reused instance) can cause EC2Launch v1/v2 or EC2Config to run attacker-controlled code as `LocalSystem`, by writing the agent config file, the baked user-data, or a task definition the agent consumes on the next boot/restart.
2. **Instance-launcher → SYSTEM code-exec as a first-class, un-gated primitive.** Show that anyone who can set user-data (`ec2:ModifyInstanceAttribute userData`, or `RunInstances` with user-data) obtains SYSTEM execution on the instance with **no `iam:PassRole` and no separate condition key** gating it — and enumerate whether any IAM condition key can scope it.
3. **Shared-AMI author → SYSTEM code-exec in the consumer's account.** Prove that a malicious published/Marketplace AMI (baked-on-AMI user-data, a planted agent config, a Sysprep hook, a poisoned driver) runs attacker code as SYSTEM the first time a victim launches it.
4. **Low-priv IAM principal → account admin via Fast Launch.** Reconfirm `EC2FastLaunchFullAccess`'s unrestricted `iam:PassRole` privesc, and test whether the SLR's `ec2fastlaunch`-name-substring instance-profile scope or "instance profile from your launch template" clause is a second, SLR-mediated PassRole-laundering path.
5. **Recover an Administrator password / baked secret from remanent storage.** Prove that the default Administrator password, a machine key, a domain-join credential, or an RDP host key survives in (a) a retained pre-provisioned snapshot (Recycle Bin), (b) an EC2Launch/console/user-data log, or (c) a shared Sysprep'd AMI.
6. **Substitute a poisoned resource into an install/update workflow.** Prove a consumer can be steered to mount an attacker's public "Windows … Installation Media" snapshot, or download an unsigned/poisoned driver, and execute its contents in-guest.

---

## 2. Components, Assets, and Design

### 2.1 What this hub configures
A **customer-owned Windows EC2 instance** after launch. The customer-facing interfaces are: the in-guest OS (RDP/SSM), the EC2 control-plane APIs (`ModifyInstanceAttribute`, `GetPasswordData`, `DescribeSnapshots`/`CreateVolume`/`AttachVolume`, `EnableFastLaunch`…), the console, and the AMI distribution channel (the instance boots from an AMI whose contents — agents, baked user-data, drivers — are chosen by the AMI author).

### 2.2 Key components (each is a boundary or an injection seam)
- **Windows launch agents** — `EC2Launch v2` (Windows Service, JSON/YAML config, WS2016–2025), `EC2Launch v1` (PowerShell scripts, WS2016/2019), `EC2Config` (legacy Service, XML, ≤WS2012R2). Run as **LocalSystem** at first boot and on stop→start / restart. v2-only capabilities that widen the surface: **sets the Administrator username**, **compressed user-data**, **local user-data baked on the AMI (configurable)**, **task configuration in user-data**, **customizable task run order**, **20 configurable tasks**. (Evidence: `configure-launch-agents.md` comparison table.)
- **Default Administrator password generator** — EC2Launch v2 (WS2022+), EC2Launch v1 (WS2016/2019), EC2Config (≤WS2012R2) generate the default local Administrator password at launch; it is retrievable from the console / `GetPasswordData` (RSA-encrypted to the instance key pair) only until the user changes it. (Evidence: `ec2-windows-passwords.md`.)
- **EC2 Fast Launch** — pre-provisions Sysprep'd+OOBE'd snapshots by launching temporary **t3 instances in an AWS-managed flow**, snapshotting, then terminating them; snapshots are stored and consumed-then-deleted; replenished automatically. Controlled by a **service-linked role `AWSServiceRoleForEC2FastLaunch`** (trusts `ec2fastlaunch.amazonaws.com`, uses managed policy `EC2FastLaunchServiceRolePolicy`) and, on the no-template path, by the customer attaching **`EC2FastLaunchFullAccess`** which auto-creates a CloudFormation stack (VPC, private subnets, IMDSv2 launch template, empty-rule SG). (Evidence: `win-ami-config-fast-launch.md`, `win-start-fast-launch-prereqs.md`, `slr-windows-fast-launch.md`.)
- **Optional-components installation media** — **public EBS snapshots owned by `amazon`** (alias), discovered by `--owner-ids amazon` + `description=Windows*`, mounted as a volume, and used as Windows "Turn features on/off" installation media. (Evidence: `windows-optional-components.md`.)
- **Device drivers** — ENA, AWS NVMe, AWS PV (Xen), Intel VF, AMD, NVIDIA — downloaded and installed in-guest as Administrator; sources include S3 and the `amzn-drivers` GitHub repo. (Evidence: `manage-device-drivers.md` + per-driver install pages.)
- **WSL** — in-guest Linux subsystem; requires nested-virtualization CPU option for WSL2. Almost entirely customer/Microsoft shared-responsibility. (Evidence: `install-wsl-on-ec2-windows-instance.md`.)

### 2.3 ASCII design / trust flow
```
 AMI author (possibly a 3rd party / Marketplace)         AWS control plane
      |  bakes: agent + agent CONFIG + baked user-data          |  GetPasswordData (RSA to key pair)
      |  + Sysprep hooks + drivers + secrets(?)                 |  ModifyInstanceAttribute(userData)  <-- SYSTEM exec primitive
      v                                                         |  EnableFastLaunch / DescribeSnapshots / CreateVolume
 +-----------------------------+     first boot / restart       v
 |  Customer Windows instance  | ---> EC2Launch v2/v1 / EC2Config  run as LocalSystem:
 |  (single-tenant, cust acct) |        - generate Admin password (-> console log? -> GetPasswordData)
 |                             |        - run user-data / baked user-data / tasks  (SYSTEM)
 |  in-guest non-admin user ---+------> can it write agent config / baked user-data / task def? (privesc)
 +-----------------------------+
      ^            ^                         Fast Launch SLR (ec2fastlaunch.amazonaws.com)
      |            |                              |  launches temp t3 fleet  [AWS-managed = HARD STOP]
 public "Windows   unsigned driver                |  Sysprep specialize + OOBE -> pre-provisioned SNAPSHOT
 Installation      download (S3/GitHub,            |  consumed+deleted (but Recycle Bin may RETAIN) <-- remanence
 Media" snapshot   TOFU)                           v
 (owner=amazon?)                            stored in account (owner's acct for shared-AMI launch)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| In-guest non-admin user (or prior instance tenant) | LocalSystem | Writes agent config / baked user-data / task def consumed on next boot/restart | Attacker code runs as `NT AUTHORITY\SYSTEM` after a restart the attacker can trigger |
| IAM principal with `ModifyInstanceAttribute(userData)` but not admin | SYSTEM on the instance → IMDS role creds | v2/v1 execute user-data as SYSTEM; no PassRole needed | User-data runs as SYSTEM; if an instance profile is attached, its creds are harvested from IMDS — **no IAM condition key scoped the user-data write** |
| Shared/Marketplace AMI author | Consumer's instance (SYSTEM), consumer's account | Baked-on-AMI user-data / planted agent config / Sysprep hook / poisoned driver runs at first launch | Attacker-authored code executes as SYSTEM in a victim account that merely launched the AMI |
| Low-priv IAM principal holding only `EC2FastLaunchFullAccess` | Account administrator | Unrestricted `iam:PassRole` (role/* + instance-profile/*) + un-`CalledVia` `RunInstances` | A principal with only this managed policy passes an admin instance profile and reads its creds from IMDS |
| EC2 Fast Launch SLR | Customer instance profiles named `*ec2fastlaunch*` / the LT's profile | SLR "get and use instance profiles whose name contains `ec2fastlaunch`" + "using the instance profile from your launch template" | SLR launches an instance with a profile the enabling principal could not have passed directly |
| Consumer of optional-components media | Attacker-published public snapshot | `DescribeSnapshots` by description; if `owner=amazon` filter omitted, an attacker look-alike is selectable | Consumer mounts a non-amazon public snapshot whose description is "Windows … Installation Media" and installs binaries from it |
| Any customer surface | AWS service plane (Nitro, Fast Launch t3 fleet, AMI/driver build pipeline, `ec2fastlaunch.amazonaws.com` backing) | — | **HARD STOP** — any such identity/credential/ARN = disclosure-only |

---

## 4. API / Interface Inventory

| Name | Method | Mut/Non-mut | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyInstanceAttribute` (userData) | API | Mutating | External | Sets user-data → SYSTEM exec on next boot (v2/v1) | Yes (SigV4) | Holder of the action on the instance | **Non-PassRole SYSTEM-exec primitive** (Lens B/E variant). Enumerate condition keys. |
| `GetPasswordData` | API | Non-mut | External | Returns RSA-encrypted default Admin password | Yes | Holder on the instance | Ownership-vs-existence scoping → see [[project_connect-windows-rdp-plan]] |
| `EnableFastLaunch` / `DisableFastLaunch` | API | Mutating | External | Turns on pre-provisioning for an AMI (incl. a shared AMI) | Yes | Holder; needs SLR + (no-template) `EC2FastLaunchFullAccess` | Cross-account snapshot-origin direction; SLR auto-created |
| `DescribeFastLaunchImages` | API | Non-mut | External | Lists Fast-Launch-enabled AMIs | Yes | Holder | — |
| `DescribeSnapshots` (owner-ids/description) | API | Non-mut | External | Finds `amazon` public installation-media snapshots | Yes | Anyone | Authenticity gate = owner alias; description is attacker-mimicable |
| `CreateVolume` / `AttachVolume` | API | Mutating | External | Mounts a chosen snapshot into the instance | Yes | Holder | Feeds the optional-components media flow |
| Agent config file / task defs (JSON/YAML) | in-guest file | Mutating | Internal | Declares tasks the agent runs as SYSTEM | No (in-guest) | Whoever can write the file | v2 YAML/JSON — deserialization + task-injection surface |
| Baked-on-AMI user-data (v2) | AMI content | — | Internal | User-data shipped inside the AMI, run as SYSTEM | No | AMI author | Supply-chain SYSTEM exec |
| Agent installer download | in-guest fetch | — | External | EC2Launch v2 install / driver downloads | Yes (egress) | in-guest admin | TOFU / signature check (Lens Q/N) |
| SNS launch-agent notifications | subscribe | Non-mut | External | Version notifications from an AWS-owned SNS topic | Yes | Subscribers | Check publish auth on the AWS account id (policy-review only) |

**`[NEW]` / focus markers:** none flagged `[NEW]` on these pages. AWS plants one operational lead worth keeping verbatim: the Fast Launch note — *"EC2 Fast Launch deletes pre-provisioned snapshots as soon as they're consumed … to minimize storage costs and prevent reuse. However, if the deleted snapshots match a retention rule, Recycle Bin automatically retains them."* → the explicit reuse/remanence risk (Area 5 / Lens AA).

---

## 5. Recommended Areas of Focus

> Areas 1 and 2 (launch agents) and Area 3 (Fast Launch / snapshots / drivers) are backed by dedicated deep-dive sub-analyses — their detailed lead lists are merged in below.

### Area 1 — Launch agents: in-guest non-admin / prior-tenant → SYSTEM (HIGHEST PRIORITY)
**Background:** EC2Launch v2 and EC2Config run as a Windows Service (`LocalSystem`); EC2Launch v1 runs PowerShell scripts at boot. All three run again on stop→start and restart. v2 reads a JSON/YAML config and a customizable, ordered set of up to 20 tasks. (Evidence: `configure-launch-agents.md` comparison table; `ec2launch-v2-settings.md`, `ec2launch-v2-task-definitions.md`.)
**Security Concern:** if a non-administrative in-guest principal (or a prior tenant of a reused/stop-started instance) can write the agent's config file, a task definition, or the scheduled-task hook, the agent will execute that content as SYSTEM on the next restart — an in-guest local privilege escalation whose trigger (a reboot) the attacker may be able to cause.
**High-level Test Scenarios (merged from deep-dive — see Area 1/2 detail below):** file/ACL on the v2 config and task-definition paths; whether `executeScript`/admin-account tasks honor a non-admin-writable location; YAML deserialization in the v2 parser; persistence flags that re-run user-data/tasks every boot.
**Doc evidence:** `configure-launch-agents.md`, `ec2launch-v2*.md`. **Severity-if-true:** High (in-guest LPE to SYSTEM).

### Area 2 — Launch agents: instance-launcher & shared-AMI author → SYSTEM (HIGH)
**Background:** EC2Launch executes user-data as SYSTEM; v2 adds **task configuration in user-data** and **local user-data baked on the AMI**. The default Administrator password is generated by the agent and is recoverable via the console/`GetPasswordData` until changed.
**Security Concern:** (a) anyone who can set user-data obtains SYSTEM execution with **no `iam:PassRole` gate** — this is the confirmed ec2:ModifyInstanceAttribute(userData) primitive, here in its native Windows form; (b) a malicious **shared/Marketplace AMI** can bake user-data/config/hooks that run as SYSTEM the first time a victim launches it; (c) the generated Administrator password and other boot secrets may be written to logs the AMI author or a later reader can recover.
**High-level Test Scenarios:** enumerate every IAM condition key that can scope `ModifyInstanceAttribute`'s `userData`; test whether baked user-data executes before the consumer can inspect it; test whether the Administrator password / machine key lands in the EC2Launch log, console log, or a user-data transcript.
**Doc evidence:** `configure-launch-agents.md`, `ec2-windows-passwords.md`, `ResettingAdminPassword.md`. **Severity-if-true:** High (supply-chain/low-priv → SYSTEM); credential recovery = High.

### Area 3 — EC2 Fast Launch: PassRole privesc, SLR scope, snapshot remanence (HIGH)
**Background / confirmed:** `EC2FastLaunchFullAccess` v5 = unrestricted `iam:PassRole` (role/* + instance-profile/*, only `PassedToService`) + `RunInstances` without a `CalledVia` condition → **already CONFIRMED privesc** by the hunter (acct 183174222929, 2026-08-30; folded from [[project_ec2-security-iam-plan]]). New surface on this page: the SLR `EC2FastLaunchServiceRolePolicy` "get and use instance profiles whose name contains `ec2fastlaunch`" + "launch instances … using the instance profile from your launch template"; pre-provisioned snapshot remanence via Recycle Bin; cross-account snapshot origin for shared AMIs.
**Security Concern:** (a) reconfirm the managed-policy PassRole privesc (Lens R); (b) can a low-priv principal create an **admin** instance profile whose name merely *contains* `ec2fastlaunch` and have the SLR pass it (Lens R/S substring-scope); (c) does a Sysprep'd pre-provisioned snapshot contain recoverable secrets, and can a **retained** (Recycle Bin) snapshot be read/mounted after the feature "deleted" it (Lens AA/Q/M); (d) confused-deputy in the cross-account snapshot-origin direction (Lens A/B/AA).
**High-level Test Scenarios (merged from deep-dive — see Area 3 detail below).**
**Doc evidence:** `slr-windows-fast-launch.md`, `win-start-fast-launch-prereqs.md`, `win-ami-config-fast-launch.md` (Recycle Bin note). **Severity-if-true:** account-admin privesc = High; cross-account snapshot remanence = High.

### Area 4 — Optional-components installation-media snapshot authenticity (MEDIUM)
**Background:** the documented flow finds installation media among **public snapshots**, gating authenticity on **Owner Alias = `amazon`** (console) / `--owner-ids amazon` (CLI) / `-Owner amazon` (PowerShell), then filtering by `description=Windows*`. The snapshot is mounted and used as Windows feature installation media. (Evidence: `windows-optional-components.md`.)
**Security Concern:** the `description` string ("Windows 2019 English Installation Media") is fully attacker-mimicable, and any account can publish a **public** snapshot. If an operator (or a script/runbook) filters **only by description** and omits the `amazon` owner filter, `DescribeSnapshots` will return attacker-owned look-alike snapshots alongside the genuine ones, and the operator may mount and install binaries from a poisoned volume — in-guest code execution via poisoned installation media. (Lens U authenticity-filter-omission; Lens A/X discovery-trust; Lens Q content-trust.)
**High-level Test Scenarios:** (i) publish a benign canary public snapshot with description "Windows 2019 English Installation Media" from a second account and confirm it appears in a description-only `DescribeSnapshots`; (ii) confirm the console "Public snapshots" + description filter, without the Owner Alias filter, surfaces it; (iii) check whether these `amazon` media snapshots are ever referenced by an enumerable fixed ID in any AWS runbook/automation that a substitution could target. **Do NOT publish anything that impersonates AWS for real consumers** — canary/benign only, in a self-owned account.
**Doc evidence:** `windows-optional-components.md` (Console step "choose Public snapshots → Owner Alias amazon"; CLI `--owner-ids amazon`). **Severity-if-true:** Medium (consumer-side code-exec requiring the operator to drop the owner filter); Low if the owner filter is always enforced.

### Area 5 — Driver install supply chain (TOFU) (MEDIUM)
**Background:** Windows ENA/NVMe/PV/Intel-VF/AMD/NVIDIA drivers are downloaded and installed in-guest as Administrator; Linux ENA/EFA drivers come from the `amzn-drivers` GitHub repo. (Evidence: `manage-device-drivers.md` + per-driver pages.)
**Security Concern:** if a driver package is fetched over a channel without a published, verified hash/signature (TOFU), a network or supply-chain adversary could substitute a malicious driver that installs as Administrator → SYSTEM-level in-guest code. (Lens Q/N.)
**High-level Test Scenarios (merged from deep-dive — see Area 3 detail below):** for each driver page, record the exact download origin (S3 bucket/URL vs GitHub vs SSM distributor), whether a hash/signature is published and verification is instructed, and whether HTTPS + cert pinning is implied.
**Doc evidence:** `manage-device-drivers.md`, `ena-adapter-driver-install-upgrade-win.md`, `xen-drivers-overview.md`, `aws-nvme-drivers.md`, `install-amd-driver.md`, `install-nvidia-driver.md`, `other-windows-device-drivers.md`. **Severity-if-true:** Medium–High (in-guest Administrator code-exec) — severity depends on the missing-integrity finding.

### Area 6 — Administrator password lifecycle & recovery (MEDIUM → see RDP sibling)
**Background:** the agent-generated default Administrator password is retrievable via the console / `GetPasswordData` (RSA-encrypted to the instance key pair) until the user changes it; after change it is not recoverable from AWS. (Evidence: `ec2-windows-passwords.md`.)
**Security Concern:** `GetPasswordData` names the instance by id — ownership-vs-existence scoping is tested in the RDP sibling plan; do not duplicate. The page-local additions here are: (a) is the generated password's randomness/entropy documented or weak; (b) `ResettingAdminPassword.md` reset flows (EC2Launch/EC2Rescue/SSM `AWSSupport-RunEC2RescueForWindowsTool`) — does any reset path run as SYSTEM from an attacker-influenceable input; (c) the `net user Administrator "{{new_password}}"` guidance places the new password on the command line (process-list / command-history exposure). **Severity-if-true:** Medium. **Cross-ref:** [[project_connect-windows-rdp-plan]] (GetPasswordData/GetConsoleOutput scoping), [[project_ec2rescue-linux-plan]] (EC2Rescue pattern).

---
### Detailed leads — Launch-agent family (Areas 1, 2, 6) [deep-dive]

**L1 — CROWN JEWEL — Sysprep first-boot blank-password / RDP window (Lens U). Severity: High–Critical.**
- **Claim:** The invariant "a Windows instance is never reachable over the network without the AWS-generated encrypted Administrator password" does not universally hold — there is a documented window on *every* AMI built with the EC2Launch v2 Sysprep flow where the Administrator account is enabled, its password blank/scrambled, and RDP may already be reachable.
- **Mechanism:** `sysprep-using-ec2launchv2.md` states verbatim: *"during the first boot session after Windows Sysprep has run, there is a short period of time where RDP allows connections and the Administrator password is blank."* The Specialize phase runs an ordered sequence — `net user Administrator /ACTIVE:YES /PASSWORDREQ:YES` (enables account, no password) → `EC2Launch.exe internal randomize-password` (scrambles, only "if you did not configure the `setAdminAccount` task") → re-enable RDP (`fDenyTSConnections=false`) — while the *real* AWS-generated encrypted password isn't set until the `setAdminAccount` task in EC2Launch v2's **PreReady** stage (`ec2launch-v2.md` default PreReady = `activateWindows, setDnsSuffix, setAdminAccount, setWallpaper`). Ordering gap: account-enable → RDP-open → password-set.
- **Confirm/Refute oracle:** Launch from a stock Sysprep-capable AMI into an SG that **already allows inbound 3389 at launch** (golden-AMI/Auto-Scaling pattern), and attempt RDP as `Administrator` from the moment the instance is `running` through the `Windows is Ready` console message. A successful or timing-winnable connection before `setAdminAccount` completes confirms; a clean refusal the whole way refutes. Also test whether the "scrambled" password is low-entropy/timing-derivable.
- **Preconditions/Cost:** **Zero AWS IAM permissions** — pure network positioning against any instance the attacker can reach at boot (same VPC, or public IP + open SG). Repeatable at scale against Auto Scaling Groups that continuously re-boot from the same golden AMI.
- **Why crown:** broadest applicability (baked into every Sysprep-v2 AMI), unauthenticated, and AWS's own doc frames the mitigation as a fallback ("if you did not configure setAdminAccount"), not a guarantee. Matches the exact "plaintext-password window" the RDP sibling flagged as untested.

**L2 — Cleartext Administrator password disk remanence in agent config (Lens T/AA). Severity: High–Critical.**
- **Claim:** The Administrator password is recoverable in cleartext from an AMI/snapshot disk — bypassing `GetPasswordData`/RSA-to-keypair entirely — when the documented cleanup races or is disabled.
- **Mechanism:** For `adminPasswordType: Specify`, `ec2launch-v2-settings.md` / `ec2launch-config.md` / `ec2launch-sysprep.md` state the password *"is stored in `agent-config.yml` [or `LaunchConfig.json`] as clear text and is deleted after Sysprep sets the administrator password"* — a write-then-delete window. Legacy `ec2config-service.md`: `RemoveCredentialsfromSyspreponStartup` must stay enabled or the password persists in `Sysprep.xml` indefinitely (*"To ensure that this password persists, edit this setting."*). Changelog corroborates a real historical gap: v2.0.146 *"Erases static password if no public key detected"*; v2.0.1881 (May 2024) *"Added an encrypted password option to setAdminAccount… CLI command to encrypt static password in agent-config.yml."* **Doc gap:** current `ec2launch-v2-task-definitions.md` still documents only `password.type: static|random|doNothing` — the safer encrypted option (2.0.1881) is undocumented on the task-definition page, so operators can't discover it.
- **Confirm/Refute oracle:** Build an AMI with `setAdminAccount`/`Specify` and `CreateImage` on an instance that has **not** completed the Sysprep+cleanup cycle (interrupted mid-flow, or legacy EC2Config with the persist flag flipped); inspect the resulting AMI's `agent-config.yml` / `Sysprep.xml` for a recoverable password. Clean `ec2launch sysprep` flow = control (should be scrubbed).
- **Preconditions/Cost:** An AMI-bakery/CI pipeline that races `CreateImage` against Sysprep cleanup, OR a legacy EC2Config AMI, OR any such AMI/snapshot later **shared** (public/org/account). **Chains to Lens AA:** unshare/deregister does **not** retroactively scrub copies already made — one-way disclosure.
- **Severity:** High–Critical for any consumer of a shared/public AMI built this way; routes entirely around the (already-refuted) `GetPasswordData` IDOR control.

**L3 — Baked-on-AMI user-data / tasks = shared-AMI SYSTEM supply chain (Lens AA, NEW/changed surface). Severity: High.**
- **Claim:** EC2Launch v2's **"Local user data baked on AMI — Yes, configurable"** and **"Task configuration in user data — Yes"** (v1/EC2Config: No, per `configure-launch-agents.md` compare table) mean a shared-AMI author's task list/user-data executes as **SYSTEM** on every consumer's first boot, surviving AMI malware scanners that don't parse `agent-config.yml` as executable content.
- **Oracle:** Bake a task into an AMI's local user-data, share it, launch as consumer, confirm it runs as SYSTEM with no consumer gate beyond the normal AMI-share prompt. **Severity:** High (supply-chain RCE-as-SYSTEM); flagged as **v2-only widening** of the "untrusted AMI" risk class → Step-5 new-surface priority.

**L4 — `ec2:ModifyInstanceAttribute(userData)` = SYSTEM code-exec with no PassRole (Lens B/E variant). Severity: Critical (when instance profile attached).**
- **Claim:** Setting user-data is a full SYSTEM-code-exec primitive, no `iam:PassRole` touched. `user-data.md` + `ec2launch-v2-task-definitions.md`: `executeScript`/`executeProgram` tasks run `runAs: localSystem|admin`; `<persist>true</persist>` re-runs every boot. A principal with only `ec2:ModifyInstanceAttribute` (+ stop/start) on an instance carrying a privileged instance profile gets SYSTEM, then harvests that role's creds from IMDS.
- **Oracle:** IAM-policy exercise — grant only `ec2:ModifyInstanceAttribute`+`Stop/StartInstances`, set `runAs: localSystem` user-data that reads IMDS role creds; confirm exec + exfil. **Preconditions:** a permission many orgs treat as a "harmless metadata edit." Anchors Objective 2; hinge doc-gap = whether ANY IAM condition key scopes `userData` (resolve `list_amazonec2.html`).

**L5 — Compressed user-data decompression bomb (Lens L). Severity: Low–Medium.**
- `user-data.md`: v2 auto-unzips compressed user-data; no documented decompressed-size/nesting/timeout cap beyond the 60KB compressed field limit. Oracle: high-ratio nested-zip payload near 60KB → observe agent memory/CPU/boot stall; self-DoS at boot, escalates only if it hangs the PreReady→PostReady pipeline (delays/skips `startSsm`).

**L6 — Legacy user-data schema 1.0 SSM-start race (Lens X). Severity: Medium.**
- `ec2launch-v2-settings.md` changelog: user-data v1.0 *"Impacted by a race condition between Systems Manager Agent start and user data tasks"*; v1.1 (default since 2.0.1245) fixed it but 1.0 stays supported for back-compat → older tooling silently re-inherits the race. Legacy-parity footgun.

**L7 — Historical config-folder ACL LPE + non-Clean-upgrade doc gap (Lens E). Severity: High on stale builds.**
- Pre-v2.0.285 (`ec2launchv2-versions.md`: *"Restricts the config folder permissions"*; today's page says restriction is *"to prevent privilege escalation"* — an admission). **Doc gap:** `ec2launch-v2-install.md` non-`Clean` MSI upgrade *"doesn't replace the agent configuration file"* — unstated whether it re-applies folder ACLs → a stale/loose ACL could survive an in-place upgrade. Also v2.0.1702 restricted previously world-readable `Telemetry.log` (carries `AdminPasswordTypeCode` — recon aid chaining into L2).

**L8 — Agent download TOFU (Lens Q/Y). Severity: Informational/Low (doc gap).**
- `ec2launch-download.md` / `ec2launch-v2-install.md`: `Invoke-WebRequest` of the v1 zip / v2 MSI from fixed `s3.amazonaws.com/...` URLs; no operator-facing Authenticode/checksum verification step documented (MSI is likely signed in practice; the *doc* never says to verify). **Scoped to "AWS should document a verification step"** — actually probing the S3 distribution bucket/signing infra = **HARD STOP** (AWS distribution plane), out of scope.

**Area-6 page-local password notes:** `ec2-windows-passwords.md` guides `net user Administrator "{{new_password}}"` — places the new password on the **command line** (process list / PowerShell history exposure). `ResettingAdminPassword.md` / `ResettingAdminPassword_EC2Launchv2.md` reset flows (EC2Launch/EC2Rescue/SSM) — check whether any reset path runs SYSTEM from attacker-influenceable input (cf. [[project_ec2rescue-linux-plan]]).

**Launch-agent null lenses (pages named):** G (no user-suppliable URL/host; `activateWindows`→fixed KMS activation servers, routes→fixed 169.254.169.x — pages: task-definitions, settings, set-dns, subscribe-notifications), H (password is RSA-to-keypair not CMK; Windows-activation "KMS" ≠ AWS KMS), J, K, P, W all null; A/C on `GetPasswordData` already REFUTED by RDP sibling (this slice routes around it via L2 disk remanence); D N/A (no control-VPC in guest-agent model); V minor-only (EC2Launch v1 bakes KMS/metadata routes into AMIs, stale-route footgun). No HARD-STOPs except L8-if-pushed-to-S3.

---
### Detailed leads — Fast Launch / snapshots / drivers (Areas 3, 4, 5) [deep-dive]

**F1 — CROWN JEWEL (of this slice) — SLR `EC2FastLaunchServiceRolePolicy` PassRole is `Resource:"*"`, contradicting the UserGuide; escalation needs only launch-template-mutation rights, NOT `iam:PassRole`. Severity: Critical primitive — but credential-harvest endpoint = HARD STOP.**
- **Claim:** `AWSServiceRoleForEC2FastLaunch` can pass **any** role/instance profile in the account, not just ones "whose name contains `ec2fastlaunch`" as `slr-windows-fast-launch.md` states.
- **Mechanism (exact doc-vs-live-policy mismatch):** `slr-windows-fast-launch.md` IAM bullet: *"…get and use instance profiles whose name contains `ec2fastlaunch`, and to launch instances on your behalf using the instance profile from your launch template."* But the **live `EC2FastLaunchServiceRolePolicy` JSON (version v7, default, edited 2026-02-12 — post-cutoff)** `AllowPassRole` statement is: `"Action":"iam:PassRole","Resource":"*","Condition":{"StringEquals":{"iam:PassedToService":["ec2.amazonaws.com","ec2.amazonaws.com.cn"]}}` — **no** `StringLike` on an instance-profile-name pattern, **no** `iam:AssociatedResourceArn`, and `AllowRunInstances` is `image/*` with **no `aws:CalledVia`** anywhere. Same "unrestricted PassRole + no CalledVia" shape as the confirmed `EC2FastLaunchFullAccess` finding, here baked into **AWS's own SLR**. Per `win-fast-launch-configure.md` "Permissions checks": with a `$Latest`/`$Default` launch-template alias, EC2 validates permissions **once at enable-time and never rechecks** — doc verbatim: *"someone who can update the launch template could pass an IAM role or instance profile to an instance… even if they don't have the `iam:PassRole` permission for that role."*
- **Net:** weaponizing needs only `ec2:CreateLaunchTemplateVersion`/`ec2:ModifyLaunchTemplate` on the Fast-Launch LT (commonly delegated to CI/CD) — **not** `EC2FastLaunchFullAccess`, **not** `iam:PassRole`. Lowers the privilege bar far below the known finding.
- **Confirm/Refute oracle (read-only):** (1) diff policy v1→v7 via `iam:ListPolicyVersions`+`GetPolicyVersion` to establish whether `AllowPassRole` was **silently broadened** from an `*ec2fastlaunch*` scope to `"*"` (a real regression vs merely loose doc wording); (2) confirm no `CalledVia` (done for v7); (3) in an authorized account, grant a principal only LT-mutation rights, point a Fast-Launch AMI's `$Latest` LT at an admin instance profile, observe the SLR's next `RunInstances` (CloudTrail principal `ec2fastlaunch.amazonaws.com`) carry it.
- **HARD STOP:** actually harvesting creds requires reaching the **ephemeral t3 provisioning instance's IMDS** (30-min lifetime; Fast Launch *forbids* user-data scripts, and the auto-CFN SG is deny-all) — that fleet is AWS's internal provisioning plane. **Report the policy-vs-doc mismatch + the "no-PassRole-needed" precondition to AWS; do NOT pursue live IMDS harvest against the fleet.**
- **Severity:** Critical as a privesc *primitive* + AWS-authored uneditable SLR (Tier-2, route `aws-security`); the doc-vs-policy drift itself is independently reportable (Lens U/R/S).

**F2 — Pre-provisioned snapshot remanence via Recycle Bin (Lens A/Q/M). Severity: Medium (intra-account).**
- `win-ami-config-fast-launch.md` Note (verbatim): Fast Launch deletes pre-provisioned snapshots *"to … prevent reuse. However, if the deleted snapshots match a retention rule, Recycle Bin automatically retains them."* These snapshots are captured **after Sysprep specialize + OOBE** → contain machine SID, computer name, and potentially RDP host key / SSM registration / agent first-boot material.
- **Oracle:** configure a broad EBS-snapshot Recycle Bin retention rule, enable Fast Launch, let a snapshot be consumed, confirm it's retained/restorable, mount it and inventory specialize/OOBE artifacts. **Preconditions:** same-account principal with Recycle Bin restore + a rule broad enough (tag-wildcard) to catch `CreatedBy=EC2 Fast Launch` snapshots. Not cross-account (snapshots aren't shared by default) → Medium. Exact secret types **unconfirmed from docs** — test in authorized account only. Cf. [[project_sysprep-ami-plan]] remanence.

**F3 — Cross-account snapshot-origin transparency gap (Lens A/B/AA). Severity: Low/Informational.**
- `win-ami-config-fast-launch.md`: enabling Fast Launch on a shared AMI creates snapshots in *your* account, but *"If you deplete the snapshots in your account, you can still use snapshots from the AMI owner's account."* `win-view-fast-launch.md` `describe-fast-launch-images` output exposes **no field** saying which account backed a given launch → an operator can't tell they booted from owner-controlled disk content. Trust-transparency gap, not a new escalation beyond running someone's AMI at all.

**F4 — SLR remaining statements audited — NULL (secure).** Live v7 JSON: `AllowKMSActions` = only `kms:ListRetirableGrants` (actual key-use is customer-granted via `kms create-grant --grantee-principal <SLR>` → grant-based delegation, narrow IAM is expected); stop/terminate/snapshot/delete statements all gated on `aws:ResourceTag/CreatedBy="EC2 Fast Launch"` with `AllowCreateTags` gated by `ec2:CreateAction ∈ {CreateSnapshot,RunInstances,CreateLaunchTemplate}` (no forged-tag pre-plant path); EventBridge scoped to `rule/FastLaunch*` + `events:ManagedBy=ec2fastlaunch.amazonaws.com`. **Secondary doc-accuracy note:** the SLR KMS prose ("create grants … describe or use keys … generate data keys") reads broader than the single `kms:ListRetirableGrants` actually present — same doc section as the F1 PassRole drift; flag both as doc-vs-policy accuracy issues.

**F5 — Auto-created CFN stack (no-template path) — NULL (secure defaults).** `win-start-fast-launch-prereqs.md`: VPC + private subnets + IMDSv2-enforced LT + **SG with no inbound/outbound rules** (deny-all = good default, no confused-deputy net path). SLR only holds `cloudformation:DescribeStacks` (read-only).

**F6 — Driver/installer download TOFU (Lens Q/N). Severity: Low–Medium (doc-hygiene).**
- Exact S3 origins, **no documented hash/signature verification step**: ENA `ec2-windows-drivers-downloads.s3.amazonaws.com/ENA/Latest/AwsEnaNetworkDriver.zip`; AWS PV `.../AWSPV/Latest/AWSPVDriver.zip`; NVMe `.../NVMe/Latest/AWSNVMe.zip` + `ebsnvme-id`; VMClock `.../AWSVMClock/Latest/AWSVMClock.zip` (installed via `pnputil /add-driver /install`); AMD buckets `ec2-amd-linux-drivers` / `ec2-amd-windows-drivers` (require customer IAM + `AmazonS3ReadOnlyAccess`). Kernel drivers are protected by Windows WHQL/Authenticode signing, **but the `install.ps1` scripts are not** — a tampered script (via a customer-side rogue proxy/root CA on the TLS path, NOT AWS S3) runs arbitrary PowerShell as Administrator before the signed driver loads.
- **Oracle:** `Get-AuthenticodeSignature` on each `install.ps1`; check for any published SHA256 manifest (none linked from the 7 pages). **Preconditions:** on-path position on the customer's own egress to S3 → customer-side residual risk + doc-completeness gap. **Probing AWS's S3 buckets/signing infra = HARD STOP.** Recommend AWS add a verification step.

**F7 — Optional-components media snapshot authenticity (Lens U/A/X/Q). Severity: Low.**
- Installation media are **intentionally public `OwnerAlias:amazon` snapshots** (example `snap-22da283e`); docs correctly anchor both console (Owner Alias filter `amazon`) and CLI/PS (`--owner-ids amazon`/`-Owner amazon`) on the **non-spoofable owner field**. Description ("Windows 2019 English Installation Media") *is* attacker-settable on an attacker's own public snapshot. **Residual risk = authenticity-filter-omission:** any automation/runbook that matches on **description substring only** (dropping the `amazon` owner anchor) would surface an attacker look-alike. Windows DISM/servicing enforces Microsoft file signatures on actual feature install → narrows real code-exec to an operator manually executing from the mounted untrusted volume. **Oracle:** publish a benign canary public snapshot with that description from a second self-owned account, confirm a description-only `DescribeSnapshots` surfaces it; confirm owner-id/alias is unforgeable (it is → the documented procedure, followed exactly, is a null lens). **Do not impersonate AWS to real consumers — canary only.**

**Fast-Launch/driver null lenses (pages named):** auto-CFN defaults (F5), SLR KMS + tag-gated CRUD + EventBridge (F4), public-snapshot procedure-as-documented (F7), EventBridge monitoring (`win-fast-launch-monitor.md`, outward-only). HARD-STOPs: t3 provisioning-fleet IMDS (F1 exploitation), S3 distribution/signing infra (F6).


---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| In-guest non-admin writes agent config/task → SYSTEM | EC2Launch v2/v1, EC2Config | File ACLs on config/task paths; service runs as LocalSystem |
| `ModifyInstanceAttribute(userData)` → SYSTEM exec with no PassRole gate | User-data execution | "only the launcher can set user-data" — is there any IAM condition key? |
| Shared/Marketplace AMI bakes SYSTEM code (user-data/config/Sysprep hook/driver) | AMI supply chain | Consumer trust in AMI author; Sysprep guidance |
| `EC2FastLaunchFullAccess` → account admin | Managed policy | `PassedToService` condition only (insufficient) — CONFIRMED |
| Admin instance profile named `*ec2fastlaunch*` passed by SLR | `EC2FastLaunchServiceRolePolicy` | Name-substring scope on `iam:PassRole`/GetInstanceProfile |
| Retained pre-provisioned snapshot read after "deletion" | Fast Launch + Recycle Bin | "deletes … to prevent reuse" vs Recycle Bin retention note |
| Poisoned public snapshot selected as installation media | Optional components | Owner Alias = `amazon` filter (advisory; description is spoofable) |
| Unsigned/poisoned driver installed as Administrator | Device drivers | Published hash/signature (to be verified per page) |
| Default Administrator password recovered post-launch | Password generator | RSA to key pair; `GetPasswordData` scoping (RDP sibling) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **AWS service-plane internals** — the Nitro hypervisor, the EC2 Fast Launch temporary **t3 provisioning fleet**, the AMI/driver **build** pipeline, and the `ec2fastlaunch.amazonaws.com` backing infrastructure. Any credential/ARN/account from these = **HARD STOP / disclosure-only**.
- **WSL internals** — WSL1/WSL2 and the Linux guest are Microsoft + customer shared-responsibility; nothing AWS-enforced on this page. The only EC2-relevant hook is that WSL2 requires the `NestedVirtualization` CPU option — nested-virt security is covered elsewhere, not here.
- **IMDS on the managed host** — out of scope as a service-plane concern; the in-scope use is the *customer's* instance profile creds reachable from SYSTEM user-data (Area 2), which is a customer-IAM composition issue.
- **Customer-authored** agent configs / launch templates / IAM policies that the customer wrote themselves = least-privilege footguns (Low/Info). **Carve-out:** `EC2FastLaunchFullAccess` and `EC2FastLaunchServiceRolePolicy` are **AWS-authored and uneditable** → in scope, Tier-2, route `aws-security`.
- **Single-tenant self-DoS** (e.g. exhausting your own Fast Launch parallel-launch quota) — out of scope.
- **Product/feature-parity gaps** (EC2Config being legacy/unsupported) — informational only.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens F (translation/wire-protocol injection):** null — no query/translation layer on these pages. Pages checked: all Section-2 children. (The v2 YAML/JSON config parser is covered under Lens Q/K deserialization in Area 1, not F.)
- **Lens H (KMS/encryption-context confusion):** partially fires only via Fast Launch's `kms:CreateGrant` to the SLR for encrypted AMIs (Area 3 deep-dive) — otherwise null; installation-media snapshots are unencrypted. Pages checked: `slr-windows-fast-launch.md`, `windows-optional-components.md`.
- **Lens J (OAuth/3P linking):** null — no 3P OAuth linking on these pages. Pages checked: all children.
- **Lens V (network segmentation):** the Fast Launch auto-CFN SG with "no inbound or outbound rules" is fail-closed; no customer-reachable cross-tenant segment documented. Pages checked: `win-start-fast-launch-prereqs.md`.
- **Lens W (attestation-conditioned authz):** null on this page (NitroTPM/Secure-Boot attestation is covered in [[project_nitrotpm-plan]] / windows-ami-reference siblings). Pages checked: hub + children.
- **Lens P (identity proofing / registration):** null — no registration/KYC/OTP workflow. Pages checked: all children.
- **Doc gaps needing live/source confirmation first:**
  1. **Exact IAM condition keys for `ec2:ModifyInstanceAttribute` `userData`** — the EC2 IAM reference (`list_amazonec2.html`, JS-rendered) must be resolved to confirm whether ANY condition key can scope user-data writes. This is the hinge of Objective 2.
  2. **The literal JSON of `EC2FastLaunchServiceRolePolicy` and `EC2FastLaunchFullAccess`** — pull via `iam:GetPolicyVersion` and audit statement-by-statement (the SLR's `ec2fastlaunch`-name-substring scope and the LT-instance-profile clause are the untested Area-3 hinges).
  3. **File-system ACLs on the EC2Launch v2 config / task-definition paths** — not stated in docs; must be confirmed on a live WS2022+ instance before rating the Area-1 in-guest LPE.
  4. **Driver download origins + published integrity** — per-driver pages must be read to confirm whether a verifiable hash/signature is published (Area 5).
  5. **Pre-provisioned snapshot contents** — whether a Sysprep'd pre-provisioned snapshot contains recoverable machine keys / RDP host keys / cached creds (Area 3, Lens Q/M).

---

## 9. Cross-references (sibling plans)

- [[project_connect-windows-rdp-plan]] — GetPasswordData/GetConsoleOutput ownership-vs-existence; RDP cert MITM → admin-pw capture kill-chain.
- [[project_windows-ami-reference-plan]] — AMI discovery name-squat, Secure-Boot cert script supply chain, the See-also injection lure; this plan closes its long-standing "EC2Launch user-data-as-SYSTEM / admin-pw-gen → EC2 UserGuide" doc-gap.
- [[project_ec2-security-iam-plan]] — source of the CONFIRMED `EC2FastLaunchFullAccess` unrestricted-PassRole privesc.
- [[project_sysprep-ami-plan]] — Sysprep AMI creation remanence (cleartext admin pw, CopyProfile, SYSTEM hooks) — directly relevant to Fast Launch pre-provisioned snapshots.
- [[project_ec2rescue-linux-plan]] — EC2Rescue reset-tool pattern (relevant to `ResettingAdminPassword`).
- [[aws-docs-see-also-injection]] — the injected agent-toolkit block (absent on this live hub 2026-09-12; watch for reappearance).
