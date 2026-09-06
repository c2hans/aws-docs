---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/migrate-to-serverless.html
---

# Migrate to Amazon OpenSearch Serverless NextGen
<a name="migrate-to-serverless"></a>

This section describes how to target an [Amazon OpenSearch Serverless NextGen](https://aws.amazon.com/opensearch-service/features/serverless/) collection when you run the Migration Assistant for Amazon OpenSearch Service solution. Targeting Amazon OpenSearch Serverless NextGen follows the same Workflow CLI lifecycle described in [Getting started with the Workflow CLI](use-the-solution.md#getting-started) — load the version-matched sample, configure the target, prove connectivity, run a pilot, and then run the full workflow. The differences are confined to how you configure the target cluster, how you grant access through a collection data access policy, and a set of platform constraints that come from the serverless model.

Every source that the solution supports can use an Amazon OpenSearch Serverless NextGen collection as its target. Backfill with Reindex-from-Snapshot (RFS) is available for all supported sources. Live capture and replay is available wherever the source itself supports it. Apache Solr supports live capture and replay only for SolrCloud sources with JSON-format writes; standalone Solr and Elasticsearch 1.x-2.x sources are backfill-only. For Solr replay into Serverless, set the Solr transform provider’s `targetType` to `NextGenOpenSearchServerless` so the replayer suppresses unsupported refresh parameters.

**Note**
Amazon OpenSearch Serverless NextGen removes the cluster-management surface that exists on an Amazon OpenSearch Service domain. There are no node-level snapshots, no `_cluster/settings`, and no cluster plugins to configure. Migration Assistant adapts metadata migration to the collection model for you, but you must recreate operational features such as index lifecycle management and ingest pipelines yourself. See [Limits and considerations](mts-limits.md).
