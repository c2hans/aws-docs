# Amazon Aurora DB Instance Classes — Attack Research Plan

Source of leads: `Concepts.DBInstanceClass.html` + 4 sub-pages (`.Types`, `.SupportAurora`, `.RegionSupportAurora`, `.Summary`) and the linked feature pages (`AuroraPostgreSQL.optimized.reads.md`, `aurora-serverless-v2*.md`). Offline mirror: `/work/aws-docs/docs/AmazonRDS/latest/AuroraUserGuide/`. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

Built with `security-questionbuilder`. Companion to the broader `AmazonAurora-attack-research-plan.md` (see [[task_aurora_userguide]]); this plan is scoped to the **compute/hardware-selection surface** (instance-class type, size, local NVMe, Serverless-v2 ACU, burstable credits) that the engine-level RDS/Aurora plans do not cover.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This surface is **infrastructure/config**, not an API with role-ARN/URL/token inputs, so the injection/credential/SSRF/token lenses are mostly **null** — recorded explicitly in §8. The live leads cluster on **data-at-rest on ephemeral local storage, tenant isolation of shared managed fleets, resource-exhaustion/DoS, and doc-vs-API capability integrity.**
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro host, the shared Serverless fleet control plane, the Grover storage fleet), stop, preserve evidence, flag for AWS-Security disclosure. Aurora compute runs on **AWS-managed hosts on the shared-responsibility line** — most of this surface sits *at* that line, so calibrate scope carefully (see §7).

---

## 1. Pentest Objectives (boundary-breach goals as concrete outcomes)
1. **Recover another tenant's data from ephemeral local NVMe** (Optimized Reads `db.r6gd`/`r6id`/`r8gd` temp objects + tiered cache) — after a class-switch, a scale event, or by reading NVMe blocks not scrubbed between tenants on the shared host.
2. **Prove customer data is written to local NVMe *unencrypted* (or under a key other than the cluster CMK)** — real row data (tiered cache) and query intermediates (temp objects) at rest on instance-store.
3. **Read/interfere with a co-resident tenant** on a shared Nitro host or shared Serverless-v2 fleet (memory remanence across ACU scaling / auto-pause resume; noisy-neighbor timing).
4. **Force cross-tenant or self denial-of-service** via burstable CPU-credit exhaustion, `FreeEphemeralStorage` exhaustion, or the immediate engine-restart triggered by an IO-Optimized↔Standard switch on an NVMe class.
5. **Show a security guarantee the docs assert is unenforced** — "dedicated hardware" (Nitro) isolation, "T classes for dev/test only," and the SupportAurora capability matrix vs the control-plane `Describe*` APIs.
6. **Flip a security-relevant posture implicitly via a compute-sizing change** — e.g. `ModifyDBInstance` to an NVMe class silently enabling Optimized Reads and placing data on local storage, with no distinct authorization gate.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** No dedicated API on this page; instance class is a *parameter* (`DBInstanceClass`) to control-plane actions `CreateDBInstance` / `ModifyDBInstance` / `CreateDBCluster` (+ `ServerlessV2ScalingConfiguration` on the cluster). Read/enumeration via `DescribeOrderableDBInstanceOptions`, `DescribeDBInstances`, `DescribeDBEngineVersions`. All SigV4 IAM, standard RDS control plane.

**Instance-class families (assets that change the physical/isolation posture):**
- **`db.serverless`** (Serverless v2) — a *shared managed fleet*; Aurora "adjusts compute, memory, network dynamically." ACU range `MinCapacity`/`MaxCapacity`; `Min=0` enables scale-to-zero auto-pause/resume. Fleet co-residency + resume-from-pause are the isolation-critical seams.
- **Memory-optimized R/X** (`r4/r5/r6i/r6g/r7g/r7i/r8g/x2g`) — EBS-optimized only, no local store. `r6i`/`r7i`/`r8g` etc. "powered by the AWS Nitro System, dedicated hardware + lightweight hypervisor" (an isolation *claim*).
- **Optimized Reads / NVMe classes** (`db.r6gd`, `db.r6id`, `db.r8gd`) — **direct-attached local NVMe SSD** (up to 11.4 TB on r8gd). Two consumers of that NVMe:
  - *Temporary objects*: PostgreSQL temp files (sorts/joins/merges) placed on `aurora_temp_tablespace` → NVMe. Cannot be moved back to EBS.
  - *Tiered cache* (I/O-Optimized clusters only): Aurora places **actual data blocks** on NVMe as an L2 cache (`pg_prewarm` proactively loads real data blocks). ~10% NVMe for internal ops, rest = tiered cache; `aurora_temp_space_size` resizes temp region up to 90% of NVMe.
  - Aurora MySQL: **not supported** ("No" across r6gd/r6id/r8gd in SupportAurora) — PostgreSQL-only, versions 14.9/15.4/16.1/17.4+.
