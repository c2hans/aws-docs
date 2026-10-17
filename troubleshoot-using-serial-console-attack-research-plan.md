# EC2 Serial Console — Attack Research Plan

**Source of leads:**
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-using-serial-console.html (target)
- `connect-to-serial-console.{html,md}`, `configure-access-to-serial-console.{html,md}`, `ec2-serial-console-prerequisites.{html,md}`, `disconnect-serial-console-session.{html,md}`, `troubleshoot-windows-sac.{html,md}`
- Mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`
- IAM refs: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2-instance-connect.md`, `.../list_ec2.md` (serial-console actions)

**Status:** documentation-derived hypotheses only; nothing has been tested against a live AWS account. Every lead below is a boundary that *might not hold* plus the exact observation that would settle it.

---

## 0. How to use this document
- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true / Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the EC2 Serial Console byte stream is terminated inside AWS's Nitro service plane. The moment any evidence shows you have reached the **Nitro hypervisor, the serial-console backend service, another tenant's instance, or any AWS-owned identity/credential/ARN**, stop, preserve evidence, and flag for AWS-Security disclosure. Do **not** escalate past existence.
- A hunter must have *authorization to test the specific account(s)* and should use only synthetic/canary instances and canary OS passwords. Every resource created (test instances, pushed keys) must be torn down.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Cross-tenant console access** — push an SSH public key to, or open a browser/SSH serial session against, an EC2 instance **owned by another AWS account** (or by another principal/team in the same account the IAM policy did not intend to reach). *Observation that proves it:* a `login:`/`SAC>`/GRUB prompt returned for an `instance-id` outside the caller's authorized set.
2. **IAM→OS privilege escalation** — go from "holds `ec2-instance-connect:SendSerialConsoleSSHPublicKey`" (and/or console access) to **root (Linux) / SYSTEM-equivalent (Windows)** on the instance **without knowing an OS password**, via GRUB boot-param editing, SysRq, or SAC built-in commands.
3. **Network-control bypass as an ingress/egress channel** — use the serial console (which is *outside the VPC and ignores Security Groups and NACLs*) to interact with an instance whose network controls would otherwise deny all access, including an instance deliberately isolated during incident response.
4. **Account-wide exposure via the binary toggle** — flip `EnableSerialConsoleAccess` (or defeat a declarative-policy/SCP meant to prevent it) to expose the serial console of **every** instance in an account/region.
5. **Revocation-completeness gap** — keep an active serial-console session alive after the IAM permission / account access that authorized it is revoked or expires.
6. **Service-plane reach (hard stop)** — from the serial port, reach the Nitro hypervisor or the shared serial-console backend. Confirm existence only, then stop.
7. **Audit evasion** — perform a security-relevant action over the serial console that produces no durable AWS-side log record.

---

## 2. Components, Assets, and Design

### 2.1 What the feature is (mechanism, not marketing)
EC2 Serial Console gives out-of-band access to an instance's **virtual serial port** (`ttyS0` on Linux, `COM1` on Windows). Per `configure-access-to-serial-console.md`: *"EC2 Serial Console uses a virtual serial port connection… This connection is independent of the instance VPC… Because this connection is outside of the VPC network, EC2 Serial Console does not use the instance security group or the subnet network ACL to authorize traffic to the instance."* The port is terminated by the Nitro system (feature requires Nitro virtualized or most bare-metal instances). It works even with no instance networking.

### 2.2 Customer-facing interfaces
- **Browser-based client** (EC2 console → *Actions ▸ Monitor and troubleshoot ▸ EC2 Serial Console ▸ Connect*). Opens an in-browser terminal over **WebSocket on port 443** to the **EC2 Instance Connect proxy** for the Region (`ec2-serial-console-prerequisites.md`):
  - Commercial + GovCloud: `prod.{region}.oneclickv2-proxy.ec2.aws.dev`
  - China: `prod.{region}.oneclickv2-proxy.ec2.a2z.org.cn`
  - "The browser-based client handles the permissions and provides a successful connection."
- **SSH client** to the regional serial-console service endpoint. Username format **`{instance-id}.port0`**; endpoint e.g. `serial-console.ec2-instance-connect.us-east-1.aws` (per-Region endpoint + SSH host fingerprint table in `connect-to-serial-console.md`). Flow:
  1. `aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id <id> --serial-port 0 --ssh-public-key file://key.pub --region <r>` pushes a public key, **valid 60 seconds**, and *starts* the session.
  2. `ssh -i key <id>.port0@<regional endpoint>` within that window.
