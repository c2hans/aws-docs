# Aurora Performance Insights "SQL statistics" — Attack Research Plan

Source of leads: `AuroraUserGuide/sql-statistics.html` (+ engine sub-pages `USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.html` and `...PostgreSQL.html`); cross-refs `USER_DatabaseInsights.html`, `USER_PerfInsights.EnableMySQL.html`, `USER_WorkingWithParamGroups.html`. Sibling plans: RDS UserGuide `task-rds-sql-statistics`, `task-rds-perfinsights`, `task-aurora-perfinsights`, `task-rds-database-insights`, `task-aurora-perfinsights-api`. Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the shared `pi:*` fleet, a monitoring-account sink you did not create), stop, preserve evidence, flag `aws-security`.
- **This surface's authorization control is entirely the `pi:` (Performance Insights) IAM action family + optional fine-grained `pi:Dimensions` Deny. There is no per-query DB GRANT gate — anyone with `pi:GetResourceMetrics`/`pi:DescribeDimensionKeys`/`pi:GetDimensionKeyDetails` on the resource reads every query's telemetry.**

## 1. Pentest Objectives (boundary-breach goals)
1. Read another principal's / another tenant's SQL query text or per-query metrics for an Aurora cluster the caller is not authorized to inspect at the DB level.
2. Read literal-value SQL (PII in `WHERE` clauses) despite a fine-grained `pi:Dimensions` Deny that the customer copied from AWS's docs believing it hides SQL.
3. Reach the same SQL text through a *sibling* channel (CloudWatch metrics, CloudWatch Logs slow-query log, cross-account OAM sink) that the `pi:`-scoped Deny does not cover.
4. Silently suppress collection (blind an auditor) or silently widen truncation on one reader of a shared/instance parameter group.

## 2. Components, Assets, and Design

**What it is.** Per-query performance telemetry exposed through the Performance Insights API (`pi:*`, `arn:aws:pi:<region>:<acct>:metrics/rds/<dbi-resource-id>`). On **Aurora specifically**, SQL statistics are collected **digest-only on both engines**:
- Aurora MySQL: *"collect SQL statistics only at the digest level. No statistics are shown at the statement level."* Source table: `events_statements_summary_by_digest` (Performance Schema).
- Aurora PostgreSQL: *"All Aurora engines collect statistics only at the digest-level."* Source: `pg_stat_statements` (must be in `shared_preload_libraries`; default-loaded on PG10+, manual on 9.6).

Every metric on both sub-pages is namespaced `db.sql_tokenized.stats.*` — **there is no `db.sql.stats.*` (statement-level statistics) namespace on Aurora at all.**

**Assets.**
- The *digest text* dimension `db.sql_tokenized.statement` — the tokenized query pattern (`SELECT * FROM emp WHERE lname = ?`). Literals replaced by `?`. Lower sensitivity, but table/column names + query shape leak schema.
- The *live query-text* dimension `db.sql.statement` (a **DB-load / Top-SQL dimension**, NOT one of the statistics metrics on this page) — captured from `pg_stat_activity` (PG) / current-statement (MySQL). **On PostgreSQL this can contain LITERAL VALUES** because `pg_stat_activity` is not tokenized; it is capped at `track_activity_query_size` (default 4096 bytes). This is the highest-value asset and is *adjacent to* — not on — the sql-statistics page. Confirm it exists on Aurora.
- Per-query numeric metrics (rows examined/sent, temp tables, block I/O) — a covert-channel / inference asset even when text is hidden.

**Identity / access.** SigV4 IAM only. Authorization = the `pi:` action family. `pi:Dimensions` condition key attaches to exactly 3 actions: `GetResourceMetrics`, `DescribeDimensionKeys`, `GetDimensionKeyDetails`. `GetDimensionKeyDetails` returns **full untruncated** text (bypasses the ~500-byte cap on the other two). AWS-managed policies `AmazonRDSPerformanceInsightsReadOnly` and `...FullAccess` grant all three on `arn:aws:pi:*:*:metrics/rds/*` with **no Condition** (see sibling memos — CONFIRMED).

**Aurora-specific topology twist.** Parameter groups are **cluster-level + instance-level**; an instance-level PG silently overrides the cluster PG and is invisible to `DescribeDBClusterParameters` (see `task-aurora-dbinstance-paramgroups`). `performance_schema`, `track_activity_query_size`, and whether PI auto-manages Perf Schema are all PG-controlled → an attacker or a mistake on one reader instance diverges collection/truncation from the rest of the cluster.

