# Windows Launch Agents (configure-launch-agents) — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-launch-agents.html` (hub) and its six children —
`ec2launch-v2.html`, `ec2launch.html` (v1), `ec2config-service.html`, `launch-agents-set-dns.html`,
`launch-agents-subscribe-notifications.html`, `launch-agents-service-admin.html`. Offline mirror at
`/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

**Live-sync check (2026-09-12):** live `.md` for hub + `ec2launch-v2` + `launch-agents-service-admin` are byte-consistent with the offline mirror.
**No "See also"/agent-toolkit injection block** on any of these live UserGuide pages (the only "run the following command as an administrator" string is legitimate telemetry-disable prose, not an injected agent directive — cf. [[aws-docs-see-also-injection]]; watch for reappearance).

> **Relationship to existing plans — READ THIS FIRST so you don't start from zero or duplicate work.**
> This page is the **launch-agents-family hub**. The launch-agent SYSTEM-exec crown jewels were already reconstructed in
> `skill-agent_..._ec2-windows-instances.html.md` (memory: [[project_ec2-windows-instances-plan]]). **Do NOT re-derive them here.** Already-documented and still the highest-value work:
> - **Launch-agent user-data → SYSTEM execution** (EC2Launch v2 `executeScript`/UserData stage; v1 "Executes user data"; EC2Config `Ec2HandleUserData`) — all run in **LocalSystem/SYSTEM**.
> - **`ec2:ModifyInstanceAttribute(userData)` has NO `iam:PassRole` and NO fine-grained condition key** → a caller who can edit a stopped instance's user-data gets SYSTEM code-exec on next start. (Lens B/E variant.)
> - **Sysprep first-boot blank-Administrator-password RDP window** (crown jewel L1 in the existing plan) — unauthenticated, recurs every ASG boot.
> - **Cleartext Admin password remanence** in `agent-config.yml` / `Sysprep.xml` on the baked AMI/disk.
> - **Fast Launch SLR `EC2FastLaunchServiceRolePolicy` v7 `iam:PassRole Resource:"*"`** doc-vs-policy drift (crown jewel F1).
>
> **This plan's job is the DELTA** — surface that hub introduces or that the prior plan did not cover:
> 1. A **newly-documented config-directory ACL guarantee** (EC2Launch v2 only) that *closes* the doc-gap the prior plan flagged — now a testable Lens U guarantee-vs-enforcement lead, plus the divergence that the *other* agent dirs are NOT stated restricted.
> 2. **`launch-agents-set-dns`** — DNS suffix search-list / devolution override (never previously analyzed).
> 3. **`launch-agents-service-admin`** — in-guest service lifecycle (stop/delete/uninstall) → defense-evasion + Windows service-hijack.
> 4. **`launch-agents-subscribe-notifications`** — hardcoded AWS publisher account IDs + release-signal channel.
> 5. **EC2Config (legacy) LocalSystem specifics** — `Ec2HandleUserData`, XML `Settings`, SSM-on-legacy.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right.
- **Scope reality:** launch agents are an **in-guest, single-account, customer-owned** surface. There is **no shared multi-tenant service fleet** here. The only AWS-owned plane touched by this family is the **Fast Launch pre-provisioning fleet** (out of this page; see prior plan) and the **AWS-authored SNS publisher accounts** (§Area 4).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the Fast Launch t3 provisioning fleet's IMDS creds, or write access to the SNS publisher accounts `309726204594` / `801119661308`), stop, preserve evidence, flag for AWS-Security disclosure.
- Most leads here are **customer-configuration footguns / local-privilege-escalation** shapes. The one genuinely AWS-owned/reportable class is **Lens U doc-vs-enforcement** (does the documented ACL actually hold?) and **AWS-authored artifact defaults**.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. From a **non-administrator in-guest principal** (or a prior tenant of a reused/stopped instance), gain **SYSTEM/LocalSystem** code execution by writing an agent config file, script, or service definition that the launch agent (running as SYSTEM) later reads and executes.
2. Prove the **documented config-dir ACL guarantee** ("restricted to the administrator account to prevent privilege escalation", EC2Launch v2) is either **not enforced** on that dir or **does not extend** to the sibling dirs (`state`, `scripts`, `sysprep`, `wallpaper`) / v1 / EC2Config that carry the same executable content but carry **no such guarantee**.
3. Hijack **name resolution** for the instance by poisoning the DNS-suffix `SearchList` (via `setDnsSuffix` / devolution) → force unqualified lookups to an attacker-controlled domain (credential relay / NTLM capture) and leave **persistent stale suffixes** the docs say are "not automatically removed".
4. **Evade defenses / disable identity hygiene** through the in-guest service-admin surface (`sc delete ec2launch`, uninstall, stop) — e.g. suppress admin-password randomization or logging — and/or **hijack the SYSTEM service** via a weak service binary-path/registry-subkey ACL.
5. Confirm the launch-agent **release-notification channel** cannot be abused (spoofed subscription confirmations, or write to the AWS publisher topics).

---

## 2. Components, Assets, and Design

### Actors / identities
- **In-guest SYSTEM/LocalSystem** — the account all three agents run as (EC2Config: "runs in the LocalSystem account"; EC2Launch v2: Windows Service; EC2Launch v1: PowerShell scripts via a scheduled task, elevated).
- **In-guest local Administrator** — can edit agent config, stop/delete/uninstall the service.
- **In-guest non-administrator / low-priv user** — the privesc *source*.
- **AWS control-plane caller** — anyone with `ec2:ModifyInstanceAttribute` / `ec2:RunInstances` (sets user-data → SYSTEM exec). Cross-referenced from prior plan; not re-derived.
- **AWS-owned SNS publishers** — accounts `309726204594` (`amazon-ec2launch-v2`), `801119661308` (`ec2-windows-ec2config`) that publish agent-release notifications.

### The three agents (comparison from the hub page)
| | EC2Config (legacy) | EC2Launch v1 | EC2Launch v2 |
|---|---|---|---|
| Run as | Windows Service (LocalSystem) | PowerShell scripts (scheduled task) | Windows Service |
| Config format | XML | JSON | JSON/YAML (`agent-config.yml`) |
| Set Admin username | No | No | **Yes** (`setAdminAccount`) |
| Task config in user data | No | No | **Yes** |
| OS | pre-2016 (EOL) | 2016 / 2019 | 2016 / 2019 / 2022 / 2025 |

### On-disk layout (the privesc terrain)
- **EC2Launch v2:** binaries+UI in `%ProgramFiles%\Amazon\EC2Launch` (incl. `EC2LaunchSettingsUI.exe`); data in `%ProgramData%\Amazon\EC2Launch` with subdirs `config` (**`agent-config.yml`**), `state` (`state.json`, `previous-state.json`, `.run-once`), `sysprep`, `wallpaper`, `logs`.
  - **DOCUMENTED GUARANTEE (v2, verbatim):** *"Permission to create files in [the `config`] directory is restricted to the administrator account to prevent privilege escalation."* (ec2launch-v2.html, dir-structure section.) — **only the `config` dir is named.**
- **EC2Launch v1:** `C:\ProgramData\Amazon\EC2-Windows\Launch` with subdirs `Scripts` (PowerShell that *is* the agent), `Module`, `Config` (customizable), `Log`. **No ACL guarantee documented.**
- **EC2Config:** binaries+settings in `%ProgramFiles%\Amazon\EC2ConfigService`; XML settings in `...\Settings` (`Config.xml`, `BundleConfig.xml`, `ActivationSettings.xml`, `DriveLetterConfig.xml`, `EventLogConfig.xml`, `WallpaperSettings.xml`). **No ACL guarantee documented.**

### Untrusted-data entry points (transform seams)
- **User data** → agent parser → SYSTEM script exec (`executeScript` / `Ec2HandleUserData`; v2 supports base64+zip). *(Primary crown jewel — prior plan.)*
- **`agent-config.yml` / `Config.xml` / `Scripts\*.ps1`** on disk → agent reads → SYSTEM exec (local privesc — this plan's Area 1).
- **DNS-suffix task input / registry `SearchList`** → resolver behavior (this plan's Area 2).
- **Service registry subkey / `ImagePath`** → SCM launches as SYSTEM (this plan's Area 3).

### ASCII (privesc pipeline this plan targets)
```
low-priv user / prior tenant ─┐
                              ├─ write agent-config.yml / *.ps1 / Config.xml / service ImagePath
