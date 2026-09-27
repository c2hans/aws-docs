# Amazon RDS / CloudWatch Database Insights — Attack & Research Plan

> **Target:** https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html
> **Method:** Documentation-only boundary-first analysis (security-questionbuilder skill). No live AWS calls were made. Every lead below is a *falsifiable hypothesis* with a doc citation and an oracle a hunter executes later.
> **Analysis fan-out:** main agent (ground truth on the RDS/PI doc family) + subagent A (cross-account observability + CloudWatch Logs reachability) + subagent B (IAM condition-key & KMS encryption-context semantics, managed-policy JSON).
> **Sources:** local mirror under `/work/aws-docs/docs/AmazonRDS/latest/UserGuide/USER_PerfInsights.*` **and** the online docs.aws.amazon.com equivalents + the Performance Insights API Reference + the `pi` Service Authorization Reference (`list_pi.html`) + the two AWS-managed policy JSONs. Where `.html` was SPA-rendered, `.md` mirrors were used and cross-checked online.

---

## 0. How to use this document

This is a research plan, not a findings report. Work the leads in **Section 5** in the order given (they are pre-ranked by severity × novelty). Each lead is written as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity**. A "confirmed" lead means the oracle fired against a live account you are authorized to test, using **synthetic/canary SQL** only (never real query text). The unifying thesis is in Section 1 — read it first, because 6 of the 9 top leads are variations of the same structural gap.

**The one-sentence thesis:** *Database Insights presents "sensitive data" (SQL text, DB user, application, host) as gated by a single fine-grained control — the `pi:Dimensions` IAM condition key — but that key is only wired to three `pi:` actions, and the same SQL text is reachable through at least five sibling paths (two other `pi:` actions, a CloudWatch metric path, a CloudWatch Logs path, and a cross-account observability path) that the `pi:Dimensions` deny never touches.*

---

## 1. Pentest objectives (what "broken" means here)

Database Insights is a **thin RDS-console wrapper over Amazon Performance Insights (PI)** — the `pi:` API family, service model `PerformanceInsightsv20180227` — plus CloudWatch metrics and (in Advanced mode / slow-query features) CloudWatch Logs. The RDS `USER_DatabaseInsights.html` page itself is almost entirely navigation; the real security surface lives in the `USER_PerfInsights.access-control.*` family and the PI API reference.

**Crown jewel:** the **sensitive-data dimensions** — `db.sql.statement` and `db.sql_tokenized.statement` (raw / digest SQL text), plus `db.user`, `db.application`, `db.host`. The docs (`cmk-policy`) explicitly enumerate these as "sensitive data." SQL text can embed table/column names, business logic, and — in the literal (`db.sql.statement`) form and in slow-query logs — **literal parameter values including secrets/passwords**.

