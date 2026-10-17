# EC2 Serial Console — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.html
**Source of leads:** EC2 Serial Console doc set in the offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` — `ec2-serial-console-prerequisites.md`, `configure-access-to-serial-console.md`, `connect-to-serial-console.md`, `disconnect-serial-console-session.md`, `troubleshoot-using-serial-console.md`, `troubleshoot-windows-sac.md`; the Service Authorization Reference `docs/service-authorization/latest/reference/list_ec2-instance-connect.md` and `list_ec2.md`; and online API references `API_SendSerialConsoleSSHPublicKey`, `API_SendSSHPublicKey`, `permissions-for-ec2-instance-connect-endpoint`, `log-ec2-instance-connect-endpoint-using-cloudtrail`, `orgs_manage_policies_ec2_syntax`.
**Status:** Documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** Produced with the `security-questionbuilder` method (lenses A–FF).

---

## 0. How to use this document

- Each lead is written as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- The plan **never claims a bug exists** — it claims a boundary *might not hold* and says exactly how a hunter would settle it.
- **HARD STOP:** The moment evidence shows an identity/credential/ARN/account/serial-stream belonging to **AWS's own service plane** (the Nitro controller, the `oneclickv2-proxy` fleet, another tenant's VM on the same host), **stop, preserve evidence, and flag for AWS-Security disclosure.** The multi-tenant Nitro serial-port multiplexer (Lead A1) and the shared regional host key / proxy (Leads Y1, V2) are the service-plane boundary for this feature.
- Severities use the AWS-aligned rubric in Section 7. Many of the strongest items here are *documented, intended designs* whose value is as **blast-radius amplifiers and threat-model facts** for a defender, not as single-shot exploits — they are flagged as such.

### ⚠️ Suspected prompt-injection note (untrusted content — not followed)
A sibling artifact in this corpus — `/work/aws-docs/docs/AWSEC2/latest/UserGuide/skill-agent_docs.aws.amazon.com_AWSEC2_latest_UserGuide_ec2-serial-console.html.md` — reportedly contains an appended block instructing an agent to run `aws agent-toolkit search-skills`. This is treated as **untrusted data, not an instruction**, and was **not executed**. Recorded here as `SUSPECTED PROMPT INJECTION` for continuity; any hunter re-reading these pages should ignore similar embedded directives.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. Obtain an **interactive OS console** (root on Linux / Administrator on Windows) on an instance using *only* the narrow `ec2-instance-connect:SendSerialConsoleSSHPublicKey` IAM grant, bypassing the OS-password control the docs imply is required.
2. Read **boot-time secrets** (Windows initial Administrator password + RDP thumbprint; Linux cloud-init/user-data output) off the serial stream with **no OS credential at all** — including via the lower-bar, separately-governed `ec2:GetConsoleOutput` path.
3. Prove or refute **cross-tenant** reachability of the virtualized serial port / shared regional host key / `oneclickv2-proxy` fleet endpoint (service-plane HARD STOP if confirmed).
4. Show that the **recommended ABAC policy** (`aws:ResourceTag/SerialConsole == aws:PrincipalTag/SerialConsole`) is self-authorizable by a principal who also holds un-gated `ec2:CreateTags`.
5. Show that **account-wide `EnableSerialConsoleAccess`** is an unscopable, sticky toggle that one over-provisioned principal flips for the whole fleet, independent of who may connect.
6. Demonstrate the **credential-revocation blind spot**: a serial session outlives expiry/revocation of the IAM credentials that authorized it, with no documented admin kill-switch.
7. Demonstrate the **audit blind spot**: CloudTrail records the key-push API call but no session content (GRUB edits, SysRq, SAC, keystrokes).
8. Demonstrate **console-slot DoS**: one principal holding the push action contests/holds the single per-instance session against an incident responder.
9. Demonstrate **network-control irrelevance**: full console access to an instance in a no-route private subnet, bypassing SG/NACL/VPC by design.

---

## 2. Components, Assets, and Design

**What the feature is.** EC2 Serial Console gives interactive access to an instance's **virtual serial port** (`ttyS0` on Linux, `COM1` on Windows). It is deliberately **out-of-band**: the connection is "independent of the instance VPC … does not use the instance security group or the subnet network ACL to authorize traffic" (`configure-access-to-serial-console.md`). It works with no instance networking at all and survives reboot/stop, showing all boot messages from the start.

**Customer-facing interfaces (two):**
- **Browser-based client** — EC2 console → WebSocket over **port 443** to the regional **service-owned proxy** `prod.{region}.oneclickv2-proxy.ec2.aws.dev` (commercial/GovCloud) / `…ec2.a2z.org.cn` (China). "The browser-based client handles the permissions."
- **SSH client + API** — `aws ec2-instance-connect send-serial-console-ssh-public-key` pushes a one-time public key (valid **60 seconds**), then `ssh {instance-id}.port0@serial-console.ec2-instance-connect.{region}.aws` (newer regions `ec2-serial-console.{region}.api.aws`; China/GovCloud variants). After the key is pushed, **"the SSH connection is not subject to the IAM policies."**

**Processes / fleets behind it (AWS-owned, multi-tenant service plane):**
- The **Nitro System controller/hypervisor** that virtualizes the serial port. Supported only on Nitro-based virtualized instances + most bare metal; **excluded**: all `mac*.metal`, `a1.metal`, `g5g.metal`, high-memory `u-*.metal` — the exact set lacking the full Nitro Card chain (Lead OS2).
- The regional **`oneclickv2-proxy`** fleet (browser path) and the **`serial-console.ec2-instance-connect`** SSH endpoint fleet — each presents a **single shared host-key fingerprint per region** for all tenants.

**Identity & session:**
- Key-push authorized by **SigV4 IAM** (`ec2-instance-connect:SendSerialConsoleSSHPublicKey`). Session **persists ~1 hour regardless of IAM credential expiry**; only client-side disconnect (`~.` / close tab) is documented. **One active session per instance**; 30 s teardown; named API exception `SerialConsoleSessionLimitExceededException`.
- OS-level auth: **Linux** needs a password-based OS user to get a *shell* (any user incl. root), but **not** to monitor logs / send SysRq; **Windows** — "granting serial console permissions is equivalent to granting admin-level privileges on the instance."

**Resource & identifier shape:** the only resource is the EC2 `instance` ARN `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`. Instance IDs are enumerable account-wide via the *mandatory* `ec2:DescribeInstances` (Resource:* forced). SSH username is the fixed-shape `{instance-id}.port0`.

**Account/org controls:** off by default; enabled per-account-per-region via `ec2:EnableSerialConsoleAccess` **or** an Organizations **declarative policy** (`ManagedBy` = `account` | `declarative-policy`; declarative locks out in-account change). SCP can gate the API; declarative policy sets the attribute directly.

### ASCII pipeline

```
                         IAM (SigV4) gate: SendSerialConsoleSSHPublicKey  (60s key TTL)
                                      │  account toggle: EnableSerialConsoleAccess (all-or-nothing / region)
  ┌─────────────┐  443/WSS   ┌────────┴─────────────┐    ┌──────────────────────────┐   virtual UART
  │  Browser    │──────────► │ oneclickv2-proxy     │    │  serial-console.ec2-     │   (ttyS0 / COM1)
  │  client     │            │ (AWS-owned, regional,│    │  instance-connect.{rgn}  │        │
  └─────────────┘            │  MULTI-TENANT)       │    │  SSH endpoint (shared    │        ▼
  ┌─────────────┐  SSH       └──────────────────────┘    │  regional host key)      │  ┌──────────────┐
  │  ssh + key  │─────────────────────────────────────► └───────────┬──────────────┘  │ Nitro serial │
  │  {id}.port0 │                                                    │                 │ multiplexer  │
  └─────────────┘                                                    └────────────────►│ (AWS plane,  │
        ▲  after push, session NOT subject to IAM; outlives cred expiry; no SG/NACL     │ shared host) │
        │                                                                               └──────┬───────┘
   out-of-VPC — SG / NACL / route table do NOT apply                                           ▼
                                                                                   Guest OS: GRUB / SysRq /
                                                                                   SAC / login:  (boot secrets)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM principal | Target instance's serial port | `SendSerialConsoleSSHPublicKey` (SigV4) | A principal reaches a serial port of an instance it is **not** authorized for (ARN/tag scope broken), or reaches a **specific OS user/port** no IAM key could restrict. |
