# AMI Billing Information (PlatformDetails / UsageOperation / Product Codes) — Attack Research Plan

**Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`)
**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html

**Source of leads (docs read, online + offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`):**
- UserGuide (the target page's own topic tree): `ami-billing-info`, `billing-info-fields`, `view-billing-info`, `verify-ami-charges`.
- Mechanism-supporting UserGuide pages (paid/marketplace + on-host signal): `paid-amis`, `get-product-code`, `using-paid-amis-finding-paid-ami`, `using-paid-amis-purchasing-paid-ami`, `using-paid-amis-support`, `sharingamis-intro`.
- APIReference (the *enforcing* mutating surface — read live 2026-09-07): `API_RegisterImage`, `API_CopyImage`. (Named-but-not-yet-read: `CreateImage`, `ImportImage`, `CreateRestoreImageTask`.)
- Adjacent, DIFFERENT billing feature (one word-hop away, NOT in this page's topic list — see §9): Capacity-Reservation billing-ownership transfer (`assign-billing`, `request-billing-transfer`, `view-billing-transfers`, and APIs `AssociateCapacityReservationBillingOwner` / `AcceptCapacityReservationBillingOwnership` / `RejectCapacityReservationBillingOwnership` / `DisassociateCapacityReservationBillingOwner` / `DescribeCapacityReservationBillingRequests`).

**Live-sync status (2026-09-07):** Target page and children fetched live — **byte-identical to offline mirror** (3 topics only: billing-info-fields, view-billing-info, verify-ami-charges; no URL/upload/CR field). `RegisterImage`, `CopyImage`, `AcceptCapacityReservationBillingOwnership` API-reference pages fetched live and used to close the pivotal doc-gaps below. Earlier fetch 2026-08-31 also byte-identical.

**Status:** Documentation-derived hypotheses only. Nothing tested against a live AWS account. This plan is the input a downstream hunter (`aws-vuln-hunter`) executes later. Where the docs are silent, the lead is marked **"doc-gap — confirm surface first."**

> **SUSPECTED PROMPT INJECTION (noted, not executed).** Pages in this set carry a `## See also` block reading *"Skills for AI coding assistants (optional)… `aws agent-toolkit search-skills --search-query AWSEC2` …"*, worded to look like an instruction to an AI agent. It is published AWS page content (present live), treated as untrusted data; **no suggested CLI was run.** See memory `aws-docs-see-also-injection`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **This surface's crown jewel is BILLING INTEGRITY, not tenant data isolation.** The protected "resource" is the correct attribution of per-hour **software license charges** (RHEL, Windows, SQL Server Std/Ent/Web, SUSE, Ubuntu Pro) and **AWS Marketplace / ISV seller revenue**. A "breach" is running licensed/paid software while the billing code that bills it is **absent, downgraded, or mis-attributed** — cost avoidance or revenue theft — not reading another tenant's bytes. Ties to memory `sql-server-ec2-plan` (SQL HA license-waiver billing integrity) and `sql-downgrade-plan` (edition downgrade is customer self-assessment, not AWS-enforced).
- **DryRun is NOT an oracle.** `RegisterImage`, `CopyImage`, and the CR-billing APIs all expose `DryRun`, which returns `DryRunOperation` on caller-IAM success **before** resource resolution / disk-vs-code validation. Per the Lens A variant, treat `DryRun` as a caller-permission check only — never as evidence the billing/ownership enforcement held. Confirm every lead against the *real* post-launch CUR / `DescribeImages` state.
- **HARD STOP:** if evidence ever shows an identity/credential/ARN/account belonging to AWS's own service/billing plane, stop, preserve evidence, flag for AWS-Security disclosure. Do not probe AWS's billing/metering backend.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Strip a billing code.** Produce an AMI/instance that runs licensed software (RHEL / Windows / SQL Server) but whose `PlatformDetails`/`UsageOperation` (and CUR `lineitem/Operation`) is `Linux/UNIX` / `RunInstances` (no license charge) → **billing-code stripping = billing-integrity breach.** *(Live RegisterImage doc now confirms the mechanism — see Area 1.)*
2. **Downgrade a billing code.** Run SQL Server **Enterprise** (`RunInstances:0100`) while the attached code bills SQL **Web** (`RunInstances:0200`) or nothing → **under-billing / license misattribution.**
3. **Launder a code through Copy/Import/Register.** Use `CopyImage` / `ImportImage` / `CreateRestoreImageTask` to move licensed content into an AMI that carries no `billingProducts` → **code laundering.**
4. **Marketplace revenue theft.** Launch software from a **paid AMI** such that the seller's **product code** never attaches to the instance (no marketplace charge), while the software still runs → **theft of licensed/paid software.**
5. **Mis-attribution to a victim seller.** Cause an instance to carry **another** ISV's product code / a competitor's `UsageOperation`, inflating a victim's bill or polluting attribution. *(Live RegisterImage doc gates the direct path — "account must be authorized to specify billing product codes" — so test the AUTHZ STRENGTH of that gate and the snapshot-propagation side-channel, see Area 3.)*
6. **Detection-evasion.** Confirm whether a stripped/mismatched code leaves any **durable AWS-side** signal, given the docs frame the only reconciliation as a **customer-run** CUR check.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane APIs (SigV4/IAM): `DescribeImages` / `Get-EC2Image`, `DescribeInstances`, and the mutating AMI-creation surface (`RegisterImage`, `CreateImage`, `CopyImage`, `ImportImage`, `CreateRestoreImageTask`). Console **AMIs** and **Instances** → Details tab. On-instance: **IMDS** `/latest/meta-data/product-codes` (`get-product-code.html`, IMDSv1 + IMDSv2 examples).

**The billing-code metadata (the asset).**
- **`PlatformDetails`** — human string for the AMI's billing code, e.g. `Red Hat Enterprise Linux`, `Windows with SQL Server Enterprise`. Docs: "If two software licenses are associated with an AMI, the field shows both."
- **`UsageOperation`** — the machine billing code, `RunInstances:<hex>` (`:0010` RHEL, `:0100` SQL Ent, `:0004` SQL Std, `:0200` SQL Web, `:0002` Windows, `:0800` Windows BYOL, `:00g0` RHEL BYOL, `:000g` SUSE, `:0g00` Ubuntu Pro). Maps 1:1 to CUR `lineitem/Operation` and the Price List API. **Footnote gotcha:** Spot appends a zone suffix (`RunInstances:0010:SV006`) → the customer-run compare is NOT a naive string match (false-negative source, Area 5).
- **Product code** — AWS Marketplace product identifier for **paid AMIs**; retrievable on the instance via IMDS `/product-codes`.

These derive from an AMI's **`billingProducts` / product codes** and are **propagated to every instance launched from the AMI**, driving the per-hour software charge. The docs describe **no live editing** of these on an existing instance — the attach point is AMI creation and instance launch.

**Live doc-gap closure (RegisterImage, fetched 2026-09-07):**
- **`BillingProduct.N`** is an optional request array. Doc: *"The billing product codes. **Your account must be authorized to specify billing product codes.** If your account is not authorized… you can publish AMIs that include billable software and list them on the AWS Marketplace [after registering as a seller]."* → There **is** an authorization gate on directly setting codes. The interesting question shifts from "can I set an arbitrary code?" to **"how strong is that gate, and can I reach the same effect WITHOUT it?"**
- **Snapshot-derivation is the load-bearing mechanism (and its own gap):** *"When creating an AMI from a snapshot, the `RegisterImage` operation **derives the correct billing information from the snapshot's metadata, but this requires the appropriate metadata to be present.** To verify if the correct billing information was applied, check the `PlatformDetails` field… **If the field is empty or doesn't match the expected operating system code…, the AMI creation was unsuccessful, and you should discard the AMI** and instead create the AMI from an instance."* → If the source snapshot lacks the billing metadata, `RegisterImage` yields an AMI with an **empty `PlatformDetails`** (no license charge). AWS's **only** stated countermeasure is advisory — *"you should discard the AMI"* — i.e. **customer self-discipline, not service-side enforcement.** This directly confirms the Area 1 stripping mechanism and its self-assessment gap (same shape as `sql-downgrade-plan`).
- **Product-code propagation:** *"If any snapshots have AWS Marketplace product codes, they are copied to the new AMI."* → product codes ride the snapshot into the AMI automatically; stripping a *product code* therefore means stripping it at the snapshot level (a different volume-level operation), not at `RegisterImage` (Area 3).

**The "verification" is customer self-service, not an AWS control.** `verify-ami-charges.html` tells the *customer* to match the instance's CUR `lineitem/Operation` against the AMI's `UsageOperation` "to ensure that you're not incurring unplanned costs." There is **no documented AWS-side enforcement that running software matches the billed code** — enforcement (if any) lives in the launch path attaching `UsageOperation` from `billingProducts`.

```
  AMI creation/import                 launch                       reconciliation (DETECTION ONLY, customer-run)
  RegisterImage/CopyImage/  ── billingProducts ─►  Instance  ── UsageOperation ─►  CUR lineitem/Operation
  ImportImage/CreateImage        (product codes)     |  IMDS /product-codes             ▲
        │  ▲ derived from SNAPSHOT metadata          └───────────────────────────────────┘
        │  │  (absent metadata → empty PlatformDetails,       customer compares by hand (Spot suffix breaks naive compare)
        │  │   "discard it yourself" = advisory only)
        └─ [asset to protect] the code that decides the $/hour software charge
```

**Assets:** billing-code integrity (correct $/hr license charge); marketplace/ISV seller revenue & attribution; product code on the instance (trusted by some on-host BYOL license checkers). **Not** in play on this surface: no cross-tenant data store, no server-side URL fetch, no file upload, no LLM, no KMS *governing the billing code* (CopyImage does take `KmsKeyId`, but for volume encryption, not billing).

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Customer creating an AMI | AWS/ISV license-billing integrity | `RegisterImage`/`CopyImage`/`ImportImage`/`CreateImage` decide `billingProducts` | An AMI runs licensed SW but carries **no / a cheaper** billing code (empty `PlatformDetails`) — instance launches and CUR shows no/low license charge |
| Customer launching an instance | The $/hr charge | Launch path attaches `UsageOperation` from AMI `billingProducts` | Running SQL Ent / RHEL while `UsageOperation`=`RunInstances` (base) — **under-billing** |
| Launcher of a paid AMI | Marketplace/ISV seller revenue | Product-code attachment + owner's "confirm launched from paid AMI" | Paid software runs but **no product code attaches** → no marketplace charge, seller cannot confirm the launch |
| Any customer | Another ISV seller's revenue/attribution | Set a foreign `BillingProduct.N` (authz-gated) OR ride a foreign product code in via a snapshot | An instance you control carries a **victim seller's** code → bill inflation / attribution pollution |
| On-instance BYOL license checker | Instance metadata | IMDS `/latest/meta-data/product-codes` is the trust signal | A BYOL/entitlement checker trusts a product code that was stripped/spoofed → license bypass on-host |
| Customer | AWS-side detection | Only documented reconciliation is **customer-run** CUR compare (`verify-ami-charges`) | A billing mismatch that produces **no durable AWS-side record** → evasion |
| Any customer | **AWS's own billing/service plane** | — | Any AWS-service-plane identity/credential/ARN = **HARD STOP + disclose** |

---

## 4. API / Interface Inventory
(Authz/parameters for `CreateImage`/`ImportImage`/`CreateRestoreImageTask` still **doc-gap** — read the API ref before probing. `RegisterImage`/`CopyImage` closed live 2026-09-07.)

| Name | Method | Mutating? | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `DescribeImages` / `Get-EC2Image` | GET | No | Yes | Returns `PlatformDetails`, `UsageOperation` for an AMI | Yes (SigV4) | AMI owner + accounts it's shared with | **Read oracle** for the billing code |
| `DescribeInstances` / `Get-EC2Instance` | GET | No | Yes | Returns billing fields for an instance | Yes | Instance owner | Read oracle post-launch |
| `RegisterImage` | POST | **Yes** | Yes | Registers an AMI; **`BillingProduct.N`** array | Yes | Caller (BillingProduct.N requires account be "authorized") | **Prime lead.** Code derived from snapshot metadata; absent → empty `PlatformDetails`, advisory-discard only. `DryRun` present (not an oracle). |
| `CopyImage` | POST | **Yes** | Yes | Copies AMI across region/Outpost/Local Zone | Yes | Caller | **Live page documents NOTHING about billingProducts persistence** → the old "codes persist through copy" anti-laundering claim is NOT doc-supported; verify empirically (Area 2). `DryRun` present. |
| `CreateImage` | POST | **Yes** | Yes | AMI from a running instance (register in one call) | Yes | Instance owner | Does the created AMI inherit the running instance's codes? doc-gap |
| `ImportImage` / `ImportInstance` (vmimport) | POST | **Yes** | Yes | AMI from an imported VM (BYOL path) | Yes | Caller w/ vmimport role | BYOL-code assignment; see memory `vm-import-snapshot-plan` |
| `CreateRestoreImageTask` | POST | **Yes** | Yes | Recreate AMI from an S3-stored AMI | Yes | Caller | Round-trip via S3 — does the code survive? doc-gap; see `ami-store-restore-plan` |
| IMDS `/latest/meta-data/product-codes` | GET | No | Instance-local | Exposes marketplace product code | No (on-host) | Anyone on the instance | On-host trust signal for BYOL checkers |
| AWS Marketplace listing / product-code association (Marketplace API) | POST | Yes | Yes | Ties a product code to a seller AMI | Yes | Registered seller | Attribution root — **out of this UserGuide's scope**; hand to a Marketplace Seller Guide pass |

**Verbatim doc leads worth keeping:** "If two software licenses are associated with an AMI, the **Platform details** field shows both." · `paid-amis.html`: "The owner of the paid AMI can confirm whether a specific instance was launched using that paid AMI." (this confirmation statement **is** the attribution boundary) · Spot CUR operation differs (`RunInstances:0010:SV006`) — the customer compare is not a naive string match. · RegisterImage: "In most cases, AMIs for Windows, RedHat, SUSE, and SQL Server require correct licensing information to be present on the AMI."

---

## 5. Recommended Areas of Focus (priority-ordered; one block per firing lens)

### Area 1 — Billing-code stripping / downgrade at AMI creation (Lens U doc-vs-enforcement + Lens I integrity; **billing integrity — TOP PRIORITY**)
**Background.** `billingProducts`/`UsageOperation` decide the per-hour license charge, are attached at AMI register/copy/import time, then propagated to instances. **Live RegisterImage doc (2026-09-07)** states the code is **derived from the source snapshot's metadata**; if that metadata is absent, the AMI registers with an **empty `PlatformDetails`** and AWS's sole countermeasure is the advisory *"you should discard the AMI."*
**Security Concern.** If a caller can present a licensed root volume whose *snapshot metadata* lacks (or misstates) the billing code, `RegisterImage` produces a launchable AMI that runs licensed software billed as plain `Linux/UNIX` (`RunInstances`) or a cheaper code. AWS documents the failure mode and a manual fix, but **no service-side enforcement stops the caller from keeping and launching the code-free AMI** — the "verify" is left to the customer.
**High-level Test Scenarios (falsifiable claims):**
- **Claim 1a (strip):** `RegisterImage` over a snapshot of a licensed root volume (RHEL/Windows/SQL) whose metadata does not carry the billing code → `DescribeImages` returns **empty `PlatformDetails`** / `UsageOperation=RunInstances`; a launched instance's CUR shows **no license line** while the OS/DB provably runs.
- **Claim 1b (downgrade):** the derived/settable code can be made a **lower-priced** value (SQL Web `:0200`) for a disk running SQL **Enterprise** → under-billing; no AWS check that disk contents match the declared code.
- **Claim 1c (CreateImage divergence):** `CreateImage` from a licensed running instance, then re-register/re-map the snapshot, to drop or lower the license code.
- **Confirm/Refute oracle:** an AMI/instance provably **running** the licensed OS/DB (boot + verify) while `PlatformDetails`/`UsageOperation`/CUR `lineitem/Operation` shows **no or a cheaper** code. *(Do NOT rely on `DryRun` — it passes on IAM alone.)*
- **Preconditions:** account able to call `RegisterImage`/`CreateImage`; a licensed source volume. **Cost:** low.
- **Doc evidence:** `billing-info-fields.html` (code table); `API_RegisterImage` `BillingProduct.N` + snapshot-derivation/empty-`PlatformDetails`/"discard the AMI" paragraph (live 2026-09-07); `verify-ami-charges.html` (detective-only).
- **Severity-if-true:** **High → Critical** (systematic license-fee avoidance; ISV revenue harm). **Stop condition:** once ONE licensed-runs-but-billed-base instance is demonstrated — do not scale across products. If evidence implicates AWS's metering plane, HARD STOP.

### Area 2 — Copy / Import / Restore code laundering (Lens X twin/round-trip parity + Lens N; billing integrity)
**Background.** `CopyImage`, `ImportImage` (vmimport), and `CreateRestoreImageTask` (S3 round-trip) are alternate AMI-creation paths. **Correction from live CopyImage doc (2026-09-07):** the current `CopyImage` reference documents **nothing** about `billingProducts`/product-code persistence — the previously assumed "AWS anti-laundering rule: codes persist through CopyImage" is **NOT doc-supported** and must be treated as an unverified assumption, i.e. a laundering path to test rather than a control to trust.
**Security Concern.** A creation path that does **not** preserve/require the code lets an attacker launder licensed content into a code-free AMI, or (cross-account copy of a shared paid AMI) strip a seller's product code so launches evade the marketplace charge.
**High-level Test Scenarios:**
- **Claim 2a:** `CopyImage` of a paid/licensed AMI to another region/account **drops or lets the caller override** `billingProducts` → copy has empty/base `UsageOperation`.
- **Claim 2b:** Export→`ImportImage` (or `CreateRestoreImageTask` via S3) of a licensed disk yields an AMI with **no** billing code (BYOL/import path abused to launder a non-BYOL license).
- **Claim 2c (twin-parity):** the three creation paths (`RegisterImage` vs `CopyImage` vs `CreateRestoreImageTask`) enforce billing-code carry-over **inconsistently** — one preserves it, another does not (Lens X divergence on the same underlying content).
- **Confirm/Refute oracle:** post-copy/import `DescribeImages` shows licensed content but a **missing/base** code, and a launched instance incurs no license/marketplace charge.
- **Doc evidence:** `API_CopyImage` (silent on billingProducts — live 2026-09-07), `paid-amis.html`, `sharingamis-intro.html`; `ImportImage`/`CreateRestoreImageTask` API refs (doc-gap; see `ami-store-restore-plan`, `vm-import-snapshot-plan`).
- **Severity:** **High–Critical.** **Stop:** first successful laundered copy.

### Area 3 — Marketplace / paid-AMI revenue & attribution (Lens A cross-tenant $ + confused-deputy on money)
**Background.** Paid AMIs bill at the **owner's** rates; a product code identifies the seller's product; "the owner can confirm whether a specific instance was launched using that paid AMI." IMDS exposes the product code on-host. **Live RegisterImage doc:** product codes on a snapshot are **auto-copied into the AMI**, and directly setting `BillingProduct.N` requires the account be **authorized** (seller registration otherwise).
**Security Concern.** Two directions: (a) **evasion** — run the paid software while the product code fails to attach (no marketplace charge, seller can't confirm the launch); (b) **mis-attribution** — get **another** seller's product code onto your AMI/instance so a victim is charged/attributed. The direct `BillingProduct.N` path is authz-gated, so the interesting mis-attribution vector is the **snapshot side-channel** (does a snapshot carrying a foreign product code, e.g. from a shared/public paid AMI's snapshot, propagate that code into an AMI *you* register?).
**High-level Test Scenarios:**
- **Claim 3a (evasion):** launching a paid AMI via a non-standard path (copied snapshot, re-registered image, launch template) yields a running instance **without** the product code in IMDS or `DescribeInstances` → no marketplace bill.
- **Claim 3b (foreign-code via snapshot):** register an AMI from a snapshot that carries a **foreign** Marketplace product code — does the "auto-copied to the new AMI" behavior attach a code your account was never authorized to specify (bypassing the `BillingProduct.N` authz gate via the snapshot path)?
- **Claim 3c (authz-gate strength):** probe whether the `BillingProduct.N` "must be authorized" check can be satisfied by a low-privilege or non-seller account (weak/absent enforcement).
- **Claim 3d (confirmation severability):** the owner's "confirm a specific instance launched from my paid AMI" mechanism can be **defeated** (instance runs the bits but is unconfirmable).
- **Confirm/Refute oracle:** a running instance provably executing paid software with **absent or foreign** product code (IMDS `/product-codes` + `DescribeInstances`), and/or a seller-confirmation query returning negative for a real launch.
- **Doc evidence:** `paid-amis.html`, `get-product-code.html`, `using-paid-amis-*`, `API_RegisterImage` (product-code auto-copy + BillingProduct.N authz — live 2026-09-07). Marketplace association API is out-of-UserGuide → **doc-gap, Marketplace Seller Guide pass.**
- **Severity:** **High** (theft of licensed software / cross-seller revenue harm). **Stop:** first confirmed code-free-but-running paid instance, or foreign-code attach.

### Area 4 — On-host product-code trust for BYOL license enforcement (Lens M-style trusted-signal spoof)
**Background.** `get-product-code.html` reads `/latest/meta-data/product-codes` (IMDSv1 + IMDSv2); BYOL/entitlement software on the instance commonly trusts this and the AMI's billing code to decide whether a license is present.
**Security Concern.** If the product/billing code can be stripped or forged (Areas 1–3), an **on-instance** license checker that trusts IMDS is bypassed even where AWS billing is unaffected — and conversely a spoofed code could unlock paid features.
**High-level Test Scenarios:**
- **Claim 4a:** an instance launched from a code-stripped AMI presents **no** product code to on-host BYOL software → license gate opens / fails-open.
- **Claim 4b:** IMDS product-code value is influenced by the launcher (via the AMI's declared codes) to a value the ISV's checker treats as "entitled."
- **Confirm/Refute oracle:** on-host license logic reaching a different decision as `/product-codes` is varied.
- **Doc evidence:** `get-product-code.html`. **Severity:** **Medium–High** (depends on ISV; product-integrity, not AWS data). **Note:** IMDS *availability* on managed hosts is out-of-scope; the *content-trust* question is in-scope.

### Area 5 — Reconciliation-as-detection-only / audit gap (Lens O)
**Background.** The only documented check that billed code == running software is the **customer-run** CUR compare in `verify-ami-charges.html`. Spot operations differ (`:SV006` suffix) and two-license AMIs "show both", so even that compare is non-trivial.
**Security Concern.** Enforcement lives (if anywhere) at launch, not reconciliation; a mismatch produced by Areas 1–3 may leave **no durable AWS-side signal** and no customer-visible one unless they run the manual compare.
**High-level Test Scenarios:**
- **Claim 5a:** a stripped/downgraded code produces a CUR line indistinguishable from legitimate base usage — no anomaly surfaced to AWS or the customer.
- **Claim 5b:** the Spot suffix / "shows both" formatting creates a false-negative in a customer's naive string-compare, hiding a genuine under-bill.
- **Confirm/Refute oracle:** a demonstrated mismatch (Area 1–3) with no corresponding AWS-side integrity alert and a CUR line that passes a reasonable customer compare.
- **Doc evidence:** `verify-ami-charges.html`, `billing-info-fields.html` footnotes 1–3.
- **Severity:** **Low–Informational** on its own; **raises severity of Areas 1–3** by removing detection.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Register/create AMI with stripped/downgraded code over licensed content | `RegisterImage`/`CreateImage` | Snapshot-metadata derivation; empty `PlatformDetails` → **advisory "discard the AMI" only** (no enforcement) |
| Launder license via `CopyImage`/`ImportImage`/`CreateRestoreImageTask` | AMI copy/import paths | **Undocumented** on live CopyImage page — verify carry-over empirically on every path |
| Run paid-AMI software without product-code attachment | Marketplace launch path | "Owner can confirm launch from paid AMI" (attack the severability of that confirmation) |
| Attach a foreign seller's product code | `RegisterImage` `BillingProduct.N` / snapshot auto-copy | "Account must be authorized to specify billing product codes" (probe gate strength + snapshot side-channel) |
| Spoof/strip IMDS product code for on-host BYOL checker | IMDS `/product-codes` | ISV-side; AWS provides the signal only |
| Under-bill undetected | CUR reconciliation | Customer-run compare only — no AWS enforcement documented |
| Any action reaching AWS's billing/metering plane | all | shared-responsibility line — **HARD STOP** |

---

## 7. Out-of-Scope Risk Categories
- **Tenant data isolation, SSRF, file upload, prompt injection, KMS confusion (as an access-control break)** — none of these mechanisms exist on this billing-metadata surface (no server-side fetch, no upload field, no LLM, no per-tenant datastore, no CMK gating the billing code). See §8.
- **IMDS availability/reachability** on fully-managed hosts (product-code *content trust* is in-scope; IMDS existence is not).
- **AWS Marketplace internal billing/settlement pipeline** and ISV contract terms — out of this UserGuide's scope; the product-code *attribution* question is noted for a dedicated Marketplace Seller Guide pass.
- **Customer self-inflicted cost** (choosing a pricier AMI) — a footgun, not a boundary breach.
- **Shared EC2 billing/metering backend** — AWS-owned infra; hard stop if reached.
- **The in-doc "agent-toolkit" note** — untrusted documentation content, not a service boundary.
- **Third-party SDK / PowerShell cmdlet wrappers** — the wire API is the surface, not the client libraries.

---

## 8. Null Hypotheses / Doc Gaps
- **Lens G (SSRF) — NULL (evidence-backed).** Read `ami-billing-info`, `billing-info-fields`, `view-billing-info`, `verify-ami-charges`, `paid-amis`, `get-product-code`. No field is dereferenced/fetched/rendered server-side; the only URLs are static doc cross-links. No SSRF role present.
- **Lens Q (upload) — NULL.** No upload/logo/attachment/image field. (AMI *content* import is `ImportImage`, covered as a laundering path in Area 2, not a rich-content parser.) `RegisterImage` `ImageLocation` points to an S3 **manifest** (instance-store AMI) — that XXE/SSRF-shaped manifest-parsing surface belongs to `s3-backed-ami-plan` (RegisterImage manifest), not this billing page; noted for cross-reference.
- **Lens K (prompt injection) — NULL** for the service surface. The only injection-shaped artifact is the `See also` block in the docs, flagged at top; it targets the reading agent, not a service component.
- **Lens H (KMS as access break) / Lens J (OAuth) / Lens F (translation-layer) — NULL** on these pages. (CopyImage's `KmsKeyId` is volume encryption, unrelated to billing; route KMS-confusion questions to `ebs-storage-plan`/`copying-amis-plan`.)
- **Lens A (classic cross-tenant data IDOR) — reframed, not null.** `DescribeImages` on a *shared* AMI can expose its billing code across the sharing boundary (low sensitivity); the money-side cross-tenant risk is Area 3 (marketplace attribution), the real cross-account concern.
- **DryRun trap (Lens A variant) — recorded.** `RegisterImage`, `CopyImage`, and the CR-billing APIs all expose `DryRun`; it validates caller IAM only, before resource/disk-vs-code resolution → never use it to confirm a billing-integrity or ownership lead.
- **DOC-GAPS still open before probing (highest value):** whether `CreateImage`/`ImportImage`/`CreateRestoreImageTask` preserve or allow override of `billingProducts` (CopyImage is now known to be silent); the **strength** of the `BillingProduct.N` "must be authorized" check; product-code ownership validation at Marketplace association; whether the **launch path** validates the declared code against actual disk contents. These live in the EC2 API/IAM reference and the AWS Marketplace Seller Guide — read those, then execute Areas 1–3 first.

---

## 9. Adjacent surface (documented, DIFFERENT feature) — Capacity-Reservation billing-ownership transfer

> **Why this is here and separate.** `ami-billing-info.html` links only three topics (billing-info-fields, view-billing-info, verify-ami-charges), none of which is Capacity-Reservation billing. The CR billing-ownership-transfer feature (`assign-billing.html` tree) shares the word "billing" but is a **different EC2 feature** — reassigning who pays for a shared Capacity Reservation's *unused* capacity. It is retained here because a prior pass built a rigorous plan for it and it is one word-hop away; a hunter working "EC2 billing" should have it. **It is NOT the target page's own surface.** Live-verified 2026-09-07: `AcceptCapacityReservationBillingOwnership` still takes **only `CapacityReservationId` + `DryRun`** — no request nonce, no consumer-account param (validates AF-1/A1 below).

**Mechanism.** A CR **owner** account and a **consumer** account under the **same AWS Organizations payer**, with the CR already **shared** to the consumer. `AssociateCapacityReservationBillingOwner(cr, consumerAccountId)` sends a `pending` request (12-hour TTL, EventBridge event to the consumer). The consumer `Accept`/`Reject`s (keyed on `cr-ID` only). On `accepted`, liability for unused capacity moves owner→consumer. `Disassociate` cancels (pending) / revokes (accepted); un-share or leave-org auto-revokes. Consent gate + "shared + same-org" precondition are the entire security model. **IAM sub-analysis (from `service-authorization/list_ec2` + RAM docs):** all 4 mutating actions are resource-scoped to `capacity-reservation*` and honor `aws:ResourceTag`; **but there is NO counterparty-account condition key and NO CR resource policy** — a targeted account cannot IAM-refuse being named. So AF-1/AF-2 business-logic gates are the *only* controls, with no IAM backstop.

**Top adjacent leads (priority within this section):**
- **AF-1 (Lens P + A, HIGHEST):** `Accept`/`Reject` take only `CapacityReservationId`. **Claim A1 (accept-by-wrong-account):** a third shared account `T` (CR shared with T, request targeted at consumer `C`) calls `Accept(cr)` and becomes billing owner, or consumes C's pending request → cross-tenant authz on a financial object. **Claim P1 (post-expiry replay):** `Accept(cr)` succeeds after the 12h window (state should be `expired`). **Oracle:** billing owner flips despite wrong account / expired state. **Severity: High.** *(Do NOT use `DryRun` as the oracle — confirm via resulting `unusedReservationBillingOwnerId` / CUR.)*
- **AF-2 (Lens P + B):** precondition-bypass. **Claim P4 (out-of-org shared target):** `Associate(cr, X)` where X is RAM-shared but in a **different** payer org — RAM can share a CR with any account, but billing requires same payer; the failure mode is undocumented. **Claim P5 (unshare TOCTOU):** `Associate(cr, C)` then un-share before `Accept` — does `Accept` still attach? **Oracle:** request delivered / billing attaches to an account the same-org rule should exclude. **Severity: High (out-of-org) / Medium (TOCTOU).**
- **AF-3 (Lens A disclosure, LOW):** targeted account reads `requestedBy` + thin `capacityReservationInfo` (AZ/AZ-id/instanceType/tenancy only) from a `pending`/terminal request it never accepted (24h post-terminal window). Thin data → **Low** (Low–Medium if chained with AF-2/P4 to hit arbitrary accounts).
- **AF-4 (Lens L, MEDIUM):** owner fans out N CRs → N unsolicited `pending` requests + EventBridge events to one victim; test per-target rate limits and `Associate`/`Disassociate` churn spam.

**Adjacent null/doc-gaps:** SSRF/upload/prompt-injection/KMS/translation-layer all NULL here too (control-plane IAM API set, `cr-…`/`[0-9]{12}` inputs only). CloudTrail coverage of the 4 mutating actions is **not documented** (Lens O doc-gap) → confirm a silent settle can't occur. Doc drift: `DescribeCapacityReservationBillingRequests` links to `transfer-billing.html` while the live topic is `assign-billing.html` (Lens N — verify no legacy endpoint).

**Preconditions to exercise AF-1/AF-2:** three accounts under one Organizations payer (owner `O`, targeted consumer `C`, third shared `T`) + one account in a **different** org (`X`). Synthetic canary CRs only; tear down every CR created.

---

### Completion note (skill-agent)
- **Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`).
- **Target:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html` (+ 3 child pages, + paid-AMI/product-code supporting pages).
- **Inputs read:** offline mirror pages listed under §Source; live target + `RegisterImage`/`CopyImage`/`AcceptCapacityReservationBillingOwnership` API refs fetched 2026-09-07 (target byte-identical to mirror; API pages used to close doc-gaps).
- **Result:** research plan produced (documentation-derived hypotheses; nothing tested live). Primary surface = AMI billing-code integrity (Areas 1–5); adjacent CR billing-ownership-transfer surface documented in §9.
- **Key live findings this pass:** (1) `RegisterImage` `BillingProduct.N` requires an "authorized" account, but billing info is snapshot-metadata-derived and an absent code yields empty `PlatformDetails` with only an advisory "discard the AMI" — **doc-confirms the stripping mechanism + self-assessment gap (Area 1).** (2) Live `CopyImage` documents **nothing** about billingProducts persistence — the assumed anti-laundering control is not doc-supported (Area 2 reframed). (3) Product codes auto-copy from snapshot → foreign-code side-channel around the BillingProduct.N authz gate (Area 3b). (4) `DryRun` on all these APIs is a caller-IAM check, not an integrity/ownership oracle.
- **Could not fully test from docs (recommend follow-up):** `CreateImage`/`ImportImage`/`CreateRestoreImageTask` code-carryover; `BillingProduct.N` authz-gate strength; Marketplace product-code ownership validation; launch-path disk-vs-code validation — read the EC2 API/IAM reference and Marketplace Seller Guide before probing.
- **Injection:** `See also` AI-agent CLI suggestion noted as untrusted; **not executed.**
