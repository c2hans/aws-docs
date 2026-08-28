---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/mts-collection-types.html
---

# Collection types
<a name="mts-collection-types"></a>

When you create an Amazon OpenSearch Serverless NextGen collection, you choose a collection type. The collection type determines how documents are indexed and, importantly for migration, whether the source document ID is preserved or replaced with a server-generated ID. Migration Assistant adapts metadata migration to the collection type so that the migrated indexes are compatible with the target.

| Collection type | Document IDs | Migration behavior |
| --- | --- | --- |
|  `SEARCH`  | Source document IDs are preserved. | Full-text search workloads. Index mappings and settings are migrated and adapted to the collection model. Because source IDs are preserved, backfill is idempotent and re-running it does not create duplicate documents. |
|  `TIMESERIES`  | Server-generated IDs (source document IDs are not preserved). | Time-series workloads. RFS auto-detects the collection type and enables server-generated IDs so backfill can write documents to the collection. Do not rely on capture and replay to reconcile updates or deletes by source `_id` on this target type. |
|  `VECTORSEARCH`  | Server-generated IDs (source document IDs are not preserved). | Vector and semantic search workloads. `knn_vector` field mappings are automatically converted to the Faiss HNSW engine for serverless compatibility, and `model_id` references are removed because Amazon OpenSearch Serverless NextGen does not support training APIs. |

**Important**
Document-ID preservation during capture and replay is only meaningful on a `SEARCH` collection. On `TIMESERIES` and `VECTORSEARCH` collections, the target assigns its own document IDs, so an update or delete captured against a specific source `_id` cannot be matched to the same document on the target. If your migration relies on capture and replay to reconcile updates and deletes by document ID, target a `SEARCH` collection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
