# Isolate-Data-From-Your-Own-Operators — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/isolate-data-operators.html` (offline==online verbatim 2026-10-15, only `---source_url---` frontmatter differs); linked whitepaper `security-design-of-aws-nitro-system/no-aws-operator-access.html`; sibling Attestable-AMI cluster pages; authoritative IAM references `list_ec2.html` (35,512 ln HTML), `list_ec2-instance-connect.html` (278 ln), `list_ssm.html` (5,920 ln), and KMS `conditions-nitro-tpm.html`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

Built with the `security-questionbuilder` skill. This is the **PARENT PROSE page** of the EC2 *Attestable-AMI / isolated-compute* chapter. It is guarantee-dense and API-sparse (introduces NO new mutating EC2 API). Its value is a set of asserted security *properties* ("prevent even your own operators from accessing the EC2 instance") expressed as **5 build-time best practices**, with **zero** IAM/control-plane guidance.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (the Nitro host, hypervisor, Nitro Controller, Nitro Security Chip, or the Nitro administrative-API fleet), stop, preserve evidence, flag for AWS-Security disclosure. The entire "zero operator access" guarantee at the top of this page is that service-plane boundary — see §7.
- **Scope posture of this plan (read first):** this page's subject is a customer **isolating its own operators from its own instance**, entirely inside the customer account. There is **no cross-tenant / cross-account primitive on this page.** Every in-scope lead is one of two shapes: (i) a **Lens-U/R documentation-and-enforcement defect** in an AWS-authored artifact (the page promises operator isolation but ships no mechanism), or (ii) an **intra-account operator-defeat** where a privileged IAM principal the page claims is "locked out" defeats a build-time best practice through the EC2 / SSM / EC2-Instance-Connect control plane. The latter is largely a **customer policy-authoring footgun** — *except* where the defeat is structurally un-scopable in IAM (serial console) or where the AWS-authored artifact itself induces it (the doc gap), which lifts it to reportable.
- **Complement, not duplicate.** This parent plan OWNS the *generic* operator-defeat action class, the 5-best-practices Lens-U audit, and the page-level doc-completeness defect. It **defers** recipe-implementation specifics, measurement/reproducibility, build-time IAM, and the KMS attestation-gate mechanism to the children — cross-referenced inline:
  - recipe specifics (overlay-not-measured, serial-cmdline, user-data provide-vs-execute, IMDS omission, under-delivery vs this page's 5-item list) → `al2023-isolated-compute-recipe-attack-research-plan.md`
  - reproducible measurement / builder-asserted PCRs / build IAM (`RegisterImage *`, EBS-direct) → `attestable-ami-attack-research-plan.md` + `build-sample-ami-attack-research-plan.md`
  - KMS `kms:RecipientAttestation:NitroTPMPCR*` gate, PCR under-binding, nonce/replay, fail-open → `nitrotpm-attestation-attack-research-plan.md` + `attestation-attest`/`prepare-attestation-service`/`nitrotpm-attestation-document-validate` plans
  - drift-after-AMI-update (stale reference measurement in KMS policy) → `working-with-isolated-amis` surface

---

## 1. Pentest Objectives

Stated as concrete breach outcomes a hunter tries to produce **inside a single customer account**:

1. From a scoped "operator" IAM role (NOT account admin), **regain interactive or data access** to an instance launched from a locked-down Attestable AMI — i.e., read its data, get a shell, or read its memory-adjacent artifacts (console screenshot, password data, boot output) **without any guest-OS cooperation**, defeating best practices #1–#4.
2. **Swap or poison the "trusted" AMI/root volume** under a running or future isolated instance via a control-plane action, so the instance runs operator-controlled code while the "immutable" data volume stays readable.
3. Demonstrate that best practice **#5 ("restrict to authenticated, authorized, logged API calls") provides no backstop** — that every operator-defeat path is itself a compliant authenticated+logged API call.
4. Show the page's **operator-isolation guarantee has no AWS enforcement mechanism** and that the page omits the two load-bearing enablers (control-plane IAM lockdown + attestation verification) — a Lens-U/R documentation defect in an AWS-authored artifact.
5. (Deferred-mechanism, parent-level) Show the one AWS-native enforcement that *could* bind access to the isolated-AMI state — the KMS attestation gate — **fails open** under a default key policy. Hand the mechanism to the attestation plans.

---

## 2. Components, Assets, and Design

**What the page describes.** A customer builds a *custom Attestable AMI* configured as an "isolated compute environment" so that even the customer's **own privileged operators** cannot access the running instance or its data. Isolation is achieved by **AMI build-time content choices** (what software is / isn't in the image, how storage is mounted, what the in-guest firewall allows), optionally *proven* after the fact by NitroTPM measured boot + attestation.

