# AMD SEV-SNP for Amazon EC2 — Attack Research Plan

**Source of leads:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html` + children
`snp-work-launch.html`, `snp-attestation.html`, `snp-find-instance-types.html`; IAM reference
`service-authorization/latest/reference/list_ec2.md` (offline mirror `/work/aws-docs`, verified
against live docs 2026-09-08 — online == offline byte-for-byte; **no injected "See also" AI-agent
block on these pages**).
**Status:** documentation-derived hypotheses only. Nothing tested against a live account.
**Archetype:** thin, single-account, hardware-confidential-compute *feature* page (same family as
[[instance-optimize-cpu]], [[nitrotpm]], [[enclaves]] plans). Most multi-tenant / parser / SSRF /
PassRole lenses are **null here** — the value concentrates in **IAM condition-key governance gaps**
(Lens S/U) and **attestation-trust-model** framing (Lens W/U). Deep confidential-compute HW /
hypervisor / crypto internals are a **hard stop** (AWS service plane).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right.
- **HARD STOP:** the moment evidence touches the AMD SEV-SNP memory-encryption HW, the hypervisor/Nitro isolation boundary, the VLEK/VCEK signing-key custody, AMD KDS internals, or any AWS-fleet identity/credential — **stop, preserve evidence, flag for AWS-Security disclosure.** This service's entire premise sits on top of the shared-responsibility line; almost everything "deep" is out of scope by construction.
- The two highest-value leads (Area 1, Area 2) are **AWS-owned IAM/enforcement governance gaps** confirmable from the *IAM reference alone* — no live confidential instance required to establish the primitive.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Governance bypass:** Show an AWS organization **cannot** use IAM/SCP to *require* or *forbid* SEV-SNP consistently, because a documented write path (`AllocateHosts --cpu-options AmdSevSnp=enabled`) carries **no** governing condition key and the `ec2:CpuOptionsAmdSevSnp` key is region-scoped to shared tenancy only. (Lens S/U — **crown**)
2. **Immutability / downgrade:** Prove (or refute) that the documented "SEV-SNP can't be disabled and you can only resize to another SEV-SNP type" invariant is enforced by the API on **every** mutation path (resize twin, ModifyInstanceAttribute, launch-template late-binding), not just the console. (Lens X/U)
3. **Attestation-as-access-control footgun:** Establish that the SEV-SNP attestation report authenticates *code + initial state*, **not tenant/account identity**, and that (unlike Nitro Enclaves' `kms:RecipientAttestation*`) there is **no AWS control-plane condition key that consumes a SEV-SNP measurement** — so a customer building an authЗ/KMS gate on SEV-SNP attestation must supply their own identity binding. (Lens W/U — informational, high-value framing)
4. **Detection blind spot:** Show SEV-SNP enablement is invisible in the EC2 console (CLI/CloudTrail only), creating an audit/compliance gap. (Lens O)
5. **Billing integrity of the 10% shared-tenancy surcharge** — bound the question, then **stop at the metering plane** (out of scope).

---

## 2. Components, Assets, and Design

**What it is.** AMD SEV-SNP (Secure Encrypted Virtualization – Secure Nested Paging) is an AMD-EPYC-Milan **CPU feature** exposed on EC2 `*6a` instances (m6a/c6a/r6a) that provides (a) **memory encryption** and (b) a **signed attestation report** measuring the instance's initial boot state. It is a per-instance *launch-time* toggle inside `CpuOptions`, not a standalone resource.

**Two deployment modes (different trust roots):**
- **Dedicated Hosts** — allocate a host with `AmdSevSnp=enabled`, run supported types on it. Attestation signed by **VCEK** (Versioned Chip Endorsement Key, *per-chip*, AMD-certified). Any commercial Region. No surcharge.
- **Shared tenancy** — `run-instances --cpu-options AmdSevSnp=enabled` directly. Attestation signed by **VLEK** (Versioned Loaded Endorsement Key, *issued by AMD for AWS*). **Only US East (Ohio) + Europe (Ireland).** +10% On-Demand-rate hourly surcharge.

**Customer-facing interface (control plane):**
- `ec2:RunInstances` `--cpu-options AmdSevSnp=enabled` (both modes).
- `ec2:AllocateHosts` `--cpu-options AmdSevSnp=enabled` (DH mode only).
- `ec2:ModifyInstancePlacement` (firmware-refresh host move), `Stop/Start/ReleaseHosts`.
- `ec2:DescribeInstances` (read `CpuOptions.AmdSevSnp`), `ec2:DescribeInstanceTypes` filter `processor-info.supported-features=amd-sev-snp`.
- Console: **cannot display** whether an instance has SEV-SNP enabled (doc-explicit).

**Attestation path (data plane, in-guest — customer-owned):** guest runs `snpguest` (3rd-party `github.com/virtee/snpguest`, built via cargo), requests report from the AMD Secure Processor **through the host**, fetches VCEK/VLEK + ARK/ASK certs from **AMD KDS** (`kdsintf.amd.com`, `--proto '=https' --tlsv1.2`), verifies the chain to AMD's root of trust. Processor model currently `milan`. **OVMF** UEFI firmware runs before the AMI boot loader and is part of the launch measurement.

**Identifier shapes:** standard `i-…` / `h-…` IDs; `AmdSevSnp` is a **string enum** field inside `CpuOptions` (`"enabled"` / absent). No new ARN, no new opaque resource ID, no tenant ID in a body.

**Identity / roles:** ordinary SigV4 IAM on the EC2 control plane. No service-linked role, no PassRole field, no credential vending, no KMS integration documented on these pages.

```
                     ┌──────────────── customer account (IAM / SigV4) ────────────────┐
  RunInstances ─────►│  EC2 control plane  ── CpuOptions.AmdSevSnp=enabled (launch-only,│
  AllocateHosts ────►│                        IMMUTABLE, resize-constrained)           │
                     └───────────────┬───────────────────────────────────────────────┘
                                     │ provisions
                    ┌────────────────▼─────────────────┐   HARD STOP (AWS service plane)
                    │  Nitro host + AMD EPYC (Milan)    │   memory-encryption HW, hypervisor
                    │  SEV-SNP FW, OVMF, VCEK/VLEK keys │   isolation, key custody
                    └────────────────┬─────────────────┘
     in-guest (customer) ┌───────────▼───────────┐  https   ┌──────────────┐  3rd-party
     snpguest ──────────►│ AMD Secure Processor  │─────────►│  AMD KDS      │  (out of scope)
     (report.bin)        │  (attestation report) │          │ kdsintf.amd  │
                         └───────────────────────┘          └──────────────┘