```
caller (SigV4, pi:* ) ──► Performance Insights API ──► pi metrics store (rds/<resource-id>)
                                                          ▲   ▲
   Aurora MySQL: events_statements_summary_by_digest ─────┘   │  (digest-only)
   Aurora PostgreSQL: pg_stat_statements (digest) ────────────┘
   Aurora PostgreSQL: pg_stat_activity (LIVE text, literals) ──► db.sql.statement dimension (adjacent surface)
                                                          │
              ┌───────────────────────────────────────────┘  sibling egress (NOT pi:-gated)
              ├─► CloudWatch metrics (Database Insights Advanced)   → cloudwatch:GetMetricData
              ├─► CloudWatch Logs slow-query log /aws/rds/...        → logs:StartQuery / FilterLogEvents
              └─► OAM cross-account sink (Database Insights)         → monitoring-account reads source SQL
```

## 3. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | `pi:Dimensions` gated | Notes |
|---|---|---|---|---|---|
| `pi:GetResourceMetrics` | Non-mut | Yes | Yes | text capped ~500B; numeric metrics + `db.sql_tokenized.statement`/`db.sql.statement` as GroupBy |
| `pi:DescribeDimensionKeys` | Non-mut | Yes | Yes | text capped ~500B; enumerates top digests/statements |
| `pi:GetDimensionKeyDetails` | Non-mut | Yes | Yes | **FULL untruncated text** — the truncation-bypass path |
| `pi:ListAvailableResourceDimensions` / `...Metrics` | Non-mut | Yes | **No** | enumerates which dims/metrics a DB exposes — confirms `db.sql` presence per engine |
| `cloudwatch:GetMetricData`, `logs:StartQuery` | Non-mut | Yes | **No** (`pi:`) | sibling channels carrying same SQL data |
| `rds:DescribeDBParameters` / `...ClusterParameters` | Non-mut | No | No | source-of-value check for `performance_schema`/`track_activity_query_size` |
| `rds:ModifyDBParameterGroup`, `rds:ResetDBParameterGroup` | **Mut** | Yes | No | collection-evasion / truncation-widening knob |

## 4. Recommended Areas of Focus (firing lenses)

### Area 1 — Managed-policy unconditioned SQL-telemetry read (Lens R / S / U) — TOP, carries over CONFIRMED
Background: `AmazonRDSPerformanceInsightsReadOnly` / `...FullAccess` grant the 3 dimension actions on `arn:aws:pi:*:*:metrics/rds/*` with no Condition (sibling-CONFIRMED).
Security Concern: any holder reads every Aurora cluster's query telemetry in the account by default; fine-grained `pi:Dimensions` Deny is opt-in and absent from all baselines.
Test Scenarios:
- Under a scoped role holding **only** the managed policy, call `GetDimensionKeyDetails` for `db.sql_tokenized.statement` (and `db.sql.statement` if present) on an Aurora cluster the role has no `rds:`/DB access to → returns query text = boundary break.
- `iam:SimulatePrincipalPolicy` first (no resources touched), then live scoped call with canary DB.
Severity-if-true: intra-account over-broad read = Medium–High (AWS-authored, uneditable → reportable Tier 2).

### Area 2 — `db.sql.statement` live literal-SQL on Aurora despite tokenized-only Deny (Lens U / A / X) — TOP doc-gap
Background: This page says Aurora *statistics* are digest-only. But the DB-load **dimension** `db.sql.statement` is separate from statistics and, on PostgreSQL, is sourced from `pg_stat_activity`, which is **not tokenized** and can hold literal values up to `track_activity_query_size`.
Security Concern: A customer who copies AWS's fine-grained Deny example (which names ONLY `db.sql_tokenized.statement` — sibling-CONFIRMED) to "hide SQL" may still expose **literal** query text via `db.sql.statement` on Aurora PostgreSQL. The docs never warn, and this page's "digest-only" statement plausibly lulls the reader into thinking no literal text exists on Aurora.
Test Scenarios:
- `pi:ListAvailableResourceDimensions` on an Aurora MySQL and an Aurora PG cluster → does `db.sql.statement` (statement group) appear even though *statistics* are digest-only? (Refute/confirm the surface.)
- With a Deny on `pi:Dimensions` = `["db.sql_tokenized.statement"]` only, call `GetDimensionKeyDetails db.sql.statement` → literal SQL returned = Deny-bypass.
- Test whether `pi:Dimensions:["db.sql.statement"]` is even honored on Aurora (doc silent).
Severity-if-true: unredacted PII/SQL past a control the customer believes is complete = High.

