# Amazon EC2 Instance Types — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/ec2/latest/instancetypes/` (`instance-types.md`, `ec2-nitro-instances.md`, `ec2-instance-type-specifications.md`, `instance-type-names.md`, `ec2-instance-regions.md`, `ec2-instance-quotas.md`, `doc-history.md`, and the per-family spec pages `gp.md`/`co.md`/`mo.md`/`so.md`/`ac.md`/`hpc.md`/`pg.md`); EC2 API Reference under `/work/aws-docs/docs/AWSEC2/latest/APIReference/`; Service Authorization Reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`; cross-checked online at docs.aws.amazon.com (append `.md` to any `.html` for markdown). Online target page: https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html

**Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.** This plan is for a hunter authorized against a test account; it never licenses touching AWS's own service plane.

---

## 0. How to use this document

- Each lead is written as: **Claim** (a thing the docs imply should hold, stated as if breakable) → **Mechanism** (the exact page/field/sentence that makes it plausible) → **Confirm/Refute oracle** (the single observation that settles it) → **Preconditions / Cost** → **Severity-if-true** → **Stop condition**. Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **The guide itself is read-only documentation** (hardware spec tables). It exposes **no customer API of its own**. The attack surface it *describes* is threefold and that is what this plan targets:
  1. the EC2 **control-plane APIs that report instance-type capabilities** (`DescribeInstanceTypes`, `GetInstanceTypesFromInstanceRequirements`) — a published capability cell that disagrees with the API, or a compliance/attestation control built on a false capability claim (Lens U/X);
  2. the **IAM condition keys** customers use to gate *which* instance types/families/hardware a principal may launch (`ec2:InstanceType`, `ec2:Attribute`, tenancy/metadata keys) — scoping-semantics and sample-policy bypasses (Lens S/R);
  3. the **Nitro trust model** the guide asserts — measured-boot/attestation (NitroTPM, Nitro Enclaves, AMD SEV-SNP), encryption-in-transit, and shared-host tenant isolation (Lens W/V/Y/L).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro controller, the hypervisor, a fleet-owned role), **stop, preserve evidence, and flag for AWS-Security disclosure.** The vast majority of "break tenant isolation on Nitro" ideas land on the shared-responsibility line and are **out of scope** — see Section 7.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. Make `DescribeInstanceTypes` (or `GetInstanceTypesFromInstanceRequirements`) report a **security capability** (`EncryptionInTransitSupported`, NitroTPM, Nitro Enclaves, AMD SEV-SNP, supported boot mode) that **contradicts the published Security-specifications table** in the family pages — a customer attestation/compliance control built on the wrong value.
2. Launch an instance of a **type/family/size the customer's IAM policy intended to forbid** (cost, hardware-isolation, or confidential-compute gating) by exploiting a condition-key scoping gap, a case/format mismatch, a nonexistent condition key, or a RunInstances multi-resource gap.
3. Obtain KMS plaintext under a **NitroTPM / Nitro Enclave attestation gate that fails open** (absent/wildcard/all-zero/under-binding PCRs) or a `PutKeyPolicy` that accepts a bogus measurement — for an enclave the attacker could not legitimately produce.
4. Degrade a **co-resident tenant's** network/disk/CPU on a shared host beyond the documented "equal share" guarantee (cross-tenant noisy-neighbor DoS), or abuse the T-instance CPU-credit / Flex-baseline accounting.
5. Have `GetInstanceTypesFromInstanceRequirements` (attribute-based selection) resolve to an **end-of-sale / previous-generation / region-unsupported** type that a control-plane check should have excluded.

---

## 2. Components, Assets, and Design

**What this guide describes.** A catalog that, for every EC2 instance *family* (e.g. `m8i`) and *size* (`.large` … `.metal`), publishes: compute/memory/network/EBS/instance-store specs **and a per-size "Security specifications" row**. There is no network endpoint or console route unique to this guide; it is reference content for the EC2 control plane.

**The security-capability model (the asset that matters).** Each family page `## Security specifications` table (e.g. `gp.md` line 1688) has these columns, each a boolean per instance *size*:

| Column | Meaning | Maps to control-plane field (to verify) |
|---|---|---|
| EBS encryption | EBS volumes can be encrypted | `DescribeInstanceTypes.EbsInfo.EncryptionSupport` |
| Instance store encryption | local NVMe encrypted at rest | `InstanceStorageInfo.EncryptionSupport` |
| **Encryption in transit** | inter-instance traffic encrypted (Nitro v3+) | `NetworkInfo.EncryptionInTransitSupported` |
| **AMD SEV-SNP** | confidential-compute memory encryption | *(boot-mode / processor info — confirm field)* |
| **NitroTPM** | virtual TPM 2.0 for measured boot | `NitroTpmInfo` / `NitroTpmSupport` |
| **Nitro Enclaves** | isolated attestable compute | *(enclave support flag — confirm field)* |

**Observed capability granularity (direct from `gp.md`) — already a lead source:**
- Capability is **size-dependent, not family-wide.** `m5.large` → Nitro Enclaves = **✗ No**, but `m5.xlarge`+ → ✓ Yes. `m6a.large–8xlarge` → AMD SEV-SNP = ✓ Yes, but `m6a.12xlarge`+ → **✗ No**.
- **`.metal` sizes lose NitroTPM and Nitro Enclaves** (e.g. `m5.metal`, `m6i.metal` → both ✗) while retaining EBS/instance-store/transit encryption.
- Encryption-in-transit tracks **Nitro version** (v3+). Nitro v2 families (`m5`, `m6g`) → ✗ No; Nitro v3+ (`m5dn`, `m6a`, `m8i`) → ✓ Yes.

