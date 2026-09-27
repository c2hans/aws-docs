# RDS Performance Insights — "SQL statistics" — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sql-statistics.html
**Source of leads:** the `sql-statistics.html` page + its four engine sub-pages (MySQL/MariaDB, Oracle, SQL Server, PostgreSQL), plus the Performance Insights (PI) access-control family (`USER_PerfInsights.access-control.*`), the SQL-text pages (`SQLTextSize`, `SQLTextLimit`, `view-download-text`, `AnalyzingSQLLevel`), CloudTrail/CloudWatch pages, and the PI API Reference (`pi:`, `PerformanceInsightsv20180227`). Offline mirror: `/work/aws-docs/docs/AmazonRDS/latest/UserGuide/`.
**Status:** documentation-derived hypotheses only. Nothing was tested against a live account. This plan is a sibling of the prior `USER_PerfInsights` and `USER_DatabaseInsights` plans — it deep-dives the *SQL-statistics* surface specifically (per-query metrics + the SQL-text dimensions they hang off).

---

## 0. How to use this document

- Each lead is written as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition**. Work in priority order (Section 5); look left/right for adjacent bugs.
- **The crown jewel here is SQL query text with literal parameter values** (`db.sql.statement`, e.g. `... WHERE lname = 'Sanchez'`), which the SQL-statistics feature exposes alongside per-query performance counters. Every lead ultimately asks: *can a principal read SQL text (or its literal-value child queries) that an access-control mechanism was meant to hide?*
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the RDS/PI fleet), stop, preserve evidence, and flag for AWS-Security disclosure. This plan otherwise stays in the customer's account and on the `pi:`/`cloudwatch:`/`logs:` HTTP application layer.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)

1. **Read full-literal SQL text** (`db.sql.statement`, statement-level) of another principal/team on a DB where an IAM control was intended to hide SQL — proving the control (a) named the wrong dimension, (b) covered the wrong action, or (c) is bypassable via a sibling action or a different service.
2. **Recover SQL text that a fine-grained `pi:Dimensions` Deny appears to hide**, via a non-denied action (`DescribeDimensionKeys`, `GetDimensionKeyDetails`) or via the console-vs-API / view-vs-download byte-limit divergence.
3. **Read SQL statistics / SQL text on a tag-scoped ("env:prod") DB** that a tag-based Deny was meant to protect — either because the Deny scoped only one action, or by self-widening the inherited tag on the parent DB.
4. **Reach SQL-derived data via a second service** (CloudWatch metrics / CloudWatch Logs slow-query) under `cloudwatch:`/`logs:` IAM that a `pi:` Deny does not touch — including cross-account via CloudWatch OAM.
5. **Evade SQL-statistics collection** (fill/poison the digest table; exceed the query-size truncation) so an attacker's own queries are never recorded — a monitoring-integrity break.
6. Confirm/refute that the PI managed policies (`AmazonRDSPerformanceInsightsReadOnly`/`FullAccess`) grant unconditioned read of the SQL-text dimensions by default.

---

## 2. Components, Assets, and Design

**What the feature is.** "SQL statistics" are per-query performance metrics ("for each second that a query is running and for each SQL call"), surfaced in the PI **Top SQL** tab and through the PI API. The feature is inseparable from the **SQL text** it labels metrics with — the page itself shows literal-value child queries (`SELECT * FROM emp WHERE lname = 'Sanchez'`).

**The two SQL identities (critical to every lead):**

| Level | Metric family | Text dimension | Content | Engines that expose it |
|---|---|---|---|---|
| **Statement** | `db.sql.stats.*` | `db.sql.statement` / `db.sql.id` / `db.sql.db_id` | **Full SQL WITH literal values** (PII: `WHERE lname='Sanchez'`) | **Oracle, SQL Server only** |
| **Digest (tokenized)** | `db.sql_tokenized.stats.*` | `db.sql_tokenized.statement` / `.id` / `.db_id` | Tokenized (`WHERE lname = ?`) | **All engines** (MySQL/MariaDB & PostgreSQL are digest-ONLY) |

- **Oracle:** statement ID = `V$SQL.SQL_ID`; digest ID = `V$SQL.FORCE_MATCHING_SIGNATURE`. Statement-level `db.sql.stats.*` present.
- **SQL Server:** statement ID = `sql_handle`; digest ID = `query_hash`. Statement-level `db.sql.stats.*` present.
- **MySQL/MariaDB:** digest-only, from `events_statements_summary_by_digest` (Performance Schema). No statement-level.
- **PostgreSQL:** digest-only, from `pg_stat_statements`. No statement-level.

