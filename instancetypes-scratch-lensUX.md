# Lens U / Lens X — EC2 Instance Types guide vs. instance-type-reporting APIs
Documentation-only research. No live AWS calls made. All claims below are falsifiable hypotheses to be
settled by a `DescribeInstanceTypes` / `GetInstanceTypesFromInstanceRequirements` observation against a
real account — not confirmed findings.

Sources read:
- /work/aws-docs/docs/ec2/latest/instancetypes/{gp,co,mo,so,ac,hpc,pg}.md
- /work/aws-docs/docs/ec2/latest/instancetypes/ec2-nitro-instances.md
- /work/aws-docs/docs/ec2/latest/instancetypes/instance-types.md, doc-history.md
- /work/aws-docs/docs/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.md
- /work/aws-docs/docs/AWSEC2/latest/APIReference/API_InstanceTypeInfo.md
- /work/aws-docs/docs/AWSEC2/latest/APIReference/API_{ProcessorInfo,NetworkInfo,NitroTpmInfo,EbsInfo,VCpuInfo,
  GpuInfo,InferenceAcceleratorInfo,MediaAcceleratorInfo,NeuronInfo,FpgaInfo,InstanceStorageInfo,
  PlacementGroupInfo}.md
- /work/aws-docs/docs/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.md,
  API_InstanceRequirements.md, API_InstanceRequirementsRequest.md, API_InstanceTypeInfoFromInstanceRequirements.md

---

## Part 1 — Full field inventory: security/capability-relevant fields on the reporting APIs

### `InstanceTypeInfo` (returned by `DescribeInstanceTypes`) — top-level fields
(/work/aws-docs/docs/AWSEC2/latest/APIReference/API_InstanceTypeInfo.md)

| Field | Type | Security relevance |
|---|---|---|
| `autoRecoverySupported` | Boolean | availability/resilience control claim |
| `bareMetal` | Boolean | isolation model (no hypervisor) — changes trust boundary for side-channel claims |
| `burstablePerformanceSupported` | Boolean | CPU credit/throttling model (confused-deputy-adjacent: perf claims) |
| `currentGeneration` | Boolean | the ONLY "is this type still a going concern" signal exposed — see Lens X §3 |
| `dedicatedHostsSupported` | Boolean | tenancy isolation control |
| `ebsInfo` → `encryptionSupport` (`EbsInfo.encryptionSupport`, `unsupported|supported`) | String | storage-at-rest crypto guarantee |
| `ebsInfo` → `nvmeSupport` | String | — |
| `freeTierEligible` | Boolean | billing/abuse surface, not security per se |
| `gpuInfo`, `inferenceAcceleratorInfo`, `mediaAcceleratorInfo`, `neuronInfo`, `fpgaInfo` | objects | accelerator presence — relevant to confidential-computing/attestation claims (GPU TEE) |
| `hibernationSupported` | Boolean | data-at-rest-on-disk-after-stop guarantee |
| `hypervisor` | String `nitro|xen` | root trust boundary — Xen vs Nitro security model differ materially |
| `instanceStorageInfo.encryptionSupport` | String `unsupported|required` | instance-store crypto guarantee |
| `instanceStorageSupported` | Boolean | — |
| `networkInfo.encryptionInTransitSupported` | **Boolean** | **the exact field the Nitro-page "Encryption in transit" column claims to mirror** |
| `networkInfo.efaSupported`, `enaSupport`, `enaSrdSupported`, `flexibleEnaQueuesSupport` | — | network path integrity/perf claims |
| `nitroEnclavesSupport` | String `unsupported|supported` | **the exact field the "Nitro Enclaves" column claims to mirror** |
| `nitroTpmSupport` / `nitroTpmInfo.SupportedVersions` | String / array | **the exact field the "NitroTPM" column claims to mirror** |
| `phcSupport` | String `unsupported|supported` | PTP hardware clock — time-source integrity, used in some compliance/log-correlation controls |
| `placementGroupInfo.SupportedStrategies` | array | — |
| `processorInfo.SupportedFeatures` (`amd-sev-snp`, `nested-virtualization`) | array of strings | **the exact field the "AMD SEV-SNP" column claims to mirror** |
| `rebootMigrationSupport` | String `unsupported|supported` | live-migration-on-reboot — matters for physical-host-pinning threat models |
| `SupportedBootModes` | array `legacy-bios|uefi` | Secure Boot / UEFI attestation precondition |
| `supportedInRegion` | Boolean | regional availability, not capability |
| `SupportedRootDeviceTypes` | array `ebs|instance-store` | — |
| `SupportedUsageClasses` | array `spot|on-demand|capacity-block` | — |
| `SupportedVirtualizationTypes` | array `hvm|paravirtual` | legacy virtualization trust model |
| `vCpuInfo` | object | — |

