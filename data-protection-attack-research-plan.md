# EC2 Data Protection — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/data-protection.md`, 96 lines; online==offline verbatim, cross-checked 2026-10-15). Child/sibling pages read: `snp-find-instance-types.md`, `snp-attestation.md`, `snp-work-launch.md`, `ebs/latest/userguide/how-ebs-encryption-works.md` + `ebs-encryption.md`, `vpc/latest/userguide/vpc-encryption-controls.md`, `tgw-encryption-support.md`, `ec2-security.md` (parent chapter). Condition-key ground truth: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines; EC2 condition-key table lines 10036–10190). Global keys: `IAM/.../reference_policies_condition-keys.md`.

Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Positioning in the corpus.** This is the FIRST plan covering the EC2 *Security* chapter's **data-protection** page (prior plans were all EC2-Networking and Fleet/Spot-Fleet). `data-protection.html` is a template-driven, **guarantee-dense / API-sparse** security-chapter page: its value is almost entirely a set of asserted security *properties* (encryption at rest / in transit / in memory). The dominant lenses are therefore **U** (documented-guarantee-vs-enforcement + doc-vs-API integrity), **H** (KMS), **W** (attestation), **Y** (transport), **S** (condition-key semantics), with **A/X/V** firing only as *hard-stop* AWS-infrastructure reuse-isolation claims. There is **no cross-tenant customer-testable primitive on this page** — the realistic deliverables are IAM-enforcement gaps (copy-path KMS-key pinning, fail-open condition-key naming) and compliance/attestation-assurance gaps, routed `aws-security` as Tier-2 where AWS-authored, or flagged out-of-scope where they are AWS-infra claims.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **Safe-first oracles:** every IAM-enforcement lead here is settleable **read-only** with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (a condition key either applies to an action/resource or it does not) — **no resource is created and no live mutating call is needed to confirm the gap.** Prefer this before any live call.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — or any test would require probing AWS's shared storage media / backbone / Nitro hardware internals — stop, preserve evidence, flag for AWS-Security disclosure. The at-rest reuse-isolation and in-transit physical-layer guarantees (Areas R1, R4, T2, T3, T5) are all in this class.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove an IAM enforcement gap on the EBS encryption key choice:** demonstrate (via policy simulation) that an admin **cannot** pin which KMS key is used on the `CopySnapshot` / `CopyVolumes` / `RunInstances`-inline-volume paths, so a holder of `CopySnapshot` + KMS `Encrypt/Decrypt/GenerateDataKey*`/`CreateGrant` on an attacker key can re-encrypt a legitimately-encrypted snapshot under a key the origin org cannot restrict.
2. **Prove a fail-open condition-key naming hazard:** demonstrate that a plausibly-guessed policy (`ec2:AmdSevSnp`) silently never evaluates, while the real key is `ec2:CpuOptionsAmdSevSnp` — a "require confidential compute" Deny that fails open.
3. **Prove a compliance/attestation gap on inter-instance encryption:** demonstrate the page's static instance-type list drifts from the authoritative `NetworkInfo.EncryptionInTransitSupported` API, and that the encryption silently drops to cleartext (no customer-visible signal, absent opt-in VPC Encryption Controls) when traffic traverses an in-path LB/TGW/virtual device.
4. **Establish the SEV-SNP attestation scope boundary:** confirm there is **no** AWS IAM/KMS attestation condition key tying SEV-SNP state to any authorization decision — so a "decrypt only if attested" control must be customer-built, and any fail-open there is the customer's, not AWS's.
5. **Delimit the hard-stop surface:** EBS block-zeroing-before-reuse, instance-store block-reset-on-stop, NVMe hardware-key isolation, and physical-layer/AZ/cross-Region/Outposts encryption are AWS-infra claims — document the breach oracle **and** the hard stop so the hunter never probes shared infra.

---

## 2. Components, Assets, and Design