**Hypervisor / platform model (`## Instance family summary`, `gp.md` line 79):** every current-gen family is on the **AWS Nitro System** (`Nitro v2`–`v6`) **except `T2`, which is still on `Xen`** — a distinct, older isolation architecture. Columns: Hypervisor, Processor type (Intel/AMD/Graviton/Apple), Metal available, Dedicated Hosts support, Spot support, Hibernation support, OS.

**The Nitro System (`ec2-nitro-instances.md`).** Components: **Nitro card** (local NVMe, networking, management, monitoring, security), **Nitro security chip** (integrated into motherboard), **Nitro hypervisor** (lightweight, memory/CPU allocation). Bare-metal instances "provide … full access to host hardware" and "eliminate virtualization overhead." Encryption-in-transit, ENA Express, RDMA, Traffic Mirroring vary by Nitro version. These are **AWS-owned service-plane components** — their internal compromise is out of scope / hard-stop; only the *documented guarantees* they expose to customers are in-scope targets.

**Multi-tenancy / resource-sharing statement (target page `instance-types.md`):** "Amazon EC2 dedicates some resources of the host computer, such as CPU, memory, and instance storage, to a particular instance. Amazon EC2 **shares** other resources of the host computer, such as the network and the disk subsystem, among instances. If each instance … tries to use as much of one of these shared resources as possible, each receives an **equal share**." → shared-fleet contention surface (Lens L). **Burstable (`T`)** instances meter CPU via **CPU credits**; **Flex** (`C7i-flex`/`C8i-flex`/`M7i-flex`/`M8i-flex`/`R8i-flex`) deliver a **40% baseline** burstable to 100% for 95% of a 24h window → credit/baseline accounting surface.

**Identifiers / namespace.** Instance-type names are structured and fully enumerable: `<series><generation><options>.<size>` (`instance-type-names.md`), e.g. `c7gn.xlarge`, `.metal`. No secret entropy — these are public catalog identifiers, not tenant-scoped resources (relevant to Lens A null hypothesis).

```
 Customer / IAM principal
        │  RunInstances(InstanceType=…, LaunchTemplate=…, InstanceRequirements=…)
        ▼
 EC2 control plane ──────────────► DescribeInstanceTypes / GetInstanceTypesFromInstanceRequirements
   │  (authz: IAM condition keys: ec2:InstanceType, ec2:Tenancy,          (reports capability cells:
   │   ec2:Attribute, ec2:MetadataHttpTokens, …)                           NitroTpm / Enclaves / SEV-SNP /
   ▼                                                                       EncryptionInTransitSupported)
 Provisioning → places instance on a host in a   ┌─────────────────────────────────────────┐
 shared Nitro fleet (or Dedicated Host/tenancy)  │  AWS service plane (OUT OF SCOPE / HARD   │
   │                                             │  STOP): Nitro card, Nitro security chip,  │
   ▼                                             │  Nitro hypervisor, host firmware,         │
 Guest instance ── shared: network, disk ───────►│  attestation root of trust                │
   (equal-share)   dedicated: vCPU, mem, store   └─────────────────────────────────────────┘
        │
        └─ KMS Decrypt gated by kms:RecipientAttestation (PCR0-15 / ImageSha384 / NitroTPMPCR0)  ← Lens W
```

---

## 3. API / Interface Inventory

The guide has no API; these are the EC2 (and KMS) APIs it *drives*. Verify each in the API Reference mirror.

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes / lens |
|---|---|---|---|---|---|---|---|---|
| `DescribeInstanceTypes` | SigV4 | Existing | Non-mut | External | Reports per-type specs **incl. security capability fields** | Yes | any IAM caller w/ `ec2:DescribeInstanceTypes` (often `Resource:*`, no ownership) | **Lens U/X** — the capability-cell oracle; diff vs guide tables |
| `GetInstanceTypesFromInstanceRequirements` | SigV4 | Existing | Non-mut | External | Attribute-based instance selection (ABIS): given min/max vCPU/mem/accelerators → list of matching types | Yes | any IAM caller | **Lens X/U** — validator divergence vs DescribeInstanceTypes; end-of-sale/region resolution |
| `DescribeInstanceTypeOfferings` | SigV4 | Existing | Non-mut | External | Which types are offered per Region/AZ/Local-Zone | Yes | any IAM caller | region-availability oracle (Lens A/U) |
| `RunInstances` | SigV4 | Existing | **Mutating** | External | Launch; `InstanceType`/`LaunchTemplate`/`InstanceRequirements` input | Yes | IAM, **gated by condition keys** | **Lens S/R** — the thing policies try to constrain; multi-resource action |
| `ModifyInstanceAttribute` | SigV4 | Existing | **Mutating** | External | Change `instanceType`, `userData`, etc. of a stopped instance | Yes | IAM | **Lens S + Lens B/E variant** — change type post-launch to escape a launch-time type gate; `userData` late-binding |
| `CreateLaunchTemplate` / `…Version` | SigV4 | Existing | Mutating | External | Encapsulates instance type + attributes | Yes | IAM | `ec2:IsLaunchTemplateResource` indirection (Lens S) |
| `kms:Decrypt` / `GenerateDataKey` (+ `Recipient`) | SigV4 | Existing | Non-mut | External | Attestation-gated decrypt for enclaves | Yes | IAM + key policy | **Lens W** — attestation fail-open |
| `kms:PutKeyPolicy` | SigV4 | Existing | Mutating | External | Author `kms:RecipientAttestation` conditions | Yes | key admins | **Lens W** — authoring-time validation of PCR key/value |