`DescribeInstanceTypes` `Filter.N` exposes the identical set as filter keys (`nitro-enclaves-support`,
`nitro-tpm-support`, `nitro-tpm-info.supported-versions`, `network-info.encryption-in-transit-supported`,
`processor-info.supported-features` [`amd-sev-snp`], `supported-boot-mode`, `bare-metal`,
`dedicated-hosts-supported`, `hibernation-supported`, `ebs-info.encryption-support`,
`instance-storage-info.encryption-support`, `supported-virtualization-type`, `supported-root-device-type`).
This is the control-plane surface that is supposed to be the single source of truth the guide's HTML
tables summarize.

**Doc-gap note:** No field anywhere in `InstanceTypeInfo` encodes "end of sale" / "no longer available for
new launches." The only generation-adjacent fields are `currentGeneration` and `supportedInRegion`. See
Lens X §3.

### `GetInstanceTypesFromInstanceRequirements` / `InstanceRequirements` (ABIS) relevant fields
(/work/aws-docs/docs/AWSEC2/latest/APIReference/API_InstanceRequirements.md)

- `BareMetal` (`included|required|excluded`, default `excluded`)
- `BurstablePerformance` (`included|required|excluded`, default `excluded`)
- `LocalStorage` (`included|required|excluded`, default `included`)
- `InstanceGenerationSet` (`current|previous`, **default = both** — i.e. end-of-sale/previous-gen types are
  returned unless the caller explicitly filters them out)
- `RequireEncryptionInTransit` (Boolean, default `false`) — maps to `networkInfo.encryptionInTransitSupported`
- `RequireHibernateSupport` (Boolean, default `false`)
- `AllowedInstanceTypeSet` / `ExcludedInstanceTypeSet` — wildcard string patterns (`c5*`, `m5a.*`, `r*`, `*3*`),
  mutually exclusive, matched purely by instance-type-name string, **not** by any capability/version pin.
- No parameter maps to `nitroTpmSupport`, `nitroEnclavesSupport`, `phcSupport`, `rebootMigrationSupport`,
  `processorInfo.SupportedFeatures` (AMD SEV-SNP), or `SupportedBootModes`. ABIS cannot select/exclude on
  these at all — doc-gap, confirm surface first (maybe deliberate scope limitation of ABIS, but it means a
  security-sensitive selection ("give me only confidential-computing-capable types") cannot be expressed
  through this API and must be done client-side via `DescribeInstanceTypes` first).

`InstanceTypeInfoFromInstanceRequirements` (the actual per-item response object) has exactly **one** field:
`instanceType` (String). (/work/aws-docs/docs/AWSEC2/latest/APIReference/API_InstanceTypeInfoFromInstanceRequirements.md)
It returns bare instance-type names with **no capability echo at all** — the caller must re-query
`DescribeInstanceTypes` to learn anything about what was actually matched. This is itself a Lens-X-relevant
gap: a consumer cannot verify from the ABIS response alone that a returned type actually satisfies a
security-relevant requirement that ABIS has no parameter for (TPM, Enclaves, SEV-SNP, boot mode) — they can
only trust that ABIS's internal matching logic enforced it for the few attributes it does expose
(`RequireEncryptionInTransit`, `RequireHibernateSupport`, `BareMetal`), and must do a second round-trip for
everything else, creating a TOCTOU window if capacity/instance type lifecycle changes between calls.

---

## Part 2 — Doc evidence: the guide's per-family "Security specifications" tables

Each family page (`gp.md`, `co.md`, `mo.md`, `so.md`, `ac.md`, `hpc.md`, `pg.md`) carries a `## Security
specifications` section (anchor `#<family>_security`) with an identical 7-column table:

```
<tr><th>Instance type</th><th>EBS encryption</th><th>Instance store encryption</th>
<th>Encryption in transit</th><th>AMD SEV-SNP</th><th>NitroTPM</th><th>Nitro Enclaves</th></tr>
```

This table publishes, per concrete instance type (e.g. `m5dn.4xlarge`, `c5n.metal`, `u-9tb1.112xlarge`), a
Yes/No value for exactly the six capabilities that correspond 1:1 to API fields:

