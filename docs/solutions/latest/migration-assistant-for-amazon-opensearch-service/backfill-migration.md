---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/backfill-migration.html
---

# Backfill migration
<a name="backfill-migration"></a>

Backfill is accomplished with Reindex-from-Snapshot (RFS) by moving existing documents from your source cluster to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. RFS takes a one-time snapshot of the source cluster (the only time the source is touched), reads the raw Lucene segment files directly from the snapshot in Amazon S3, extracts documents, applies transformations, and bulk-indexes them on the target. The format of Elasticsearch and OpenSearch indices is such that each shard of each index can be parsed, extracted, and reindexed independently, which means the work can be fanned out at the shard level on Amazon EKS.

This approach improves the migration experience by:
+ Removing load from the source cluster during backfill migration after the source cluster snapshot is taken
+ Enabling "hopping" across multiple major versions without having to pass through the intermediate versions
+ Creating a migration path from post-fork versions of Elasticsearch to Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen
+ Increasing the speed of backfill migration by parallelizing work at the shard level
+ Simplifying the process of pausing and resuming a migration — RFS automatically resumes from the last checkpoint when restarted, already-migrated shards are skipped, and no data is duplicated

Useful RFS tuning settings include `podReplicas` (number of RFS worker pods), `maxConnections` (bulk-indexer concurrency to the target), `documentsPerBulkRequest` and `documentsSizePerBulkRequest` (bulk request count and byte-size limits), `maxShardSizeBytes` (default 80 GiB and used to calculate ephemeral storage), `initialLeaseDuration` (default `PT1H`), `serverGeneratedIds` for Serverless collection compatibility, `allowedDocExceptionTypes` for expected document-level target errors, and sourceless migration options when `_source` is disabled or filtered.