The page asserts guarantees across three data states. No new API is introduced *by the page itself*; the relevant control-plane actions live in EC2, EBS, KMS, and VPC.

```
 Customer                    EC2 control plane (IAM/SigV4/TLS1.2+)         AWS-owned infra (HARD STOP)
 ────────                    ─────────────────────────────────────        ───────────────────────────
 RunInstances ─┐
 CreateVolume ─┼─► EBS volume ──(AES-256 data key, wrapped by KMS key)──► EBS storage media
 CopySnapshot ─┤        │                                                  └─ "zeroed/pseudorandom before reuse" (R1)
 CopyVolumes  ─┘        │  ec2:Encrypted ✔  ec2:KmsKeyId ✔ create / ✘ copy+runinstances (R2/R3)
                        │
 RunInstances(--cpu-options AmdSevSnp=enabled) ─► instance
                        ├─ NVMe instance store: XTS-AES-256, per-customer/vol HW key, no BYOK, no disable (R4/T-nvme)
                        │     └─ block reset on stop/hibernate/terminate (R4 cross-tenant, HARD STOP)
                        ├─ Memory encryption always-on: Graviton2+/Intel TME/AMD SME/AMD SEV-SNP (R5)
                        │     └─ SEV-SNP attestation: snpguest → AMD KDS (VCEK/VLEK) — customer-only, NO AWS IAM/KMS gate (R6)
                        │
 instance ◄──► instance : Nitro AEAD-256 "encryption between instances" (T1)
    │   requirements: capable type (NetworkInfo.EncryptionInTransitSupported) + same Region + same/peered VPC + NO in-path LB/TGW
    │   silently OFF otherwise; per-flow signal only via opt-in VPC Encryption Controls flow-log encryption-status (T1)
    │
 cross-Region VPC-peering / TGW-peering ─► bulk-encrypted on Region exit (T3, HARD STOP infra)
 all AZ / cross-Region backbone ─► physical-layer encryption (T2, HARD STOP infra)
 Outposts service links ─► fully encrypted (T5, out-of-scope pointer)
 SSH/RDP/app traffic ─► CUSTOMER responsibility (no AWS enforcement); SSM Session Manager = TLS1.2+SigV4+IAM (T4)
```

**Identity / control model:** EC2 control-plane actions are SigV4/IAM-authed over TLS≥1.2 (enforced by endpoint construction, not an IAM condition). The instance **data plane** (SSH/RDP/application) is **not** IAM-authed — "require TLS 1.2" does not reach it. EBS encryption key choice is the one customer-controllable at-rest lever; instance-store and memory encryption are hardware-fixed with no customer control and no attestation (except SEV-SNP, which has customer-only attestation).

**Assets:** EBS volume/snapshot plaintext; instance-store (ephemeral NVMe/HDD) plaintext; instance memory; inter-instance network traffic; the KMS keys wrapping EBS data keys.

---

## 3. API / Interface Inventory

