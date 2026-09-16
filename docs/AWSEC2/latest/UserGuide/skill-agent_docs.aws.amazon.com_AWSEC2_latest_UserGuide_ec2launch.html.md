# EC2Launch v1 (Windows launch agent) — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch.html` (main) + children
`ec2launch-config.html`, `ec2launch-download.html`, `ec2launch-version-details.html`, and the referenced
`ec2launch-sysprep.html`. Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2launch*.md`.
**Live check 2026-09-12:** `ec2launch.md` + `ec2launch-config.md` fetched live, byte-consistent with the offline
mirror; **NO "See also"/agent-toolkit injection block** on these UserGuide pages (cf. the injection block seen on
`windows-ami-reference` siblings — watch for reappearance). Status: documentation-derived hypotheses only; nothing
tested against a live account.

> **What this target is, and how it relates to siblings.** `ec2launch.html` documents **EC2Launch v1** — the
> *PowerShell-based* launch agent shipped on Amazon-managed Windows Server **2016/2019** AMIs (`C:\ProgramData\Amazon\
> EC2-Windows\Launch`). It is the predecessor of EC2Launch **v2** (the compiled agent covered by the sibling
> `ec2launch-v2.html` plan) and one of the three members of the launch-agents family hub (`configure-launch-agents.html`).
> This plan is the **v1 slice**. It deliberately does NOT re-derive the two headline family crown jewels already owned by
> `ec2-windows-instances.html` / `sysprep`-family plans — (a) the Sysprep first-boot blank-password/RDP window, and
> (b) the `EC2FastLaunchServiceRolePolicy` `iam:PassRole Resource:"*"` SLR gap — but cross-references them where the v1
> mechanism composes with them. It focuses on what is **specific to or newly documented for v1**: the version-gated
> config-directory ACL guarantee, the cleartext-`Specify` password remanence and its version-gated `Encrypted`
> mitigation, the SYSTEM scheduled-task exec surface, and the v1 install supply chain.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.**
  Work in priority order; look left and right for adjacent bugs the plan did not anticipate.
- This is an **in-guest, single-account, customer-owned** agent. There is **no shared multi-tenant service fleet** in
  scope here. Lens A (cross-tenant IDOR), C, D/V (network segmentation), F (translation-layer), K (LLM), M, N, W fire
  as explicit **null hypotheses** — see §8. The value is concentrated in **Lens U (guarantee-vs-enforcement, heavily
  version-gated), Q/E (writable-config → SYSTEM exec), T (cleartext-password remanence), B/E-variant (user-data-as-SYSTEM),
  and Y (install supply chain).**
- **HARD STOP:** the S3 download bucket `ec2-downloads-windows`, the EC2Launch **telemetry ingest** endpoint, and the
  AWS-managed AMI build fleet are **AWS-owned service plane**. Do **not** attempt to write to the bucket, poison the
  package, or probe the telemetry sink. The moment evidence points at any AWS-owned identity/credential/endpoint, stop,
  preserve evidence, flag for `aws-security` disclosure.
- The whole target is **customer-side**: findings are either (a) **customer footguns** (out of scope unless they stem
  from an AWS-authored default) or (b) **AWS-authored defect in a shipped artifact** — the `install.ps1`-set ACLs, the
  agent's password-handling logic, the shipped `LaunchConfig.json`/Sysprep answer files, and the version-gated behavior
  are AWS-authored and non-editable-in-spirit → **Tier-2 reportable** when they weaken a documented guarantee.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Non-admin → SYSTEM privilege escalation inside the guest:** demonstrate that a *standard* (non-administrator) local
   account, or a prior tenant of a reused/shared AMI, can cause SYSTEM-context code execution on the next EC2Launch
   scheduled-task run — by writing an executable path or `handleUserData`/script content into a Launch directory file
   that the documented ACL guarantee should have made read-only to standard users.
2. **Recover a cleartext administrator password** from disk/snapshot that the docs say is stored "as clear text" in
   `LaunchConfig.json` before Sysprep, on a version/config that predates or bypasses the `Encrypted` option.
3. **Confirm the SYSTEM user-data exec primitive requires no `iam:PassRole` / no OS credential** — an EC2 principal with
   only `ec2:ModifyInstanceAttribute(userData)` or `RunInstances` executes attacker PowerShell as SYSTEM (composes with
   the shared-AMI baked-user-data supply chain).
4. **Trace each documented security guarantee to its enforcing mechanism** and find where the guarantee is version-gated,
   set only by `install.ps1`, or advisory-only — so an AMI on an older agent, or one where `install.ps1` was not re-run,
   silently lacks it.
5. **Assess the v1 install/download supply chain** (TOFU, no published hash/signature, Server-2016 manual-TLS-1.2
   window) — *observationally only*; the bucket is AWS-owned (hard stop on any write attempt).

---

## 2. Components, Assets, and Design

**Interface / mechanism.** EC2Launch v1 is **not an API** — it is a set of Windows PowerShell scripts + a settings
`.exe`, installed under `C:\ProgramData\Amazon\EC2-Windows\Launch`, driven by JSON config files and invoked as **Windows
Scheduled Tasks** during instance boot. The only *AWS-API* touchpoints are indirect: `ec2:ModifyInstanceAttribute` /
`RunInstances` deliver **user data** the agent executes, and `ec2:GetPasswordData` retrieves the encrypted admin password
the agent set. There is no EC2Launch-v1-specific IAM action or condition key.

**Processes / execution context.**
- `InitializeInstance.ps1` — the main init task; reads `LaunchConfig.json`; runs the default tasks (rename, wallpaper,
  DNS suffix, extend boot volume, **set admin password**, **execute user data**, set persistent metadata/KMS routes).
  Scheduled via `-Schedule` (once) or `-SchedulePerBoot` (every boot). **Runs as SYSTEM** (Windows Scheduled Task from a
  privileged installer; not stated verbatim but implied by its ability to set the local admin password and execute
  user data — treat "runs as SYSTEM/LocalSystem" as the working assumption; confirm at test time).
- `InitializeDisks.ps1` — reads `DriveLetterMappingConfig.json`; initializes/partitions/maps volumes (`-Schedule` = per boot).
- `SendEventLogs.ps1` (reads `EventLogConfig.json`), `SendWindowsIsReady.ps1` — console-log tasks.
- `SysprepInstance.ps1` / `BeforeSysprep.cmd` / `SysprepSpecialize.cmd` / `unattend.xml` — image-prep, run in the AMI build path.
- `Ec2LaunchSettings.exe` (in `\Settings`) — GUI wrapper.
- `install.ps1` — the installer; **sets the directory/file ACLs** (per version 1.3.2004592).

**Directory structure (assets).** `\Scripts` (the PowerShell), `\Module` (Ec2Launch.psm1/.psd1), `\Config`
(`LaunchConfig.json`, `DriveLetterMappingConfig.json`, `EventLogConfig.json` — the customer-editable inputs the SYSTEM
tasks read), `\Sysprep` (answer + batch files), `\Settings` (the GUI exe), `\Library` (shared libs for EC2 launch agents),
`\Log` (incl. `UserdataExecution.log`). **These files ARE the attack surface** — a SYSTEM-context task reading a file
that a lower-privileged principal can write is the whole game.

**Identity / secrets.**
- **Administrator password.** `adminPasswordType` ∈ {`Random`, `Specify`, `DoNothing`} (task-definition prose) — GUI names
  them Random/Specify/DoNothing too. `Random` → agent generates + encrypts under "the user's key" (the EC2 key pair), then
  auto-disables (→ `DoNothing`). `Specify` → **stored in `LaunchConfig.json` as CLEAR TEXT** until Sysprep sets it, then
  deleted; also encrypted "using the user's key". `DoNothing` → uses `unattend.xml`; if none, **admin account disabled**.
  Version 1.3.2004891 (May 2024) added an `Encrypted` option + `SetAdminPasswordConfig.ps1` to convert `Specify`→`Encrypted`,
  and made the Settings-UI encrypt by default. In-memory password encryption was only added in 1.3.2003824/…3857 (Aug–Oct 2022).
- **RDP certificate thumbprint**, **instance metadata**, **telemetry** — sent to EC2 console / AWS.

**Untrusted-data entry points (transform seams).** (1) User data → `handleUserData` → **PowerShell executed as SYSTEM**.
(2) The three JSON config files → parsed by the SYSTEM scheduled tasks. (3) `unattend.xml` / Sysprep answer + batch files
→ executed during image prep. (4) `DriveLetterMappingConfig.json` → drive init logic (potential data-destruction on
mis-detection — see the v2 sibling's `initializeVolume` lead).

```
                         C:\ProgramData\Amazon\EC2-Windows\Launch
   [ EC2 control plane ]        |  \Config\LaunchConfig.json   (handleUserData, adminPasswordType, adminPassword=cleartext)
   ModifyInstanceAttribute ---> |  \Config\DriveLetterMappingConfig.json
   (userData)  / RunInstances   |  \Config\EventLogConfig.json
        |                       |  \Scripts\InitializeInstance.ps1  --(Scheduled Task, SYSTEM)-->  runs tasks + user data
        v                       |  \Sysprep\{unattend.xml,*.cmd}     --(image prep)
   user data blob  ------------>|  \Settings\Ec2LaunchSettings.exe
                                |  \Log\UserdataExecution.log       (ACL'd to Administrators since 1.3.2004438)
   install.ps1  (from S3, AWS-owned)  --sets ACLs on the whole tree (since 1.3.2004592)-->  read-execute only for std users
```

---

## 3. API / Interface Inventory
EC2Launch v1 exposes **no service API of its own**. The relevant *AWS-API* levers (owned by other services, listed so the
hunter routes them correctly) and the *local* interfaces:

| Name | Type | Mutating? | Reachable from | Authorized callers | Functionality / lead |
|---|---|---|---|---|---|
| `ec2:ModifyInstanceAttribute` (userData) | AWS API | Yes | Internet (SigV4) | any principal w/ the action on the instance | Delivers user data the agent runs **as SYSTEM**. **No `iam:PassRole`, no OS cred.** → Area 3 / Lens B-variant |
| `ec2:RunInstances` (UserData) | AWS API | Yes | Internet | launcher | Bakes user data at launch → SYSTEM exec first boot |
| `ec2:GetPasswordData` | AWS API | No | Internet | principal w/ action on instance | Returns encrypted admin pw (decrypt needs the private key). Scoping deferred to `connect-windows-rdp` sibling |
| `LaunchConfig.json` | local file | (input) | in-guest FS / snapshot | whoever can write the file | `handleUserData`, `adminPasswordType`, cleartext `adminPassword` → Areas 1,2,3 |
| `DriveLetterMappingConfig.json` | local file | (input) | in-guest FS | file writer | drive init/map → data-destruction lead (Lens L/U) |
| `EventLogConfig.json` | local file | (input) | in-guest FS | file writer | which logs ship to console |
| `InitializeInstance.ps1 -Schedule/-SchedulePerBoot` | local script | Yes | in-guest | admin (documented) | registers SYSTEM scheduled task |
| `Ec2LaunchSettings.exe` | local exe | Yes | in-guest (GUI) | interactive user | schedules per-boot, Sysprep options |
| `install.ps1` + `EC2-Windows-Launch.zip` | S3 download | — | Internet (in-guest) | anyone | supply chain, sets ACLs → Areas 1,5 / Lens Y |
| Telemetry emit | outbound | — | AWS-owned sink | agent | opt-out via `EC2LAUNCH_TELEMETRY=0` / `install.ps1 -EnableTelemetry:$false`. **HARD STOP** on the sink |

There is **no undocumented control-plane knob** here (no API). The "hidden knob" analog is the set of config-file fields
and the **version-gated behaviors** in the version-history table — treat each version-history security bullet as a
statement of "what was broken before this version," i.e. a lead against any AMI/agent older than that version.

---

## 4. Boundary-lens catalog — firing lenses

### AREA 1 (TOP) — Config-directory ACL: documented guarantee, version-gated + installer-set enforcement (Lens U / Q / E)
**Background.** The v1 install changelog states (version **1.3.2004592**, 2 Jan 2024): *"Updated access permissions set by
`install.ps1` for `%ProgramData%\Amazon\EC2-Windows\Launch`. Restricted EC2Launch folder/file access to **read-execute only
for standard user accounts**."* Separately (version **1.3.2004438**, 4 Oct 2023): *"Limited `UserdataExecution.log`
permissions to `Administrators` only."* The main page's directory-structure note points at these permissions. The SYSTEM
scheduled task (`InitializeInstance.ps1`) reads `LaunchConfig.json` and, when `handleUserData`/scripts are configured,
executes content in a privileged context.

**Security Concern.** The privilege-escalation guarantee ("standard users get read-execute only") is (a) **set by
`install.ps1` at install time, not by the OS/AMI baseline**, and (b) **only present from Jan 2024 onward**. Therefore:
- An AMI whose baked EC2Launch predates 1.3.2004592, **or** one where a custom image was captured before the newer
  `install.ps1` re-ran, **or** where a customer overwrote the ACLs, leaves `\Config` (and `\Scripts`) **writable by
  standard users**. A non-admin who writes a `handleUserData:true` + malicious user-data path, or edits a scheduled
  script, gets **SYSTEM execution on the next boot / next scheduled run** = local privesc.
- "read-**execute** only" is a specific ACL claim — verify it actually denies **write** to `LaunchConfig.json`,
  `DriveLetterMappingConfig.json`, `EventLogConfig.json`, every `.ps1` in `\Scripts`, the Sysprep `.cmd` files, and the
  `Ec2LaunchSettings.exe` binary. A single writable script or a writable scheduled-task definition is a SYSTEM primitive.
- Contrast with the **v2** sibling, where only the `config` dir carries the documented restriction and `state`/`sysprep`/
  `wallpaper`/`log` do not (see `[[project_ec2launch-v2-plan]]`). For **v1** the changelog phrases the restriction over the
  *whole* `Launch` tree — so the v1 question is **enforcement completeness + version-gating**, not scope.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** On an Amazon-managed Windows Server 2016/2019 AMI with EC2Launch **older than 1.3.2004592**, a standard user
  can write `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\LaunchConfig.json`. → **Oracle:** `icacls` shows a
  write/modify ACE for `Users`/`Authenticated Users`/a standard SID on the file, or a test write succeeds; then a crafted
  `handleUserData:true` + attacker user-data executes as SYSTEM on next scheduled run (or `InitializeInstance.ps1` is
  re-scheduled). Confirm the executing token is SYSTEM. **Refute:** ACL denies write to standard users on all agent
  versions in scope.
- **Claim:** Even on ≥1.3.2004592, one or more of the SYSTEM-executed scripts under `\Scripts`, the Sysprep `.cmd` files,
  or the scheduled-task XML in `C:\Windows\System32\Tasks` is writable by a non-admin, defeating the guarantee. →
  **Oracle:** `icacls` write ACE + SYSTEM exec on next run.
- **Claim:** The ACL is set by `install.ps1`, so re-imaging/AMI-capture or a partial install can leave the tree with
  default `ProgramData` inheritance (writable by `CREATOR OWNER`/authenticated users for newly-created files). →
  **Oracle:** capture an AMI, relaunch, inspect ACLs vs a fresh `install.ps1` run.

**Doc evidence:** `ec2launch-version-details.md` (1.3.2004592, 1.3.2004438); `ec2launch.md` directory-structure note;
`ec2launch-config.md` (`handleUserData`, scheduled-task steps). **Severity-if-true:** non-admin→SYSTEM local privesc =
**High**; because the ACL is **AWS-authored (`install.ps1`)** and the guarantee is documented, an enforcement/version-gating
gap is **Tier-2 reportable**, not merely a customer footgun. **Doc-gap:** the *actual* NTFS DACLs, the scheduled-task
principal (SYSTEM vs Administrators), and the task-definition file ACLs are **not printed in the docs** — confirm surface
in-guest first.

### AREA 2 — Cleartext `Specify` admin-password remanence; version-gated `Encrypted` mitigation (Lens T / U)
**Background.** `ec2launch-config.md` and `ec2launch-sysprep.md` state, for `adminPasswordType: Specify`: *"The password is
stored in `LaunchConfig.json` as **clear text** and is deleted after Sysprep sets the administrator password."* Version
**1.3.2004891** (31 May 2024) *"Added an `Encrypted` password option to `LaunchConfig.json`; Changed Settings UI behavior to
encrypt the user specified password by default; Added `SetAdminPasswordConfig.ps1` to convert the `Specify` password option
to the `Encrypted` password option."* In-memory password encryption only arrived in 1.3.2003824/3857 (Aug–Oct 2022).

**Security Concern.** A caller who obtains the disk contents — via an **EBS snapshot** (shared or made public),
`CreateStore`/`RestoreImageTask` .bin, a stopped-instance volume attach, a captured AMI, or in-guest read if ACLs are weak
(Area 1) — recovers the **cleartext local administrator password** for any instance provisioned with `Specify` on an agent/
config that predates or does not use the `Encrypted` option. The mitigation is **version-gated and opt-in**: older agents
have no `Encrypted` option; the conversion (`SetAdminPasswordConfig.ps1`) is a manual/Settings-UI step. Note the window: the
password lives in the file until **Sysprep** runs — on an instance that never re-Syspreps (a long-lived server configured
with `Specify`), the cleartext may persist indefinitely.

**High-level Test Scenarios.**
- **Claim:** A `Specify`-provisioned instance on EC2Launch <1.3.2004891 leaves the admin password in cleartext in
  `LaunchConfig.json`, recoverable from a snapshot/volume without the EC2 key pair. → **Oracle:** create snapshot →
  restore/attach → read `\Config\LaunchConfig.json` → `adminPassword` present in cleartext. **Refute:** the field is empty/
  encrypted, or deleted, on all in-scope versions.
- **Claim:** The `Encrypted` option / Settings-UI default does not retroactively scrub a previously-written cleartext value
  from disk remanence (deleted-but-not-overwritten). → **Oracle:** carve free space / VSS shadow for the prior value.
- **Chain:** Area 1 (writable/readable config on old agent) + Area 2 = **non-admin reads local admin password** → full
  admin without touching the AWS API. Composes with the **Sysprep first-boot blank-password/RDP window** crown jewel in
  `[[project_ec2-windows-instances-plan]]` (network-unauth admin during the Sysprep boot).

**Doc evidence:** `ec2launch-config.md` (`Specify` clause); `ec2launch-sysprep.md` lines 54/73; `ec2launch-version-details.md`
(1.3.2004891, 1.3.2003824/3857). **Severity-if-true:** local-admin credential recovery = **High** (Medium if only in-guest
read is possible and ACLs already limit it). AWS-authored logic → Tier-2 where the doc's "clear text … deleted after Sysprep"
promise under-delivers (persists past expected window / survives deletion).

### AREA 3 — User-data-as-SYSTEM as a first-class primitive, no PassRole / no OS cred (Lens B-variant / E)
**Background.** Default task list (main page): *"Executes user data (if specified)."* `handleUserData:true` in
`LaunchConfig.json` (default) causes `InitializeInstance.ps1` to run user-data PowerShell. Per-boot: `HandleUserData` resets
to `false` unless the user data sets `persist:true`.

**Security Concern.** Delivering attacker PowerShell to run as **SYSTEM** needs only an EC2 principal with
`ec2:ModifyInstanceAttribute` on the `userData` attribute (on a stopped instance) or `RunInstances` — **no `iam:PassRole`,
no `iam:` on any role, no OS credential**. This is the confirmed non-PassRole-reaches-live-credentials shape from the
catalog's Lens-B variant (`ec2:ModifyInstanceAttribute(userData)` is the exemplar): the resulting SYSTEM shell can read the
instance profile's IMDS credentials, so `ModifyInstanceAttribute(userData)` is *effectively* a role-assumption/PassRole for
the attached instance profile — yet no PassRole gate exists on it. Additionally, **shared-AMI supply chain:** a baked
`LaunchConfig.json` with `handleUserData` + `persist:true`, or a poisoned baked user data, executes on every downstream
launch.

**High-level Test Scenarios.**
- **Claim:** A principal holding only `ec2:ModifyInstanceAttribute` (userData) + `ec2:StartInstances` on a Windows instance
  (no `iam:PassRole`) achieves SYSTEM code exec and IMDS credential theft on next boot. → **Oracle:** set benign canary
  user data (`echo` to a file), start, confirm SYSTEM-context execution + IMDS reachability; do **not** exfiltrate real
  creds. **Refute:** user data is not executed / requires an additional gate.
- **Claim:** There is **no EC2 IAM condition key** that scopes/denies user-data-driven SYSTEM exec (e.g. no
  `ec2:UserData`-shaped key). → **Oracle:** enumerate the EC2 IAM condition keys; absence confirms the gap. (Defer the full
  condition-key audit to `[[project_ec2-windows-instances-plan]]` L4 / `[[project_imds-config-options-plan]]`.)

**Doc evidence:** `ec2launch.md` task list; `ec2launch-config.md` (`handleUserData`, per-boot note). **Severity-if-true:**
effective root-on-instance + instance-profile credential access with no PassRole = **High** (customer least-privilege
footgun for the *IAM design*, but the missing-condition-key is an AWS platform gap worth noting). **This is a shared/known
primitive across the launch-agent family — cross-reference, do not double-count.**

### AREA 4 — Default tasks that mutate host/AMI state: baked metadata/KMS routes, drive-init data destruction, DNS suffix (Lens U / L)
**Background.** Default tasks include *"Sets persistent static routes to reach the metadata service and AWS KMS servers,"*
with the **Important** note: *"If a custom AMI is created from this instance, these routes are captured as part of the OS
configuration and any new instances launched from the AMI will retain the same routes, regardless of subnet placement."*
`InitializeDisks.ps1` + `DriveLetterMappingConfig.json` initialize/partition volumes. `addDnsSuffixList` adds
`{{region}}.ec2-utilities.amazonaws.com` (routes to `[[project_configure-launch-agents-plan]]` Area 2 for SearchList poisoning).

**Security Concern.**
- **Baked routes → availability/routing integrity:** an AMI captured without re-running the Sysprep/EC2LaunchSettings
  route-refresh (documented `update-metadata-KMS` step) carries **subnet-specific static routes** to IMDS/KMS into every
  downstream instance regardless of its subnet. If those routes point at an address only valid in the origin subnet, IMDS/
  KMS reachability breaks (self-DoS); the *interesting* variant is whether a route baked toward an attacker-influenceable
  next-hop could redirect IMDS/KMS traffic on a downstream instance — likely no (link-local IMDS is fixed), so this is
  mostly an **availability / mis-provisioning** issue, not a redirection primitive. Rate **Low/Informational** unless a
  redirection path is demonstrated.
- **Drive-init empty-detection:** mirror the v2 `initializeVolume` lead — a non-empty volume mis-detected as empty could be
  initialized/wiped. If a malicious `DriveLetterMappingConfig.json` or a mis-detection is baked into a shared AMI →
  **data destruction** on downstream launches. Confirm the empty-detection logic in-guest.

**Doc evidence:** `ec2launch.md` (Important route note); `ec2launch-config.md` (`DriveLetterMappingConfig.json`,
`InitializeDisks.ps1`); `ec2launch-sysprep.md` (`update-metadata-KMS`). **Severity-if-true:** data destruction on shared
AMI = High; baked-route availability = Low/Informational. **Doc-gap:** the drive empty-detection heuristic is not in docs.

### AREA 5 — v1 install / download supply chain (Lens Y) — observational only, AWS-owned bucket = HARD STOP
**Background.** `ec2launch-download.md` instructs downloading `EC2-Windows-Launch.zip` and `install.ps1` from
`https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/…` and running `install.ps1`. **No published SHA/signature**
in the doc. Server 2016 note: manually enable **TLS 1.2** for the PowerShell session
(`[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`) — i.e. the default may negotiate
**below TLS 1.2**.

**Security Concern.** Trust-on-first-use install with no integrity verification: the customer runs whatever the zip/`install.ps1`
contains, as administrator, and it **sets the ACLs** for the whole tree (Area 1). The TLS-1.2-must-be-enabled-manually note
means the pre-1.2 negotiation window is a **downgrade/MITM** opportunity for the download on Server 2016 (network-position
required). **However:** the bucket and package are **AWS-owned service plane**. This lens is **observational** — verify only
(a) whether the doc omits an integrity check that ought to exist, and (b) the TLS floor of the documented download. **Do NOT
attempt to write to `ec2-downloads-windows`, tamper with the package, or MITM a real download.** The moment any AWS-owned
credential/endpoint is implicated → stop, flag for disclosure.

**High-level Test Scenarios.** **Claim:** the documented install path publishes no hash/signature and permits sub-TLS-1.2
negotiation on Server 2016 → integrity/downgrade gap in an AWS-authored procedure. → **Oracle:** doc review + passive TLS
handshake observation of the documented URL (no tampering). **Severity-if-true:** supply-chain integrity gap =
Informational–Medium (AWS-owned procedure defect; disclosure-worthy, not exploitable by the tester).

### AREA 6 — Password lifecycle edge cases & fail-open (Lens U)
**Background / claims (from config + version history):**
- **`Specify` fail-open to Random:** *"If the password does not meet the system requirements, EC2Launch generates a random
  password instead."* → a caller who sets a weak `adminPassword` silently gets an agent-generated one; benign, but confirm
  no path leaves the account with a **known/blank** password on invalid input.
- **`DoNothing` + no `unattend.xml` password → admin account DISABLED** — confirm this does not instead leave a **blank-
  password enabled** account (composes with the Sysprep first-boot blank-pw window crown jewel).
- **Per-boot `Random` → auto-`DoNothing`:** after one per-boot generation the type flips to `DoNothing`; a subsequent boot
  will not rotate — is the last-generated password recoverable/predictable? (In-memory encryption only since 1.3.2003824.)
- **Fast-launch interaction:** version 1.3.2003961 fixed *"explicitly specified administrator passwords … overwritten with a
  random password on fast-launched instances."* → on older agents a `Specify` password on a Fast-Launch AMI may be silently
  replaced — an availability/expectation gap, and a hint that Fast Launch and EC2Launch password logic interact (route Fast
  Launch itself to `[[project_ec2-windows-instances-plan]]` / `[[project_ec2-security-iam-plan]]`).
- **Password complexity:** 1.3.2003411 *"Changed password generation logic to exclude passwords with low complexity"* — pre-
  this-version generated passwords had lower complexity (predictability lead against very old AMIs).

**Oracle:** provision each password type on representative agent versions; inspect the resulting account state
(`net user Administrator`) and any on-disk/in-memory password material. **Severity:** blank/known-password on invalid input
= High; predictability on ancient agent = Medium; expectation gaps = Low.

---

## 5. Prioritized lead order
1. **Area 1** — config/script/task ACL enforcement completeness + version-gating → non-admin→SYSTEM (**High**, AWS-authored ACL).
2. **Area 2** — cleartext `Specify` password remanence, version-gated `Encrypted` mitigation (**High**, snapshot/volume recovery).
3. **Area 3** — user-data-as-SYSTEM, no PassRole/no OS cred (**High**; shared primitive — cross-reference).
4. **Area 6** — password-lifecycle fail-open / blank-account edge cases (**High** if blank/known; composes with Sysprep window).
5. **Area 4** — drive-init data destruction (**High** on shared AMI) / baked routes (**Low**).
6. **Area 5** — install supply chain (**Info–Medium**, observational, HARD STOP on the bucket).

**Kill chain to compose:** Area 1 (writable `\Config` on pre-2024 agent) → Area 2 (read cleartext admin pw) **or** Area 3
(inject `handleUserData` → SYSTEM) → full local admin/SYSTEM with **zero AWS-API privilege and no OS credential**; then IMDS
→ instance-profile credentials. Rate at the chain end (**High**, local privesc + credential access).

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin writes `LaunchConfig.json`/script → SYSTEM exec | `\Config`, `\Scripts`, Scheduled Task | "read-execute only for standard user accounts" (install.ps1, v1.3.2004592) — **version-gated & installer-set** |
| Recover cleartext admin pw from snapshot | `LaunchConfig.json` (`Specify`) | "stored as clear text … deleted after Sysprep"; `Encrypted` option (v1.3.2004891) — **opt-in & version-gated** |
| SYSTEM exec via user data w/o PassRole | `handleUserData` / `InitializeInstance.ps1` | none (no EC2 condition key scoping user-data exec) |
| Blank/known admin account via password-type edge case | password logic | `Specify` fails to Random; `DoNothing` disables account — confirm no blank-enabled path |
| Data destruction via drive-init mis-detection | `InitializeDisks.ps1` / `DriveLetterMappingConfig.json` | empty-only initialization (heuristic not in docs) |
| Tampered/downgraded install | `install.ps1`/zip from `ec2-downloads-windows` | none published (no hash/sig); manual TLS 1.2 on Server 2016 — **AWS-owned, hard stop** |
| `UserdataExecution.log` info leak | `\Log` | "Limited to Administrators only" (v1.3.2004438) — **version-gated** |

---

## 7. Out-of-Scope / Risk Categories
- **No multi-tenant/shared service fleet** — EC2Launch v1 is entirely in-guest, single-account, customer-owned. No Lens-A
  cross-tenant IDOR, no Lens-C credential-vending, no Lens-D/V control-plane/network-segmentation surface here.
- **Customer-authored config as footgun:** a customer who loosens the ACLs, hand-edits `LaunchConfig.json`, or bakes a bad
  AMI owns that risk — **except** where the weakness stems from the AWS-authored `install.ps1` ACLs, agent password logic,
  or version-gated defaults (those are Tier-2, in scope).
- **AWS-owned service plane (HARD STOP):** the `ec2-downloads-windows` S3 bucket, the EC2Launch telemetry ingest endpoint,
  the AWS Windows-AMI build fleet, and the `{{region}}.ec2-utilities.amazonaws.com` service. Do not probe/write/poison.
- **IMDS on the managed host** — treat as out of scope as a target; it is the *sink* of Area 3, not a bug in itself.
- **`ec2:GetPasswordData` / RDP password-decrypt scoping** — deferred to `[[project_connect-windows-rdp-plan]]`.
- **Fast Launch PassRole/SLR crown jewel** — owned by `[[project_ec2-windows-instances-plan]]` / `[[project_ec2-security-iam-plan]]`; only its *interaction* with v1 password logic (Area 6) is noted here.
- **Sysprep first-boot blank-password/RDP window** — owned by `[[project_ec2-windows-instances-plan]]`; composes with Areas 2/6.

## 8. Null hypotheses / doc gaps
- **Lens A / C / D / V / M / N / W — NULL.** Pages checked: `ec2launch.md`, `ec2launch-config.md`, `ec2launch-download.md`,
  `ec2launch-version-details.md`, `ec2launch-sysprep.md`. No shared fleet, no per-tenant resource-by-id, no STS/credential-
  vending, no control ENI / VPC / network segmentation, no session-id/token interception surface, no dual-namespace
  migration, no attestation gate. (User-data delivery uses standard EC2 APIs governed elsewhere.)
- **Lens F — NULL.** No translation/wire-protocol layer; JSON config is parsed by PowerShell (no downstream-language
  transform). (Watch: PowerShell JSON parsing of attacker-controlled config is a possible injection into the SYSTEM script
  — low-probability; note as a doc-gap since the parsing code is not in docs.)
- **Lens K — NULL.** No LLM/agent in the pipeline.
- **Lens H / I / R / S — NULL for this page set.** No IAM policy JSON, managed policy, CFN snippet, KMS key policy, or tag
  API is printed on the EC2Launch v1 pages. (The user-data→instance-profile reach in Area 3 is an IAM *design* gap, audited
  in the Windows-instances plan, not a printed-artifact defect here.)
- **Lens O — LOW.** Telemetry + `UserdataExecution.log` (Administrators-only since v1.3.2004438); `\Log` rotation not
  detailed. Defense-evasion via `sc delete`/uninstall routes to `[[project_configure-launch-agents-plan]]` Area 3.
- **Lens G — routed, not null.** The only server-side-dereference field is `addDnsSuffixList` (SearchList poisoning) → owned
  by `[[project_configure-launch-agents-plan]]` Area 2.
- **Doc gaps to close in-guest FIRST (docs do not print these):** (1) actual NTFS DACLs on `\Config`, `\Scripts`, `\Sysprep`,
  `\Settings\Ec2LaunchSettings.exe`, and the scheduled-task XML; (2) the scheduled-task run-as principal (SYSTEM vs
  Administrators); (3) the drive empty-detection heuristic; (4) whether `Specify` cleartext survives deletion in disk
  remanence; (5) the exact set of agent versions present on current Amazon-managed 2016/2019 AMIs vs the version gates in §4.

---
### Cross-references (memory)
Siblings: `[[project_ec2launch-v2-plan]]` (compiled v2 agent — config-dir ACL scope asymmetry), `[[project_configure-launch-agents-plan]]`
(family hub / DNS / service-admin), `[[project_ec2-windows-instances-plan]]` (Windows config hub — owns Sysprep blank-pw window +
Fast Launch SLR PassRole crown jewels), `[[project_sysprep-ami-plan]]`, `[[project_connect-windows-rdp-plan]]`,
`[[project_imds-config-options-plan]]`, `[[project_ec2-security-iam-plan]]`. Injection-block watch: `[[project_aws-docs-see-also-injection]]`.