| Caller (push rights only) | Guest OS root/admin | GRUB single-user / SAC / boot-secret read | A root/admin shell or a cleartext credential obtained **without** the OS password the docs frame as required. |
| Any serial-authorized tenant | Another tenant's VM on the same Nitro host | Virtual UART multiplexer (AWS plane) | Any byte of another tenant's serial stream, or a SysRq/console command landing on the wrong VM = **HARD-STOP service-plane breach.** |
| Browser client | `oneclickv2-proxy` fleet (shared) | WSS/443 session establishment | A session bound/routed to an instance the browser session was not authorized for; proxy-level session mix-up = **HARD-STOP.** |
| SSH client | Regional serial-console endpoint | SSH host-key TOFU (one shared key/region) | A MITM accepted because verification is optional/shared-key TOFU → session hijack. |
| Account admin / org | Account serial-console setting | `EnableSerialConsoleAccess` / declarative policy | A low-priv principal flips account-wide access, or learns org governance posture, beyond intended scope. |
| Revoked/expired principal | Live serial session | Session persistence past cred expiry | An interactive session usable after its authorizing credentials are revoked. |
| **Any customer surface** | **AWS service plane** (Nitro / proxy / shared key) | — | **Hard stop: preserve evidence, flag for disclosure.** |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | API/CLI | Yes | External | Push 60 s one-time pubkey → start serial session | Yes (SigV4) | IAM on `instance` ARN; cond keys **only** `aws:ResourceTag`,`ec2:ResourceTag` | **No `ec2:osuser`** (sibling SSH has it). Params: `InstanceId`, `SerialPort` (**fixed 0**), `SSHPublicKey`. Exception `SerialConsoleSessionLimitExceededException`. **This is the only correctly instance-scopable control in the surface.** |
| `ec2-instance-connect:SendSSHPublicKey` | API/CLI | Yes | External | Standard (in-VPC) SSH key push | Yes | IAM on `instance`; **+ `ec2:osuser`** | Sibling with a *stronger* condition surface — parity gap (Lens X). |
| `ec2-instance-connect:OpenTunnel` (EIC Endpoint) | API | Yes | External | SSH tunnel via EIC Endpoint | Yes | IAM on `instance-connect-endpoint`; `+remotePort`,`privateIpAddress`,`maxTunnelDuration` | Even stronger condition surface; needs an SLR to create the endpoint. |
| `ec2:EnableSerialConsoleAccess` | API/CLI | Yes | External | Enable serial console **account-wide/region** | Yes | IAM; **no resource type** (Resource:*), only `ec2:Region` | Unscopable, sticky toggle. Access-level "Write" **understates** its sensitivity. |
| `ec2:DisableSerialConsoleAccess` | API/CLI | Yes | External | Disable account-wide | Yes | same | Only off-switch; no auto-expiry. |
| `ec2:GetSerialConsoleAccessStatus` | API/CLI | No | External | Read status + `ManagedBy` | Yes | IAM; Resource:* forced | Leaks org governance posture (`ManagedBy=declarative-policy`) to any read-only principal. |
| `ec2:DescribeInstances` / `DescribeInstanceTypes` | API/CLI | No | External | Enumerate instances/types | Yes | IAM; **Resource:* forced** by docs | Mandatory in the recommended policy → account-wide instance enumeration regardless of push scope. |
| `ec2:GetConsoleOutput` | API/CLI | No | External | Read persisted system log / console output | Yes | IAM (separate, older action) | **Lower-bar, separately-governed** read path to the same Windows boot password/thumbprint — not covered by serial-console IAM/SCP/declarative controls. |
| Browser proxy `prod.{region}.oneclickv2-proxy.ec2.aws.dev` | WSS/443 | — | **Internal/service** | Terminates browser serial sessions | Yes (443) | "client handles permissions" | Multi-tenant AWS fleet; **no documented tenant-isolation/session-binding model** (doc-gap). |
| SSH endpoint `serial-console.ec2-instance-connect.{region}.aws` | SSH | — | **Internal/service** | Serial SSH relay | Yes | key pushed within 60 s | **One shared host-key fingerprint per region.** |