| Doc column | API field |
|---|---|
| EBS encryption | `InstanceTypeInfo.ebsInfo.encryptionSupport` (`supported`) |
| Instance store encryption | `InstanceTypeInfo.instanceStorageInfo.encryptionSupport` (`required`/`unsupported`) or "Instance store not supported" ⇒ `instanceStorageSupported=false` |
| Encryption in transit | `InstanceTypeInfo.networkInfo.encryptionInTransitSupported` |
| AMD SEV-SNP | `InstanceTypeInfo.processorInfo.SupportedFeatures` contains `amd-sev-snp` |
| NitroTPM | `InstanceTypeInfo.nitroTpmSupport` |
| Nitro Enclaves | `InstanceTypeInfo.nitroEnclavesSupport` |

This is a complete, falsifiable, per-SKU dataset — the ideal Lens-U substrate: ~700+ concrete
(doc-cell, API-field) pairs that can be diffed mechanically against a live `DescribeInstanceTypes` call.

Separately, `ec2-nitro-instances.md` publishes a coarser **version-level generalization**:
"Nitro v3 → **Encryption in transit**" (and implicitly, by omission, that Nitro v2 and earlier do not have
it) — i.e. a blanket claim "every type built on Nitro v3+ supports encryption in transit." The per-family
tables are consistent with this blanket claim for every row spot-checked (M5/M5a/M5ad/M5d = Nitro v2 → "No";
M5dn/M5n/M5zn = Nitro v3 → "Yes", including their `.metal` variants; C5n = Nitro v3 → "Yes" throughout;
U-9tb1/12/18/24 = Nitro v3 → "Yes" throughout). No internal contradiction was found in the sampled rows, but
the full table (700+ rows across 7 pages) was not exhaustively diffed — see Lead 1 for the oracle to do that
mechanically and Lead 2 for the AMD SEV-SNP size-tier cliff which **is** a genuine intra-family
inconsistency (though plausibly intentional/correct).

---

## LEADS

### Lead 1 — Doc security table vs. `DescribeInstanceTypes` ground truth (Lens U, primary)

**Claim:** For every instance type listed in a family page's "Security specifications" table, the
Yes/No/"Instance store not supported" cell values exactly match what `DescribeInstanceTypes` reports for
that `InstanceType` in `us-east-1` (or whichever region the guide implicitly documents against — the guide
does not state a region, which is itself worth flagging: capability support can be region-dependent via
`supportedInRegion`/hardware rollout, but the doc tables carry no per-region caveat).

**Mechanism (doc evidence):**
- `/work/aws-docs/docs/ec2/latest/instancetypes/gp.md` (and co/mo/so/ac/hpc/pg `.md`), section `## Security
  specifications`, e.g. gp.md:1697 `m5.large` → EBS encryption=Yes, Encryption in transit=No, AMD SEV-SNP=No,
  NitroTPM=Yes, Nitro Enclaves=No.
- API ground truth: `InstanceTypeInfo.ebsInfo.encryptionSupport`, `.networkInfo.encryptionInTransitSupported`,
  `.processorInfo.SupportedFeatures[]` (contains `amd-sev-snp`), `.nitroTpmSupport`,
  `.nitroEnclavesSupport` (API_InstanceTypeInfo.md lines 38-131).

**Confirm/Refute oracle:** Run
`aws ec2 describe-instance-types --instance-types m5.large m5n.large m5n.metal m6a.large m6a.metal c5n.metal
u-9tb1.112xlarge ... (full enumerated set)` and diff each of the 6 booleans against the doc table cell for
that exact instance type. Any mismatch (e.g. doc says NitroTPM=Yes but API returns `nitroTpmSupport:
unsupported`, or doc says Encryption-in-transit=No for a type the API marks `true`) is a confirmed Lens-U
defect. Pay special attention to **newly-added rows** (M8-generation, M9g/M9gd, G6f/Gr6f, P6-B200/B300,
Hpc8a — all added per `doc-history.md` in 2025/2026) since these are most likely to have stale/placeholder
values if the doc table is hand-maintained separately from the API's internal capability database.