- **Control-plane APIs** (account-level toggle): `ec2:EnableSerialConsoleAccess`, `ec2:DisableSerialConsoleAccess`, `ec2:GetSerialConsoleAccessStatus`.

### 2.3 Accounts / ownership
- **Customer account** owns the instances; identity to reach the console is IAM (SigV4) for the push action + OS-level credential for the shell.
- **AWS serial-console service account** owns the shared regional endpoint `serial-console.ec2-instance-connect.{region}.aws` and the `oneclickv2-proxy` browser proxy. This single regional endpoint **fronts the serial consoles of all customers' instances in the Region** → classic shared-service-account/multi-tenant surface.
- **AWS Nitro service plane** terminates the virtual serial port (the hard-stop boundary).

### 2.4 Identity & gating (three stacked gates)
1. **Account level (binary, per-Region):** `SerialConsoleAccessEnabled` true/false. `GetSerialConsoleAccessStatus` also returns `ManagedBy` ∈ {`account`, `declarative-policy`}. When managed by a declarative policy you *cannot* change it in-account. SCPs can allow/deny org-wide.
2. **IAM level (per-instance):** `ec2-instance-connect:SendSerialConsoleSSHPublicKey` on resource `arn:…:instance/{id}`. **Supported condition keys: `aws:ResourceTag/${TagKey}` and `ec2:ResourceTag/${TagKey}` only.** Docs recommend scoping to specific instance IDs or ResourceTag ABAC; default (if unscoped) is "all users with this permission can connect to the serial console of all EC2 instances." **Critical doc statement:** *"After pushing the SSH key to the instance, the SSH connection is not subject to the IAM policies that you configured to grant users EC2 Serial Console access."*
3. **OS level:**
   - **Linux:** a **password-based OS user** must exist to *use* the console (you can *connect* without one). GRUB single/emergency mode prompts for the user password. SysRq magic keys and GRUB menu editing are reachable pre-auth.
   - **Windows:** **SAC**. "Granting serial console permissions is equivalent to granting admin-level privileges on the instance." SAC `cmd` channels require admin credentials, **but the SAC built-in commands do not require sign-in** (see 2.6).

### 2.5 Session properties (`connect-to-serial-console.md`, `disconnect-serial-console-session.md`)
- **Only 1 active serial-console connection per instance.**
- Session lasts ~**1 hour**; AWS disconnects it during system maintenance.
- **~30 seconds to tear down** a session before a new one can start.
- Pushed public key removed after **60 seconds** if not used.
- **"The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist until the maximum duration… is reached."**
- Instance must be `running`.

### 2.6 Untrusted-input / privileged-action surfaces reachable from the serial port
- **Linux GRUB (`troubleshoot-using-serial-console.md`):** attacker presses a key to stop boot, presses `e`, edits the kernel command line (`linux`/`linux16`), adds `single`/`emergency`. Docs' own example shows the full editable cmdline including `rd.shell=0`, `console=ttyS0,115200n8`.
- **Linux SysRq:** `CTRL+0` (browser) or `~B` (SSH) sends a break; then single-key kernel commands incl. `b` reboot, `c` crash, `e` terminate-all-tasks, `f` OOM-kill, `i` kill-all-tasks, `o` poweroff, `s` sync, `u` unmount, `k` SAK. Governed by `kernel.sysrq` sysctl.
- **Windows SAC built-ins (`troubleshoot-windows-sac.md`, "These commands do not require you to sign in"):** `restart`, `shutdown`, `crashdump` (force stop error → memory dump), `k <pid>` (kill process), `l`/`r` (change priority), `m <pid> <MB>` (limit memory), `i` (list NICs + IPs), `i <#> <ip> <subnet> <gateway>` (**reconfigure networking**), `d` (kernel log), `t`/`f`/`p` (process & thread list), `id` (instance identification), `s` (set system clock), `lock`. The `cmd` channel itself requires admin credentials.

### 2.7 ASCII pipeline

