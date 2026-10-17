# EC2 Windows Sysprep / Image-Preparation — Attack Research Plan

**Source of leads:** AWS EC2 Windows UserGuide, offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` and the live docs (`.md` mirror of each `.html`). Primary (seed) page: `sysprep-troubleshoot.html`. Surrounding set read in full: `ami-create-win-sysprep`, `sysprep-using` (EC2Config), `ec2launch-sysprep` (EC2Launch v1), `sysprep-using-ec2launchv2` (EC2Launch v2), `ec2launch-config`, `ec2launch-v2`, `ec2launch-v2-settings`, `ec2launch-v2-task-definitions`, `ec2config-service`, `ec2-windows-passwords`, `connecting_to_windows_instance`, `ResettingAdminPassword{,_EC2Config,_EC2Launch,_EC2Launchv2}`, `building-shared-amis`, `sharingamis-intro`, `sharingamis-explicit`, `cancel-sharing-an-AMI`, `block-public-access-to-amis`. IAM surface from `service-authorization/latest/reference/list_ec2.md`.

**Status:** Documentation-derived hypotheses only. Nothing has been tested against a live account. Severities are "if-true" estimates for a downstream hunter to confirm/refute.

---

## 0. How to use this document

- Each lead is stated as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity-if-true → Scope**. Work the Recommended Areas of Focus (§5) in the priority order given. Look left and right for adjacent bugs the lens didn't name.
- The dominant scope rule for this mechanism: **a customer baking their own secret into their own private AMI is a self-footgun (Low / out-of-scope). It becomes High/Critical when (a) the secret-baking is AWS's *default* agent behavior the customer never opted into, or (b) the AMI is shared cross-account or made public.** Mark every lead against that line.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (Nitro, IMDS credential vending for a service role, the EC2 control plane fleet), stop, preserve evidence, and flag for AWS-Security disclosure. *Note: the entire Sysprep/AMI mechanism analyzed here lives on the customer-owned instance filesystem and the customer's AMIs — no analyzed path reaches AWS's service plane. If one appears, it is unexpected and a hard stop.*

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Recover a usable Administrator credential (cleartext password, blank password, or predictable/un-scrambled password) from an AMI or a running instance you do not own** — especially one obtained by launching a *shared or public* Windows AMI.
2. **Recover another principal's / another account's secret material** (DPAPI secrets, saved credentials, keys, logs) that AWS's default `CopyProfile=True` or un-cleaned logs baked into an image.
3. **Obtain SYSTEM-level code execution on an instance** by writing a Sysprep hook script / answer file / agent task that the privileged image-prep pipeline later executes — and have that execution persist into every instance launched from a derived AMI (supply-chain).
4. **Reach a Windows instance over RDP without credentials** during the documented first-boot blank-password / RDP-open window.
5. **Bypass an intended login/password-retrieval control** (reset or read the admin password using permissions that were meant only for disk/lifecycle management, or a console channel meant to be gated).
6. **Prove that AMI-sharing revocation does not retract already-disclosed secrets** (share-once-leak-forever).

---

## 2. Components, Assets, and Design

### Mechanism (reconstructed from docs)
Windows "golden image" creation generalizes a running instance with Microsoft **Sysprep**, orchestrated by one of three AWS launch agents:
- **EC2Config** (legacy, Windows Server ≤2012R2/2016 era; runs as **LocalSystem**; officially end-of-support).
- **EC2Launch v1** (Windows Server 2016/2019).
- **EC2Launch v2** (Windows Server 2022+; also back-portable).

Each agent reads a **config file** and drives Sysprep through **Generalize → Specialize → OOBE** phases via an **answer file**, running agent-owned **hook scripts** at predictable paths, as SYSTEM. After the instance reaches `Stopped`, the operator captures an **AMI** (EBS snapshot of the root volume), which may be kept private, **shared with specific accounts**, or **made public**, and which recipients can **re-derive** into their own AMIs.

### Key assets / identifiers
| Asset | Where it lives | Why it matters |
|---|---|---|
| Admin password (cleartext, `Specify`/`Keep Existing` mode) | `sysprep2008.xml` (EC2Config), `LaunchConfig.json` (v1), `agent-config.yml`/`unattend.xml` (v2) | Baked into AMI if not scrubbed before capture |
| Admin password (encrypted, `Random` mode) | EC2 **console output**, retrieved via `GetPasswordData` + launch-key private key | Ciphertext leaks via alternate channel (`GetConsoleOutput`) |
| Built-in Administrator **user profile** | Copied into default profile when `CopyProfile=True` (**default**) | DPAPI secrets / saved creds silently distributed to every future login |
| Sysprep/agent **logs** | `%WINDIR%\Panther\Unattendgc`, `%WINDIR%\System32\Sysprep\Panther`, `Ec2ConfigLog.txt`, `EC2Launch.log`, `agent.log` | Baked into AMI; may echo accounts/config |
| **Hook scripts** run as SYSTEM | `BeforeSysprep.cmd`, `SysprepSpecialize(Phase).cmd`, `C:\Windows\Setup\Scripts\SetupComplete.cmd` → `PostSysprep.cmd`, `InitializeInstance.ps1 -Schedule` (next-boot Scheduled Task) | Writable path → local privesc + persistent-code-in-AMI |
| **Answer file** `unattend.xml` | `C:\ProgramData\Amazon\EC2Launch\sysprep\` (v2) | SYSTEM-parsed; v2 writes a registry-sourced `LocaleName` into it (injection seam) |

### ASCII pipeline
```
[Operator/build pipeline] --customize--> [Running Win instance]
        |  choose password mode (Random | Specify | Keep Existing)
        v
  Launch-agent config  (sysprep2008.xml | LaunchConfig.json | agent-config.yml)
        |  ec2config.exe -sysprep  /  ec2launch sysprep
        v
  BeforeSysprep.cmd (fDenyTSConnections=1)  --> sysprep.exe /generalize /oobe /shutdown /unattend:<answer file>
        |                                           |
   GENERALIZE (strip SID/name/domain)          SPECIALIZE (SYSTEM):
                                                 order1 net user Administrator /ACTIVE:YES
                                                 order2 ScramblePassword.exe / randomize-password   <-- the ONLY access-prevention step
                                                 order3 SysprepSpecialize*.cmd (fDenyTSConnections=0)  <-- RDP re-enabled here
        v
   OOBE (answer-file automated) --> SetupComplete.cmd --> PostSysprep.cmd (SYSTEM)
        v
   Instance -> Stopped   ==="safe to create an AMI" (power-state only; NO Sysprep-success gate)===
        v
   [AMI / EBS snapshot]  --launchPermission / Public--> [Other account launches instance] --rebundle--> [Derivative AMI...]
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| AMI recipient account (or the public) | AMI author's secrets at rest | Launch an instance from a **shared/public** AMI → full OS-volume read | Reading the author's cleartext password, admin-profile DPAPI secret, or log content from a launched instance / mounted snapshot = **cross-account disclosure breach** |
| Low-priv local user on an instance | SYSTEM | Write a hook script / answer-file / agent task that image-prep executes as SYSTEM | A payload at a predictable path executing as SYSTEM = **local privesc breach**; if captured into a shared AMI = **supply-chain cross-account breach** |
| Unauthenticated network peer | A freshly-launched Windows instance | RDP during the first-boot blank-password window | TCP 3389 accepts an empty-password `Administrator` logon before `Ec2SetPassword` runs = **credential-less takeover breach** |
| Same-account ops principal (disk/lifecycle rights, no login rights) | Admin login on a "no-login" instance | EBS detach/reattach reset flow; or `GetConsoleOutput` ciphertext channel | Resetting/reading the admin password without `GetPasswordData`/RDP/SSM = **separation-of-duties bypass** |
| AMI author post-revocation | Already-disclosed bytes | `cancel-image-launch-permission` / disable public access | Recipient still reads the secret via a derivative AMI/instance after revoke = **revocation-incompleteness breach** |
| Any customer surface | **AWS service plane** | — | *None expected here.* Any AWS-fleet credential/ARN seen = **HARD STOP** |