**Two distinct, unrelated trust guarantees are stated in adjacent paragraphs (framing hazard — see Lead D5):**
- **Nitro "zero operator access"** — AWS firmware guarantee that no AWS system/person can log into the Nitro host, read instance memory, or read encrypted EBS/instance-store. Enforced in Nitro hardware/firmware. **AWS-infra; HARD STOP; §7.**
- **Customer-operator isolation** — customer must *build* this (AMI content) and *govern* it (IAM on the launch/management path). **In scope.** The page conflates the two by placing them back-to-back with no statement that they are different boundaries enforced by different parties.

**Assets:** the sensitive data processed in the isolated instance (on the root volume, attached EBS data volumes, instance-store, and in instance memory); the "trusted" AMI identity (its PCR measurement); any KMS-sealed secret released only to an attesting instance.

**Enforcement chain for the *proof* (established, deferred to children for depth):**

```
 Customer AMI build (KIWI NG)                     Runtime proof (optional, opt-in)
 ───────────────────────────                     ──────────────────────────────────
 best-practice content choices  ──measured──►  UKI/PCR4,7,12  ──Attestation Doc (CBOR/COSE)──►
   #1 remove interactive access   (hash of          │                                         │
   #2 only trusted code            boot bytes)       │                              ┌──────────▼───────────┐
   #4 read-only (erofs/dm-verity)                    │                              │ AWS KMS verifier     │  OR  3rd-party
   #3 in-guest firewall  ── NOT concretely          │                              │ kms:RecipientAttest  │      verifier
       implemented in sample ──────────────────────┘                              │ :NitroTPMPCR4/7/12   │  (customer-built,
   #5 restrict mgmt API ── NO mechanism, NO sample, NO link anywhere ──────────X   └──────────────────────┘   validate page)
                                                                            (structurally outside PCR scope)
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────
 CONTROL PLANE (the gap this plan attacks): EC2 / SSM / ec2-instance-connect APIs act on the instance
 REGARDLESS of AMI content or attestation. An operator IAM principal defeats #1–#4 here. ◄── IN SCOPE
```

**Resource / identity shape:** the "operator" is an ordinary IAM principal in the customer account (e.g. a role carrying broad `ec2:*` / `ssm:*` / `ec2:Get*`). The "resource" is an EC2 `instance` (ARN `arn:…:instance/i-…`) and its attached `volume`/`snapshot`. No opaque low-entropy IDs; instance IDs are the normal `i-` long form. Identity is SigV4 IAM. There is no multi-tenant service account here.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Customer "operator" IAM principal | Customer's isolated instance (guest OS / data) | EC2/SSM/EIC control-plane API | **A control-plane API call reaches a shell, the data, or an operator-chosen AMI on the instance the page claims the operator is locked out of** — proven under a scoped operator role, not admin. (In-account footgun unless un-scopable or doc-induced.) |
| Customer operator | "Immutable" EBS data volume | `CreateSnapshot`→create-volume→`AttachVolume` elsewhere | **Data read/modified off the "read-only/immutable" volume with zero interaction with the isolated instance's guest OS** (guest mount flags don't travel with the bytes). |
| Customer operator | KMS-sealed secret gated on attestation | `kms:Decrypt`/`GenerateDataKey` under default key policy | **Secret released to a principal/instance NOT satisfying `kms:RecipientAttestation:NitroTPMPCR*`** because a parallel unconditioned grant (default root statement) authorizes it. (Mechanism deferred to attestation plans.) |
| Any customer surface | AWS Nitro host / hypervisor / Nitro admin-API fleet | — | **ANY identity/credential/memory-read of the Nitro host = HARD STOP, service-plane breach. Not customer-testable.** (§7) |