Doc-flagged leads to keep verbatim:
- **End-of-sale (verbatim):** "The **U-9tb1**, **U-12tb1**, **U-18tb1**, and **U-24tb1** instance types are **no longer available for new instance launches**." → Lens X (can ABIS / RunInstances still launch them? is the block control-plane-wide or console-only?).
- **`[NEW]` surface (from `doc-history.md`):** Nitro **v6** card (M8i/C8i/R8i/M8gn/…, 2026), **Graviton5** (M9g/R9g/C9g/C9gd, 2026), **T8i** (Sep 2026), **P6-B300 / P6e-GB200** (Blackwell GPUs), new `.metal-48xl`/`.metal-96xl` sizes. New Nitro-version + new metal sizes are the least-reviewed capability rows → prioritize their Security-spec cells (Section 5.1).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal (customer) | EC2 control plane capability data | `DescribeInstanceTypes` | A capability cell returned by the API **disagrees with the published Security-specifications table** for the same type/size → a compliance control reads the wrong value. In-scope (AWS-owned doc/API). |
| IAM principal (restricted) | `RunInstances` of a forbidden type/family/size | condition-key authz | An instance of a type the policy's `ec2:InstanceType`/attribute Deny intended to forbid **reaches `running`** (or `SimulateCustomPolicy` returns `allowed`) → policy scoping gap. |
| Caller's enclave (attacker) | KMS plaintext of a key gated on attestation | `kms:RecipientAttestation` condition | `Decrypt` **succeeds** for a request with **absent/wildcard/all-zero/under-binding** attestation, or `PutKeyPolicy` **accepts** a bogus PCR → gate fails open. |
| Tenant A guest (shared host) | Tenant B guest (co-resident) | shared network/disk subsystem | Tenant A degrades Tenant B's throughput **below the documented equal share**, or observes B's traffic/data. **Cross-tenant = High; but reaching the Nitro plane to do it = HARD STOP / out of scope.** |
| Guest instance | AWS Nitro service plane (card/chip/hypervisor) | — | **Any packet, credential, ARN, or control response from the Nitro controller/hypervisor = hard-stop breach.** Not a hunting target; preserve evidence, disclose. |
| Attribute-based requirements | an excluded instance type | `GetInstanceTypesFromInstanceRequirements` | ABIS returns an **end-of-sale / previous-gen / region-unsupported** type that `DescribeInstanceTypeOfferings` would exclude → validator divergence. |

---

## 5. Recommended Areas of Focus

Ordered by priority: NEW capability surface first, then the authz-gating surface, then attestation, then shared-host contention.

### 5.1 Capability-cell integrity: published Security-specs table vs `DescribeInstanceTypes` (Lens U, Lens X) — **PRIORITY 1**

**Background.** Every family page publishes a per-size `Security specifications` table with boolean cells for EBS encryption, instance-store encryption, **Encryption in transit, AMD SEV-SNP, NitroTPM, Nitro Enclaves**. `DescribeInstanceTypes` returns machine-readable equivalents. Customers and compliance tools (Config rules, attestation gates, "is this type FIPS/confidential-capable" checks) consume one or the other and assume they agree.

**Security Concern.** A single mismatched cell lets a customer build a control on a false premise: e.g. a Config rule that "allows only Encryption-in-transit-capable types" trusting the doc table while the API reports otherwise (or vice-versa), or an attestation policy that assumes `m6a` supports SEV-SNP when `m6a.12xlarge+` does **not** (confirmed size-granularity gap in `gp.md`). AWS owns both artifacts, so a divergence is AWS's defect (Lens U → Informational/Low, but reportable; **High if a customer-reachable enforcement path keys on the wrong value**).

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** For some current type/size, `DescribeInstanceTypes.NetworkInfo.EncryptionInTransitSupported` ≠ the family page's "Encryption in transit" cell. → **Oracle:** diff the full column across all families for every size vs the API for the same Region; any single disagreement confirms. → Sev: Low (Info) / High if an in-scope control enforces on it.
- **Claim:** `AMD SEV-SNP` / `NitroTPM` / `Nitro Enclaves` doc cells disagree with the control-plane field (incl. the **size-dependent** cutoffs — `m5.large` no-Enclaves, `m6a.12xlarge+` no-SEV-SNP, all `.metal` no-NitroTPM/Enclaves). → **Oracle:** per-size diff; a type whose doc says ✓ but API says ✗ (or no field exists) is the finding. → Sev: Low/Info; **Medium–High if used in a KMS attestation or SEV-SNP launch gate** (chains to 5.3).
- **Claim (Lens X validator divergence):** `GetInstanceTypesFromInstanceRequirements` returns a type that `DescribeInstanceTypes`/`DescribeInstanceTypeOfferings` would mark unavailable, or classifies a capability differently. → **Oracle:** request requirements that only an end-of-sale/previous-gen type satisfies; see whether ABIS surfaces it. → Sev: Low–Medium (enumeration / policy-bypass enabler).
- **Claim (Lens X legacy — strongest X lead):** the four **end-of-sale U-* types** are still returned by `GetInstanceTypesFromInstanceRequirements`. **Mechanism:** ABIS defaults `InstanceGenerationSet` to **both current and previous generation**, and **no API field encodes "end of sale"** (confirmed: `u-9tb1`/`u-12tb1`/`u-18tb1`/`u-24tb1` are still fully specified, still-valid enum values in `API_InstanceTypeInfo.md` / the requirements model), while `doc-history.md:55` + the guide banner say they are blocked for new launches since 2025-06-20. → **Oracle:** query ABIS with a U-9tb1-shaped requirement under the default generation filter → it is returned; then `RunInstances(InstanceType=u-9tb1.*)` and record the rejection *shape* (hard 400 vs capacity-style error) to tell a control-plane block from mere capacity. → Sev: Low (product/doc-gap) unless the "blocked" state is only cosmetic.