---

## 4. API / Interface Inventory (relevant control-plane + local interfaces)

| Name | Type | Mutating | Internet-callable | Authorized callers | Condition keys (from `list_ec2.md`) | Notes / lead |
|---|---|---|---|---|---|---|
| `ec2:GetPasswordData` | EC2 API (Read) | No | Yes | holder on `instance*` | **none** beyond resource/tag family | Encrypted admin password; no cross-account resource policy (Area 3 L8) |
| `ec2:GetConsoleOutput` | EC2 API (Read) | No | Yes | holder on `instance*` | **none** | Same ciphertext leaks here; separate action from GetPasswordData (Area 3 L4) |
| `ec2:CreateImage` | EC2 API (Write) | Yes | Yes | holder on `image*` | `ec2:ImageID/Owner/Region`, tags | AMI capture; `NoReboot` can image a *running* instance |
| `ec2:ModifyImageAttribute` | EC2 API (**Permissions mgmt**) | Yes | Yes | image owner | image family incl. **`ec2:Public`**, `ec2:Owner` | launchPermission / make-public; `ec2:Public` SCP can block public (Area 1 L5) |
| `ec2:CancelImageLaunchPermission` | EC2 API (Write) | Yes | Yes | — | image family incl. `ec2:Public` | Revoke; does not retract derivatives (Area 1 L6) |
| `ec2:CopyImage` / `RegisterImage` / `CreateRestoreImageTask` | EC2 API (Write) | Yes | Yes | — | varies | Re-derivation / cross-region propagation of baked secrets |
| `ec2:ModifyInstanceAttribute` | EC2 API (Write) | Yes | Yes | holder on `instance*` | incl. `ec2:Attribute/${AttributeName}` | `userData` attribute → SYSTEM exec on next boot (adjacent to Area 2) |
| `ec2launch sysprep` / `ec2config.exe -sysprep` / `SysprepInstance.ps1` | Local CLI (SYSTEM) | Yes | No | local admin | n/a | Entry point into the SYSTEM-context hook chain |
| `executeScript` / `executeProgram` tasks | EC2Launch v2 `agent-config.yml` | Yes | No | `runAs: localSystem`/`admin` | n/a | `-ExecutionPolicy Unrestricted` default, no integrity check (Area 2 L6) |