control-plane ModifyInstance ─┘         │
   Attribute(userData) ────────────────►│ (cross-ref: prior plan)
                                        ▼
                          Launch agent (SYSTEM/LocalSystem)  ── reads config/script/user-data
                                        │  executes
                                        ▼
                              SYSTEM code execution / admin-pw / DNS / RDP tampering
```

---

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| In-guest **non-admin** | Launch-agent **config/script dir** | writing a file the SYSTEM agent later reads/executes | A non-admin-authored `agent-config.yml`/`.ps1`/`Config.xml` runs as SYSTEM on next agent run = **privilege escalation** |
| In-guest non-admin | **v2 `config` dir specifically** | attempt file-create | Create **succeeds** despite the documented "restricted to administrator" guarantee = enforcement gap (Lens U) |
| In-guest non-admin | **v2 `state`/`sysprep`/`wallpaper` dirs, v1 `Config`/`Scripts`, EC2Config `Settings`** | writing executable/config content in an **un-guaranteed** dir | Agent consumes the file as SYSTEM = privesc via the dir the doc never promised to protect |
| In-guest low-priv | **SYSTEM Windows service** | writing service `ImagePath`/registry subkey or an unquoted-path/binary the SCM starts | Attacker binary runs as SYSTEM at agent start = service hijack |
| Instance (any user) | **network name resolution** | `setDnsSuffix`/devolution rewrite of `SearchList` | An unqualified hostname resolves to an attacker-chosen domain; stale suffix persists after "disable" = resolution hijack + persistence |
| In-guest admin (or malware) | **security posture** | `sc delete ec2launch` / uninstall / stop | Admin-pw randomization, RDP-cert, logging, or the setAdminAccount task no longer runs = defense evasion / blank-pw window persistence |
| Customer subscriber | **AWS SNS publisher accounts** `3097…`/`8011…` | SNS Subscribe | Any ability to **publish** to those topics, or forge a confirmation = supply-chain signal tamper (**expected: none → HARD STOP if reached**) |
| Any in-guest surface | **AWS service plane** (Fast Launch fleet IMDS, publisher accounts) | — | Any AWS-owned credential/account = **hard-stop breach** |

---

## 4. API / Interface Inventory

| Name | Type | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:ModifyInstanceAttribute` (userData) | AWS API | Yes | Yes (SigV4) | IAM-permitted | **No PassRole / no fine-grained condition key** → SYSTEM exec. Cross-ref prior plan. |
| `ec2:RunInstances` (user-data) | AWS API | Yes | Yes | IAM-permitted | Sets initial user-data. |
| `ec2:GetPasswordData` | AWS API | No | Yes | IAM-permitted | Retrieves encrypted admin pw the agent set; ownership scoping deferred to [[project_connect-windows-rdp-plan]]. |
| `agent-config.yml` / `Config.xml` / `Scripts\*.ps1` | On-disk config | (local) | No | in-guest ACL-gated | The local privesc surface — Areas 1. |
| `setDnsSuffix` task / `SearchList` registry | In-guest task+registry | (local) | No | in-guest | Area 2. |
| `EC2LaunchSettingsUI.exe` | In-guest GUI | (local) | No | in-guest | Edits `agent-config.yml`. |
| `sc delete ec2launch` / `sc delete ec2config` / Uninstall | In-guest SCM | (local) | No | in-guest admin | Area 3 — service lifecycle. |
| SNS `Subscribe` to `arn:aws:sns:us-east-1:309726204594:amazon-ec2launch-v2` / `:801119661308:ec2-windows-ec2config` | AWS SNS | Yes (own sub) | Yes | any AWS customer | Area 4 — publisher accounts are **AWS-owned**. |
| SSM (on pre-2016 EC2Config AMIs) | AWS API | Yes | Yes | IAM-permitted | Legacy: EC2Config processes SSM requests as LocalSystem. |