No `[NEW]` markers on these pages; the feature is GA across all Regions except AWS European Sovereign Cloud (Germany), all Outposts, all Local Zones (Wavelength not supported).

---

## 5. Recommended Areas of Focus (ordered by priority)

Priority order follows: (1) confirmed-by-docs credential/root reach with the lowest IAM bar, (2) service-plane cross-tenant hard-stops, (3) IAM/ABAC scoping gaps, (4) session/transport/audit amplifiers.

### Area 1 — Boot-time credential disclosure over serial (Windows admin password; Linux cloud-init) — **highest-confidence**
**Background.** The serial stream carries all boot output. EC2Launch v2 "relies on the serial port to perform several initialization tasks during boot, such as **emitting the instance password and RDP thumbprint**" (`troubleshoot-windows-sac.md`). Reaching the serial TTY needs **no OS credential** ("You can connect to the serial console without a password"). This output is **also persisted** and readable via the separate, lower-privilege `ec2:GetConsoleOutput` API.
**Security Concern.** A principal with only `SendSerialConsoleSSHPublicKey` (or merely `ec2:GetConsoleOutput`) can read a freshly-launched Windows instance's **cleartext initial Administrator password** and RDP thumbprint; Linux user-data/cloud-init frequently echoes tokens/passwords to `ttyS0`.
**High-level Test Scenarios.**
- Launch a Windows instance; with push-only serial rights, read the serial stream during init → observe the admin password/thumbprint. Then confirm the same value via `ec2:GetConsoleOutput` with a principal that lacks serial rights entirely.
- Launch a Linux instance with a user-data script that echoes a canary secret; read it off the serial console with no OS login.
**Doc evidence.** `troubleshoot-windows-sac.md` ("emitting the instance password and RDP thumbprint"; "available from … get-console-output"); `configure-access-to-serial-console.md` ("connect … without a password"). **Severity-if-true:** High (credential disclosure; `GetConsoleOutput` path broadens the exposed principal set and sidesteps every serial-console control). **Stop:** once a canary credential is read, that is the PoC — do not reuse it.

