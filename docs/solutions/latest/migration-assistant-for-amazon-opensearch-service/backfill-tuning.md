---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/backfill-tuning.html
---

# Backfill tuning
<a name="backfill-tuning"></a>

Configure RFS settings under `documentBackfillConfig` in the workflow configuration. For one-off manual runs, the same behavior is exposed by the `console backfill` and RFS command-line options.

## Scope and parallelism
<a name="backfill-scope-and-parallelism"></a>
+  `indexAllowlist` - filters which indices RFS migrates from the snapshot. For Elasticsearch and OpenSearch snapshots, each entry is either an exact index name or a regex prefixed with `regex:`. For Apache Solr backups, use exact collection or core names only; `regex:` entries are not applied by the Solr reader. An empty list includes all non-system indices in the snapshot, or all discovered Solr collections and cores in the backup.
+  `podReplicas` - number of RFS worker pods. Each worker independently acquires snapshot shards, so throughput scales up to the number of eligible source shards.
+  `maxConnections` - maximum concurrent HTTP connections from each RFS worker to the target for bulk indexing. Increasing this can improve throughput, but it also increases target write pressure.
+  `allowLooseVersionMatching` - allows document migration when source and target versions are not an exact match. Leave enabled unless you are troubleshooting snapshot parsing or version compatibility behavior.

For Elasticsearch and OpenSearch `indexAllowlist` entries prefixed with `regex:`, the pattern must match the entire index name. Use expressions such as `regex:logs-. ` for prefixes or `regex:.` for suffixes; `regex:logs` matches only the exact string `logs`. For Solr sources, list collection or core names exactly.

Because RFS reads from snapshot storage in Amazon S3, increasing worker count does not add live read load to the source cluster. It mainly changes how quickly the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection is driven.

## Bulk request sizing
<a name="backfill-bulk-sizing"></a>
+  `documentsPerBulkRequest` - maximum number of documents per bulk request. The workflow default is effectively unlimited (`2147483647`), so the payload-size limit usually controls batching.
+  `documentsSizePerBulkRequest` - maximum aggregate document size per bulk request in bytes. The default is 10 MiB (`10485760`). Individual documents larger than this limit are sent as single-document requests.

If the target rejects large bulk requests or experiences indexing pressure, reduce `documentsSizePerBulkRequest`, `documentsPerBulkRequest`, `maxConnections`, or `podReplicas`. If the target has capacity and RFS workers are waiting on target writes, increase these values gradually while monitoring target metrics.

## Shards, leases, and storage
<a name="backfill-shards-leases-and-storage"></a>
+  `maxShardSizeBytes` - expected maximum source shard size in bytes. The default is 80 GiB (`85899345920`). Set this to at least the largest shard you plan to migrate; RFS rejects shards that exceed the configured value.
+  `initialLeaseDuration` - ISO-8601 duration for the first worker lease on a shard. The workflow default is `PT1H`; the underlying RFS command default is `PT10M`, so pass `--initial-lease-duration` explicitly when you run RFS outside the workflow and want workflow-equivalent lease timing. If a worker does not finish the shard before the lease expires, another worker can pick it up and the lease duration doubles on retry. Increase this for very large shards so workers have enough time to download, unpack, and checkpoint progress without repeatedly re-downloading the same shard.
+  `resources` - Kubernetes resource requests and limits for RFS workers. If you omit `ephemeral-storage`, the workflow calculates it as `ceil(2.5 * maxShardSizeBytes)`. If you set an ephemeral-storage request or limit below that value, workflow validation fails.

RFS needs local ephemeral storage while it downloads and unpacks snapshot shard files. Raising `maxShardSizeBytes` can therefore require larger RFS pod storage, even if you do not override `resources` directly.

## Target compatibility and transformations
<a name="backfill-target-compatibility"></a>
+  `serverGeneratedIds` - controls document ID behavior. `AUTO` is the default: RFS preserves source document IDs for target types that support custom IDs and enables server-generated IDs for Serverless `TIMESERIES` or `VECTORSEARCH` collections that require them. `ALWAYS` discards source document IDs for all targets. `NEVER` preserves source document IDs, which can fail for Serverless time-series or vector collections.
+  `emitDocType` - controls whether RFS sends legacy Elasticsearch `_type` metadata. `AUTO` emits `_type` only for Elasticsearch 6 or earlier sources when a document transformer is configured. Leave this on `AUTO` unless you have a legacy multi-type migration plan.
+  `documentTransforms` - preferred workflow field for document backfill transform pipelines. Use it when the workflow should mount JavaScript or Python transform files and generate the raw document transformer configuration.
+  `docTransformerConfig`, `docTransformerConfigBase64`, and `docTransformerConfigFile` - raw document transformer configuration forms for manual or expert use. Do not set these fields together with `documentTransforms`.
+  `allowedDocExceptionTypes` - list of target bulk-item error type strings to accept as successful document operations. Accepted documents are not retried and are not counted as failures. Use this carefully for expected, idempotent errors such as `version_conflict_engine_exception`. Other common OpenSearch bulk error type strings include `mapper_parsing_exception`, `strict_dynamic_mapping_exception`, `document_missing_exception`, `action_request_validation_exception`, `invalid_index_name_exception`, `routing_missing_exception`, `illegal_argument_exception`, and `resource_already_exists_exception`.