```
                         AWS service plane (shared, multi-tenant)
                   ┌───────────────────────────────────────────────┐
 Customer IAM      │  oneclickv2-proxy (WSS/443)  serial-console.*  │
 principal         │        │  (browser)             │ (SSH, 1/instance)
   │ SigV4         │        │                        │  user=<id>.port0
   │ SendSerialConsoleSSHPublicKey (push key, 60s)   │
   ▼               │        ▼                        ▼
 [IAM authz: instance/{id}, ResourceTag only] ── gate 2
                   │   ┌──────────────────────────────────────┐
 Account toggle ───┼──▶│   Nitro virtual serial port (ttyS0/COM1) │ ◀── HARD STOP (hypervisor / backend)
 Enable/Disable    │   └──────────────────────────────────────┘
 SerialConsoleAccess (gate 1, per-Region, binary)        │  (NO Security Group / NACL — gate bypasses VPC)
                   └─────────────────────────────────────┼─────────┘
                                                          ▼
                                            Guest OS console (gate 3)
                                     Linux: login+passwd │ GRUB edit │ SysRq
                                     Windows: SAC (built-ins pre-auth; cmd=admin creds)
```

---

## 3. API / Interface Inventory

| Name | Method / IAM action | Mutating | Internal/External | Callable from Internet | Authorized callers | Notes (question seeds) |
|---|---|---|---|---|---|---|
| Push serial key | `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | **Yes** (starts session) | External | Yes (SigV4) | Principals with the action on `instance/{id}` | Resource = `instance/{id}`; **cond keys ResourceTag only — NO `ec2:osuser`** (sibling `SendSSHPublicKey` *has* `ec2:osuser`). Starts a session; one at a time. → Lens A, X, S |
| Push standard key (sibling) | `ec2-instance-connect:SendSSHPublicKey` | Yes | External | Yes | Same shape | Supports `ec2:osuser` → parity contrast for X |
| Enable account access | `ec2:EnableSerialConsoleAccess` | **Yes, account-wide** | External | Yes | Holder of the action | **No resource type (`Resource:"*"`), cond key `ec2:Region` only.** Binary per-Region. → Lens E, R, S |
| Disable account access | `ec2:DisableSerialConsoleAccess` | Yes, account-wide | External | Yes | Holder | Same shape; does it kill live sessions? → Lens AA |
| Account access status | `ec2:GetSerialConsoleAccessStatus` | No | External | Yes | Holder | Returns `SerialConsoleAccessEnabled` + `ManagedBy`. No resource-level perms → sample policies force `Resource:"*"`. → Lens A/U |
| Browser connect | console → WSS/443 → `prod.{region}.oneclickv2-proxy.ec2.aws.dev` | n/a (session) | External | Yes | "handles the permissions" | What identity does the proxy use to authorize? WebSocket. → Lens CC/A/V |
| SSH connect | `ssh <id>.port0@serial-console.ec2-instance-connect.{region}.aws` | n/a (session) | External | Yes | Anyone holding the private key for the 60s-pushed public key | **"not subject to the IAM policies" after push.** Username enumerable. → Lens A/M/U |
| In-session shell | GRUB / SysRq / SAC | Yes (OS state) | — | — | OS user / pre-auth kernel/SAC paths | Privilege-escalation + DoS primitives → Lens E/L |

No `[NEW]` marker is present on these pages, but the **China/GovCloud partition endpoints**, the `ManagedBy: declarative-policy` field, and the **SAC-enabled-by-default AMIs since 2026.09.09** (`troubleshoot-windows-sac.md`) are the freshest surface — prioritize accordingly (Section 5).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Customer A IAM principal | Customer B's instance serial console | `SendSerialConsoleSSHPublicKey` / SSH to `<id>.port0@shared-endpoint` | A `login:`/`SAC>`/GRUB prompt returns for an `instance-id` the caller's account does not own → **cross-account breach (Critical, hard stop)** |
| Intra-account low-priv principal | Instance the IAM policy did not intend | Unscoped or ResourceTag-only policy | Push/connect succeeds against an instance outside intended tag/ID scope → ABAC/least-priv breach |
| IAM authorization plane | Live serial byte stream | Post-push SSH session | Session continues to authorize actions after the IAM permission is revoked/expired → **revocation gap** |
| Customer VPC network controls (SG/NACL) | Instance OS | Out-of-VPC virtual serial port | Interactive shell reached on an instance whose SG/NACL deny all ingress → network-control bypass channel (by design; concern = isolation during IR) |
| "Can push key / open console" privilege | OS root / SYSTEM | GRUB edit, SysRq, SAC built-ins | Root shell / instance crash / reconfigured NIC obtained **without an OS password** → IAM→OS privesc |
| Holder of `EnableSerialConsoleAccess` | All instances in account/Region | Binary account toggle | One API call exposes every instance's console; or a declarative-policy/SCP meant to block it is defeated |
| Any serial-port occupant | Nitro hypervisor / shared serial-console backend | Serial port termination | **Any** packet/response/identity from the hypervisor or backend service → **HARD STOP, service-plane breach** |
| One session on a shared endpoint | Another instance's/session's bytes | Shared regional endpoint, 1-session cap | Receiving another instance's console output, or holding the single slot to deny the owner → cross-tenant leak / DoS |

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Cross-tenant / cross-scope console access via the shared endpoint (Lens A) — **TOP PRIORITY**
**Background.** A single regional endpoint (`serial-console.ec2-instance-connect.{region}.aws`) and one browser proxy front *every* customer's instance consoles in the Region. The only tenant binding is the IAM check on `SendSerialConsoleSSHPublicKey` for `instance/{id}` and whatever the backend enforces on the SSH username `<instance-id>.port0`.
**Security Concern.** Instance IDs are the sole resource identifier in the username and are *not* secret; the recommended-but-optional scoping (specific IDs / ResourceTag) means a broad or mis-scoped policy connects to "all EC2 instances." The question is whether the **service backend** independently re-binds the pushed key / SSH username to the caller's account, or trusts that IAM already did.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* `SendSerialConsoleSSHPublicKey` authorizes on **instance existence** but the SSH endpoint does not re-verify account ownership → pushing a key for a **foreign-account** `instance-id`, then `ssh <foreign-id>.port0@endpoint`, yields a prompt. **Oracle:** any prompt for a non-owned ID. **Hard stop on success — Critical.**
- *Claim:* The browser `oneclickv2-proxy` authorizes using a session/identity that can be pointed at an `instance-id` outside the signed-in principal's scope (→ also Lens CC). **Oracle:** WSS session established to a non-authorized instance.
- *Claim:* `GetSerialConsoleAccessStatus` / error differentials (NotFound vs AccessDenied vs 500) across `SendSerialConsoleSSHPublicKey` form an **instance-existence oracle** across accounts. **Oracle:** distinct, reliable response classes for own-exists / foreign-exists / nonexistent.
**Doc evidence:** `connect-to-serial-console.md` (username `<id>.port0`, shared endpoint table); `configure-access-to-serial-console.md` ("all users with this permission can connect to the serial console of all EC2 instances"). **Severity-if-true:** cross-account = **Critical**; intra-account wildcard = Medium. **Preconditions:** two test accounts you control. **Cost:** low. **Stop:** first foreign prompt.

### Area 2 — IAM/console-access → OS root/SYSTEM privilege escalation without an OS password (Lens E, +L)
**Background.** Three documented pre-authentication paths exist on the serial port before any OS login succeeds.
**Security Concern.** The feature's intended OS gate (Linux password-based user; Windows admin creds for the `cmd` channel) can be side-stepped by boot-time and out-of-band primitives the docs themselves describe.
**High-level Test Scenarios:**
- *Claim (Linux/GRUB):* With console access + reboot (via SysRq `b`, SAC `restart`, `ec2:RebootInstances`, or `sudo reboot`), press `e` at the GRUB menu and append `init=/bin/bash` (or `rd.break`) to the kernel line → **root shell with no password**, despite the docs steering users to the password-gated `single`/`emergency`. **Oracle:** a `#` root prompt with no password entered. **Severity:** High (full instance compromise from console-access alone).
- *Claim (Linux/SysRq):* SysRq keys (`c` crash, `b` reboot, `o` poweroff, `e`/`i` kill tasks) are reachable with console access and `kernel.sysrq=1`, giving **DoS/forced-reboot** without OS login — and the forced reboot enables the GRUB chain above. **Oracle:** instance reboots/crashes from console input alone.
- *Claim (Windows/SAC):* The SAC built-ins `restart`/`shutdown`/`crashdump`/`k <pid>`/`m <pid> <MB>`/`i <#> <ip> <subnet> <gateway>`/`d`/`id` run **without sign-in** ("These commands do not require you to sign in"), so a principal holding only `SendSerialConsoleSSHPublicKey` on a Windows instance can **crash it, force a memory dump, kill arbitrary processes, rewrite its IP/gateway, read the kernel log, and read instance identification** with **no Windows credential**. **Oracle:** any of those effects observed from the `SAC>` prompt pre-auth. **Severity:** High (unauthenticated DoS + network reconfiguration + kernel/identity info-leak on the instance).
**Doc evidence:** `troubleshoot-using-serial-console.md` (GRUB edit, SysRq table); `troubleshoot-windows-sac.md` (built-in command table + "do not require you to sign in"; "equivalent to granting admin-level privileges"). **Preconditions:** console access to a test instance. **Cost:** low. **Stop:** demonstrate one primitive per OS; do not pivot further into the OS.

