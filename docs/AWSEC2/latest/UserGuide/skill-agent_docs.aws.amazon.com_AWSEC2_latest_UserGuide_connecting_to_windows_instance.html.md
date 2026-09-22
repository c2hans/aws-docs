# Connect to Windows Instance (RDP) — Attack Research Plan

**Source of leads:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/connecting_to_windows_instance.html` (hub) and its children/near-neighbors, read from the offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` and cross-checked live 2026-09-10 (live `connect-rdp.html` is byte-identical to the mirror — corpus is current):
- `connecting_to_windows_instance.md` (hub)
- `connect-rdp.md` (RDP client path — **crown-jewel page**: `GetPasswordData`, RDP self-signed cert / `RDPCERTIFICATE-THUMBPRINT` verification)
- `connect-rdp-fleet-manager.md` (SSM Fleet Manager RDP-in-console path — bypasses security groups)
- `connect-to-linux-instanceWindowsFileTransfer.md` (RDP local drive/folder mapping — bidirectional file sharing)
- Near-neighbors pulled for mechanism: `connection-prereqs-general.md` (private key, instance fingerprint via console output), `ec2-windows-passwords.md`, `ResettingAdminPassword.md`, `connect-with-ec2-instance-connect-endpoint.md` (EICE identity-aware TCP proxy / `OpenTunnel`), `ec2-windows-security-best-practices.md`.

**Status:** documentation-derived hypotheses only. Nothing was tested against a live account. This is the plan a hunter (`aws-vuln-hunter`) executes later.

**Refresh 2026-09-20:** all four child/hub pages re-fetched live — byte-identical to mirror, plan current. Two of the three flagged doc-gaps now **closed** from the offline Service Authorization Reference (`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` and `list_ec2-instance-connect.md`) and `ExamplePolicies_EC2.md`. Net effect: the "`GetConsoleOutput` is the looser twin at the IAM layer" sub-hypothesis is **REFUTED** (the two actions have identical IAM scoping capability); the "AWS ships a `Resource:"*"` `GetPasswordData` sample" sub-hypothesis is **REFUTED** (no such sample is printed on that page); the EICE `OpenTunnel` scoping is now **concretely** established (endpoint-scoped, not instance-scoped). See the per-area "Doc-gap closure" notes and Section 8.

---