- **Burstable T** (`t2`/`t3`/`t4g`) — Unlimited mode by default (burst beyond baseline → extra charge). Docs: "dev/test/nonproduction only." Small memory (2–8 GiB).

**Accounts / hosts / tenancy.** Customer account owns the cluster/instances; the **physical host, hypervisor, and local NVMe are AWS-owned managed fleet**. Provisioned R/X classes = one DB instance per host tenancy model *asserted via Nitro* but not detailed here. Serverless-v2 = explicitly shared, dynamically packed fleet. Storage (cluster volume) is the separate Grover fleet (not on this page).

**Untrusted-data transforms.** None on this page — no parser, translator, or customer-URL/blob field. Injection/SSRF seams live in the engine, not in class selection.

```
Customer IAM (SigV4) ──Create/ModifyDBInstance(DBInstanceClass)──▶ RDS control plane
                                                                     │
                    ┌────────────────────────────────────────────────┼─────────────────────┐
                    ▼                         ▼                        ▼                      ▼
             db.serverless             db.r6gd/r6id/r8gd         db.r6i/r7i/r8g...        db.t3/t4g
          (SHARED fleet, ACU        (local NVMe SSD:            (EBS-only, Nitro       (burstable,
           scale + auto-pause)       temp objects + tiered       "dedicated HW")        Unlimited-mode
                    │                 cache = REAL data)              │                  credits)
                    ▼                         ▼                                              ▼
        [tenant-isolation of        [data-at-rest on ephemeral                   [CPU-credit/noisy-
         shared fleet: DOC-GAP]      NVMe: encryption + scrub                      neighbor, billing DoS]
                                     lifecycle DOC-GAP]
                             ─────────────── AWS-managed host / hypervisor (shared-responsibility line) ───────────────
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Tenant A DB engine | Local NVMe blocks previously used by Tenant B (same host, after class-switch/reprovision) | Instance-store reuse across tenant lifecycles | Reading any byte of B's temp/tiered-cache data from A's NVMe = **breach** |
| Customer (reads own NVMe temp/cache) | Data-at-rest confidentiality guarantee (cluster CMK) | Aurora writes temp objects + real data blocks to local NVMe | NVMe contents readable in cleartext, or under a key ≠ cluster CMK = **encryption-guarantee breach** |
| Tenant A Serverless-v2 instance | Tenant B on same Serverless fleet host | Dynamic ACU packing / resume-from-pause on shared fleet | Reading B's memory/data, or resume returning stale B state = **cross-tenant breach** |
| Any tenant | Shared Nitro host / co-resident tenant | CPU/cache/memory-bandwidth contention on shared HW | Cross-tenant DoS or a side-channel read = **breach** (side-channel on Nitro HW = likely out of scope / hard-stop) |
| Low-priv IAM principal | Security posture of a running instance | `ModifyDBInstance(DBInstanceClass)` to NVMe class silently enables on-disk data placement | Posture flip (data now on local NVMe) with no distinct authz gate = **weak-enforcement** |
| Customer / attacker within account | Shared fleet availability for others | Burstable Unlimited credits / `FreeEphemeralStorage` exhaustion / IO-Opt↔Std restart | Another tenant's availability degraded = **High**; self-DoS/billing = Low–Med |
| Any customer surface | AWS service plane (Nitro host cred, Serverless control fleet, Grover) | — | Any AWS-fleet identity/ARN = **HARD STOP** |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `CreateDBInstance` / `CreateDBCluster` | POST (SigV4) | Yes | Yes | Sets initial `DBInstanceClass` / `ServerlessV2ScalingConfiguration` | Yes | Account IAM w/ `rds:CreateDB*` | Choosing NVMe class auto-enables Optimized Reads (posture side-effect) |
| `ModifyDBInstance` | POST | Yes | Yes | Changes `DBInstanceClass` in place (Graviton swap, →NVMe, →burstable) | Yes | `rds:ModifyDBInstance` | Class change to/from NVMe alters on-disk data placement; IO-Opt↔Std on NVMe = **immediate engine restart** |
| `ModifyDBCluster` | POST | Yes | Yes | `--serverless-v2-scaling-configuration Min/MaxCapacity` | Yes | `rds:ModifyDBCluster` | Min=0 → scale-to-zero auto-pause/resume |
| `DescribeOrderableDBInstanceOptions` | POST | No | Yes | Which classes are orderable per engine/version/Region | Yes | any `rds:Describe*` | **Ground-truth for Lens U capability diff** vs SupportAurora table |
| `DescribeDBEngineVersions` / `DescribeDBInstances` | POST | No | Yes | Version↔class support; current class | Yes | any `rds:Describe*` | Confirms doc capability cells |
| CloudWatch `FreeEphemeralStorage`, Optimized-Reads cache-hit | metric | No | Yes | NVMe free space / cache hit | Yes | `cloudwatch:GetMetricData` | Exhaustion/monitoring signal (Lens L) |
| Instance params `aurora_temp_space_size`, `temp_tablespaces`, `aurora_temp_tablespace` | param-group | Yes | Yes | Resize NVMe temp region (2× mem → 90% NVMe); temp tablespace is read-only-to-EBS | Yes | `rds:ModifyDBParameterGroup` | `aurora_temp_tablespace` **cannot** be modified or pointed back to EBS |

No non-SDK/hidden endpoints on this surface. **Undocumented-knob check:** the only near-hidden behavior is that a *compute* parameter (`DBInstanceClass` = NVMe family) implicitly toggles a *data-placement* feature (Optimized Reads) with no separate flag or warning — treat as a Lens U lead, not an auth knob.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### AREA 1 — Data-at-rest on ephemeral local NVMe: encryption + key binding (Lens H / U) — TOP
**Background.** Optimized Reads classes (`db.r6gd`/`r6id`/`r8gd`) place two kinds of customer data on **direct-attached local NVMe SSD**: PostgreSQL temporary objects (sort/join/merge intermediates via `aurora_temp_tablespace`) and — on I/O-Optimized clusters — a **tiered cache of actual data blocks** (`pg_prewarm` loads real rows; up to ~90% of an 11.4 TB NVMe). The Aurora cluster volume is encrypted with the cluster KMS CMK, but **this page and `AuroraPostgreSQL.optimized.reads.md` are silent on whether the local NVMe instance store is encrypted at rest, and under which key.**
**Security Concern.** If the local NVMe is unencrypted, or encrypted under an AWS-fleet/instance-ephemeral key rather than the customer cluster CMK, then real customer rows and query intermediates sit at rest outside the CMK boundary the customer believes protects "their data at rest" — defeating a compliance/attestation control built on "all data encrypted with my CMK." Directly parallels the confirmed doc-gap pattern in RDS temp-file/NVMe pages ([[task_rds_postgresql_managingtempfiles]], [[task_rds_oracle_tempfiles]], [[task_aurora_secretsmanager_storagetype]]).
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* Data on the Optimized-Reads NVMe is **not** encrypted under the cluster CMK. → *Oracle:* on an encrypted cluster, disable/revoke the cluster CMK and confirm whether temp-object queries and tiered-cache reads still succeed (if NVMe access survives CMK revocation, it is not CMK-bound). Cross-check `DescribeDBInstances`/docs for any statement that instance-store is CMK-encrypted. → *Severity: High (encryption-boundary gap); Informational if AWS confirms CMK coverage but never documented it (still a doc defect).* → *Stop:* documentation/behavior settles the key binding.
- *Claim:* NVMe holds real row data (not just scratch) confirming blast radius. → *Oracle:* `pg_prewarm` + Optimized-Reads cache-hit metric shows table blocks resident on NVMe. → *Severity: raises Area-2/3 impact.*
**Doc evidence:** `AuroraPostgreSQL.optimized.reads.md` L24–61 (tiered cache = data blocks; `aurora_temp_tablespace` NVMe, non-revertible). **Severity-if-true: High.**

### AREA 2 — Ephemeral-NVMe scrub lifecycle across class-switch / reprovision (Lens AA / A / EE)
**Background.** Docs instruct switching Optimized Reads off by **modifying `db.r6gd.4xlarge` → `db.r6g.4xlarge`** (drop the NVMe). They never state what happens to the data on the local NVMe at that moment, nor when the instance is reprovisioned onto a different physical host, nor how instance-store is scrubbed before the host/NVMe is handed to the next tenant.
**Security Concern.** Instance-store on shared managed fleets is the classic cross-tenant remanence surface: if NVMe blocks are not cryptographically erased (or the encryption key not destroyed) between tenant lifecycles, a later tenant provisioned onto the same physical NVMe could read the prior tenant's temp/tiered-cache data. This is exactly the "revocation/teardown completeness" shape of Lens AA and the shared-fleet remanence of Lens EE.
**High-level Test Scenarios:**
- *Claim:* After a class-switch away from NVMe (or delete), the freed NVMe is reassigned to another cluster/tenant without a scrub the customer can rely on. → *Oracle:* provision → write canary to temp/tiered cache → switch class / delete → reprovision an NVMe instance repeatedly and scan instance-store for the canary. (Live test only in an authorized single-account lab; **cross-tenant read against a foreign tenant = HARD STOP + disclose.**) → *Severity: cross-tenant remanence = Critical; doc-gap only = flag.*
- *Claim:* The switch itself loses/mishandles in-flight temp data. → lower priority (availability, not confidentiality).
**Doc evidence:** `optimized.reads.md` L47 (IO-Opt↔Std switch = immediate restart), L83 (class-switch to drop NVMe). **Severity-if-true: Critical (if cross-tenant); otherwise doc-gap.**

### AREA 3 — Serverless-v2 shared-fleet isolation & resume-from-pause remanence (Lens EE / V / A) — DOC-GAP, confirm surface first
**Background.** `db.serverless` runs on a fleet Aurora dynamically scales (ACU up/down) and can **pause to zero and resume** (`MinCapacity=0`). Nothing on the instance-class pages describes how compute/memory is isolated between tenants on that shared fleet, how memory is zeroed across ACU downscale/upscale, or whether resume-from-pause guarantees a clean state.
**Security Concern.** A dynamically packed multi-tenant fleet is the highest-value cross-tenant zone (skill Step-1). Memory remanence across ACU scaling or a resume that restores stale/foreign in-memory state would cross the tenant boundary. Matches the "isolation asserted, not described" note in [[task_aurora_featuregrids]].
**High-level Test Scenarios:**
- *Claim:* ACU downscale→upscale or pause→resume can expose another tenant's in-memory state / cached pages. → *Oracle:* in an authorized lab, drive rapid ACU oscillation and scale-to-zero cycles while probing buffer/temp contents for non-self data. **Any foreign-tenant byte = HARD STOP.** → *Severity: Critical if confirmed.*
- *Claim:* Resume-from-zero returns stale session/connection state. → *Oracle:* connection/session behavior across auto-pause boundary. → *Severity: Medium–High.*
**Doc evidence:** `Concepts.DBInstanceClass.Types.md` (db.serverless "adjusts resources dynamically"); `aurora-serverless-v2.create.md` L69 (Min=0 auto-pause). **Severity-if-true: Critical.** *Mark doc-gap: the class pages assert isolation only implicitly — confirm the mechanism before hunting.*

### AREA 4 — Resource exhaustion / DoS on burstable + ephemeral resources (Lens L)
**Background.** T-classes default to **Unlimited mode** (burst beyond baseline for an *additional charge*). Optimized-Reads NVMe is finite (`FreeEphemeralStorage`), and an IO-Optimized↔Standard switch on an NVMe class forces an **immediate engine restart**. `aurora_temp_space_size` can claim up to 90% of NVMe.
**Security Concern.** (a) Unlimited-mode credits turn a CPU-heavy workload into unbounded cost = **billing/financial DoS**. (b) A query flood that fills NVMe temp space → `FreeEphemeralStorage` exhaustion → failed queries / instability. (c) On a shared host, a noisy neighbor consuming CPU/credits/NVMe/network-bandwidth (see the per-class Mbps/Gbps caps) degrades co-resident tenants.
**High-level Test Scenarios:**
- *Claim:* One tenant can exhaust NVMe temp space and destabilize the instance (self-DoS) — or, on a shared host, a co-resident. → *Oracle:* saturate temp objects, watch `FreeEphemeralStorage`→0 and query failure. → *Severity: self-DoS Low; cross-tenant High.*
- *Claim:* Unlimited-mode burst yields uncapped cost with no default ceiling. → *Oracle:* doc confirms Unlimited default + no cap knob on this page. → *Severity: Low (billing, single-tenant).*
**Doc evidence:** `Types.md` (t4g/t3/t2 Unlimited default); `optimized.reads.md` L39/L158 (`aurora_temp_space_size` 90%; `FreeEphemeralStorage`); `Summary.md` (per-class bandwidth caps). **Severity-if-true: cross-tenant High, else Low.**

### AREA 5 — Documented-guarantee vs enforcement & doc-vs-API capability integrity (Lens U)
**Background.** Three assertions to turn back on the docs: (1) Nitro classes give "dedicated hardware and lightweight hypervisor" (isolation claim); (2) "We recommend T classes only for dev/test/nonproduction"; (3) the whole SupportAurora capability matrix (which class × engine × version is supported; Optimized-Reads = "No" for all Aurora MySQL; t4g `2xlarge`/`small` = "No").
**Security Concern.** (1) "Dedicated hardware" is an isolation *promise* — nothing on the customer side enforces or attests it; a compliance control built on it is advisory-only. (2) The dev/test recommendation is prose, not a guardrail — nothing stops production on an under-provisioned burstable class (availability posture). (3) A capability cell that disagrees with `DescribeOrderableDBInstanceOptions`/`DescribeDBEngineVersions` lets a customer build a false gating assumption ("MySQL can't use NVMe classes so no data hits local disk") — if the API actually orders it, the doc-based control is wrong.
**High-level Test Scenarios:**
- *Claim:* At least one SupportAurora matrix cell contradicts the control-plane API. → *Oracle:* diff every cell against `DescribeOrderableDBInstanceOptions` per Region/engine/version; count mismatches. → *Severity: Informational/Low but AWS-owned and filable.*
- *Claim:* "Dedicated hardware" isolation has no customer-verifiable attestation. → *Oracle:* look for any `Describe*` field or attestation exposing host tenancy; absence = advisory-only guarantee. → *Severity: Informational.*
- *Claim:* Nothing gates a compute-sizing change from silently changing data-placement posture (→NVMe class auto-enables Optimized Reads). → *Oracle:* `ModifyDBInstance` to an NVMe class needs only `rds:ModifyDBInstance`, no separate consent for on-disk placement. → *Severity: Low–Medium (posture-flip via generic action).*
**Doc evidence:** `Types.md` (Nitro claim, T dev/test note); `SupportAurora.md` (matrix); `optimized.reads.md` L75 ("automatically uses Optimized Reads"). **Severity-if-true: Informational–Medium.**

### AREA 6 — ABAC / authorization scoping of class-change actions (Lens I / S) — thin
**Background.** `DBInstanceClass` is just a parameter to `Modify/CreateDBInstance`; there is no class-specific condition key documented.
**Security Concern.** If an org relies on IAM to *restrict which instance classes* a principal may select (e.g. "no NVMe classes for team X to keep data off local disk", or "no giant classes for cost"), is there a condition key that actually binds the class value? RDS has no `rds:DatabaseClass`-style key documented here — so such a control likely cannot be expressed, and a principal with `rds:ModifyDBInstance` can pick any class (self-widen the physical posture).
**High-level Test Scenarios:**
- *Claim:* No IAM condition key scopes `DBInstanceClass`, so class selection cannot be least-privileged. → *Oracle:* check the RDS IAM condition-key reference for a class key; attempt a Deny on class value. → *Severity: Low (customer least-priv footgun) unless class = data-placement control, then Medium.*
**Doc evidence:** absence across all four pages + [[task_rds_iam_dbauth_hub]] (RDS condition-key gaps). **Severity-if-true: Low–Medium.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant read of prior tenant's NVMe temp/tiered-cache data | Optimized-Reads local NVMe instance-store | (undocumented) instance-store scrub / key destruction between lifecycles |
| Customer data at rest on NVMe outside cluster CMK | `aurora_temp_tablespace`, tiered cache | (undocumented) NVMe encryption + CMK binding |
| Cross-tenant memory remanence on Serverless-v2 fleet | `db.serverless` shared fleet, ACU scale / auto-pause | (undocumented) per-tenant memory isolation & zeroing |
| Noisy-neighbor / cross-tenant DoS on shared Nitro host | any provisioned class on shared HW | Nitro "dedicated hardware" claim; per-class bandwidth caps |
| NVMe temp exhaustion instability | `aurora_temp_space_size`, `FreeEphemeralStorage` | size ceiling (90%) + CloudWatch monitoring (customer-side) |
| Immediate restart via IO-Opt↔Std switch on NVMe class | `ModifyDBInstance` / `ModifyDBCluster` | none (documented as expected behavior) |
| Posture flip: sizing change enables on-disk data placement | `ModifyDBInstance(DBInstanceClass→NVMe)` | none (auto-enabled, no separate gate) |
| Capability matrix vs control-plane API divergence | SupportAurora table vs `DescribeOrderableDBInstanceOptions` | doc accuracy only |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The Nitro hypervisor, host firmware, and CPU micro-architectural side-channels** (Spectre-class, cache timing) on AWS-managed hosts — shared-responsibility line; IMDS on managed hosts. Any evidence reaching the host/hypervisor identity = **HARD STOP + disclose**, not a hunt target.
- **Grover / cluster-volume storage fleet** — separate surface, not this page.
- **Engine-internal injection / SSRF / auth** (SQL, `sp_execute_postgresql`, DSN egress, IAM-DB-auth) — covered by the engine-specific RDS/Aurora plans, not the class surface.
- **Single-tenant self-DoS and Unlimited-mode billing surprise** — customer-inflicted, Low/out-of-scope unless it degrades *other* tenants.
- **Customer-authored IAM least-privilege gaps** on class selection — footgun, not an AWS defect (the *absence of a condition key* is the only AWS-owned angle, Area 6).
- **DNS rebinding / private-only endpoints** — N/A, no fetch surface here.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked and why they don't fire)
Pages checked for triggers: `Concepts.DBInstanceClass.md`, `.Types.md`, `.SupportAurora.md`, `.RegionSupportAurora.md`, `.Summary.md`, `AuroraPostgreSQL.optimized.reads.md`, `aurora-serverless-v2.create.md`, `aurora-serverless-v2-administration.md`.
- **B/C (confused-deputy / PassRole / credential vending):** no role-ARN, `SourceArn`, session-policy, or STS input on this surface. **Null.**
- **G (SSRF):** no field the service dereferences (no URL/host/endpoint). **Null.**
- **J (OAuth/3P), K (prompt injection), FF (JWT/OIDC), DD (cache-key), CC (upstream-context), BB (canonicalization):** no OAuth, no LLM/agent, no token validation, no caching layer, no multi-parser request path, no authorizer context. **Null.**
- **F (translation-layer injection):** no parser/translator in class selection (temp-file placement is not a customer-input transform). **Null** here; engine injection is out of scope (§7).
- **N (namespace migration):** instance-class *generations* co-exist (r5…r8g) but resolve to the same control-plane action with the same authz — no dual-namespace authz seam. **Null.**
- **W (attestation-conditioned authz):** no `kms:RecipientAttestation`/enclave gate on class selection. **Null** (the Nitro "dedicated hardware" claim is Lens U, not W — no PCR policy exposed).
- **Q (upload):** no upload/blob field. **Null.**
- **O (audit-log evasion):** class changes are standard `Modify*` CloudTrail events; no special evasion surface. **Low, not pursued.**
- **DOC-GAPS to confirm before hunting (surface unverified in docs):** (1) NVMe instance-store encryption + key binding (Area 1); (2) instance-store scrub between tenant lifecycles (Area 2); (3) Serverless-v2 per-tenant memory isolation & resume-from-pause state (Area 3). All three are the crux leads and all three are **undocumented** — treat as open, not closed.

---

## Priority summary (fire order)
1. **Area 1** — NVMe data-at-rest encryption/CMK binding (High; strong precedent).
2. **Area 2** — NVMe scrub lifecycle across class-switch/reprovision (Critical-if-cross-tenant; HARD-STOP-bounded).
3. **Area 3** — Serverless-v2 shared-fleet remanence (Critical-if-true; doc-gap, confirm first; HARD-STOP-bounded).
4. **Area 4** — burstable/ephemeral exhaustion & noisy-neighbor DoS (cross-tenant High).
5. **Area 5** — doc-vs-API capability + guarantee-vs-enforcement (Informational–Medium; AWS-owned, filable).
6. **Area 6** — no condition key to scope class selection (Low–Medium footgun).

> Every lead is a boundary hypothesis, not a claimed bug. The dominant theme unique to this surface: **customer data (real blocks + query intermediates) and compute both land on AWS-managed ephemeral hardware whose encryption, scrubbing, and tenant-isolation the instance-class docs never describe.** Confirm those three doc-gaps first; they gate the Critical outcomes.