**Undocumented/under-surfaced knobs flagged:** `RemoveCredentialsfromSyspreponStartup` (EC2Config `Config.xml`) can be *disabled* to deliberately retain the cleartext password; `CopyProfile=True` default is in the answer file, not the console; the `executeScript` `-ExecutionPolicy Unrestricted` default is only in the task-definition reference.

---

## 5. Recommended Areas of Focus

Priority: §5.1 and §5.3-L1/L5 are the highest-blast-radius, cheapest-to-test leads. Cross-account/shared-AMI leads outrank single-tenant ones of the same mechanism.

### 5.1 Secrets baked into AMIs → cross-account / public disclosure  (Lenses T, Q, A, AA, U)

**Background.** Three independent AWS *default or documented* behaviors deposit secrets on the root volume at image-prep time; AMI sharing then grants full OS-volume read to other accounts, and revocation does not retract what was copied.

**Security Concern.** AWS's "safe to create an AMI" checkpoint is defined purely by **power state (`Stopped`)**, never by Sysprep success or a secret-scrub, and the AMI-sharing path performs **no secret-content gate**.

**High-level Test Scenarios (falsifiable claims):**
- **[L1 — High/Critical-if-shared] Cleartext password survives capture.** *Claim:* the cleartext admin password in `sysprep2008.xml`/`LaunchConfig.json`/`agent-config.yml` is still on disk at capture. *Mechanism:* docs say it is "deleted after Sysprep sets the password" / "when the service **starts again**" — but the documented flow only **shuts down**, never restarts, before "safe to create an AMI." *Oracle:* mount a stopped-&-imaged `Specify`-mode instance's volume; grep the config file for the literal password. *Scope:* Low same-account; **Critical** when shared/public.
- **[L2 — High-if-shared] No Sysprep-success gate.** *Claim:* an instance where Specialize errored (e.g. the troubleshoot page's `CopyProfile failed 0x80070003`) before `ScramblePassword` ran can still be imaged. *Mechanism:* "safe to image" = `Stopped` only; no exit-status / Panther-log / `IMAGE_STATE_UNDEPLOYABLE` check documented. *Oracle:* force a Specialize fault, reach `Stopped`, image, launch, test for blank/previous admin password. *Scope:* escalates with sharing.
- **[L3 — Critical-if-shared] `CopyProfile=True` default bakes the admin profile.** *Claim:* AWS's default copies the built-in Administrator profile (DPAPI secrets, saved/RDP creds, cached logons) into the default profile; every future login silently inherits a copy. *Mechanism:* `sysprep-using*.md` — "The default value is True … All accounts that you log in to after running Windows Sysprep receive a copy of that profile and its contents at first login." *Oracle:* seed a Credential-Manager/DPAPI artifact in the admin profile, image with default settings, launch, log in as a *different* account, check for the inherited artifact. *Scope:* AWS-default (in-scope even same-account as a default defect); Critical when shared.
- **[L4 — Medium-if-shared] Logs baked in.** *Claim:* Panther/`EC2Launch.log`/`agent.log` persist into the AMI with no documented cleanup; may echo accounts/config/passwords. *Oracle:* inspect imaged volume for the listed log paths and grep for L1's password string, domain/account names.
- **[L5 — Critical] Sharing has no secret-content gate.** *Claim:* the only automated blocks on public sharing are encrypted volumes/snapshots/product codes — never a secret scan; recipients get a full-filesystem launch. *Oracle:* share an AMI containing an L1/L3 artifact; from a second account launch and read it. *Scope:* cross-account by construction.
- **[L6 — High] Revocation doesn't retract derivatives.** *Claim:* after a recipient launches + re-derives an AMI, `cancel-image-launch-permission` / block-public-access does not retract the already-copied secret (docs: "after they have launched an instance … they can then create an AMI"; "if you already have public AMIs, they remain publicly available"). *Oracle:* share→recipient re-derives→owner revokes→recipient's derivative still exposes the secret.
- **[L7 — Informational] Doc asymmetry (Lens U).** `building-shared-amis.md` (Linux) has explicit "remove sensitive data / SSH host key" guidance **and a stated AWS auditing process that marks leaky AMIs private**; the Windows Sysprep page set has **no** equivalent for `CopyProfile`/cleartext passwords/logs. The absence is the root cause that makes L1–L6 practical. *Secondary open question for AWS-Security:* does AWS's shared-AMI auditing pipeline scan Windows AMIs for these artifacts? (not doc-observable).

**Doc evidence:** `ec2launch-config.md`, `ec2launch-v2-settings.md`, `sysprep-using.md`, `sysprep-using-ec2launchv2.md`, `sysprep-troubleshoot.md`, `sharingamis-intro.md`, `sharingamis-explicit.md`, `cancel-sharing-an-AMI.md`, `block-public-access-to-amis.md`, `building-shared-amis.md`.
**Severity-if-true:** Critical (L5, L3-shared, L1-shared), High (L2, L6), Medium (L4), Informational (L7).

### 5.2 SYSTEM privesc & persistent-code-in-AMI via Sysprep hooks/tasks  (Lenses E, B, Q/supply-chain, R-variant)

**Background.** The hook scripts, answer file, and agent tasks all run as SYSTEM/LocalSystem from predictable `C:\ProgramData\Amazon\…` and `C:\Program Files\Amazon\…` paths and are baked into the AMI.

**Security Concern.** AWS's own docs name "writable config dir ⇒ privilege escalation" as a risk and harden exactly **one** folder — the EC2Launch v2 `config` folder — while saying nothing about the sibling `sysprep`/`log`/`state` folders or the v1/EC2Config trees that hold the SYSTEM-executing hooks.

**High-level Test Scenarios:**
- **[L1 — Medium→High] EC2Launch v2 `sysprep` folder ACL asymmetry.** *Claim:* `…\EC2Launch\sysprep` (holds `unattend.xml`, `BeforeSysprep.cmd`, `SysprepSpecialize.cmd`) is writable by non-admins because only the adjacent `config` folder carries the documented "restricted to the administrator account to prevent privilege escalation" statement. *Oracle:* compare `icacls …\sysprep` vs `…\config` as non-admin; `BUILTIN\Users` write on `sysprep` confirms. *Scope:* Medium local; **High** on a golden-image build host (SYSTEM code ships in the shared AMI, fires at first boot before any agent/EDR).
- **[L2 — Medium→High] EC2Launch v1 trees carry no ACL claim at all.** `…\EC2-Windows\Launch\{Config,Scripts,Sysprep}` incl. `InitializeInstance.ps1 -Schedule` (creates a next-boot SYSTEM Scheduled Task). *Oracle:* `icacls` the three dirs; `schtasks /query … /v` to confirm the task runs as SYSTEM and its script dir is admin-only.
- **[L3 — Medium→High] Cleartext password + ACL.** Same cleartext-password fact as §5.1-L1 but attacked locally: a non-admin reading `agent-config.yml`/`LaunchConfig.json` before Sysprep scrubs it (ties to L1/L2 ACL question).
- **[L4 — Medium] `SetupComplete.cmd`→`PostSysprep.cmd` native hook.** AWS-populated SYSTEM hook at `C:\Windows\Setup\Scripts\`; likely admin-only by stock Windows ACLs (expect refute) **unless** a build-pipeline installer loosened `C:\Windows\Setup` ACLs. *Oracle:* `icacls` both paths on a legacy EC2Config AMI.
- **[L5 — Medium→High] Legacy EC2Config LocalSystem + EOL.** Entire `EC2ConfigService\{Settings,Scripts}` tree (incl. `ScramblePassword.exe`, `BeforeSysprep.cmd`, `SysprepSpecializePhase.cmd`, `PostSysprep.cmd`) runs as LocalSystem on an EOL agent with zero ACL commitment in docs.
- **[L6 — severity multiplier] `executeScript` runs SYSTEM with `-ExecutionPolicy Unrestricted` default, no signature/integrity check.** Confirmed-in-doc; it removes a defense that would otherwise blunt L1/L2/L5 — not a standalone bug.
- **[L7 — doc-gap] Shipped sample scripts unexamined.** `InstallUpdates.ps1`, the `*.cmd` hook bodies, etc. — pull from a live AMI or the public EC2Launch/EC2Config package and grep for `Invoke-WebRequest`/`http://`/`Invoke-Expression`/hardcoded creds before any exploitation claim.

**Doc evidence:** `ec2launch-v2.md` (directory-structure "restricted to the administrator account"), `ec2launch-config.md`, `ec2launch-sysprep.md`, `ec2config-service.md` ("runs in the LocalSystem account" + EOL), `ec2launch-v2-task-definitions.md` (`-ExecutionPolicy Unrestricted`, `runAs`).
**Severity-if-true:** Medium local-only; High when the write primitive lands on a build host feeding a shared/public AMI. **No HARD STOP** — all instance-filesystem/AMI-content.

### 5.3 Admin-password lifecycle, RDP window, retrieval & answer-file injection  (Lenses M, U, C, F, P, Y)

**Background.** The password-scramble step is the only thing preventing access to a Sysprep'd image; RDP is explicitly re-enabled *within* Specialize before the real per-instance password is set; password reset and ciphertext retrieval have alternate channels.

**Security Concern.** The access-prevention guarantees ("scramble prevents the instance from being accessible", "RDP disabled during the blank-password window") are enforced by orchestration ordering, not by any transactional/fail-closed mechanism, and recur on *every* launch from the baked image.

**High-level Test Scenarios:**
- **[L1 — Critical-if-shared] Recurring blank-password / open-RDP race on every launch.** *Claim:* Specialize re-enables RDP (`fDenyTSConnections=0`, order 3) *before* `Ec2SetPassword`/`SetPassword` (post-Sysprep, parallel) generates the per-instance password — and nothing re-arms `BeforeSysprep.cmd`'s `fDenyTSConnections=1` on the *next* instance's first boot. So the documented "RDP open + blank Administrator password" window reopens on every launch of the AMI. *Oracle:* launch instances from a test Sysprep'd AMI; during first ~60–120 s attempt RDP as `Administrator` empty-password while correlating "Sysprep End" vs "Windows is ready" log timestamps. *Scope:* **Critical** public/shared (any launcher's instance briefly takeover-able by a network peer); High private.
- **[L2 — Critical-if-shared] Cleartext password in a shared AMI** (`Specify`/`Keep Existing`; `RemoveCredentialsfromSyspreponStartup` disabled). Same artifact as §5.1-L1, framed around the EC2Config `RemoveCredentialsfromSyspreponStartup` toggle that an insider can disable to *deliberately* retain the password.
- **[L3 — Critical-if-shared] Partial Sysprep leaves RDP on + password un-scrambled.** The three Specialize synchronous commands are not documented as transactional; a `CopyProfile` fault between order 1 and order 2 can skip the scramble while order 3 (or OOBE) still re-enables RDP → known pre-Sysprep password + open RDP ships in the image.
- **[L4 — Medium] `GetConsoleOutput` leaks the `GetPasswordData` ciphertext.** The agent writes the encrypted password to **console output**; `ec2:GetConsoleOutput` and `ec2:GetPasswordData` are separate actions with the same resource/condition surface and **no** coupling — a role `Deny`d `GetPasswordData` but `Allow`ed the commonly-broad `GetConsoleOutput` still gets the ciphertext (full takeover only with the launch-key private key). *Oracle:* `GetConsoleOutput` after a `Random`-mode launch; grep for the encrypted-password banner.
- **[L5 — Critical-if-sub-admin-writable] `unattend.xml` injection via `LocaleName`.** *Claim:* EC2Launch v2 writes the registry value `HKEY_USERS\.DEFAULT\Control Panel\International\LocaleName` into `unattend.xml` with no documented XML-escaping, *before* SYSTEM Sysprep parses it. A crafted `LocaleName` (`"><`…) could inject a `RunSynchronousCommand`/`AutoLogon` element executed as SYSTEM, baked into every future instance. *Load-bearing unknown:* who can write `HKU\.DEFAULT\…\LocaleName` — if admin/SYSTEM-only (likely default), this collapses to a same-privilege non-issue; if a sub-admin/build-pipeline path exists, Critical. *Oracle:* check the key's ACL; if sub-admin-writable, write a benign marker + metacharacters, run `ec2launch sysprep`, inspect generated `unattend.xml` for unescaped injection.
- **[L6 — Medium–High] EBS volume-swap password reset bypasses the login gate.** All three `ResettingAdminPassword*` flows reset the admin password via **disk manipulation only** (detach root → attach to temp instance → flip `Ec2SetPassword` state / delete `.run-once` / EC2Rescue offline reset → reattach) — no original password, launch key, or `GetPasswordData` needed. A same-account ops role with only `ec2:Stop/Start/Attach/Detach/RunInstances` can mint itself admin on a "no-login" instance. *Mitigating control to check:* a dedicated EBS CMK whose key policy denies the ops role `kms:Decrypt`.
- **[L7 — Informational] Self-signed RDP cert, manual-only thumbprint check.** `SetRDPCertificate`/`Ec2OutputRDPCert` provide no automated client-side pinning; MITM-in-path can substitute. Client-side UX issue, not an AWS account boundary — low priority.
- **[L8 — refutation note] `GetPasswordData` has no cross-account surface** (no resource-policy / cross-account condition key). One open sub-question: do RAM shared-subnet / Outposts / License-Manager host-sharing scenarios ever place the `instance` resource type itself under dual-account control? If not, cross-account `GetPasswordData` is fully refuted.