### Area 2 — Privilege escalation to root via GRUB single-user / emergency boot (OS-password bypass)
**Background.** `troubleshoot-using-serial-console.md` documents interrupting GRUB and appending `single`/`emergency` to the kernel line to boot a lower runlevel. Whether a password is then demanded depends on the AMI/distro `sulogin`/`rd.shell` config — **not** on the serial-console feature.
**Security Concern.** A principal with push rights + any reboot capability (own `ec2:RebootInstances`, an in-guest low-priv shell, or **SysRq `b` sent over the same serial session** — no extra IAM) reaches a **root shell without the OS password** the docs frame as required ("to *use* the serial console … the instance must have a password-based OS user").
**High-level Test Scenarios.**
- For each major AMI family (AL2, AL2023, Ubuntu, RHEL, CentOS), reboot into `single`/`emergency` via serial and observe whether `sulogin` actually prompts for a password before granting shell. Any family that drops straight to shell confirms the escalation.
- Confirm the instance-state gate (must be `running`) is checked only at *connect* time, not continuously, so a mid-session `sudo reboot`/SysRq-`b` keeps the session alive through the GRUB window (Lead OS3b).
**Doc evidence.** `troubleshoot-using-serial-console.md` (GRUB single-user steps; example kernel line contains `rd.shell=0`, config-dependent); `ec2-serial-console-prerequisites.md` ("Instance state … must be `running`"). **Severity-if-true:** High (push-only → root, bypassing the documented password control on any AMI without enforced `sulogin`). **Stop:** a single root prompt on one test AMI is the PoC.