```

---

## 3. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `RunInstances` | POST (Query) | Existing | **Yes** | External | Launch instance; `CpuOptions.AmdSevSnp=enabled` | Yes | Caller w/ ec2:RunInstances | **Carries** `ec2:CpuOptionsAmdSevSnp` cond key (region-scoped, see Area 1) |
| `AllocateHosts` | POST | Existing | **Yes** | External | Allocate DH w/ `--cpu-options AmdSevSnp=enabled` | Yes | Caller w/ ec2:AllocateHosts | **NO** SEV-SNP cond key at all (Area 1) — keys: RequestTag,TagKeys,AutoPlacement,AZ,HostRecovery,InstanceType,Quantity,Region |
| `ModifyInstanceCpuOptions` | POST | Existing | Yes | External | Change CoreCount/ThreadsPerCore (Stopped) | Yes | ec2:ModifyInstanceCpuOptions | Carries `ec2:CpuOptionsAmdSevSnp`; **cannot** toggle AmdSevSnp (immutable) — verify it rejects (Area 2) |
| `ModifyInstanceAttribute` (instanceType) | POST | Existing | Yes | External | Resize path | Yes | ec2:ModifyInstanceAttribute | Resize must stay within SEV-SNP-capable types — verify enforcement (Area 2) |
| `ModifyInstancePlacement` | POST | Existing | Yes | External | Move instance to new DH (firmware refresh) | Yes | caller | Continuity of encryption/attestation across move = infra, out of scope |
| `DescribeInstances` | GET | Existing | No | External | Read `CpuOptions.AmdSevSnp` | Yes | caller | Only programmatic way to see status (console can't) — Area 4 |
| `DescribeInstanceTypes` | GET | Existing | No | External | `processor-info.supported-features=amd-sev-snp` | Yes | any | Capability oracle; cross-check vs security-capability doc tables (Lens U) |
| `snpguest report/fetch/verify` | in-guest CLI | Existing | No | N/A | Generate & verify attestation report | No | in-guest root | 3rd-party repo → out of scope; runbook integrity noted in Area 3 |

**Undocumented/hidden-knob sweep:** `AmdSevSnp` accepts `enabled` (doc) / effectively-`disabled` (absent). No console exposure for the *host*-level flag beyond the allocate wizard; the enum is small and non-permissive — no `NONE`-style auth-weakening value. Nothing further hidden on the API model for this feature.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Org / SCP author | member-account launches | `ec2:CpuOptionsAmdSevSnp` cond key on RunInstances | **Breach = the org cannot deny/require SEV-SNP** because the key is region-scoped (Ohio/Ireland only) and `AllocateHosts` carries no such key → policy is a no-op on the DH path / other regions (Area 1) |
| Caller | own running instance | immutability invariant ("can't be disabled", resize constrained) | Breach = any API path that clears `AmdSevSnp` on a live instance, or resizes a SEV-SNP instance to a non-SEV-SNP type (Area 2) |
| Attestation-report verifier | instance identity | launch measurement + VCEK/VLEK signature | Breach *shape* = treating the report as proof of *tenant/account* identity (it isn't — Area 3). No AWS boundary broken; a **customer-side** design footgun |
| Any customer surface | AMD SEV-SNP HW / hypervisor / key custody | memory encryption, VLEK/VCEK signing | **HARD STOP** — AWS service plane; do not probe |
| Guest | AMD KDS (`kdsintf.amd.com`) / `virtee/snpguest` | https cert fetch, cargo build | 3rd-party — out of scope; runbook TLS hygiene noted (Area 3) |
| Console operator | SEV-SNP status | (no console field) | Breach *of visibility* = a compliance/detection blind spot (Area 4) |

---

## 5. Recommended Areas of Focus

### Area 1 — IAM governance gap: SEV-SNP is not uniformly govern­able by condition key  *(Lens S + Lens U — CROWN, doc-CONFIRMED from IAM reference)*
**Background.** SEV-SNP is a compliance-relevant control: a security org may want to **mandate** it for regulated workloads or **forbid** it (e.g. to preserve hibernation/Nitro-Enclaves, which SEV-SNP disallows). The only IAM lever is the `ec2:CpuOptionsAmdSevSnp` condition key.
**Security Concern.** Two concrete, verified defects in the *shipped IAM surface*:
- **G1 — `AllocateHosts` carries no SEV-SNP condition key.** `list_ec2.md` line 4651-4654: `AllocateHosts` condition keys are exactly `aws:RequestTag`, `aws:TagKeys`, `ec2:AutoPlacement`, `ec2:AvailabilityZone`, `ec2:HostRecovery`, `ec2:InstanceType`, `ec2:Quantity`, `ec2:Region` — **`ec2:CpuOptionsAmdSevSnp` is absent**, even though `snp-work-launch.html` documents `allocate-hosts --cpu-options AmdSevSnp=enabled` as a first-class write path. ⇒ An org **cannot** write an SCP that forbids/requires SEV-SNP at Dedicated-Host allocation. A DH allocated with SEV-SNP then silently permits SEV-SNP instances (which need no per-instance key match on that host).
- **G2 — the RunInstances key is region-scoped to shared tenancy only.** `list_ec2.md` line 10027, the key definition itself: *"Filters access by the state of AMD SEV-SNP CPU Options. **Currently, only US East (Ohio) and Europe (Ireland) are supported**"* — the two shared-tenancy Regions. ⇒ On the **Dedicated-Host / other-commercial-Region** path (where the doc says SEV-SNP *is* available "in any commercial AWS Region"), a `Deny … unless ec2:CpuOptionsAmdSevSnp = enabled` (or `= disabled`) condition may not evaluate as intended — the governance control the customer *thinks* they wrote is inert outside Ohio/Ireland.
**High-level Test Scenarios (falsifiable):**
1. **Claim:** A `Deny AllocateHosts` conditioned on `ec2:CpuOptionsAmdSevSnp` is a no-op → **Mechanism:** key absent from AllocateHosts (line 4651) → **Oracle:** `iam:SimulateCustomPolicy` for `ec2:AllocateHosts` with a `Condition{StringEquals: ec2:CpuOptionsAmdSevSnp: disabled}` — simulation should show the condition **ignored / policy has no effect on the AmdSevSnp dimension**; then a live `allocate-hosts --cpu-options AmdSevSnp=enabled` under that policy still succeeds. → **Severity:** Low–Medium (org-wide governance gap, AWS-owned).
2. **Claim:** A `RunInstances` require-SEV-SNP (or forbid-SEV-SNP) SCP silently fails outside Ohio/Ireland → **Mechanism:** key def line 10027 region caveat → **Oracle:** `SimulateCustomPolicy` / live `run-instances` in `us-west-2` with the condition; observe whether the condition key is populated in the request context (a `Deny unless enabled` that lets a *non*-SEV-SNP launch through = confirmed inert). → **Severity:** Low–Medium.
3. **Adjacent (Lens U doc-vs-API):** Does `DescribeInstanceTypes … amd-sev-snp` return supported types in Regions where the *condition key* is unsupported? A capability/enforcement mismatch (feature usable, IAM key not) is itself the finding.
**Doc evidence:** `snp-work-launch.html` (allocate-hosts + run-instances CLI); `list_ec2.md` L4651-4654 (AllocateHosts keys), L10027 (key def + region caveat), L5093 (RunInstances carries the key). **Severity-if-true:** Low–Medium, **AWS-owned governance/enforcement gap** (route `aws-security` as Tier-2 doc/enforcement inconsistency; *not* a customer footgun — the customer cannot add the missing key).
**Stop condition:** confirmed once simulation/live shows the condition is ignored on AllocateHosts and/or outside the two Regions. Do not escalate into metering/HW.

### Area 2 — Immutability & no-downgrade invariant enforcement  *(Lens X + Lens U)*
**Background.** `sev-snp.html` Considerations promise: *"After it is enabled, AMD SEV-SNP can't be disabled … remains enabled throughout the instance lifecycle"* and *"You can only change the instance type to another instance type that supports AMD SEV-SNP."*
**Security Concern.** A confidential-compute guarantee is only as strong as the *weakest mutation path* that could clear or bypass it. The invariant must hold on **every** twin/sibling, not just the console wizard.
**High-level Test Scenarios:**
1. **Claim:** Some mutation path clears `AmdSevSnp` on a live/stopped instance → **Oracle:** attempt `modify-instance-cpu-options` and `modify-instance-attribute` on a stopped SEV-SNP instance passing `AmdSevSnp=disabled` / omitting it / passing a non-SEV-SNP `--instance-type`; expect `ValidationException`/reject. A 200 that drops SEV-SNP = broken invariant. → **Severity:** Medium (silent loss of a compliance control; Low if it forces a stop+relaunch anyway).
2. **Claim:** Resize to a **non-`*6a`** type is accepted → **Oracle:** `modify-instance-attribute --instance-type c5.large` on a SEV-SNP `c6a`; expect refuse. → **Severity:** Medium.
3. **Claim (Lens X launch-template late-binding — chains [[launch-templates-plan]]):** a launch template / ASG `$Latest`/`$Default` that omits `AmdSevSnp` re-launches replacement capacity **without** SEV-SNP while the fleet is nominally "confidential." → **Oracle:** build LT version without CpuOptions, drive an ASG refresh, `describe-instances` the new members. → **Severity:** Medium (integrity-of-fleet).
**Doc evidence:** `sev-snp.html` Considerations; `ec2-instance-resize.html` cross-link. **Severity-if-true:** Medium.

### Area 3 — Attestation trust model: authenticates code+state, not tenant identity  *(Lens W + Lens U — informational, high-value framing; mirrors [[nitrotpm-plan]])*
**Background.** The report's `launch measurement` = hash of initial guest memory + vCPU state, signed VCEK (per-chip, DH) or VLEK (per-AWS, shared tenancy), chaining to AMD root.
**Security Concern.** Unlike Nitro Enclaves (`kms:RecipientAttestation:PCR0…`/`ImageSha384`) and NitroTPM, **there is no AWS control-plane condition key that consumes a SEV-SNP measurement** — attestation verification happens entirely *in-guest* by the customer against AMD KDS. Consequences a downstream builder must not get wrong:
- The measurement proves *"this exact boot image is running on genuine AMD SEV-SNP HW"* — it does **not** prove *which AWS account/tenant* owns the instance. Two different tenants booting the identical AMI produce the **same** launch measurement.
- On **shared tenancy** the VLEK is *"issued by AMD for AWS"* — i.e. **one AWS-wide loaded key** signs every shared-tenancy report, not a per-tenant key. So a valid VLEK-signed report only attests "some AWS shared-tenancy SEV-SNP instance," and any AWS customer can produce one with the same image.
**High-level Test Scenarios (framing / customer-side, not an AWS-plane breach):**
1. **Claim:** A relying party gating access on "valid SEV-SNP attestation + expected measurement" can be satisfied by an attacker booting the *same public AMI* in their **own** account → measurement + VLEK match, identity does not. → **Oracle:** compare `report.bin` launch measurements across two accounts running the same AL2023 SEV-SNP image; identical measurement + both VLEK-valid = the design gap is real. → **Severity:** Informational (customer footgun; AWS docs never claim tenant binding, so document, don't file against AWS unless AWS sample code builds an authЗ gate on it — none here).
2. **Claim (Lens W fail-open):** verifier accepts a report with a **stale/replayed nonce** or skips freshness → **Oracle:** re-present an old `report.bin`; the `--random` request nonce is the only freshness input — a verifier ignoring it is replayable. → **Severity:** Informational (customer verifier flaw).
3. **Runbook hygiene (Lens R/Y, minor):** `snp-attestation.html` uses `sudo curl … | openssl verify` and `git clone … && cargo build` — pinned to `--proto '=https' --tlsv1.2` (good) but **no commit pin / checksum** on `snpguest`, and `virtee/snpguest` is 3rd-party. Supply-chain trust of the verify tool is a **customer** responsibility; bugs in `snpguest`/AMD KDS = **out of scope**.
**Doc evidence:** `snp-attestation.html`, `sev-snp.html#snp-concepts` (VCEK/VLEK defs). **Severity-if-true:** Informational.