**Doc evidence:** `sysprep-using.md`, `sysprep-using-ec2launchv2.md`, `ec2config-service.md` (`RemoveCredentialsfromSyspreponStartup`, `Ec2OutputRDPCert`, `SetRDPCertificate`), `ec2launch-sysprep.md`, `ResettingAdminPassword{_EC2Config,_EC2Launch,_EC2Launchv2}.md`, `list_ec2.md` (`GetPasswordData`/`GetConsoleOutput`).
**Severity-if-true:** Critical (L1-shared, L2-shared, L3-shared, L5-if-writable), Medium–High (L6), Medium (L4), Informational (L7/L8).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Recover cleartext admin password from a shared AMI | Answer file / `LaunchConfig.json` / `agent-config.yml` | "deleted after Sysprep sets the password" / `RemoveCredentialsfromSyspreponStartup` |
| Inherit admin profile secrets as a different account | `CopyProfile=True` default | (none documented; opposite — it's the default) |
| Image an instance where Sysprep failed mid-Specialize | `CreateImage` + Specialize ordering | "safe to create an AMI" = `Stopped` (power-state only) |
| Credential-less RDP during first-boot window | `fDenyTSConnections` ordering vs `Ec2SetPassword` | `BeforeSysprep.cmd` sets `fDenyTSConnections=1` (source-instance only) |
| SYSTEM code-exec via writable hook script | `…\EC2Launch\sysprep`, v1 `Scripts`/`Sysprep`, EC2Config tree | v2 `config` folder "restricted to the administrator account" (sibling folders unstated) |
| SYSTEM code-exec via `unattend.xml` injection | v2 `LocaleName`→`unattend.xml` write | (none documented; escaping/ACL unknown) |
| Reset admin password with disk-only permissions | `ResettingAdminPassword*` volume-swap flow | (none in EC2 IAM; only an out-of-band EBS CMK key policy) |
| Read password ciphertext through unintended channel | `GetConsoleOutput` vs `GetPasswordData` | Separate IAM actions (no coupling) + launch-key private key for decrypt |
| Secret persists after share revoked | `launchPermission` / block-public-access | revoke prunes grant only; derivatives/launched instances unaffected |

---

## 7. Out-of-Scope Risk Categories

- A customer baking **their own** secret into **their own private** AMI, never shared (self-footgun / least-privilege the customer authored).
- Single-tenant self-DoS; a local admin "injecting" into their own build where no privilege boundary is crossed (e.g. §5.3-L5 if `LocaleName` is admin/SYSTEM-only writable).
- IMDS on these fully-managed Windows hosts; the Nitro hypervisor; the EC2 control-plane fleet — **any evidence reaching these is a HARD STOP, not a finding to pursue.**
- Generic Windows RDP client trust-dialog UX (§5.3-L7) is a Windows/client issue, not an AWS boundary — informational only.
- Third-party driver/software installers' own ACL-loosening behavior, except insofar as it is the documented precondition that activates an AWS-path lead.
- Standard EBS cross-account snapshot sharing mechanics (covered by their own docs), except where they propagate a Sysprep-baked secret.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens EE (predictable-name AMI land-grab):** N/A for this page set — checked `sharing-amis`, `sharingamis-intro/explicit`, `ami-create-win-sysprep`; no name/alias-based Windows-AMI resolution described (unlike `resolve:ssm`/`--owners`). May apply to a different AMI-discovery doc.
- **Lens W (attestation), Lens H (KMS enc-context confusion):** no attestation/encryption-context content in the Sysprep/sharing pages. KMS cross-account AMI-share key access *is* a documented, enforced control (cited as a contrast, not a lead).
- **Lens Y (transport/sig):** only the self-signed RDP cert (§5.3-L7, Informational); no TLS/SigV4 surface in this mechanism.
- **Lens FF/CC/BB/DD (JWT, upstream-context, canonicalization, cache):** do not fire — this is an OS/image mechanism, no multi-parser request path or token validation.
- **Doc gaps the hunter must resolve before claiming exploitation:**
  1. Actual NTFS ACLs on `…\EC2Launch\sysprep`, v1 `Config/Scripts/Sysprep`, EC2Config tree, `C:\Windows\Setup\Scripts` (§5.2 L1/L2/L4/L5).
  2. Writer ACL on `HKU\.DEFAULT\Control Panel\International\LocaleName` and whether EC2Launch v2 XML-escapes it (§5.3 L5) — the single gate that makes that lead Critical vs non-issue.
  3. Bodies of `InstallUpdates.ps1` and the shipped `*.cmd` hooks (§5.2 L7).
  4. Transactional/fail-closed semantics of the three Specialize synchronous commands (§5.1 L2, §5.3 L3).
  5. Whether AWS's shared-AMI auditing pipeline scans Windows AMIs for cleartext passwords / CopyProfile artifacts (§5.1 L7) — ask AWS-Security; not doc-observable.
  6. Whether any instance-resource-sharing primitive (RAM/Outposts/License Manager) ever enables cross-account `GetPasswordData` (§5.3 L8).

---

*Prepared with the `security-questionbuilder` skill from AWS documentation only. Hunters: start with §5.1-L5/L1, §5.3-L1, and §5.2-L1 (highest blast radius, cheapest oracles); confirm the §8 doc gaps first where a lead depends on them.*