**Preconditions:** Read access to `ec2:DescribeInstanceTypes` (unauthenticated-safe — this is a read-only,
unauthenticated-pricing-tier-irrelevant describe call available to any IAM principal with the default
EC2 read permission; no special privilege needed. Can be run with `--dry-run` even without IAM permission to
merely confirm the call shape, though dry-run won't return data).

**Severity if true:** Informational/Low as a pure doc-vs-API inconsistency (AWS-owned documentation bug).
Downstream severity inherits whatever control a customer built on the false claim — e.g. a compliance
program that greenlit a workload for "data-in-transit encryption required" controls based on reading the
doc table instead of calling the API, when the API would have reported `false`. That is a customer-side
control-gap, not an AWS authZ bypass, but it is the kind of "documented guarantee contradicts enforcement"
finding Lens U is targeting. Likewise for NitroTPM/Nitro Enclaves underpinning an attestation chain (e.g.
confidential-computing or boot-integrity controls keyed off the doc table rather than a live describe call).

---

### Lead 2 — AMD SEV-SNP support "cliff" within a single instance family (Lens U, secondary / self-consistency)

**Claim:** Within the M6a family, SEV-SNP support is documented as size-dependent: `m6a.large` and
`m6a.xlarge` = Yes, but `m6a.2xlarge`...wait — re-check: actual rows show `m6a.large`=Yes, `m6a.xlarge`=Yes,
`m6a.2xlarge`=Yes, `m6a.4xlarge`=Yes, `m6a.8xlarge`=Yes, then `m6a.12xlarge` and larger (16xlarge, 24xlarge,
32xlarge, 48xlarge, metal) = No. If this tier boundary is real (plausibly due to a single-NUMA-node
requirement for SEV-SNP), it should hold as a **hard architectural constraint**, meaning the *API* field
`processorInfo.SupportedFeatures` must also flip at exactly `m6a.12xlarge` and never for a smaller size. If
the doc's cliff point is off-by-one relative to the API's actual cliff point (e.g. doc says `8xlarge`=Yes but
API says `8xlarge` lost SEV-SNP), that's a direct Lens-U defect with a concrete security impact: a customer
provisioning for confidential computing at `m6a.8xlarge` on the strength of the doc table would get an
instance that silently lacks memory encryption/attestation if the API disagrees.

**Mechanism:** `/work/aws-docs/docs/ec2/latest/instancetypes/gp.md` lines ~76-86 (M6a block in the Security
specifications table). API field: `InstanceTypeInfo.processorInfo.SupportedFeatures` valid value
`amd-sev-snp` (API_ProcessorInfo.md:23-26), filterable via `processor-info.supported-features` on
`DescribeInstanceTypes` (API_DescribeInstanceTypes.md:67).

**Confirm/Refute oracle:** `aws ec2 describe-instance-types --filters
Name=processor-info.supported-features,Values=amd-sev-snp --instance-types m6a.large m6a.xlarge m6a.2xlarge
m6a.4xlarge m6a.8xlarge m6a.12xlarge m6a.16xlarge ... m6a.metal` and compare the returned set to the doc's
Yes-rows. Also repeat for M7a, M8a, C6a/C7a/C8a, R6a/R7a/R8a — every AMD family should have the same cliff
semantics; if the cliff point differs by family inconsistently (not clearly explained by a documented NUMA
rule), that is further evidence of a maintenance/transcription error rather than a real hardware constraint.

**Preconditions:** Same as Lead 1 — plain `DescribeInstanceTypes` read access.

**Severity if true:** Informational/Low (doc bug) with inherited severity = whatever a customer's
confidential-computing attestation policy assumed. Could be classified Medium if an organization's actual
compliance sign-off (e.g. PCI/FedRAMP control narrative) cites the EC2 Instance Types guide table verbatim
as evidence of SEV-SNP coverage for a specific instance size, and the live API contradicts it.

---

### Lead 3 — Nitro-version "Encryption in transit" blanket claim vs. per-type table precision (Lens U, cross-page consistency)

**Claim:** `ec2-nitro-instances.md`'s "Network feature support" section states as a per-*version* bullet,
not per-instance-type: "**Nitro v3** + Encryption in transit." (ec2-nitro-instances.md:58-61). This is a
coarser claim than the per-family tables and is explicitly a *summary*: "The following content summarizes
key networking capabilities for each version of the Nitro System" (line 35). The risk is a reader (or an
automated compliance-mapping tool) that keys off the **Nitro-version-to-feature table alone** (coarse) rather
than the per-instance-type table (fine-grained), inferring "my instance is on Nitro v3 per the Hypervisor
column in the Platform-summary table, therefore it has encryption in transit" — skipping the per-type
Security-specifications table. Because the "Features are cumulative" note (line 40) states newer Nitro
versions inherit older features, a reader might further assume *every* Nitro v4/v5/v6 type also has it. That
syllogism is actually sound per the sampled rows (all v4+ GP/CO/MO/HPC rows checked are "Yes") — but the doc
never states a machine-checkable guarantee that NO exception exists; it only says "except where explicitly
stated otherwise" (line 40) without listing exceptions. If even one Nitro v3+ instance type exists whose API
`encryptionInTransitSupported` is `false` (e.g. a HPC/accelerated-computing type with EFA-only networking
that bypasses the standard ENA path, or a Mac-metal type), the version-level summary becomes a false
blanket guarantee that the per-type table (if also wrong, per Lead 1) would not catch either.

