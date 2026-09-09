---
name: teardown-quirks
description: Athena FEDERATED data-catalog teardown quirks (tombstones, orphaned Glue connection)
metadata:
  type: reference
---

Tearing down Athena `FEDERATED` DataCatalogs:
- `DeleteDataCatalog` on a COMPLETE FEDERATED catalog kicks off async backing teardown (deletes the CFN stack, Lambda, IAM FunctionRole) — but does **NOT** delete the derived **Glue connection** `athenafederatedcatalog_<name>`. Delete it manually with `glue delete-connection`.
- FEDERATED catalogs that ended in `CREATE_FAILED_CLEANUP_COMPLETE`, or a catalog after `DELETE_COMPLETE`, remain visible in `ListDataCatalogs` as **tombstones**: `GetDataCatalog` resolves them, but `DeleteDataCatalog` returns `InvalidRequestException: DataCatalog X was not found` (both with and without `--delete-catalog-only`). They have **zero backing infrastructure** and self-purge over time — benign residual, document and move on.
- To reveal the sanitized derived resource name cheaply without full provisioning: issue a `FEDERATED` `MYSQL` create with missing required props; it fast-fails but `GetDataCatalog` Parameters still shows the derived `connection-arn` (`athenafederatedcatalog_<sanitized>`).