**Interface / API surface.** The `pi:` API (`PerformanceInsightsv20180227`), endpoint `pi.<region>.amazonaws.com` (SigV4). SQL-statistics data is read via `GetResourceMetrics` (the `db.sql.stats.*` / `db.sql_tokenized.stats.*` metrics), `DescribeDimensionKeys` and `GetDimensionKeyDetails` (the SQL-text dimensions), and discovered via `ListAvailableResourceDimensions`. Console: RDS → Performance Insights → Top SQL.

**Resource / identifier shape.** PI metrics ARN: `arn:aws:pi:<region>:<acct>:metrics/rds/db-<DbiResourceId>` where `db-ABC1DEFGHIJKL2MNOPQRSTUV3W` is the immutable, high-entropy (~26-char) DbiResourceId (not enumerable). Tags are **inherited from the parent DB instance** (see §5-F).

**Identity / roles.** SigV4 IAM. Access is shaped by: managed policies (`AmazonRDSPerformanceInsightsReadOnly`, `AmazonRDSPerformanceInsightsFullAccess`), the `pi:Dimensions` fine-grained condition key (only 3 actions), `aws:ResourceTag` tag-based policies, and CMK key policy for encrypted data.

**Untrusted-data seam.** The SQL text is *customer-database content* flowing outward into a metrics/observability plane; the security question is not injection *into* the DB but **who downstream can read the exfiltrated text**, and whether it lands in a second service under weaker IAM.

**Byte-limit / truncation surface (a feature that doubles as a redaction assumption):**
- Console **Top SQL** row: 500 bytes; **SQL text** section: up to 4 KB (console-imposed).
- **Download**: up to the DB-engine limit — MySQL/MariaDB 4,096 B (PS on) / 65,535 B (PS off); SQL Server 4,096 chars; Oracle 1,000 B; **PostgreSQL up to 1 MB** (`track_activity_query_size`, max 1 MB on v13+).
- **API**: `DescribeDimensionKeys` and `GetResourceMetrics` return **at most 500 bytes**; **`GetDimensionKeyDetails` returns the full query** (subject to engine limit).
- PostgreSQL: "console displays only the first 4 KB; if you download the query you get the full 1 MB … viewing and downloading return different numbers of bytes."
- PostgreSQL also *drops* collection for queries longer than `track_activity_query_size` (default 1,024 B on v9.6, 4,096 B on v10+): "Performance Insights can only collect statistics for queries in `pg_stat_activity` that aren't truncated."

```
                       ┌─────────────────── customer account ───────────────────┐
 customer principals   │                                                          │
 (IAM, various teams)  │   RDS DB instance (Oracle/SQLServer/MySQL/PG)            │
        │              │      │  Performance Schema / pg_stat_statements /         │
        │  pi: SigV4   │      │  V$SQL — SQL text + literal child queries          │
        ▼              │      ▼                                                    │
  ┌──────────────┐     │   Performance Insights collector ──► PI store (7d free / │
  │ pi: API      │◄────┼───  db.sql.stats.* (Oracle/MSSQL: FULL text)             │
  │ GetResource  │     │      db.sql_tokenized.stats.* (all engines)              │
  │ DescribeDim  │     │            │                                             │
  │ GetDimKeyDet │     │            ├──(Advanced mode)──► CloudWatch metrics  ◄── cloudwatch: IAM
  │ ListAvailDim │     │            └──(SlowSQL)────────► CloudWatch Logs     ◄── logs: IAM
  └──────────────┘     │                                        │                 │
    ▲ pi:Dimensions     │                                       └── OAM ──► monitoring ACCOUNT (cross-acct)
    │ (only 3 actions)  └──────────────────────────────────────────────────────────┘
    │
  aws:ResourceTag (inherited from parent DB) — tag-based Deny
```

---

## 3. API / Interface Inventory (SQL-statistics-relevant `pi:` actions)

| Name | Mutating | Facing | Returns SQL text? | `pi:Dimensions`-scopable? | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `GetResourceMetrics` | No | External | Yes — as dimension in `db.load` breakdown; **≤500 B** | **Yes** | any principal w/ pi: on the metrics ARN | The `db.sql.stats.*`/`db.sql_tokenized.stats.*` metrics are read here. |
| `DescribeDimensionKeys` | No | External | Yes — SQL-text dimension keys; **≤500 B** | **Yes** | same | Doc's own O01 example shows text still readable here when Deny scoped only to GetResourceMetrics. |
| `GetDimensionKeyDetails` | No | External | **Yes — FULL query** (engine-limited, bypasses 500 B) | **Yes** | same | The un-truncated leak path. |
| `ListAvailableResourceDimensions` | No | External | No (lists which dims are *authorized*) | No (but `AuthorizedActions` param reveals the intersection) | same | Recon oracle: shows which SQL-text dimension is still reachable after a Deny. |
| `ListTagsForResource` | No | External | No | No | same | Returns parent-DB tags on a metrics ARN. |
| `TagResource`/`UntagResource` | Yes | External | No | No | same | **Error** on PI metrics (tags inherited) — see §5-F. |
| `GetResourceMetadata` | No | External | No | No | same | Feature-flag fingerprint (e.g. digest-stats enabled). |