Undocumented/console-hidden knobs to enumerate on a live box: the *actual NTFS ACLs* on every agent dir (docs assert only the v2 `config` dir); EC2Config `Ec2SetPassword` re-enable semantics; `SetPasswordAfterSysprep` toggle in `BundleConfig.xml`.

---

## 5. Recommended Areas of Focus

### Area 1 — Config/script-directory ACL: documented guarantee vs. enforcement, and the un-guaranteed siblings  *(Lens U, E, S — highest priority NEW work)*
**Background.** EC2Launch v2 documents, verbatim, that its `config` directory is *"restricted to the administrator account to prevent privilege escalation."* This is a **newly-documented security guarantee** that *closes* the doc-gap the prior EC2-Windows plan explicitly flagged ("config-path ACLs not in docs"). It is now a first-class Lens U lead: a promise traced to a mechanism (an NTFS ACL) that a hunter can measure. Critically, **only the v2 `config` dir carries the promise** — the v2 `state`/`sysprep`/`wallpaper` dirs, **all** of EC2Launch v1's dirs (`Config`, `Scripts`, `Module`), and EC2Config's `Settings` dir carry **no** such statement, yet all contain content the SYSTEM agent reads and executes.

**Security Concern.** The launch agents run as SYSTEM/LocalSystem and blindly consume on-disk config + scripts. If any of these files is writable by a non-administrator, that non-admin escalates to SYSTEM at the next agent run/reboot — a classic writable-config → SYSTEM local privesc.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** A non-administrator can create/replace a file in the v2 `%ProgramData%\Amazon\EC2Launch\config` dir despite the "restricted to administrator" guarantee. → **Mechanism:** ec2launch-v2.html dir-structure guarantee. → **Oracle:** as a low-priv user, attempt `New-Item`/write in that path; success (or write to `agent-config.yml`) = **enforcement gap, Lens U, reportable if the ACL is agent-installed/AWS-owned**. → Sev: **High** (SYSTEM privesc) if it holds.
- **Claim:** The guarantee does **not** extend to the sibling dirs. Writing a task/script into v2 `state`/`sysprep`, or into v1 `Config`/`Scripts\*.ps1`, or into EC2Config `Settings\Config.xml`, is accepted and executed as SYSTEM. → **Oracle:** low-priv write to each un-guaranteed dir → observe SYSTEM exec on reboot. → Sev: **High**.
- **Claim (Lens U integrity):** the guarantee is prose-only — no equivalent hardening on v1/EC2Config even though they run the same SYSTEM scripts (v1 is literally its `Scripts\*.ps1`). → Sev: **Medium–High** (customer builds a false trust boundary on the v2 sentence).
- **Preconditions:** a low-priv shell on a running instance (or a reused/stopped instance from a prior tenant). **Cost:** low. **Stop condition:** SYSTEM shell obtained → PoC complete, do not persist.
- **Owner-to-fix note:** if the enforced ACL is set by the AWS-shipped installer, an enforcement gap is **AWS-owned (Tier-2 reportable)**; if the customer re-ACL'd the dir, it drops to a customer footgun.

