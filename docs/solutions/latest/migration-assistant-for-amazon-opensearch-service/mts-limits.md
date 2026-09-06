---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/mts-limits.html
---

# Limits and considerations
<a name="mts-limits"></a>

The serverless model removes infrastructure management but also removes several cluster-level capabilities that exist on an Amazon OpenSearch Service domain. Plan for the following before you migrate to an Amazon OpenSearch Serverless NextGen collection.

 **Index size.** For an Amazon OpenSearch Serverless NextGen `SEARCH` or `VECTORSEARCH` collection, an index can hold up to 1 TiB of data. If a source index would exceed this limit, split it before migration or reduce its scope.

 **Request payload size.** Amazon OpenSearch Serverless NextGen enforces a maximum size for an individual indexing request. Reindex-from-Snapshot limits bulk requests with both `documentsSizePerBulkRequest` (default 10 MiB) and `documentsPerBulkRequest`. If backfill returns request-too-large errors against the collection, lower `documentsSizePerBulkRequest`; if many small documents still produce oversized requests, also lower `documentsPerBulkRequest`.

 **RFS work coordination.** RFS tracks shard leases and completion state in an OpenSearch-compatible coordination store. Do not set `documentBackfillConfig.useTargetClusterForWorkCoordination` to `true` for an Amazon OpenSearch Serverless NextGen target; Serverless does not support the coordination indices RFS requires. Leave the setting at its default `false` so the workflow deploys a temporary single-node OpenSearch coordinator cluster.

 **Features you must recreate manually.** Amazon OpenSearch Serverless NextGen does not provide the following, and Migration Assistant does not migrate them automatically. Recreate them on the collection (or in your application and ingest tier) after migration:
+ Node-level snapshots and snapshot repositories.
+ Index State Management (ISM) and Index Lifecycle Management (ILM) policies.
+ Ingest pipelines.
+ Custom plugins.
+ Cluster-level settings managed through `_cluster/settings`.

For metadata that the solution does migrate (index settings, mappings, templates, and aliases), see how field-type and collection-type adaptations are applied in [Collection types](mts-collection-types.md). For an end-to-end walkthrough of an Amazon OpenSearch Service domain to Amazon OpenSearch Serverless NextGen collection migration, see the [Amazon OpenSearch Service to Amazon OpenSearch Serverless NextGen](playbook-aos-to-serverless.md) playbook. To deploy the solution on Amazon EKS before you begin, see [Deploy the solution](deploy-the-solution.md).