**Confirmed API substrate (from the Lens U/X capability-audit subagent — `instancetypes-scratch-lensUX.md`):** `DescribeInstanceTypes` → `InstanceTypeInfo` exposes a 1:1 machine-readable equivalent for **every** security cell: `networkInfo.encryptionInTransitSupported`, `nitroTpmSupport`/`nitroTpmInfo.SupportedVersions`, `nitroEnclavesSupport`, `processorInfo.SupportedFeatures` (`amd-sev-snp`, `nested-virtualization`), `bareMetal`, `hypervisor` (`nitro`|`xen`), `ebsInfo.encryptionSupport`, `instanceStorageInfo.encryptionSupport`, `SupportedBootModes` (`legacy-bios`|`uefi`), `dedicatedHostsSupported`, `phcSupport`, `rebootMigrationSupport` — all also usable as `Filter.N` keys. The ~700-row Security-specs dataset across the seven family pages is therefore mechanically diffable against the API per Region. **Critically, the ABIS response object `InstanceTypeInfoFromInstanceRequirements` has exactly ONE field, `instanceType` — no capability echo** — so a caller using `RequireEncryptionInTransit`/`RequireHibernateSupport`/`BareMetal` requirements must trust ABIS's internal filtering blind; cross-checking each returned type via `DescribeInstanceTypes` is the oracle that would turn any filter miss into a real enforcement-gap finding (not just an Info diff). The `AllowedInstanceTypeSet`/`ExcludedInstanceTypeSet` wildcard matching (`c5*`) has **no capability/version pin** — AWS's own example shows `c5*` silently pulling in `C5a`/`C5n`, so a requirements-based allowlist *grows* as AWS ships new SKUs under a matched prefix (scope-creep lead; ties to 5.2).

### 5.2 Instance-type IAM gating: condition-key scoping semantics & AWS sample policies (Lens S, Lens R) — **PRIORITY 2**

**Background.** Customers restrict launches to approved families/sizes (cost control, hardware-isolation posture, "no bare-metal," "confidential-compute only") with IAM conditions on `RunInstances`, chiefly `ec2:InstanceType`. `RunInstances` is a **multi-resource action** (instance, volume, network-interface, …); a condition attached to one resource type does not gate the others.

**Condition-key inventory (from the Lens S/R subagent — `instancetypes-scratch-lensSR.md`, verified in `list_ec2.md`).** The hardware/type-gating keys `ec2:InstanceType`, `ec2:Tenancy`, `ec2:RootDeviceType`, `ec2:PlacementGroup`, **`ec2:CpuOptionsAmdSevSnp`** (confidential-compute *is* gatable by a real key), `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting` are bound **only to the `instance*` resource row** of `RunInstances` (`list_ec2.md` ~9585-9609) — **not** to `image*`, `launch-template`, `subnet*`, `network-interface*`, `security-group*`, or `key-pair`. There is **no** condition key for Nitro-version, bare-metal, accelerator, or enclave-support.

**Security Concern — the five confirmed failure shapes:**

- **(1) Nonexistent-key, Medium.** Beyond `ec2:InterfaceType`, there is **no** `ec2:NitroVersion`/`ec2:BareMetal`/`ec2:Accelerator`/`ec2:EnclaveOptions`-style key. A Deny an operator writes against any such *expected* key is silently inert. → **Oracle:** `SimulateCustomPolicy` with a Deny on a hallucinated key → the launch is still `allowed`.
- **(2) Case-sensitivity, High — the control mechanism is void.** `API_ModifyInstanceAttribute.md:23` shows the wire-level `Attribute` enum is **camelCase** (`instanceType`), while the same doc's parameter heading (`:74`) and every SDK/CLI surface use **PascalCase** (`InstanceType`). A Deny written `StringEquals {"ec2:Attribute":"InstanceType"}` **never matches** the camelCase request value. → **Oracle:** `SimulateCustomPolicy`/scoped `ModifyInstanceAttribute` with that Deny → not denied. (Doc-gap: whether the API normalizes case before IAM evaluation is unstated — confirm live.)
- **(3) Multi-resource RunInstances gap, High.** A policy limiting `ec2:InstanceType` to `t3.*` gates only the `instance` ARN; the launch's other required resources are unconditioned, so a non-`t3` launch can still succeed. → **Oracle:** scoped-role `RunInstances` with a disallowed type under such a policy reaches `running` / `SimulateCustomPolicy` = `allowed`. → Sev: **High where the condition is the sole cost/isolation control.**
- **(4) Action indirection, High.** `CreateFleet` doc text (`list_ec2.md:5114`) states resource-level perms **exclude** launch-template-specified resources; `RequestSpotInstances`/`RequestSpotFleet` have **no `instance*` row or `ec2:InstanceType` key at all** (~9465-9480); `autoscaling:InstanceType(s)` is a **separate namespace** (`list_autoscaling.md:850-851`) blind to launch-template-native types, and ASG launches run under a **service-linked role**, bypassing the caller's `RunInstances` type restriction entirely. → **Oracle:** launch a forbidden type via Spot/Fleet/ASG that the direct `RunInstances` Deny blocks.
- **(5) Self-widen via adjacent action, Medium–High.** `ec2:ModifyInstanceAttribute` exposes the identical `ec2:InstanceType` key, but no AWS sample gates it → **stop → resize to forbidden type → start** escapes the launch-time cap. → **Oracle:** launch allowed `t3`, stop, `ModifyInstanceAttribute(instanceType=x2idn)`, start → runs.