| Name | Mutating | Ext-facing | Functionality | Authorized callers | Notes (relevance) |
|---|---|---|---|---|---|
| `CreateVolume` | Y | Y | create EBS vol | account IAM | **has `ec2:Encrypted` AND `ec2:KmsKeyId`** (baseline — key pinnable here) |
| `CreateFleet` (launch-spec volume) | Y | Y | fleet launch vols | account IAM | has `ec2:Encrypted` + `ec2:KmsKeyId` |
| `RunInstances` (inline `volume`) | Y | Y | launch + block-device-mappings | account IAM | has `ec2:Encrypted`, **NO `ec2:KmsKeyId`** (R3) |
| `CopySnapshot` | Y | Y | copy snapshot, can re-key | account IAM | has `ec2:Encrypted`, **NO `ec2:KmsKeyId`** (R2 headline) |
| `CopyVolumes` | Y | Y | copy volume, can re-key | account IAM | has `ec2:Encrypted`, **NO `ec2:KmsKeyId`** (R2 twin, Lens X) |
| `CopyImage` | Y | Y | copy AMI | account IAM | **NO encryption condition keys at all** (doc-gap — may be by-design) |
| `CreateSnapshot` / `AttachVolume` | Y | Y | snapshot / attach | account IAM | `ec2:Encrypted` only; no `ec2:KmsKeyId` **by design** (no new key chosen) — null |
| `EnableEbsEncryptionByDefault` / `Disable…` / `GetEbsEncryptionByDefault` / `GetEbsDefaultKmsKeyId` | Y/N | Y | account-level EBS default | account IAM | **no condition keys** — account-wide toggle, not per-principal/request (R3 context) |
| `RunInstances` / `AllocateHosts` `--cpu-options AmdSevSnp=enabled` | Y | Y | enable SEV-SNP (launch-only) | account IAM | gated by **`ec2:CpuOptionsAmdSevSnp`** (list_ec2:10065); only us-east-2 & eu-west-1 |
| `DescribeInstances` (`.CpuOptions`) | N | Y | read SEV-SNP state | account IAM | **console does NOT show it** (R6 audit gap) |
| `DescribeInstanceTypes` (`network-info.encryption-in-transit-supported`, `processor-info.supported-features=amd-sev-snp`) | N | Y | capability discovery | account IAM | the authoritative oracle; **console shows neither** (T1 / R6) |
| `GetConsoleOutput` / `GetConsoleScreenshot` | N | Y | boot log / screenshot | own `instance*` only | **detection surface** for a reuse-isolation breach (R4); correctly scoped — null |
| `GetInstanceTpmEkPub` | N | Y | NitroTPM EK pubkey | own `instance*` | key-retrieval, NOT attestation-verification; no attestation gate (R6) |
| `CreateVpcEncryptionControl` / `Modify…` / `DescribeVpcEncryptionControls` / `GetVpcResourcesBlockingEncryptionEnforcement` / `Delete…` | Y/N | Y | opt-in inter-instance encryption enforce/monitor | account IAM | **NOT mentioned on data-protection.html** (T1 doc-fragmentation finding) |

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Scoped IAM principal (copy perms + KMS on attacker key) | Legitimately-encrypted snapshot's plaintext | `CopySnapshot`/`CopyVolumes` re-key to attacker KMS key | **A copy succeeds under a KMS key the origin org's EC2 IAM policy could not restrict** (no `ec2:KmsKeyId` to pin) → attacker now holds a copy decryptable by their key |
| Policy author guessing `ec2:AmdSevSnp` | "Require confidential compute" gate | Deny-unless-condition on a non-existent key | **A launch WITHOUT SEV-SNP is permitted** despite the intended Deny (gate fails open) |
| Any workload able to insert an LB/TGW in path | "Nitro-encrypted" inter-instance traffic | in-path virtual network device | **Traffic silently drops to unencrypted with no customer-visible signal** (absent opt-in VPC Encryption Controls flow-log `encryption-status`) |
| Customer compliance control | "always-on memory encryption" / instance-store HW encryption | — | **No API/attestation field exists** to verify the claim (prose-only; SEV-SNP is the sole exception, and its attestation is customer-only) |
| Any customer surface | EBS storage media reuse / instance-store block reset / AWS backbone encryption | shared-infra reuse / physical layer | **Reading another tenant's residual bytes, or AWS-fleet encryption state = HARD STOP, AWS service-plane** |

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### R2 — [HEADLINE, Lens H + X] EBS copy/launch path cannot pin the KMS key (`ec2:KmsKeyId` omission)
**Background.** EBS encryption is KMS-backed; `ebs-encryption.md`: *"You cannot change the KMS key associated with an existing snapshot or volume. However, you can associate a different KMS key during a snapshot copy operation."* So the copy path is the one place a key is (re)chosen.
**Security Concern.** `list_ec2.md` exposes `ec2:KmsKeyId` on `CreateVolume` and `CreateFleet`(launch-spec volume), but **NOT** on `CopySnapshot` (snapshot* block: `ec2:Encrypted, ec2:OutpostArn, ec2:Owner, ec2:ParentSnapshot, ec2:ParentVolume, ec2:ProductCode, ec2:SnapshotID, ec2:SnapshotTime, ec2:VolumeSize`), **NOT** on `CopyVolumes` (volume* block likewise lacks it), and **NOT** on `RunInstances`'s inline `volume` resource type. The create-path has the key, the copy/launch-path does not — a **systemic copy-path schema gap** (Lens X: a write-twin/clone cousin missing a control its sibling has), not a one-off.
**High-level Test Scenarios.**
- Claim: An org **cannot** author an EC2 IAM/SCP condition that forces "copied snapshots must be re-encrypted only under KMS key X." → **Oracle:** `iam:SimulateCustomPolicy` action=`ec2:CopySnapshot`, resource=snapshot ARN, context `ec2:KmsKeyId=<any>` — the condition is reported *not applicable* to the action (key absent from its condition set). Repeat for `ec2:CopyVolumes` and `ec2:RunInstances`(volume). Read-only, zero resources.
- Claim: a holder of `CopySnapshot` + `kms:Encrypt/Decrypt/GenerateDataKey*`+`kms:CreateGrant` on an attacker-controlled key can produce a copy of a legitimately-encrypted snapshot decryptable by that key, and **EC2 IAM cannot stop the key choice** (only the KMS key *policy* of the destination key can — a different control plane). → confirm the gap by simulation only; **do NOT run a live CopySnapshot with a hostile key** (live-account mutation, out of scope).
**Doc evidence:** `list_ec2.md` CopySnapshot/CopyVolumes/CreateVolume/RunInstances condition-key blocks; `ebs-encryption.md` re-key-on-copy sentence. **Severity-if-true:** Medium–High (defense-in-depth / key-pinning gap on the most common re-encryption path; AWS-owned IAM-schema gap → Tier-2 hardening report, `aws-security`). **Stop condition:** gap confirmed by simulation; no live copy.