### Area 3 — Cross-tenant isolation of the virtual serial port / shared host-key / proxy (SERVICE-PLANE HARD STOP)
**Background.** The serial port is multiplexed by the **Nitro controller** on a physically shared host; the SSH endpoint presents **one host-key fingerprint per region** for all tenants; the browser `oneclickv2-proxy` is a shared AWS fleet. The docs describe **none** of the per-instance isolation, session-to-instance binding, or proxy tenant-segregation mechanisms (doc-gaps).
**Security Concern.** If any layer binds a session to an instance by a guessable/forgeable identifier rather than cryptographic ownership, one tenant could read or command another tenant's serial port — a service-plane breach.
**High-level Test Scenarios.** *(authorized live test only; the moment any evidence points at another tenant or the AWS fleet identity — STOP and flag for disclosure)*
- Probe whether the SSH username `{instance-id}.port0` is the sole session selector and whether the pushed key is validated against instance *ownership* or merely instance *existence*.
- Examine the browser session-establishment handshake: is it an instance-scoped, short-lived, signed token (like EIC-Endpoint `OpenTunnel`), or a bearer value reusable across instances/tenants?
- The excluded instance types (`mac*/a1/g5g/u-*.metal`) corroborate a hard Nitro-Card dependency — map which component enforces the per-instance boundary.
**Doc evidence.** `ec2-serial-console-prerequisites.md` (proxy endpoint; Nitro-only instance list); `connect-to-serial-console.md` (single fingerprint per region; MITM warning). **Severity-if-true:** Critical (cross-tenant console/credential/DoS). **Stop / HARD STOP:** any cross-tenant byte or AWS-fleet identity → preserve evidence, cease, disclose.

### Area 4 — ABAC self-authorization via un-gated `CreateTags` (Lens S)
**Background.** AWS's recommended tag policy allows the push "only if that instance's resource tag and the principal's tag have the same `SerialConsole` value" (`configure-access-to-serial-console.md`). `ec2:CreateTags` carries **no condition key / no resource constraint** in `list_ec2.md`.
**Security Concern.** A principal holding the ABAC-scoped push action **plus** un-gated `CreateTags` can set the target instance's `SerialConsole` tag to match their own `PrincipalTag` and **self-authorize** — the recommended pattern is incomplete without a companion Deny on mutating the scoping tag key (a warning AWS gives for the analogous instance-profile ABAC but **omits here**).
**High-level Test Scenarios.** With `PrincipalTag/SerialConsole=red` and un-gated `CreateTags`: retag an instance from `SerialConsole=blue` to `red`, then push the serial key → session succeeds. Also test `StringEquals` case-sensitivity and absent-key-on-both-sides resolution (doc-gap).
**Doc evidence.** `configure-access-to-serial-console.md` ABAC JSON; `list_ec2.md` `CreateTags` row (no condition/resource). **Severity-if-true:** High (defeats the documented access-control mechanism). **Stop:** one successful self-authorized push.

### Area 5 — No `ec2:osuser` on serial push → OS-user least-privilege is unexpressible; sibling-parity gap (Lens U / X)
**Background.** `SendSerialConsoleSSHPublicKey` supports only `aws:ResourceTag`/`ec2:ResourceTag`; the sibling `SendSSHPublicKey` additionally supports `ec2:osuser`, and `OpenTunnel` supports port/IP/duration keys. The serial push also has no username field in its request schema.
**Security Concern.** A security team that pins standard SSH to `osuser=appuser` has **no equivalent statement** for serial console: whoever types the pushed key at the `login:` prompt authenticates as **any** password-enabled user, including root (Windows = always admin). Serial is strictly the weakest-controlled of the three EC2 Instance Connect paths and additionally bypasses all network compensating controls.
**High-level Test Scenarios.** Attempt to author an IAM policy restricting serial access to one OS user → demonstrate it is inexpressible. Confirm a tag/instance-scoped grantee can log in as root.
**Doc evidence.** `list_ec2-instance-connect.md` (condition-key tables for the three actions); `API_SendSerialConsoleSSHPublicKey` (schema). **Severity-if-true:** Medium–High. **Stop:** documented asymmetry confirmed.