**Mechanism:** ec2-nitro-instances.md:32-41 ("Network feature support" + cumulative-features note);
cross-reference against every per-family Security-specifications table's "Encryption in transit" column for
all instance types the Nitro page assigns to v3/v4/v5/v6 (full membership lists at ec2-nitro-instances.md:75-161).

**Confirm/Refute oracle:** Enumerate every instance type the Nitro page assigns to v3 or later (lines 76-161),
call `DescribeInstanceTypes` for each, and check `networkInfo.encryptionInTransitSupported`. Any `false`
among a Nitro-v3+ type is a direct refutation of the version-level blanket claim and should be flagged
regardless of whether the per-family table (Lead 1) independently also gets it wrong — these are two
separate claims that could fail independently (one false, one true) or together.

**Preconditions:** `DescribeInstanceTypes` read access; full enumeration of ~250 instance types across the
Nitro v3+ membership lists.

**Severity if true:** Informational/Low (doc-owned); inherited severity = compliance-control severity for
whoever relied on "my fleet is on Nitro v3+, therefore encryption in transit is guaranteed" as an
inter-instance confidentiality control without checking per-type status.

---

### Lead 4 — ABIS (`GetInstanceTypesFromInstanceRequirements`) can return end-of-sale instance types (Lens X, primary)

**Claim:** `GetInstanceTypesFromInstanceRequirements` / `InstanceRequirements.InstanceGenerationSet`
defaults to **both** `current` and `previous` generation types (API_InstanceRequirements.md:156-163:
"Default: Current and previous generation instance types"). The U-9tb1/U-12tb1/U-18tb1/U-24tb1 instance
types are flagged by the guide as "no longer available for new instance launches" as of **June 20, 2025**
(doc-history.md:55; same notice repeated verbatim in ec2-nitro-instances.md:8-9, instance-types.md:8-9, and
mo.md:8-9) — yet they remain fully present and fully specified in every family page's full spec tables
(mo.md:67-70 size list, 129-132 platform summary, 546-557 vCPU/memory table, 1059-1070 network table,
1587-1598 EBS table, 2306-2317 security table) and remain **valid enum values** for `InstanceType` on both
`DescribeInstanceTypes` and `InstanceTypeInfo` (both API docs list `u-9tb1.112xlarge | u-12tb1.112xlarge |
u-18tb1.112xlarge | u-24tb1.112xlarge` plus their `.metal` variants in the `Valid Values` enum, with no
annotation that they are deprecated/end-of-sale). There is no `InstanceTypeInfo` field (`currentGeneration`,
`supportedInRegion`, or any other) that encodes "end of sale, blocked for new launches" — `currentGeneration`
is a generational-recency flag unrelated to sale status, and nothing in `InstanceRequirements` lets a caller
exclude "end of sale" types short of hand-maintaining an `ExcludedInstanceTypeSet` with the exact SKUs (a
list the API gives the caller no programmatic way to discover other than reading this guide's prose notice).

Therefore: a caller building an Auto Scaling Group / EC2 Fleet / Spot Fleet mixed-instances policy via ABIS,
specifying only `VCpuCount`/`MemoryMiB` and leaving `InstanceGenerationSet` at its default, could have
`GetInstanceTypesFromInstanceRequirements` return `u-9tb1.112xlarge` as a seemingly-viable candidate — a type
that the service's own launch path (RunInstances/CreateFleet/Auto-Scaling's internal launch call) will then
reject for new capacity, since it's end-of-sale. This is a **validator-divergence oracle**: the
selection-time API (ABIS) and the launch-time enforcement disagree about whether the type is "available."