### R6 — [HEADLINE, Lens S/U] `ec2:AmdSevSnp` does not exist → "require confidential compute" fails open
**Background.** SEV-SNP is enabled launch-only via `--cpu-options AmdSevSnp=enabled` (`snp-work-launch.md`: *"You can't enable AMD SEV-SNP after launch"*). The console label is "AMD SEV-SNP"; the CLI param is `AmdSevSnp`.
**Security Concern.** The **real** IAM condition key is **`ec2:CpuOptionsAmdSevSnp`** (`list_ec2.md:10065`, *"only US East (Ohio) and Europe (Ireland) are supported"*), present on `RunInstances`/`CreateFleet`(instance*)/`AttachVolume`/`GetConsoleOutput`/`GetConsoleScreenshot`/`GetInstanceTpmEkPub` etc. **`ec2:AmdSevSnp` (the plausibly-guessed name) does NOT exist anywhere in `list_ec2.md`.** A `Deny` structured as `"Condition":{"BoolIfExists":{"ec2:AmdSevSnp":"false"}}` never sees the key → vacuously true → **Deny does not fire → launch without confidential compute is permitted** (fails open). This is the Lens-S "condition key that does not exist / is silently ignored" shape.
**High-level Test Scenarios.**
- Claim: a policy keyed on `ec2:AmdSevSnp` is a silent no-op; only `ec2:CpuOptionsAmdSevSnp` evaluates. → **Oracle:** `iam:SimulateCustomPolicy` on `ec2:RunInstances` with context `ec2:AmdSevSnp=true` (no match) vs `ec2:CpuOptionsAmdSevSnp=true` (matches). Read-only.
- Adjacent: confirm the regional constraint — the key only governs us-east-2 / eu-west-1; in other Regions even the correct key cannot gate (enforcement-coverage gap).
**Doc evidence:** `list_ec2.md:10065`; `snp-work-launch.md`. **Severity-if-true:** High for any org that authored the guessed-name policy (silent fail-open on a confidential-compute mandate). Framed as a **doc/naming hazard** (AWS's own link text is correct; risk is customer policy-authors guessing from the console/CLI label). **Stop condition:** simulation confirms; no live launch.

### T1 — [HEADLINE, Lens U + V] Inter-instance Nitro encryption: static list drift + silent downgrade + undocumented enforcement layer
**Background.** `data-protection.md:65–76`: some types auto-encrypt inter-instance traffic (AEAD-256) **iff** capable type + same Region + same/peered VPC + **no in-path virtual network device (LB/TGW)**. The page hardcodes ~130 type names and gives the CLI oracle `describe-instance-types --filters Name=network-info.encryption-in-transit-supported,Values=true`.
**Security Concern (three sub-findings).**
1. **Doc-vs-API drift (Lens U integrity).** The static list shadows the authoritative Boolean `NetworkInfo.EncryptionInTransitSupported` (`API_NetworkInfo.md`; filter name confirmed in `API_DescribeInstanceTypes.md`). A security team scoping "encryption-eligible" fleets off the prose list risks false negatives (new types) / false positives (deprecations).
2. **Silent conditional downgrade (Lens V).** Encryption is **not a property of the instance** — it drops to cleartext, with **no application-visible signal**, the moment traffic transits an ALB/NLB/GWLB/Transit Gateway or crosses non-peered VPC / Region boundaries. `tgw-encryption-support.md` documents the boundary-drop verbatim. An attacker who can get flows routed through *any* in-path virtual device inside an otherwise "encrypted" VPC achieves a silent downgrade.
3. **Undocumented enforcement/attestation layer (Lens U doc-fragmentation — NET-NEW).** **VPC Encryption Controls** (`CreateVpcEncryptionControl`/`ModifyVpcEncryptionControl`/`DescribeVpcEncryptionControls`/`GetVpcResourcesBlockingEncryptionEnforcement`, `vpc-encryption-controls.md`) add a per-flow VPC-Flow-Logs field **`encryption-status`** (`0`=not encrypted, `1`=nitro, `2`=application, `3`=both, `(-)`=unknown/off) and an **enforce mode** that blocks ENI attach to non-capable instances. This is the one control that would *close* the gap the page implies — but **`data-protection.html` never links or mentions it** (link is one-way, VPC-doc → EC2-page). Default posture of essentially every existing VPC is `(-)` (no attestation).
**High-level Test Scenarios.**
- Diff oracle (read-only, safe): `describe-instance-types --filters Name=network-info.encryption-in-transit-supported,Values=true` vs the ~130 names parsed from `data-protection.md:67–72` → list any doc-only / API-only entries (Info/Low drift).
- Default-state oracle (read-only, safe): `describe-vpc-encryption-controls` on a VPC that never called `CreateVpcEncryptionControl` → confirm absent/`(-)` → prove the default is zero attestation.
- Enforcement-gap oracle (**HARD STOP for doc-only phase** — needs live authorized VPC): insert an NLB/TGW between two capable instances, compare flow-log `encryption-status` before/after.
**Doc evidence:** `data-protection.md:64–86`; `API_NetworkInfo.md`; `API_DescribeInstanceTypes.md:55`; `vpc-encryption-controls.md`; `tgw-encryption-support.md`. **Severity-if-true:** Medium — not an AWS product bug but a **high-value compliance/attestation finding**: orgs citing "Nitro encrypts instance traffic" as a compensating control (in lieu of app-layer TLS) have an unverified, frequently-false claim unless they query the API, enable VPC Encryption Controls, and audit for in-path devices. **Stop condition:** drift + default-state confirmed read-only; topology downgrade test deferred to live phase.

### T4 — [Lens Y] "We require TLS 1.2" is control-plane only; no TLS-version / signature-version condition key
**Background.** `data-protection.md:12`: *"We require TLS 1.2 and recommend TLS 1.3"*; `:92` SSM Session Manager/Run Command = TLS 1.2 + SigV4 + IAM; `:94` *"It is your responsibility to use … TLS … between clients and your Amazon EC2 instances."*
**Security Concern.** The TLS-1.2 "requirement" is enforced by **endpoint construction** (every SDK/CLI call to `ec2.<region>.amazonaws.com` is already HTTPS), not by any IAM condition. `aws:SecureTransport` **is** a valid global key usable in an EC2 `Deny` (`reference_policies_condition-keys.md:2166`) but has no teeth (no plaintext EC2 control-plane endpoint to catch). **No `aws:TlsVersion` and no `aws:SignatureVersion` key exists** (absent from both `list_ec2.md` and the global key index) → an org **cannot** express "minimum TLS 1.2 vs 1.3" or "SigV4-only" on EC2 actions. The **data plane (SSH/RDP/app) is entirely outside the guarantee** — not IAM-authed, so no condition can ever apply; the clarifying sentence (`:94`) is 80 lines away from the bullet (`:12`) under a different heading → easy to misread as covering instance traffic. SSM Session Manager is the one remote-access path where "TLS 1.2" is actually IAM-governable.
**High-level Test Scenarios.**
- Claim: no EC2 or global key enforces a minimum TLS version/signature version. → **Oracle:** confirmed null by `list_ec2.md` + global key index; corroborate with `iam:SimulateCustomPolicy` showing `aws:SecureTransport` Deny simulates (valid) but `aws:TlsVersion` is unknown.
- Claim: SSH/RDP transport security has **no AWS-side default or enforcement** (customer-managed keys only); Windows "allow only encrypted connections" (`:96`) is advisory SG/firewall authoring with no managed guardrail (SG rules are IP/port/proto, not encryption-aware).
**Doc evidence:** `data-protection.md:12,92,94,96`; `reference_policies_condition-keys.md:2166`; `list_ec2.md` (no TLS-version/sig-version key). **Severity-if-true:** Low — correctly-scoped shared-responsibility statement; risk is **doc-clarity misread**, not an enforcement bug. Worth filing as a documentation-clarity gap.

### R5/R6-attestation — [Lens W] SEV-SNP attestation has NO AWS IAM/KMS tie-in (scope-defining finding)
**Background.** `snp-attestation.md`: attestation is customer-driven — build `snpguest` (`github.com/virtee/snpguest`), request a report from the AMD Secure Processor, fetch VCEK (Dedicated Hosts, per-chip) or **VLEK (shared tenancy, issued by AMD for AWS)** cert chain from **AMD's KDS** (`kdsintf.amd.com`), validate chain to AMD root. The launch measurement = hash of initial guest memory + vCPU state.
**Security Concern (Lens W).** There is **no `kms:RecipientAttestation`-class key, no NitroTPM-tied attestation key, no AWS verification API** that consumes SEV-SNP attestation for any authorization decision (grep of all 10,190 lines of `list_ec2.md`: no `attestation`/`Recipient`/`VCEK`/`VLEK`). `GetInstanceTpmEkPub` is key-*retrieval*, not attestation-verification, and carries only ordinary `instance*` scoping. **Therefore a policy "Deny `kms:Decrypt` unless the instance presents a valid SEV-SNP attestation" is not expressible** — the whole trust chain terminates at the customer's own `snpguest verify` step. This is **expected-by-design** (SEV-SNP's threat model is the cloud operator itself, so AWS deliberately staying out of the gate is arguably correct), but it is a **crucial scoping fact**: anyone hunting a "fail-open attestation gate" in EC2 IAM/KMS will find **there is no gate to break** — any "decrypt only if attested" enforcement must be **customer-built** (e.g. a KMS-proxy that checks the report), and *that* layer is where a fail-open bug would live, not in AWS.
**High-level Test Scenarios.**
- Claim: no EC2/KMS condition key ties SEV-SNP attestation to authz. → **Oracle:** confirmed null by `list_ec2.md` grep; no `--debug`/measurement-bypass flag documented for `--cpu-options AmdSevSnp` (only `enabled|disabled`).
- Claim (VLEK nuance): on **shared tenancy** the report is VLEK-signed (AMD-for-AWS), not per-chip VCEK — a naive customer verifier that skips nonce freshness or full chain validation is replay/forgery-exposed; this is a **customer-tooling** weakness (snpguest is a 3P repo), not an AWS surface. Out of scope as an AWS finding; note for customer-build guidance.
**Doc evidence:** `snp-attestation.md`, `snp-work-launch.md`; `list_ec2.md` (null). **Severity-if-true:** N/A as an AWS bug (by-design); High-value as a **scoping/assurance fact** for the hunter.