**Primary objectives, phrased as breaches:**
1. **Read another tenant's / another account's sensitive SQL text.** (cross-account = Critical; intra-account bypass of a customer's own deny = High.)
2. **Bypass a customer's fine-grained `pi:Dimensions` "hide SQL" policy** via any sibling path that the deny does not gate. (High–Critical — this is the central theme.)
3. **Self-widen access** by mutating the ABAC input (DB-instance tags) that a `pi:` deny relies on. (High.)
4. **Decrypt sensitive PI data outside the intended per-database KMS scope.** (High.)
5. **Any identity/credential/ARN belonging to AWS's own PI/RDS/CloudWatch fleet** reached from a customer surface = hard-stop breach; preserve evidence, flag for disclosure, do not proceed.

---

## 2. Components, assets, and design

### 2.1 Mechanism (not marketing)

- **Customer-facing interfaces:**
  - RDS console "Database Insights" dashboard (Standard and Advanced modes).
  - The **`pi:` API** (`PerformanceInsightsv20180227`), SigV4 IAM-authenticated. This is the real data-access surface.
  - **CloudWatch** (`cloudwatch:GetMetricData`/`GetMetricStatistics`/`ListMetrics`) — Database Insights publishes metrics into the `AWS/RDS` and `DB_PERF_INSIGHTS`-style namespaces.
  - **CloudWatch Logs** (`logs:GetLogEvents`/`FilterLogEvents`) — slow-query and engine logs under `/aws/rds/instance/<name>/<log_type>`.
  - **CloudWatch cross-account observability (OAM)** and the legacy `CloudWatch-CrossAccountSharingRole` — a monitoring account can view a source account's Database Insights.

- **Backing service split:** the customer never talks to PI's fleet directly for data; PI stores sensitive dimensions encrypted under a KMS key and vends them through the `pi:` API using the *caller's* credentials + a KMS decrypt check. A Database Insights **agent** runs on the DB host (limited CPU/memory) collecting per-query metrics (`USER_PerfInsights.Enabling`).

- **Resource & identifier shape:**
  - PI metric resource ARN: `arn:aws:pi:<region>:<account>:metrics/rds/<DbiResourceId>` where `<DbiResourceId>` is the **immutable 26-char high-entropy** DB resource id (`db-ABC1DEFGHIJKL2MNOPQRSTUV3W`) — **not** trivially enumerable.
  - Performance analysis report id: `report-[0-9a-f]{17}` (17 hex chars ≈ 68 bits — also not trivially enumerable, but far shorter than the DbiResourceId).
  - Perf-report resource ARN under `arn:aws:pi:*:*:perf-reports/rds/*`.

- **Identity:** SigV4 IAM. Fine-grained data control via the **`pi:Dimensions`** condition key (`ArrayOfString`). KMS decrypt gated by the CMK key policy + encryption context.

- **Untrusted-data entry → transform:** customer SQL executed against the DB → agent tokenizes/captures → stored as PI dimensions (both raw and tokenized) and, for slow queries, written **verbatim** to CloudWatch Logs. Every "read sensitive dimension" API is a controlled-disclosure seam.

### 2.2 The sensitive-data reachability fan-out (the core diagram)

```
                       customer SQL text (crown jewel)
                                  │
              ┌───────────────────┼──────────────────────────────┐
              ▼                   ▼                                ▼
   Performance Insights     CloudWatch metrics            CloudWatch Logs
     dimension store         (DB_PERF_INSIGHTS /           /aws/rds/instance/
   (raw + tokenized SQL)      AWS/RDS namespaces)          <name>/slowquery
        │                          │                            │
   ┌────┴───────────────┐     cloudwatch:GetMetricData     logs:GetLogEvents
   ▼        ▼        ▼   ▼     cloudwatch:GetMetricStatistics logs:FilterLogEvents
 GetResource Describe  GetDimension GetPerformance   │            │
  Metrics   Dimension  KeyDetails   AnalysisReport   │            │
   [P]       Keys [P]   [P]         (NOT [P])        │            │
    │         │          │            │              │            │
    └─────────┴──────────┘            │              │            │
   gated by pi:Dimensions        NOT gated       NOT gated     NOT gated
   condition key  ◄── the ONLY   by pi:Dimensions by pi:      by pi:Dimensions
   fine-grained SQL control                       Dimensions
       │
   [P] = the three (and only three) actions on which pi:Dimensions is a
         valid condition key, per the pi Service Authorization Reference.

  Cross-account overlay: CloudWatch OAM link / CloudWatch-CrossAccountSharingRole
  lets a MONITORING account render all of the above for a SOURCE account.
```

**Every arrow that does not say "gated by pi:Dimensions" is a candidate SQL-leak path around a customer's "hide SQL" policy.** That is the plan.

### 2.3 Doc-derived artifacts to carry into testing (verbatim)

- **`dimensionAccess-policy` — the deny the docs themselves ship (and its documented gap):**
  ```json
  {
    "Sid": "O01DenySQLForGetResourceMetrics",
    "Effect": "Deny",
    "Action": ["pi:GetResourceMetrics"],
    "Resource": ["arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"],
    "Condition": { "ForAnyValue:StringEquals": { "pi:Dimensions": ["db.sql_tokenized.statement"] } }
  }
  ```
  The doc's own annotated `DescribeDimensionKeys` response under this policy returns `{ "Identifier": "db.sql_tokenized.statement" }` with the comment *"allowed for DescribeDimensionKeys because our IAM Policy denies it only for GetResourceMetrics."* AWS documents the parity gap as intended behavior.

- **`cmk-policy` — scoped KMS Allow:**
  ```json
  {
    "Sid": "AllowViewingRDSPerformanceInsights",
    "Effect": "Allow",
    "Principal": {"AWS": ["arn:aws:iam::444455556666:role/Role1"]},
    "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
    "Resource": "*",
    "Condition": {
      "StringEquals": {"kms:ViaService": "rds.us-east-1.amazonaws.com"},
      "ForAnyValue:StringEquals": {
        "kms:EncryptionContext:aws:pi:service": "rds",
        "kms:EncryptionContext:service": "pi",
        "kms:EncryptionContext:aws:rds:db-id": "db-AAAAABBBBBCCCCDDDDDEEEEE"
      }
    }
  }
  ```

- **`tag-based-policy` — ABAC deny + the tag-inheritance rule:**
  ```json
  { "Effect": "Deny", "Action": "pi:GetResourceMetrics", "Resource": "*",
    "Condition": { "StringEquals": { "aws:ResourceTag/env": "prod" } } }
  ```
  Doc: *"Database Insights automatically applies your DB instance tags... To add or update tags for Database Insights metrics, modify the tags on your DB instance."* + *"`TagResource`/`UntagResource`... return an error if you try to use them directly on Database Insights metrics."*

- **`AmazonRDSPerformanceInsightsReadOnly` (v7):** grants `pi:DescribeDimensionKeys`, `pi:GetDimensionKeyDetails`, `pi:GetResourceMetrics` on `arn:aws:pi:*:*:metrics/rds/*` **with no `pi:Dimensions` and no tag condition** — i.e. unconditioned SQL-text read across the account/region. Also `pi:ListTagsForResource` on `arn:aws:pi:*:*:*/rds/*` unconditioned.
- **`AmazonRDSPerformanceInsightsFullAccess` (v6):** grants **no `kms:*`** — confirms KMS decrypt authority must come from elsewhere (Section 5, Lead 7).

---

## 3. Trust-boundary map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Caller with a `pi:Dimensions` deny on `GetResourceMetrics` | Sensitive SQL dimension | sibling `pi:` action (`DescribeDimensionKeys`, `GetDimensionKeyDetails`) | Any SQL digest/text returned despite the deny → deny is not action-complete |
| B2 | Same caller | Sensitive SQL, derived | `GetPerformanceAnalysisReport` (report id, not dimension-gated) | Report body contains SQL/top-query insight the deny should have suppressed |
| B3 | Same caller | Sensitive SQL, as a metric | `cloudwatch:GetMetricData` on DB_PERF_INSIGHTS/per-query metric | Per-query metric keyed by SQL id/text readable via `cloudwatch:` while `pi:` denies it |
| B4 | Same caller | Literal SQL incl. param values | `logs:GetLogEvents` on `/aws/rds/instance/<name>/slowquery` | Verbatim SQL (with literals) read from Logs while `pi:` denies SQL |
| B5 | Monitoring account | Source account's Database Insights | CloudWatch OAM link / `CloudWatch-CrossAccountSharingRole` | Monitoring-account principal renders source-account SQL dimensions |
| B6 | Caller scoped to `db-id=A` in the CMK policy | `db-id=B`'s encrypted PI data | a *second*, unconditioned `kms:Decrypt` grant on the same CMK | B's SQL decrypts though the caller is "scoped" to A |
| B7 | DBA with `pi:` read + `rds:*Tags*` write | ABAC-denied prod DB's SQL | mutate the DB-instance tag the `aws:ResourceTag` deny keys on | Strip `env:prod`, read SQL, (optionally) restore tag |
| B8 | Any customer surface | AWS PI/RDS/CloudWatch fleet identity | — | Any AWS-owned ARN/credential observed = **hard stop**, preserve + disclose |

---

## 4. API / interface inventory

| Name | Svc | Mutating | Ext-facing | `pi:Dimensions` gated? | Returns sensitive SQL? | Notes / lead |
|---|---|---|---|---|---|---|
| `GetResourceMetrics` | pi | No | Yes | **Yes** | Yes (via SQL dims) | The one action AWS's deny examples target |
| `DescribeDimensionKeys` | pi | No | Yes | **Yes** | Yes (`db.sql_tokenized.statement`) | B1 — but deny examples routinely omit it |
| `GetDimensionKeyDetails` | pi | No | Yes | **Yes** | **Yes — full SQL up to ~65 KB** | B1 — highest-fidelity SQL path |
| `GetResourceMetadata` | pi | No | Yes | **No** (key not supported) | metadata | Lens S vacuous-condition surface |
| `ListAvailableResourceDimensions` | pi | No | Yes | **No** (key not supported) | dimension catalog | Lead 1 — `ForAllValues` on it is vacuous |
| `ListAvailableResourceMetrics` | pi | No | Yes | **No** | metric catalog | enumeration |
| `GetPerformanceAnalysisReport` | pi | No | Yes | **No** | SQL-derived insights | B2 — dual-identifier + not gated |
| `CreatePerformanceAnalysisReport` | pi | Yes | Yes | No | — | creates `report-…` id |
| `ListPerformanceAnalysisReports` | pi | No | Yes | No | report ids | id-enumeration recon |
| `ListTagsForResource` | pi | No | Yes | No | DB tags | Lead 8 recon; unconditioned in ReadOnly policy |
| `TagResource` / `UntagResource` | pi | Yes | Yes | — | — | **Error on PI metrics** — tags only via `rds:` |
| `rds:AddTagsToResource` / `RemoveTagsFromResource` | rds | Yes | Yes | — | — | **B7 — the real ABAC control surface** |
| `cloudwatch:GetMetricData` / `GetMetricStatistics` | cloudwatch | No | Yes | **No** | per-query metrics | B3 |
| `logs:GetLogEvents` / `FilterLogEvents` | logs | No | Yes | **No** | **literal SQL** | B4 |
| `oam:CreateLink` / `oam:CreateSink` | oam | Yes | Yes | — | — | B5 — ResourceTypes has **no** PI/RDS type |

**Note the `[NEW]`/focus signal:** the docs' own dimension-access page *demonstrates* a deny that leaves SQL readable via a sibling action and presents it as correct — AWS effectively planted the lead. Start there.

---

## 5. Recommended areas of focus (ranked leads)

### Lead 1 — `GroupBy.Group` with the `Dimensions` sub-field omitted: does `pi:Dimensions` populate with the group name or the expanded members? *(Lens S/U — CRITICAL, single highest-leverage test)*
- **Claim:** A `GetResourceMetrics`/`DescribeDimensionKeys` call that supplies `GroupBy={"Group":"db.sql_tokenized"}` with **no** `Dimensions` array is documented to expand server-side to *all* members (incl. `db.sql_tokenized.statement`). If, at IAM-evaluation time, the `pi:Dimensions` request-context key is populated with the **group name** (`"db.sql_tokenized"`) rather than the expanded member identifiers, then the canonical AWS "deny SQL" policy — keyed on `"db.sql_tokenized.statement"` under `StringEquals` — never matches, and omitting one field is a one-line bypass of the exact policy AWS publishes.
- **Mechanism:** `API_DimensionGroup` — *"If this parameter is not present, then it signifies that all of the dimensions in the group were requested."* No doc states how the implicit expansion populates `pi:Dimensions` for authorization. Genuine doc gap.
- **Oracle:** Apply `Deny GetResourceMetrics ForAnyValue:StringEquals pi:Dimensions=["db.sql_tokenized.statement"]` + broad Allow. Call with `GroupBy={"Group":"db.sql_tokenized"}` and no `Dimensions`. **Confirmed-bypass** if SQL digest text returns.
- **Preconditions:** one DB with PI on; a role with the deny. **Cost:** minutes. **Severity if true:** Critical.

### Lead 2 — Action-parity gap: SQL denied on `GetResourceMetrics` still flows through `DescribeDimensionKeys` / `GetDimensionKeyDetails` *(Lens X/U — HIGH, doc-confirmed)*
- **Claim:** The docs' own worked deny scopes only `pi:GetResourceMetrics`, leaving `db.sql_tokenized.statement` fully retrievable via the two sibling actions — and `GetDimensionKeyDetails` returns **full SQL up to ~65 KB**. Customers who copy the example get a redaction they believe is complete.
- **Mechanism:** `dimensionAccess-policy` Sid `O01DenySQLForGetResourceMetrics` + the doc's annotated `DescribeDimensionKeys` response comment (Section 2.3). `AmazonRDSPerformanceInsightsReadOnly` grants all three actions unconditioned, so most real principals hold the siblings.
- **Oracle:** Under the exact documented deny + an Allow for all three, call `GetDimensionKeyDetails`/`DescribeDimensionKeys` for `db.sql_tokenized`. Confirmed if SQL text/ids return (doc asserts it will — the live test verifies the doc is not stale).
- **Preconditions:** trivial. **Cost:** minutes. **Severity:** High.

### Lead 3 — CloudWatch Logs slow-query path: literal SQL (with parameter values) around every `pi:` control *(Lens T — HIGH)*
- **Claim:** Slow-query / general / engine logs under `/aws/rds/instance/<name>/<log_type>` contain **literal, non-tokenized** SQL including parameter values (and, per AWS's own warning, potentially passwords). They are read via `logs:GetLogEvents`/`FilterLogEvents` — a **completely different IAM namespace** with no `pi:Dimensions` analogue. A perfect `pi:` SQL deny provides zero protection here.
- **Mechanism:** subagent A — RDS log export to CloudWatch Logs; AWS docs warn about credential exposure in query logs; log-group encryption is independent of the PI CMK.
- **Oracle:** Configure a DB to export slow-query logs; issue a canary slow query with a canary literal (`SELECT /*CANARY-<uuid>*/ ...`); as a principal with a full `pi:Dimensions` SQL deny but `logs:GetLogEvents`, read the log group. Confirmed if the canary literal appears.
- **Preconditions:** log export enabled (common). **Cost:** low. **Severity:** High (literal values, not just digests).

### Lead 4 — CloudWatch metric path: per-query metrics readable via `cloudwatch:` bypassing `pi:` *(Lens T/X — MEDIUM-HIGH)*
- **Claim:** Advanced mode publishes detailed per-query / DB-counter metrics to CloudWatch (DB_PERF_INSIGHTS-style namespace). These are retrievable via `cloudwatch:GetMetricData`/`GetMetricStatistics`/metric-math — not gated by `pi:Dimensions`. If metric dimensions carry SQL id/tokenized-id (or the text), a `pi:` SQL deny is bypassed. **Also:** the SLR `AWSServiceRoleForCloudWatchMetrics_DbPerfInsights` holds `pi:GetResourceMetrics` on `Resource:"*"` conditioned only on `aws:ResourceAccount == PrincipalAccount` (no `pi:Dimensions`) — audit whether metric-math over that SLR-published data re-exposes denied dimensions.
- **Mechanism:** `USER_PerfInsights.Enabling` (per-query metrics in Advanced mode); subagent A (SLR policy).
- **Oracle:** With a `pi:` SQL deny + `cloudwatch:GetMetricData`, enumerate the DB_PERF_INSIGHTS namespace and pull any metric dimensioned by SQL id/text. Confirmed if SQL-identifying data returns via `cloudwatch:` alone.
- **Preconditions:** Advanced mode. **Cost:** low-med. **Severity:** Medium-High (id/tokenized more likely than literal text).

### Lead 5 — Cross-account observability decouples from the source account's `pi:Dimensions` denies *(Lens A — HIGH / Critical if cross-account)*
- **Claim:** A monitoring account linked via CloudWatch OAM or the legacy `CloudWatch-CrossAccountSharingRole` ("Include read-only access for Database Insights") renders the source account's Database Insights. Monitoring-account local permissions are typically wildcard, and the source-side sharing role's auto-generated CFN policy — the *actual* boundary — is opaque and not automatically covered by the source account's `pi:Dimensions` denies. Result: a source-account "hide SQL" deny may not apply to the cross-account render path.
- **Mechanism:** subagent A — `oam:CreateLink` `ResourceTypes` has **no** PI/RDS type (so OAM's own type list doesn't gate PI); legacy sharing-role checkbox explicitly includes Database Insights; the sharing role's generated policy is never shown in docs.
- **Oracle:** In a source account, apply a `pi:Dimensions` SQL deny to the sharing role (or rely on defaults). From the monitoring account, open Database Insights for the source DB and attempt to view SQL dimensions. Confirmed if SQL renders cross-account despite the source-side deny; **hard-stop escalation** only if it reaches beyond the two authorized accounts.
- **Preconditions:** two accounts, OAM/legacy link. **Cost:** medium (setup). **Severity:** High; cross-account = Critical.

### Lead 6 — ABAC self-widening: strip the DB-instance tag the `pi:` deny keys on *(Lens I — HIGH)*
- **Claim:** A tag-based `pi:` deny (`aws:ResourceTag/env=prod`) is enforced against tags **inherited from the DB instance**, and `TagResource`/`UntagResource` error on the PI metric — so the only way to change the authz input is `rds:AddTagsToResource`/`RemoveTagsFromResource` on the DB instance. A DBA role that holds both `pi:` read and `rds:*Tags*` (a plausible pairing) can remove `env:prod`, read the SQL, then restore the tag. The control surface lives in a different IAM namespace (`rds:`) than the deny (`pi:`), so a `pi:`-only least-privilege review misses it.
- **Mechanism:** `tag-based-policy` (inheritance rule + `TagResource` error note); subagent B.
- **Oracle:** Principal with the `env:prod` `pi:` deny + `rds:RemoveTagsFromResource` on the `db:*` ARN: `GetResourceMetrics` (expect deny) → strip tag → retry. Confirmed if the retry succeeds.
- **Preconditions:** co-granted `pi:` read + `rds:` tag write. **Cost:** minutes. **Severity:** High.
- **Sub-lead 6a (Lens I, TOCTOU):** the docs claim tags are usable "immediately" but give no consistency model — tag an untagged DB and tight-loop `GetResourceMetrics` under the deny; any window where calls succeed after the tag-write ack is a fail-open race. Severity Medium.

### Lead 7 — KMS: the scoped Allow is additive, not exclusive *(Lens H — HIGH)*
- **Claim:** The `AllowViewingRDSPerformanceInsights` statement scopes decrypt to one `aws:rds:db-id`, but KMS authz is OR-across-Allows. If the CMK retains its default "Enable IAM User Permissions" root delegation, or the principal separately holds an unconditioned `kms:Decrypt`/`kms:GenerateDataKey` on that key (common — shared with EBS/Secrets Manager), that alone authorizes decrypt for **any** `db-id` sharing the key. The per-database boundary the example implies does not exist unless the customer independently ensures no other Decrypt grant applies. `AmazonRDSPerformanceInsightsFullAccess` grants no `kms:*`, confirming decrypt authority comes from elsewhere.
- **Mechanism:** `cmk-policy` (recommendation phrased as an *additional* Allow, never "deny all other decrypt"); managed-policy JSON (subagent B).
- **Oracle:** Role with (a) the scoped Allow for `db-id=A` only + (b) a separate unconditioned `kms:Decrypt` on `Resource:"*"`. Request PI sensitive data for `db-id=B` sharing the CMK. Confirmed-bypass if B decrypts.
- **Preconditions:** shared CMK + a second decrypt grant. **Cost:** medium. **Severity:** High.
- **Sub-lead 7a (Lens U, doc gap):** `DbiResourceId` lifecycle across restore/rename/clone is undocumented; if it is preserved, key-policy statements scoped to the "old" DB identity silently authorize the restored/renamed one — test restore + snapshot flows.

### Lead 8 — Dimension-name string fragility: aliases and vacuous conditions *(Lens S — MEDIUM)*
- **Claim (8a, alias):** `db.sql.tokenized_id` is documented to *"fetch the value of the `db.sql_tokenized.id` dimension"* but is a **different string** in a different group (`db.sql`). Since `pi:Dimensions` is matched by `StringEquals`, a deny on `db.sql_tokenized.id` never matches the alias `db.sql.tokenized_id`. Probe systematically for a `db.sql.statement` ⇄ `db.sql_tokenized.statement` analogue.
- **Claim (8b, vacuous):** `pi:Dimensions` is not a supported condition key on `ListAvailableResourceDimensions`/`ListAvailableResourceMetrics`/`GetResourceMetadata`; a `ForAllValues:StringEquals pi:Dimensions=[…]` condition on those actions is unconditionally true (vacuous truth on an absent key), so a policy author's intended discovery restriction is a no-op.
- **Claim (8c, wrong operator):** a customer who writes `ForAllValues:StringEquals` on a **Deny** (instead of AWS's `ForAnyValue`) gets a deny that only fires when *every* requested dimension equals the single denylisted value — mixing the sensitive dimension with any other in one multi-member (`Dimensions` supports 10) call defeats it.
- **Mechanism:** `API_DimensionGroup` (alias language); `pi` Service Authorization Reference condition-key table (subagent B); `API_DimensionGroup` (10-member max).
- **Oracle:** (8a) deny `db.sql_tokenized.id`, request via `GroupBy.Group=db.sql`, `Dimensions=["db.sql.tokenized_id"]` — confirmed if value returns. (8c) deny with `ForAllValues`, request `["db.sql_tokenized.statement","db.wait_event.name"]` — confirmed if SQL returns.
- **Severity:** Medium (8a/8b info-disclosure/hash; 8c High if the wrong-operator pattern is circulating — sweep blogs/SO/CFN templates).

### Lead 9 — Report-id enumeration & `GetPerformanceAnalysisReport` dual-identifier *(Lens A/X — MEDIUM)*
- **Claim:** `GetPerformanceAnalysisReport` is **not** gated by `pi:Dimensions` yet returns SQL-derived top-query insights, and the report id `report-[0-9a-f]{17}` is shorter (~68 bits) than the DbiResourceId. Test (a) whether the report body leaks SQL a `pi:Dimensions` deny should suppress, and (b) whether the API validates report **ownership** vs merely existence when a report id is supplied alongside a DB identifier (two-ways-to-name-one-resource IDOR shape).
- **Mechanism:** PI API Reference (`API_GetPerformanceAnalysisReport` — dual identifier, Insights Dimensions/Filter maps); not in the `pi:Dimensions`-supported action list.
- **Oracle:** With a `pi:Dimensions` SQL deny, create a report, then `GetPerformanceAnalysisReport` and inspect for SQL. Separately, attempt to fetch a report id belonging to another DB/tenant. Confirmed if SQL leaks or a foreign report is read.
- **Severity:** Medium (report insights are aggregated, but derived from SQL); cross-tenant read = High.

---

## 6. Threat-model test objectives (execution checklist for the hunter)

Run against an authorized account with PI enabled. **Use canary SQL only** — e.g. `SELECT /*CANARY-<uuid>*/ <marker> FROM ...` — so any leak is unambiguous and no real query text is exposed.

1. Stand up a DB with PI **Advanced** mode + slow-query log export + a customer-managed KMS key.
2. Create a role holding `AmazonRDSPerformanceInsightsReadOnly` + the documented `O01DenySQLForGetResourceMetrics` deny; confirm Leads 1, 2, 8, 9 against it.
3. Create a second role with `logs:GetLogEvents` + `cloudwatch:GetMetricData` but the full `pi:` SQL deny; confirm Leads 3, 4.
4. Create a DBA role with `pi:` read + `rds:*Tags*`; confirm Lead 6 (+6a race).
5. Configure a shared CMK with a second unconditioned decrypt grant; confirm Lead 7 (+7a restore semantics).
6. Link a second authorized account via OAM/legacy sharing role; confirm Lead 5 — **stop immediately if evidence reaches beyond the two in-scope accounts or touches an AWS-owned identity (B8).**
7. For every confirmed leak, record the exact request/response with the canary marker as evidence; tear down all created resources.

---

## 7. Out of scope / hard stops

- **No live testing was performed in producing this plan** — all leads require an authorized account to confirm.
- Any AWS-owned service-plane identity, credential, ARN, or the PI/RDS/CloudWatch fleet (B8) → **hard stop, preserve evidence, flag for disclosure, do not proceed.**
- No DNS/port/subdomain enumeration; HTTP/application (AWS API) layer only.
- No destructive actions; read-only + canary data; restore all mutated tags/policies.
- Do not exfiltrate real customer SQL — canary markers only.

## 8. Null hypotheses & documentation gaps

- **Direct cross-tenant IDOR on `pi:` metric ARNs (Lens A, base):** *likely N/A* — the DbiResourceId is 26-char high-entropy and not enumerable. Checked: PI API Reference resource ARN shapes, `USER_DatabaseInsights` overview. The realistic cross-tenant path is cross-**account** via OAM (Lead 5), not id-guessing. Report-id (68-bit) enumeration is weaker but non-trivial (Lead 9).
- **SSRF / URL-dereference (Lens G):** *N/A* — checked `Enabling`, `access-control.*`, `Considerations`, dashboard/report pages; no field the service dereferences (no `…Url`/webhook/logo). Database Insights takes no customer-supplied URI.
- **Translation-layer injection (Lens F):** *N/A for the `pi:` control plane* — PI dimensions are read-only projections; no customer-supplied query is re-parsed by PI. (The SQL *content* is the asset, not an injection vector into PI itself.)
- **Documentation gaps flagged (each is itself a lead to close with a live oracle):**
  1. How `pi:Dimensions` populates when `GroupBy.Group` omits `Dimensions` (Lead 1) — **highest-value gap.**
  2. `DbiResourceId` lifecycle across restore/rename/clone (Lead 7a).
  3. No complete KMS key policy (with the default root statement) shown beside the scoped Allow (Lead 7).
  4. No consistency/propagation model for DB-instance-tag → PI-metric-tag inheritance (Lead 6a).
  5. Whether other cross-group dimension aliases exist beyond `db.sql.tokenized_id` (Lead 8a).
  6. The `pi` Service Authorization Reference slug given in some cross-references (`list_amazonrdsperformanceinsights.html`) 302-redirects / is dead; the live slug is `list_pi.html` — broken cross-reference worth noting.

---

*End of plan. Prepared documentation-only; every lead is a hypothesis to be confirmed or refuted against an authorized environment with synthetic data.*
