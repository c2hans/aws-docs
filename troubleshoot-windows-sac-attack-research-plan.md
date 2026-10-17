# EC2 Serial Console + Windows SAC — Attack Research Plan

Source of leads:
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-windows-sac.html (primary target)
- configure-access-to-serial-console.html, ec2-serial-console-prerequisites.html, connect-to-serial-console.html, ec2launch-v2.html
- Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` and `/work/aws-docs/docs/service-authorization/latest/reference/{list_ec2-instance-connect.md,list_ec2.md}`

Status: **documentation-derived hypotheses only; nothing has been tested against a live account.** This plan is for a hunter authorized to test their own instances/accounts. The feature is a legitimate out-of-band admin channel — most leads below are about whether the *authorization and isolation* around that channel hold, not whether the channel exists.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's own service plane (the serial-console proxy fleet, the EC2 Instance Connect service account, the Nitro hypervisor control plane), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not pivot off it.
- **Scope discipline:** the serial console deliberately gives instance-admin/out-of-band access to the *instance owner*. "I used my own serial console access to run SAC on my own instance" is **not** a finding. A finding is: access *without the authorization the docs require*, access to *another tenant's* instance, disclosure to a principal the docs imply is walled off, or an AWS-authored artifact that grants more than it claims.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. **Cross-tenant serial-console reach** — push an SSH key to / open a serial console session on an EC2 instance owned by *another account* (or another team denied by IAM), using only the `instance-id.port0` username and the shared regional proxy endpoint. Any `SAC>` prompt or login prompt on a foreign instance = Critical breach.
2. **IAM gate bypass / over-broad default** — obtain serial-console (=> Windows admin, see §2) access to an instance the caller's IAM policy was *intended* not to cover: via `Resource:"*"` footgun, ABAC tag self-widening, missing condition-key coverage, or an action-family sibling that skips the check.
3. **No-auth SAC command abuse** — from a serial console session on an instance where the caller has *no OS credentials*, execute state-changing SAC built-in commands (`restart`, `shutdown`, `crashdump`, `k <pid>`, `i <#> <ip> ...`) that require no sign-in, and confirm they take effect. Establish whether serial-console authorization alone (without Windows auth) is sufficient to disrupt/DoS/reconfigure the instance.
4. **Credential / sensitive-boot-output disclosure** — recover the Windows admin password material, RDP certificate thumbprint, or SAC session content emitted over COM1, via a principal/path the docs imply should not see it (notably `ec2:GetConsoleOutput` system-log retrieval vs serial-console access vs RDP).
5. **Session-isolation / interception** — hijack, intercept, or deny the single-per-instance serial console session; defeat the host-key fingerprint (MITM); or ride a session whose IAM creds have expired.
6. **AWS-authored IAM artifact audit** — prove any of the four sample policies in `configure-access-to-serial-console` grants more serial-console reach than its text claims.

---

## 2. Components, Assets, and Design

**What the feature is.** The EC2 Serial Console is an **out-of-band** virtual serial-port channel to an instance's COM1 (Windows) / `ttyS0` (Linux). On Windows, the serial port speaks to **SAC (Special Administration Console)** — a Windows Emergency Management Services (EMS) console enabled via `bcdedit /ems` + `/emssettings` and (optionally) a boot menu via `bcdedit /set {bootmgr}`. SAC lets you open authenticated `cmd` channels **and** run a set of built-in commands that require **no sign-in**.

**The decisive design facts (all doc-quoted):**

