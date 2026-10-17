# EC2 Instance Console Screenshot Service (ICS) — Attack Research Plan

Source of leads:
- Target page: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ics-common.html (`.md` mirror) — "Common screenshots to troubleshoot unreachable Windows instances".
- Parent/feature pages: `troubleshoot-unreachable-instance.html` (Instance console output + "Capture a screenshot of an unreachable instance"), `instance-console.html`.
- API references: `API_GetConsoleScreenshot`, `API_GetConsoleOutput`, `API_GetPasswordData` (AWSEC2 APIReference mirror).
- IAM: Service Authorization Reference `list_ec2.md` + `list_ec2-instance-connect.md`; AWS-managed policies (`ReadOnlyAccess`, `PowerUserAccess`, `ViewOnlyAccess`, `SystemAdministrator`, `NetworkAdministrator`).
- Nitro trust model: *Security Design of the AWS Nitro System* whitepaper.
- Cross-reference: existing `create-key-pairs-attack-research-plan.md` (Lens T / SSM `/ec2/keypair/{id}` storage).

Status: **documentation-derived hypotheses only; nothing has been tested against a live AWS account.** Online docs were cross-checked against the local `/work/aws-docs` mirror where possible (some EC2 UserGuide pages are JS-rendered and did not return table data to WebFetch — those rest on the mirror, which carries a recent internal edit stamp and is internally self-consistent).

---

## 0. How to use this document

- Each lead follows: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity → Stop condition.** Work in priority order (§5); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — or a screenshot/console-buffer belonging to a *different tenant* captured by the shared hypervisor — **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not iterate the hypervisor/framebuffer path against live infrastructure.
- **What ICS is:** `GetConsoleScreenshot` returns a JPG screenshot of a running instance's video framebuffer (base64, ≤100 KB), captured at the **hypervisor** layer (Nitro/Xen), rendered in the EC2 console and downloadable. Its sibling read APIs `GetConsoleOutput` (boot/console log; Windows = last 3 system-event-log errors) and `GetPasswordData` (encrypted Windows admin password) share the same shape: a single required `InstanceId`, `instance*` IAM resource, Read access level. The capture is **not** performed by an in-guest agent — the exclusion list (bare-metal `*.metal`, NVIDIA GRID, Graviton/Arm, Windows on Outposts/Local Zones) is the doc evidence that a hypervisor-mediated emulated-display read does it (bare metal runs no hypervisor → no capture path).
- The target page itself (`ics-common.html`) is *troubleshooting prose* (what each Windows screen state means). The **feature mechanism** behind it is the attack surface; this plan reconstructs and targets that.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Retrieve a screenshot, console log, or Windows password of an instance in another AWS account** (cross-account IDOR). → Critical.
2. **Retrieve the same for an instance in the same account you should not have access to** (intra-account / cross-team via tag-ABAC gaps or over-broad managed policy). → Medium–High.
3. **Recover a Windows administrator password in cleartext** by chaining `GetPasswordData` (ciphertext) with the private key reachable in SSM Parameter Store (`/ec2/keypair/{id}`) under a different IAM wall. → Medium–High.
4. **Cause a guest-OS state change (wake from sleep) holding only a Read-tier permission** via `WakeUp=true`. → Medium.
5. **Establish that a screenshot/console buffer is ever bound to the wrong instance/tenant** at the hypervisor layer. → Critical / **HARD STOP** (service-plane; document, do not exploit).
6. **Confirm that an AWS-authored, uneditable managed policy (`ReadOnlyAccess`/`PowerUserAccess`) grants these sensitive reads/writes broadly**, contradicting its "safe to distribute" positioning. → High / Medium–High (Tier 2 report).
7. **Inject active content into the EC2 console UI** via unsanitized guest-controlled console output rendered in "Get system log". → Medium.

---

## 2. Components, Assets, and Design

### Customer-facing interface
- SigV4-authenticated EC2 query/JSON API on the `ec2.<region>.amazonaws.com` endpoint. Actions: `GetConsoleScreenshot`, `GetConsoleOutput`, `GetPasswordData` (+ CLI/PowerShell/SDK wrappers, EC2 console "Monitor and troubleshoot" menu).
- No non-SDK/internal-only variant was found for this family (explicitly ruled out — see §4).

