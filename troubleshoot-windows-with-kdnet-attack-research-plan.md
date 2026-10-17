# KDNET Kernel Debugging for Windows EC2 (ENA KDNET Extensibility Module) — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-windows-with-kdnet.html (mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/troubleshoot-windows-with-kdnet.md`), plus adjacent EC2 UserGuide pages (serial console, ENA driver, NitroTPM) and Microsoft KDNET debugger docs (learn.microsoft.com). Status: **documentation-derived hypotheses only; nothing tested against a live account.** Produced via the `security-questionbuilder` skill.

Feature maturity: **NEW** — the required OS builds are Windows Server 2025 build 26100.7462 "December 2025 patch", Windows 11 24H2 26100.7309, 25H2 26200.7309. This is a late-2025 capability with minimal public review → **Step-5 top priority as new surface.**

---

## 0. How to use this document

- Each lead follows: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **Scope reality for a hunter:** the *target* kernel being debugged is a **customer-owned** OS. KDNET is guest↔guest over the customer VPC. So most impact here is **intra-customer** (one instance/principal taking over another customer instance) — High when it crosses a tenant/team/account trust line inside the customer, and a serious **customer-facing posture defect** that AWS's own guidance induces. It is **not** a path into AWS's service plane by itself.
- **HARD STOP:** if any probe ever produces evidence of an identity/credential/ARN/account belonging to **AWS's own service/Nitro plane** (e.g. KDNET traffic reaching a Nitro/host interface, or the ENA module leaking host-side state), STOP, preserve evidence, and flag for AWS-Security disclosure. KDNET is expected to be guest-only; any host-plane reach is out-of-expectation and reportable.
- **AWS-authored-artifact carve-out:** the self-referencing security-group recipe and the "up to 13 chars" key guidance are **AWS-authored guidance a customer is told to copy**. A weak default there is in scope as an AWS documentation/hardening defect (Tier 2), not dismissed as a customer footgun.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)

1. **Drive a victim's kernel debugger without being the designated debug host** — from any instance that shares the recommended security group (or any neighbor in the subnet), reach a target's KDNET UDP stub and obtain ring-0 read/write/exec on that target.
2. **Defeat the only authenticator (the KDNET key)** — brute-force or recover a low-entropy / captured KDNET key and establish a session, or determine whether the key authenticates the debugger at all vs merely encrypting.
3. **Crash or corrupt the target kernel pre-auth** — send malformed KDNET UDP frames to the kernel parser (`kd_02_1d0f.dll`) and cause BSOD / memory corruption without a valid key.
4. **Turn a transient debug session into a persistent network backdoor** — find a target left in `/debug on` state after cleanup was skipped, or propagated into an AMI/snapshot, and recover its key.
5. **Determine the detection blind spot** — confirm whether a full KDNET takeover produces any AWS control-plane / CloudTrail / GuardDuty signal.
6. **Map the control-plane path to the port** — enumerate the IAM actions/condition keys that let a principal open UDP 50000–50039 or join the KDNET SG, and whether a low-privilege principal can do so.

---

## 2. Components, Assets, and Design

**What it is.** A kernel-debugging transport for Windows EC2 instances. The **KDNET Extensibility Module for ENA** (`C:\Windows\system32\kd_02_1d0f.dll`, a kernel-mode driver) lets the in-box Windows KDNET kernel debugger transport ride the Elastic Network Adapter, so WinDbg on one instance can kernel-debug another over UDP.

**Components / hosts:**
- **Debug target** — Windows EC2 instance being debugged. Runs the KDNET ENA module in-kernel; parses attacker-reachable UDP debug frames at/early in boot. Must have `bcdedit /debug on`, Secure Boot OFF, a supported instance type, and a supported OS build.
- **Debug host** — Windows EC2 instance running WinDbg (`windbgx -k net:port=..,key=..`). Listens on the KDNET UDP port.
- **ENA device** — the NIC carrying debug traffic. When debugging is active it is **dedicated** to debugger traffic (target loses normal connectivity on that NIC unless a 2nd ENA is attached).
- **Security group(s)** — the sole AWS-layer access control on the wire. Recommended config: one SG with an inbound rule allowing **UDP from itself**, attached to both instances.
- **No AWS control-plane component** is in the debug datapath — there is **no EC2 API, no IAM action, and no service-side authorization** that gates establishing a KDNET session. This is a critical design fact (contrast with EC2 Serial Console, which *is* IAM-gated via `ec2:SendSerialConsoleSSHPublicKey` + an org/account opt-in).