For type-mapping migrations, configure compatible metadata, document backfill, and replay transforms together. See [Transform type mappings](transform-type-mappings.md).

### Backfilling data stream documents
<a name="backfill-data-streams"></a>

Metadata migration does not create data streams or their templates. To backfill documents from a source data stream, first create the matching index template and target data stream yourself. Then configure RFS to read the source data stream’s `.ds-*` backing indexes from the snapshot and write each document to the target data stream alias.

Use `documentBackfillConfig.indexAllowlist` to include the backing indexes. For Elasticsearch and OpenSearch sources, list exact backing-index names such as `.ds-logs-000001`, or use a full-match regex entry such as `regex:\.ds-logs-.*`.

The standard RFS image includes a JavaScript transform at `js/dataStreamBackingIndexTransform.js`. Configure it through the raw `docTransformerConfig` field because workflow-managed `documentTransforms` is for inline or mounted user scripts. The transform rewrites bulk operations whose `_index` starts with `.ds-` so that `_index` becomes the data stream name and `op_type` becomes `create`.

```
documentBackfillConfig:
  indexAllowlist:
    - 'regex:\.ds-logs-.*'
  docTransformerConfig: >-
    [{"JsonJSTransformerProvider":{"initializationResourcePath":"js/dataStreamBackingIndexTransform.js","bindingsObject":"{}"}}]
  allowedDocExceptionTypes:
    - version_conflict_engine_exception
```

Use `allowedDocExceptionTypes` only for errors that are expected and safe to treat as successful document operations. `version_conflict_engine_exception` is useful for data streams when duplicate create attempts can occur, such as when the target already contains a document or a retried RFS operation reaches the same document again.

## Sourceless migrations
<a name="backfill-sourceless-migrations"></a>

Some source indices have `_source` disabled or partially filtered. RFS can reconstruct those documents from stored fields, `doc_values`, Lucene point values, indexed terms, and mapping-level constant values, but you must opt in explicitly:
+  `enableSourcelessMigrations` - enables sourceless document reconstruction. Set this in both `metadataMigrationConfig` and `documentBackfillConfig` so metadata evaluation and document backfill use the same assumptions.
+  `useRecoverySource` - treats `_recovery_source` as `_source` during document backfill when it is available in Elasticsearch 7 or OpenSearch snapshots with soft deletes. This field is transient and may not exist for every document, so use it only when stored-field and `doc_values` reconstruction is insufficient. Metadata evaluation does not read document bodies, so the required metadata-side opt-in for sourceless indexes is `metadataMigrationConfig.enableSourcelessMigrations`.
+  `positionGapStopword` - token used to preserve skipped Lucene positions while reconstructing analyzed text fields. The default is `a`. The token must be a stopword for the target analyzer or it can become searchable text. Set it to an empty string only if you intentionally want to opt out of this filler behavior.

During reconstruction, RFS preserves any existing `_source` fields first, then fills missing fields from the Lucene segment. It suppresses `copy_to` target fields because those targets are index-time mirrors and do not appear in the original `_source`; when possible, it can reverse-derive a missing source field from a less-lossy `copy_to` target such as a keyword-style field.

**Important**
Sourceless reconstruction is best-effort, not a byte-for-byte replacement for `_source`. Stored fields preserve the original value best. `doc_values` can sort multi-valued scalars differently from the original JSON order, analyzed text recovered from indexed terms may lose original surface text, and object-array subfields recovered from `doc_values` can only be assigned approximately. Validate representative documents and phrase/proximity queries before widening the migration.

## Coordination and automation
<a name="backfill-coordination-and-automation"></a>
+  `useTargetClusterForWorkCoordination` - controls where RFS stores shard lease and work-assignment metadata. The default is `false`, which deploys a dedicated single-node OpenSearch coordinator cluster for the migration and avoids adding coordination writes to the target. Set it to `true` only when you intentionally want the target cluster to handle coordination. Leave it `false` for Amazon OpenSearch Serverless targets; RFS cannot use Serverless as the coordination store.
+  `coordinatorRetryMaxRetries`, `coordinatorRetryInitialDelayMs`, and `coordinatorRetryMaxDelayMs` - expert controls for retrying coordinator updates, such as marking a shard work item complete. The defaults are 7 retries, 1000 ms initial delay, and 64000 ms maximum delay. These affect coordinator write retries, not target bulk indexing retries.
+  `skipApproval` - skips the manual approval gate after document backfill completes. Use this for automated pipelines only when your validation and rollback path are already defined.
+  `jvmArgs` - additional JVM arguments for RFS workers.
+  `loggingConfigurationOverrideConfigMap` - ConfigMap name for a custom RFS logging configuration.
+  `otelMetricsCollectorEndpoint` and `otelTraceCollectorEndpoint` - OpenTelemetry collector endpoints for RFS workers. Metrics default to `http://otel-collector:4317`; set the metrics endpoint to an empty string to disable metrics export. Trace export is disabled unless you configure a trace endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