### Processes / hosts / fleets behind it
- **EC2 control plane** — authorizes the call (IAM + account-scoped resource resolution), fetches the captured artifact.
- **Nitro (or legacy Xen) hypervisor** — performs the actual framebuffer read and JPG encode (≤100 KB) and the console-log buffering. Runs with privilege over the guest; this is the trust boundary of record. *Not documented publicly* — the capture mechanism is a genuine doc gap.
- **EC2 console web app** — renders the returned JPG as an image and the console log as text to the operator's browser.

### Accounts / tenancy
- Shared multi-tenant hosts (except bare-metal). A single Nitro host runs instances for multiple customers; the hypervisor reads each guest's framebuffer. This is the highest-value (and hardest-stop) finding zone: any cross-tenant framebuffer/buffer bleed is a service-plane breach.

### Resource & identifier shape
- `InstanceId` = `i-` + 17-hex suffix (post-2016), ARN `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}` — **account-scoped**. ~64 bits of ID entropy; AWS does *not* document IDs as secret/sensitive, so ID secrecy is not a relied-upon control. EC2 instances have **no resource-based policy**.

### Identity / privilege
- SigV4 IAM only. The real cross-account backstop is **control-plane account-scoped resource resolution** (a foreign `InstanceId` resolves to `InvalidInstanceID.NotFound`, not `UnauthorizedOperation`), *not* IAM policy design — an implicit, undocumented-as-a-named-control guarantee.
- Within an account, access is bound only by the IAM principal's permission + optional tag conditions. There is **no `ec2:Owner`-style "who provisioned this" condition key** on any of the three Read actions (`ec2:Owner` exists in the glossary but is not attached here).

### Untrusted data entering / transformed
- Guest framebuffer pixels → hypervisor capture → JPG encoder → base64 → console image render (Lens F memory-safety; Lens Q render side).
- Guest-written boot/console text → console-log buffer → base64 → console "Get system log" text render (Lens Q stored-XSS/terminal-escape; Lens U "owner only").
- `WakeUp=true` → simulated keystroke injected **into** the guest (a reverse data flow: customer request → guest input).

### ASCII pipeline