**Assets:**
- Ring-0 control of the debug target (the crown jewel: a KDNET session = arbitrary kernel read/write + code execution + halt/break-in).
- The **KDNET key** (256-bit, 4×64-bit, each segment ≤13 chars of `[a-z0-9]`), persisted in the target's **BCD store** (`bcdedit /dbgsettings`), readable by any local admin and captured into any image/snapshot taken while configured.
- The debug **port** (UDP, recommended 50000–50039 — a 40-port predictable range).

**Identity / authN model:** There is **no principal-level identity.** A debugger is "authenticated" only by (a) IP reachability to the UDP port (gated by SG + in-guest Windows Firewall) and (b) possession of the KDNET key. Kernel debugging **bypasses all OS-level RBAC** once established.

**ASCII pipeline:**
```
                      customer VPC subnet (same subnet required)
  [ Debug host EC2 ]  --- UDP 50000-50039 (KDNET, key-"encrypted") --->  [ Debug target EC2 ]
     WinDbg -k net                                                         kd_02_1d0f.dll (kernel)
     port=,key=                                                            bcdedit /debug on, SecureBoot OFF
        ^                                                                       |
        |________________ Security Group: "allow UDP from SELF" ______________ |
                          (attached to BOTH -> every instance in the SG can reach the port)

  AWS control plane: (none in datapath)  <-- no IAM/API gate on the KDNET session itself
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Any instance sharing the recommended SG | Target's KDNET UDP stub | Self-referencing SG allows UDP from the whole SG, not just the host | A **non-host** instance in the SG completes a KDNET handshake / reads target kernel memory = boundary breach |
| Any neighbor in the same subnet (if SG wider / misconfigured) | Target UDP 50000–50039 | Same-subnet requirement + 40-port predictable range | Any subnet neighbor reaches the stub and drives the debugger |
| Attacker knowing/guessing the key | Target kernel (ring-0) | KDNET key is the sole authenticator | A guessed/brute-forced/recovered key yields a working session = full target compromise |
| Unauthenticated packet sender | `kd_02_1d0f.dll` kernel parser | UDP frames parsed in-kernel, pre-session | A malformed frame causes BSOD / memory corruption **without** a valid key |
| Principal with EC2 SG/ENI IAM | The UDP port's openness | `ec2:AuthorizeSecurityGroupIngress`, `ec2:ModifyInstanceAttribute`(groups), `ec2:AttachNetworkInterface`, `ec2:RunInstances` into subnet/SG | A low-priv principal opens the port or lands an instance inside the KDNET SG |
| Holder of a snapshot/AMI of a debug-configured target | The live KDNET key in the BCD store | Key persisted in BCD, copied into images | Key recovered from an image/snapshot authenticates to a still-live stub |
| Cross-account principal in a **shared VPC subnet** (RAM) | Target's UDP stub | Shared subnet + SG referencing | A different *account's* instance reaches the stub = cross-account High |
| **Any customer surface** | **AWS Nitro / host / service plane** | (not expected in datapath) | **HARD STOP** — any KDNET reach to a host/Nitro interface or ENA-module leak of host state |

---

## 4. API / Interface Inventory

KDNET exposes **no AWS SDK/API surface of its own** — the entire datapath is UDP + in-guest `bcdedit`/WinDbg. The relevant *control-plane* surface is the generic EC2 networking APIs that shape reachability, plus the in-guest commands.

| Name | Type | Mutating | Internet-callable | Authorized callers | Functionality / relevance | Notes |
|---|---|---|---|---|---|---|
| `windbgx -k net:port=,key=` | in-guest (host) | n/a | no (UDP on VPC) | anyone on the host OS | Opens listener; initiates debug session | No AWS authz |
| `bcdedit /dbgsettings net ...` | in-guest (target) | yes (BCD) | no | local admin on target | Sets host IP/port/key/busparams; **persists key in BCD** | Key readable by any admin + in images |
| `bcdedit /debug on` / `/bootdebug on` | in-guest (target) | yes | no | local admin | Enables kernel/boot debugging; weakens integrity posture | Requires Secure Boot OFF |
| KDNET UDP stub (50000–50039) | network | yes (kernel) | VPC-reachable | **anyone who can reach the port + has the key** | The actual attack surface | **No principal identity** |
| `ec2:AuthorizeSecurityGroupIngress` | AWS API | yes | yes (SigV4) | IAM-dependent | Opens the UDP port on the SG | See §5 lens V/IAM; subagent-enriched |
| `ec2:ModifyInstanceAttribute` (groups) / `ec2:AttachNetworkInterface` / `ec2:RunInstances` | AWS API | yes | yes | IAM-dependent | Lands/joins an instance into the KDNET SG/subnet → gains reach to the port | Control-plane path to the stub |
| `ec2:CreateImage` / `CreateSnapshot` + `ebs:GetSnapshotBlock` | AWS API | yes | yes | IAM-dependent | Captures a debug-configured target → key recovery (Lens T) | Chains to backdoor |

> **Undocumented/console-hidden knob sweep:** the `{{port-number}}` is free-form (doc only *recommends* 50000–50039 — nothing forces it); `{{encryption-key}}` accepts user-chosen low-entropy values (the API/command does not enforce a minimum). `bcdedit /bootdebug on` (exposes the earliest boot stage to the network) is tucked in a "Tip" with no warning. These are the weakest-value knobs the prose under-surfaces.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority-ordered)

> Crypto/protocol specifics, the EC2 IAM condition-key table, and Secure-Boot posture specifics below were cross-checked against Microsoft's KDNET manual-setup page and the offline EC2 Service Authorization reference. Areas are priority-ordered: 1–3 are the top-tier leads (reachability, the published/weak key, the pre-auth kernel parser).

### Area 1 — Network reachability: the self-referencing SG over-breadth (Lens V, U, A) — TOP PRIORITY
**Background.** The doc's "simplest way" is a single SG with an inbound rule allowing **UDP from itself**, attached to **both** instances. A self-referencing SG authorizes *every* member instance to send UDP to *every* other member on that port — not just the one debug host.
**Security Concern.** A KDNET session is ring-0 control of the target. If the KDNET SG is shared by more than the two debug instances (common for a reused/standard SG), **any** member instance — not the intended host — can attempt to drive the target's debugger. In a RAM-shared subnet this can span accounts.
**High-level Test Scenarios (falsifiable):**
- *Claim:* a non-host instance that merely shares the SG can reach the target's UDP 50000–50039 stub. *Mechanism:* "create a security group with an inbound rule that allows UDP traffic from itself as the source, and then attach that security group to both instances." *Oracle:* UDP from a third SG-member instance reaches the port (and, with the key, drives the debugger). *Severity:* High (intra-customer lateral kernel takeover); **Critical if the SG/subnet is RAM-shared cross-account.**
- *Claim:* the AWS-recommended rule is broader than needed vs a least-privilege rule (host private IP /32, or a dedicated 2-member SG created/destroyed per session). *Mechanism:* same sentence. *Oracle:* doc review — no narrower alternative is offered. *Severity:* Low–Medium **AWS-authored hardening defect** (Tier 2, routable as doc fix).
- *Claim (cross-account nuance):* the SG itself does **not** span accounts — in a RAM-shared VPC a participant cannot attach another account's SG by default. The true cross-account path is a **permissive subnet NACL** on a shared subnet (NACLs apply to all participants regardless of SG/account), which would let a different account's instance reach UDP 50000–50039. *Oracle:* confirm a shared-subnet NACL allows the range. *Severity:* **High if found** (cross-account ring-0), but this is an **orthogonal shared-VPC/NACL hygiene footgun**, not a KDNET-doc defect — keep same-account exposure (Area 1 main) as the primary, AWS-owned finding.
**Doc evidence:** Prerequisites §, security-group paragraph. **Stop condition:** once a non-host SG member completes a handshake, record and stop (do not pivot deeper into the victim kernel beyond proof).

### Area 2 — The KDNET key is the only authenticator: published example key, weak entropy, auth semantics (Lens Y, M) — TOP PRIORITY
**Background.** Access to the target kernel is gated solely by (a) reaching the UDP port and (b) the KDNET key. The doc prints a **literal, fully-formed example key inside the copy-pasteable command template** (`1kdnet2keys3.4kdnet5keys6.7kdnet8keys9.10kdnet11ke`), and permits each of 4 key segments to be **"up to 13 characters"** of `[a-z0-9]` with **no stated minimum**. Microsoft's equivalent manual-setup page states the *auto-generated* key (produced when you omit `key:`) is "more secure and provides a unique value" — AWS's template always supplies a key up front, steering operators into the weaker manual path.
**Security Concern.** If an operator copies the command without substituting a real secret, the instance is "secured" by a value **published on a public AWS doc page** — a known-key default, directly scannable with zero cryptanalysis. If the key provides only confidentiality (not debugger authentication), anyone who recovers/guesses it can inject, not just read.
**High-level Test Scenarios (priority order):**
- **[HEADLINE PoC] *Claim:*** a target exists whose live KDNET key is the doc's verbatim example `1kdnet2keys3.4kdnet5keys6.7kdnet8keys9.10kdnet11ke`. *Mechanism:* the example key sits inside a literal `bcdedit /dbgsettings net … key:{{encryption-key}}` code block, not a "replace this" warning box. *Oracle:* `windbgx -k net:port=<p>,key=1kdnet2keys3.4kdnet5keys6.7kdnet8keys9.10kdnet11ke` across ports 50000–50039 against a rebooting target completes a kernel-debug session. *Severity:* **Critical** (ring-0 takeover, no brute force) — contingent only on operator copy-paste hygiene. **This is the single most concrete, doc-grounded lead.**
- *Claim:* a user-chosen short key is brute-forceable — `bcdedit` accepts near-trivial keys (e.g. `a.a.a.a`, ~21 bits). *Mechanism:* "each 64-bit value can be **up to** 13 characters" (no floor). *Oracle:* confirm `bcdedit` accepts a 1-char-per-segment key, then estimate online brute-force cost against the handshake. *Severity:* High if practical. **AWS doc defect:** permits/illustrates weak keys with no minimum-entropy requirement.
- *Claim:* the host listener is promiscuous — AWS's `windbgx -k net:port=,key=` command omits `target=`, so the host binds without pinning a target IP and the key is the sole discriminator; a 3rd SG-member can impersonate the target (or win the post-reboot connection race). *Mechanism:* Step 3 command has no `target=`; Microsoft notes the host otherwise auto-selects/listens broadly. *Oracle:* a 3rd instance with the key connects to the host / races the legitimate target's reboot handshake. *Severity:* High (impersonation / session hijack — Lens M).
- *Claim (DOC-GAP):* the key provides confidentiality only, not authenticated integrity — any party with the key can inject/modify debugger packets (no AEAD/sender-auth documented). *Oracle:* needs Microsoft algorithm disclosure or protocol capture (out of doc scope). *Severity:* Critical if confirmed → key secrecy is the *only* control even against a strong key.
**Doc evidence:** Step 2 key definition + example; Step 3 `windbgx -k net:…` (no `target=`). **Stop condition:** a single successful session (esp. via the example key) is the PoC — do not escalate into the kernel.

### Area 3 — Kernel packet-parser memory safety: `kd_02_1d0f.dll` (Lens F native memory-safety) — TOP PRIORITY
**Background.** `kd_02_1d0f.dll` is a **kernel-mode** KDNET ENA extensibility module that parses attacker-reachable UDP frames, potentially at the earliest boot stage (and pre-session before the key is validated).
**Security Concern.** A length/offset/size field trusted before bounds-checking in a kernel UDP parser = ring-0 memory corruption (RCE) or BSOD — potentially **pre-auth** (no key needed) if the parser touches a frame before key validation.
**High-level Test Scenarios:**
- **[PRE-AUTH] *Claim:*** outer frame/length/offset parsing necessarily runs **before** the payload can be decrypted and the key validated — so a subset of the kernel receive path is reachable with **zero key knowledge**. KDNET takes exclusive control of the NIC (no NDIS miniport loaded, per Microsoft), so there is no upstream OS IP/UDP sanitization; KDNET parses raw frames itself. *Oracle:* a malformed-length frame with a garbage key causes a crash *before* any key-mismatch reject. *Severity:* Critical — the key's brute-force resistance is **irrelevant** to this bug class; a single UDP packet → BSOD (DoS) or ring-0 RCE.
- *Claim:* malformed/oversized/truncated/deeply-structured frames cause BSOD / memory corruption. *Oracle:* crafted frame → observable crash on a `/debug on` target. *Severity:* pre-auth BSOD = Medium–High (cross-instance DoS); corruption→RCE = Critical.
- **[DOC-GAP — HIGHEST-PRIORITY UNKNOWN] *Claim:*** the parser is reachable **whenever `/debug on` + busparams are set every boot**, not only during an active WinDbg session. *Oracle:* determine (Microsoft/empirical) whether the stub listens persistently or only while a host is connected — this sets the real exposure window. *Severity:* if persistent, every debug-configured (or debug-left-on) instance is continuously attackable.
- *Claim (ownership/doc-gap):* `kd_02_1d0f.dll` is **Microsoft-signed/distributed** ("distributed as part of Windows … updated through Windows monthly cumulative updates") yet is ENA-specific (`1D0F` = Amazon PCI vendor ID). Patch cadence is therefore a **≥1-month Patch-Tuesday floor** with no AWS out-of-band fix path. *Oracle:* confirm the Microsoft-core-vs-Amazon-shim authorship split for disclosure routing (MSRC vs AWS). *Severity:* n/a (routing + remediation-SLA risk note).
**Doc evidence:** `Test-Path C:\Windows\system32\kd_02_1d0f.dll`; "distributed as part of Windows … updated through Windows monthly cumulative updates." **Stop condition:** a reproducible crash is the PoC; do NOT weaponize memory corruption.

### Area 4 — Kernel debug = total privilege bypass (Lens E)
**Background.** A KDNET session grants arbitrary kernel read/write, breakpoint, and code execution — above any OS account, bypassing all Windows RBAC/UAC.
**Security Concern.** A network-adjacent actor (Areas 1–2) who should have had *no* OS account on the target obtains SYSTEM-and-above. This is the severity multiplier for Areas 1–3.
**Test Scenario:** *Claim:* a successful KDNET session lets the debugger read LSASS/secrets and execute code in ring-0. *Oracle:* conceptually established by KDNET semantics; the PoC is simply *having a session as a non-owner*. *Severity:* Critical on the target instance (full compromise). **Stop condition:** session establishment proves it — do not dump secrets.

### Area 5 — Persistent debug backdoor & key recovery from images (Lens T, AA, U)
**Background.** Cleanup is a manual post-step (`bcdedit /debug off`, `/dbgsettings LOCAL`, `/deletevalue loadoptions`). The key lives in the BCD store.
**Security Concern.** A target left debug-enabled (cleanup skipped) is a standing network kernel backdoor for anyone with port+key. Worse, the **key persists in BCD** and is copied into any **AMI/snapshot** taken while configured; sharing that AMI/snapshot (or reading it via `ebs:GetSnapshotBlock`) leaks the live key — a **secret coming to rest under different IAM reachability than the datapath** (Lens T).
**Test Scenarios:**
- *Claim:* the key is stored **in cleartext** in the BCD store, recoverable by any local admin and from an image/snapshot. *Mechanism:* Microsoft's `bcdedit /dbgsettings` output shows `key XXXXX.XXXXX.XXXXX.XXXXX` in plaintext. *Oracle:* `bcdedit /enum` / offline BCD parse exposes `hostip/port/key`. *Severity:* High (standing backdoor + key disclosure).
- *Claim:* an AMI built from a debug-enabled instance silently distributes a live kernel backdoor (port+key) to every instance launched from it. *Mechanism:* no EC2 control-plane flag/console banner detects `/debug on` at `CreateImage`; AWS `AMIs.md` says nothing about BCD surviving Sysprep/generalize (confirmed zero matches). Sysprep's exact behavior toward `{dbgsettings}` is an open sub-question. *Oracle:* create an AMI from a debug-configured instance, launch it, read BCD — key still present. *Severity:* High.
- *Claim:* the doc gives no warning that cleanup must precede imaging, and AWS's own `ec2-windows-security-best-practices.md` never cross-references this ring-0-capable feature (confirmed zero `debug`/`kdnet` matches). *Oracle:* doc review. *Severity:* Medium **AWS doc defect.**
**Doc evidence:** Clean-up §; `bcdedit /dbgsettings`; absence in `AMIs.md` / `ec2-windows-security-best-practices.md`. **Stop condition:** recovering the key string from an image you own is proof.

### Area 6 — Availability: dedicated ENA + kernel break-in (Lens L)
**Background.** "When kernel debugging is active, the ENA device … is dedicated to debugger traffic only." A debugger can also *break into* (halt) the target kernel.
**Security Concern.** An attacker reaching the stub (Areas 1–2) can halt/freeze the target or, via the dedicated-ENA behavior, disrupt its normal networking — cross-instance DoS. Also a pre-auth parser crash (Area 3).
**Test Scenario:** *Claim:* a non-owner with the key can issue a break-in that freezes the target; or a flood/parser-crash causes DoS without the key. *Oracle:* target becomes unresponsive attributable to KDNET traffic. *Severity:* High if cross-tenant on shared infra; Medium intra-account. **Stop condition:** a single confirmed freeze is proof.

### Area 7 — Security-posture downgrade required to use the feature (Lens U, W)
**Background.** The feature requires `bcdedit /debug on` and **Secure Boot OFF** ("does not currently support instances with Secure Boot enabled … Amazon images with a 'TPM' prefix have Secure Boot enabled by default"), plus `FORCEHVTONOTSHAREDEBUGDEVICE` and optional `/bootdebug on`.
**Security Concern.** To follow this AWS-documented procedure the customer must **materially weaken boot/kernel integrity** (measured/Secure Boot off; kernel debugging interacts with code-integrity, PatchGuard, VBS/HVCI). The page presents these as functional prerequisites/tips with **no prominent security warning**.
**Test Scenarios:**
- *Claim:* AWS **omits a security-tradeoff warning that Microsoft's own identical procedure includes.** *Mechanism:* Microsoft places an **"Important"** callout *before* its `bcdedit` commands — "you might need to temporarily suspend Windows security features, such as BitLocker and Secure Boot … Re-enable these … when testing is complete." AWS's 228-line page has no analogous callout anywhere; Secure Boot appears only as a neutral compatibility "Note" under Limitations, *after* the steps. *Oracle:* admonition diff (confirmed). *Severity:* Medium–High **AWS doc defect** (AWS is the AMI/instance vendor and drops the OS vendor's warning).
- *Claim:* enabling KDNET disables kernel self-protection (PatchGuard/KPP, DSE, HVCI/VBS) the compliance posture assumes. *Oracle (Microsoft docs):* enumerate what `/debug on` disables — **unverified doc-gap** (primary Microsoft source not located; widely asserted in rootkit research that a debug-enabled boot config neuters PatchGuard even with no debugger attached). *Severity:* Medium if confirmed.
- *Claim:* `/bootdebug on` (a one-line "Tip" with no explanation) exposes the pre-OS boot stage — before Windows Firewall / EDR / SSM init — to the network attacker. *Oracle:* Microsoft boot-debug behavior. *Severity:* amplifies Area 3's pre-auth window (note: the SG still gates the ENI, so this is primarily a guest-side monitoring blind spot).
**Doc evidence:** Limitations §; Step 2 Tip; loadoptions; Microsoft manual-setup "Important" callout. **Stop condition:** documentation/analysis only.

### Area 8 — Control-plane path to the port & IAM scoping (Lens V IAM, S)
**Background.** Reachability to the stub is shaped by EC2 networking APIs. There is **no KDNET-specific IAM**; generic SG/ENI/instance APIs decide who can open the port or join the SG.
**Security Concern.** A low-privilege principal who can mutate the KDNET SG or land an instance into it gains network reach to a ring-0 stub.
**Confirmed condition keys** (verified in `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`):

| Action | SG-relevant resource | Condition keys available |
|---|---|---|
| `ec2:AuthorizeSecurityGroupIngress`/`Egress` | `security-group` | `ec2:SecurityGroupID`, `ec2:Vpc`, `ec2:Region`, `aws:ResourceTag`, `ec2:ResourceTag` |
| `ec2:ModifyInstanceAttribute` (groups) | `instance`, `security-group` | SG block: `ec2:SecurityGroupID`, `ec2:Vpc` |
| `ec2:ModifyNetworkInterfaceAttribute` | `network-interface`, `security-group`, `subnet` | SG block: `ec2:SecurityGroupID`, `ec2:Vpc`; `ec2:Subnet` |
| `ec2:AttachNetworkInterface` | `instance`, `network-interface` | `ec2:Subnet`, `ec2:Vpc`, `ec2:NetworkInterfaceID` (no SG-ID key) |
| `ec2:RunInstances` | `security-group*` (required) | `ec2:SecurityGroupID`, `ec2:Vpc`, `ec2:ResourceTag`; `iam:PassedToService=ec2.amazonaws.com` |

**Test Scenarios:**
- **[HIGH-LIKELIHOOD] *Claim:*** a principal with only the **common, broad** `ec2:RunInstances` or `ec2:ModifyInstanceAttribute` (no `ec2:SecurityGroupID` condition) can **join the KDNET SG** — launching into / re-attaching the SG — thereby enlarging item-1's blast radius, *without* needing SG-authoring rights (`Authorize*SecurityGroup*`). *Mechanism:* `RunInstances` only needs *selection* permission on the `security-group` resource; `ModifyInstanceAttribute` changes an existing instance's SG membership. *Oracle:* inspect the account's policies for any `Deny`/`Condition` on `ec2:SecurityGroupID = sg-<kdnet>` across these actions — absence = any launch/modify-capable principal can self-add to the blast radius. *Severity:* Medium–High enabler; High composed with Areas 1–2.
- *Claim:* the KDNET doc never cross-references these condition keys, so operators don't scope the SG. *Oracle:* doc review (confirmed — no IAM scoping guidance). *Severity:* customer footgun that AWS's own Service Authorization Reference *could* close but the KDNET page omits.
**Doc evidence:** Prerequisites SG paragraph + `list_ec2.md`. **Stop condition:** static policy analysis only; `iam:SimulatePrincipalPolicy` as the safe oracle if ever run live.

### Area 9 — Detection blind spot (Lens O)
**Background.** The entire takeover is UDP between instances + in-guest `bcdedit`. No EC2 API is called to establish a session.
**Security Concern.** A full kernel takeover produces **no CloudTrail/EC2 control-plane event**; only VPC Flow Logs (UDP 50000–50039) and in-guest tooling (SSM inventory of BCD) could reveal it.
**Test Scenario:** *Claim:* no AWS-native audit record attributes the kernel takeover. *Mechanism:* no step calls an EC2 API, so CloudTrail is silent; VPC Flow Logs capture only 5-tuple UDP metadata (not "kernel debug", not the key); GuardDuty has **no documented finding type** for this port range/behavior (confirmed absent in `guardduty_finding-types-ec2.md` / `_active.md`); bcdedit state is visible only to in-guest SSM Inventory/EDR. *Oracle:* Flow Logs are the only passive AWS signal, and only if enabled (not default). *Severity:* Low/Informational as a lens, but a potent **enabler** that raises every other area's practical severity; the doc's lack of any "detection/monitoring" section is itself an AWS doc gap. **Stop condition:** analysis only.

### Composed kill chains (rate at the end of the chain)
1. **IAM → network → key → ring-0:** low-priv `ec2:RunInstances`/`ModifyInstanceAttribute` with no `ec2:SecurityGroupID` condition (Area 8) → join the self-referencing KDNET SG (Area 1) → scan 50000–50039 → connect with the **doc's example key** or a brute-forced weak key (Area 2) → full ring-0 control of a peer instance (Area 4). **End severity: Critical** (intra-account; higher if cross-account via shared-subnet NACL).
2. **Image capture → key recovery → standing backdoor:** `CreateImage`/`CreateSnapshot` of a debug-left-on instance (or `ebs:GetSnapshotBlock` on a shared snapshot) → recover cleartext `key`/`port` from the BCD store (Area 5) → connect to the still-live stub → ring-0 (Area 4). **End severity: High–Critical.**
3. **Pre-auth parser → kernel RCE/BSOD (no key, no IAM):** reach the UDP port (Area 1) → malformed KDNET frame hits `kd_02_1d0f.dll` outer-frame parsing *before* key validation (Area 3) → BSOD (cross-instance DoS) or ring-0 memory corruption. **End severity: Critical** — bypasses the key entirely; the only gate is network reachability + an instance left in `/debug on`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Doc's verbatim example key still live on a target | KDNET key | example key printed in copy-paste command (claim: known-key default) |
| Non-host SG member drives the debugger | Self-referencing SG | "allow UDP from itself" rule (claim: over-broad) |
| Weak/short KDNET key brute-forced | KDNET key | "up to 13 chars [a-z0-9]" (claim: no min entropy) |
| Pre-auth kernel parser crash (no key) | `kd_02_1d0f.dll` | outer-frame parse before key validation (claim: key-independent) |
| Session hijack / impersonation despite `hostip` | KDNET UDP transport | `hostip:` setting (claim: not source-enforced) |
| Pre-auth kernel crash via malformed frame | `kd_02_1d0f.dll` | implicit: key "encrypts" (claim: parser runs pre-key) |
| Standing backdoor after skipped cleanup | BCD store / lifecycle | manual Cleanup section (claim: no warning on imaging) |
| Key recovery from AMI/snapshot | BCD + EBS/AMI | none documented |
| Target freeze / ENA-dedication DoS | ENA device | 2nd-ENA note (availability only) |
| Low-priv principal opens port / joins SG | EC2 SG/ENI IAM | SG config (claim: generic APIs, no KDNET IAM) |
| Posture downgrade (Secure Boot off, debug on) | Boot integrity | Limitations note (claim: no security warning) |
| No audit trail for takeover | CloudTrail/Flow Logs | none documented |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **AWS Nitro / host / service plane** — KDNET is guest↔guest; any reach here is a HARD STOP + disclosure, not routine testing.
- **A customer debugging their own single instance with a strong key on a tight 2-member SG** — intended use; not a finding.
- **Bugs in Microsoft WinDbg / the core KDNET protocol unrelated to the ENA extensibility layer** — route to MSRC, not AWS (but note the ownership ambiguity of `kd_02_1d0f.dll` as a doc-gap).
- **IMDS on the managed host; Nitro hypervisor isolation** — not in this datapath.
- **Single-tenant self-DoS** (customer freezes their own box) — out of scope.
- **Customer-authored SG tightenings** — a customer who narrows the rule is fine; the finding is the *AWS-recommended* broad rule.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did not fire — pages named)

Page set checked for triggers: the full `troubleshoot-windows-with-kdnet.md` (Prerequisites, Steps 1–4, Cleanup, Limitations, Additional notes), plus adjacency scan of the EC2 UserGuide index (serial-console, ENA driver, NitroTPM pages) and the EC2 Service Authorization reference.

- **Lens A (classic resource-by-ID IDOR):** no resource-by-ID API on this surface — folded the cross-tenant angle into V (shared SG/subnet). No opaque-ID enumeration oracle. *Null (page has no API returning a resource by caller-supplied id).*
- **Lens B / C (PassRole / credential vending / STS):** no role ARN, no STS, no credential-vending in the KDNET datapath. *Null — Prerequisites/Steps checked; no role input.*
- **Lens D (data→control plane):** no AWS control-plane reachable from the debug datapath; the "target kernel" is customer-owned, not AWS control plane. Host-plane reach would be a HARD STOP, not an expected finding. *Null, with hard-stop note.*
- **Lens G (SSRF):** no field the service dereferences server-side; `hostip`/`port`/`key` are in-guest config the *target* connects **from**, not a server-side fetch. *Null — whole page checked, no `*Url`/fetch/import/webhook field.*
- **Lens H (KMS/encryption-context):** the "256-bit key" is a KDNET symmetric secret, not KMS; crypto weakness routed to Y. *Null for KMS.*
- **Lens J / K / P / Q / BB / CC / DD / FF:** no OAuth/3P linking, no LLM/agent, no registration/proofing workflow, no file upload, no multi-parser HTTP front/origin, no asserted-upstream identity headers, no caching layer, no JWT/OIDC token validation on this surface. *Null — page checked; none of these mechanisms present.*
- **Lens I / R / S (IAM artifacts):** the page prints **no** IAM policy JSON, no AWS-managed policy, no CFN/SLR/runbook block — so R does not fire on this page; S/IAM scoping is pursued only via the generic EC2 networking APIs in Area 8. *Null for printed-artifact audit; Area 8 covers the generic-API path.*
- **Lens N / X / EE:** no ARN namespace migration, no action-family twin, no predictable-*resource-name* land-grab (the predictable *port range* is folded into V). *Null.*
- **Lens W:** fires only as the Secure-Boot posture-downgrade angle (Area 7); there is no KMS attestation gate. *Partial — see Area 7.*

**Doc gaps to confirm before/with live testing (ranked — these settle real-world severity):**
1. **[TOP] Parser exposure window** — is `kd_02_1d0f.dll` reachable **every boot whenever `/debug on` + busparams are set**, or only during an active WinDbg session? Persistent = every debug-configured instance continuously attackable (Area 3). Settle this first.
2. **KDNET key cipher semantics** — authenticated/AEAD (integrity + sender-auth) vs confidentiality-only. If confidentiality-only, key secrecy is the *sole* control and an on-path/replay attacker can inject even against a strong key (Area 2). Needs Microsoft algorithm disclosure or protocol capture.
3. **Pre-auth parsing depth** — how much outer-frame parsing runs before key validation (the key-independent attack surface size) (Area 3).
4. **Minimum enforced key entropy** — does `bcdedit`/KDNET reject trivially short keys (e.g. `a.a.a.a`), or is the doc's "up to 13" the only guardrail? (Area 2).
5. **Session-slot arbitration + VPC anti-spoofing** — first-UDP-wins vs stricter; does EC2 source/dest-check block spoofed KDNET UDP within a subnet? (Area 2 impersonation).
6. **Sysprep/AMI behavior toward `{dbgsettings}`** — does generalize/Sysprep scrub the BCD debug key, or does it propagate into AMIs? (Area 5).
7. **Code-ownership split of `kd_02_1d0f.dll`** (Microsoft core vs Amazon ENA shim) for disclosure routing (MSRC vs AWS) and patch-cadence risk (≥1-month Patch-Tuesday floor).
8. **PatchGuard/DSE/HVCI suspension** under `/debug on` — unverified; needs a primary Microsoft Windows-internals source before relying on it (Area 7).
```