### Area 2 — DNS-suffix `SearchList` poisoning & devolution  *(Lens F/name-resolution, O-persistence — NEW, never previously analyzed)*
**Background.** `launch-agents-set-dns.html`: all three agents **override** `System\CurrentControlSet\Services\Tcpip\Parameters\SearchList` with the instance domain, devolution results, NV domain, and per-NIC domains. Devolution walks a domain up to its parent (`locale.region.corp.example.com` → … → `example.com`). "When you disable devolution … the SearchList registry key **still contains the suffixes that were added previously. They are not automatically removed.**"

**Security Concern.** The DNS suffix search list decides how **unqualified** names resolve. An attacker who controls the `setDnsSuffix` task input (via `agent-config.yml`/user-data — Area 1 / prior-plan primitive) or the registry can insert an attacker-owned suffix so that `intranet` (unqualified) resolves to `intranet.attacker.com` → credential relay / NTLM capture / software-update hijack. Devolution to a parent domain can pull resolution into a broader, less-trusted zone. Stale-entry non-removal yields **persistence**: entries survive a "disable".

**High-level Test Scenarios.**
- **Claim:** A `setDnsSuffix` value / config edit lets an in-guest attacker add an arbitrary suffix to `SearchList`, and Windows will then resolve unqualified names against it. → **Oracle:** set a malicious suffix via the task; issue an unqualified lookup; observe egress to the attacker domain. → Sev: **Medium–High** (credential relay).
- **Claim:** Disabling devolution / lowering the level does **not** purge previously-injected suffixes → attacker persistence across reconfig. → **Oracle:** inject suffix, disable devolution, re-check `SearchList` still contains it. → Sev: **Medium** (persistence enabler).
- **Preconditions:** in-guest config write (chains from Area 1) or registry write. **Cost:** low. **Note:** this is largely a customer-config hardening/persistence finding, not an AWS service-plane bug — rate accordingly.

### Area 3 — In-guest service lifecycle: defense evasion & SYSTEM service hijack  *(Lens E, O — NEW)*
**Background.** `launch-agents-service-admin.html` documents stop/restart, and **`sc delete ec2launch` / `sc delete ec2config`**, and uninstall. "Deleting a service removes its registry subkey. Uninstalling … removes the files, the registry subkey, and any shortcuts." v1 is managed as a scheduled task.

