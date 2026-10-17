# EC2 Instance Types — Naming, Capability-Reporting & Type-Gating — Attack / Research Plan

> **Target:** `https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html`
> (the EC2 instance-type **naming convention** page and the surrounding `instancetypes` documentation set).
> **Method:** `security-questionbuilder` skill — boundary-first research plan generated from documentation only.
> **Source corpus:** offline mirror `/work/aws-docs/docs/ec2/latest/instancetypes/` cross-checked against the online `.md` of each page (`…/instance-type-names.md` etc.), plus the EC2 Service Authorization reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`, EC2 APIReference, and `ec2-nitro-instances.md`.
> **Analysis date:** 2026-10-17. **Mode:** documentation-only; no live AWS calls. Every lead below is a *falsifiable hypothesis* for a hunter (`aws-vuln-hunter`) to settle with observed API evidence.

---

## 0. How to use this document

This is a research plan, not a findings report. Each lead is written as:

> **Claim** (a thing the docs imply should hold, stated so it can be broken) → **Mechanism** (the exact page/field that makes breaking it plausible) → **Confirm/Refute oracle** (the observation that settles it) → **Preconditions / Severity-if-true.**

**Read the surface correctly first — this is the single most important framing for this target.** The instance-type *catalog itself* is a **global, non-tenant, read-only reference**. There are no per-tenant instance-type resources, no instance-type ARNs, no instance-type IDs scoped to a caller. Therefore the classic cross-tenant lenses (A/IDOR, C/credential-vending, M/shared-identifier) **do not fire on the catalog**. The real, live security surface of "instance types" is **three derived things**:

1. **IAM authorization that *gates* on instance-type / hardware attributes** (`ec2:InstanceType`, `ec2:Tenancy`, `ec2:Attribute`, launch-template keys) — where a Deny/Allow keyed on a *type* or *capability* can be silently inert, bypassable via a sibling API, or voided by a casing/namespace mismatch. **This is the highest-value zone** and is covered in depth in the companion scratch file `instancetypes-scratch-lensSR.md`.
2. **Capability-reporting APIs** (`DescribeInstanceTypes`, `GetInstanceTypesFromInstanceRequirements`/ABIS) whose output the customer *trusts* to build those IAM gates and selection policies — where the doc "Security specifications" tables, the ABIS selector, and the ground-truth API can **diverge**, and where no field encodes "end of sale" / "previous generation". Covered in `instancetypes-scratch-lensUX.md`.
3. **The Nitro attestation + encryption-in-transit guarantees** that per-type capability claims feed into (NitroTPM, Nitro Enclaves, AMD SEV-SNP, automatic in-transit encryption) — where an attestation-gated or "automatic encryption" guarantee is weaker than the doc asserts. Covered in `instancetypes-scratch-lensWVL.md`.

A hunter should start at the three companion scratch files (they contain the field-level evidence and line numbers), then use §6 of this document as the prioritized firing list and §8 as the explicit null/doc-gap ledger so no surface is silently skipped.

**Hard shared-responsibility stop (applies to every lead):** the moment any observation touches **AWS's own service plane** — the Nitro hypervisor key, the Nitro attestation PKI / CA, cross-tenant memory or device state, fleet/host credentials, the physical-host scheduler — **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not probe Nitro isolation, do not attempt a live cross-tenant "equal share" demonstration, do not attempt to read another tenant's enclave. Those are hard stops, not test steps.

---

## 1. Pentest Objectives (what a win looks like here)

1. Demonstrate that an IAM policy a customer (or an AWS sample policy) writes to **restrict which instance types/hardware can be launched** is **inert or bypassable** — i.e. a principal who should be capped to (say) `t3.*` or to AMD-SEV-SNP-capable types can launch outside the cap. *(Lens S/R/X — Tier-1 customer-authored + Tier-2 AWS-sample.)*
2. Demonstrate that an IAM **Deny** keyed on an instance-type/hardware condition is **silently void** (hallucinated condition key, case mismatch, wrong resource type, sibling API not covered). *(Lens S/R.)*
3. Demonstrate that **capability ground truth diverges** from what the doc "Security specifications" tables or the ABIS selector lead a customer to trust — e.g. a type the doc/ selector treats as safe/available is not, or vice-versa, in a way that weakens a security decision built on it. *(Lens U/X.)*
4. Demonstrate that a **documented security guarantee** on a Nitro feature (attestation gating, automatic encryption-in-transit, "equal share") is enforced more weakly than stated, *without* crossing into the hard-stop service-plane zone. *(Lens W/Y/L.)*

A clean, well-evidenced **negative** on all four is a correct and complete result for this surface.

---

## 2. Components, Assets, and Design (Step 1 reconstruction)

### 2.1 What the target actually is
`instance-type-names.html` documents the **naming grammar** only:

```
   [series][generation][options].[size]              e.g.  c7gn.xlarge  ,  m8idn.metal-48xl
     │        │          │        └── size: nano…metal-NNxl, "flex" tier
     │        │          └────────── option letters (see table)
     │        └───────────────────── generation integer (1..9 observed; higher = newer)
     └────────────────────────────── family/series letter(s): A C D F G Hpc I Im Is Inf M Mac P R T Trn U VT X Z