**Lens R — AWS-authored sample-policy weakness (Tier 2, reportable).** `ExamplePolicies_EC2.md`'s "Instance types" recipe (`:304-386`) and "Launch templates" recipe (`:862-990`) are presented as independent, composable `RunInstances` statements in the same guide. Composed, the launch-template Allow (keyed only on `ec2:LaunchTemplate`, `Resource:"*"`) **silently overrides** the instance-type cap via IAM's OR-across-Allow-statements evaluation. → **Oracle:** under a role holding exactly both printed statements, launch a forbidden type through a launch template → `allowed`. → Sev: High; reportable precisely because the artifact is AWS-authored.

### 5.3 Attestation-gated authorization: NitroTPM / Nitro Enclaves / SEV-SNP (Lens W) — **PRIORITY 3**

**Background.** The Security-specs tables advertise NitroTPM, Nitro Enclaves, and AMD SEV-SNP per size. Nitro Enclaves + NitroTPM provide measured boot and attestation that KMS key policies consume via `kms:RecipientAttestation:PCR0..15` / `:ImageSha384` / `:NitroTPMPCR0`. The attestation gate is the sole control over enclave-sealed secrets.

**Security Concern.** The gate must fail **closed**. A request lacking attestation, or carrying a wildcard/all-zero/under-binding measurement, must be denied; `PutKeyPolicy` should reject bogus measurements at authoring time.

**High-level Test Scenarios:**
- **Claim:** `Decrypt` on a key with a `kms:RecipientAttestation:PCR0` condition **succeeds when the request carries no `Recipient`/attestation** (fail-open on absence). → **Oracle:** `AccessDenied` = fail-closed (good); plaintext returned = finding. → Sev: **Critical** (enclave-sealed secret).
- **Claim:** a **wildcard** PCR (`StringLike …PCR0:"abc*"`), an **all-zero / debug-enclave** measurement, or **only PCR0 pinned** (under-binding kernel/app PCRs) authorizes an enclave the attacker controls. → **Oracle:** a non-production/attacker enclave whose measurement satisfies the loose condition gets plaintext. → Sev: High–Critical.
- **Claim:** `PutKeyPolicy` **accepts a nonexistent PCR index (`PCR99`) or wrong-length measurement** → operator believes a gate exists that cannot match. → **Oracle:** policy write returns success instead of `ValidationException`. → Sev: High (silent non-enforcement).
- **Claim (ties to 5.1):** a size that the doc marks "Nitro Enclaves ✓" cannot actually attest (API/field disagreement) → an attestation control deployed on it is advisory only. → Sev: Medium–High.

**Concrete leads (from the Lens W/V/L/Y subagent — `instancetypes-scratch-lensWVL.md`; cross-refs the sibling `nitrotpm-attestation`, `isolate-data-operators`, `sev-snp` plans, do not duplicate those):**