### Area 6 — Account-wide `EnableSerialConsoleAccess`: unscopable, sticky blast-radius toggle (Lens E / U)
**Background.** `Enable/Disable/GetSerialConsoleAccessStatus` have **no resource type** (Resource:* only, `ec2:Region`). Off by default; sticky until explicitly disabled; no auto-expiry.
**Security Concern.** A principal holding only `ec2:EnableSerialConsoleAccess` (easily bundled into broad EC2-admin policies) can flip serial access on for **every** instance in the account/region — the precondition that turns every narrow push grant live. Access-level "Write" understates this; treat it like a privilege-escalation enabler.
**High-level Test Scenarios.** Grant only `ec2:EnableSerialConsoleAccess`; confirm the call succeeds account-wide with no instance/tag filter and flips `GetSerialConsoleAccessStatus`. Check for config-drift (left enabled after a one-time task).
**Doc evidence.** `list_ec2.md` (Enable/Disable/Get rows); `configure-access-to-serial-console.md` (Resource:* example; "all instances in the account"). **Severity-if-true:** Medium standalone / amplifier for all other leads. **Stop:** toggle flipped once.

### Area 7 — Session persistence past credential revocation; no admin kill-switch (Lens C / O)
**Background.** "The duration of the connection is not determined by the duration of your IAM credentials … the connection continues to persist until the maximum duration … is reached" (`connect-to-serial-console.md`). Only client-side disconnect is documented (`~.`, close tab); no `TerminateSerialConsoleSession`-shaped admin API found.
**Security Concern.** Revoking/expiring a compromised or offboarded principal's credentials does **not** end an in-progress serial session (~1 hour) — a credential-revocation blind spot during incident response.
**High-level Test Scenarios.** Open a session with STS temporary creds; revoke the policy / invalidate the STS session; confirm the SSH/WSS session remains interactive. Search `AWSEC2/latest/APIReference` for any admin session-termination action (expected null).
**Doc evidence.** `connect-to-serial-console.md`; `disconnect-serial-console-session.md`. **Severity-if-true:** Medium–High (operational/IR gap). **Stop:** persistence after revocation observed once.

### Area 8 — Audit blind spot: CloudTrail logs the key-push, not session content (Lens O)
**Background.** CloudTrail records the `SendSerialConsoleSSHPublicKey` call (who/when/source IP) but no session transcript; no data-event/session-recording mechanism is documented.
**Security Concern.** An attacker with a push-capable credential leaves a forensic trail of "a key was pushed at time T" only — GRUB edits, SysRq, SAC, login attempts, and data read off the TTY are **invisible**. Amplifies Areas 1, 2, 7.
**High-level Test Scenarios.** Perform GRUB/SysRq/SAC actions in a session; confirm CloudTrail/Config/flow-logs contain no record of the in-session activity.
**Doc evidence.** `log-ec2-instance-connect-endpoint-using-cloudtrail.md` (event schema is management-event envelope, no `responseElements`/transcript). **Severity-if-true:** Medium (detection/forensics enabler). **Stop:** absence of session-content logging confirmed.

### Area 9 — Single-session-per-instance / 60 s window race → console-slot DoS (Lens M / L)
**Background.** One active session per instance; 60 s key TTL; 30 s teardown; `SerialConsoleSessionLimitExceededException`.
**Security Concern.** A principal holding the push action (e.g., via the over-broad grant AWS warns against) can repeatedly win/hold the single slot to **deny an incident responder** console access during an emergency, or race the 30 s teardown on reconnect.
**High-level Test Scenarios.** Two principals contend for the slot; measure whether the attacker reliably pre-empts the victim (first-come vs. fair queueing). Hold the slot and measure lock-out duration.
**Doc evidence.** `connect-to-serial-console.md` (1 session; 30 s teardown; 60 s key); `API_SendSerialConsoleSSHPublicKey` (exception). **Severity-if-true:** Medium (insider/self DoS; **Critical only if chained to a confirmed cross-tenant Area 3 breach**). **Stop:** reliable lock-out demonstrated once.