---

## 4. API / Interface Inventory

This page cites **no API**. The inventory below is the operator-defeat control surface the page *fails to constrain*, confirmed against the IAM SAR. Scopability = whether the action supports a resource ARN + `aws:ResourceTag`/`ec2:ResourceTag` condition (so an org *could* fence it) or has a blank resource cell (account-wide, un-fenceable).

| Action | Service | Mutating | Resource type (SAR) | Scopable? | Defeats best practice |
|---|---|---|---|---|---|
| `ec2:EnableSerialConsoleAccess` | ec2 | yes | **blank** (only `ec2:Region`) | **NO — account-wide** | #1 (re-enables serial console for ALL instances in account) |
| `ec2:DisableSerialConsoleAccess` / `GetSerialConsoleAccessStatus` | ec2 | yes/no | blank | **NO** | #1 (toggle/status, account-wide) |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | ec2-instance-connect | yes | `instance*` | yes (tag) — **no `osuser` key for this one** | #1 (60s serial-console login key) |
| `ec2-instance-connect:SendSSHPublicKey` | ec2-instance-connect | yes | `instance*` | yes (`ec2:osuser` + tag) | #1 (push SSH key; `InstanceOSUser` is a **Required** caller field — see note) |
| `ec2-instance-connect:OpenTunnel` | ec2-instance-connect | yes | `instance-connect-endpoint*` **only (no `instance` type)** | **weakly — endpoint-ARN only; `privateIpAddress`/`remotePort` are OPTIONAL** | #1 (TCP tunnel to any private IP reachable from the EICE subnet) |
| `ec2:CreateInstanceConnectEndpoint` | ec2 | yes | `instance-connect-endpoint*`,`security-group`,`subnet*` | subnet/SG scoped | enables the EICE path |
| `ssm:StartSession` / `ssm:SendCommand` / `ssm:ResumeSession` | ssm | yes | `instance`,`managed-instance`,`document*` | yes (tag) | **#1 (interactive root shell / arbitrary command) while satisfying #5 verbatim** |
| `ec2:CreateReplaceRootVolumeTask` | ec2 | yes | `image`,`instance*`,`replace-root-volume-task*`,`snapshot` | yes (tag) | **#1+#2 at once (swap the attested AMI under a running instance)** |
| `ec2:ModifyInstanceAttribute` (userData) | ec2 | yes | `instance*` | yes (+ fine `ec2:Attribute/${AttributeName}`) | #1+#2 (rewrite user-data; next boot runs operator script as root) |
| `ec2:CreateLaunchTemplateVersion` / `ec2:ModifyLaunchTemplate` | ec2 | yes | `launch-template*` | yes (+ `ec2:Attribute/${AttributeName}`) | #2 (poison future launches via `$Latest`/`$Default` late-binding) |
| `ec2:CreateSnapshot` + `ec2:CreateVolume` + `ec2:AttachVolume`/`DetachVolume` | ec2 | yes | `snapshot*`,`volume*`,`instance*` | yes (tag) | **#4 (read "immutable" data off-instance; no guest interaction)** |
| `ec2:GetPasswordData` | ec2 | no (Read) | `instance*` | yes (tag) | leak (encrypted Windows admin password) |
| `ec2:GetConsoleScreenshot` | ec2 | no (Read) | `instance*` | yes (tag) | leak (console JPEG — on-screen secrets/login) |
| `ec2:GetConsoleOutput` | ec2 | no (Read) | `instance*` | yes (tag) | leak (boot/serial text — user-data/cloud-init output) |
| `ec2:AuthorizeSecurityGroupIngress` / `ModifyNetworkInterfaceAttribute` | ec2 | yes | `security-group*`/`network-interface*` | yes | **NOT a standalone defeat of #3** (SG ≠ guest firewall; see Area 3) |

**Note on `SendSSHPublicKey` osuser (correction to a tempting premise):** the `InstanceOSUser` field is **Required: Yes** (caller-supplied), *not* a silent default-to-root. The "defaults to root/ec2-user" lines in AWS docs are per-distro OS **username conventions**, not an API default. So the SSH-key push is to a caller-named user; still a full #1 defeat if that user exists / is privileged. (Supersedes the looser phrasing in `project_infrastructure-security-plan-note`.)