> **Undocumented-knob sweep:** the `Identifier` in request bodies is a `db-...` id validated loosely by the API regex; the SQL-text dimensions are addressed only by dimension string in `pi:Dimensions`. Confirm live whether `pi:Dimensions` accepts the **statement-level** string `db.sql.statement` as a Deny value at all (if the console/docs only ever show `db.sql_tokenized.statement`, the operator may not know the other string exists → §5-A).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv team principal | Another team's SQL text on a shared-account DB | `pi:` read on the metrics ARN | Reading `db.sql.statement` literal text the principal's `pi:Dimensions`/tag Deny was meant to hide = **intra-account confidentiality break** |
| Principal under a `db.sql_tokenized.statement` Deny (Oracle/MSSQL DB) | The **statement-level** `db.sql.statement` (literal values) | The Deny names only the tokenized dimension | Full-literal SQL returned = the more-sensitive text was never covered |
| Principal under a Deny scoped to `GetResourceMetrics` | Same SQL text via `DescribeDimensionKeys`/`GetDimensionKeyDetails` | Sibling action not covered by the Deny | Text returned by the sibling where GetResourceMetrics is denied |
| Principal denied `pi:` on prod DB (via `aws:ResourceTag/env=prod`) | SQL text via a non-denied `pi:` action, or after stripping the tag | Deny scoped to one action; tag mutable on parent DB | Text returned; or `env:prod` removed via `rds:RemoveTagsFromResource` then read |
| Principal denied `pi:` entirely | SQL-derived data in CloudWatch metrics / Logs | Advanced-mode publish / SlowSQL, governed by `cloudwatch:`/`logs:` | `cloudwatch:GetMetricData` / `logs:GetLogEvents` returns SQL-derived data the `pi:` Deny cannot see |
| Monitoring-account principal | Source-account SQL data | CloudWatch OAM sink/link | Cross-account read of SQL-derived CloudWatch data |
| Attacker running queries on the DB | The SQL-statistics record of their own queries | Digest-table fill / query-size truncation | Attacker's queries absent from Top SQL = monitoring evasion |
| **Any customer principal** | **AWS PI/RDS service plane** | — | **Any AWS-owned identity/ARN/credential = HARD STOP, disclose** |

---

## 5. Recommended Areas of Focus (one block per firing lens)

### A. Doc-steered fine-grained Deny names the wrong SQL dimension — statement-level literal SQL left readable *(Lens S / U / X — TOP LEAD)*

**Background.** Fine-grained access (`USER_PerfInsights.access-control.dimensionAccess-policy`) lets a customer Deny individual dimensions on `GetResourceMetrics`/`DescribeDimensionKeys`/`GetDimensionKeyDetails`. Every SQL-text Deny example AWS prints names **only `db.sql_tokenized.statement`** (the tokenized form). But `sql-statistics` establishes that **Oracle and SQL Server also expose statement-level `db.sql.statement`** — the *more* sensitive form, carrying literal values (`WHERE lname='Sanchez'`, i.e. actual PII).

**Security Concern.** A customer following AWS's documented pattern to "hide SQL from PI viewers" denies `db.sql_tokenized.statement` and believes SQL is hidden. On an **Oracle or SQL Server** instance, the statement-level `db.sql.statement` dimension is *not* denied, so the reader still gets full literal SQL. The doc never warns that a second, higher-sensitivity dimension string exists. This is an AWS-authored footgun (a copy-verbatim example), engine-conditioned.

**High-level Test Scenarios (falsifiable claims):**
- *Claim:* On an Oracle/SQL Server DB, a `pi:Dimensions` Deny listing `db.sql_tokenized.statement` does **not** block `DescribeDimensionKeys`/`GetDimensionKeyDetails` from returning `db.sql.statement` full-literal text. → **Oracle:** issue those calls requesting the `db.sql` group under the Deny; text with literal values returned = confirmed.
- *Claim:* `pi:Dimensions` *can* name `db.sql.statement` — i.e. the gap is closeable but undocumented, so operators don't. → confirm the dimension string is accepted in a Deny.
- *Claim:* `ListAvailableResourceDimensions` with `AuthorizedActions` reveals `db.sql` still authorized after the tokenized-only Deny (recon oracle pointing straight at the gap).