### Area 10 — SysRq as an OS-auth-bypassing DoS/integrity primitive (Lens L)
**Background.** SysRq "send[s] the kernel a command, outside of a shell … regardless of what the kernel is doing" — `c` crash, `o` poweroff, `b` reboot, `e`/`i` kill-all. Needs **no OS password** (carved out explicitly). Distro default `kernel.sysrq` is often non-zero (e.g., Ubuntu 176).
**Security Concern.** A push-only principal can crash/reboot/poweroff an instance with no OS credential, depending on the (often non-zero) default `kernel.sysrq`.
**High-level Test Scenarios.** On stock AMIs, read `/proc/sys/kernel/sysrq` default, then send `~B` + `c`/`o`/`b` over serial and observe the DoS. Map which ops the default mask permits.
**Doc evidence.** `troubleshoot-using-serial-console.md` (SysRq table); `ec2-serial-console-prerequisites.md` ("Configure SysRq" — framed as opt-in, baseline default unstated → doc-gap). **Severity-if-true:** Medium (single-tenant self-DoS); Critical if chained to Area 3. **Stop:** one DoS on an owned test instance.

### Area 11 — SSH host-key MITM: shared regional key, optional TOFU-only verification (Lens Y / M)
**Background.** One fingerprint per region for all tenants; verification is an "(Optional)" manual step shown only on first connect; comparison is against text in the same doc, no signed/out-of-band channel. The 60 s window pressures automation toward `StrictHostKeyChecking=no`.
**Security Concern.** A user in a DNS/routing/MITM position (or compromised proxy/VPN) who is accepted via TOFU — or whose automation disables host-key checking — can hijack a session that yields root-/admin-equivalent OS access.
**High-level Test Scenarios.** Assess real-world tooling for `StrictHostKeyChecking=no`; evaluate whether AWS offers a programmatic signed fingerprint source (expected null). *(No live interception against AWS endpoints — reason from docs + published fingerprints only.)*
**Doc evidence.** `connect-to-serial-console.md` (MITM warning; optional verify; per-region fingerprint table). **Severity-if-true:** High if exploitable (session hijack). **Stop:** documentation assessment only; do not MITM AWS infra.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Push-only → root without OS password | GRUB single-user over serial | "must have a password-based OS user" (assumed, config-dependent `sulogin`) |
| Read Windows admin password / Linux secrets off serial | Boot output / `GetConsoleOutput` | None stated; "connect without a password" is explicit |
| Cross-tenant serial-port / proxy / host-key reach | Nitro multiplexer, `oneclickv2-proxy`, shared SSH key | Undocumented (doc-gap) — generic Nitro isolation only |
| ABAC self-authorize via tag mutation | `CreateTags` + ABAC policy | Tag-match ABAC (no companion CreateTags Deny recommended) |
| OS-user restriction on serial | IAM condition keys | None — `ec2:osuser` not supported for serial |
| Account-wide enable by low-priv principal | `EnableSerialConsoleAccess` | SCP / declarative policy (if configured); none by default |
| Session after credential revocation | Session lifetime | "connection continues to persist"; client-side disconnect only |
| In-session activity forensics | CloudTrail | Key-push event only; no session recording |
| Console-slot DoS vs. responder | 1-session limit / 60 s window | "restrict access to specific instances" (IAM) |
| SysRq crash/reboot without OS auth | Kernel SysRq over serial | Admin opt-in `kernel.sysrq`; default unstated |
| MITM via shared TOFU host key | SSH endpoint | Optional manual fingerprint verification |
| Network isolation of a private instance | Out-of-VPC transport | None — SG/NACL/VPC bypassed by design |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)