### Area 3 — Post-push session / revocation-completeness gaps (Lens AA, +M, +C)
**Background.** The connection "is not subject to the IAM policies" after key push and "continues to persist until the maximum duration… even if your IAM credentials expire."
**Security Concern.** Grants are checked at *push* time only; neither IAM-permission removal, account-access disable, nor credential expiry is documented to terminate an in-flight session.
**High-level Test Scenarios:**
- *Claim:* After a session is established, calling `DisableSerialConsoleAccess` (account toggle) does **not** drop the live session. **Oracle:** session still interactive post-disable. **Severity:** High (revocation gap during IR).
- *Claim:* Detaching/denying the `SendSerialConsoleSSHPublicKey` IAM permission (or the principal's keys expiring/being deleted) does **not** terminate the live session. **Oracle:** session persists. **Severity:** High.
- *Claim (M):* The 60-second pushed public key is **not** strictly single-use / instance-bound — e.g. the same pushed key authorizes more than one connection within the window, or the `<id>.port0` username + a race around the 30-second teardown lets a second party seize the single session slot. **Oracle:** two successful connects from one push, or session seizure. **Severity:** Medium–High.
**Doc evidence:** `connect-to-serial-console.md` (persistence past IAM-cred expiry; 60s key window; 30s teardown; 1 session/instance). **Preconditions:** one account. **Cost:** low–medium. **Stop:** first confirmed persistence/replay.

### Area 4 — Account-wide binary toggle & declarative-policy/SCP enforcement (Lens E, R, S, U)
**Background.** `EnableSerialConsoleAccess`/`DisableSerialConsoleAccess` are **account-wide, per-Region, no resource type, condition key `ec2:Region` only**; status carries `ManagedBy: account | declarative-policy`.
**Security Concern.** A single low-granularity permission flips the console on for **all** instances in the account/Region; and the "declarative policy" / SCP meant to *prevent* enabling must actually be enforced server-side, not just hidden in the console.
**High-level Test Scenarios:**
- *Claim (E/R):* Any principal granted `ec2:EnableSerialConsoleAccess` (sample policies use `Resource:"*"`) can expose every instance's console account-wide — there is **no way to scope the enable to a subset of instances** (only `ec2:Region`). Confirm no finer scoping exists. **Oracle:** IAM reference shows no resource type / only `ec2:Region`. **Severity:** least-priv footgun → Low; but **the AWS-authored sample policy pins `Resource:"*"` for the Describe/status actions as well** — audit whether that is forced or avoidable (Lens R, AWS-authored artifact). 
- *Claim (U):* When `ManagedBy=declarative-policy`, the account-direct `EnableSerialConsoleAccess` call is actually **rejected server-side**, not merely blocked in the console. If a direct API call still flips it, the declarative-policy guarantee is advisory only. **Oracle:** `EnableSerialConsoleAccess` succeeds against an account under a deny-ing declarative policy / SCP. **Severity:** High (org guardrail bypass).
- *Claim (S):* An SCP/IAM `Deny` written against `ec2:DisableSerialConsoleAccess` but not `Enable` (or vice-versa), or keyed on a wrong/absent condition, leaves one direction open. **Oracle:** the un-denied twin still works. **Severity:** Medium.
**Doc evidence:** `list_ec2.md` (both actions: no resource type, `ec2:Region` only); `configure-access-to-serial-console.md` (declarative-policy / SCP / `ManagedBy`; sample policies with `Resource:"*"`). **Severity-if-true:** guardrail bypass High; footgun Low. **Stop:** confirm enforcement location.

### Area 5 — Network-control bypass as an alternate ingress/egress channel (Lens V, D)
**Background.** The console connection is "independent of the instance VPC" and "does not use the instance security group or the subnet network ACL." It works with no instance networking.
**Security Concern.** This is a *by-design* out-of-band path, but it is a trust-boundary statement: any control a defender builds on SG/NACL (including **isolating a compromised instance during incident response** by stripping its SGs) does **not** cover the serial console. It is also a candidate data-exfil / command-ingress channel that evades VPC flow logs.
**High-level Test Scenarios:**
- *Claim:* An instance with **all security groups removed / a deny-all NACL** (the standard IR "network quarantine") is still fully reachable and controllable via the serial console. **Oracle:** interactive shell on a network-quarantined instance. **Severity:** High as an IR-evasion / persistence channel (note: expected behavior — frame as a documented risk the hunter should confirm defenders account for).
- *Claim (D, hard-stop-adjacent):* From the serial port, can input influence anything beyond the single instance — the control ENI, the Nitro control plane, failover/health, or a neighboring instance on the shared backend? **Oracle:** any response originating outside the target instance. **HARD STOP on any service-plane signal — Critical.**
**Doc evidence:** `configure-access-to-serial-console.md` (independent of VPC, ignores SG/NACL); `troubleshoot-windows-sac.md` ("does not require your instance to have any networking capabilities"). **Stop:** at the instance boundary; escalate to disclosure on any cross-boundary signal.

### Area 6 — Action-family parity gap: missing `ec2:osuser` on the serial action (Lens X, S)
**Background.** `ec2-instance-connect:SendSSHPublicKey` (standard SSH) supports the `ec2:osuser` condition key — a policy can restrict *which OS user* a pushed key may target. Its sibling **`SendSerialConsoleSSHPublicKey` supports only `aws:ResourceTag`/`ec2:ResourceTag` — no `ec2:osuser`.**
**Security Concern.** For the serial path there is **no IAM-level control over which OS user the session can target**: the `SendSerialConsoleSSHPublicKey` request model has **no `InstanceOSUser` parameter at all** (its sibling `SendSSHPublicKey` requires one, marked Required: Yes), and no `ec2:osuser` condition key. A policy author who assumes `ec2:osuser` restricts serial logins (as it does for standard EC2 Instance Connect) is wrong.
- **Linux:** partly moot — OS identity is re-established at the guest `login:`/`Password:` prompt, so the missing lever does not by itself grant OS access (but it does nothing to stop a `root` login attempt, and chains straight into the Area 2 GRUB/SysRq pre-auth bypass).
- **Windows:** **NOT moot** — `configure-access-to-serial-console.md`: *"Granting serial console permissions is equivalent to granting admin-level privileges on the instance."* There is **no IAM or API mechanism to scope a serial-console grant to a non-admin Windows user**; any principal granted the serial push on a Windows instance is effectively an instance admin.
**High-level Test Scenarios:**
- *Claim (Windows):* A principal granted `SendSerialConsoleSSHPublicKey` on a Windows instance has **admin-equivalent** reach with no way for the account to down-scope it via IAM. **Oracle:** admin-level SAC/cmd outcome from a grant the operator believed was limited. **Severity:** High (grant is implicitly admin; combine with Area 2 pre-auth SAC built-ins).
- *Claim (Linux):* A policy intended to confine a principal to a non-root OS user via `ec2:osuser` is **inert** for serial-console access; the principal reaches the `login:` prompt and can attempt `root`, then pivots via GRUB (Area 2). **Oracle:** serial `root` login / GRUB root shell despite an `ec2:osuser`-style intent. **Severity:** Medium–High.
- *Claim (U/doc-vs-API):* Confirm the request model asymmetry (serial action has no OS-user param; standard action requires one). **Oracle:** `API_SendSerialConsoleSSHPublicKey` vs `API_SendSSHPublicKey` request syntax. **Severity:** Informational (sharpens the above). **(Confirmed from the API reference during planning.)**
**Doc evidence:** `list_ec2-instance-connect.md` (condition-key rows); `API_SendSerialConsoleSSHPublicKey.md` / `API_SendSSHPublicKey.md` (parameter lists); `configure-access-to-serial-console.md` (Windows admin-equivalence). **Stop:** confirm the delta and its runtime consequence per OS.

### Area 7 — Transport & endpoint trust (Lens Y, M)
**Background.** Browser client is WSS/443 to `oneclickv2-proxy`; SSH client verifies a **per-Region published host fingerprint**; "the fingerprint only appears the first time you connect."
**Security Concern.** First-connect TOFU on the SSH fingerprint and the proxy's TLS posture are the MITM surface the docs explicitly flag ("someone might be attempting a man-in-the-middle attack").
**High-level Test Scenarios:**
- *Claim:* The regional serial-console SSH endpoint negotiates below a documented TLS/cipher floor, or presents a cert/host key not matching the published fingerprint under some path (e.g. a partition endpoint). **Oracle:** fingerprint/cert mismatch accepted, or downgraded negotiation. **Severity:** High (MITM of a root-capable console).
- *Claim:* The `oneclickv2-proxy` WSS endpoint lacks HSTS / accepts http→ws downgrade / weak TLS. **Oracle:** cleartext or downgraded connection accepted. **Severity:** Medium–High.
**Doc evidence:** `connect-to-serial-console.md` (fingerprint table + MITM warning); `ec2-serial-console-prerequisites.md` (WSS/443 proxy endpoints). **Note:** this requires *interacting with the AWS-owned endpoint directly* — frame as network/TLS posture checks only, never attempts to reach another tenant; any success touching the service plane is a hard stop.

### Area 8 — Audit-log evasion (Lens O)
**Background.** The account-toggle APIs are ordinary `ec2:` calls covered by "all Amazon EC2 API actions are logged as management events" (`monitor-with-cloudtrail.md`). The sibling `SendSSHPublicKey` has an **explicit** CloudTrail audit walkthrough (worked JSON, `eventSource: ec2-instance-connect.amazonaws.com`, `requestParameters` with instance ID + OS user + key). The **interactive session bytes** are explicitly outside IAM ("not subject to the IAM policies").
**Security Concern.** Two gaps: (a) **doc-gap** — no AWS page gives a named statement or example that `SendSerialConsoleSSHPublicKey` *itself* is recorded in CloudTrail (unlike its sibling, which is documented); it is only *inferable* by analogy. (b) **No AWS-side logging of session content exists anywhere in the corpus** — unlike SSM Session Manager (separate service), there is no serial-console session transcript, no CloudTrail data-event type, and (per Area 5) no SG/NACL/VPC-Flow-Log telemetry because the path is outside the VPC. So pre-auth SAC built-ins (crash, NIC reconfig, process kill) and GRUB/SysRq actions execute with no documented AWS-side record.
**High-level Test Scenarios:**
- *Claim:* `SendSerialConsoleSSHPublicKey` is (or is not) emitted to CloudTrail, and with which `requestParameters`. **Oracle:** inspect CloudTrail after a push; confirm presence + fields. **Severity:** Informational (closes the doc-gap); High *as an attribution gap* if the push is unlogged.
- *Claim:* After the push, in-session actions (SysRq reboot, SAC `shutdown`/`crashdump`, GRUB edit) generate no CloudTrail / no session audit log. **Oracle:** diff CloudTrail + EC2 console-output before/after an in-session destructive action; only the push (if any) appears. **Severity:** Low–Informational alone; **enabler** that raises Area 2/5 severity.
**Doc evidence:** `monitor-with-cloudtrail.md` (sibling `SendSSHPublicKey` example; "all EC2 API actions are management events"); `connect-to-serial-console.md` ("not subject to the IAM policies"); `troubleshoot-windows-sac.md` (SAC built-ins pre-auth). **Stop:** characterize the logging gap; do not disable logging.

### Area 9 — Resource exhaustion / single-session denial (Lens L)
**Background.** Exactly **1 active session per instance**, **30-second teardown**, 1-hour cap.
**Security Concern.** The single-slot design is a self-DoS lever: a principal who can push keys can hold the only serial-console slot, **denying the legitimate operator out-of-band access precisely during an incident** (when network access is already broken).
**High-level Test Scenarios:**
- *Claim:* Holding one session (or rapidly re-pushing around the 30s teardown) prevents the owner from ever connecting. **Oracle:** owner's connect attempts fail while attacker holds the slot. **Severity:** Medium (intra-account IR denial); higher if combined with a cross-tenant push (Area 1 → cross-tenant DoS = High).
**Doc evidence:** `connect-to-serial-console.md` / `disconnect-serial-console-session.md` (1 session, 30s teardown). **Stop:** confirm the denial window.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Push key / connect to a **foreign-account** instance | Shared regional endpoint + `SendSerialConsoleSSHPublicKey` | IAM resource `instance/{id}`; backend account-binding of `<id>.port0` |
| Reach an instance the ABAC/tag policy excluded | IAM `aws/ec2:ResourceTag` conditions | Tag-based `Condition` on the push action |
| Root/SYSTEM without OS password | GRUB / SysRq / SAC built-ins | Linux password-based user; Windows admin creds for `cmd` channel |
| Session survives IAM/account-access revocation | Post-push SSH session | (none documented — "not subject to IAM policies"; persists past cred expiry) |
| Reach another tenant / Nitro from the serial port | Nitro serial-port termination | VPC-independent isolation; service-plane boundary |
| Expose all consoles via account toggle / defeat declarative policy | `EnableSerialConsoleAccess`, SCP, declarative policy | Account-level default-off; SCP/declarative-policy guardrail |
| `ec2:osuser` assumed to restrict serial logins | `SendSerialConsoleSSHPublicKey` condition keys | (gap — osuser unsupported on serial action) |
| MITM the console connection | SSH fingerprint TOFU / WSS proxy TLS | Per-Region published fingerprints; TLS |
| Invisible in-session destructive actions | CloudTrail / session audit | (key-push event only; session unlogged) |
| Single-slot console denial during IR | 1-session cap + 30s teardown | (none — by design) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Nitro hypervisor, the shared serial-console backend, and the `oneclickv2-proxy` service itself** — AWS service plane. Probe only to the point of proving a boundary broke, then **hard stop + disclose**. Do not attempt code exec on, or lateral movement within, AWS-owned fleet.
- **The out-of-VPC design itself** is not a bug — SG/NACL bypass is documented and intended. In scope only as a *risk defenders must account for* (Area 5), not as a vuln in the service.
- **A user compromising their own instance** via GRUB/SysRq/SAC when they *legitimately* own it and hold console access is expected admin capability; the finding is only interesting when it **crosses a boundary** (cross-account, or privilege the IAM policy intended to deny — e.g. non-root-only principal → root; no-OS-cred principal → crash/NIC-reconfig).
- **Customer-authored** over-broad IAM policies (unscoped `SendSerialConsoleSSHPublicKey`) are least-privilege footguns, not AWS defects — *except* where an **AWS-authored sample policy** forces a weak default (Area 4, Lens R: audit the printed `Resource:"*"` statements).
- **OS/kernel bugs** in GRUB, SysRq, Linux, or Windows SAC themselves are vendor issues, not EC2 Serial Console issues (though reachability via the console is in scope).
- **DNS rebinding / private-only endpoint games**, IMDS on the managed Nitro layer, and product-feature-parity gaps.

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, with pages checked)
- **Lens B/C (PassRole / credential vending):** NULL. No API in `troubleshoot-using-serial-console.md`, `connect-to-serial-console.md`, `configure-access-to-serial-console.md`, or `list_ec2-instance-connect.md` accepts a role ARN or returns vended credentials; the push action takes only `InstanceId`/`SerialPort`/`SSHPublicKey`. No `roleArn`/`credentialProvider` field exists. *(Re-open if a future endpoint vends an OS credential.)*
- **Lens F (translation/injection):** NULL for a query/translation layer — the serial port carries **raw bytes**, no wire-protocol translation. *Partial doc-gap:* the serial-console backend presumably parses SSH + a framing layer; its native memory-safety is undocumented → mark "doc-gap — not testable from docs."
- **Lens G (SSRF):** NULL — pages checked: prerequisites, connect, configure-access, troubleshoot, SAC. **No field is a URL/URI/host the service dereferences, fetches, previews, or renders.** The only user-supplied blob is an **SSH public key** (routed instead to Lens M/key-handling).
- **Lens H (KMS/encryption-context):** NULL — no customer-managed-key or encryption-context field in any serial-console page.
- **Lens K (prompt injection):** NULL — no LLM/agent in the pipeline.
- **Lens P (identity proofing / registration):** NULL for IDV/KYB/OTP — no onboarding/verification workflow; the closest gate is the OS password (Area 2) and account toggle (Area 4), covered elsewhere.
- **Lens Q (file upload):** NULL — no logo/image/document/attachment upload; the SSH public key is the only uploaded artifact (Lens M).
- **Lens N (ARN/namespace migration):** NULL — no dual-live namespace; single `ec2-instance-connect:*` + `ec2:*SerialConsoleAccess` actions.
- **Lens W (attestation-conditioned authz):** NULL — no `kms:RecipientAttestation`/PCR/enclave gating on this feature.
- **Lens EE / FF (predictable-name land-grab / JWT-claims confusion):** NULL from docs — no global-namespace resolution and no customer-facing JWT/OIDC token in the serial-console flow (the browser proxy's internal auth is undocumented → **doc-gap**, see Lens CC note in Area 1).
- **Lens DD (cache-key vs authz):** NULL from docs — no documented caching layer; the `oneclickv2-proxy` internals are a **doc-gap**.
- **Lens CC (upstream-context injection):** **Doc-gap, keep open.** The browser `oneclickv2-proxy` "handles the permissions" but the docs do not describe how it asserts the caller's identity to the serial-console backend — fold into Area 1's browser-path scenario rather than closing it.

---

*Hard-stop reminder: the serial-console backend and Nitro layer are AWS's service plane. Confirm existence of any boundary break, preserve evidence, and route to AWS-Security disclosure — never escalate past the proof.*