- **W-1 (confirmed-closed, record only):** a `Decrypt` with no `Recipient` against a key whose *only* grant carries `kms:RecipientAttestation:*` is denied — doc states fail-closed for both Enclaves (`conditions-nitro-enclave.md`) and NitroTPM (`conditions-nitro-tpm.md`). **Not a lead to spend time on**; the real fail-open is architectural (W-2).
- **W-2 — fail-open by policy *composition* (⭐ strongest W lead), High.** The attestation condition only constrains the statement it sits on. If the key policy keeps the **AWS-auto-created default "account-root full access" Allow** (or any second unconditioned `Allow kms:Decrypt` for the same principal), that statement independently satisfies the request and the gate is bypassed with no error. `conditions-attestation.md` itself notes the default policy "allows all actions like Decrypt" and only *optionally* suggests `NotAction:kms:Decrypt`; none of the four KMS/enclave sample pages tells the author to remove/deny the default grant. → **Oracle:** 2-statement key policy (sample Allow+condition *plus* default root Allow), call `Decrypt` without `Recipient` as root → plaintext = confirmed. → **Route the "AWS sample never warns" slice to `aws-security`** as a doc-completeness defect (same shape as sibling AF-3).
- **W-3 — `PutKeyPolicy` value-acceptance, Medium–High.** Does authoring-time validation reject (a) a nonexistent PCR id (`PCR99`/`NitroTPMPCR255`), (b) non-hex / wrong-length values, (c) a `StringLike` wildcard operator on `kms:RecipientAttestation:PCR0`? Policy JSON is opaque to the authoring API and `condition_operators.md` permits `StringLike` on any String key, so the likely answer is "accepted, 200 OK." The **dangerous** case is a typo'd *Deny* condition that silently never fires (fail-open with no signal); the second is a mis-sized wildcard silently broadening an image-hash pin. → **Oracle:** live/simulated `PutKeyPolicy` with each bad key/op → accepted. Purely an AWS-API-behavior question — no enclave/instance needed.
- **W-4 — under-binding, Medium (doc-completeness).** `set-up-attestation.md` recommends **PCR3+PCR8** ("best flexibility") — role ARN + signing-cert, which **never bind PCR0 (code hash)**. A policy built exactly to AWS's recommendation authorizes *any* image signed by the right cert under the right role, including an attacker-modified app (different PCR2). → **Oracle:** two images, same cert+role, different code — both `Decrypt`. No "Warning: PCR3+PCR8 do not verify which application runs" callout exists.
- **W-5 — all-zero debug PCRs, Medium.** `--debug-mode`/`--attach-console` enclaves emit all-zero PCRs; the docs say these "can't be used" but never state KMS special-case-rejects them. If an author ever pins an all-zero reference value (copy-paste, or a legitimately-zero optional PCR — cf. sibling AF-3 PCR12-all-zeros), a debug enclave satisfies it. → **Oracle:** policy with an all-zero ref value + debug enclave.
- **W-6 — capability ground truth (Informational, feeds every W precondition).** `.metal*` types are **excluded from Nitro Enclaves** (enclaves need the Nitro Hypervisor's memory/vCPU partitioning, which bare metal bypasses) and the NitroTPM allow-list (`enable-nitrotpm-prerequisites.md`) is **narrower than "built on Nitro"** (excludes e.g. G4ad, DL1, Trn1/Trn1n). A customer threat-modeling from the Nitro-instances page alone **over-assumes attestation coverage**. → **Oracle:** `describe-instance-types --filters Name=bare-metal,Values=true --query 'InstanceTypes[].NitroEnclavesSupport'` should be all `unsupported`. This is the scoping check that connects 5.3 back to 5.1's capability-cell diff.

### 5.4 Shared-host cross-tenant contention & CPU-credit accounting (Lens L) — **PRIORITY 4**

**Background.** The target page states shared resources (network, disk subsystem) are split so each instance "receives an **equal share**." `T` instances meter CPU with credits; Flex instances give a 40% baseline. These are the only multi-tenant-isolation guarantees the guide makes about *performance*.

**Security Concern.** Cross-tenant noisy-neighbor: one tenant degrading a co-resident tenant below the equal-share guarantee = cross-tenant DoS on shared fleet (High). Single-tenant self-DoS and merely "slow neighbor within equal share" are out of scope.

**High-level Test Scenarios:**
- **Claim:** a tenant can drive a shared resource so a co-resident tenant drops **below** its guaranteed equal share (not just contend within it). → **Oracle:** measured sustained degradation of a second-account instance known co-resident, beyond the documented floor. → Sev: High (cross-tenant). *Note: establishing co-residency and attributing degradation is expensive and may be unobservable from a test account; likely doc-gap/needs-live-confirm.*
- **Claim:** T-instance **CPU-credit** or Flex-baseline accounting can be manipulated for sustained above-baseline CPU without the metered cost (billing/perf integrity). → **Oracle:** sustained >baseline utilization with credit balance not decrementing as documented. → Sev: Low–Medium (single-tenant billing; raises if it starves neighbors).

**Concrete framing (from the Lens W/V/L/Y subagent — `instancetypes-scratch-lensWVL.md`):**

- **L-1 — "equal share" has no denominator, SLA, or fairness-violation metric (⭐ the in-scope deliverable here), Medium (visibility gap).** The one sentence is the *entire* documented guarantee against noisy-neighbor degradation of network/disk. It names no co-tenancy density cap, no time window, no enforcement mechanism, and **no customer-facing metric that distinguishes "my share is small because many tenants are busy" from "I am being starved below my equal share."** EC2 exposes only *your own* instance-level metrics (`NetworkIn/Out`, EBS `VolumeQueueLength`), never a host-level contention/fairness indicator. **Document this gap — it is fully confirmable from docs alone and is the safe deliverable.**
- **L-1 live-demonstration half = HARD STOP.** Actually *showing* one tenant degrade a co-resident tenant below equal share requires confirmed cross-account co-residency and reaches into the Nitro hypervisor/network-card QoS enforcement on AWS's own fleet → **High if ever confirmed, but flag for disclosure, do not pursue as a standalone test.**
- **L-2 — CPU credits = null/out-of-scope.** Credits are strictly per-instance; exhausting them is single-tenant self-DoS. Unlimited-mode's 24h rolling-average billing window is gameable only for *the account's own bill* (legitimate optimization, not an attack). Recorded as explicit null.
- **L-3 — Flex "95% of the time / gradual reduction" = null as cross-tenant.** The docs attribute the burst-ceiling reduction to the instance's **own** sustained utilization, not co-tenant demand — a self-throttling algorithm like CPU credits, not a Lens-L contention mechanism. Doc is silent on whether the 5%/threshold varies with host load (unremarkable, since framed as self-caused).

### 5.5 Region / availability resolution integrity (Lens A/U, minor)

**Background.** `ec2-instance-regions.md`: "Each Region supports a subset … An instance type supported in a Region might not be supported in all AZs." `DescribeInstanceTypeOfferings` reports this.

**Security Concern / Scenario.** Low-value: the per-type **existence oracle** (not-found vs unsupported-in-region vs unauthorized) across `DescribeInstanceTypes` / offerings / ABIS could differ, giving an enumeration signal — but instance-type names are already a public, fully-enumerable catalog, so there is **no secret to enumerate** (see Section 8 null hypothesis for Lens A). Keep only as a validator-divergence corroborator for 5.1.

### 5.6 Encryption-in-transit compliance integrity & bare-metal tenancy framing (Lens Y, Lens U/V) — **doc-completeness, route to `aws-security`**

**Y-1 — "automatic" in-transit encryption silently exits its envelope with zero per-flow verifiability (⭐ crown Lens-Y lead), Medium (compliance-integrity).** The target page's Nitro v3+ "Encryption in transit" bullet and `data-protection.md`'s "automatically encrypt… no impact on network performance" framing invite a customer to file a compliance claim ("inter-instance traffic is encrypted"). But the guarantee **silently stops applying** when any of three conditions is violated: (a) both ends must be on the supported-type list (`networkInfo.encryptionInTransitSupported=true`) — a mixed-generation pair silently drops to baseline; (b) same Region; (c) same/peered VPC **with no intervening virtual network device** — introducing an ALB/NLB, Transit Gateway (and likely NAT Gateway / PrivateLink) between two otherwise-qualifying instances disables the layer. **There is no per-flow signal** — no Flow Logs field, no CloudWatch metric, no IAM condition key, no attestation — to tell a customer whether a given flow was actually encrypted. Contrast Lens W, which fails closed and loudly (`AccessDeniedException`); this fails **open and silently**. → **Oracle (doc-only, falsifiable):** search `data-protection.md`/`ena-express.md`/EC2 API ref for any per-flow encryption observability signal or any mechanism to *require* the property → current read: **absent**; `ec2:InstanceType` can restrict launches to supported types but nothing constrains *topology*. → **Impact:** High if a customer filed an audit attestation on this property without an ongoing verification mechanism, because nothing re-checks it as the topology evolves (someone later adds an LB and silently regresses it). Recommend AWS add a per-flow signal or a louder topology-dependency warning on the headline page.
- **Y-2 (Low/Info):** the data-protection page repeats "additional layer at the physical layer" in three subsections; a fast reader of the one-line Nitro-v3 bullet could conflate the **unconditional physical-layer** encryption with the **conditional instance-type-gated** layer — a page-boundary doc gap reinforcing Y-1.

**V/D-2 — "bare metal" conflated with tenancy exclusivity, Low/Informational.** `ec2-nitro-instances.md`'s "full access to host hardware" reads security-adjacent but is a *performance* claim. `API_InstanceTypeInfo.md` exposes `bareMetal` and `dedicatedHostsSupported` as **independent, orthogonal** fields — a bare-metal instance is *not* inherently single-tenant; only Dedicated Hosts / `ec2:Tenancy` give the billable, API-visible exclusivity guarantee. A compliance narrative built on "I chose bare metal so no one else is on this hardware" is wrong unless Dedicated Host/Tenancy was *also* selected, and the page never states that boundary. → **Oracle:** doc search for any sentence equating bare metal with tenancy exclusivity → **absent**. Route as a Tier-2 clarity gap. *(The isolation-enforcement question itself — does bare-metal hardware access reach the Nitro control plane or a co-tenant — is **HARD STOP / out of scope**, Section 7; V/D-3's 20-min boot-verification latency is a single-tenant self-availability footgun, also out of scope.)*

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Capability cell disagrees with control-plane API | Family Security-specs tables ↔ `DescribeInstanceTypes` | implicit guarantee that doc == API |
| Compliance/attestation control built on false SEV-SNP/NitroTPM/transit claim | Security-specs tables | per-size capability booleans |
| Launch of IAM-forbidden instance type | `RunInstances` + `ec2:InstanceType` condition | the condition key as sole gate |
| Type-restriction bypass via launch template / fleet / ABIS / ModifyInstanceAttribute | `RunInstances`/`ModifyInstanceAttribute`/`CreateLaunchTemplate` | `ec2:IsLaunchTemplateResource`, launch-time Deny |
| AWS sample "approved instance types" policy leaves a bypass | AWS-published IAM example (Lens R) | the sample's own stated scope |
| Attestation gate fails open (absent/wildcard/all-zero/under-binding PCR) | KMS `kms:RecipientAttestation` + NitroTPM/Enclaves | measured-boot attestation condition |
| `PutKeyPolicy` accepts bogus PCR | KMS key policy authoring | authoring-time validation |
| End-of-sale U-* type still launchable | `RunInstances` / ABIS | "no longer available for new launches" |
| Cross-tenant degradation below equal share | shared Nitro host (network/disk) | "each receives an equal share" |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)