```

**Option letters** (customer-visible, security-relevant ones in bold):
`a`=AMD CPU, `g`=**AWS Graviton**, `i`=**Intel CPU**, `d`=instance-store NVMe, `n`=network-optimized, `e`=extra storage/memory, `z`=high CPU freq, `q`=Qualcomm, `b`=EBS-optimized block, `flex`=Flex (baseline-burst) tier, plus combinations (`idn`, `aedz`, `gn`, `gb`, `gd`). The letter is a **human-readable capability hint**, *not* an authorization token — nothing enforces that `g`=Graviton at the IAM layer (see Lens S null on `ec2:InstanceType` substring matching).

### 2.2 The `instancetypes` doc set (pages read)
| Page (mirror `/docs/ec2/latest/instancetypes/`) | Role |
|---|---|
| `instance-type-names.md` | **Target** — naming grammar + full option-letter table. |
| `instance-types.md` | Current-gen family lists; **end-of-sale notice** (U-9tb1/12tb1/18tb1/24tb1 → U7i, end of sale 2025-06-20); "equal share" shared-resource sentence; Burstable/Flex descriptions. |
| `ec2-instance-type-specifications.md` | Category descriptions; links to per-family pages (gp/co/mo/so/ac/hpc/pg). |
| `ec2-nitro-instances.md` | Nitro system, **NitroTPM / Nitro Enclaves / AMD SEV-SNP / encryption-in-transit** guarantees. |
| `ec2-instance-quotas.md` | On-Demand/Spot/Dedicated-Host/Capacity-Blocks quota tables (most default 0; Standard default 5; all adjustable via Service Quotas). |
| `ec2-instance-regions.md` | Per-region type availability (confirms region-dependent availability; contains SKU anomalies — see Lead X-7). |
| `doc-history.md` | Change log — confirms **very high NEW-type churn through 2026** (T8i 2026-09-15; R9g/R9gd Graviton5 2026-08-31; C9g/C9gd 2026-06-30; G7/G7e; Nitro-v6 M8in/M8ib/M8idn/M8idb/C8in families 2026-04..05; M9g/M9gd Graviton5 2026-06-09; X8aedz/X8i/C8a/R8a Turin 2025-12..2026-01). |

### 2.3 Behind-the-interface mechanisms (the parts with an actual trust boundary)
- **`DescribeInstanceTypes`** → `InstanceTypeInfo` (the authoritative per-type capability record: `ProcessorInfo`, `EbsInfo.EncryptionSupport`, `InstanceStorageInfo.EncryptionSupport`, `NetworkInfo.EncryptionInTransitSupported`, `ProcessorInfo.SupportedFeatures` (amd-sev-snp), `NitroTpmInfo`, `NitroEnclavesSupport`, `BareMetal`, `DedicatedHostsSupported`, `SupportedUsageClasses`, etc.). ~700+ types.
- **`GetInstanceTypesFromInstanceRequirements`** (Attribute-Based Instance Selection / ABIS) → `InstanceTypeInfoFromInstanceRequirements` (a thin wrapper carrying a **single** field, `instanceType`). Input `InstanceRequirements` includes `AllowedInstanceTypes`/`ExcludedInstanceTypes` (wildcard patterns), `InstanceGenerationSet` (current/previous), accelerator/CPU/memory bounds.
- **IAM gating keys** (from `list_ec2.md`): `ec2:InstanceType`, `ec2:Tenancy`, `ec2:Attribute`, `ec2:LaunchTemplate`, `ec2:IsLaunchTemplateResource`, plus the launch action family (`RunInstances`, `CreateFleet`, `RequestSpotInstances`, `RequestSpotFleet`, `ModifyInstanceAttribute`, `CreateLaunchTemplate[Version]`) and the separate `autoscaling:InstanceType`/`InstanceTypes` namespace.
- **Attestation keys** (KMS condition keys): `kms:RecipientAttestation:ImageSha384`, `kms:RecipientAttestation:PCR<0-15>`.

### 2.4 Assets
- **Customer-authored IAM policies** that gate launches on type/capability (the thing most likely to be *silently broken*).
- **AWS-shipped sample policies** (`ExamplePolicies_EC2.md` "Instance types" + "Launch templates" recipes) that customers copy verbatim.
- **The capability ground truth** customers trust (doc tables + `DescribeInstanceTypes` + ABIS output).
- **The Nitro security guarantees** (attestation, in-transit encryption, SEV-SNP memory encryption).

---

## 3. Trust-Boundary Map (Step 2)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller with type-capped IAM | The set of launchable instance types/hardware | `RunInstances`/sibling launch APIs evaluated against `ec2:InstanceType`/`ec2:Attribute`/launch-template keys | **Launching (or modifying into) a type/capability outside the documented cap is a breach of the customer's intended control.** |
| Policy author (customer or AWS sample) | The IAM evaluation engine | Condition key name + value + resource type the author *believes* enforces a cap | **A Deny/Allow that silently evaluates to no-effect (unknown key, case/namespace mismatch, uncovered sibling action) is a fail-open boundary.** |
| Customer security decision | Capability ground truth | Doc "Security specifications" table / ABIS selector vs `DescribeInstanceTypes` | **A security control built on a capability claim that the ground-truth API contradicts is a divergence breach (severity inherited from the consuming control).** |
| Attested enclave consumer | Attestation-gated KMS key | `kms:RecipientAttestation:*` key policy + default key-policy root Allow | **Decrypting/using an "attestation-gated" key *without* presenting a valid attestation document is a breach (W-2).** |
| Any customer surface | **AWS Nitro service plane** (hypervisor key, attestation PKI, cross-tenant memory, host scheduler) | — | **HARD STOP. Any identity/key/memory belonging to AWS's own fleet = disclosure, not a test.** |

---

## 4. API / Interface Inventory (Step 3)

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes / lens |
|---|---|---|---|---|---|---|---|
| `DescribeInstanceTypes` | GET-style | No | External | Returns `InstanceTypeInfo` capability records | Yes (SigV4) | Any EC2-authorized principal | **Global catalog, not tenant-scoped.** Ground-truth oracle for Lens U/X. |
| `GetInstanceTypesFromInstanceRequirements` (ABIS) | POST | No | External | Resolves `InstanceRequirements` → matching type list | Yes | Any EC2-authorized principal | Response carries **only** `instanceType` — zero capability fields echoed (Lead X-6 trust-then-verify). |
| `RunInstances` | POST | **Yes** | External | Launch; honors `ec2:InstanceType`/`ec2:Attribute`/`ec2:Tenancy` | Yes | Launch-authorized principals | Primary gated action. |
| `CreateFleet` / `RequestSpotInstances` / `RequestSpotFleet` | POST | **Yes** | External | Bulk/spot launch | Yes | Launch-authorized principals | **`ec2:InstanceType` coverage differs from RunInstances** → Lead SR-4 (sibling-API bypass). |
| `ModifyInstanceAttribute` | POST | **Yes** | External | Change an instance's type post-launch | Yes | Instance owner | `ec2:Attribute` **camelCase vs PascalCase** mismatch → Lead SR-2 (Deny void). |
| `CreateLaunchTemplate` / `CreateLaunchTemplateVersion` | POST | **Yes** | External | Author a launch template carrying a type | Yes | Launch-template-authorized | `Resource:"*"` in AWS sample → Lead SR-3 (template statement overrides type cap). |
| `autoscaling:*` (CreateAutoScalingGroup, etc.) | POST | **Yes** | External | ASG launches via SLR | Yes | ASG-authorized | **Separate `autoscaling:InstanceType(s)` namespace** → Lead SR-4. |
| KMS `Decrypt`/`GenerateDataKey` under attestation key | POST | varies | External | Enclave key use | Yes | Key-policy principals | Default root Allow bypasses attestation → Lead W-2. |

> No non-SDK/console-hidden instance-type API surfaced in the `instancetypes` docs. The under-tested knob here is **ABIS `InstanceRequirements` parameters** (`InstanceGenerationSet` default, wildcard `AllowedInstanceTypes`) — see Lens X.

---

## 5. Prioritized NEW / changed surface (Step 5 — concentrate fire here)

The `doc-history.md` churn is the loudest signal on this surface: **AWS ships new instance types almost weekly**, each introducing a new `ec2:InstanceType` string value and new capability flags. Every one of those is a value that **pre-existing customer wildcard allow/deny policies and ABIS selectors silently expand to cover** without the author's knowledge.

Concentrate on:
1. **Wildcard/generation-set scope creep** — any policy or ABIS selector using `*` or `InstanceGenerationSet` grows its covered set every time AWS ships a SKU (Lead X-5, SR-wildcards). Highest leverage because it is *structurally* guaranteed to drift.
2. **New hardware capability (SEV-SNP, NitroTPM, Nitro v6, Graviton5) on new types** reachable through an *old* capability-blind allow policy (Lead X-2, SR-1).
3. **Nitro-v6 / Graviton5 families (M8*/M9g/R9g 2026)** whose "Security specifications" doc rows may lag or lead the `DescribeInstanceTypes` ground truth (Lead U-1/U-3).

---

## 6. Recommended Areas of Focus (firing leads, by lens)

> Field-level evidence (line numbers, exact policy text) lives in the three companion scratch files. Severities below are the skill's doc-only estimates; a hunter settles them.

### Lens S / R — Condition-key scoping & AWS-authored IAM-artifact audit  *(see `instancetypes-scratch-lensSR.md`)*
- **SR-1 (Medium) — Inert Deny on hallucinated hardware keys.** **Claim:** a customer Deny keyed on `ec2:InterfaceType` / `ec2:BareMetal` / `ec2:NitroVersion` / `ec2:AcceleratorType` / `ec2:EnclaveOptions` is silently inert. **Mechanism:** none of those keys exist in `list_ec2.md`; an unknown condition key makes the statement not match → no Deny. **Oracle:** policy simulator / live launch of the "blocked" hardware succeeds. **Sev:** Medium (customer footgun; very easy to author by analogy to the option letters).
- **SR-2 (High) — `ec2:Attribute` case mismatch voids `ModifyInstanceAttribute` Deny.** **Claim:** a Deny on `ec2:Attribute = InstanceType` (PascalCase) never matches because the API emits `instanceType` (camelCase). **Mechanism:** `API_ModifyInstanceAttribute.md` line 23 vs 74. **Oracle:** `ModifyInstanceAttribute` resizing into a capped type succeeds despite the Deny. **Sev:** High.
- **SR-3 (High) — AWS sample launch-template recipe overrides the instance-type cap.** **Claim:** combining AWS's own `ExamplePolicies_EC2.md` "Instance types" recipe with its "Launch templates" recipe lets the launch-template statement (`Resource:"*"`) satisfy `RunInstances` while the type cap is bypassed. **Mechanism:** the two shipped recipes compose fail-open. **Oracle:** launch a disallowed type via a launch template under the combined policy. **Sev:** High (Tier-2 AWS-authored sample defect).
- **SR-4 (High) — Sibling launch APIs escape a `RunInstances`-scoped cap.** **Claim:** `CreateFleet`, `RequestSpotInstances`/`RequestSpotFleet`, and `autoscaling:*` can launch capped types because `ec2:InstanceType` coverage/semantics differ (Spot request entries in `list_ec2.md` ~9465-9480 lack the key; autoscaling is a separate namespace launching via SLR). **Oracle:** launch disallowed type via each sibling path. **Sev:** High.
- **SR-5 (Medium-High) — Post-launch self-widen.** **Claim:** a principal launches an allowed small type, then `ModifyInstanceAttribute`-resizes to a disallowed large/GPU type. **Oracle:** resize succeeds. **Sev:** Medium-High (compounds SR-2).

### Lens U / X — Documented-guarantee vs ground truth & capability selection  *(see `instancetypes-scratch-lensUX.md`)*
- **U-1 (Low, AWS-owned; inherits consuming severity) — Per-type doc "Security specifications" table vs `DescribeInstanceTypes`.** **Claim:** a security table cell (EBS encryption / instance-store encryption / in-transit / SEV-SNP / NitroTPM / Enclaves) for some type disagrees with `InstanceTypeInfo`. **Oracle:** diff all ~700 types' six security columns against the API. **Sev:** Informational–Low alone; inherits the severity of any control that trusts the wrong cell.
- **U-2 (Low) — AMD SEV-SNP size-tier "cliff".** **Claim:** SEV-SNP support varies by *size within* a family (observed in M6a) but the doc reads as family-wide. **Oracle:** `ProcessorInfo.SupportedFeatures` per size. **Sev:** Low (a memory-encryption control scoped to "M6a" may cover non-SEV sizes).
- **U-3 (Low) — "Nitro v3+ ⇒ encryption in transit" blanket claim vs per-type precision.** **Oracle:** `NetworkInfo.EncryptionInTransitSupported` per type vs the blanket statement. **Sev:** Low (see Y-1 for the scope caveats).
- **X-4 (Medium) ⭐ — ABIS can return end-of-sale types.** **Claim:** `GetInstanceTypesFromInstanceRequirements` with default `InstanceGenerationSet` (current **and** previous) can return end-of-sale U-9tb1/12tb1/18tb1/24tb1 (end of sale 2025-06-20) — no API field encodes "end of sale" — producing a **selection-time vs launch-time validator divergence**. **Oracle:** ABIS call returns an end-of-sale type that then fails or behaves unexpectedly at `RunInstances`. **Sev:** Medium.
- **X-5 (Medium) ⭐ — Wildcard `AllowedInstanceTypes`/`ExcludedInstanceTypes` has no capability/version pin.** **Claim:** a selector or IAM value like `m*` / `*.xlarge` auto-expands to every future SKU AWS ships (see §5 churn), so an allow-set silently grows to include newer, more capable, or SEV/NitroTPM-bearing types the author never evaluated. **Oracle:** compare the matched set before/after a doc-history SKU addition. **Sev:** Medium (structural, guaranteed to drift).
- **X-6 (Low-Medium) — ABIS trust-then-verify TOCTOU.** **Claim:** ABIS echoes *zero* capability fields (only `instanceType`), so any consumer must re-`Describe` each result; a consumer that trusts the selector's filter without re-verifying inherits a TOCTOU gap. **Oracle:** selector filtered on a capability bound returns a type; confirm the capability is *not* re-checked downstream. **Sev:** Low-Medium.
- **X-7 (Informational) — Region-page SKU anomalies.** **Claim:** `ec2-instance-regions.md` lists `I3p` and `G3s` that appear **nowhere else** in the `instancetypes` set (not in the naming grammar, family pages, or doc-history), only in `us-gov-west-1`. **Mechanism:** confirmed by grep — `i3p`/`g3s` occur only in `ec2-instance-regions.md`. **Oracle:** `DescribeInstanceTypes` in GovCloud for those type names. **Sev:** Informational (doc-consistency / possible GovCloud-only or stale SKU); note as a ground-truth-vs-doc gap, not a vuln.

### Lens W / Y / L — Nitro attestation, encryption-in-transit, resource-share guarantees  *(see `instancetypes-scratch-lensWVL.md`)*
- **W-2 (High) ⭐ — Attestation-gated KMS key reachable *without* attestation.** **Claim:** a key the docs present as "only usable from an attested enclave" is usable by the account root because the **default KMS key policy's account-root full-access Allow** is not removed when the attestation condition is added. **Mechanism:** AWS sample omits removing the root grant. **Oracle:** `Decrypt` under the key from a non-enclave principal succeeds. **Sev:** High (defeats the whole attestation control).
- **W-3 (Medium-High) — `PutKeyPolicy` accepts bogus/malformed attestation conditions.** **Claim:** a PCR id that doesn't exist, a malformed PCR value, or a `StringLike` wildcard on the attestation value is accepted silently → the author believes the key is gated when it is effectively fail-open. **Oracle:** author a bogus condition, then use the key without a matching attestation. **Sev:** Medium-High.
- **W-4 (Medium) — PCR3+PCR8 "best flexibility" pairing never binds code (PCR0).** **Claim:** the doc-recommended "flexible" PCR pairing attests parent-instance role / enclave-image-signing but not the enclave *code measurement*, so a different code image under the same signer passes. **Oracle:** two enclaves, same PCR8 signer, different PCR0, both pass the key policy. **Sev:** Medium.
- **W-5 (Medium) — All-zero debug PCRs vs all-zero reference values.** **Claim:** an enclave run in debug mode presents all-zero PCRs that can collide with a carelessly authored all-zero reference value. **Oracle:** debug enclave satisfies a production key policy. **Sev:** Medium.
- **W-6 (Informational) — Capability ground truth.** `.metal*` is excluded from Nitro Enclaves; the NitroTPM allow-list is **narrower** than "built on Nitro." Feeds U-1.
- **Y-1 (Medium) ⭐ — "Automatic" encryption-in-transit silently exits scope.** **Claim:** the "automatic encryption between supported instances" guarantee holds only for specific type pairings, same Region, same-VPC with no intervening LB/TGW/… — and there is **zero per-flow verifiability** exposed to the customer, so traffic the customer believes is encrypted silently is not. **Oracle:** identify a documented pairing/topology where the guarantee lapses; note the absence of any per-flow attribute. **Sev:** Medium.
- **L-1 (Medium, split) — "Equal share" guarantee has no denominator/SLA/fairness metric.** **Claim:** `instance-types.md` line 13's "equal share" of a shared resource defines no denominator, no SLA, no fairness-violation metric → unfalsifiable as written. **Oracle:** documentation analysis only — **a live cross-tenant demonstration is a HARD STOP.** **Sev:** Medium as a doc/guarantee gap; the exploit half is out of scope.

---

## 7. Threat-Model Test Objectives (handoff checklist for the hunter)

Execute against an **authorized** test account only, with synthetic/canary resources, tearing down everything created. Stop at the first service-plane signal.

1. **Build the three IAM caps** AWS's own samples and a typical customer would write (instance-type allow-list; launch-template recipe; SEV-SNP/NitroTPM "capability" Deny) and **try to bypass each** via: (a) a sibling launch API (SR-4), (b) `ModifyInstanceAttribute` resize (SR-2/SR-5), (c) a launch template (SR-3), (d) a hallucinated-key Deny that never matches (SR-1).
2. **Diff capability ground truth:** pull all `DescribeInstanceTypes` records and diff the six security columns against the per-type doc tables (U-1/U-2/U-3); record every mismatch and whether a plausible control would trust the wrong side.
3. **ABIS drift:** craft `InstanceRequirements` with default `InstanceGenerationSet` and a wildcard allow-set; confirm it returns end-of-sale (X-4) and newer-than-authored (X-5) types, and that no capability field is echoed for re-verification (X-6). Query GovCloud for `I3p`/`G3s` (X-7).
4. **Attestation gating:** stand up an attestation-gated KMS key per the AWS Nitro Enclaves sample; confirm whether the **account root** can still `Decrypt` without attestation (W-2), and whether `PutKeyPolicy` accepts a bogus PCR condition (W-3). **Do not** attempt to read another tenant's enclave or touch the attestation PKI — hard stop.
5. **In-transit encryption scope:** from the docs alone, enumerate the pairings/topologies where the "automatic" guarantee lapses and confirm no per-flow attribute exists (Y-1). No live cross-tenant traffic capture.

---

## 8. Out-of-scope & Null-hypothesis ledger (Step 4 completeness — pages named)

Each null below names the page(s) checked, per skill discipline. A null here means "no lead on documentation evidence," **not** "unexamined."

| Lens | Verdict | Evidence (pages checked) |
|---|---|---|
| **A — Cross-tenant IDOR** | **Null.** | `instance-type-names.md`, `instance-types.md`, `ec2-instance-type-specifications.md`, `ec2-instance-regions.md`: the instance-type catalog is a **global, non-tenant, read-only reference** — no per-tenant instance-type resource, ID, or ARN exists to confuse-name or enumerate. (Cross-tenant *compute* isolation lives in Nitro = hard stop, not IDOR.) |
| **B — Confused deputy / PassRole** | **Null for the catalog; pointer.** | No instance-type API in this set accepts a role ARN. The PassRole surface attaches to `RunInstances` *IamInstanceProfile*, which is an EC2-launch concern documented elsewhere (`iam-roles-for-amazon-ec2`), not in `instancetypes`. Out of this target's scope. |
| **C — Credential vending / session scope** | **Null.** | No STS/session-policy/credential-vending mechanism in the `instancetypes` set. |
| **D — Data→control-plane escape** | **Hard-stop-adjacent / Null for docs.** | `ec2-nitro-instances.md`: the only data→control path here is Nitro isolation itself = **HARD STOP, do not probe** (scratch-lensWVL V/D-1). "Bare metal ≠ tenancy exclusivity" conflation noted (V/D-2, Low). |
| **E — RBAC privesc** | **Fires via S/R.** | Covered as the instance-type-cap bypass family (SR-1..SR-5); no separate built-in-role model in the `instancetypes` set. |
| **F — Translation / wire injection** | **Null.** | `instance-type-names.md`: the naming grammar is parsed by AWS, not a customer-supplied-string→downstream-language transform. Instance-type strings are closed-enum, server-validated; no injection sink documented. |
| **G — SSRF** | **Null.** | Checked `instance-type-names.md`, `instance-types.md`, `ec2-instance-type-specifications.md`, `ec2-instance-quotas.md`, `ec2-instance-regions.md`, `ec2-nitro-instances.md`: **no field the service dereferences** (no URL/URI/endpoint/callback/logo/webhook input anywhere in this doc set). |
| **H — KMS / encryption-context** | **Fires via W.** | Attestation-condition / key-policy leads captured as W-2..W-5. |
| **I — Tagging / ABAC** | **Weak null / pointer.** | `ec2:InstanceType` is a request key, not a tag; ABAC on instance *tags* (`aws:ResourceTag`) is a general EC2 concern not specific to the type catalog. Note: a type-cap built on tags rather than `ec2:InstanceType` would share SR-4's sibling-API gap. |
| **J — OAuth / 3P** | **Null.** | No third-party identity/integration in the `instancetypes` set. |
| **K — Prompt injection** | **Null.** | No LLM/agent consumes instance-type doc content in this surface. |
| **L — Resource exhaustion / DoS** | **Split.** | "Equal share" guarantee gap = L-1 (Medium, doc-only; live demo = hard stop). CPU-credit self-DoS (Burstable) and Flex 95% are **self-caused, out of scope** (`instance-types.md` Burstable/Flex sections). Quota defaults (most 0; Standard 5) are a **cost-abuse guardrail, working as intended** (`ec2-instance-quotas.md`). |
| **M — Shared-identifier interception** | **Null.** | Instance-type names are a public global enum, intentionally shared and non-secret; no interception semantics. |
| **N — ARN / namespace migration** | **Fires narrowly via X-4.** | "Previous generation" / end-of-sale types persist in the ABIS namespace with no "retired" field (`instance-types.md` end-of-sale notice) → X-4. No ARN rename surface for types. |
| **O — Audit-log evasion** | **Null.** | No instance-type-specific logging claim in this set; CloudTrail coverage of `RunInstances`/`ModifyInstanceAttribute` is a general EC2 concern. |
| **P — Identity proofing / registration** | **Null.** | No registration/onboarding/approval gate in the `instancetypes` set. |
| **Q — File upload** | **Null.** | No blob/upload/attachment field anywhere in the pages listed under Lens G. |
| **T — Cross-service secret reachability** | **Null for catalog; W-2 is the closest.** | No service-generated secret persisted by the instance-type surface. The attestation-key reachability (W-2) is the nearest analog and is captured there. |
| **U — Documented-guarantee vs enforcement** | **Fires.** | U-1/U-2/U-3, Y-1, L-1. |
| **V — Network segmentation** | **Hard stop.** | Nitro isolation (scratch-lensWVL V/D-1). |
| **W — Attestation-conditioned authz** | **Fires.** | W-2..W-6. |
| **X — Action-family / twin / legacy parity** | **Fires.** | X-4..X-7 (ABIS generation-set + wildcard parity, end-of-sale legacy, region anomalies). |
| **Y — Transport / TLS / signature** | **Fires.** | Y-1 (in-transit encryption scope). |
| **S — Condition-key scoping semantics** | **Fires.** | SR-1..SR-5. |
| **R — AWS-authored IAM-artifact audit** | **Fires.** | SR-3 (ExamplePolicies_EC2 composition). |
| **AA — Share / revoke lifecycle** | **Null.** | No share/invite/revoke resource for instance types. |
| **BB — Canonicalization / parser differential** | **Weak lead, folds into S.** | The one canonicalization risk is the `ec2:Attribute` case differential (SR-2) and option-letter substring matching on `ec2:InstanceType` wildcards (SR-1/X-5); no separate parser-differential surface. |
| **CC — Trusted-upstream-context injection** | **Null.** | No upstream context field in this set. |
| **DD — Cache-key vs authz-key divergence** | **Null.** | No caching-authz surface documented for the type catalog. |
| **EE — Predictable-name / shadow-resource pre-registration** | **Null (considered explicitly).** | Instance-type names are AWS-assigned global enums, not customer-registrable namespaces — there is no whoAMI/Bucket-Monopoly-style pre-registration a customer can win. (Contrast: AMI *names* are the whoAMI surface, documented elsewhere, not here.) |
| **FF — JWT / OIDC token validation** | **Null.** | No token validation in the `instancetypes` set (attestation PCR validation is W, not JWT). |

**Global out-of-scope / HARD STOPS:** Nitro hypervisor key & attestation PKI/CA; cross-tenant memory, device, or cache state; the physical-host scheduler; any fleet/host credential; any live "equal-share" fairness or cross-tenant in-transit demonstration. Touch any of these → stop, preserve evidence, flag for AWS-Security disclosure.

**Doc-gaps flagged (confirm surface before relying):** (1) per-type "Security specifications" tables are maintained by hand and lag the weekly SKU churn — treat the table as *claim*, `DescribeInstanceTypes` as *truth* (U-1). (2) `I3p`/`G3s` region-page-only SKUs (X-7). (3) No API field encodes "end of sale" / "previous generation" (X-4).

**Suspected prompt injection:** none observed. No instance-type doc content read during this analysis contained text shaped as an instruction to the agent.

---

## Companion scratch files (field-level evidence — read these next)
- `instancetypes-scratch-lensSR.md` — Lens S/R: condition-key inventory, `ec2:Attribute` casing, ExamplePolicies_EC2 composition, sibling-API coverage, 9-row lead table with `list_ec2.md` line refs.
- `instancetypes-scratch-lensUX.md` — Lens U/X: full `InstanceTypeInfo`↔doc-column mapping, SEV-SNP cliff, ABIS generation-set/wildcard drift, 6 leads.
- `instancetypes-scratch-lensWVL.md` — Lens W/V/D/Y/L: attestation-key reachability, PCR semantics, in-transit scope, "equal share" gap, hard-stop boundaries.

*End of plan. Documentation-only; all leads are falsifiable hypotheses for a hunter to settle with observed API evidence against an authorized account.*