**Security Concern (two shapes).**
1. **Defense evasion / identity-hygiene suppression.** An in-guest admin (or malware that gained admin) can stop/delete the agent so that admin-password randomization (`Ec2SetPassword`/`setAdminAccount`), RDP-cert setup, logging, and the post-Sysprep tasks no longer run. Combined with the prior plan's **blank-password first-boot window**, disabling `setAdminAccount` can *prolong* an unauthenticated-RDP window.
2. **SYSTEM service hijack (doc-gap).** The docs never state the ACLs on the service binary (`EC2Launch.exe`/`EC2Config.exe`), its `ImagePath` registry value, or the v1 scheduled task. A low-priv user who can rewrite `ImagePath`, replace the binary, or edit the scheduled-task action gets **SYSTEM at service start** — classic Windows weak-service-permissions / unquoted-service-path escalation.

**High-level Test Scenarios.**
- **Claim:** A non-admin can modify the launch-agent service's `ImagePath` / binary / scheduled-task action → SYSTEM exec. → **Oracle:** `Get-Acl` on the service key/binary + `AccessChk`; if writable by a non-admin group, replace and restart → SYSTEM. → Sev: **High**. → **Doc-gap:** binary/service ACLs not in docs; confirm on a live box.
- **Claim:** Deleting/stopping the agent removes SYSTEM-enforced identity hygiene without any control-plane signal (audit-evasion). → **Oracle:** `sc delete`, reboot, confirm admin pw not rotated / no CloudTrail-visible signal. → Sev: **Low–Medium** (evasion enabler; requires admin).
- **Preconditions:** shape 1 needs admin; shape 2 needs only a weak ACL. **Cost:** low.

### Area 4 — Launch-agent notification channel  *(Lens A/O — mostly NULL, documented for completeness)*
**Background.** `launch-agents-subscribe-notifications.html` gives **hardcoded AWS publisher account IDs**: `arn:aws:sns:us-east-1:309726204594:amazon-ec2launch-v2` and `arn:aws:sns:us-east-1:801119661308:ec2-windows-ec2config` (both in `us-east-1`, email protocol).

**Security Concern.** These accounts are **AWS-owned**. The channel is a release/patch **signal** customers may rely on to know when to update (relevant to the driver/agent TOFU supply chain in the prior plan). The lead is: can the channel be abused to *suppress* or *forge* a release signal?

**High-level Test Scenarios.**
- **Claim:** A non-AWS party can publish to, or alter subscriptions on, these topics. → **Oracle:** attempt `sns:Publish`/`sns:GetTopicAttributes` cross-account → expect `AuthorizationError`. **If publish succeeds → HARD STOP (AWS service-plane).** → Sev: Critical if true (do not expect it).
- **Claim:** Subscription confirmation is spoofable (attacker subscribes a victim, or forges the confirmation email). → **Oracle:** review confirm-URL entropy; expected out-of-scope (SNS-managed). → Sev: Informational.
- **Verdict:** likely **NULL** — publisher accounts are AWS-owned and not writable; keep only as a supply-chain-signal note that feeds the driver/agent TOFU concern.