**Doc evidence.** `sql-statistics.md` literal child queries; Oracle/SQLServer sub-pages `db.sql.stats.*` (statement-level); `dimensionAccess-policy.md` examples name only `db.sql_tokenized.statement`; `DimensionGroup` API reference for valid strings.
**Severity-if-true.** Medium–High (intra-account confidentiality of PII-bearing SQL; AWS-authored copy-verbatim example → reportable, not a customer footgun). **Stop:** once literal text is read under the Deny for one query.

### B. Multi-path leak — SQL text recoverable via an action the Deny didn't scope *(Lens X / U — HIGH)*

**Background.** `pi:Dimensions` attaches to exactly three actions. AWS's own O01 example (`dimensionAccess-policy`) denies `db.sql_tokenized.statement` **only for `pi:GetResourceMetrics`**, and the doc *annotates* that the same text is "**allowed for DescribeDimensionKeys because our IAM Policy denies it only for GetResourceMetrics**."

**Security Concern.** A customer copying the O01 example (or any single-action scoping) leaves SQL text readable through `DescribeDimensionKeys` and, fully un-truncated, through `GetDimensionKeyDetails`. The 500-byte truncation on GetResourceMetrics/DescribeDimensionKeys is **not** a redaction control — `GetDimensionKeyDetails` "returns the full query."

**High-level Test Scenarios:**
- *Claim:* With a Deny on `db.sql_tokenized.statement` scoped to `GetResourceMetrics`, `DescribeDimensionKeys` still returns the (truncated) text and `GetDimensionKeyDetails` returns the **full** text. → call all three, diff outputs.
- *Claim:* The 500-byte API cap is bypassed by `GetDimensionKeyDetails` (full engine-limit text) → confirm a >500-byte query returns full text.

**Doc evidence.** `dimensionAccess-policy.md` O01 annotations; `SQLTextSize.md` ("`DescribeDimensionKeys` and `GetResourceMetrics` return at most 500 bytes"; "`GetDimensionKeyDetails` returns the full query").
**Severity-if-true.** High (documented, AWS-annotated leak path). **Stop:** full text recovered via the un-denied sibling.

### C. Console-vs-API and view-vs-download byte-limit divergence defeats a truncation-based redaction assumption *(Lens U)*

**Background.** The console shows 500 B (Top SQL) / 4 KB (SQL text). Download returns up to the **engine limit** — for PostgreSQL up to **1 MB** (`track_activity_query_size`). The doc states plainly for PostgreSQL: "the console displays only the first 4 KB. If you download the query, you get the full 1 MB … viewing and downloading return different numbers of bytes."

**Security Concern.** Any control or operator assumption that "PI only shows a truncated snippet, so long-tail PII in a large query is safe" is false: **Download / `GetDimensionKeyDetails`** return the full text (up to 1 MB on PostgreSQL). A reviewer who audited only the console view under-estimates exposure; a data-classification control keyed on the 500 B/4 KB view misses the rest.

**High-level Test Scenarios:**
- *Claim:* A PostgreSQL query >4 KB (with `track_activity_query_size` raised toward 1 MB) is truncated in console but fully returned on Download/API — the extra bytes contain literal values not visible in the console.
- *Claim:* Raising `track_activity_query_size` (a DB-parameter-group change) *widens* how much literal SQL PI captures and exports — a parameter-group principal indirectly widens the PI exposure surface (chain to parameter-group blast radius from the prior EnableMySQL/paramgroups work).

**Doc evidence.** `SQLTextSize.md`, `SQLTextLimit.md`, `view-download-text.md`.
**Severity-if-true.** Low–Medium (redaction-assumption gap; AWS-owned doc/behavior). **Stop:** demonstrate view ≠ download bytes for one query.

### D. SQL-derived data reachable via CloudWatch / CloudWatch Logs under different IAM *(Lens T / A — HIGH; SUBAGENT-CONFIRMED BELOW)*

**Background.** Database Insights Advanced mode publishes PI data to CloudWatch; a SlowSQL feature may publish full SQL to CloudWatch Logs. These are governed by `cloudwatch:`/`logs:` IAM, and reachable cross-account via CloudWatch OAM — none of which a `pi:Dimensions` or `pi:`-scoped Deny touches.

**Security Concern.** A principal denied `pi:` entirely (or denied the SQL dimension) may still read SQL-derived statistics/text via `cloudwatch:GetMetricData`/`logs:GetLogEvents`, and a monitoring account may read it cross-account via OAM — bypassing the entire `pi:` access-control model.