- **AWS Nitro service plane** — the Nitro card, Nitro security chip, Nitro hypervisor, host firmware, and the attestation root of trust are AWS-owned. Attempting to reach them, extract their credentials/ARNs, or break hypervisor memory isolation is the **shared-responsibility line → HARD STOP + disclosure**, not a hunting target.
- **Bare-metal "full access to host hardware"** is the *documented product behavior*; using it to attack the Nitro controller is out of scope. The in-scope angle is only the documented-guarantee-vs-enforcement question (Lens U).
- **IMDS on these managed hosts** — instance-metadata-service attacks are a general EC2 topic, not specific to this guide; out of scope here.
- **Single-tenant self-DoS** (exhausting your own instance's credits/share) and **performance within the equal-share guarantee** (merely slow neighbor) — out of scope.
- **Hardware/CPU micro-architectural side channels** (Spectre-class, cross-tenant cache timing) on shared hosts — AWS-plane / research-grade, out of scope for a docs-derived application-layer plan.
- **Product/feature-parity gaps** (a region lacking a type, a size not offering enclaves) are design facts, not vulnerabilities — only a *false documented claim* about them is in scope (Lens U).
- **Customer-authored** IAM policies that over-grant (a customer's own least-privilege footgun) — out of scope; **AWS-authored** sample/managed policies are in scope (Lens R, carve-out).

---

## 8. Null Hypotheses / Doc Gaps (lenses checked and why they don't fire)

Pages checked for triggers: `instance-types.md`, `ec2-nitro-instances.md`, `ec2-instance-type-specifications.md`, `instance-type-names.md`, `ec2-instance-regions.md`, `ec2-instance-quotas.md`, `doc-history.md`, and family pages `gp/co/mo/so/ac/hpc/pg.md` (summary + security-spec sections). The guide is a read-only hardware catalog with no customer API, upload, URL field, parser, OAuth, session, or 3P integration of its own, so most input-handling lenses are genuine nulls:

- **Lens A (cross-tenant IDOR):** instance-type names are a **public, fully-enumerable catalog** (`instance-type-names.md`), not tenant-scoped resources with ownership — nothing to IDOR. Checked all guide pages: no resource-by-ID API unique to this guide. Null (the capability-API enumeration angle folds into 5.1/5.5).
- **Lens B/C (PassRole / credential vending):** the guide describes no role-ARN input or credential-vending. Null for this guide (but see 5.2 `ModifyInstanceAttribute(userData)` late-binding note, which belongs to the broader EC2 surface, not this guide).
- **Lens D/V (data→control-plane / network segmentation):** the only such boundary is guest→Nitro-plane, which is **out of scope / hard stop** (Section 7). No customer-reachable control ENI described here.
- **Lens F (injection / translation):** no customer-input parser/translator in this guide. Null.
- **Lens G (SSRF):** checked `instance-types.md`, Nitro, specs, names, regions, quotas pages — **no field the service dereferences** (no URL/URI/webhook/logo/import). Null.
- **Lens H (CMK/encryption-context):** EBS/instance-store encryption is mentioned as a capability only; no key-policy/encryption-context mechanics in this guide. Folds into Lens W (5.3) for enclave keys. Otherwise null here.
- **Lens I (tagging/ABAC):** no tag mechanics in this guide (tag-on-launch belongs to RunInstances docs elsewhere). Partially relevant to 5.2 self-widen; otherwise null.
- **Lens J (OAuth/3P), K (prompt/LLM), M (shared-identifier/session), N (ARN migration), O (audit-log), P (registration/proofing), Q (file upload), T (secret storage), AA (share/revoke), BB (canonicalization), CC (upstream-context), DD (cache-key), EE (predictable-name), FF (JWT):** **no triggers** on any guide page — no sessions, tokens, uploads, shares, caches, auth layers, or predictable-name resolution described. All null for this guide.
- **Lens Y (transport/TLS):** "Encryption in transit" is a per-type **capability claim** (handled under 5.1/5.3 as a doc-vs-enforcement question — is it default-on, verifiable, conditionable?). No customer-facing `http://` endpoint or signature-version surface in this guide. Mostly folded into 5.1; see subagent detail.
- **Doc gaps requiring live/API confirmation first:** the exact `DescribeInstanceTypes` field names for SEV-SNP and Nitro-Enclaves support, and whether encryption-in-transit is API-conditionable, are **not fully resolved from the guide alone** — marked "doc-gap — confirm surface first" and assigned to the capability-audit subagent (results merged into 5.1/5.3).

---

## Appendix — Deep-dive subagent findings & related plans

The leads in Sections 5.1–5.6 are distilled from three parallel documentation deep-dives. The **full** per-lead detail (exact doc line cites, longer mechanism write-ups, per-lead severity/scope tables, and explicit-null registers) lives in these scratch files alongside this plan — read them before executing a lead, not instead of this plan:

- **`instancetypes-scratch-lensUX.md`** — Lens U (doc-vs-API capability integrity) and Lens X (action-family / end-of-sale / ABIS parity). Backs Section 5.1. Confirms the `InstanceTypeInfo` field substrate and the single-field `InstanceTypeInfoFromInstanceRequirements` ABIS response.
- **`instancetypes-scratch-lensSR.md`** — Lens S (condition-key scoping semantics) and Lens R (AWS-authored sample-policy audit). Backs Section 5.2. Holds the full `list_ec2.md`/`list_autoscaling.md` condition-key inventory, the camelCase/PascalCase `Attribute` evidence, and the `ExamplePolicies_EC2.md` composition walk-through.
- **`instancetypes-scratch-lensWVL.md`** — Lens W (attestation-conditioned authz: Enclaves + NitroTPM), V/D (bare-metal/host isolation), Y (transport), L (shared-host contention). Backs Sections 5.3, 5.4, 5.6. Holds the W-1..W-6 detail, the HARD-STOP register, and the Y-1 per-flow-verifiability analysis.

**Related sibling plans in `/work/aws-docs/` (do not duplicate — cite and defer to them for their owned surface):**
- `nitrotpm-attestation` plan (AF-1..AF-7) — owns the NitroTPM attestation-hub PCR-value-acceptance questions; this plan's W-3/W-4/W-5 are the Enclaves-side extension of that dependency.
- `isolate-data-operators` plan — owns the Nitro "no operator access" isolation claim (the B1/HARD-STOP boundary); this plan's V/D-1 defers to it.
- `sev-snp` plan — owns the AMD SEV-SNP feature-page attestation/condition-key analysis; this plan references it for the confidential-compute capability cells (5.1) and `ec2:CpuOptionsAmdSevSnp` (5.2).

Each scratch file is documentation-derived only; treat identically to the leads above. Nothing in this plan or its scratch files has been tested against a live AWS account.