**Mechanism (doc evidence):**
- API_InstanceRequirements.md:156-163 (`InstanceGenerationSet` default = both).
- doc-history.md:55 + ec2-nitro-instances.md:8-9 (end-of-sale notice, no API analog).
- API_InstanceTypeInfo.md:28-31 (`currentGeneration` — the only generation signal, doesn't mean "on sale").
- API_DescribeInstanceTypes.md / API_InstanceTypeInfo.md enum lists still containing all four U-*tb1 families
  with no deprecation marker.
- mo.md:67-70, 129-132 (U-9tb1/12tb1/18tb1/24tb1 still fully specified, including Hibernation=No,
  Dedicated-Host=Yes, Nitro v3 hypervisor — i.e. these are not stub/placeholder rows, they're complete specs).

**Confirm/Refute oracle:**
1. Call `GetInstanceTypesFromInstanceRequirements` with `VCpuCount={Min:448,Max:448}` (or whatever matches
   the U-9tb1 vCPU count from mo.md:547) and `MemoryMiB` bracketing 9216 GiB, `InstanceGenerationSet` left at
   default (unset). Confirm/refute: does `u-9tb1.112xlarge` appear in `instanceTypeSet`?
2. If it appears, attempt (in an authorized test env only — this step is for the vuln-hunter stage, not this
   doc-only pass) to actually launch via an ASG/Fleet referencing that requirements set, and observe whether
   the launch is blocked with an "end of sale"/`Unsupported`/capacity-style error, and what HTTP/error-code
   shape that takes (400 `InvalidParameterValue` vs opaque `InsufficientInstanceCapacity` vs silent partial
   fulfillment) — the divergence in *how* it fails (clear 400 "no longer offered" vs a capacity-shaped error
   that looks transient and invites retry-storms) is itself worth documenting, since a caller might retry
   indefinitely against a permanently-false-negative capacity error instead of recognizing a permanent
   policy block.
3. Separately confirm whether `DescribeInstanceTypeOfferings` (which reports per-region/AZ offering, a
   different API not fully reviewed here — doc-gap, confirm surface first) also still lists U-9tb1 as
   "offered," which would compound the inconsistency (three APIs: ABIS says selectable, Offerings says
   offered, RunInstances says blocked).

**Preconditions:** `ec2:DescribeInstanceTypes`, `ec2:GetInstanceTypesFromInstanceRequirements` read access
(both are standard read-only EC2 permissions); for step 2, launch permissions in an authorized test account
plus willingness to attempt (and expect to fail/clean up) a real launch of a 9–24 TB RAM instance type —
expensive, so should be deprioritized or simulated via `DryRun`/`CreateFleet` dry-run semantics if available.

**Severity if true:** The pure API-reporting inconsistency (ABIS returns a type RunInstances will reject) is
Informational/Low and AWS-owned — it's a UX/consistency gap, not a privilege or data-boundary breach. But it
inherits the severity of whatever automation breaks on it: an Auto Scaling group that silently never scales
because every attribute-matched candidate in a batch is end-of-sale and all launches fail, or a capacity-
planning/cost tool that budgets for U-9tb1 pricing having been told by ABIS it's a live option. Treat as
Low/Informational unless the vuln-hunter stage finds the launch-time error is misleading enough to cause an
operational-availability impact (e.g., ASG stuck permanently retrying a doomed launch instead of health-check
failing over) — that would escalate to a Medium availability finding, still AWS-owned (error-message/behavior
quality), not a security boundary bypass.

---

### Lead 5 — `AllowedInstanceTypeSet`/`ExcludedInstanceTypeSet` wildcard matching has no capability or version pin (Lens U variant / Lens X "no owner/allowlist pinning" shape)

**Claim:** The guide's attribute-based-selection input,
`InstanceRequirements.AllowedInstanceTypeSet`/`ExcludedInstanceTypeSet`, matches purely on the **instance
type name string** with shell-style wildcards (`c5*`, `m5a.*`, `r*`, `*3*` — API_InstanceRequirements.md:89-98,
144-154), not on any capability, generation-pin, or Nitro-version marker. A policy author who writes an
allowlist like `m5*` intending "the M5 family as it exists today" will, by the API's own stated example
("if you specify `c5*`, Amazon EC2 will allow the entire C5 instance family, **which includes all C5a and
C5n instance types**" — API_InstanceRequirements.md:91-92), silently also match any *future* instance type
AWS adds under that name prefix (e.g., were AWS to ship an `m5x` or `m53` variant later) without the policy
author re-reviewing it. This is the Lens-X "resolve to a type without owner/allowlist pinning a policy writer
would not expect" shape: the control is a **name-prefix pattern**, not a pinned set of SKUs or a capability
predicate, so the matched set can grow out from under a static security review as AWS ships new SKUs into
an already-matched family. Compounding this: `AllowedInstanceTypeSet` and `ExcludedInstanceTypeSet` are
mutually exclusive with each other (can't combine), so a defense-in-depth "allow m5* but exclude m5.metal"
posture requires the caller to get the wildcard precise on the first attempt — there is no "allow-then-carve-
out" combinator in a single request.

**Mechanism:** API_InstanceRequirements.md:89-98 (`AllowedInstanceTypeSet`, wildcard semantics, explicit C5/C5a/C5n
example demonstrating broader-than-expected matches), lines 144-154 (`ExcludedInstanceTypeSet`, same wildcard
semantics, mutual exclusivity with Allowed).

**Confirm/Refute oracle:** This is a *design* property stated directly in the docs (not something that needs
a live call to confirm) — the oracle is instead: enumerate, for a given wildcard pattern a policy might
plausibly write (`m5*`, `c5*`, `r*`), the **full current membership** returned by
`GetInstanceTypesFromInstanceRequirements` with that `AllowedInstanceTypeSet` and maximally loose other
constraints, and confirm it includes every variant/suffix family member (a/ad/d/dn/n/zn/metal) a policy
author would not have enumerated by hand — i.e., confirm the breadth-surprise is real and quantify it (how
many SKUs does `m5*` actually resolve to vs. what a naive reading of "M5" suggests).

**Preconditions:** None beyond standard ABIS read access; this is a documentation/design-review finding more
than a live-oracle finding.

**Severity if true:** Informational — this is a documented, intentional design (AWS states the behavior
plainly as a feature, not a bug), but it is exactly the kind of "policy writer would not expect" gap Lens X
asks to flag: if a customer's security review approved `AllowedInstanceTypes=["c5*"]` believing it pinned a
reviewed set of SKUs, and AWS later ships `c5z` or similar, the review's assumption silently erodes. Severity
is bounded by the fact that all members are still AWS-vetted, non-end-of-sale (modulo Lead 4) EC2 types —
there's no attacker-controlled resource being matched, just scope creep within AWS's own catalog. Flag as
Informational/Low, note for defense-in-depth guidance rather than as an exploitable bug.

---

### Lead 6 — ABIS response (`InstanceTypeInfoFromInstanceRequirements`) echoes no capability data, forcing a trust-then-verify gap (Lens X, secondary)

**Claim:** `InstanceTypeInfoFromInstanceRequirements`, the actual element type returned by
`GetInstanceTypesFromInstanceRequirements`, has a single field: `instanceType` (String) — no
`encryptionInTransitSupported`, no `nitroTpmSupport`, no `bareMetal`, nothing (API_
InstanceTypeInfoFromInstanceRequirements.md:13-16). So even for the handful of security-relevant predicates
ABIS *does* support as request filters (`RequireEncryptionInTransit`, `RequireHibernateSupport`, `BareMetal`
included/required/excluded), the response gives the caller no way to independently verify, from the ABIS
call alone, that the returned SKUs actually satisfy the requested predicate — the caller must trust ABIS's
internal filtering and/or make a second `DescribeInstanceTypes` call per returned type to confirm. Between
the two calls there is a non-atomic window; if instance-type capability data is ever updated between the ABIS
call and the follow-up Describe call (e.g. mid-migration of a capability flag, or cross-region/version-skew
of the control-plane's internal catalog service), the two calls could disagree, and most integrations
(Auto Scaling mixed-instances policies especially) do **not** make the follow-up Describe call at all — they
feed the ABIS output straight into a launch template, trusting ABIS's filtering end-to-end.

**Mechanism:** API_InstanceTypeInfoFromInstanceRequirements.md (single-field response);
API_InstanceRequirements.md:225-230 (`RequireEncryptionInTransit`), :231-236 (`RequireHibernateSupport`),
:101-109 (`BareMetal`) — all three are the only security-shaped predicates ABIS exposes, and none of their
truth is echoed back per-result.

**Confirm/Refute oracle:** Call `GetInstanceTypesFromInstanceRequirements` with
`RequireEncryptionInTransit=true` and a broad `VCpuCount`/`MemoryMiB` range spanning both Nitro v2 and v3+
types (so a filtering bug would be observable), then independently `DescribeInstanceTypes` every returned
`instanceType` and confirm 100% have `networkInfo.encryptionInTransitSupported=true`. Any returned type
failing that check is a confirmed enforcement bug in ABIS's filter (not just a reporting inconsistency) —
severity would then escalate per the next paragraph. Absent such a failure, this lead stands only as a
*design*-shaped gap (no response echo), Informational.

**Preconditions:** `ec2:DescribeInstanceTypes` + `ec2:GetInstanceTypesFromInstanceRequirements` read access.

**Severity if true:** If the filter itself is faithfully enforced (most likely, since this is a mature,
widely-used API), this is Informational — a response-shape nit, not a bug. **If** the confirm/refute oracle
ever surfaces a type that violates `RequireEncryptionInTransit=true`/`RequireHibernateSupport=true`/
`BareMetal=excluded`, that promotes to a genuine Lens-X enforcement-gap finding whose severity inherits the
downstream action: an Auto Scaling group launching a non-encrypted-in-transit instance into a fleet that a
compliance control assumed was 100% encrypted-in-transit is a data-confidentiality control failure (Medium-
High depending on data sensitivity), even though the root cause is still "AWS's own filter," not a customer
misconfiguration.

---

## Summary table

| # | Lens | Claim (one line) | Oracle | Severity-if-true |
|---|---|---|---|---|
| 1 | U | Per-type doc Security-specifications table cells == `DescribeInstanceTypes` fields for all ~700 rows | Diff doc table vs `describe-instance-types` output per instance type | Informational/Low (AWS-owned), inherits consuming control's severity |
| 2 | U | M6a/M7a/M8a/etc AMD SEV-SNP size-tier cliff point in doc == cliff point in API | `describe-instance-types --filters processor-info.supported-features=amd-sev-snp` across all sizes | Informational/Low, inherits confidential-computing control severity |
| 3 | U | Nitro-page "Nitro v3+ → Encryption in transit" blanket claim holds for every member type, no undocumented exception | Enumerate Nitro v3+ membership lists, check `networkInfo.encryptionInTransitSupported` per type | Informational/Low, inherits inter-instance-confidentiality control severity |
| 4 | X | ABIS (`GetInstanceTypesFromInstanceRequirements`) can still return end-of-sale U-9/12/18/24tb1 types; no API field encodes "end of sale" | Query ABIS matching U-9tb1 spec with default `InstanceGenerationSet`; check if it's returned; then test launch-time rejection shape | Informational/Low reporting gap; escalate to Medium if launch-time error shape causes availability failure (stuck ASG) |
| 5 | U/X | `AllowedInstanceTypeSet`/`ExcludedInstanceTypeSet` wildcard matching has no capability/version pin — scope can silently grow as AWS ships new SKUs under a matched prefix | Enumerate full match set of a representative wildcard today; documented design property, no live oracle needed to confirm existence | Informational — defense-in-depth note, not exploitable against AWS |
| 6 | X | ABIS response object echoes zero capability fields; callers trust filtering end-to-end with no response-side verification | Call ABIS with `RequireEncryptionInTransit=true` (or Hibernate/BareMetal) across a broad spec range; cross-check every returned type via `DescribeInstanceTypes` | Informational if filter holds; Medium-High if a returned type ever violates the requested predicate (real enforcement gap, not just reporting) |

## Explicitly out of scope / doc-gaps not pursued further
- `DescribeInstanceTypeOfferings` (region/AZ offering reporting) was not reviewed in depth — doc-gap, confirm
  surface first before claiming anything about offering-vs-sale-status consistency (mentioned only
  speculatively in Lead 4 step 3).
- `GetSpotPlacementScores`, `RunInstances`, `CreateFleet`, Auto Scaling's instance-type validation path were
  not reviewed — Lead 4's "launch-time rejection" step is a hypothesis about behavior at those APIs, not a
  reviewed claim; flag as doc-gap for the live-testing stage.
- GPU/accelerator-level confidential-computing claims (e.g. NVIDIA H100 confidential computing / GPU TEE)
  are not represented anywhere in the guide's Security-specifications table (only EBS/instance-store/transit/
  SEV-SNP/TPM/Enclaves columns exist) — doc-gap, the guide makes no claim here one way or the other, so there
  is nothing to falsify yet.