**High-level Test Scenarios (refine with §"Subagent B findings"):**
- *Claim:* Advanced mode exposes per-SQL metrics with SQL id/text as a CloudWatch metric **dimension** readable under `cloudwatch:` IAM.
- *Claim:* SlowSQL writes full (literal) SQL to a CloudWatch Logs group readable under `logs:` IAM.
- *Claim:* OAM lets a monitoring account read source-account SQL-derived CloudWatch data.

**Doc evidence.** `USER_DatabaseInsights.TurningOnAdvanced.md`, `USER_DatabaseInsights.SlowSQL.md`, `USER_PerfInsights.Cloudwatch.md` (see Subagent B section).
**Severity-if-true.** High (cross-service / cross-account SQL leak bypassing `pi:` controls). **Stop:** SQL-derived data read under `cloudwatch:`/`logs:` while `pi:` is denied.

### E. SQL-statistics collection evasion — digest-table fill & query-size truncation *(Lens O / L)*

**Background.** MySQL/MariaDB collect digest stats from `events_statements_summary_by_digest`, which **"doesn't have an eviction policy."** When full, "MariaDB and MySQL don't track SQL queries." PI auto-truncates the table **only** when it manages Performance Schema automatically (`performance_schema=0` **and** Source ≠ `user`). PostgreSQL drops collection for queries longer than `track_activity_query_size`.

**Security Concern.** An attacker who (a) floods the instance with many distinct query digests to fill the digest table, or (b) pads a malicious query beyond `track_activity_query_size`, can make their queries **absent from SQL statistics / Top SQL** — a monitoring-integrity break that hides malicious DB activity from the very tool used to detect it. If the customer set `performance_schema` manually (`Source=user`), PI will **not** auto-truncate → a persistent blind spot (ties to the shared-param-group blast-radius finding in the prior EnableMySQL work).

**High-level Test Scenarios:**
- *Claim:* Filling `events_statements_summary_by_digest` halts SQL-stat collection for subsequent queries on that instance; with `Source=user` the table is never auto-truncated → durable evasion.
- *Claim:* A query longer than `track_activity_query_size` (PostgreSQL) is not collected by PI (`pg_stat_activity` truncation) → the attacker's large query never appears.

**Doc evidence.** `AdditionalMetrics.MySQL.md` (no eviction; auto-truncate conditions), `AdditionalMetrics.PostgreSQL.md` (truncation note), `SQLTextLimit.md`.
**Severity-if-true.** Medium (single-instance monitoring evasion; Low if not cross-tenant). **Stop:** demonstrate a query absent from Top SQL after the fill/pad.

### F. Tag-based Deny scoped to one action + self-widen via inherited parent-DB tag *(Lens I / S / X)*

**Background.** `USER_PerfInsights.access-control.tag-based-policy` shows a Deny of **`pi:GetResourceMetrics`** for DBs tagged `env:prod`, using `aws:ResourceTag/env` **inherited from the parent DB instance**. `TagResource`/`UntagResource` error on PI metrics; tags are mutated on the parent DB.

**Security Concern.** Two gaps: (1) the printed Deny scopes only `pi:GetResourceMetrics` — `DescribeDimensionKeys`/`GetDimensionKeyDetails` (which return SQL text) remain allowed on the same prod DB; (2) a principal with `rds:RemoveTagsFromResource`/`AddTagsToResource` on the parent DB can strip `env:prod`, defeating the Deny (self-widen), and tag-propagation timing may fail-open.

**High-level Test Scenarios:**
- *Claim:* The tag-based Deny (as printed) does not stop `GetDimensionKeyDetails` from returning SQL text on an `env:prod` DB.
- *Claim:* Removing `env:prod` from the parent DB (via `rds:` tag APIs) then calling `pi:GetResourceMetrics` succeeds — the Deny is defeated by a principal who can tag the DB.

**Doc evidence.** `tag-based-policy.md` (single-action Deny, inheritance, TagResource error).
**Severity-if-true.** Medium–High where tags are the access-control mechanism. **Stop:** SQL data read on a supposedly-protected tagged DB.

### G. Managed-policy default breadth — ReadOnly/FullAccess grant unconditioned SQL-text read *(Lens R — SUBAGENT-CONFIRMED BELOW)*

**Background.** `AmazonRDSPerformanceInsightsReadOnly`/`FullAccess` grant the three dimension actions. If they grant them on `*` with **no** `pi:Dimensions` condition, any holder reads full `db.sql.statement` by default.