```
 Caller (IAM principal)
   │  SigV4: GetConsoleScreenshot / GetConsoleOutput / GetPasswordData (InstanceId[, WakeUp|Latest])
   ▼
 EC2 Control Plane ──(IAM eval + account-scoped resource resolution)──► authorize
   │                                                   ▲ InvalidInstanceID.NotFound if foreign-account
   ▼
 Nitro / Xen Hypervisor  (NO operator access per Nitro whitepaper; shared host, multi-tenant)
   │  reads guest VGA/emulated-display framebuffer  ──► JPG encode (≤100KB)
   │  buffers guest console/serial output           ──► text buffer
   │  WakeUp=true ──► injects keystroke INTO guest OS  (mutating side effect)
   ▼
 imageData / output / passwordData (base64)
   ▼
 EC2 Console web app ──► renders image / renders log text in browser
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `GetConsoleScreenshot` | EC2 API | Existing | **Read-level but `WakeUp=true` mutates guest** | External | JPG framebuffer screenshot | Yes (SigV4) | Any principal w/ `ec2:GetConsoleScreenshot` on the instance | Resource `instance*`. Condition keys incl. **extra `ec2:NewInstanceProfile`** vs siblings. `WakeUp` injects keystroke. |
| `GetConsoleOutput` | EC2 API | Existing | Non-mutating | External | Console/boot log; Win=last 3 event-log errors | Yes | Principal w/ `ec2:GetConsoleOutput` on the instance | `Latest=true` → latest serial output, **Nitro-only**. Doc guarantee: *"Only the instance owner can access the console output."* |
| `GetPasswordData` | EC2 API | Existing | Non-mutating | External | Encrypted Windows admin password | Yes | Principal w/ `ec2:GetPasswordData` on the instance | Returns **ciphertext**; decrypt needs the launch key pair's private key. Chains to Lens T. |
| `GetSerialConsoleAccessStatus` | EC2 API | Existing | Non-mutating | External | Account-level serial-console status | Yes | Principal w/ the action | **No resource type** — account/region-level only. |
| `Enable/DisableSerialConsoleAccess` | EC2 API | Existing | Write | External | Toggle serial console account-wide | Yes | Principal w/ the action | **No resource type** — all-or-nothing per account/region. |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | API | Existing | Write | External | Push SSH key for interactive serial console | Yes | Principal w/ action (tag-scoped) | **Missing `ec2:osuser`** that `SendSSHPublicKey` has (Lens X parity gap). |
| `ec2-instance-connect:SendSSHPublicKey` | API | Existing | Write | External | Push SSH key for Instance Connect | Yes | Principal w/ action | Has `ec2:osuser` (restrict login user). |

**`[NEW]` / "testing should focus on…":** none flagged on these pages. **Undocumented/console-hidden knob:** `WakeUp=true` on `GetConsoleScreenshot` is a keystroke-injection side effect not surfaced as security-relevant anywhere; `ec2:NewInstanceProfile` is accepted on `GetConsoleScreenshot` but semantically inert (§5, Lens S).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller in Account B | Instance in Account A | `GetConsoleScreenshot/Output/PasswordData` w/ foreign `InstanceId` | Any 200/imageData/passwordData for a foreign-account instance = **Critical breach**. Expected: `InvalidInstanceID.NotFound`. |
| Low-priv / "read-only" principal | Any instance in same account | Over-broad managed policy / tag-ABAC gap | Reading a screenshot/log/password of an instance the principal's intent excludes = intra-account breach (Medium–High). |
| Principal w/ `ec2:GetPasswordData` only | Windows admin cleartext | `GetPasswordData` ⨁ `ssm:GetParameter /ec2/keypair/{id}` | Recovering cleartext admin password without `ec2` key-material permission = **Lens T breach** (Medium–High). |
| Customer request | Guest OS input path | `WakeUp=true` | Guest resumes from sleep with caller holding only Read-tier IAM = access-level/boundary mismatch (Medium). |
| Guest VM (tenant A) | Guest VM (tenant B) framebuffer/buffer | Shared hypervisor capture path | A screenshot/console buffer containing **another tenant's** display = **Critical / HARD STOP** (service plane). |
| Guest-controlled console text | EC2 console operator's browser | "Get system log" render | Guest-injected bytes executing as active content / terminal escape in the console UI = Medium. |
| Any customer surface | AWS Nitro/service plane | Framebuffer capture / JPG encoder memory-safety | Any guest→host escape or service-plane credential/identity = **Critical / HARD STOP**. |

Canonical boundaries named: customer account ↔ service account (hypervisor); data plane (the instance) ↔ control plane (EC2 API auth); untrusted parsed content (framebuffer/console text) ↔ generated artifact (JPG/rendered log); caller request ↔ guest input (`WakeUp`).

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Cross-tenant framebuffer / hypervisor capture (Lens D/V/F) — **HARD STOP / OUT-OF-SCOPE to exploit**
**Background:** The screenshot is produced by the hypervisor reading the guest's emulated-display framebuffer; the console log is buffered at the same layer. On shared multi-tenant Nitro hosts, the capture path is trusted across the customer↔service boundary. AWS public docs *never* name `GetConsoleScreenshot`, a VGA/framebuffer device, or the capture mechanism — a confirmed documentation gap. The bare-metal/GRID/Graviton exclusion list is the only public evidence of the mechanism.
**Security Concern:** (a) Is the returned frame provably bound to the requested `InstanceId`'s own buffer, with no stale/co-resident reuse? (b) Memory-safety of the JPG encode/capture pipeline — the historical bug class here is real (Xen/QEMU Cirrus VGA XSA-208/CVE-2017-2615, XSA-209/CVE-2017-2620, XSA-211/CVE-2016-9603, XSA-119/CVE-2015-2152 — OOB read/write & heap overflow in emulated display device models). Nitro's minimized firmware-like hypervisor is AWS's stated mitigation, but no doc confirms the screenshot path specifically was hardened vs a legacy path.
**High-level Test Scenarios (DOC/DISCLOSURE ONLY — do not probe live infra):**
- Claim: a screenshot/console buffer can be bound to the wrong instance/tenant → Mechanism: no documented per-request identity binding or inter-tenant buffer zeroing for the display path (whitepaper's "state removed between instances" covers compute context, not explicitly display) → Oracle: requires AWS-internal review of the capture code; **not customer-testable** → Severity Critical (hypothetical). **HARD STOP.**
- Claim: the JPG encoder/capture component has a memory-safety defect triggerable by a crafted guest framebuffer → Oracle: source/binary analysis of the proprietary hypervisor; **not obtainable from docs** → Severity Critical. **HARD STOP.**
- Claim (IN-SCOPE, documentation inference, CONFIRMED): the exclusion list proves capture is hypervisor-mediated (bare metal = no hypervisor = no feature). Useful model-building; not a vuln.
**Doc evidence:** `troubleshoot-unreachable-instance` limitations list; Nitro whitepaper ("no operator access… cannot access the memory of EC2 instances"). **Severity-if-true:** Critical. **Disposition:** document as questions for AWS's own security org; preserve-and-flag on any hint of cross-tenant content.

### Area 2 — AWS-managed-policy over-grant of sensitive console reads/writes (Lens R) — **IN SCOPE, Tier 2**
**Background:** `GetConsoleScreenshot`/`GetConsoleOutput`/`GetPasswordData` expose live screen content, boot logs, and (encrypted) Windows admin passwords — credential-adjacent data. AWS ships uneditable managed policies that grant them.
**Security Concern:** A policy whose *name* implies safe-to-distribute hands out these reads/writes account-wide with no condition.
**High-level Test Scenarios:**
- Claim: **`ReadOnlyAccess`** grants all three reads unconditionally → Mechanism: statement `ReadOnlyActionsGroup1` contains wildcard `"ec2:Get*"`, `Resource:"*"`, **no Condition** → it matches `GetConsoleScreenshot/Output/PasswordData/GetSerialConsoleAccessStatus` → Oracle: `iam:SimulatePrincipalPolicy` for a principal holding only `ReadOnlyAccess` returns `allowed` for `GetPasswordData`/`GetConsoleScreenshot` on any instance ARN (no live data needed — JSON is unambiguous) → **Medium–High**.
- Claim: **`PowerUserAccess`** is strictly worse — its `NotAction:[iam:*,organizations:*,account:*]` wildcard additionally grants `ec2-instance-connect:SendSerialConsoleSSHPublicKey`/`SendSSHPublicKey` + `EnableSerialConsoleAccess` (interactive console takeover) to a "no admin" tier → Oracle: same simulate → **High**.
- Corroboration: **`ViewOnlyAccess`** *hand-curates these three OUT* (enumerates individual `ec2:Get*`/`Describe*`, omitting Screenshot/Output/PasswordData, keeps only `GetSerialConsoleAccessStatus`) → AWS's own authors treat them as sensitive → the `ReadOnlyAccess` wildcard inclusion is an unintended `Get*` consequence. `SystemAdministrator`/`NetworkAdministrator` list them by name intentionally (not a finding — baseline).
**Doc evidence:** `ReadOnlyAccess.md` (L1109–1117, 1645), `PowerUserAccess.md` (L39–45), `ViewOnlyAccess.md` (L455–475). **Severity-if-true:** High / Medium–High. **In scope** (AWS-authored, uneditable); remediation is customer-side SCP/boundary deny. **Stop:** once the simulate confirms the grant, that is the finding — do not pull real passwords.

### Area 3 — Windows-password cleartext recovery across an IAM wall (Lens T chain) — **IN SCOPE**
**Background:** `GetPasswordData` returns the **ciphertext** admin password, encrypted with the launch key pair's public key. For key pairs created via CloudFormation `AWS::EC2::KeyPair` (and the native CreateKeyPair → SSM flow), the **private key is persisted in SSM Parameter Store** as a `SecureString` at `/ec2/keypair/{key_pair_id}` under the default `alias/aws/ssm` managed key.
**Security Concern:** The ciphertext and the decryption key rest in two services under two different IAM+KMS reachabilities. A principal with `ec2:GetPasswordData` + `ssm:GetParameter --with-decryption` (and KMS decrypt satisfied via the managed key's `kms:ViaService` delegation) recovers the **cleartext** admin password with **no EC2 key-material permission**.
**High-level Test Scenarios:**
- Claim: `GetPasswordData` (ciphertext) ⨁ `ssm:GetParameter /ec2/keypair/{id}` (private key) → cleartext admin login → Oracle: under a scoped role holding only those two reads (explicitly denied `ec2:CreateKeyPair`/key export), recover and decrypt a canary instance's password in one run → **Medium–High**.
- Adjacent: deterministic/enumerable SSM path from the public `key_pair_id`; secret outliving the resource (orphaned `/ec2/keypair/{id}` after instance/stack delete).
**Doc evidence:** `GetPasswordData` API ref; `create-key-pairs.md` + existing `create-key-pairs-attack-research-plan.md` (hub Area 1 / Lens T). **Cross-reference that plan; do not restate its reachability test — this plan contributes the `GetPasswordData`-as-ciphertext-source half.** **Severity-if-true:** Medium–High.

### Area 4 — `WakeUp` keystroke injection under Read-tier IAM (Lens X twin / Lens U access-level mismatch) — **IN SCOPE**
**Background:** `GetConsoleScreenshot` is classified **Read** access level, yet `WakeUp=true` "acts as keystroke input and wakes up an instance that's in standby or 'sleep' mode" — a **mutating side effect inside the guest**, gated by no additional IAM action.
**Security Concern:** A "read-only"/monitoring principal (e.g. holding `ReadOnlyAccess`, Area 2) can force a parked guest to resume, with no write permission and no distinct audit signal.
**High-level Test Scenarios:**
- Claim: a principal with only `ec2:GetConsoleScreenshot` (no `StartInstances`/`RebootInstances`/Instance Connect/SSM) can wake a sleeping guest → Oracle: in an owned account, park a test instance in OS standby, call with `WakeUp=true` as the scoped principal, confirm resume → **Medium**.
- Claim: the wake is not distinctly auditable → Oracle: inspect the CloudTrail event's `requestParameters.wakeUp` field; confirm whether it is recorded and whether any AWS detection guidance flags it (none found) → **Low–Medium** (detection gap).
- Claim: `WakeUp` is a residual guest-input-injection path that bypasses the Serial Console's deliberate gating (account opt-in + IAM + OS password; docs call serial-console grants "equivalent to admin-level privileges") → Oracle: doc comparison — **CONFIRMED inconsistency** at doc level → Medium (defense-in-depth).
**Doc evidence:** `API_GetConsoleScreenshot` (WakeUp); `ec2-serial-console.html`. **Severity-if-true:** Medium.

### Area 5 — Console-output render side: stored XSS / terminal-escape injection (Lens Q) — **IN SCOPE**
**Background:** `GetConsoleOutput` returns guest-written boot/console text (Linux kernel/console; Windows event-log errors); the EC2 console renders it in "Get system log". The guest fully controls these bytes.
**Security Concern:** If the console UI renders console-log text without sanitization, a guest-controlled boot message (a hostname, a kernel/service log line, a crafted event-log error) could carry HTML/JS or terminal-escape sequences that execute/spoof in the operator's browser — a stored-XSS vector delivered *by the instance into the console of whoever reads its log* (including cross-account support/MSP operators with `ec2:Get*`).
**High-level Test Scenarios:**
- Claim: guest-controlled console text is rendered unsanitized → Oracle: on an owned instance, emit a benign marker (`<b>CANARYTAG</b>` / ANSI escape) to the console log, then open "Get system log" and inspect whether it renders as markup/escape vs escaped text → **Medium** (High if it executes in a cross-account operator's session).
- Screenshot side (JPG image bytes) is lower risk but confirm content-type/`Content-Disposition` on the download path (no active-content interpretation).
**Doc evidence:** `GetConsoleOutput` ("exact console output… normally displayed on a physical monitor"; Windows = last 3 system-event-log errors). **Severity-if-true:** Medium.

### Area 6 — Tag-ABAC is the only native ownership lever (Lens A/S) — **IN SCOPE (customer-controllable)**
**Background:** No `ec2:Owner`-style condition key is attached to the three Read actions. The only IAM-native way to say "my team's instances" is a tag condition (`aws:ResourceTag/${key}` / `ec2:ResourceTag/${key}`). Tags are mutable by any holder of `ec2:CreateTags`/`DeleteTags` on the instance unless a Tag Policy/SCP locks them.
**Security Concern:** Tag drift or tag-mutation by the instance's own launcher lets a principal whose policy trusts a tag read another team's screenshot/password; absent tags make `aws:ResourceTag` conditions deny-by-default, pushing teams toward broad `Resource:"*"` scoped only by coarse env tags.
**High-level Test Scenarios:**
- Claim: a principal scoped by `aws:ResourceTag/team=x` reads a password/screenshot of an instance retagged `team=x` by an unrelated role holding only `ec2:CreateTags` → Oracle: reproduce in an owned account; success proves ownership was a trusted label, not a structural bind → **Medium**.
**Doc evidence:** `list_ec2.md` condition-key lists for the three actions; `ec2:Owner` present in glossary but unattached. **Severity-if-true:** Medium. **Disposition:** tagging-governance gap (fix = Tag Policy + SCP), **not** an AWS control-plane bug — report as a documentation/guidance finding about the absence of a stronger binding.

### Area 7 — Condition-key semantics on the console-read family (Lens S) — **IN SCOPE (doc-accuracy / footgun)**
**Background / Scenarios:**
- **`ec2:NewInstanceProfile` on `GetConsoleScreenshot` (absent on its siblings):** glossary defines it as "the ARN of the instance profile *being attached*" — a **write-time request parameter** (RunInstances/AssociateIamInstanceProfile). `GetConsoleScreenshot` attaches no profile, so the key has nothing to bind to. Claim: it is inert template/doc-generation noise, not a stricter control. Oracle: an Allow with `ArnEquals ec2:NewInstanceProfile=…` → request context never contains the key → condition **fails closed → call always denied** (an availability footgun for authors who believe it scopes screenshot access; a *genuine* finding only if AWS instead evaluates it fail-open/ignore, diverging from default-deny-on-missing-key). Severity: Low exploit / Medium doc-accuracy.
- **`ec2:CpuOptionsAmdSevSnp`:** a *resource-attribute* key (is the target an SEV-SNP confidential-compute VM), not an enforced restriction. Claim: using it to "screenshot-protect confidential VMs" is misleading — SEV-SNP encrypts guest memory from the hypervisor, but `GetConsoleScreenshot` reads the hypervisor-mediated framebuffer and is **not** denied on SEV-SNP instances by default. Oracle: launch an SEV-SNP instance, call `GetConsoleScreenshot` with only the base grant, confirm it returns a real frame → the "confidential compute" framing does not extend to this API family. Severity: Medium (false sense of security; see Lens W note).
- **`ec2:ManagedResourceOperator`:** "presence of an EC2 operator provisioning a managed resource." Claim: a presence-only (`Null`) check could enable a confused-deputy across managed-service tenants. Oracle: not determinable from the Service Authorization Reference (no enumerated values). **OUT-OF-SCOPE / shared-infra** — needs the EC2 managed-resource IAM section or authorized managed-instance testing.
**Doc evidence:** `list_ec2.md` glossary + action rows. **Severity:** Low–Medium / Medium / Unknown respectively.

### Area 8 — Action-family & serial-console parity (Lens X) — **IN SCOPE**
**Background / Scenarios:**
- Screenshot vs Output vs PasswordData: condition sets are byte-identical except the inert `NewInstanceProfile` → **no real parity gap** (cosmetic). No legacy alias or lower-level cousin reaching the same bytes exists (full-file grep of `list_ec2.md` — explicitly ruled out).
- **Real gap:** `ec2-instance-connect:SendSerialConsoleSSHPublicKey` lacks the `ec2:osuser` key that its twin `SendSSHPublicKey` has. Claim: an org that scopes Instance Connect to non-root OS users has **no equivalent lever** for serial-console key push; the broader primitive (serial console, which bypasses network/security-group reachability and reaches GRUB/single-user/EMS) is *less* constrainable than the narrower one. Oracle: build identical-intent policies ("push key for ec2-user only"); the regular one enforces via `StringEquals ec2:osuser`, the serial variant has no such key (confirmed `list_ec2-instance-connect.md`). → **Medium–High**.
- Serial console enable/disable/status have **no resource type** — account/region-wide, strictly coarser than per-instance screenshot scoping. A principal holding `GetPasswordData` + unconstrained `SendSerialConsoleSSHPublicKey` has a materially larger blast radius than screenshot-only. → **Medium–High**, in-scope (no IAM lever to narrow further than tag; compensate by not granting broadly).
**Doc evidence:** `list_ec2.md`, `list_ec2-instance-connect.md`, `ec2-serial-console.html`.

### Area 9 — "Only the instance owner can access" — enforcement vs guarantee (Lens U) — **IN SCOPE baseline / HARD-STOP edges**
**Background:** `GetConsoleOutput` docs assert *"Only the instance owner can access the console output."* No verbatim equivalent is stated for `GetConsoleScreenshot` (same model implied, not restated).
**Security Concern:** The guarantee rests on **control-plane account-scoped resource resolution** (foreign `InstanceId` → `InvalidInstanceID.NotFound`), an implicit, undocumented-as-a-named-control behavior — *not* a special per-API control. The docs do not enumerate edge cases (RAM sharing — EC2 instances are generally not RAM-shareable; Organizations/delegated-admin; cross-account `ec2:Get*` via StackSets).
**High-level Test Scenarios:**
- Claim (baseline, IN-SCOPE, owned accounts): a maximally permissive `ec2:*` principal in Account B cannot read Account A's instance console → Oracle: confirm `InvalidInstanceID.NotFound` (not `UnauthorizedOperation`) → Informational baseline. Any success = Critical / HARD STOP.
- Claim: "owner" = the **account**, so *any* in-account principal with the Read action (e.g. via `ReadOnlyAccess`, Area 2) sees live screen content/secrets — and AWS IAM best-practice/security-reference pages do **not** list `GetConsoleScreenshot`/`GetConsoleOutput`/`GetPasswordData` among sensitive actions (unlike `secretsmanager:GetSecretValue`/`kms:Decrypt`) → Oracle: doc search, confirmed absence → **Medium** guidance gap.
- Claim: `GetConsoleOutput` leaks cloud-init/user-data secrets if the AMI echoes them at boot → Oracle: launch with verbose non-secret user-data, confirm it appears → **Medium** (shared-responsibility hygiene).
**Doc evidence:** `troubleshoot-unreachable-instance` / `instance-console`; `ec2-api-permissions.html`. **Severity:** Informational baseline; Medium guidance gaps; Critical only if a customer-reachable cross-account sharing primitive is found (then HARD STOP).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account screenshot/log/password read | EC2 control plane | Account-scoped resource resolution (implicit); confirm `NotFound` not `Unauthorized` |
| Cross-tenant framebuffer/buffer bleed | Nitro hypervisor | Nitro "no operator access / no cross-instance memory" (HARD STOP to test) |
| JPG-encoder / capture memory-safety | Hypervisor display path | Minimized Nitro hypervisor (HARD STOP) |
| "Read-only" principal reads passwords/screenshots | IAM / managed policies | `ReadOnlyAccess`/`PowerUserAccess` over-grant (Tier 2) vs `ViewOnlyAccess` curation |
| Windows password cleartext recovery | GetPasswordData + SSM | Key-pair private key in `/ec2/keypair/{id}` SecureString; IAM separation |
| Guest wake via Read-tier IAM | GetConsoleScreenshot `WakeUp` | None documented (access-level mismatch) |
| Stored XSS via console log | EC2 console render | Output sanitization (unverified) |
| Tag-ABAC ownership bypass | IAM tag conditions | Tag Policy / SCP immutability (customer) |
| Serial-console over-reach | ec2-instance-connect | `ec2:osuser` (absent on serial variant) |
| SEV-SNP "confidential" screenshot | Hypervisor + IAM | None — framebuffer read not denied on SEV-SNP |

---

## 7. Out-of-Scope Risk Categories

- **Shared Nitro/Xen hypervisor internals** — framebuffer capture binding, buffer zeroing, JPG-encoder memory safety (Area 1 Q1.1/Q1.2): service plane. Document and flag for AWS disclosure; **never probe live**.
- **`ec2:ManagedResourceOperator` semantics** — AWS managed-service operator trust; undeterminable from docs.
- **Probing arbitrary/foreign `InstanceId`s** against accounts you do not own — unauthorized access against third parties even if expected to fail. Own-account ID sampling only.
- **Instance-ID entropy** as a primary control — AWS does not treat IDs as secret; relevant only as dependent defense-in-depth if Area 9 baseline ever fails.
- **Customer AMI/user-data hygiene** (secrets echoed to console) — shared responsibility; note, don't own.
- **Customer-authored tag policies / least-privilege composition** — Area 6/7 footguns are customer-fixable, reported as guidance not AWS defects. (Carve-out: the **AWS-managed** `ReadOnlyAccess`/`PowerUserAccess` over-grants in Area 2 **are** in scope — Tier 2.)
- **DryRun as an existence/ownership oracle** — `DryRun=true` validates caller IAM only (`DryRunOperation` vs `UnauthorizedOperation`), evaluated *before* resource resolution; it returns `DryRunOperation` for a non-existent/not-owned instance given sufficient IAM. **Do not use it as an IDOR oracle** (documented negative result).

---

## 8. Null Hypotheses / Doc Gaps

- **Lens G (SSRF):** N/A — read `API_GetConsoleScreenshot/Output/PasswordData`, `troubleshoot-unreachable-instance`, `instance-console`; no field the service dereferences/fetches. No URL/URI/callback input.
- **Lens J (OAuth/3P), K (prompt injection), N (namespace migration), P (proofing/registration), AA (share/revoke), BB (canonicalization/multi-parser), CC (trusted-upstream header), DD (cache-key), EE (predictable-name), FF (JWT/token):** N/A — no such mechanism on these pages (SigV4 IAM only, single-API path, no tokens/LLM/registration/caching/global-namespace resolution).
- **Lens B/C (PassRole/credential vending):** N/A for confused-deputy — these APIs take no role ARN and vend no session. The `InstanceProfile`/`NewInstanceProfile` keys are resource attributes, routed to Lens S.
- **Lens H (KMS context):** minimal — `GetPasswordData` encrypts with the EC2 key pair, not a CMK; the only KMS angle is the SSM managed-key delegation in Area 3 (Lens T). `ec2:CpuOptionsAmdSevSnp` handled in Lens W/S.
- **Lens L (DoS):** low — screenshot ≤100 KB, no data-transfer cost; `WakeUp` spam and shared-capture-pipeline contention are single-tenant/noisy-neighbor and largely out of scope.
- **Lens Y (transport):** standard SigV4 over the EC2 TLS endpoint; no `http://` path or legacy signature documented. N/A.
- **Doc gaps (confirm surface first):** (1) the **capture mechanism** is undocumented — Area 1 cannot be escalated past doc review without AWS-internal access. (2) Whether the EC2 console **sanitizes** rendered console-log text (Area 5) is not documented — confirm against the live console UI in an owned account. (3) Whether `GetConsoleScreenshot` is **denied on SEV-SNP** instances (Area 7) is not stated — confirm live in an owned account. (4) `requestParameters.wakeUp` presence in CloudTrail (Area 4) — confirm live.

---

### Priority order for the hunter
1. **Area 2** (managed-policy over-grant) — pure IAM/JSON + `SimulatePrincipalPolicy`, no live data, highest-confidence, Tier 2 reportable.
2. **Area 3** (Windows password cleartext via SSM) — concrete cross-service chain, canary-testable.
3. **Area 4** (`WakeUp` under Read-tier) + **Area 5** (console-log XSS) — cheap owned-account confirmations.
4. **Area 8/7/6** (serial-console parity, condition-key semantics, tag-ABAC) — IAM-reasoning + targeted live checks.
5. **Area 9** baseline (cross-account `NotFound`; DryRun non-oracle) — establishes the boundary and prevents wasted effort.
6. **Area 1** (hypervisor/framebuffer) — **documentation/disclosure only; HARD STOP on any live signal.**

*Kill-chain note:* Area 2 (a "read-only" principal holds `GetPasswordData`) → Area 3 (that principal also has `ssm:GetParameter` on `/ec2/keypair/*`) → **cleartext Windows admin password from a nominally read-only role** — rate at the end of the chain (High).
