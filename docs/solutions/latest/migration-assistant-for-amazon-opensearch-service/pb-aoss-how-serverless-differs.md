---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-how-serverless-differs.html
---

# How Serverless differs
<a name="pb-aoss-how-serverless-differs"></a>

Amazon OpenSearch Serverless NextGen removes the cluster-management surface you may rely on with an Amazon OpenSearch Service domain. Account for these differences before you plan the migration:
+  **No snapshot restore.** You cannot restore a source snapshot directly into a collection. Migration Assistant still uses a snapshot as the read source for RFS, but it bulk-indexes documents through the OpenSearch API rather than restoring.
+  **No ISM/ILM policies, ingest pipelines, or custom plugins.** These are not migrated and have no equivalent to configure on the collection. Plan replacement logic in your ingestion path (for example, [OpenSearch Ingestion](https://aws.amazon.com/opensearch-service/features/ingestion) pipelines) before cutover.
+  **No `_cluster/settings` and no node-level tuning.** Capacity scales automatically through OpenSearch Compute Units (OCUs), so the cluster-tuning knobs you set on a domain do not apply.
+  **SigV4 only.** All access is IAM-based. There is no basic-auth or FGAC user on the collection.
+  **Index size limit.** A single index in a collection has a maximum size (1 TB for the search and vector-search collection types). Reduce oversized source shards or split large source indexes before backfill.
+  **Bulk payload limit.** Keep bulk requests modest. `documentsSizePerBulkRequest` caps the aggregate document bytes per bulk request (default 10 MiB), and `documentsPerBulkRequest` caps the document count. Lower the byte-size limit first if the collection rejects large requests.