### Area 5 — EC2Config legacy LocalSystem specifics  *(Lens E/K, cross-ref)*
**Background.** EC2Config "runs in the LocalSystem account"; `Ec2HandleUserData` "creates and runs scripts created by the user on the first launch … Commands wrapped in script tags are saved to a batch file, and commands wrapped in PowerShell tags are saved to a .ps1 file"; `Ec2SetPassword` generates a random encrypted admin pw (disabled after first launch); `BundleConfig.xml → SetPasswordAfterSysprep`; EC2Config also **processes SSM requests** on pre-2016 AMIs published after Nov 2016.
**Security Concern.** Legacy SYSTEM exec path identical in shape to the v2 crown jewel but on EOL OS with **no config-dir ACL guarantee** (Settings XML). SSM-on-legacy widens the remote-exec-as-SYSTEM surface. `ActivationSettings.xml` points activation at a KMS server (Windows KMS product activation) — a poisoned/redirected activation target is a minor lead.
**Test Scenarios.**
- **Claim:** low-priv write to `EC2ConfigService\Settings\Config.xml` (enable `Ec2HandleUserData` + supply script) → SYSTEM exec. → Oracle: write, reboot, observe SYSTEM. → Sev: High (on legacy OS only).
- **Claim:** `Ec2SetPassword` re-enable / `SetPasswordAfterSysprep=Yes` interacts with reboot to reset a user-chosen admin pw to a fresh random one the attacker can read via `GetPasswordData`. → Oracle: toggle, reboot, `GetPasswordData`. → Sev: Medium (cross-ref RDP plan).
- **Preconditions:** EOL Windows Server (<2016). **Cost:** low. Note EOL scope caveat.

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin → SYSTEM via writable config | v2 `config` dir | "restricted to the administrator account to prevent privilege escalation" (test the ACL holds) |
| Non-admin → SYSTEM via un-guaranteed dir | v2 `state`/`sysprep`/`wallpaper`, v1 `Config`/`Scripts`, EC2Config `Settings` | **none documented** (doc-gap → open lead) |
| SYSTEM service hijack | `EC2Launch.exe`/`EC2Config.exe` service `ImagePath`/binary/task | **none documented** (doc-gap → confirm ACLs live) |
| Name-resolution hijack + persistence | `SearchList` / `setDnsSuffix` / devolution | agent overrides SearchList; stale entries "not automatically removed" (persistence, not mitigated) |
| Defense evasion (disable hygiene) | service-admin `sc delete`/uninstall/stop | requires admin; no control-plane signal noted |
| Signal-channel tamper | SNS publisher accounts `3097…`/`8011…` | AWS-owned accounts (expected authz-denied → HARD STOP if not) |
| control-plane user-data → SYSTEM | `ec2:ModifyInstanceAttribute(userData)` | **no PassRole / no condition key** (cross-ref prior plan) |

---

## 7. Out-of-Scope Risk Categories
- The **SYSTEM-exec crown jewels** themselves (user-data-as-SYSTEM, `ModifyInstanceAttribute(userData)` no-condition-key, Sysprep blank-pw window, cleartext-pw remanence, Fast Launch SLR PassRole) — **already owned by [[project_ec2-windows-instances-plan]]**; execute there, don't duplicate.
- **A user steering their own instance** — an admin who edits their own agent config to run their own SYSTEM code is not a boundary crossing (customer owns the box). Only **non-admin → SYSTEM** or **prior-tenant → next-tenant** crosses a boundary.
- **IMDS on the customer's managed instance** (single-tenant); the Fast Launch provisioning-fleet IMDS is a **HARD STOP**, not in-scope testing.
- **Shared AWS infra / service plane** — SNS publisher accounts, Fast Launch fleet.
- **DNS rebinding against private-only endpoints**; product/feature-parity gaps; EOL-OS bugs beyond documented behavior (EC2Config runs on unsupported Windows — note but don't over-invest).
- **`GetPasswordData` ownership scoping** — deferred to [[project_connect-windows-rdp-plan]].
- Customer-authored config/policy weaknesses = least-privilege footguns (out of scope) **unless the weak default ships in an AWS-authored/enforced artifact** (the Area 1 ACL, if agent-installed, is the in-scope exception).

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR):** N/A — no multi-tenant resource-by-ID surface on this family (checked all six child pages). The only cross-account objects are the AWS-owned SNS topics (Area 4, expected authz-denied).
- **Lens B/C/H/W (PassRole/creds/KMS/attestation):** N/A on these pages — no role-ARN input, no KMS key input, no attestation. (Fast Launch KMS/PassRole lives in the prior plan.) `ActivationSettings.xml` "AWS KMS" is Windows KMS product-activation, not AWS KMS — minor doc-confusion, not a key-policy surface.
- **Lens G (SSRF):** N/A — no field on these six pages that the *service* dereferences server-side (checked hub + all children). DNS-suffix is in-guest resolver behavior, not a server-side fetch. `setDnsSuffix`/devolution routed to Area 2 as a resolution-hijack, not SSRF.
- **Lens Q (upload):** N/A — user-data script ingest is the SYSTEM-exec primitive (prior plan), not a parsed-blob/render surface.
- **Lens J/P/M/N/Y (OAuth/proofing/session/namespace/TLS):** N/A — none of these mechanisms appear on the launch-agents pages.
- **DOC-GAPS to close on a live box (do these first when you get an instance):**
  1. Actual NTFS ACL on the v2 `config` dir (verify the guarantee) **and** on the un-guaranteed siblings, v1 dirs, EC2Config `Settings` (Area 1/5).
  2. Service binary / `ImagePath` registry / v1 scheduled-task ACLs (Area 3 shape 2).
  3. Whether the config-dir ACL is set by the AWS-shipped installer (→ Tier-2 reportable) or left to the customer (→ footgun).