### Area 4 — Detection / audit blind spot  *(Lens O)*
**Background.** `snp-work-launch.html#snp-work-check`: *"The Amazon EC2 console does not display this information"* — SEV-SNP status is visible only via `describe-instances … CpuOptions` or the CloudTrail `cpuOptions:{AmdSevSnp:enabled}` field on the launch event.
**Security Concern.** A console-only operator (or a Config rule / GuardDuty consumer not inspecting `CpuOptions`) has **no visibility** into whether "confidential" workloads actually have SEV-SNP on, or whether an instance quietly *lacks* it. Combined with Area 2's late-binding path, drift is undetectable in the console.
**High-level Test Scenarios:** confirm no console surface; confirm CloudTrail records enablement on `RunInstances` **but** check whether a *host-level* `AllocateHosts --cpu-options AmdSevSnp` is equivalently logged/queryable (it may not be, compounding Area 1's G1). → **Oracle:** diff console vs `describe-instances` vs CloudTrail for a SEV-SNP instance and a SEV-SNP host. → **Severity:** Low / Informational (detection enabler).

### Area 5 — Billing integrity of the 10% shared-tenancy surcharge  *(Lens U → metering plane = OUT OF SCOPE, bounded here)*
**Background.** `sev-snp.html#snp-pricing`: shared-tenancy SEV-SNP adds +10% of On-Demand rate, *separate* from instance usage, unaffected by RIs/Savings Plans/OS. **Spot quirk (verbatim):** *"If the allocation strategy uses price as an input, Spot Fleet does not include this additional fee; only the Spot price is used."*
**Security Concern (bounded).** The Spot-Fleet carve-out means the price-optimized allocation *ignores* the 10% surcharge when ranking — a documented metering behavior, not a bypass of the charge itself. Whether SEV-SNP can be enabled and the surcharge under-metered is a **metering-plane** question.
**Decision:** **Do not probe.** Metering/billing is the AWS service plane / shared-responsibility line. Record the Spot carve-out as a documented quirk and stop. → **Severity:** N/A (out of scope).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Org cannot require/forbid SEV-SNP via IAM | AllocateHosts / RunInstances IAM | `ec2:CpuOptionsAmdSevSnp` cond key (absent on AllocateHosts; region-scoped on RunInstances) |
| SEV-SNP silently cleared / downgraded post-launch | ModifyInstanceCpuOptions / ModifyInstanceAttribute / LT late-binding | "can't be disabled"; resize restricted to SEV-SNP types |
| Attestation report reused as tenant-identity proof | snpguest / VLEK-VCEK verify | launch measurement + nonce + cert chain (proves code+HW, **not** tenant) |
| Replayed / stale attestation accepted | in-guest verifier | `--random` request nonce (freshness) |
| Confidential status invisible to operators | Console vs CloudTrail/DescribeInstances | CLI/CloudTrail `cpuOptions.AmdSevSnp` only |
| SEV-SNP enabled without surcharge | Billing / Spot Fleet | 10% On-Demand fee (Spot price-based allocation excludes it) — **out of scope** |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AMD SEV-SNP memory-encryption hardware, the hypervisor/Nitro isolation boundary, VCEK/VLEK signing-key custody, AMD Secure Processor, OVMF firmware internals** — AWS service plane / AMD HW. **Hard stop.**
- **AMD KDS (`kdsintf.amd.com`) and `virtee/snpguest`** — third-party; bugs there are out of scope (3rd-party reference repo/service).
- **Billing/metering correctness** of the 10% surcharge and the Spot carve-out — metering plane.
- **Live migration / host-maintenance continuity** on shared tenancy (manual stop/start to a new host) — shared managed-fleet infra.
- **Cross-tenant memory/side-channel attacks** on the shared host — the very threat SEV-SNP mitigates; probing the HW guarantee = hard stop.
- **A customer building a weak attestation-based authЗ gate** — customer design responsibility (documented in Area 3 for the hunter's awareness, not as an AWS finding).

---

## 8. Null Hypotheses / Doc Gaps (pages checked)
- **Lens A/V (cross-tenant IDOR / network):** N/A — read all four SEV-SNP pages + `snp-find-instance-types`; no multi-tenant resource-by-ID API, no ENI/VPC/PrivateLink surface, no shared-fleet resource the caller names. SEV-SNP *is* the isolation control, not a multi-tenant service.
- **Lens B/C (PassRole / credential vending):** N/A — no role-ARN input, no AssumeRole/session-policy, no credential provider on any SEV-SNP page or in the RunInstances/AllocateHosts CpuOptions surface.
- **Lens F/Q (parser / upload):** N/A — no customer-supplied blob parsed server-side; `AmdSevSnp` is a fixed string enum. (Deep BSON/manifest parsers live in other EC2 plans, not here.) The attestation `report.bin` is parsed **in-guest by the customer's own tool** — out of scope.
- **Lens G (SSRF):** N/A — read all pages; no field the *service* dereferences server-side. The only URL fetches (`kdsintf.amd.com`) run **in-guest under the customer's identity**, not fleet identity.
- **Lens H (KMS/enc-context):** N/A — **no KMS integration documented** for SEV-SNP (contrast Enclaves/NitroTPM). Memory encryption keys are HW-managed, not customer-KMS. If a future revision adds a `kms:RecipientAttestation`-style SEV-SNP key, re-open under Lens W.
- **Lens K (prompt injection), Lens J (OAuth), Lens M (session), Lens N (namespace), Lens T (secret reachability):** no triggers on any page.
- **Lens W (attestation-conditioned authZ) — partial/doc-gap:** SEV-SNP measurements are **not** consumed by any AWS control-plane condition key today (unlike Enclaves). If AWS later ships one, the fail-open / wildcard-PCR / all-zero-measurement tests from Lens W apply directly.
- **Doc-gap:** neither the UserGuide nor the IAM reference states *why* `ec2:CpuOptionsAmdSevSnp` is region-limited, nor whether AllocateHosts SEV-SNP will ever gain a key — **confirm the current IAM surface live before asserting the governance gap is unfixed** (Area 1 depends on the reference being current; re-check `list_ec2` / `aws iam get-context-keys` at hunt time).

---
**Priority order for the hunter:** Area 1 (crown, IAM-reference-confirmable now) → Area 2 (immutability, cheap live checks) → Area 4 (detection, trivial) → Area 3 (attestation framing, informational) → Area 5 (bounded, stop). Everything HW/crypto/metering = hard stop.