- **AWS-owned shared infrastructure internals** — Nitro controller, `oneclickv2-proxy` fleet, shared regional SSH host key: **do not probe beyond existence**; any cross-tenant/service-plane evidence is a **HARD STOP + disclosure**, not a continued exploit.
- **Single-tenant self-DoS / self-destruction** on your own instance (SysRq crash of your own VM, holding your own session) — low/out-of-scope unless it crosses tenants.
- **User steering their own OS session** — using the console as root on your own instance is the intended feature, not a finding.
- **Customer-authored IAM footguns** — an over-broad `SendSerialConsoleSSHPublicKey` or un-gated `CreateTags` the *customer* wrote is a least-privilege footgun; **but** AWS's *recommended* ABAC pattern omitting the CreateTags Deny (Area 4) is an AWS-authored-doc defect worth filing.
- **MITM against AWS endpoints** — do not perform live interception; reason from docs/published fingerprints only.
- **Third-party/Marketplace AMIs shipping preset root passwords** (Lead OS7) — needs AMI-catalog research, not serial-console docs; AWS-published AMIs explicitly have no password-based user by default.
- **Wavelength Zones** — serial console not supported there at all.
- **DNS rebinding / generic cloud-init secret-echo risk** — the serial console is the *delivery* path (in scope as such), but the "secrets in boot logs" root cause is a workload practice, not a serial-console bug.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did not fire, with pages read)

- **Lens B (confused deputy / PassRole):** NULL. `API_SendSerialConsoleSSHPublicKey` has no `RoleArn`/credential-forwarding field; no SLR for the push/connect path (SLR appears only for EIC *Endpoint* creation). Pages: API ref, `configure-access-to-serial-console.md`, `ec2-serial-console-prerequisites.md`.
- **Lens G (SSRF) / Lens Q (upload):** NULL — no URL/URI/location field and no file/blob upload anywhere in the surface; it is a bidirectional character stream, not an HTTP API with dereferenced inputs. Pages: all four core UserGuide pages + Windows SAC.
- **Lens A cross-account sharing / Lens AA share-revoke:** NULL — no RAM share, no resource-based policy, no launchPermission-style grant; access is strictly IAM-principal + instance-ARN within the owning account. Page: `configure-access-to-serial-console.md`.
- **Lens H / W (KMS / attestation):** NULL — no customer KMS key, encryption context, or attestation condition in the serial-console flow. Pages: all core pages.
- **Lens Y transport floor:** NULL/clean per docs — port 443 + WebSocket (TLS implied) and SSH only; SigV4 on the API; no cleartext fallback documented. TLS version/cipher is a live-probe question, out of scope here.
- **Lens FF (JWT/OIDC) / DD (cache) / BB (parser differential) / CC (upstream-context):** NULL on the documented surface — no JWT/token validation, no caching layer, no multi-parser request path, no asserted-identity header described. (The `oneclickv2-proxy` session model is undocumented — see doc-gaps below.)
- **Undocumented knobs (Lens I):** `SerialPort` is pinned to a fixed value `0`; no OS-user/role/duration/port-selection parameter exists in the published schema. A non-zero `SerialPort` should return `InvalidArgsException` (expected refute).

**Open doc-gaps (confirm the surface before treating as closed):**
1. **Tenant-isolation of the Nitro virtual serial port** — no public statement specific to this data path (Area 3). *Highest-value, service-plane; needs internal/architecture source or authorized multi-tenant test.*
2. **`oneclickv2-proxy` session-to-instance binding / tenant segregation** — endpoint host+port only; no handshake/token model documented (Area 3).
3. **Baseline `kernel.sysrq` default on AWS-provided AMIs** — unstated; determines which SysRq ops are reachable out-of-the-box (Area 10).
4. **`sulogin`/emergency-target password enforcement per AMI family** — determines whether GRUB single-user yields a passwordless root shell (Area 2).
5. **SCP-deny-`EnableSerialConsoleAccess` vs. declarative-policy-`status:enabled` conflict** — the two mechanisms act on different layers; AWS gives no worked example of the conflict case.
6. **Admin-side session-termination API** — none found; confirm absence against the full EC2 API reference (Area 7).
7. **Throttling/anti-automation on the push + SysRq key-send paths** — not documented either way (Area 9).

---

*End of plan. Documentation-derived hypotheses only; a hunter must validate each against an authorized environment, honoring the HARD STOP on any AWS service-plane / cross-tenant evidence.*