### R6-audit — [Lens U/O] SEV-SNP (and encryption-in-transit capability) invisible in console
**Background/Concern.** `snp-find-instance-types.md:8` and `snp-work-launch.md:182`: *"The Amazon EC2 console does not display this information."* Both the capability (`processor-info.supported-features=amd-sev-snp`) and the per-instance state (`DescribeInstances .CpuOptions.AmdSevSnp`) are API/CLI-only; same strongly-inferred pattern for `network-info.encryption-in-transit-supported` (console hides most instance-type attributes per `instance-discovery.md:34`). A console-only security reviewer can miss whether an instance has/lacks confidential compute. CloudTrail *does* carry `cpuOptions.AmdSevSnp` on the launch event → retrospective audit via CloudTrail+API is possible.
**Oracle (read-only):** compare console view vs `describe-instances`/`describe-instance-types` output. **Severity:** Low–Medium (audit/visibility gap, not an enforcement gap).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Re-encrypt an encrypted snapshot under an attacker KMS key, org IAM unable to pin key | `CopySnapshot`/`CopyVolumes` | `ec2:Encrypted` (present) — but **`ec2:KmsKeyId` absent** (R2) |
| "Require confidential compute" Deny silently fails open | `RunInstances` SEV-SNP | real key `ec2:CpuOptionsAmdSevSnp`; **`ec2:AmdSevSnp` nonexistent** (R6) |
| Force inter-instance traffic through in-path device → cleartext, no signal | Nitro inter-instance encryption | requirement list + opt-in VPC Encryption Controls `encryption-status` (T1) |
| Build a compliance control on "always-on memory encryption" that cannot be verified | Memory encryption (TME/SME/Graviton) | prose-only; **no attestation API** (except SEV-SNP, customer-only) |
| "Decrypt only if SEV-SNP attested" assumed enforceable by IAM/KMS | SEV-SNP attestation | **no AWS attestation condition key** — customer-built only (R6-attestation) |
| Enforce minimum TLS version / SigV4 on EC2 actions | Transport | `aws:SecureTransport` only; **no `aws:TlsVersion`/`aws:SignatureVersion`** (T4) |
| Read another tenant's residual EBS/instance-store bytes | EBS media / NVMe reset | "zeroed/pseudorandom before reuse" / "block reset" — **HARD STOP, AWS infra** |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AWS shared storage-media reuse** (EBS "zeroed/pseudorandom before re-use", DoD/NIST erase "reflected to underlying media"), **instance-store block reset on stop/terminate**, **NVMe hardware-key isolation** ("inaccessible to AWS personnel") — AWS-infra / Nitro-hardware internals. The cross-tenant reuse oracle (write canary → terminate → relaunch at scale → read raw device for canary) is a **live dual-account, AWS-infra-targeting HARD STOP** — recorded only as a lead for a properly-scoped live engagement, never for this pass.
- **Physical-layer / AZ-to-AZ / cross-Region VPC-peering & TGW-peering bulk encryption, Outposts service-link encryption** — AWS-backbone claims with no customer-facing verification API; **HARD STOP** (do not probe AWS backbone).
- **Instance data-plane transport** (SSH/RDP/app TLS) — customer responsibility; no AWS enforcement; IMDS and in-guest config are managed-host/customer surfaces.
- **Customer-authored IAM policies / SG rules / Windows Firewall** that fail to enforce the page's recommendations — customer footgun (the R2/R6 findings are in scope precisely because they are **AWS-authored IAM-schema gaps**, not customer policy mistakes).
- **snpguest third-party tooling** weaknesses — customer-build / 3P-repo, not AWS.
- Single-tenant self-DoS; product/feature-parity gaps.