### Area 3 — Sibling-channel SQL egress not covered by `pi:` Deny (Lens A cross-service / T / O) — carries over CONFIRMED
Background: Database Insights Advanced publishes per-query metrics to CloudWatch; slow-query log ships FULL literal SQL to CloudWatch Logs `/aws/rds/cluster/<name>/<log_type>`; OAM shares Logs+Metrics to a monitoring account "for Database Insights."
Security Concern: A `pi:Dimensions` Deny does not constrain `cloudwatch:`/`logs:`; AWS sample grants `cloudwatch:GetMetricData`/`ListMetrics` at `Resource:"*"`. OAM lets a monitoring account read source SQL without any `pi:` in the source.
Test Scenarios:
- With `pi:` fully denied but `logs:StartQuery Resource:"*"` allowed, query the Aurora slow-query log group → literal SQL = bypass.
- From an OAM monitoring account, read source Aurora SQL telemetry with no `pi:` in source.
Severity-if-true: cross-account SQL read = Critical (HARD STOP if it implicates a shared/AWS sink); intra-account channel bypass = High.

### Area 4 — Collection-evasion & truncation-widening via (instance-level) parameter group (Lens O / L / I) — Aurora twist
Background: MySQL digest table has **no eviction**; when full, "Aurora MySQL doesn't track SQL queries" — auto-truncate only fires if `performance_schema=0` AND Source≠`user`. If an operator set Source=`user`, the blind spot is permanent. PG drops collection for queries longer than `track_activity_query_size`.
Security Concern: On Aurora, an **instance-level** PG silently overrides the cluster PG and is hidden from `DescribeDBClusterParameters` (`task-aurora-dbinstance-paramgroups`). One reader instance can be pushed to Source=`user` (permanent digest blind spot) or have `track_activity_query_size` shrunk (collection drop) without cluster-level visibility; conversely widening it enlarges the literal-text exposure window. Shared PG → blast radius across every cluster using it.
Test Scenarios:
- Set `performance_schema` Source=`user` on one Aurora MySQL reader; fill the digest table; confirm queries stop being tracked and no auto-truncate occurs while the rest of the cluster still reports → audit blind spot on that instance.
- Shrink/grow `track_activity_query_size` via an instance-level PG on Aurora PG; confirm `DescribeDBClusterParameters` does not reflect it, and confirm `db.sql.statement` truncation changes on that instance only.
Severity-if-true: audit evasion = Low–Medium (High as an enabler for stopping SQL capture during an attack); shared-PG blast = Medium.

### Area 5 — Truncation is not a redaction control (Lens U) — carries over
Background: console shows 500B (Top SQL) / 4KB (SQL text); API `GetResourceMetrics`/`DescribeDimensionKeys` ≤500B; **`GetDimensionKeyDetails` = full**; PG download up to 1 MB via `track_activity_query_size`. View ≠ download.
Security Concern: Anyone treating the console's truncated view as "SQL is not fully exposed" is wrong — `GetDimensionKeyDetails` returns the full text.
Test: fetch a >500B digest via `GetDimensionKeyDetails` and confirm full return.
Severity: reinforces Area 1/2 (Informational alone).

## 5. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read literal SQL despite tokenized-only Deny | `pi:GetDimensionKeyDetails db.sql.statement` | `pi:Dimensions` fine-grained Deny (proves it names only `db.sql_tokenized.statement`) |
| Default over-broad telemetry read | Managed PI policies | "read-only" naming implies scoped; policy has no Condition |
| SQL egress via non-`pi:` channel | CloudWatch / Logs / OAM | `pi:` Deny (proves it doesn't cover siblings) |
| Silence SQL capture / widen exposure | instance-level PG override | cluster PG as assumed single control point |

## 6. Out-of-Scope
- Shared Aurora/Grover storage-plane internals; IMDS on managed hosts.
- A principal reading telemetry for DBs it *is* authorized to inspect (intended use).
- User steering their own account's telemetry.
- **REFUTED for Aurora (do not pursue as "engine differential"):** statement-level `db.sql.stats.*` literal-value *statistics*. Aurora has none — both engines digest-only. The literal-text exposure on Aurora rides the *dimension* `db.sql.statement` (Area 2), not the statistics namespace. This is the decisive Aurora-vs-RDS(Oracle/SQLServer) difference.

## 7. Null hypotheses / doc gaps
- **Lens F/G/Q/K/W/Y/BB/CC/DD/EE/FF — N/A on this page.** Checked: sql-statistics.html + both engine sub-pages. No URL/host field the service dereferences (G), no upload/parse of caller content (Q/F), no LLM (K), no attestation (W), no transport claim on this page (Y — deferred to `iamdbauth`/`ssl` memos), no multi-parser request path or cache/token layer described here (BB/CC/DD/FF), no predictable-name resolution (EE). These are pi-API-mechanics belonging to `task-aurora-perfinsights-api`.
- **doc-gap (Area 2):** whether `db.sql.statement` dimension exists on Aurora MySQL/PG and whether it carries literals is NOT stated on this page — confirm surface via `ListAvailableResourceDimensions` before ranking.
- **doc-gap:** whether `pi:Dimensions:["db.sql.statement"]` is honored on Aurora is undocumented.