---

## 5. Recommended Areas of Focus

Priority order: Area 1 (headline doc defect, AWS-authored, reportable) → Area 2 (root-volume/AMI swap) → Area 3 (storage exfil) → Area 4 (interactive-access re-entry) → Area 5 (Lens-W KMS gate, deferred mechanism) → Area 6 (#5 is no backstop) → Area 7 (console/data leaks) → Area 8 (framing).

### Area 1 — The operator-isolation guarantee ships with NO enforcement and NO IAM guidance [Lens U / R — HEADLINE, AWS-authored, Tier-2 reportable]
**Background.** The page promises you can "prevent even your own operators from accessing the EC2 instance" and lists 5 best practices. All 5 are **guest-OS / build-time** choices. None is enforced by an AWS IAM condition key on its own terms. The property that *would* bind an operator — control-plane IAM scoping of EC2/SSM/EIC against the instance — is **best practice #5**, and the page provides **no mechanism, no sample policy, no condition key, and not one in-body link** to how to do it.
**Security Concern.** This is an **AWS-authored artifact** (a security best-practices page a customer is told to follow verbatim). A reader who implements all 5 bullets as written still leaves every operator-defeat path in §4 wide open, because bullets #1/#2/#4 are defeated from the control plane and bullet #5 as worded only guarantees the operator's action is *logged*, not *prevented*. The two load-bearing enablers — (i) IAM lockdown of the management path, (ii) wiring attestation into KMS — are each one TOC click away but **never cited in the page body** (raw-HTML link audit: the body has exactly ONE inline hyperlink, to the Nitro whitepaper; "Attestable AMIs" is not even linked to `attestable-ami.html`; the two other hrefs are prev/next TOC nav after the page footer).
**High-level Test Scenarios (falsifiable claims).**
- Claim: no page in the Attestable-AMI cluster (`isolate-data-operators`, `attestable-ami`, `al2023-isolated-compute-recipe`, `prepare-attestation-service`, `attestation-attest`, `working-with-isolated-amis`) contains a customer-facing sample IAM policy that scopes EC2/SSM management actions (`StopInstances`, `SendCommand`, `CreateReplaceRootVolumeTask`, `GetConsoleScreenshot`, `GetPasswordData`, `ModifyInstanceAttribute`) to an isolated-compute instance. → confirmed absent across the cluster in this pass; refute by finding one.
- Claim: the condition keys that *could* close most defeat paths (`aws:ResourceTag`/`ec2:ResourceTag` on `instance*`, `ec2:Attribute/${AttributeName}` on `ModifyInstanceAttribute`/launch-template) exist but are undocumented on this page → the gap is a documentation defect, not an IAM impossibility.
**Doc evidence.** `isolate-data-operators.html` body (5 bullets, 1 inline link); absence across the 6 cluster pages; SAR condition-key columns.
**Severity-if-true.** Informational/Low as a pure doc-completeness defect **but AWS-owned and reportable** (Lens R/U carve-out: the artifact is AWS-authored and copy-verbatim); real-world impact inherits whatever the misled customer fails to lock down (up to High). Cross-ref `al2023-isolated-compute-recipe` Area U-COMPLETE (the sample implements only #1+#4) — this parent plan owns the *guarantee-has-no-enforcement* framing; the recipe plan owns the *sample-under-delivers* instance.

### Area 2 — Control-plane AMI/root-volume swap defeats "only trusted code" + "remove interactive access" at once [Lens X / E / U]
**Background.** `ec2:CreateReplaceRootVolumeTask` replaces the root EBS volume of a **running** instance with a different AMI/snapshot, no stop required. `ec2:ModifyInstanceAttribute(userData)` and launch-template `$Latest`/`$Default` late-binding (`CreateLaunchTemplateVersion`/`ModifyLaunchTemplate`) redirect the code an instance (or future fleet) runs.
**Security Concern.** The "trusted, attested" AMI identity is enforced *only* at build time and (optionally) *detected* by attestation after the fact — **nothing in EC2 IAM pins "this instance may only ever run AMI X."** An operator with `CreateReplaceRootVolumeTask` boots an operator-controlled OS (sshd + known creds) on the instance while non-root data volumes stay attached and readable — defeating #1 and #2 simultaneously and setting up #4 for free.
**High-level Test Scenarios.**
- Claim: `CreateReplaceRootVolumeTask` on an isolated instance is accepted with no attestation/AMI-pinning check (only tag-scopable IAM). Oracle: in a sandbox account, launch from a locked-down AMI, attach a data volume, call `CreateReplaceRootVolumeTask` with an attacker AMI → new OS boots, data volume still attached+readable. **DryRun is caller-IAM only, NOT an ownership/attestation oracle** — needs a real canary.
- Claim: a principal with only `ec2:CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` (no `RunInstances`, no `iam:PassRole`) controls the AMI/user-data of every future `$Latest`-referencing launch. (Cross-ref the fleet $Latest late-binding leads in `ec2-fleet-instance-weighting-walkthrough` Area 2.)
**Doc evidence.** SAR `list_ec2` rows (resource types `image`/`instance*`/`snapshot`/`replace-root-volume-task*`); page's silence on any AMI-pinning control.
**Severity-if-true.** High (intra-account); it is the cleanest single-call defeat of the page's stated goal. In-account footgun, but the *absence of any pinning mechanism* is the Lens-U hook that makes it worth filing alongside Area 1.

### Area 3 — "Read-only / immutable storage" defeated off-instance via snapshot/attach [Lens X / U]
**Background.** Best practice #4 relies on guest-kernel mount semantics (`ro`, `chattr +i`, erofs/dm-verity, tmpfs overlay). Those are enforced by the instance's **own kernel**, not by EBS.
**Security Concern.** `ec2:CreateSnapshot` → `CreateVolume` → `ec2:AttachVolume` to an operator-controlled instance reads (or, after copy, alters) the "immutable" data **with zero interaction with the isolated instance's guest OS** — the read-only/immutable enforcement is never consulted because the bytes are mounted read-write elsewhere. `DetachVolume`+attach-elsewhere is the live variant.
**High-level Test Scenarios.** Claim: mount a volume `ro`/`chattr +i` in instance A; from an operator role snapshot it, create a volume, attach to instance B, mount read-write, read/modify → succeeds. Oracle = the data is read off-box. Precondition: operator holds `CreateSnapshot`+`AttachVolume` (common in broad `ec2:*`).
**Doc evidence.** SAR `CreateSnapshot`/`AttachVolume`/`DetachVolume` (`volume*`/`snapshot*`/`instance*`, tag-scopable); no EBS "immutable snapshot/lock" referenced on the page. (Cross-ref `al2023-isolated-compute-recipe` Area W1 — the overlay/dm-verity measurement scope; this plan owns the *off-instance EBS exfil* class, that plan owns the *in-guest overlay-not-measured* class.)
**Severity-if-true.** High (intra-account data exfil bypassing the stated guarantee). Note Snapshot Lock / Recycle Bin exist as EBS features but the page never invokes them → documentation gap.

### Area 4 — Interactive-access re-entry via Serial Console / EIC / SSM [Lens X / V — includes the one un-scopable control]
**Background.** Best practice #1 ("remove all interactive access") is implemented by *omitting* sshd/cloud-init/SSM-agent/EIC packages from the AMI (per the recipe). The control plane can re-introduce access paths that do not depend on those packages being present, or exploit them if present.
**Security Concern & Scenarios.**
- **Serial console (the one structurally un-scopable control):** `ec2:EnableSerialConsoleAccess` has a **blank resource cell — only `ec2:Region`** → a single grant flips serial console for **every** instance in the account/region; **no `aws:ResourceTag` scoping is possible**. SAR verbatim: "enable access to the EC2 serial console of all instances for your account." Then `ec2-instance-connect:SendSerialConsoleSSHPublicKey` (`instance*`, tag-scopable) pushes a 60s login key. Oracle: attach an `ec2:ResourceTag` condition to an `EnableSerialConsoleAccess` statement → it has no effect (no resource-level support), while the same condition on `SendSerialConsoleSSHPublicKey` does bind. (Cross-ref `al2023-isolated-compute-recipe` Area X-SERIAL: the recipe disables guest serial *login* by kernel cmdline, but the Nitro virtual-UART attach survives at the control plane — this plan owns the *account-wide un-scopability* angle.)
- **EC2 Instance Connect tunnel scoping gap:** `ec2-instance-connect:OpenTunnel` has **no `instance` resource type at all** — only `instance-connect-endpoint*` + OPTIONAL `privateIpAddress`/`remotePort`. A policy scoping EICE by endpoint ARN alone (plausible author mistake) permits tunneling to **any** private IP in that subnet, unlike `SendSSHPublicKey` which is `instance*`-scoped. Oracle: grant `OpenTunnel` on one EICE ARN, no IP condition → tunnels to multiple IPs in the subnet all succeed.
- **SSM:** if the SSM agent is in the AMI (default on Amazon-provided AL2/AL2023/Windows), `ssm:StartSession`/`SendCommand` is an interactive root shell / arbitrary exec — see Area 6 for the #5 contradiction.
**Doc evidence.** SAR `list_ec2`, `list_ec2-instance-connect`, `list_ssm`; EC2 Serial Console + EIC guides.
**Severity-if-true.** Medium–High. Serial-console un-scopability = Medium (gates a capability account-wide, impossible to tag-fence — a genuine IAM-architecture gap, not just a footgun). EIC-tunnel scoping gap = Medium–High depending on subnet layout.

### Area 5 — The AWS-native attestation gate (KMS) can fail open [Lens W — PARENT POINTER, mechanism deferred]
**Background.** The one AWS mechanism that can bind access to the isolated-AMI *state* is a KMS key policy with `kms:RecipientAttestation:NitroTPMPCR4`/`PCR7`/`PCR12` conditions (defined in KMS `conditions-nitro-tpm.html`, **not** in `list_ec2`). KMS docs state absent-attestation is denied "because this condition is not satisfied" — fail-closed **for that statement evaluated alone**.
**Security Concern.** The condition is an `Allow + Condition` grant, not a `Deny + Condition{Not…}`. The default auto-generated key policy's "Enable IAM User Permissions" statement (account root `kms:*`, no condition) plus any ordinary identity policy granting `kms:Decrypt` on the key ARN **independently satisfies KMS's same-account authorization and bypasses the attestation condition entirely.** `prepare-attestation-service.html`/`attestation-attest.html` show only the single conditioned statement and **never warn** to strip the root statement or make the attestation statement the sole grant. Classic Lens-W "over-privileged parent/root delegation defeats the gate."
**High-level Test Scenarios.** Claim: an admin/root identity path decrypts the attestation-gated secret **without** presenting an attestation document, because a parallel unconditioned grant is in force. Oracle (doc-first): confirm no KMS attestation-chapter guidance states the conditioned statement must be the *only* grant; then (live, in the attestation plan) prove a non-attesting principal decrypts.
**Severity-if-true.** High–Critical (the gate is the sole control over enclave/isolated-AMI-sealed secrets). **This parent plan only flags the pointer; the full mechanism, PCR under-binding, nonce/replay, and fail-open live oracle are OWNED by `nitrotpm-attestation` / `attestation-attest` / `prepare-attestation-service` plans — do not re-derive here.**

### Area 6 — Best practice #5 is not a backstop: every defeat is a compliant "authenticated, authorized, logged API call" [Lens U — structural]
**Background.** #5 reads: "Restrict instance access to authenticated, authorized, and logged API calls."
**Security Concern.** Every operator-defeat in Areas 2–4 and 7 **is** an authenticated, IAM-authorized, CloudTrail-logged API call (`SendCommand`, `StartSession`, `CreateReplaceRootVolumeTask`, `CreateSnapshot`, `AttachVolume`, `SendSSHPublicKey`, `GetConsoleScreenshot`). #5 as worded constrains the *shape* of access (API-call-shaped, not a shared root password) and guarantees *auditability after the fact* — it does **not** constrain *what those calls may do* and provides **no** additional permission boundary. The sharpest instance: SSM Session Manager fully defeats #1 while *literally* satisfying #5. This is the page's core internal contradiction.
**High-level Test Scenarios.** Claim: an operator role holding only `ssm:StartSession`+`ssm:SendCommand` (no console/SSH perms) gets an interactive root shell on an SSM-agent-bearing isolated instance — satisfying #5, defeating #1. Oracle: the session opens; CloudTrail logs it (compliant). Precondition: SSM agent in AMI.
**Doc evidence.** page bullet #5; `list_ssm` action descriptions; CloudTrail logging of the management event.
**Severity-if-true.** High (the stated backstop is vacuous). Doc-logic defect, AWS-authored.

### Area 7 — Console / credential leak from a "locked-out" instance [Lens A-adjacent / U, read-only]
**Background.** Three Read-level EC2 actions extract data from a running instance with zero guest interaction.
**Security Concern.** `ec2:GetConsoleScreenshot` (console JPEG — login prompts, on-screen secrets), `ec2:GetConsoleOutput` (boot/serial text — cloud-init/user-data output, stack traces), `ec2:GetPasswordData` (encrypted Windows admin password). All `instance*`, tag-scopable, but a broad `ec2:Get*`/`Describe*` operator grant (very common) reads them. The page's "isolation" says nothing about these.
**High-level Test Scenarios.** Claim: an operator with `ec2:GetConsoleScreenshot`/`GetConsoleOutput` on the isolated instance retrieves screen/boot content that leaks workload data. Oracle: non-empty screenshot/output returned.
**Severity-if-true.** Medium (info-leak; higher if secrets are on-screen/in boot output). In-account footgun; the Lens-U hook is the page's silence.

### Area 8 — Framing-misdirection: Nitro guarantee vs customer-operator isolation [Lens U, Informational]
**Background/Concern.** The page opens with the AWS-infra "zero operator access" sentence, then immediately pivots to "preventing even your own operators," in the same two-paragraph block, **with no statement that these are two different trust boundaries enforced by different parties.** A reader (or a hunter) may conflate them and either (a) over-trust the customer-side isolation as if Nitro firmware enforced it, or (b) misroute effort toward attacking the Nitro hard-stop. This is exactly the misdirection this research pass is meant to pre-empt (§7).
**Oracle.** Pure documentation-framing/clarity gap; no enforcement bug. **Severity: Informational** — AWS-owned, worth a doc note.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Operator swaps attested AMI under running instance | `CreateReplaceRootVolumeTask` | "only trusted software/code in the AMI" (#2) — no control-plane AMI pinning exists |
| Operator reads "immutable" data off-box | `CreateSnapshot`+`AttachVolume` | "read-only/immutable storage" (#4) — guest mount flags don't travel with EBS bytes |
| Operator regains shell on "no interactive access" box | `ssm:StartSession`, serial console, EIC | "remove all interactive access" (#1) + "restrict to authed/authorized/logged API" (#5) |
| Account-wide serial console re-enable | `ec2:EnableSerialConsoleAccess` | #1 — action is un-scopable (blank resource cell), no tag fence possible |
| EICE tunnel to unintended instance | `ec2-instance-connect:OpenTunnel` | #1 — no `instance` resource type; endpoint-ARN scoping only |
| Attestation-gated secret released to non-attesting principal | KMS `kms:RecipientAttestation:NitroTPMPCR*` | the attestation gate (deferred mechanism) — default root key-policy statement bypasses it |
| Workload data leaked via console/password API | `GetConsoleScreenshot`/`Output`/`GetPasswordData` | "isolation" — page is silent; broad `ec2:Get*` reads them |
| #5 provides a permission backstop | all management APIs | #5 — vacuous: every defeat is itself a compliant authenticated+logged call |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **AWS Nitro "zero operator access" (HARD STOP).** Logging into a Nitro host; reading another/any customer's instance memory; decrypting EBS/instance-store ciphertext without the customer key; bypassing the Nitro administrative-API restriction. These are firmware/hardware-enforced AWS service-plane guarantees, **not customer-testable**, and if evidence ever touches a Nitro-host identity/credential → **stop, preserve, disclose.** Do not spend hunter time here.
- **Customer-authored IAM least-privilege footguns, standalone.** Where a defeat path is fully tag-scopable (`SendCommand`, `AttachVolume`, `CreateReplaceRootVolumeTask`, `Get*`), an operator over-grant is a customer policy mistake, not an AWS defect — **except** as evidence for the Area-1 doc defect (the AWS page omits the fencing guidance) and except the structurally un-scopable serial-console triple (Area 4) which IS an IAM-architecture gap.
- **IMDS on managed hosts / credential-to-in-guest-process** — adjacent; owned by `al2023-isolated-compute-recipe` Area U-IMDS. Do not re-derive.
- **Reproducible-measurement / builder-asserted PCR / build-time code-exec / unpinned supply chain** — owned by `attestable-ami` + `build-sample-ami`.
- **KMS attestation-gate mechanism depth (PCR under-binding, nonce/replay, COSE validation, fail-open live oracle)** — owned by `nitrotpm-attestation` / `attestation-attest` / `prepare-attestation-service` / `nitrotpm-attestation-document-validate`. Area 5 here is a pointer only.
- **Guest-OS runtime integrity after boot (in-memory overlay not re-measured, TOCTOU)** — owned by `al2023-isolated-compute-recipe` Area W1 + `attestable-ami` Area 6.
- **Cross-tenant / cross-account anything** — there is no such primitive on this page; this is a single-account customer-isolation surface.
- **Single-tenant self-DoS** (e.g. customer forgets to update KMS reference measurement after root-volume replace → locked out) — availability/operational, not a breach.

---

## 8. Null hypotheses / doc gaps

- **Lens A (IDOR) — NULL.** Checked the page + the operator-defeat action set: all resources are the customer's **own** (instance/volume/snapshot in-account). No multi-tenant service account, no resource-by-foreign-ID, no cross-account naming. Not a false negative — there is simply no cross-tenant resource on this surface.
- **Lens F (translation/injection) — NULL.** No wire-protocol translator, parser, or query builder on this page.
- **Lens G (SSRF) — NULL on this page.** Checked the page body: the only dereferenced URL is the whitepaper hyperlink (doc nav, not a service-side fetch of a customer-supplied field). The IMDS/credential-bridge SSRF-adjacent surface is in the recipe (user-data / IMDS omission), owned by `al2023-isolated-compute-recipe` — not re-opened here.
- **Lens B / C (PassRole / credential vending) — NULL on this page.** No role-ARN input field, no STS/session-policy, no credential-provider field named. (The launch-path `iam:PassRole` on an instance profile is a RunInstances/launch-template concern, owned elsewhere.)
- **Lens Q (upload) — N/A** (no upload field; build-time content injection is owned by `build-sample-ami` / recipe).
- **Lens H (KMS confusion) / W (attestation)** — H deferred; W fires as Area 5 (pointer).
- **Lens I/J/M/N/O/BB/CC/DD/EE/FF — NULL** (no tagging-authz surface, no OAuth/3P, no session-id/presigned, no namespace migration, no caching/authorizer-context/edge layer, no predictable-name resolution, no JWT/OIDC on this page).
- **Lens Y (transport) — NULL on this page** (no `http://` endpoint, no TLS-floor claim, no internal-hop cert).
- **Lens EE / X variant — doc gap to settle:** does `CreateReplaceRootVolumeTask` or any launch path accept an AMI by **name** without an owner filter (whoAMI-style)? Not asserted on this page; route to the AMI-resolution surface if a hunter pursues Area 2.
- **DOC-GAPs to settle on a canary:** (1) `CreateReplaceRootVolumeTask` performs no attestation/AMI-pinning check (Area 2 — DryRun can't answer, needs canary); (2) SSM agent presence in the AMI (default-installed vs stripped) decides Area 6 reachability; (3) EBS Snapshot Lock / Recycle Bin existence vs the page's silence on them (Area 3); (4) whether the KMS attestation-chapter anywhere warns to strip the default root statement (Area 5 — doc-first, before live).

---

*Offline==online verified 2026-10-15. Companion/parent of `al2023-isolated-compute-recipe-attack-research-plan.md`; sibling of the `attestable-ami` / `nitrotpm-attestation` cluster. See those plans for measurement, build-IAM, and KMS-gate depth deliberately not restated here.*