**Security Concern.** The default posture for a broad "read-only PI" grant may include full literal-SQL read across all account DBs — a least-privilege gap in an AWS-authored, uneditable managed policy (Lens R, reportable).

**High-level Test Scenarios.** *Claim:* a principal holding only `AmazonRDSPerformanceInsightsReadOnly` can call `GetDimensionKeyDetails` for `db.sql.statement` on any account DB. → prove under a scoped role holding exactly that policy (`iam:SimulatePrincipalPolicy` first).
**Doc evidence.** `access-control.managed-policy.md`, `FullAccess-managed-policy.md` (+ live `GetPolicyVersion`). See Subagent A section.
**Severity-if-true.** Medium (intra-account over-broad default; AWS-owned artifact). **Stop:** simulate/confirm the grant.

### H. Audit-visibility of the SQL-text read itself *(Lens O — Low)*

**Background.** CloudTrail logs PI calls (`GetResourceMetrics`, `DescribeDimensionKeys`, etc.) with `requestParameters` but `responseElements: null` — the *content* read (the SQL text) is not in the trail.
**Security Concern.** An investigator sees that `GetDimensionKeyDetails` was called but not *which* SQL text was exfiltrated; combined with §B/§F this weakens forensic attribution of a SQL-text exfiltration.
**Doc evidence.** `USER_PerfInsights.CloudTrail.md` (example entry, `responseElements: null`).
**Severity-if-true.** Low/Informational (enabler). **Stop:** confirm response content absent from the trail.

### I. CMK / encryption-context on SQL-statistics data *(Lens H — Medium, carried from prior PI work)*

**Background/Concern.** PI SQL data encrypted under a CMK with encryption context `aws:rds:db-id`=DbiResourceId, `service`=pi, `kms:ViaService: rds.<region>`. Reader needs `kms:Decrypt`+`GenerateDataKey`. Ask: is a cross-account/disabled key rejected; can encryption context be manipulated so one DB's SQL decrypts under another's key; does `kms:ViaService` bind the app role.
**Doc evidence.** `USER_PerfInsights.access-control.cmk-policy.md`.
**Severity-if-true.** Medium. **Stop:** decrypt under wrong resource's key.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Read literal SQL under a tokenized-only Deny | `pi:Dimensions` + Oracle/MSSQL `db.sql.statement` | fine-grained dimension Deny (names only `db.sql_tokenized.statement`) |
| Recover SQL via un-scoped sibling action | `DescribeDimensionKeys`/`GetDimensionKeyDetails` | per-action `pi:Dimensions` scoping (doc shows single-action example) |
| Full text past the 500 B/console cap | `GetDimensionKeyDetails` / Download | 500 B API cap / 4 KB console cap (not a redaction control) |
| SQL data via CloudWatch/Logs under other IAM | Advanced mode / SlowSQL / OAM | `pi:` access-control model (does not cover cloudwatch:/logs:) |
| Hide own queries from Top SQL | digest table / `track_activity_query_size` | PI collection (no eviction; truncation drops collection) |
| Read prod SQL despite `env:prod` Deny | `aws:ResourceTag` (inherited) | single-action tag Deny + mutable parent-DB tag |
| Over-broad default SQL-text read | `AmazonRDSPerformanceInsights*` managed policies | managed-policy scoping |

---

## 7. Out-of-Scope Risk Categories