## 0. How to use this document
- Each lead is **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (SSM Fleet Manager backend, EICE proxy fleet, the console's password-decrypt helper), stop, preserve evidence, flag for AWS-Security disclosure.
- **Scope reality check.** This surface is largely a **single-account, customer-owned** control path: the caller connects to *their own* instance. The highest-value questions are therefore (a) **authorization scoping** of the data-retrieval APIs (`GetPasswordData`, `GetConsoleOutput`) — ownership vs existence, and whether an intra-account low-privilege principal can pull the admin-password ciphertext / MITM material for an instance they should not reach; (b) **AWS-authored IAM sample/managed policies** for the three connection paths (RDP-direct, Fleet Manager/SSM, EICE); (c) the **advisory-only MITM control** (self-signed RDP cert verified out-of-band against console output the user is invited to skip). Cross-*account* impact here is unlikely by design — say so where it applies rather than forcing it.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes to aim for:
1. **Retrieve the initial Administrator password ciphertext (`GetPasswordData`) for an instance the caller does not own / is not authorized for** — i.e. prove the action is gated by instance *existence* or an over-broad `Resource:"*"` grant rather than ownership + intended condition scoping. Then show the ciphertext is decryptable given the (separately obtained/weak/reused) launch key pair.
2. **Obtain the RDP MITM-defeat material** (`RDPCERTIFICATE-THUMBPRINT` and SSH host fingerprint, both delivered via `GetConsoleOutput`/"Get system log") for an instance the caller should not reach, or show the thumbprint check is advisory and trivially skipped ("choose **Yes** to connect").
3. **Reach an instance's RDP over a path that bypasses the customer's network controls** (Fleet Manager over SSM, or EICE `OpenTunnel`) using IAM that the security-group model would have blocked — and show the AWS-authored policy for that path is broader than its stated purpose.
4. **Exfiltrate local-machine files into / out of the session** via RDP drive mapping where the instance (not the operator) is the adversary — a compromised/hostile AMI reading mapped local drives.
5. **Escape the intended blast radius of a connection-path IAM policy** (privilege escalation or cross-workload instance reach) using only an AWS-authored sample/managed policy attached verbatim.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces (three connection paths + one data path):**
- **Path 1 — RDP client (direct):** operator's `mstsc`/Remmina → TCP **3389** to the instance's **public IPv4 DNS / IPv6**. Requires an inbound RDP security-group rule from the operator IP. Auth = local Windows Administrator password (or domain creds).
- **Path 2 — Fleet Manager (SSM):** AWS console → **Systems Manager Fleet Manager Remote Desktop** → RDP rendered in-console for up to 4 instances. **"You do not need to specifically allow incoming RDP traffic … Fleet Manager handles that for you"** — i.e. no inbound 3389 SG rule; reaches the instance via the SSM agent / SSM data channel. Auth = Windows/domain credentials entered into the console page.
- **Path 3 — EICE (EC2 Instance Connect Endpoint):** an **identity-aware TCP proxy**; `OpenTunnel` establishes a private tunnel authenticated/authorized by the caller's IAM entity before traffic reaches the VPC. **Max tunnel duration up to 3,600s and the tunnel persists after the IAM credentials expire.**
- **Data path — RDP local resource redirection:** RDP drive/folder mapping (`Local Resources → More → Drives`, macOS `Redirect folders`) makes the *operator's* local disks/DVD/portable/mapped-network drives visible inside the remote session (`\\tsclient`). Bidirectional file movement between local computer and instance.

**Assets:**
- **Initial Administrator password** — generated on first boot by the launch agent (**EC2Launch v2** on WS2022+, **EC2Launch** on WS2016/2019, **EC2Config** on ≤WS2012R2), **RSA-encrypted with the public half of the launch key pair**, and returned as ciphertext by `GetPasswordData`. Plaintext requires the **private key** (`.pem`), which the console/CLI decrypts **client-side**. `Password never expires` is disabled for WS2016+.
- **Launch key pair private key** (`.pem`) — the sole cryptographic gate turning the password ciphertext into plaintext. Its confidentiality/entropy/reuse is off-band to this service but is the pivot.
- **Instance fingerprint + `RDPCERTIFICATE-THUMBPRINT`** — MITM-defeat values published only in the **console output / system log** (`GetConsoleOutput`).
- **RDP self-signed server certificate** — instance-generated; not chained to any trusted CA ("publisher … unknown"); no pinning; verified only by manual out-of-band thumbprint compare.
- **Downloaded `.rdp` file** — contains public DNS hostname + Administrator username (no secret, but a targeting artifact).
- **Domain credentials** (optional) — via AWS Directory Service when the instance is domain-joined (`corp.example.com\Admin`).

**Identity / authz surfaces involved:**
- `ec2:GetPasswordData` (returns password ciphertext), `ec2:GetConsoleOutput` (returns system log incl. thumbprint/fingerprint), `ec2:DescribeInstances`, `ec2:DescribeKeyPairs`.
- SSM/Fleet Manager permissions (`ssm:StartSession`, Fleet-Manager RDP actions) — governed by the SSM User Guide, referenced but not printed here (**doc-gap — confirm exact policy from SSM docs before testing Path 2**).
- EICE: `ec2-instance-connect:OpenTunnel` with a documented max-duration condition (`permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel`).

**ASCII (Path map):**
```
                         ┌──────────────────── ec2:GetPasswordData → RSA-ciphertext blob
 operator IAM ──────────>│ EC2 control plane   ec2:GetConsoleOutput → system log (THUMBPRINT, SSH FP)
   │                     └──────────────────── DescribeInstances / DescribeKeyPairs
   │  (.pem, client-side decrypt)
   ▼
 [P1] mstsc ─TCP3389─────────────────────────> Windows instance (self-signed RDP cert)  ← SG inbound 3389 required
 [P2] console → SSM Fleet Manager RDP ────────> Windows instance                          ← NO SG rule (SSM data channel)
 [P3] client → EICE OpenTunnel (IAM proxy) ───> Windows instance                          ← identity-aware, tunnel outlives creds
        ▲ local drives redirected (\\tsclient)  ▼  session
   operator local disk  <────────────────────>  remote session (bidirectional file sharing)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal in account | Another instance's admin-password ciphertext | `ec2:GetPasswordData` on an instance id | Ciphertext returned for an instance the principal's tags/conditions should exclude → authz checks existence, not ownership/scope |
| Low-priv IAM principal | Another instance's MITM material | `ec2:GetConsoleOutput` returning `RDPCERTIFICATE-THUMBPRINT` + SSH FP | System log returned for an out-of-scope instance |
| Operator without inbound 3389 | Instance RDP | Fleet Manager (SSM) / EICE `OpenTunnel` | RDP session established with **no** security-group ingress rule; network control bypassed by an IAM-only path |
| Caller with expiring STS creds | Live RDP tunnel | EICE `OpenTunnel` max-duration | Tunnel persists **after** IAM credentials expire (up to 3600s) — revocation does not sever the session |
| Hostile/compromised **instance** (server side) | Operator's local filesystem | RDP drive redirection (`\\tsclient`) | Remote session reads/writes mapped local drives the operator exposed → client-side data theft |
| Man-in-the-middle on 3389 | Operator's RDP session | Self-signed cert + advisory thumbprint compare | Operator clicks **Yes** past the cert warning without console-log compare → credential capture / session MITM |
| Any customer surface | AWS SSM/EICE service plane | Fleet Manager backend, EICE proxy fleet | **HARD STOP** — any AWS fleet identity/credential/ARN reached from the connection path |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `GetPasswordData` | SDK/Query | Existing | Non-mut | External | Return RSA-encrypted initial admin password for an instance | Yes | IAM principals w/ `ec2:GetPasswordData` | **Crown jewel.** **CONFIRMED (auth ref):** resource type `instance*` (required — supports instance-ARN scoping, not `"*"`-only); condition keys incl. `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, `ec2:InstanceProfile`; Access level Read. Returns ciphertext; plaintext needs the `.pem`. |
| `GetConsoleOutput` | SDK/Query | Existing | Non-mut | External | Return system log incl. `RDPCERTIFICATE-THUMBPRINT` + SSH host fingerprint | Yes | IAM principals w/ `ec2:GetConsoleOutput` | MITM-defeat material lives here. **CONFIRMED (auth ref):** resource type `instance*` + condition-key set **IDENTICAL** to `GetPasswordData` (both `aws:ResourceTag`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, …), Access level Read → the two are IAM-symmetric; the "looser twin" divergence is a *customer-grant-practice* risk, not an IAM-capability one. Sibling `GetConsoleScreenshot` (`instance*`, same keys + `ec2:NewInstanceProfile`) is a third source of instance-visual data at the same scoping. |
| `DescribeInstances` / `DescribeKeyPairs` | SDK | Existing | Non-mut | External | Enumerate instance ids / key-pair fingerprints for targeting | Yes | broad | Enumeration oracle for id/key-pair guessing feeding the two above. |
| SSM Fleet Manager RDP (`ssm:StartSession` + FM actions) | SDK/console | Existing | Mutating(session) | External | RDP-in-console without SG ingress | Yes (console) | SSM-permitted principals | **Doc-gap — exact IAM from SSM UG.** Path that bypasses SG. Route policy audit to Lens R. |
| `ec2-instance-connect:OpenTunnel` (EICE) | SDK | Existing | Mutating(tunnel) | External | Identity-aware TCP proxy tunnel to 3389 | Yes | IAM w/ OpenTunnel + endpoint | Tunnel **outlives IAM creds**. **CONFIRMED (auth ref):** resource type is **`instance-connect-endpoint*`, NOT `instance`** — there is **no instance-ownership condition key**; the only destination-narrowing keys are `ec2-instance-connect:privateIpAddress`, `ec2-instance-connect:remotePort`, and `ec2-instance-connect:maxTunnelDuration` (Numeric), plus `aws:/ec2:ResourceTag` on the *endpoint*. If the customer omits the IP/port conditions, `OpenTunnel` on one endpoint reaches **any** instance/port routable from that endpoint's subnet. |
| Console "Get password" decrypt helper | Console (non-SDK) | Existing | Non-mut | **Internal-facing (browser)** | Client-side RSA decrypt of ciphertext using uploaded `.pem` | via console | console user | Confirm the `.pem` is decrypted **in-browser** and never posted to an AWS endpoint — if the private key transits to a service, that is a disclosure-grade defect. |

**Undocumented/hidden-knob sweep:** the "Administrator (Other)" localized-username selection, the `.rdp` file generator, and the console decrypt path are console-only; check whether any of them call a non-SDK endpoint that accepts an instance id / key material without the same authz as the SDK `GetPasswordData`.

---

## 5. Recommended Areas of Focus

### Area 1 — `GetPasswordData` / `GetConsoleOutput` authorization scoping (Lens A, Lens X) — **PRIORITY 1**
**Background.** The initial Administrator password is delivered as RSA-ciphertext by `ec2:GetPasswordData`; the MITM-defeat thumbprint/fingerprint is delivered by `ec2:GetConsoleOutput`. Both name an instance by id. The docs assert "You must be the instance owner to get the console output," but that is *prose* on a user-guide page, not a statement of the IAM mechanism.
**Security Concern.** If either action is granted with `Resource:"*"` (a common EC2 footgun) or checks instance *existence* rather than ownership/intended tag-condition, a low-privilege intra-account principal (or a role scoped by a tag it can dodge) can pull the admin-password ciphertext and the cert thumbprint for instances it should never reach. `GetConsoleOutput` is the softer twin *in customer grant practice* (often granted freely for "troubleshooting") and yields the exact material that defeats the RDP MITM control.

**Doc-gap closure (2026-09-20, from `list_ec2.md`).** Both actions are now confirmed to carry resource type **`instance*` (required)** and an **identical** condition-key set — `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:Tenancy`, etc. Two consequences for the hunter: (a) the **Lens X "GetConsoleOutput is the looser twin at the IAM layer" hypothesis is REFUTED** — IAM *can* scope the two identically; any real divergence is because the customer *chose* to grant `GetConsoleOutput` on `"*"`, which is a customer footgun, not an AWS defect. (b) The scoped-role test must be built on the **real keys** — pin `ec2:ResourceTag/team` or `ec2:InstanceID`, not an invented key. Cross-*account* is refuted structurally: a policy `instance` ARN embeds the caller's own account id, and neither action reaches another account's instance.
**High-level Test Scenarios.**
- **Claim:** `ec2:GetPasswordData` returns the ciphertext whenever the caller holds the action on the instance's id, with no ownership/tag re-check beyond what the attached policy expresses. → **Oracle:** under a scoped role whose policy intends to allow only `ec2:ResourceTag/team=A` instances, call `GetPasswordData` on a `team=B` instance id; a returned `PasswordData` blob (not `UnauthorizedOperation`) refutes ownership scoping. Confirm the *value* semantics: does `ec2:ResourceTag/K:"*"` (key-present) let any tagged instance through (Lens S variant)?
- **Claim (REFRAMED — IAM-symmetry now confirmed):** `GetConsoleOutput` is not *inherently* looser than `GetPasswordData` (identical resource type + condition keys), but a **customer-authored** policy commonly grants it on `"*"` for troubleshooting while scoping the password action — so the thumbprint/fingerprint leaks where the password does not. → **Oracle:** compare authz outcomes of the two actions under a role that mirrors a *realistic* grant split (password tag-scoped, console-output `"*"`); a `GetConsoleOutput` success on a foreign instance where `GetPasswordData` denies = the MITM material is reachable below the password wall. Because both can be scoped identically, this is a **customer least-privilege footgun (Low–Medium)**, not an AWS defect — do not route `aws-security`. Also test `GetConsoleScreenshot` (same scoping) as a third leak of instance-visual state.
- **Claim:** instance ids/key-pair fingerprints are enumerable enough (via `DescribeInstances`/`DescribeKeyPairs`, or structured ids) to target the above without prior knowledge. → **Oracle:** enumerate and confirm distinct not-found vs access-denied responses form an oracle. Note the embedded-checksum defense on `i-…` ids (a fabricated foreign id may be rejected outright — a genuine null, not a bug).
- **Adjacent (disclosure-timing):** the password "takes a few minutes after launch before available." Does a race or repeated poll expose the ciphertext for an instance still in a state where policy conditions (e.g., a tag applied post-launch) have not yet attached? → **Oracle:** poll `GetPasswordData` during the launch→tag window.
**Doc evidence.** `connect-rdp.md` ("Your account must have permission to call the `GetPasswordData` action"); `connection-prereqs-general.md` ("You must be the instance owner to get the console output"). **Severity-if-true.** Intra-account cross-workload admin-password/MITM-material reach = **High**; pure enumeration oracle = Low–Medium.

### Area 2 — RDP self-signed cert MITM: advisory-only thumbprint verification (Lens Y, Lens U) — **PRIORITY 1**
**Background.** The instance presents a **self-signed** RDP certificate. The only integrity control is a manual out-of-band compare of the cert **Thumbprint** against `RDPCERTIFICATE-THUMBPRINT` pulled from the system log — and the docs explicitly permit skipping it ("If you trust the certificate, choose **Yes** to connect").
**Security Concern.** There is no cert pinning, no CA chain, no `aws:SecureTransport`-style enforcement for the RDP hop. The guarantee ("confirm the identity of the remote computer") is enforced by *user diligence*, not by mechanism. An on-path attacker (rogue AP, ARP/DNS spoof on the operator LAN, BGP/route hijack toward the public DNS) can terminate RDP with any self-signed cert; the operator who clicks **Yes** hands over the Administrator password.
**High-level Test Scenarios.**
- **Claim:** nothing binds the RDP cert the client sees to the EC2-published thumbprint at protocol level — the check is 100% manual. → **Oracle:** stand up a MITM on 3389 in a lab, present an unrelated self-signed cert, confirm `mstsc` proceeds on **Yes** with no automated thumbprint enforcement.
- **Claim:** the thumbprint's *source of truth* (`GetConsoleOutput`) is itself an unauthenticated/looser control (chains to Area 1) — so even a diligent operator can be fed a spoofed thumbprint if console output is reachable/mutable by the attacker. → **Oracle:** can any principal influence the system-log content, or is it read-only fleet-generated?
- **Claim (doc-vs-enforcement):** no IAM/condition mechanism exists to *require* verified RDP transport, so the "confirm identity" promise is advisory. → **Oracle:** search the EC2 IAM reference for any RDP-transport / cert condition key; absence confirms.
**Doc evidence.** `connect-rdp.md` cert-warning step; `connection-prereqs-general.md` MITM/fingerprint section. **Severity-if-true.** Credential capture via MITM on an authenticated path = **High** (mitigant: requires on-path position; largely customer-owned network).

### Area 3 — Network-control bypass via Fleet Manager (SSM) and EICE (Lens B/C, Lens V, Lens R) — **PRIORITY 2**
**Background.** Path 2 (Fleet Manager) reaches RDP **without any inbound security-group rule** ("Fleet Manager handles that for you"). Path 3 (EICE) is an identity-aware proxy whose tunnel **persists after the caller's IAM credentials expire** (up to 3600s).
**Security Concern.** Both paths convert a *network* control (SG ingress) into an *IAM* control. If the AWS-authored policies for these paths are broader than their purpose (e.g., `ssm:StartSession` / `OpenTunnel` on `Resource:"*"` with no instance-ownership condition), an IAM principal reaches instances that the customer deliberately walled off at the network. The EICE credential-outlives-tunnel property means revoking a compromised principal's IAM does **not** kill its live RDP session — a revocation-completeness gap (Lens AA flavor).
**Doc-gap closure (2026-09-20, from `list_ec2-instance-connect.md`).** `ec2-instance-connect:OpenTunnel` is scoped to resource type **`instance-connect-endpoint*` (required), NOT `instance`**. There is **no instance-ownership condition key** on the action; the only destination-narrowing keys are `ec2-instance-connect:privateIpAddress` (IPAddress), `ec2-instance-connect:remotePort` (Numeric), and `ec2-instance-connect:maxTunnelDuration` (Numeric), plus `aws:/ec2:ResourceTag` on the endpoint. **This materially strengthens the network-bypass concern:** whether a tunnel can reach a given instance is decided by the *endpoint's subnet routing* + whatever `privateIpAddress`/`remotePort` conditions the customer bothered to add — not by instance ownership. A grant of `OpenTunnel` on one endpoint with no IP/port condition = tunnel to any 3389 reachable in that subnet.
**High-level Test Scenarios.**
- **Claim:** the Fleet Manager / SSM policy needed to RDP is not instance-scoped, so a principal can Fleet-Manager-RDP any managed Windows instance regardless of SG posture. → **Oracle:** under a scoped SSM role, start a Fleet Manager RDP session to an instance with **no** RDP ingress; success = network bypass by IAM breadth. **(Remaining doc-gap: the exact SSM Fleet-Manager RDP policy lives in the SSM User Guide, not the EC2 corpus — pull it before this test.)**
- **Claim (SHARPENED):** an `OpenTunnel` grant lacking `privateIpAddress`/`remotePort` conditions reaches instances the customer walled off, because the action binds the *endpoint*, not the target instance. → **Oracle:** hold `OpenTunnel` on an endpoint with no IP/port condition; open a tunnel to a co-subnet instance with no RDP SG ingress; success = IAM-breadth network bypass with the *endpoint* as the only resource anchor.
- **Claim:** `maxTunnelDuration` lets a tunnel outlive credential revocation (up to 3600s). → **Oracle:** open an EICE tunnel, revoke/expire the IAM creds, confirm the RDP session survives to the max duration. Severity of the *revocation gap* independent of any authz break.
- **Claim (Lens R/S):** the AWS-authored `OpenTunnel` policy / any printed EICE or Fleet Manager sample policy grants more than "tunnel to my instances." → **Oracle:** resolve `permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel` and the SSM FM policy; audit statement-by-statement with `iam:SimulateCustomPolicy` (no resources touched) for wildcard `Resource`/missing ownership condition.
**Doc evidence.** `connect-rdp-fleet-manager.md` ("You do not need to specifically allow incoming RDP traffic"); `connect-with-ec2-instance-connect-endpoint.md` (tunnel outlives creds, max-duration condition). **Severity-if-true.** IAM-breadth network bypass to foreign-workload instances = **High**; tunnel-outlives-revocation = **Medium–High**.

### Area 4 — AWS-authored IAM sample policies for the connection paths (Lens R, Lens S) — **PRIORITY 2**
**Background.** `connect-rdp.md` routes the reader to **`ExamplePolicies_EC2.md`** ("Example policies to control access to the Amazon EC2 API") for the `GetPasswordData` grant, and the EICE/SSM paths ship their own permission blocks.
**Security Concern.** These are **AWS-authored artifacts the customer copies verbatim.** A sample that grants `ec2:GetPasswordData`/`GetConsoleOutput` on `Resource:"*"`, or pairs a launch/`RunInstances` grant with an unconditioned `iam:PassRole`, is AWS's defect (in scope, Tier 2), not a customer footgun.

**Doc-gap closure (2026-09-20, from `ExamplePolicies_EC2.md`).** The page `connect-rdp.md` routes to for the `GetPasswordData` grant was read in full: it contains **no `GetPasswordData` and no `GetConsoleOutput` sample statement at all** (its topics are read-only access, Region restriction, work-with-instances, RunInstances, Spot/Reserved, tagging, IAM roles, route tables, source-instance, launch templates, instance metadata, EBS). → the **"AWS ships a `Resource:"*"` password sample here" sub-hypothesis is REFUTED.** The link is a *generic* pointer to the EC2-API access-control model, not a shipped password policy. **This narrows Area 4 to the EICE and SSM Fleet-Manager permission blocks** (which *are* AWS-authored and *do* print — audit those instead). Note the **RunInstances** and **IAM-roles** samples on this same page remain relevant to the launch/PassRole privesc surface but belong to the launch/PassRole plans, not this connect plan.
**High-level Test Scenarios.**
- **Claim (retargeted):** the AWS-published EICE `OpenTunnel` example policy (`permissions-for-ec2-instance-connect-endpoint.md`) omits the `privateIpAddress`/`remotePort` conditions, so a copy-verbatim holder tunnels to any 3389 in the endpoint's subnet. → **Oracle:** resolve that page's printed JSON; if it grants `OpenTunnel` on the endpoint with no destination condition, prove under a scoped role holding *exactly that policy* that a foreign-workload co-subnet instance is reachable.
- **Claim (Lens S semantics):** any condition block in the EICE/SSM samples binds the *endpoint*'s tag/existence rather than the target instance's ownership, or a broad statement silently overrides a narrow sibling. → **Oracle:** statement-by-statement audit; `SimulatePrincipalPolicy` as the safe first oracle.
**Doc evidence.** `connect-rdp.md` → `ExamplePolicies_EC2.md` (no password sample — refuted); EICE `permissions-for-ec2-instance-connect-endpoint.md`. **Severity-if-true.** Copy-verbatim AWS EICE policy enabling cross-workload network reach = **Medium–High**, route `aws-security`.

### Area 5 — RDP local-drive redirection: hostile-instance → operator filesystem (Lens Q) — **PRIORITY 3**
**Background.** The file-transfer page instructs operators to map local drives/folders (`Local Resources → Drives`, macOS `Redirect folders`) into the RDP session so `\\tsclient` exposes hard disks, DVD, portable media, and **mapped network drives**.
**Security Concern.** Redirection is **bidirectional and the trust flows the wrong way** if the instance is the adversary — a compromised or maliciously-published Windows AMI (or a foothold on the instance) can silently read/enumerate/write the operator's mapped local and *network* drives during the session, and harvest clipboard. The docs present this as pure convenience with no warning about exposing local data to an untrusted server.
**High-level Test Scenarios.**
- **Claim:** with default redirection, a process on the instance can read arbitrary files under the mapped local/network drives without further operator interaction. → **Oracle:** in a lab, map a local drive, then from the instance enumerate `\\tsclient\C` and read a canary file; success = client-side exfil primitive from a hostile server.
- **Claim:** mapped **network** drives extend the reach from the operator's laptop into the operator's internal file shares (lateral pivot). → **Oracle:** map a network drive, confirm instance-side reach.
**Doc evidence.** `connect-to-linux-instanceWindowsFileTransfer.md`. **Severity-if-true.** Client-side data theft / internal pivot from an untrusted AMI = **Medium** (High if the AMI is a shared/marketplace image trusted by many operators — supply-chain flavor). Owner-to-fix largely customer (operator chooses to redirect), but AWS docs omit the risk warning (Informational doc gap).

### Area 6 — Console client-side private-key decrypt integrity (Lens U, disclosure-grade check) — **PRIORITY 3**
**Background.** The console "Get password" flow has the operator **upload the `.pem`** and "Decrypt password"; the plaintext appears in-browser.
**Security Concern.** The security model *requires* the private key to be decrypted entirely client-side (in the browser) and never transmitted. If any part of the flow posts the `.pem` or its derived key to an AWS endpoint, the customer's private key transits AWS's service plane — a serious defect.
**High-level Test Scenarios.**
- **Claim:** the console decrypt is purely client-side JS; no request carries the `.pem` bytes or the plaintext password. → **Oracle:** capture browser traffic during "Decrypt password"; any request body containing the private key or plaintext = **HARD STOP**, preserve, disclose.
**Doc evidence.** `connect-rdp.md` "Upload private key file" / "Decrypt password". **Severity-if-true.** Private key transiting service plane = **Critical / hard stop**.

### Area 7 — Two-connection RDP license limit as a self-DoS lever (Lens L) — **PRIORITY 4**
**Background.** "The license … allows two simultaneous remote connections for administrative purposes. … If you attempt a third connection, an error occurs."
**Security Concern.** Any principal able to open RDP (or Fleet Manager, which displays up to 4) can hold the two admin slots, locking out legitimate operators (self/tenant-scoped DoS). Minor, single-account.
**Oracle.** Open two sessions, confirm a third is refused; check whether Fleet Manager's "up to four" bypasses the two-session administrative cap (a capability-vs-license inconsistency, Lens U). **Severity.** Low (single-tenant availability); note only.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read foreign-workload admin-password ciphertext | `GetPasswordData` authz | "You must have permission to call GetPasswordData" (prose) + presumed instance resource-level scoping |
| Read foreign-workload MITM material (thumbprint/FP) | `GetConsoleOutput` authz | "You must be the instance owner to get the console output" (prose) |
| MITM the RDP session | Self-signed cert + manual thumbprint compare | Out-of-band `RDPCERTIFICATE-THUMBPRINT` comparison (advisory; skippable) |
| Reach instance RDP with no SG ingress | Fleet Manager (SSM) / EICE | IAM permissions gate the SSM/EICE path (replaces network control) |
| Live tunnel survives credential revocation | EICE `OpenTunnel` max-duration | Operator told to set max duration < credential lifetime (advisory) |
| Hostile instance reads operator local/network drives | RDP drive redirection | None documented (operator opt-in) |
| Private key leaves the browser | Console decrypt helper | Client-side decrypt (must verify) |
| Lock out admins | 2-connection license cap | Purchase RDS CAL for >2 (availability, not security) |

---

## 7. Out-of-Scope Risk Categories
- **Weakness of the customer's launch key pair** (short/reused/leaked `.pem`) — off-band to this service; the plaintext-recovery pivot but not an EC2 defect.
- **Windows OS-level hardening** (password policy, `net user`, RDS CAL licensing, in-guest RDP config) — customer shared-responsibility.
- **On-path network position** required for the RDP MITM — attacker-precondition on the (typically customer-owned) network; report the *missing enforcement*, not the customer's LAN.
- **SSM / EICE service-plane internals** (Fleet Manager backend, proxy fleet) — **HARD STOP** if reached; do not probe AWS infra.
- **Single-tenant self-DoS** from the 2-connection cap — noted, not chased.
- **Customer-authored IAM policies** — only AWS-authored sample/managed policies (Area 4) are in scope; a customer's own over-broad grant is a footgun.

## 8. Null hypotheses / doc gaps
- **Lens F (translation/injection), H (KMS encryption-context), K (prompt injection), W (attestation):** N/A — read all four child pages + prereqs + best-practices; this is a control/connection path with no query-translation layer, no customer-KMS encryption context in the connect flow, no LLM/agent, and no attestation gate. The password RSA-encryption uses the *key pair*, not KMS.
- **Cross-account IDOR (Lens A cross-account):** unlikely by design — instances, key pairs, console output, and the connect paths are single-account resources; the realistic breach is **intra-account** cross-workload (Areas 1/3/4). Do not force a cross-account narrative.
- **Doc-gaps — status (updated 2026-09-20):**
  - ✅ **CLOSED — Resource-level + condition-key support for `GetPasswordData` / `GetConsoleOutput`:** both are `instance*` (required) with an identical condition-key set (`aws:ResourceTag`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:Tenancy`, …), Access level Read — resolved from the **offline** `list_ec2.md` (the live `list_amazonec2.html` remains JS-rendered). `GetConsoleScreenshot` is the same shape. `ec2-instance-connect:OpenTunnel` = `instance-connect-endpoint*` + `privateIpAddress`/`remotePort`/`maxTunnelDuration` keys.
  - ✅ **CLOSED — `ExamplePolicies_EC2.md`:** read in full; **no `GetPasswordData`/`GetConsoleOutput` sample exists** → the "`Resource:"*"` password sample" hypothesis is refuted; Area 4 retargeted to the EICE/SSM policy blocks.
  - ⬜ **STILL OPEN — exact Fleet Manager / SSM IAM policy for RDP:** lives in the SSM User Guide (`fleet-manager-remote-desktop-connections.html#rdp-prerequisites`), not the EC2 corpus. Pull it before the Area 3 Fleet-Manager test.
  - ⬜ **STILL OPEN — EICE `permissions-for-ec2-instance-connect-endpoint.md` printed JSON:** confirm whether the AWS-published `OpenTunnel` example omits `privateIpAddress`/`remotePort` (Area 4 retargeted claim).

---

### Priority order for the hunter
1. **Area 1** — `GetPasswordData`/`GetConsoleOutput` ownership-vs-existence scoping (crown jewel; the admin password + MITM material).
2. **Area 2** — RDP self-signed cert MITM / advisory thumbprint (chains into Area 1's `GetConsoleOutput`).
3. **Area 3** — Fleet Manager (SSM) + EICE network-control bypass and tunnel-outlives-revocation.
4. **Area 4** — AWS-authored sample-policy audit (`ExamplePolicies_EC2`, EICE, SSM FM).
5. **Area 6** — console private-key decrypt integrity (fast, high-severity-if-true).
6. **Area 5 / Area 7** — RDP drive-redirection client-side exfil; license-cap self-DoS.

**Kill-chain to compose:** Area 1 (`GetConsoleOutput` reachable below the password wall) → Area 2 (feed operator a spoofed thumbprint / operator skips check) → MITM RDP → capture Administrator password → full instance takeover, all without ever holding `GetPasswordData` or the `.pem`.
