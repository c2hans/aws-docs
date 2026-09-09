---
name: athena-cross-tenant-variant-analysis
description: Outcome of variant analysis of the fixed Athena system-catalog cross-tenant bug (act.security/Oren Yomtov) — all V1-V8 refuted, fix is robust
metadata:
  type: project
---

Variant analysis (run 2026-09-09-1) of the disclosed+fixed Athena engine-v3 cross-tenant
bug (act.security / Oren Yomtov, "Reading other AWS accounts' SQL on Amazon Athena";
`QueryExecutionContext.Catalog=system` → `system.runtime.queries` leak, fixed Aug 2025).

**Result: every variant REFUTED. The fix is comprehensive and defense-in-depth.** Observed
post-fix guard behavior (worth not re-deriving next time):

- Two distinct guards now exist: textual `system.x.y` in SQL → parser error
  `"Queries of this type are not supported"`; out-of-band `QueryExecutionContext.Catalog`
  normalized-equals `system` → dedicated start-time error `"System database is not supported"`.
- The Catalog guard normalizes case + surrounding ASCII whitespace (System/SYSTEM/" system"/tab all blocked).
- Guard-bypassing values (trailing dot `system.`, zero-width `​system`, cyrillic/soft-hyphen
  homoglyphs) get PAST the guard but resolve to the CALLER'S OWN default Glue catalog
  (AwsDataCatalog) or CATALOG_NOT_FOUND — never the shared Trino `system` catalog. Verified via
  identical `information_schema` counts (8 tables / 1 schema) vs AwsDataCatalog baseline. So the
  guard/resolver normalization mismatch is NOT exploitable (hardening note only).
- Metadata plane (ListDatabases/GetDatabase/GetTableMetadata/ListTableMetadata) does strict
  registered-catalog resolution → `"Cannot find catalog system"` for all variants; never reaches Trino internals.
- Prepared statements validate at create AND update time (`"Exception parsing query"`); execute-time
  still hits the context guard. No deferred-validation gap.
- Federation: `CreateDataCatalog` name system/System/awsdatacatalog rejected
  (`"...is restricted"` / `"...is reserved"`); no name-shadowing.
- Spark plane: per-session isolated container (own /tmp, own warehouse in caller's S3 bucket,
  own Glue metastore, own scoped AthenaExecutor role). Cross-account IDOR on
  Get/ListCalculationExecution*, GetSession* → `"Not authorized to make this request"`. IMDS reachable
  from user code but yields only the session's own execution role.

Methodology that worked: run a background canary loop in Account B submitting
`CANARY_<uuid>` in query text (validates via B's own history that the marker is live in the shared
plane), then probe from Account A checking only aggregate COUNTs / canary presence.