- Shared RDS/Aurora/Grover storage infrastructure and the PI collector fleet (AWS-owned; any AWS service-plane credential = HARD STOP + disclose).
- IMDS on the managed DB host; DB-engine internals (`pg_stat_statements`, Performance Schema) as products.
- A customer inflicting a least-privilege footgun in a policy **they authored** (in-scope only for AWS-authored managed/sample policies — §A/§B/§G).
- Single-tenant self-DoS that does not cross a tenant boundary (the digest-table fill is scoped to the attacker's own instance → Medium-at-most monitoring evasion, not cross-tenant DoS).
- SQL injection *into* the customer DB (a customer-app concern, not a PI-boundary concern).

## 8. Null hypotheses / doc gaps (pages checked)

- **Cross-account IDOR on the PI metrics ARN (Lens A direct):** *null* — the ARN embeds the high-entropy immutable DbiResourceId (`db-ABC1DEFGHIJKL2MNOPQRSTUV3W`), not enumerable; pages checked: `dimensionAccess-policy.md`, `USER_PerfInsights.API.md`. The realistic cross-boundary reads are intra-account (§A/§B/§F) and cross-service/cross-account-via-OAM (§D).
- **SSRF / server-side fetch (Lens G):** *N/A* — pages checked: all four sql-statistics sub-pages, `SQLTextSize`, `view-download-text`, `AnalyzingSQLLevel`; no field the service dereferences (download is a client-side action).
- **Injection / prompt (Lens F/K):** *N/A* — SQL text flows *out* to metrics; no translation layer or LLM on this surface.
- **Doc-gaps to confirm live (marked in leads):** (1) whether `pi:Dimensions` accepts `db.sql.statement` as a Deny value; (2) whether managed policies grant the 3 dimension actions unconditioned; (3) whether Advanced mode surfaces SQL id/text as a CloudWatch dimension and SlowSQL writes literal SQL to Logs; (4) whether `GetDimensionKeyDetails` is fully coverable by `pi:Dimensions` (if not, it is a permanent leak of full text). These are resolved by the two subagent sections below.

---

## Subagent A findings — pi:Dimensions coverage of SQL-text dimensions (CONFIRMED against live docs)

Cross-checked live vs. offline mirror (1:1, no staleness). Files: `performance-insights/latest/APIReference/API_DimensionGroup.md`, `API_GetDimensionKeyDetails.md`, `API_ListAvailableResourceDimensions.md`; `service-authorization/latest/reference/list_pi.md`; `aws-managed-policy/latest/reference/AmazonRDSPerformanceInsights{ReadOnly,FullAccess}.md`.

1. **`db.sql` and `db.sql_tokenized` are two distinct dimension groups.** `API_DimensionGroup` normative enum: group `db.sql` = "The text of the SQL statement that is currently running (all engines except DocumentDB)" with identifiers `db.sql.id`, `db.sql.db_id`, **`db.sql.statement`** ("The full text of the SQL statement that is running, as in `SELECT * FROM employees`"), and `db.sql.tokenized_id`; group `db.sql_tokenized` with `db.sql_tokenized.id/.db_id/.statement` ("as in `... WHERE employee_id = ?`"). → `db.sql.statement` and `db.sql_tokenized.statement` are **different strings** under `StringEquals`; a Deny naming one does not cover the other. **CONFIRMS §A.**
   - *Bonus footgun:* the `API_DimensionGroup` intro paragraph is internally inconsistent — it lists `db.sql.id`, `db.sql.db_id`, `db.sql.statement` **and** `db.sql_tokenized.id` as if all under one "`db.sql`" group. An operator reading the prose (not the normative enum) may believe denying "the db.sql dimension group" covers the tokenized statement too (or vice-versa). AWS doc-authoring error that reinforces the mis-scoping. (Lens U.)
2. **`pi:Dimensions` supports exactly 3 actions** (`list_pi`): `GetResourceMetrics`, `DescribeDimensionKeys`, `GetDimensionKeyDetails`. All other `pi:` actions carry only `aws:ResourceTag/RequestTag/TagKeys`. Confirms §B/§F.
3. **`db.sql.statement` as a Deny value = doc-gap (confirm live).** Every Allow/Deny example in `dimensionAccess-policy` uses only `db.sql_tokenized.*`/`db.application.name`. AWS **never demonstrates** denying `db.sql.statement`, though it is a valid `DimensionGroup` identifier usable in the same array syntax. → An admin has no worked example teaching them to close the statement-level gap. **Confirm live that `pi:Dimensions:["db.sql.statement"]` actually matches/enforces** (top open verification for §A).
4. **`GetDimensionKeyDetails` returns full text**, bypassing the 500 B cap on the other two (`API_GetDimensionKeyDetails`: exists precisely because the others "don't support retrieval of large SQL statement text, lock snapshots, and execution plans"). It is itself dimension-scopable — but if a Deny omits it, full literal SQL leaks. Confirms §B/§C.
5. **Managed policies grant all 3 dimension actions on `arn:aws:pi:*:*:metrics/rds/*` with NO `Condition` block** (read from the actual JSON). `AmazonRDSPerformanceInsightsReadOnly` and `FullAccess` both let any holder call `GetDimensionKeyDetails` for `db.sql.statement` on **every** RDS instance in the account — full untruncated literal SQL, no dimension restriction. Fine-grained Deny is opt-in and absent from every AWS baseline. **CONFIRMS §G (now confirmed, not hypothesis).**
6. **`ListAvailableResourceDimensions` + `AuthorizedActions` is a documented recon primitive**: per-action, it returns the intersection of authorized dimensions — an attacker/auditor enumerates exactly which SQL-text dimension (`db.sql.statement` vs `db.sql_tokenized.statement`) remains reachable after a Deny, pointing straight at the gap. Confirms §A oracle.

## Subagent B findings — cross-service SQL-stat leak (CloudWatch / SlowSQL / OAM) (CONFIRMED)

Decisive page (not in original list): `AmazonCloudWatch/latest/monitoring/Database-Insights-Get-Started.md` ("Required permissions for Database Insights"). Also `Database-Insights.md`, `Database-Insights-Cross-Account-Cross-Region.md`, `Database-Insights-Database-Instance-Dashboard.md`, `Database-Insights-Fleet-Health-Dashboard.md`; RDS `USER_PerfInsights.Cloudwatch.md`, `USER_DatabaseInsights.SlowSQL.md`, `USER_LogAccess.Procedural.UploadtoCloudWatch.md`.

1. **Advanced mode publishes per-query + per-database counter metrics to CloudWatch** (`USER_PerfInsights.Cloudwatch`: "RDS publishes detailed per-query and database counter metrics to Amazon CloudWatch"). The IAM boundary is the finding: Database Insights **requires you to also attach** `cloudwatch:GetMetricData/ListMetrics/GetMetricStatistics`, and AWS's own sample full-access policy grants these with **`"Resource": "*"`**, while the `pi:*` block is scoped to `arn:aws:pi:*:*:*/rds/*`. → A `pi:Dimensions` Deny on `db.sql.statement` constrains only the 3 `pi:` actions, **not** `cloudwatch:GetMetricData`. **Doc-gap:** the exact CloudWatch namespace/dimension key carrying the SQL id/text is not stated — **confirm live** (`cloudwatch:ListMetrics` on an Advanced-mode instance). **Strengthens §D.**
2. **SlowSQL exports full literal SQL to CloudWatch Logs.** SlowSQL uses the engines' native slow-query logs (`log_min_duration_statement`, `slow_query_log`) → streamed to log group `/aws/rds/instance/{name}/{log_type}`. The instance dashboard warns: **"Slow queries may contain sensitive data. Mask your sensitive data with CloudWatch Logs"** — i.e. literal, non-tokenized SQL with parameter values lands there. Read via `logs:StartQuery`/`GetQueryResults` (granted `Resource:"*"` in the sample). Independent of any `pi:` Deny. **Confirms §D.**
3. **OAM cross-account read confirmed.** `Database-Insights-Cross-Account-Cross-Region`: the sink/link shares "Logs, Metrics, Traces" and a dedicated **"Include read-only access for Database Insights"** toggle. A monitoring-account principal reads source-account SQL-derived telemetry (metrics + slow-query logs) **without holding any `pi:` permission in the source account** — OAM operates at the CloudWatch/Logs layer. **Confirms §D cross-account arm.**
4. **Retention 1–24 months (Advanced).** Per-query metrics persist up to 24 months in CloudWatch (`Database-Insights.md`), reachable under `cloudwatch:` — far beyond PI's 7-day free `pi:` retention. A longer, differently-gated exposure window. New: strengthens §D severity.
5. **Fleet aggregation (inference — confirm live).** The Fleet Health Dashboard surfaces "top queries" across a fleet of hundreds of instances through the `cloudwatch:`-gated dashboard (Resource `*` in the sample), not per-instance `pi:` ARNs. A principal scoped/denied at one instance's `pi:` ARN may see that instance's SQL data via the fleet-wide `cloudwatch:` grant. **Not stated verbatim by AWS — documented-permission-shape inference; confirm live.** New sub-lead under §D (Lens U/A isolation-shape).

---

## Post-subagent priority summary (for the hunter)

1. **§A + §G (confirmed doc facts, live-verify the exploit):** managed ReadOnly/FullAccess = unconditioned full-`db.sql.statement` read on all account DBs; and even a diligent admin who copies AWS's fine-grained Deny examples denies only `db.sql_tokenized.statement`, leaving Oracle/SQL-Server statement-level literal SQL open. **First live test:** under a role holding only `AmazonRDSPerformanceInsightsReadOnly` + a Deny on `pi:Dimensions:["db.sql_tokenized.statement"]`, call `GetDimensionKeyDetails` for `db.sql.statement` on an Oracle instance → expect full literal SQL. Also test whether `pi:Dimensions:["db.sql.statement"]` is even honored (Subagent A Q3 gap).
2. **§D (confirmed cross-service, live-verify namespace/dimension):** deny all `pi:`, then read SQL-derived data via `cloudwatch:GetMetricData`/`ListMetrics` and `logs:StartQuery` on the RDS log group; then via OAM from a monitoring account.
3. **§B (confirmed leak path):** single-action Deny → recover via the sibling action / `GetDimensionKeyDetails`.
4. **§F, §C, §E, §I, §H** as time allows.
