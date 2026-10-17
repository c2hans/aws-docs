# EC2 Serial Console (EC2 Instance Connect `SendSerialConsoleSSHPublicKey`) — Attack Research Plan

Source of leads (documentation-derived only; nothing tested against a live account):
- Target page: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disconnect-serial-console-session.html (`.md` mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/disconnect-serial-console-session.md`) — thin page; it anchors the broader EC2 Serial Console feature analyzed below.
- `ec2-serial-console.md`, `configure-access-to-serial-console.md`, `connect-to-serial-console.md`, `ec2-serial-console-prerequisites.md`, `troubleshoot-using-serial-console.md` (all under `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`).
- API reference: `ec2-instance-connect/latest/APIReference/API_SendSerialConsoleSSHPublicKey.html` (and `API_SendSSHPublicKey`).
- IAM reference: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2-instance-connect.md` (service prefix `ec2-instance-connect`); account-level actions in `list_ec2.md` (`ec2:EnableSerialConsoleAccess`, `ec2:DisableSerialConsoleAccess`, `ec2:GetSerialConsoleAccessStatus`).

> **Note for the downstream hunter:** This feature is a rare "AWS service plane reaches directly into the customer OS kernel, out-of-band of the VPC" surface. Many of the most interesting leads below land on, or adjacent to, **AWS's own serial-console service fleet** (`*.ec2-instance-connect.<region>.aws`, `*.oneclickv2-proxy.ec2.aws.dev`). Per the hard-stop rule, the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, **stop, preserve evidence, flag for AWS-Security disclosure** — do not keep pulling.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs the plan did not anticipate.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the serial-console proxy fleet, its fetch identity, a cross-customer serial stream), stop, preserve evidence, flag for AWS-Security disclosure. Confirm existence, never exploit beyond it.
- Dummy/canary data only. One serial console session per instance; the push creates a 60-second connect window and a 30-second teardown — respect these as rate limits, not things to hammer.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. **Cross-account / cross-tenant serial reach** — from account A, push a key to or open a serial console session on an instance owned by account B (or read account B's serial stream through the shared AWS serial-console fleet). *Critical.*
2. **IAM-gate bypass on the push** — invoke `SendSerialConsoleSSHPublicKey` against an instance the caller's IAM policy (instance-ID or tag scoped) was written to deny — via tag race, ARN/ID canonicalization, or a validator that checks existence but not the scoped condition. *High.*
3. **Post-push connection hijack** — exploit the documented fact that "the SSH connection is **not subject to the IAM policies**" once the key is pushed: a party other than the pusher (same key, or a co-resident process, or a racing connector) establishes/steals the 60-second serial session. *High.*
4. **OS-auth bypass via the serial channel** — reach root/admin on the guest without the OS password the docs require, via GRUB single-user/emergency mode, SysRq, or Windows SAC. *High (customer-impact), but see scope caveat.*
5. **Network-control evasion** — use the serial console's documented bypass of Security Groups and NACLs to reach an instance an org believed was network-isolated. *Medium–High.*
6. **Account-setting / governance bypass** — flip or misreport the account-level serial-console enablement (`Enable/Disable/GetSerialConsoleAccessStatus`, `ManagedBy` declarative-policy vs account). *Medium.*
7. **Service-plane escape** — any packet, credential, or identity reachable **from** the serial channel or the push path that belongs to AWS's serial-console fleet. *Critical + hard stop.*

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- **Control API (SigV4, Internet-facing):** `ec2-instance-connect:SendSerialConsoleSSHPublicKey` — JSON body `{InstanceId, SerialPort, SSHPublicKey}`. `InstanceId` pattern `^i-[a-f0-9]+$` (len 10–32); `SerialPort` fixed `0`; `SSHPublicKey` len 80–4096. Returns `{RequestId, Success}`. Pushes a caller-supplied SSH **public** key that lives **60 seconds** on the serial-console service.
- **SSH data path (Internet-facing, AWS service fleet):** `ssh -i <priv> i-<id>.port0@serial-console.ec2-instance-connect.<region>.aws` (newer regions: `ec2-serial-console.<region>.api.aws`; China: `*.api.amazonwebservices.com.cn`; GovCloud: `*.amazonaws.com`). Username shape is **deterministic**: `<instance-id>.port0`. First-connect prompts a **per-region host fingerprint** (MITM warning in docs).
- **Browser client (WebSocket, port 443):** EC2 console → `prod.<region>.oneclickv2-proxy.ec2.aws.dev` (China `…ec2.a2z.org.cn`). "The browser-based client handles the permissions."
- **Account-level control:** `ec2:EnableSerialConsoleAccess` / `DisableSerialConsoleAccess` / `GetSerialConsoleAccessStatus` (all `Resource:"*"`, no resource-level perms). Status carries `ManagedBy` = `account` | `declarative-policy`.

**Processes / fleets behind the interface**
- An **AWS-owned, multi-tenant serial-console service fleet** (the `*.ec2-instance-connect.<region>.aws` endpoint and the `oneclickv2-proxy` fleet) that terminates the customer SSH/WebSocket and bridges to the instance's **virtual serial port** via the Nitro hypervisor. This fleet is the trust anchor and the highest-value finding zone.
- The **Nitro hypervisor / instance serial port** (`ttyS0` Linux / `COM1` Windows, "port 0"). Only Nitro-based and most bare-metal instances are supported.
- The **guest OS** getty/login, GRUB bootloader, kernel SysRq handler (Linux); SAC (Windows).

**Accounts / VPCs / network**
- The serial connection is **explicitly outside the instance VPC**: *"this connection is independent of the instance VPC… Because this connection is outside of the VPC network, EC2 Serial Console does not use the instance security group or the subnet network ACL to authorize traffic to the instance."* → The only access controls are (a) the account-level enablement, (b) IAM on the push action, and (c) the guest OS password. SG/NACL/VPC isolation **do not apply** — a deliberate design inversion worth centering the threat model on.

**What is a "resource" and its identifier shape**
- Resource = the EC2 **instance** (`arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`). The push action's only resource type is `instance*`.
- The **serial session identifier** is implicit: username `i-<id>.port0`. The instance-ID is low-entropy/discoverable, the port is fixed. There is **no session token** in the documented connect flow — the 60-second pushed public key *is* the bearer, and possession of the matching private key is the only connect-time secret.

**Identity / credential model**
- Push: SigV4 IAM. **Connect: not IAM** — docs state the SSH connection "is not subject to the IAM policies that you configured." 
- **Credential/session decoupling:** *"The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist until the maximum duration (1 hour)."* Session also **survives instance reboot and stop**.
- OS layer: a **password-based OS user** is required to *use* a Linux serial console for troubleshooting, but *not* to connect; on Windows "granting serial console permissions is **equivalent to granting admin-level privileges** on the instance."

**Roles / privilege levels**
- IAM principals scoped by instance-ARN or `aws:ResourceTag`/`ec2:ResourceTag` (ABAC). Notably **no `ec2:osuser` condition key** exists for `SendSerialConsoleSSHPublicKey` (it exists for `SendSSHPublicKey`) — so the serial push cannot be constrained to a specific OS user via IAM.

**ASCII pipeline**
```
 Caller (SigV4)                                    AWS Serial-Console Service Fleet            Nitro host / guest
 ─────────────                                     ─────────────────────────────              ─────────────────
 SendSerialConsoleSSHPublicKey ───IAM authz───►  [push store: pubkey, TTL=60s] ──────────►  virtual serial port (ttyS0/COM1)
   {InstanceId, SerialPort=0, SSHPublicKey}                     │                                     │
                                                                │  (SG/NACL/VPC NOT consulted)        │
 ssh i-<id>.port0@serial-console.<region>.aws ──NO IAM here──►  [SSH term + fingerprint] ───bridge──► getty/login │ GRUB │ SysRq │ SAC
 browser WS :443 → oneclickv2-proxy.<region> ──"handles perms"─►      │                                     │
                                                                 session: 1/instance, 1h, survives reboot/stop, 30s teardown
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal in account A | EC2 instance in account B | `SendSerialConsoleSSHPublicKey` with foreign `InstanceId` | Push returns `Success:true` (not `AuthException`/`EC2InstanceNotFound`) for an instance the account does not own → cross-account serial push = **Critical** |
| IAM principal (instance/tag-scoped) | Instance outside the scope | push action with crafted ID/tag/ARN | A push the policy was written to deny succeeds (tag race, casing, ID normalization) → **High** |
| Pusher's identity/source | The live 60-second serial session | SSH with the pushed key; "connection **not subject to IAM**" | A party other than the authorized pusher (different source IP, co-resident host, racing connector) establishes/takes the session → **High** |
| Customer network vantage (Internet) | Instance with restrictive SG/NACL / no public IP | serial path bypasses SG/NACL/VPC | Serial session reaches an instance that SG/NACL would block on every normal port → **Medium–High** (documented-but-surprising) |
| Any caller | AWS serial-console service fleet | SSH term / WebSocket proxy / serial bridge | Any response, credential, ARN, or cross-customer serial byte originating from AWS's fleet identity → **Critical + HARD STOP** |
| Serial connector (unauth at OS) | guest root/admin | GRUB single-user/emergency, SysRq, SAC | Root/SYSTEM shell reached without the OS password the docs require → **High** (customer-owned guest; see scope) |
| Principal with account-setting perms | Org governance of serial access | `Enable/Disable/GetSerialConsoleAccessStatus`, declarative policy | Enablement flipped against org intent, or status misreports `ManagedBy` so a declarative deny appears locally mutable → **Medium** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | API (SigV4) | Existing | **Mutating** (pushes key, opens session slot) | External | Push 60s pubkey → open serial session | **Yes** | IAM principals with the action on the instance ARN / matching tag | Resource `instance*`; cond keys **only** `aws:ResourceTag`,`ec2:ResourceTag`; **no `ec2:osuser`**; errors distinguish NotFound / Auth / StateInvalid / TypeInvalid / **SessionLimitExceeded** / Disabled |
| `ec2-instance-connect:SendSSHPublicKey` | API (SigV4) | Existing | Mutating | External | Push 60s pubkey for **standard** SSH | Yes | IAM; supports `ec2:osuser` | Sibling/"twin" of the serial action — compare authz parity (Lens X) |
| Serial SSH endpoint `i-<id>.port0@serial-console.<region>.aws` | SSH | Existing | Mutating (consumes session) | **External, AWS fleet** | Establish serial session with pushed key | **Yes** | **Anyone with the private key reaching the endpoint — NOT IAM-gated** | Deterministic username; per-region fingerprint; port 0 only |
| Browser WebSocket → `prod.<region>.oneclickv2-proxy.ec2.aws.dev:443` | WS | Existing | Mutating | External, AWS fleet | Browser serial session | Yes | Console session ("handles the permissions") | Proxy fleet — distinct host from SSH endpoint |
| `ec2:EnableSerialConsoleAccess` | API | Existing | Mutating | External | Account-level allow | Yes | IAM `Resource:"*"` | No resource scoping possible |
| `ec2:DisableSerialConsoleAccess` | API | Existing | Mutating | External | Account-level deny | Yes | IAM `Resource:"*"` | — |
| `ec2:GetSerialConsoleAccessStatus` | API | Existing | Non-mutating | External | Read enablement + `ManagedBy` | Yes | IAM `Resource:"*"` | `ManagedBy` ∈ {account, declarative-policy} |

**Doc-flagged leads to keep verbatim:**
- *"After pushing the SSH key to the instance, the SSH connection is **not subject to the IAM policies** that you configured to grant users EC2 Serial Console access."*
- *"Because this connection is outside of the VPC network, EC2 Serial Console **does not use the instance security group or the subnet network ACL** to authorize traffic to the instance."*
- *"The duration of the connection is **not determined by the duration of your IAM credentials**… the connection continues to persist."*
- *"Granting serial console permissions is **equivalent to granting admin-level privileges** on the instance."* (Windows)
- Username format `instance-id.port0`; key lives **60 seconds**; **30 seconds** to tear down a session; **1 active session per instance**.

---

## 5. Recommended Areas of Focus (ordered by priority; one block per firing lens)

### Area 1 — Post-push connection is decoupled from IAM (Lens M / C — HIGHEST PRIORITY)
**Background:** The push is IAM-authorized, but the docs explicitly say the subsequent SSH connection "is not subject to the IAM policies." The only connect-time secret is possession of the private key matching the 60-second pushed public key; the username is the deterministic `i-<id>.port0`; there is no session token.
**Security Concern:** If the connection is bound *only* to the pushed public key and not to the pushing principal's identity/source, then (a) anyone who obtains or substitutes the private key, (b) a racing third party, or (c) a co-resident process could ride the 60-second window and seize the single per-instance session.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* The serial session can be established from a **different principal / source IP / network** than the one that called `SendSerialConsoleSSHPublicKey`, provided it holds the private key. → *Oracle:* push from principal/host X, connect successfully from unrelated host Y within 60s. Refuted if the endpoint binds the session to the caller's source or a derived identity.
- *Claim:* The pushed **public key is not cryptographically bound to the requester** — pushing an attacker-chosen key for which the victim-targeted flow expected a different key still lets the attacker connect. → *Oracle:* observe whether any field ties the key to the principal; a plain pubkey store implies no binding.
- *Claim:* The **credential-expiry decoupling** lets a session outlive revoked/expired IAM credentials (documented) — test whether an **explicit IAM deny / key disablement** mid-session tears the session down, or it persists the full hour. → *Oracle:* revoke the principal after connect; session stays up = the documented behavior is a durable post-revocation access window.
**Doc evidence:** connect-to-serial-console.md ("not subject to the IAM policies"; credential-expiry text); 60s key TTL. **Severity-if-true:** High (persistent / transferable serial access past the authz point).
**Stop condition:** session established from an unrelated identity → documented, record and move on; do not pivot into the guest beyond proving the session opened.

### Area 2 — Cross-account / cross-tenant push and fleet multi-tenancy (Lens A / V — HARD-STOP ADJACENT)
**Background:** `SendSerialConsoleSSHPublicKey` takes a bare `InstanceId` (`^i-[a-f0-9]+$`). The resource ARN embeds `${Account}`, so IAM *should* scope to the caller's account; but the serial-console **service fleet is multi-tenant** and bridges to many customers' serial ports.
**Security Concern:** Does authorization bind the instance to the **caller's account**, or only to the instance's **existence**? A foreign instance-ID that returns anything other than a clean `AuthException`/`EC2InstanceNotFoundException` is an enumeration/ownership oracle; a successful push is cross-account OS access.
**High-level Test Scenarios:**
- *Claim:* Pushing a key to an instance-ID owned by a **different account** succeeds or yields a distinguishing error. → *Oracle:* compare responses for (self-owned valid) vs (foreign valid) vs (nonexistent) IDs. `EC2InstanceNotFoundException` vs `AuthException` vs `EC2InstanceStateInvalidException` timing/wording forms a **cross-account existence oracle** (Lens A differential-error variant). *Note:* instance-IDs carry no checksum here (pure `i-[a-f0-9]+`), so foreign IDs are fabricable/enumerable — unlike checksummed resource IDs.
- *Claim:* On the **shared fleet**, one customer's serial session can observe another's serial byte-stream (session-slot collision, mis-routing by the deterministic `i-<id>.port0` username). → *Oracle:* any cross-customer serial content = **Critical + HARD STOP**.
**Doc evidence:** list_ec2-instance-connect.md (resource `instance`, account in ARN); ec2-serial-console.md ("grant account access"); multi-tenant fleet endpoints. **Severity-if-true:** Critical.
**Stop condition:** first cross-account/cross-tenant signal → preserve evidence, disclose, stop.

### Area 3 — IAM scoping bypass on the push: ABAC tag race & missing `osuser` (Lens I / S / X)
**Background:** The only condition keys for the serial action are `aws:ResourceTag`/`ec2:ResourceTag`. The recommended "secure" policy is tag-based ABAC (`aws:ResourceTag/SerialConsole == aws:PrincipalTag/SerialConsole`). There is **no `ec2:osuser` key** (its sibling `SendSSHPublicKey` has one).
**Security Concern:** Tag-based gates on a mutating action are vulnerable to tag races and to the holder self-tagging; and the absence of `osuser` scoping means IAM cannot restrict *which OS user* a serial push ultimately logs in as — all serial access is all-or-nothing per instance.
**High-level Test Scenarios:**
- *Claim:* A principal who can also `ec2:CreateTags` can **self-widen** — tag a foreign/unintended instance with the gating `SerialConsole` value, then push. → *Oracle:* push succeeds after self-tagging where it was denied before (Lens S self-tag variant).
- *Claim:* **Tag-vs-action race** — the ResourceTag condition is evaluated against a tag state the caller can flip between evaluation and the serial bridge. → *Oracle:* TOCTOU between `CreateTags` and the push/connect.
- *Claim:* **Twin-action parity** — `SendSSHPublicKey` (standard) and `SendSerialConsoleSSHPublicKey` (serial) differ in condition-key coverage (`osuser` only on the former). A policy that denies standard SSH to a user via `ec2:osuser` does **not** constrain serial access, which bypasses the OS-user gate entirely (GRUB single-user → root). → *Oracle:* a principal denied non-root standard SSH still reaches root via serial. (Lens X.)
- *Claim:* ABAC **case-sensitivity / normalization** fail-open on the tag value (Lens S case variant). → *Oracle:* a Deny keyed on one casing is inert against another.
**Doc evidence:** configure-access-to-serial-console.md (tag policy example); list_ec2-instance-connect.md (condition keys; no `osuser` on serial). **Severity-if-true:** High (serial = root/admin).
**Stop condition:** one confirmed scope-bypass push; do not enumerate further instances.

### Area 4 — Network-control evasion: SG/NACL/VPC bypass by design (Lens V / U)
**Background:** Docs state plainly the serial connection is outside the VPC and **does not consult the security group or NACL**. Many orgs treat "no inbound SG rule / private subnet / no public IP" as the isolation boundary.
**Security Concern:** The serial path is an **out-of-band ingress to the OS** that none of the customer's network controls can see or block; the only levers are account-enablement, IAM on the push, and the OS password (itself bypassable — Area 5). A documented guarantee ("SG protects my instance") is simply not enforced on this path.
**High-level Test Scenarios:**
- *Claim:* An instance with a fully-closed SG and no public IP is still reachable via the serial console by any principal holding the push permission. → *Oracle:* connect to the serial console of such an instance. (Confirms the documented inversion; value is in making the blast radius explicit for the customer.)
- *Claim:* There is **no network-layer condition key** (`aws:SourceIp`, VPC, etc.) that constrains the serial *connect* step — so an org cannot restrict serial access to, e.g., a bastion CIDR. → *Oracle:* enumerate condition keys; absence = unmitigable-by-network (Lens U doc-vs-enforcement).
**Doc evidence:** configure-access-to-serial-console.md ("does not use the instance security group or the subnet network ACL"). **Severity-if-true:** Medium–High (the control the customer relies on is advisory on this path).

### Area 5 — OS-auth bypass through the serial channel (Lens U / E — guest-scoped)
**Background:** Docs require a password-based OS user to *use* the Linux serial console, but the troubleshooting guide documents **GRUB single-user / emergency mode** (edit kernel line → `single`/`emergency` → root shell) and **SysRq**, neither of which needs the OS password. Windows serial perms are "equivalent to admin-level privileges."
**Security Concern:** The OS-password requirement is presented as the guest-level access control, but it is bypassable by anyone who reaches the serial console at boot — i.e., the real gate is the push IAM permission (+ account enablement), and that gate yields **root/admin**, not a limited user.
**High-level Test Scenarios:**
- *Claim:* A serial connector with **no OS credentials** reaches root via GRUB single-user/emergency mode (reboot via SysRq `b`, interrupt GRUB, append `single`). → *Oracle:* root prompt without password.
- *Claim:* SysRq from the serial console can **crash/reboot (`c`/`b`)** the instance → DoS or forced reboot to reach GRUB. → *Oracle:* instance reboots on command.
- *Claim:* Session **persists across reboot and stop** (documented) → an attacker who opens a session can ride a reboot into single-user mode and view all boot/secret output. → *Oracle:* boot messages / secrets visible post-reboot in the same session.
**Doc evidence:** troubleshoot-using-serial-console.md (GRUB single-user, SysRq `b`/`c`); disconnect/connect pages (session survives reboot/stop). **Severity-if-true:** High on the guest. **Scope caveat:** this is access the customer *granted via IAM* acting on the customer's *own* guest — frame as "serial permission ⇒ unconditional root, bypassing the documented OS-password gate," a privilege-escalation/blast-radius finding, **not** a cross-tenant AWS defect unless Area 1/2 also fire.

### Area 6 — Session-slot DoS & teardown race (Lens L / M)
**Background:** "Only 1 active serial console session per instance"; a 2nd push fails with `SerialConsoleSessionLimitExceededException`; 30-second teardown after disconnect; 60-second key window.
**Security Concern:** A principal with push permission can **hold the single session open for the full hour**, denying the legitimate operator serial access during an incident (exactly when the serial console matters). The 30s teardown + 60s key window are TOCTOU surfaces.
**High-level Test Scenarios:**
- *Claim:* An attacker with push rights can **monopolize** the single session (re-open before teardown completes) → serial-console denial to the real operator during a boot failure. → *Oracle:* legitimate push returns `SessionLimitExceeded` while attacker holds the slot.
- *Claim:* **Teardown race** — within the 30s teardown or the 60s key window, two connectors contend; does the service cleanly reject the second, or can state be confused (session handed to the wrong key)? → *Oracle:* race two pushes/connects; look for mis-binding.
**Doc evidence:** connect/disconnect pages (1 session, 30s teardown, 60s key); API error `SerialConsoleSessionLimitExceededException`. **Severity-if-true:** Medium (single-tenant self-DoS / incident-time DoS); **High only if it crosses a tenant on the shared fleet.**

### Area 7 — Account-setting governance & declarative-policy reporting (Lens U / O)
**Background:** Account enablement is per-Region; `GetSerialConsoleAccessStatus` returns `ManagedBy` = `account` | `declarative-policy`. Under a declarative policy "you can't modify the setting directly within an account."
**Security Concern:** Does the service **faithfully enforce and report** declarative-policy management? If a principal with `ec2:EnableSerialConsoleAccess` can flip the setting while `ManagedBy` still reports `declarative-policy` (or vice-versa), an org-level control is bypassed or misrepresented.
**High-level Test Scenarios:**
- *Claim:* `EnableSerialConsoleAccess` succeeds in a Region governed by a declarative policy that should pin it off (declarative control not enforced on the data path). → *Oracle:* status flips despite declarative management.
- *Claim:* `ManagedBy` **misreports** the controlling entity, hiding the real governance state. → *Oracle:* compare reported `ManagedBy` against the actual org policy.
- *Claim:* Enablement/push of serial access is **under-logged** (no CloudTrail/record for a security-relevant OS-ingress event). → *Oracle:* check that push + connect emit durable, attributable events. (Lens O enabler.)
**Doc evidence:** configure-access-to-serial-console.md (declarative policy; `ManagedBy`). **Severity-if-true:** Medium (governance bypass) / Low-Info (logging gap enabler).

### Area 8 — Endpoint trust, fingerprint & MITM (Lens Y)
**Background:** Connect uses per-region SSH endpoints with a **documented host fingerprint** and an explicit MITM warning ("If these fingerprints don't match, someone might be attempting a man-in-the-middle attack"). Browser path is WebSocket:443 to a separate `oneclickv2-proxy` fleet.
**Security Concern:** The private SSH key is the bearer for a root-granting channel; endpoint authenticity and transport integrity are the only things standing between the operator and a fleet impersonator.
**High-level Test Scenarios:**
- *Claim:* The SSH endpoint accepts a connection whose transport is **downgraded** or whose host key is **unvalidated** (clients that skip fingerprint check), enabling MITM capture of the serial stream and keystrokes. → *Oracle:* downgrade/MITM attempt against the documented endpoint; refuted if strict key pinning.
- *Claim:* The browser proxy (`oneclickv2-proxy`) and the SSH endpoint are **distinct fleets** with possibly different TLS/validation postures — is the WebSocket:443 path's certificate/origin validation as strict as the SSH path? → *Oracle:* compare, look for an origin/cert gap. **Any fleet-identity leakage here = HARD STOP.**
**Doc evidence:** connect-to-serial-console.md (fingerprint table, MITM text); prerequisites (proxy endpoint:443). **Severity-if-true:** High (MITM on a root channel). **Note:** attacking AWS's own endpoint TLS trends toward the service plane — reason from docs; do not attack live AWS endpoints beyond confirming the documented control exists.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account serial push | `SendSerialConsoleSSHPublicKey` authz | Instance ARN embeds `${Account}`; `AuthException` on foreign instance |
| Post-push session hijack / transfer | SSH data path, 60s key | "connection not subject to IAM"; single session/instance |
| Session outlives revoked IAM creds | session lifetime | "duration not determined by IAM credentials" (this *is* the risk) |
| Tag-ABAC self-widen / race | push condition keys | `aws:ResourceTag`/`PrincipalTag` equality policy |
| Twin-action parity gap (`osuser`) | push vs `SendSSHPublicKey` | `ec2:osuser` on standard SSH only |
| SG/NACL bypass to isolated instance | serial network path | "outside VPC … does not use SG or NACL" (documented inversion) |
| OS-password bypass to root | GRUB/SysRq/SAC on guest | password-based OS user requirement |
| Single-session monopoly DoS | session slot | 1 session/instance; `SessionLimitExceeded`; 30s teardown |
| Declarative-policy enforcement/report | account setting | `ManagedBy`; "can't modify directly" under declarative policy |
| Endpoint MITM / fingerprint skip | SSH/WS endpoints | per-region fingerprint; MITM warning |
| Cross-tenant stream on shared fleet | serial-console fleet | multi-tenant endpoint (→ HARD STOP) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Guest-OS compromise as the "finding" by itself.** Reaching root on the customer's *own* instance via a serial permission the customer granted is expected behavior (Windows docs call it "admin-level"); only report it as blast-radius context or when chained with an IAM-scope bypass (Area 3) or cross-tenant reach (Area 2). GRUB/SysRq are standard OS features, not AWS defects.
- **IMDS / in-guest secrets on a fully-managed host** — out of scope as an AWS defect.
- **Single-tenant self-DoS** (monopolizing your own instance's session) — Low/out-of-scope unless it crosses a tenant on the shared fleet.
- **Attacking live AWS serial-console endpoints** (`*.ec2-instance-connect.<region>.aws`, `oneclickv2-proxy`) beyond confirming documented controls — this is AWS's service plane. Reason from docs; the moment live evidence implicates the fleet, **HARD STOP + disclose**.
- **Product/feature-parity gaps** (regions not supported, instance types excluded) — not vulnerabilities.
- **Customer-authored IAM footguns** (over-broad `Resource:"*"` on the push the customer wrote themselves) — least-privilege advice, not an AWS defect. *Exception:* the docs' own sample policies (Section "Explicitly allow / tag-based") — if a **shipped AWS sample** is insecure-by-default, that is in scope (Lens R).

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages read)
- **Lens B (Confused deputy / PassRole):** No role-ARN input on any serial-console API — `SendSerialConsoleSSHPublicKey` takes only `{InstanceId, SerialPort, SSHPublicKey}`. Checked: API_SendSerialConsoleSSHPublicKey, list_ec2-instance-connect. **Null.**
- **Lens G (SSRF):** No customer-supplied URL/host field that the service dereferences in the documented surface. The push takes a public *key*, not a URL. Checked: API reference, connect/configure pages. **Null** — *but* re-open if the hunter finds an undocumented fetch of key material or fingerprint retrieval.
- **Lens H (KMS/encryption-context):** No customer-managed-key or encryption-context mechanism documented for serial console. Checked: all 5 UserGuide pages. **Null.**
- **Lens K (Prompt injection):** No LLM/agent in the pipeline. **Null.**
- **Lens Q (File upload):** The only "upload" is the SSH public key (len 80–4096, validated as key material). No image/doc/archive ingestion. Checked: API reference. **Null**, but verify the key parser rejects malformed/oversized material cleanly (overlaps Lens F memory-safety of the key parser — worth a cheap probe).
- **Lens F (translation/parser):** Possible thin surface — the serial-console service parses the SSH public key and bridges a raw byte stream to the serial port. **Doc-gap:** no documentation of how the pushed key is parsed or how serial bytes are framed on the fleet. Mark "doc-gap — confirm surface first"; a malformed-key / oversized-frame probe is in scope but trends toward the service plane (reason carefully).
- **Lens N / EE (namespace / predictable-name):** Username `i-<id>.port0` is predictable, but resolution is to the caller's own instance via IAM; no global/first-come namespace the attacker pre-registers. **Null** (folded the predictability concern into Area 1/2).
- **Lens W / DD / BB / CC / FF / J / T:** No attestation gate, no caching layer, no multi-parser auth front-end, no upstream-asserted-identity header, no JWT/OIDC token, no OAuth/3P linking, and no generated-and-persisted secret documented for the serial-console feature itself. Checked: all target pages + IAM reference. **Null** for this feature (note: `OpenTunnel` / EC2 Instance Connect **Endpoint** is a *different* feature in the same service prefix with `privateIpAddress`/`remotePort`/`maxTunnelDuration` keys and its own ENI/network surface — out of scope for this plan but a natural adjacent target).

---

### Priority summary for the hunter
1. **Area 1** (IAM-decoupled connection) and **Area 2** (cross-account / shared-fleet) — highest impact, Area 2 is HARD-STOP territory.
2. **Area 3** (ABAC/tag + `osuser` twin-parity bypass) — concrete, testable IAM boundary.
3. **Area 5** (OS-auth bypass) and **Area 4** (SG/NACL evasion) — establish blast radius; chain to Area 3 for impact.
4. **Area 6/7/8** — DoS, governance, transport — lower severity, round out coverage.