- **Out of band / bypasses all network controls:** *"This connection is independent of the instance VPC... Because this connection is outside of the VPC network, EC2 Serial Console does not use the instance security group or the subnet network ACL to authorize traffic to the instance."* → SG/NACL/VPC isolation are **not** in the trust path. The entire gate is account opt-in + one IAM action.
- **Windows serial console == instance admin:** *"Granting serial console permissions is equivalent to granting admin-level privileges on the instance. Further authentication is driven by Windows..."* → the IAM action `ec2-instance-connect:SendSerialConsoleSSHPublicKey` is effectively an admin-grant on every in-scope Windows instance.
- **SAC built-ins need no OS auth:** *"These commands do not require you to sign in."* The no-auth command set includes `restart`, `shutdown`, `crashdump` (forced bugcheck + memory dump), `k <pid>` (kill), `l/r/m <pid>` (reprioritize / memory-cap a process), `i <#> <ip> <subnet> <gateway>` (rewrite a NIC's IP config), `s mm/dd/yyyy` (set clock), `t`/`d` (process+thread list, kernel log), `id` (instance identification). Only `cmd` (open a shell channel) requires administrative credentials.
- **SAC on by default in newer AMIs:** *"Starting with version 2026.09.09, SAC is enabled by default on ... `EC2LaunchV2-Windows_Server-2019-English-Core-Base-*` [and] `-Full-Base-*`."* → serial-console access to instances from these AMIs immediately yields the `SAC>` prompt and its no-auth commands; no attacker setup step.
- **Credential emission over the serial port:** *"EC2Launch v2 relies on the serial port to perform several initialization tasks during boot, such as emitting the instance password and RDP thumbprint... If you connect before EC2Launch v2 emits its output... you might not be able to retrieve the instance password or other console output."* (whether the password is cleartext or encrypted blob = key question, see §5 Area D / subagent-2 findings).
- **SAC output lands in the system log:** *"If you enable SAC or the boot menu, the Amazon EC2 system log (available from the EC2 console or the `get-console-output` CLI command) might contain output from SAC or the boot menu."* → a second retrieval path (`ec2:GetConsoleOutput`) with its own IAM.
- **Post-key-push SSH is NOT subject to IAM:** *"After pushing the SSH key to the instance, the SSH connection is not subject to the IAM policies that you configured to grant users EC2 Serial Console access."* The pushed public key is removed after **60 s**; the session persists up to **~1 hour**; *"The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist."*
- **One session per instance; 30 s teardown.** *"Only 1 active serial console connection is supported per instance."*

**Identity / resource shape.**
- Resource identifier in the SSH path is the **instance-id** encoded in the username: `i-0123....port0` → `<regional-serial-console-endpoint>`. The instance-id is the *only* resource name the client supplies to the proxy after key push.
- Regional proxy / endpoints (shared AWS fleet): browser client → `prod.<region>.oneclickv2-proxy.ec2.aws.dev:443`; SSH → `serial-console.ec2-instance-connect.<region>.aws` (and `ec2-serial-console.<region>.api.aws` in some partitions). Per-region host-key **fingerprints** published for MITM verification.
- Account opt-in flag: `SerialConsoleAccessEnabled` (per-account, per-region), set by `ec2:EnableSerialConsoleAccess` / read by `ec2:GetSerialConsoleAccessStatus`, `ManagedBy = account | declarative-policy`.
- IAM gate: `ec2-instance-connect:SendSerialConsoleSSHPublicKey` (supports per-instance ARN; recommended restriction). `DescribeInstances`/`DescribeInstanceTypes`/`GetSerialConsoleAccessStatus` are `Resource:"*"` only.

**ASCII pipeline:**

```
  Caller (IAM principal)
     │  (1) ec2-instance-connect:SendSerialConsoleSSHPublicKey  [IAM-checked, per-instance ARN]
     │      pushes ephemeral SSH pubkey (valid 60s)
     ▼
  EC2 Instance Connect / Serial Console proxy fleet   <-- SHARED AWS SERVICE PLANE (hard stop zone)
     │  (2) SSH to  i-xxxx.port0 @ serial-console.ec2-instance-connect.<region>.aws
     │      *** NOT subject to IAM after key push ***  <-- what binds session to the right instance/account?
     ▼  out-of-band virtual serial port  (bypasses SG / NACL / VPC)
  Instance COM1  ──►  Windows SAC (EMS)
     ├─ built-in cmds (NO sign-in): restart/shutdown/crashdump/k/i/...
     └─ cmd channel (requires Windows admin creds)
         │
  (boot) EC2Launch v2 ──emits──► admin password + RDP thumbprint over COM1
         └──────────► also captured into EC2 system log  ──►  ec2:GetConsoleOutput  [separate IAM path]
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM principal | A specific instance's serial console | `SendSerialConsoleSSHPublicKey` (per-instance ARN) | Opening a `SAC>`/login prompt on an instance **not covered** by the caller's allow (or explicitly denied) = breach |
| Account A principal | Account B's instance serial console | shared regional proxy; username = `instance-id.port0` | Any session/prompt reaching an instance in **another account** = **Critical** |
| Caller (no OS creds) | Windows instance state | SAC no-auth built-ins | `restart`/`shutdown`/`crashdump`/`i`/`k` taking effect **without Windows login** — expected for the owner; a breach only if serial-console authz itself was bypassed/over-broad |
| Serial-console client | AWS serial-console proxy fleet | SSH to proxy endpoint | Reaching any proxy-fleet host service beyond one's own session, or obtaining proxy-fleet identity/creds = **Critical + hard stop** |
| Principal with `ec2:GetConsoleOutput` only | Boot/SAC console output (password material, RDP thumbprint) | system-log retrieval | Reading sensitive boot output via `GetConsoleOutput` when denied serial-console/RDP = disclosure breach |
| One serial-console session | Another session on the same instance | single-session + 30 s teardown | Intercepting/reading/injecting into a session you did not open = breach; blocking the owner's session = DoS |
| Client ↔ proxy endpoint | TLS/SSH host key | published per-region fingerprint | A `SAC>` session established against a **mismatched** host key (MITM) that the client accepted = breach |
| Caller | AWS service plane (any) | — | Any AWS-owned credential/ARN/account surfaced = **hard stop** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | API | Existing | **Mutating** (starts a session, pushes key) | External | Push 60 s SSH pubkey → start serial console session | Yes | IAM principals w/ the action (per-instance ARN recommended) | **The admin-grant on Windows.** Supports resource-level ARN. Condition-key coverage = Area F. |
| `ec2-instance-connect:SendSSHPublicKey` | API | Existing | Mutating | External | In-VPC EC2 Instance Connect (SSH), not serial | Yes | IAM principals | **Sibling** — compare condition-key / resource parity (Lens X) |
| `ec2:EnableSerialConsoleAccess` | API | Existing | **Mutating** (account-wide toggle) | External | Opt the whole account+region into serial console | Yes | IAM principals w/ action, `Resource:"*"` | Account-wide blast radius; no resource scoping |
| `ec2:DisableSerialConsoleAccess` | API | Existing | Mutating | External | Opt account out | Yes | " | Can an attacker *disable* to hide / DoS troubleshooting? |
| `ec2:GetSerialConsoleAccessStatus` | API | Existing | Non-mutating | External | Read opt-in flag | Yes | " (`Resource:"*"`) | No resource scoping |
| `ec2:GetConsoleOutput` | API | Existing | Non-mutating | External | Retrieve system log (may contain SAC/boot output) | Yes | IAM principals | **Second disclosure path** — Area D |
| `ec2:GetPasswordData` | API | Existing | Non-mutating | External | Retrieve **encrypted** admin password blob | Yes | IAM principals | Normal password path — contrast with serial emission |
| SSH to `i-xxxx.port0@serial-console...<region>.aws` | SSH | Existing | Mutating (interactive) | External | Interactive serial session | Yes | **Anyone with the ephemeral key** — *not IAM-checked post-push* | Key valid 60 s; session ~1 h; survives cred expiry |
| Browser client → `prod.<region>.oneclickv2-proxy.ec2.aws.dev` | WSS/443 | Existing | Mutating | External (service plane) | Browser serial terminal | Yes | Console users | Shared proxy fleet |
| SAC built-in cmds (`restart`,`shutdown`,`crashdump`,`k`,`i`,`l`,`r`,`m`,`s`,`t`,`d`,`id`,`ch`,`lock`) | in-band | Existing | Mutating | OS-internal via serial | via serial only | **No OS auth required** | `cmd`/`lock` are the only auth-gated ones |

**Doc-flagged NEW / focus-worthy surface:** the **2026.09.09 default-SAC-enabled AMIs** (`EC2LaunchV2-Windows_Server-2019-English-{Core,Full}-Base-*`) — newest, least-reviewed change; it turns "attacker must enable SAC" into "SAC already waiting." Prioritize.

---

## 5. Recommended Areas of Focus
*(ordered: newest/cross-tenant/service-plane first)*

### Area A — Cross-tenant serial-console reach via the shared proxy (Lens A / V / M) — **HIGHEST**
**Background.** After key-push the SSH connection is *not* IAM-checked; the only resource name the client gives the proxy is the instance-id baked into the username `i-xxxx.port0`. The proxy fleet is shared across all tenants in a region (single `serial-console.ec2-instance-connect.<region>.aws` endpoint).
**Security Concern.** If instance→account ownership is enforced *only* at the `SendSerialConsoleSSHPublicKey` IAM call and not re-bound inside the proxy/session, a caller who can push a key (or replay/guess the ephemeral key window) might reach a foreign instance by naming its instance-id. Instance-ids are structured and semi-enumerable.
**High-level Test Scenarios.**
- Claim: *I can open a serial console session on an instance in another account by pushing a key for its instance-id and SSH-ing `i-<foreign>.port0@<regional-endpoint>`.* → Oracle: a `SAC>`/login prompt or any COM1 output from the foreign instance. → Precondition: two accounts you control; foreign instance-id. → Severity: **Critical**. → Stop if it works and it is genuinely cross-account.
- Claim: *The IAM check validates the instance-id string but not that the instance is in the caller's account* (existence-not-ownership, Lens A). → Oracle: `SendSerialConsoleSSHPublicKey` succeeds (not AccessDenied/NotFound) for a foreign/arbitrary instance-id. → Note the error-differential oracle: `AccessDenied` vs `InvalidInstanceID.NotFound` vs validation-500 across own/foreign/nonexistent ids (enumeration signal).
- Claim: *The 60 s ephemeral pubkey can be used by a different network client than the one that pushed it* (session not pinned to push identity/source) → interception/relay. → Oracle: key pushed by principal X, SSH completed from an unrelated client, reaches the session.
**Doc evidence:** "the SSH connection is not subject to the IAM policies"; "username format is `instance-id.port0`"; single shared regional endpoint table. **Severity-if-true:** Critical (cross-account) / High (cross-tenant same-org). **Note:** reaching *proxy-fleet* internals = hard stop.

### Area B — The `Resource:"*"` footgun + AWS-authored sample-policy audit (Lens R / S / U) — **HIGH**
**Background.** Four sample policies ship in `configure-access-to-serial-console`. The docs themselves warn: *"We recommend restricting access to specific EC2 instances. Otherwise, all users with this permission can connect to the serial console of all EC2 instances."* On Windows that is *admin on every instance in the account*.
**Security Concern.** The "explicitly deny" and "allow-all" samples use `Resource:"*"` on `SendSerialConsoleSSHPublicKey`; the ABAC sample keys on a tag-key *value match*. Each is copied verbatim.
**High-level Test Scenarios.**
- Claim: *A principal holding the "allow-all" sample policy gets admin-equivalent serial access to every Windows instance in the account, including ones it should never touch.* → Oracle (safe-first): `iam:SimulatePrincipalPolicy` for `SendSerialConsoleSSHPublicKey` on several instance ARNs under a role holding *only* the sample policy → all Allow. → Severity: **High** (over-broad AWS-published artifact; in scope precisely because it is copy-verbatim).
- Claim (ABAC self-widening, Lens S — **confirmed structural gap**): *The tag-based sample (`aws:ResourceTag/SerialConsole == aws:PrincipalTag/SerialConsole`) is defeated by any principal in its blast radius that also holds `ec2:CreateTags`/`ec2:DeleteTags` on the instance, or any `iam:TagRole`/`iam:TagUser`/`sts:TagSession`-equivalent on itself.* The sample policy grants **neither** CreateTags nor principal-tag management, and the docs **never instruct the reader to separately deny them** — so a real deployment that grants EC2 tag-write elsewhere has a live self-widening path (retag the target instance's `SerialConsole` value to match your principal tag → push now Allows → Windows admin on an instance the author meant to exclude). AWS itself flags this ABAC-tag class as fragile elsewhere ("Do not try to control who can pass a role by tagging the role... This approach does not have reliable results", `access_tags.md`). → Oracle: under a scoped role holding the sample policy **+** `ec2:CreateTags`, retag a same-account instance to the shared value and confirm the push flips from Deny to Allow. → Severity: **Medium–High** (ABAC *is* the access-control mechanism; blast radius = Windows admin).
- Claim (tag case-sensitivity, Lens S): *The condition compares the tag **key** case-insensitively but the **value** with case-sensitive `StringEquals`* (`reference_policies_elements_condition_operators.md`: "Exact matching, case sensitive"). An auto-tagging/CFN/SCP tag-policy path that normalizes value casing differently on the resource side vs the principal side yields either over-restrictive denial or an accidental bypass if some *other* check case-folds. → Oracle: set `SerialConsole=Prod` on the instance vs `prod` on the principal → push denied; probe whether any adjacent workflow case-folds inconsistently. → Severity: Low–Medium.
- Claim (condition-key gap, Lens S — see Area F): *`SendSerialConsoleSSHPublicKey` supports only `aws:ResourceTag`/`ec2:ResourceTag` — no OS-user/platform/port key* — so a policy cannot express "Linux only"/"non-admin only" and an osuser-pattern copy is silently inert. → Oracle: Area F table. → Severity: Informational–Medium (AWS-owned expressiveness gap).
**Doc evidence:** the four JSON samples; "equivalent to granting admin-level privileges." **Severity-if-true:** High.

### Area C — No-auth SAC built-ins as the real privilege boundary (Lens E / U / L) — **HIGH**
**Background.** SAC built-ins run with no Windows sign-in; `restart`, `shutdown`, `crashdump`, `k`, `i`, `l`, `m` are all state-changing. The docs promise *"Further authentication is driven by Windows"* — but that promise only covers the `cmd` channel, not the built-ins.
**Security Concern.** The *documented* mental model ("serial console = you still need Windows creds") is contradicted by the no-auth built-in set. Anyone who clears the serial-console authz gate (see Areas A/B) can reboot, force-crash (DoS + memory dump), kill security processes (`k` on an EDR/AV pid), or rewrite the NIC's IP (`i`) — **without any OS credential**. This is the enforcement-gap (Lens U): the guarantee "authentication is driven by Windows" is only advisory for the built-ins.
**High-level Test Scenarios.**
- Claim: *From a serial session with no OS login, `crashdump` forces a bugcheck → instance DoS and a memory dump that may contain secrets.* → Oracle: instance bugchecks; dump artifact appears. → Severity: **Medium** single-tenant (High if the dump is readable by a less-privileged principal, chains to Area D).
- Claim: *`k <pid>` can terminate a security agent / `i` can rewrite NIC config to break or redirect connectivity, with no OS auth.* → Oracle: targeted process ends / IP changes. → Severity: integrity/availability, Medium–High.
- Claim: *The `lock` command and `cmd` credential gate can be bypassed* (e.g., output-reading restriction, race on channel creation). → Oracle: reading prior channel output or entering a `cmd` channel without creds. → Severity: High if it yields an authenticated shell without creds.
**Doc evidence:** built-in command table; "do not require you to sign in"; `crashdump` "Forces a stop error... generates a memory dump." **Severity-if-true:** Medium–High.

### Area D — Credential / sensitive-boot-output disclosure chain (Lens A / T / O / U) — **MEDIUM–HIGH** *(partly resolved from docs)*
**Background & what the docs resolve.**
- **Password is only ever an *encrypted* blob off-instance.** `GetPasswordData` *"Retrieves the **encrypted** administrator password... encrypted using the key pair you specified when you launched the instance"*; cleartext exists **only client-side** after the operator supplies the `.pem`. So the SAC doc phrase *"emitting the instance password ... over the serial port"* is **ambiguous** (literal password string vs. a readiness/pipeline marker) — the only password-related boot string AWS documents verbatim is the *status* line `Ec2SetPassword: Disabled` and telemetry `AdminPasswordTypeCode=0`, neither a secret. → **DOC-GAP: confirm against a live `get-console-output` whether any password string (cleartext or ciphertext) actually lands on COM1 / in the system log.**
- **RDP certificate thumbprint IS disclosed via the system log.** `connect-rdp.md` tells users to read `RDPCERTIFICATE-THUMBPRINT` from *"Actions → Monitor and troubleshoot → Get system log"* — the **same** action backed by `ec2:GetConsoleOutput`. EC2Launch v2 documents a task *"Send the RDP certificate thumbprint to the Amazon EC2 console."*
- **Doc-vs-doc contradiction (Lens U).** `API_GetConsoleOutput` claims Windows output is only *"the last three system event log errors"* — but the SAC "Known behaviors" section and the RDP page say the *same* system log carries SAC session fragments (`SAC> EVENT: The CMD command is now available.`), boot-menu ANSI, and the RDP thumbprint. The API reference is stale/under-stating the actual content. Worth filing on its own (Informational, AWS-owned) because a customer could build an access-control assumption on the narrower claim.

**Security Concern.** `ec2:GetConsoleOutput` is a **separately-scoped side-channel** (confirmed: supports per-instance ARN + 21 condition keys incl. tags — Area F) to serial-/SAC-adjacent output. A principal locked out of `SendSerialConsoleSSHPublicKey` and `ec2:GetPasswordData` is **not** necessarily denied `GetConsoleOutput`; the docs confirm that path surfaces the RDP thumbprint and SAC fragments. An operator who hardened only the serial action leaves this open.
**High-level Test Scenarios.**
- Claim: *A principal with only `ec2:GetConsoleOutput` reads the RDP cert thumbprint* → combined with a network MITM position, defeats the *only* AWS-prescribed RDP identity check (self-signed cert thumbprint comparison). → Oracle: thumbprint present in console-output body under a role lacking serial/RDP/GetPasswordData. → Severity: **Medium** (MITM enabler; the thumbprint is a verification value, not a secret AWS treats as sensitive — note the doc-gap that AWS nowhere marks it access-restricted).
- Claim: *The system log also carries recoverable credential material (password string) for SAC-enabled instances.* → Oracle: live `get-console-output` sample on a 2026.09.09 default-SAC AMI. → Severity: **High if confirmed cleartext/credential-adjacent**; otherwise N/A. **DOC-GAP — confirm surface first.**
- Chain (Area C → T): SAC `crashdump` writes a **local on-disk** memory dump (`diagnostic-interrupt.md`: *"memory dump data is generated locally by the OS on the instance itself"*) → not exfil'd via serial, but recoverable by a principal with **EBS snapshot / volume-attach / SSM** access but not instance admin (Lens T cross-service reachability) → LSASS/secret recovery. → Oracle: snapshot the volume, mount off-instance, extract the dump. → Severity: **High** if the dump crosses to a lower-privileged principal.
**Doc evidence:** `GetPasswordData` ("encrypted"); `connect-rdp.md` (`RDPCERTIFICATE-THUMBPRINT` via Get system log); SAC "Known behaviors"; `API_GetConsoleOutput` vs SAC/RDP content contradiction; `diagnostic-interrupt.md` (local dump). **Severity-if-true:** Medium–High.

### Area E — Session isolation, replay, and host-key MITM (Lens M / Y) — **MEDIUM–HIGH**
**Background.** One session per instance; 30 s teardown; ephemeral key valid 60 s; session survives IAM-cred expiry; first-connect host-key fingerprint check is the only MITM defense and is user-optional ("(Optional) Verify the fingerprint").
**Security Concern.** (a) The single-session model is a *denial-of-troubleshooting* primitive — a principal who can push a key can camp the only session for ~1 h and block the owner during an incident. (b) Session survives credential revocation — a de-provisioned/expired principal keeps an admin serial session. (c) Skipped fingerprint verification → MITM of the serial stream (which carries password/RDP-thumbprint emission).
**High-level Test Scenarios.**
- Claim: *An attacker with push rights can hold the single session and deny the legitimate operator serial access during an outage.* → Oracle: owner's `SendSerialConsoleSSHPublicKey` fails "session already open." → Severity: Medium (High during incident response).
- Claim: *A session opened before IAM-cred revocation persists afterward with full SAC access.* → Oracle: session still interactive after the principal's creds are invalidated. → Severity: Medium–High (revocation incompleteness, Lens AA).
- Claim: *The host-key fingerprint is region-static and MITM-detectable only if the user checks it; a proxy-impersonation would capture emitted credentials.* → Oracle: documentation confirms optional verification; (live MITM is out of scope / against AWS infra — note, don't execute). → Severity: High-if-exploitable but **against AWS infra = hard stop / report, do not attack**.
**Doc evidence:** "Only 1 active serial console connection"; "connection continues to persist... If your IAM credentials expire"; "(Optional) Verify the fingerprint... someone might be attempting a man-in-the-middle attack." **Severity-if-true:** Medium–High.

### Area F — `ec2-instance-connect` authorization-surface & action-family parity (Lens S / X) — **MEDIUM** *(CONFIRMED from Service Authorization Reference)*
**Background.** `SendSerialConsoleSSHPublicKey` and its sibling `SendSSHPublicKey` both push an SSH key to an `instance`; the serial one bypasses network controls (§2), the other does not. Confirmed condition-key coverage (`list_ec2-instance-connect.md`, `list_ec2.md`):

| Action | Resource-level ARN? | Condition keys |
|---|---|---|
| `SendSerialConsoleSSHPublicKey` | Yes (`instance/${InstanceId}`) | **`aws:ResourceTag`, `ec2:ResourceTag` ONLY** |
| `SendSSHPublicKey` (sibling) | Yes | `aws:ResourceTag`, `ec2:ResourceTag`, **`ec2:osuser`** |
| `OpenTunnel` (EIC endpoint) | Yes (`instance-connect-endpoint`) | tags + `maxTunnelDuration`, `privateIpAddress`, `remotePort` |
| `ec2:EnableSerialConsoleAccess` | **No — account/region only** | `ec2:Region` only |
| `ec2:DisableSerialConsoleAccess` | **No — account/region only** | `ec2:Region` only |
| `ec2:GetSerialConsoleAccessStatus` | **No — account/region only** | `ec2:Region` only |
| `ec2:GetConsoleOutput` | Yes (`instance/${InstanceId}`) | 21 keys incl. `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:InstanceType`, AZ keys |

**Security Concern.** Two confirmed structural gaps:
1. **No OS-user / platform / port / AZ scoping on the serial action.** The highest-blast-radius action (Windows admin-equivalent) has the *thinnest* condition-key surface — only tags. There is **no `ec2:osuser`** (the sibling has it), no Windows-vs-Linux key, and the API's `SerialPort` is hard-pinned to `0` with no key to filter it. An operator who copies the osuser-scoping pattern from standard EC2 Instance Connect onto the serial policy gets **silent no-op enforcement** (Lens S: condition key that is not evaluated for this action).
2. **Account-wide toggle, no resource scoping.** `Enable/Disable/GetSerialConsoleAccessStatus` support only `ec2:Region` — any principal with `ec2:EnableSerialConsoleAccess` flips the master opt-in for *every* instance in the account/region; `ec2:DisableSerialConsoleAccess` is an availability/anti-forensics primitive (disable to deny an incident responder the channel).

**High-level Test Scenarios.**
- Claim: *A policy intending to restrict serial access by OS user (osuser pattern) is inert — the condition is silently ignored and the push succeeds regardless.* → Oracle: `iam:SimulateCustomPolicy` with an `ec2:osuser` condition on `SendSerialConsoleSSHPublicKey` → the condition does not constrain (Allow where a deny was intended).
- Claim: *A single principal with `ec2:EnableSerialConsoleAccess` can re-enable account-wide serial access an org tried to turn off, or `Disable` it to blind responders.* → Oracle: toggle flips `SerialConsoleAccessEnabled` account-wide; no per-instance scoping possible.
**Doc evidence:** `list_ec2-instance-connect.md`, `list_ec2.md` (lines 7848-52, 8113-17, 8252-56, 8534-38); `API_SendSerialConsoleSSHPublicKey.md` (`SerialPort` fixed=0). **Severity-if-true:** Medium (hardening/expressiveness gap, AWS-owned since no key exists to express the docs' own "restrict" advice beyond tags/ARN).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account session via instance-id in username | Serial-console proxy fleet | Instance→account ownership binding (claimed only at IAM push time) |
| Admin on all instances from one over-broad policy | IAM sample policies | "We recommend restricting access to specific EC2 instances" (advisory only) |
| ABAC tag self-widening | Tag-based sample policy | `aws:ResourceTag==aws:PrincipalTag` + (implicit) deny on `ec2:CreateTags` |
| No-auth state change (crashdump/kill/IP-rewrite) | Windows SAC built-ins | "Further authentication is driven by Windows" (covers `cmd` only) |
| Credential/thumbprint read via console output | `ec2:GetConsoleOutput` / system log | Separation of serial-console vs GetConsoleOutput vs GetPasswordData IAM |
| Session persists past cred revocation | Serial console session lifecycle | "connection continues to persist" (documented, not mitigated) |
| Single-session denial-of-troubleshooting | Serial console session model | 1-session-per-instance + 30 s teardown |
| MITM of serial stream carrying credentials | Proxy endpoint host key | Optional fingerprint verification |
| Platform/OS-scoping gap in IAM | `ec2-instance-connect` condition keys | Resource-ARN + tag conditions only |

---

## 7. Out-of-Scope Risk Categories

- **Using your own, properly-authorized serial console / SAC on your own instance** — this is the feature working as designed; instance-admin out-of-band access is the point. Not a finding.
- **Any attack against the AWS serial-console proxy fleet, the EC2 Instance Connect service account, or Nitro control plane** — hard stop; preserve evidence; report to AWS-Security. Do not pursue.
- **Live MITM against the published serial-console endpoints** — AWS infrastructure; out of scope.
- **IMDS on the managed Windows host, Nitro hypervisor isolation** — managed-host internals, out of scope.
- **Customer-authored over-broad IAM policies** — a least-privilege footgun the customer inflicts on themselves (in scope *only* when the weak default ships in the AWS-published sample policies, per Area B).
- **Single-tenant self-DoS** of your own instance (`shutdown` on your own box) — out of scope except where it denies *another* authorized operator (Area E) or crosses tenants.
- **Windows/Microsoft EMS/SAC bugs themselves** — upstream Microsoft, not AWS surface (but AWS's *exposure* of them via serial console is in scope).

---

## 8. Null hypotheses / doc gaps

- **SSRF (Lens G):** N/A — read troubleshoot-windows-sac, configure-access, prerequisites, connect-to-serial-console, ec2launch-v2; no field the service dereferences/fetches on the caller's behalf (serial console pushes a key and opens a byte stream; no URL/location input).
- **Upload / rich-content (Lens Q):** N/A — read the same pages; no file/image/blob upload surface (the SSH *public key* is a key, not parsed content; EC2Launch v2 config files are written by the instance admin, not an external caller).
- **Translation-layer injection (Lens F):** N/A for the serial channel — it is a raw byte stream to COM1; no customer-input→language transform in the AWS layer. (Native-parser memory safety of the proxy's SSH/stream handling is AWS-fleet-internal → hard-stop zone, not for active probing.)
- **Prompt injection / LLM (Lens K):** N/A — no LLM/agent in this pipeline.
- **KMS/attestation (Lens H/W):** N/A — read pages; no customer-KMS or attestation condition in the serial-console path (the admin password is RSA-encrypted to the instance keypair on the normal path — note for Area D, not a KMS-context bug).
- **RESOLVED from docs (no longer gaps):**
  - Condition-key coverage for `ec2-instance-connect:*`, the serial `ec2:*` toggles, and `ec2:GetConsoleOutput` — fully enumerated in **Area F**.
  - Password off-instance is **always encrypted** (RSA to the launch keypair); cleartext only client-side (**Area D**).
  - RDP thumbprint **is** surfaced via the `GetConsoleOutput`/"Get system log" path (**Area D**).
  - `crashdump` memory dump lands as a **local on-instance file**, not via serial (**Area D** chain → needs separate disk/snapshot access).
  - **Lens U doc-vs-doc inconsistency** confirmed: `API_GetConsoleOutput` ("last three system event log errors") contradicts the SAC/RDP docs (thumbprint + SAC fragments in the same log). Informational, AWS-owned, file it.
- **DOC GAPS — confirm surface first (do not rate as null):**
  - *Where exactly instance→account ownership is enforced for the serial SSH session* (IAM push time only, or re-checked in the proxy?) — the docs say the SSH leg is **not** IAM-checked but are silent on the proxy's binding. **This is the Area A pivot; confirm against live before concluding.** Highest-value gap.
  - *Whether any password string (cleartext OR ciphertext) actually appears on COM1 / in the system log* for SAC-enabled instances — the "emitting the instance password" wording is ambiguous; AWS shows no sample log line containing a password. Pull a live `get-console-output` from a 2026.09.09 default-SAC AMI (Area D).
  - *Whether the 60 s ephemeral pubkey is pinned to the pushing principal's network/source* — determines Area A session-relay feasibility.

---

### Kill-chain summary (compose, don't stop at one lens)
`Area B over-broad/ABAC-widened IAM` **→** `SendSerialConsoleSSHPublicKey` on a target instance **→** out-of-band COM1 (bypassing SG/NACL) **→** `SAC>` no-auth built-ins (`crashdump`) **→** memory dump readable off-instance (Area D / Lens T) **→** credential recovery. Rate at the chain **end** (credential compromise / cross-tenant), not the entry point. The cross-account variant (Area A) short-circuits straight to Critical.