## 8. Null Hypotheses / Doc Gaps (lenses checked, pages named)
- **Lens A/IDOR — null (customer-testable):** no shared-fleet resource-by-ID API on this page; the only cross-tenant claims are AWS-infra reuse-isolation (hard stop). `GetConsoleOutput`/`GetConsoleScreenshot` are the *detection* surface for a reuse breach and are correctly scoped to the caller's own `instance*` — no IAM gap. Pages checked: `data-protection.md`, `list_ec2.md:8252–8261`.
- **Lens W debug/bypass — null:** no `--debug`/all-zero/wildcard measurement path documented for `--cpu-options AmdSevSnp`; only `enabled|disabled`. Pages: `snp-work-launch.md`.
- **Lens U — NVMe "cannot disable / cannot BYOK" is doc-consistent, not a gap:** the guarantee says *no* customer control exists, and the IAM surface has none either way (no `InstanceStore`/`NvmeEncrypt` key in `list_ec2.md`) — true doc-vs-API consistency; the residual is a **transparency gap** (unattestable, strictly weaker than SEV-SNP which at least gives a verifiable report).
- **Lens H — `CreateSnapshot`/`AttachVolume` lacking `ec2:KmsKeyId` is by-design** (no new key chosen; attach only triggers `CreateGrant`/`Decrypt`, per `how-ebs-encryption-works.md`) — null, not a gap.
- **Lens G — doc-gap pointer:** the `:18` "do not include credentials in a URL to an external server" line is generic boilerplate shared across AWS `data-protection.html` pages; **no EC2 field is named on this page.** Adjacent EC2 features that *do* dereference a customer URL (for a later dedicated SSRF pass, NOT found on this page): user-data cloud-init `#include`/`include-once`, SSM documents/Run Command S3/HTTP sources, EC2 Image Builder component sources. Marked **doc-gap — confirm the field's surface before investing.**
- **Lens T (free-form/tags) — Low/Info:** `:18` warns tag/Name-field values "may be used for billing or diagnostic logs" — info-disclosure footgun, customer-authored, Low.
- **Open doc-gaps to settle before a hunter invests (not fabricated):**
  1. `encryption-examples.md#ebs-volume-encryption-outcomes` **unread** — needed to settle whether `CopyImage`'s total absence of encryption condition keys is by-design (inherits backing-snapshot key) or a true R2-sibling gap.
  2. `encryption-by-default.md` — confirmed via `list_ec2.md` that the four `*EbsEncryptionByDefault`/`*DefaultKmsKeyId` actions carry **no condition keys** (account-wide toggle, no per-principal/request scoping); the prose interaction with per-request `Encrypted=false` override attempts not re-verified this pass.
  3. `ebs-encryption-requirements.md` / `kms-key-rotation.md` — potential extra Lens-H leads (does CMK rotation interact with "cannot change key on existing volume" to create a stale-grant / availability gap?).
  4. Live console check that `network-info.encryption-in-transit-supported` is genuinely console-hidden (high-confidence inference from `instance-discovery.md:34`, not verbatim-confirmed for this field).

---
*Generated by the `security-questionbuilder` skill (documentation-only). All leads are falsifiable hypotheses with read-only (`iam:SimulateCustomPolicy` / `describe-*`) first oracles; AWS-infra reuse-isolation and backbone-encryption claims are explicit HARD STOPs. Route AWS-authored IAM-schema gaps (R2, R6) to `aws-security` as Tier-2.*
