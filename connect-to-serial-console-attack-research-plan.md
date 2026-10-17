# EC2 Serial Console — Attack Research Plan

Source of leads: AWS docs (online + offline mirror `/work/aws-docs/docs/`):
`AWSEC2/latest/UserGuide/connect-to-serial-console.md` (primary target), `ec2-serial-console.md`, `configure-access-to-serial-console.md`, `ec2-serial-console-prerequisites.md`, `disconnect-serial-console-session.md`, `troubleshoot-using-serial-console.md`; IAM reference `service-authorization/latest/reference/list_ec2-instance-connect.md` and `list_ec2.md`; EC2 Instance Connect APIReference (`SendSerialConsoleSSHPublicKey`, `SendSSHPublicKey`).
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP:** the serial-console fleet (`serial-console.ec2-instance-connect.<region>.aws`, `ec2-serial-console.<region>.api.aws`) and the browser proxy fleet (`prod.<region>.oneclickv2-proxy.ec2.aws.dev`) are **AWS service-plane infrastructure**. The moment evidence shows you have reached, enumerated, or obtained an identity/credential/host belonging to that fleet (as opposed to your own instance's serial port), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not pivot within it.
- Two-account test setup is required for every cross-tenant claim (an attacker account + a victim account), plus two instances within one account for intra-account scoping tests.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Cross-tenant serial access:** from account A, obtain a serial-console SSH session to an instance owned by account B (or a second instance in A you were not granted), by exploiting that the SSH leg is "not subject to the IAM policies." → Critical.
2. **Granular-restriction bypass:** obtain a **root** serial login on an instance where the customer intended to restrict OS access (e.g. standard SSH is `ec2:osuser`-pinned to a non-root user, or no OS password was ever set) — proving the serial action is strictly coarser than its siblings. → High.
3. **ABAC / tag self-widen:** gain serial (root-capable) access to an instance by setting a tag (or principal tag) that satisfies the recommended `aws:ResourceTag == aws:PrincipalTag` policy. → High.
4. **Denial-of-recovery:** hold or race the single per-instance serial session so the legitimate operator cannot troubleshoot during an incident. → Medium.
5. **Revocation incompleteness:** keep an active serial session alive after `DisableSerialConsoleAccess`, an IAM policy revoke, or credential expiry. → Medium–High.
6. **Service-plane reach (hard stop):** from inside a serial session or the SSH/WebSocket transport, reach any host other than your own instance's serial port. → Critical + hard stop.

---

## 2. Components, Assets, and Design

**What it is.** Out-of-band access to an EC2 instance's virtual serial port (`ttyS0` Linux / `COM1` Windows), independent of the instance's network. Used to troubleshoot boot/network failures. "The serial console does not require your instance to have any networking capabilities … this connection is outside of the VPC network, [so] EC2 Serial Console does not use the instance security group or the subnet network ACL to authorize traffic to the instance" (`configure-access-to-serial-console.md`).

**Customer-facing interfaces**
- **Control API (SigV4/IAM):** `ec2-instance-connect:SendSerialConsoleSSHPublicKey` — pushes a caller-chosen SSH **public** key to the serial console service, starting a session. Key is valid for **60 seconds**. Params: `InstanceId`, `SerialPort` (0), `SSHPublicKey`, `Region`.
- **SSH data path:** `ssh -i <priv> <instance-id>.port0@serial-console.ec2-instance-connect.<region>.aws`. **Explicitly: "After pushing the SSH key to the instance, the SSH connection is not subject to the IAM policies that you configured."** Username = routing id `instance-id.port0`.
- **Browser client:** WebSocket over **443** to `prod.<region>.oneclickv2-proxy.ec2.aws.dev` (China: `…ec2.a2z.org.cn`). Requires SSM Agent ≥ 3.0.854.0. The console "handles the permissions."
- **Account-level toggle (SigV4/IAM):** `ec2:EnableSerialConsoleAccess`, `ec2:DisableSerialConsoleAccess`, `ec2:GetSerialConsoleAccessStatus` (resource `*`, no resource-level perms). `GetSerialConsoleAccessStatus` returns `SerialConsoleAccessEnabled` and `ManagedBy` ∈ {`account`,`declarative-policy`}.

**Processes / fleets behind it (AWS service account — service plane)**
- Serial console service fleet (region endpoints `serial-console.ec2-instance-connect.<region>.aws` and newer `ec2-serial-console.<region>.api.aws`; GovCloud/China use `.amazonaws.com`/`.amazonwebservices.com.cn`). **Multi-tenant** (one regional fleet fronts every customer's instances; routing is by the `instance-id.port0` username).
- Browser proxy fleet `prod.<region>.oneclickv2-proxy.ec2.aws.dev`.
- Nitro hypervisor virtual serial port; guest OS `getty` on `ttyS0`/`COM1`; GRUB; SysRq (Linux); Special Admin Console/SAC (Windows).

**Accounts / trust zones.** Customer account owns the EC2 instance. The serial console + proxy fleets live in **AWS's service account**. The customer's SSH client / console browser is the caller.

**Identity & gates (there are only three, and network is NOT one of them).**
1. **IAM** on `SendSerialConsoleSSHPublicKey` (push leg only).
2. **OS password** (Linux: a password-based user you set with `passwd`; required to *use*, not to *connect*. Windows: SAC). 
3. **SSH host-key fingerprint** (per-region, published) = the MITM/server-auth anchor.
Network controls (SG, NACL, VPC routing) are **deliberately bypassed**.

**Resource / identifier shapes.** Instance ARN `arn:aws:ec2:<region>:<acct>:instance/i-<17hex>`. The serial routing identifier is the **non-secret** `i-<17hex>.port0`. Session properties: **1 active session per instance**, **60 s** key-validity window, **30 s** teardown, **~1 h** max connection, **persists past IAM credential expiry**.

**Blast radius once connected.** A serial session is keyboard-to-serial-port: boot messages, GRUB menu, SysRq, login prompt. Windows: "Granting serial console permissions is **equivalent to granting admin-level privileges** on the instance." Linux: root password can be set for serial use; GRUB/SysRq are reachable pre-login.

```
                         [ IAM: SendSerialConsoleSSHPublicKey ]   (push leg — checked)
caller (acct A) ── SigV4 ──► Serial Console Service Fleet (AWS service acct, MULTI-TENANT)
                                   │  holds pushed pubkey 60s, keyed on instance-id
   ssh i-....port0@endpoint  ──────┘  (DATA leg — "NOT subject to IAM")   ◄── trust = key possession + instance-id
                                   ▼
                      Nitro virtual serial port ──► guest OS getty (ttyS0/COM1)
                                   ▲                         │
   browser WS:443 ─► oneclickv2-proxy fleet ────────────────┘   GRUB / SysRq / SAC (pre-login)
            (NO SG / NO NACL / outside VPC)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller IAM principal (acct A) | Serial console service, instance ARN | `SendSerialConsoleSSHPublicKey` SigV4 | A key push **succeeds for an instance the principal's IAM does not allow** (incl. another account's instance). |
| SSH client (post-push) | Serial console fleet routing | `ssh <instance-id>.port0@endpoint` — **not IAM-checked** | A session is **established to an instance the key was not pushed for**, or to another tenant's instance → cross-tenant. |
| Serial console fleet (AWS svc acct, multi-tenant) | A specific customer instance serial port | Fleet routes by username id | Reaching **another customer's instance or session** on the shared fleet. |
| Out-of-band serial connection | Instance network controls (SG/NACL/VPC) | By design bypassed | The only remaining gates are IAM + OS password; **network isolation cannot contain serial access** (documented, by design — frames all other leads). |
| Caller with serial access | Instance OS privilege | GRUB / SysRq / SAC pre-login | Obtaining a **root/SYSTEM shell without the OS password** (GRUB `init=/bin/bash`, single-user). |
| IAM principal w/ `ec2:CreateTags` + ABAC policy | Instance serial (root) | Tag the instance to satisfy `ResourceTag==PrincipalTag` | Serial access gained **by self-tagging**, not by a grant on the instance. |
| Account/declarative-policy setting | Serial access state | `Enable/DisableSerialConsoleAccess`, SCP, declarative policy | A push **succeeds while account access is Disabled** (fail-open), or an active session **survives a Disable/revoke**. |
| Any serial/SSH/WS transport | AWS service-plane fleet | pivot from session or transport | **Any host other than your own instance's serial port** → **HARD STOP**. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | API/CLI (SigV4) | Existing | **Mutating** (opens session) | External | Push 60-s pubkey → start serial session | Yes | IAM principals w/ the action on the instance ARN | **Only condition keys: `aws:ResourceTag`/`ec2:ResourceTag`.** No `ec2:osuser`, no port/IP/duration keys. Resource type: `instance*`. |
| `ec2-instance-connect:SendSSHPublicKey` (**sibling**) | API/CLI | Existing | Mutating | External | Push 60-s pubkey for **standard** SSH | Yes | IAM principals | **Supports `ec2:osuser`** condition — the serial twin does NOT. Parity-divergence lead (Lens X). |
| SSH to `…port0@serial-console…<region>.aws` | SSH (22) | Existing | Mutating | External | Serial data session | Yes | **Anyone with the private key + instance-id — NOT IAM-checked** | Core cross-tenant surface. Username = routing id. |
| Browser WebSocket → `oneclickv2-proxy` | WS/443 | Existing | Mutating | External→svc fleet | Browser serial terminal | Yes (TLS) | Console session; "handles the permissions" | Identity-assertion from console→proxy is doc-thin (Lens CC — doc-gap). |
| `ec2:EnableSerialConsoleAccess` | API/CLI | Existing | **Mutating** | External | Turn on account-wide serial access | Yes | IAM principals (resource `*`) | Opens the out-of-band door account-wide; no resource scoping possible. |
| `ec2:DisableSerialConsoleAccess` | API/CLI | Existing | Mutating | External | Turn off account-wide access | Yes | IAM principals (`*`) | Revocation-completeness question (Lens AA). |
| `ec2:GetSerialConsoleAccessStatus` | API/CLI | Existing | Non-mutating | External | Read access state + `ManagedBy` | Yes | IAM principals (`*`) | No resource-level perms. |

**Hidden/undocumented-knob sweep:** `SerialPort` is documented with a **valid range locked to `0`** — confirm whether the control plane/SDK silently accepts other values and what they route to (a non-0 port reaching a different serial device would be a hidden knob). `InstanceOSUser`/`AvailabilityZone` exist on `SendSSHPublicKey` but **are absent from the serial API model** — verify the serial endpoint rejects (not silently ignores) an injected `InstanceOSUser`. Full request/error model folded into Section 9.

---

## 5. Recommended Areas of Focus (priority order; one block per firing lens)

### Area 1 — SSH data-leg authorization binding (Lens A / M) — **TOP PRIORITY**
**Background.** The push leg is IAM-gated per instance ARN, but the docs state plainly: *"After pushing the SSH key to the instance, the SSH connection is not subject to the IAM policies that you configured to grant users EC2 Serial Console access."* The multi-tenant fleet routes the SSH session by the **non-secret** username `i-<17hex>.port0`.
**Security Concern.** The security of the data leg therefore rests entirely on the fleet binding the pushed public key to **exactly** the instance it was authorized for, for that one session. If the binding is by instance-id-in-username rather than by the (key, authorized-instance) tuple, a caller could push a key against instance A (which they own) and then open an SSH session naming instance B's id.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* With a key pushed for owned instance A, `ssh i-<B>.port0@endpoint -i privA` establishes a session to **instance B** (second instance same account, then cross-account). → **Confirm/Refute:** a login/boot prompt from B. *(If the fleet rejects because the key is bound to A, the claim is refuted — a genuine null.)*
- *Claim:* Two keys can be registered in the 60-s window such that a second caller races onto the single session. → observe session hijack/interception.
- *Claim:* `SendSerialConsoleSSHPublicKey` against another account's instance id returns success (not `AccessDenied`/`NotFound`) — a push-leg IDOR even before SSH.
- *Claim (push-leg enumeration):* varying `InstanceId` (hex, enumerable) distinguishes `EC2InstanceNotFoundException` vs `AuthException` vs `EC2InstanceStateInvalidException` vs `SerialConsoleSessionLimitExceededException` — building a cross-account existence/power-state/live-session map **without `ec2:DescribeInstances`** (see Section 9 oracle table). `SerialConsoleSessionLimitExceeded` additionally reveals when an operator is actively on the console (attack-timing signal).
**Doc evidence.** `connect-to-serial-console.md` (SSH section); `list_ec2-instance-connect.md` (instance ARN resource, ResourceTag only). **Severity-if-true:** cross-account = **Critical** (hard stop if it reaches another tenant); intra-account = High.
**Stop condition.** A single confirmed cross-tenant session; preserve evidence, do not enumerate further instances.

### Area 2 — Condition-key / OS-user restriction asymmetry with the standard-SSH sibling (Lens X / U) — **strongest doc-provable lead**
**Background.** `SendSSHPublicKey` (standard EC2 Instance Connect) supports the **`ec2:osuser`** condition key — a customer can pin SSH to e.g. `ec2-user`. Its twin `SendSerialConsoleSSHPublicKey` supports **only** `aws:ResourceTag`/`ec2:ResourceTag` (verified in `list_ec2-instance-connect.md`). The serial login prompt accepts **any** OS username, including `root`.
**Security Concern.** A customer who believes they have constrained interactive OS access by osuser-pinning standard SSH has **no equivalent lever for the serial path** — the serial twin is strictly coarser and routes around the restriction. Granting `SendSerialConsoleSSHPublicKey` on an instance is effectively "may attempt login as any OS user, including root."
**High-level Test Scenarios:**
- *Claim:* On an instance where `SendSSHPublicKey` is restricted to `ec2:osuser = ec2-user`, a principal granted `SendSerialConsoleSSHPublicKey` reaches a **root** login prompt via serial. → **Refute** only if some serial-side osuser control exists (none documented).
- *Claim:* No IAM condition key exists to restrict the serial OS user, port, or session duration (contrast OpenTunnel's `maxTunnelDuration`/`remotePort`/`privateIpAddress`). → confirm by exhaustive condition-key enumeration in the service-authorization reference.
**Doc evidence.** `list_ec2-instance-connect.md` action rows (osuser on `SendSSHPublicKey` only); `configure-access-to-serial-console.md` ("set the password for any OS user, including the root user"; Windows = admin-equivalent). **Severity-if-true:** High (OS-access-restriction bypass, documented asymmetry). Pure doc-vs-capability portions = Low/Informational but AWS-owned.

### Area 3 — ABAC tag self-widen + CreateTags privilege escalation (Lens I / S / R)
**Background.** AWS's recommended granular policy is ABAC: `"aws:ResourceTag/SerialConsole": "${aws:PrincipalTag/SerialConsole}"` over `instance/*`.
**Security Concern.** The condition binds **tag-value equality**, not ownership. If the principal can set the instance tag (`ec2:CreateTags`) or influence its own `aws:PrincipalTag`, it can manufacture a match and grant itself serial (root-capable) access to instances it was never meant to reach.
**High-level Test Scenarios:**
- *Claim:* A principal holding the ABAC serial policy **plus** `ec2:CreateTags` tags a target instance `SerialConsole=<its principal-tag value>` and then successfully pushes a serial key. → session on a non-granted instance. **Oracle:** prove the push is denied **before** tagging and allowed **after**, under a scoped role.
- *Claim:* The principal can set/modify its own `SerialConsole` principal tag (session tag via AssumeRole `Tags`, or `TagRole`/`TagUser`) to match a target instance's existing tag. → same escalation from the principal side.
- *Claim (Lens S):* The ABAC policy over `instance/*` has no second statement re-checking ownership; a broad `*` grant elsewhere silently overrides it.
**Doc evidence.** `configure-access-to-serial-console.md` ABAC sample. **Severity-if-true:** High (self-service to root on tagged instances). Note: when the customer authored the policy it's a least-priv footgun, **but the sample is AWS-published guidance** — flag the missing "cannot self-tag" caveat (Tier-2, routed `aws-security`).

### Area 4 — IAM-to-root reachability via GRUB/SysRq pre-login (Lens E / U)
**Background.** To *use* the serial console for Linux troubleshooting the docs say you need a password-based OS user, "However, to monitor the logs, you don't need a password-based user." The prerequisites configure **GRUB** (`GRUB_TERMINAL="console serial"`) and **SysRq** on the serial port.
**Security Concern.** GRUB and SysRq are reachable **before** the OS login prompt. A caller with serial access can interrupt GRUB and boot `init=/bin/bash` / single-user → root shell **without any OS password**. Thus the IAM permission `SendSerialConsoleSSHPublicKey` on an instance ≈ root on that instance regardless of whether a password was ever set — contradicting the implied "OS password is a second gate."
**High-level Test Scenarios:**
- *Claim:* From a serial session on an instance with **no** OS password set, editing the GRUB entry yields a root shell. → root prompt.
- *Claim:* SysRq over serial (`sysctl kernel.sysrq=1` is a documented prereq) permits reboot/SAK/kill from serial without authentication.
- *Claim (Windows):* Serial permission alone yields SAC admin actions ("equivalent to admin-level privileges").
**Doc evidence.** `ec2-serial-console-prerequisites.md` (GRUB/SysRq config), `configure-access-to-serial-console.md` (OS-level access, Windows admin-equivalence). **Severity-if-true:** High within the customer account (coarse IAM grant → root). Largely documented/by-design — frame as "the OS password is not an authorization boundary against serial access."

### Area 5 — Revocation completeness & session survival (Lens AA)
**Background.** The docs state the serial connection **outlives IAM credential expiry**: *"If your IAM credentials expire, the connection continues to persist until the maximum duration of the serial console connection is reached."* Max ~1 h; 30-s teardown.
**Security Concern.** If the session survives credential expiry, does it also survive an explicit **`DisableSerialConsoleAccess`**, an IAM **Deny** policy added mid-session, an **instance stop**, or a declarative-policy flip? A revoked/off-boarded operator (or attacker whose access was cut) could retain a live root channel for up to an hour.
**High-level Test Scenarios:**
- *Claim:* An active serial session persists after `DisableSerialConsoleAccess` is called account-wide. → session still interactive.
- *Claim:* Adding an explicit Deny on `SendSerialConsoleSSHPublicKey` mid-session does not terminate the existing session.
- *Claim:* A declarative-policy-managed account ("you can't modify directly") can still be overridden via the account-level API, or vice-versa — mismatch between `ManagedBy` and effective state.
**Doc evidence.** `connect-to-serial-console.md` considerations; `configure-access-to-serial-console.md` (ManagedBy, declarative policy). **Severity-if-true:** Medium–High (stale privileged access window).

### Area 6 — Single-session denial-of-recovery / shared-fleet DoS (Lens L)
**Background.** "Only 1 active serial console connection is supported per instance"; "60 seconds before [the key] is removed"; "30 seconds to tear down a session." Error surface includes a session-limit-exceeded condition.
**Security Concern.** During an incident the serial console is the recovery channel. A principal with serial access (or an attacker, if Area 1 breaks) can **hold or repeatedly re-grab the single session**, denying the real operator any serial recovery path — an availability attack precisely when the instance is already unhealthy. Also test whether unfinished/half-open pushes leak session slots on the shared fleet (noisy-neighbor).
**High-level Test Scenarios:**
- *Claim:* A loop of `SendSerialConsoleSSHPublicKey` + idle SSH keeps the session continuously occupied, so the owner always gets `SerialConsoleSessionLimitExceeded`.
- *Claim:* Rapid connect/disconnect churn against the 30-s teardown window causes session-slot starvation.
**Doc evidence.** `connect-to-serial-console.md`, `disconnect-serial-console-session.md`. **Severity-if-true:** Medium (single-tenant denial-of-recovery); High only if one tenant degrades the shared fleet for others.

### Area 7 — Out-of-band reach / service-plane pivot (Lens D / V) — **hard-stop zone**
**Background.** The connection is "outside of the VPC network" and transits the AWS-managed serial/proxy fleets.
**Security Concern.** (a) From inside a serial session (root shell), can the customer reach the serial-console fleet or Nitro controller via the serial channel (a back-channel to the service plane)? (b) Does the serial port expose anything beyond the guest's own `ttyS0`/`COM1` — e.g. another instance co-resident on the host, the control plane? (c) Does the `oneclickv2-proxy` leak internal routing/identity?
**High-level Test Scenarios:**
- *Claim:* The serial channel reaches a host other than this instance's serial port. → **HARD STOP on any hit.**
- *Claim:* The proxy/fleet reflects internal identifiers or accepts a spoofed instance-id in the WS handshake.
**Doc evidence.** `configure-access-to-serial-console.md` (out-of-band design). **Severity-if-true:** Critical + hard stop (service-plane). Treat with extreme care; this is AWS infrastructure.

### Area 8 — Transport / host-key MITM (Lens Y / M)
**Background.** Server auth = per-region SSH **fingerprint** (published table); endpoints use non-standard TLDs `.aws` / `.api.aws`; browser uses WS/443 TLS. The docs explicitly warn: "If these fingerprints don't match, someone might be attempting a man-in-the-middle attack." Fingerprint "only appears the first time you connect."
**Security Concern.** TOFU (trust-on-first-use) on an unusual TLD invites a MITM against operators who skip verification; a stale/rotated fingerprint, or divergence between the two endpoint families (`serial-console.ec2-instance-connect…` vs `ec2-serial-console….api.aws`), could cause silent acceptance.
**High-level Test Scenarios:**
- *Claim:* The two endpoint families for one region present **different** host keys / the published fingerprint is stale → verification ambiguity.
- *Claim:* The browser client does not pin/verify an equivalent server identity, enabling a WS MITM where a network-position attacker sits between browser and `oneclickv2-proxy`.
**Doc evidence.** `connect-to-serial-console.md` fingerprint table + MITM note; `ec2-serial-console-prerequisites.md` (proxy endpoint). **Severity-if-true:** High (MITM of a root channel) — but requires network position; largely a doc/hardening observation.

### Area 9 — Account-setting fail-open & audit gaps (Lens P / O)
**Background.** "By default, there is no access … you need to explicitly grant access at the account level." Error `SerialConsoleAccessDisabledException` suggests fail-closed.
**Security Concern.** Confirm the push **fails closed** when account access is Disabled (not merely UI-hidden). Separately: the **SSH data leg is not IAM-checked** → is the actual session (who connected, when, for how long, what OS user) recorded anywhere in CloudTrail, or only the push? An attacker who obtains a session leaves only the push event; serial keystrokes are unlogged by AWS.
**High-level Test Scenarios:**
- *Claim:* `SendSerialConsoleSSHPublicKey` succeeds while `GetSerialConsoleAccessStatus=false` (fail-open). → refute expected.
- *Claim:* No CloudTrail/management event records the SSH session establishment or OS-user login; only the push is logged → audit blind spot for post-push activity.
**Doc evidence.** `configure-access-to-serial-console.md` (account gate); `connect-to-serial-console.md` (SSH not IAM-checked). **Severity-if-true:** fail-open = High; audit gap = Low/Informational (enabler).

### Area 10 — Dual endpoint-namespace parity (Lens N)
**Background.** Two live endpoint families per feature: legacy `serial-console.ec2-instance-connect.<region>.aws` and newer `ec2-serial-console.<region>.api.aws` (plus partition-specific `.amazonaws.com`/`.amazonwebservices.com.cn`).
**Security Concern.** Do both endpoint families enforce the **same** host-key, the same push-binding, and the same regional access gate? A parity gap between namespaces is a classic migration-window bypass.
**High-level Test Scenarios:** *Claim:* a session refused on one endpoint family succeeds on the other for the same instance/key. **Doc evidence.** endpoint table. **Severity-if-true:** High if it bypasses an otherwise-enforced control; else Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant serial session via unbound key / guessable `instance-id.port0` | Serial console fleet (SSH leg) | "SSH connection is not subject to the IAM policies" — binding to authorized instance is the sole control |
| Root serial login where OS access was meant to be constrained | `SendSerialConsoleSSHPublicKey` vs `SendSSHPublicKey` | `ec2:osuser` exists only on the standard-SSH twin |
| Self-grant via tagging | ABAC sample policy | `ResourceTag == PrincipalTag` equality (no ownership/self-tag guard) |
| OS-password bypass to root | GRUB / SysRq prereqs | "password-based user" implied as a gate (bypassed pre-login) |
| Stale session after revoke/disable | Account toggle + session lifecycle | "connection persists until max duration" even after creds expire |
| Denial-of-recovery | 1-session-per-instance limit | single-session + 30-s teardown |
| Service-plane pivot | serial/proxy fleets | out-of-band, AWS-managed (shared-responsibility line) |
| MITM of serial channel | SSH fingerprint / WS TLS | published per-region fingerprint + first-use verification |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- The AWS-managed serial-console and `oneclickv2-proxy` **fleets themselves** — do not pentest AWS infrastructure; any reach into them is a **hard-stop disclosure**, not an exploit to develop.
- **IMDS** on the managed hosts / Nitro internals.
- A customer **steering their own instance** (serial access to an instance you legitimately own at root is the feature working as designed — not a finding).
- **Customer-authored** over-broad IAM (e.g. granting `SendSerialConsoleSSHPublicKey` on `*`) is a customer least-privilege footgun — **except** where AWS's own sample/guidance omits a necessary caveat (Area 3), which is in-scope Tier-2.
- Guest-OS vulnerabilities / weak customer OS passwords (customer responsibility) — except the GRUB/SysRq pre-login bypass framing (Area 4), which is a documentation/design observation.
- DNS rebinding against private-only endpoints; feature-parity gaps.

---

## 8. Null Hypotheses / Doc Gaps (pages checked named)
- **Lens G (SSRF): N/A** — checked `connect-to-serial-console`, `configure-access-to-serial-console`, `ec2-serial-console-prerequisites`, `disconnect`, `troubleshoot`. No field the service dereferences/fetches (the SSH public key is consumed locally, not fetched from a URL). Closed.
- **Lens H (KMS/encryption-context): N/A** — feature is at no cost, no CMK, no encryption-context in any page. Closed.
- **Lens J (OAuth/3P): N/A** — no third-party identity linking in any serial-console page. Closed.
- **Lens K (prompt injection): N/A** — no LLM/agent in the pipeline. Closed.
- **Lens T (secret reachability): N/A** — the pushed key is ephemeral (60 s) and not persisted to SSM/Secrets Manager/S3; OS password lives only in the guest. Closed.
- **Lens FF (JWT/OIDC): N/A** — no bearer-token validation documented. Closed.
- **Lens DD (cache): N/A** — no caching layer documented. Closed.
- **Lens EE (predictable-name land-grab): N/A** — endpoint hostnames are predictable but AWS-owned; no customer-resolvable global namespace. Closed.
- **Lens CC (trusted-upstream-context): DOC-GAP** — the browser console "handles the permissions" and the `oneclickv2-proxy` sits between console and fleet; how identity is asserted from console→proxy is **not documented**. Confirm the proxy handshake surface before ruling in/out.
- **Lens B/C (PassRole/vending): N/A for customer input** — no role-ARN parameter; the fleet-to-instance leg uses an internal AWS identity (service plane — out of scope / hard stop). Closed on the customer side.
- **Lens F (parser memory-safety): OPEN-LOW** — the fleet parses the SSH public-key blob, the `instance-id.port0` username, and `SerialPort`; malformed/oversized key or crafted username/port is worth a fuzz pass, but the component is AWS-managed (careful — hard-stop zone). Note, do not develop.

---

## 9. Integrated API error-oracle & blast-radius notes (from API-reference + architecture deep-dives)

**Request model (confirms the surface is minimal and the id is enumerable).**
- `SendSerialConsoleSSHPublicKey`: `InstanceId` (required, `^i-[a-f0-9]+$`, len 10–32), `SSHPublicKey` (required, len 80–4096), `SerialPort` (optional, **locked to 0**). **No `InstanceOSUser`, no `AvailabilityZone`.** Response `{RequestId, Success}`.
- `SendSSHPublicKey` (sibling): adds **required `InstanceOSUser`** (`^[A-Za-z_]...`) and optional `AvailabilityZone`. The serial twin has no OS-user concept at all — reinforcing Area 2 (you cannot scope the serial OS user because the API has no field and no `ec2:osuser` key for it).
- Instance id is hex, non-secret, and only syntactically checked — guessable/enumerable space (Area 1 precondition).

**Error-oracle inventory (sharpens Area 1 enumeration and Area 9 fail-open/audit).** These are `SendSerialConsoleSSHPublicKey`-specific unless noted; each is a documented, client-distinguishable signal:
| Error | HTTP | Oracle it provides |
|---|---|---|
| `AuthException` | 400 | **Merges** bad-credentials AND not-authorized-for-instance into one message (does *not* itself reveal existence). |
| `EC2InstanceNotFoundException` | 400 | **Existence oracle** — distinct from `AuthException`, so varying `InstanceId` reveals which ids exist vs not, independent of usability. |
| `EC2InstanceStateInvalidException` | 400 | **Power-state oracle** — "exists but stopped/terminated" vs "not found," without `ec2:DescribeInstances`. |
| `EC2InstanceTypeInvalidException` | 400 | **Instance-type oracle** — leaks Nitro vs non-Nitro (serial-only). |
| `SerialConsoleSessionLimitExceededException` | 400 | **Live-session/timing oracle** — proves a session is *active right now* (infer admin activity; time an attack). Serial-only. |
| `SerialConsoleAccessDisabledException` | 400 | **Account/region feature-flag oracle** — decoupled from any instance; confirms whether serial is enabled account-wide. Serial-only. |
| `SerialConsoleSessionUnavailableException` | **500** | backend session-establishment failure (distinct status from the 400 validation set). |
| `AccessDeniedException` (common) | 403 | IAM-layer deny — **different status from the 400 `AuthException`**; test which layer fires first (resource/SCP vs IAM vs service authz) — a layer-ordering oracle. |

Research note: a malformed id (`InvalidArgsException`/`ValidationError`) vs a well-formed-nonexistent id (`EC2InstanceNotFoundException`) is itself a distinguishing oracle. Feed this table into Area 1 (push-leg IDOR/enumeration) and the fail-open test in Area 9.

**Blast-radius refinements.**
- **GRUB nuance (revises Area 4):** AWS's own single-user/emergency-mode walkthrough (`troubleshoot-using-serial-console.md`) shows the OS **still prompting for a password** at the `login`/`Password` step on the systemd distros it documents — so single-user mode does *not* trivially bypass the password there. The real root-bypass hypothesis is **GRUB kernel-command-line editing** (`init=/bin/bash`, `rd.break`, `single` on distros that don't prompt), which varies by distro/init and must be verified per-AMI — **contrast documented behavior against the actual distro default**, don't assume.
- **SysRq (no-auth, pre-login):** reachable with **no authentication** once a session exists — `b`(reboot), `c`(crash), `o`(poweroff), `e`/`i`(kill tasks), `k`(SAK). So even without an OS password, serial access ⇒ **unauthenticated crash/reboot/panic DoS** of the instance (feeds Area 4 + Area 6).
- **Windows SAC (no-auth built-ins):** `restart`, `shutdown`, `crashdump` (forced BSOD), `k`(kill pid), and **network-interface reconfig** (`i <#> <ip> <subnet> <gateway>`) run **without sign-in**; only the `cmd`/`powershell` channel needs admin creds. So serial access to Windows ⇒ unauthenticated reboot/BSOD/network-break even before the "admin-equivalent" credentialed shell.
- **No documented tenant-isolation guarantee** exists for the serial/proxy fleet beyond "outside the VPC" — the only disclosed controls are the IAM action gate, the OS password, and the human TOFU fingerprint check. That absence is itself why Area 1 and Area 7 are the priority.
- **Fingerprint TOFU (Area 8):** purely manual trust-on-first-use, shown only on first connect, over unusual `.aws`/`.api.aws` TLDs, with **no documented SSHFP/known_hosts/pinning** mechanism — a clean MITM window for operators who skip the check.
