---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/migrate-metadata.html
---

# Migrate metadata
<a name="migrate-metadata"></a>

Metadata migration shapes the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection so that it can accept the incoming documents and traffic. It moves index settings, index mappings, legacy and composable index templates, component templates, and aliases from the source cluster to the target before document backfill or traffic replay becomes meaningful.

In the workflow model, metadata migration is a configured phase inside the migration workflow rather than a separate manual tool run. When a `metadataMigrationConfig` is present in your workflow configuration, the workflow runs two logical steps:
+  `evaluateMetadata` — scans the source, applies your filtering and transformations, and reports what *would* be migrated. Nothing is written to the target.
+  `migrateMetadata` — applies the evaluated items to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

If approval gates are enabled, the workflow pauses between these two steps so you can inspect the evaluation result before any change is written. The metadata migration tool gathers information from the source through a snapshot or through HTTP requests, and the snapshots it uses are fully compatible with the Reindex-from-Snapshot (RFS) backfill phase. For how to create the source snapshot, see [Creating a snapshot](creating-a-snapshot.md).

In workflow runs, metadata evaluation and migration reports are stored as managed output artifacts on the `SnapshotMigration` resource. Use `workflow manage` and **Show Output**, or use `workflow show --list` followed by `workflow show snapshotmigration.<NAME> evaluatemetadata` or `workflow show snapshotmigration.<NAME> migratemetadata`, to review those reports before approving the next gate.

The `console metadata` commands described in this section run the same logic outside the workflow. Reach for them when you want to preview or apply metadata manually during validation or troubleshooting.

## What metadata migration covers
<a name="meta-scope"></a>

Metadata migration handles the following:
+ index settings,
+ index mappings,
+ legacy and composable index templates,
+ component templates, and
+ aliases.

It also applies built-in transformations to reconcile version-specific behavior between the source and the target. See [Built-in transformations](#meta-builtin-transforms).

Plan separate work for the following — these are **not** migrated automatically:
+ security configuration,
+ Index State Management (ISM) and Index Lifecycle Management (ILM) policies,
+ ingest pipelines,
+ OpenSearch Dashboards or Kibana saved objects,
+ data streams, and
+ cluster-level tuning.

For data streams, this means metadata migration does not create the target data stream, data-stream template, or backing-index structure. If you need to backfill documents that are stored in source `.ds-*` backing indexes, prepare the target data stream separately and configure RFS as described in [Backfilling data stream documents](backfill-tuning.md#backfill-data-streams).

## Evaluate metadata
<a name="meta-evaluate"></a>

Before migrating, preview what will be migrated. In the workflow, this is the `evaluateMetadata` step. To run it manually from the Migration Console pod:

```
console metadata evaluate
```

This scans the source cluster, applies filtering and modifications, and produces a list of items that will be migrated. Items not listed will not be migrated. Use this as a safety check before modifying the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

Example output:

```
Starting Metadata Evaluation
Clusters:
   Source:
      Remote Cluster: OpenSearch 1.3.16

   Target:
      Remote Cluster: OpenSearch 2.14.0

Migration Candidates:
   Index Templates:
      simple_index_template

   Component Templates:
      simple_component_template

   Indexes:
      blog_2023, movies_2023

   Aliases:
      alias1, movies-alias

Results:
   0 issue(s) detected
```

## Run metadata migration
<a name="meta-migrate"></a>

The migrate step applies all evaluated items to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. In the workflow, this is the `migrateMetadata` step. To run it manually:

```
console metadata migrate
```

If you run the workflow more than once, target indexes that already exist are reported as non-fatal so workflow reconciliation can rerun safely. For manual `console metadata migrate` runs, pass `--allow-existing-indexes true` when you want the same idempotent behavior; otherwise, an existing target index is treated as a fatal error. To re-migrate an item with changed metadata, delete it from the target first, then rerun evaluate and migrate.

Example output:

```
Starting Metadata Migration

Clusters:
   Source:
      Snapshot: OpenSearch 1.3.16

   Target:
      Remote Cluster: OpenSearch 2.14.0

Migrated Items:
   Index Templates:
      simple_index_template

   Component Templates:
      simple_component_template

   Indexes:
      blog_2023, movies_2023

   Aliases:
      alias1, movies-alias

Results:
   0 issue(s) detected
```

## Filter what gets migrated
<a name="meta-filter"></a>

Use allowlists in your workflow configuration to scope metadata migration. During a pilot, restrict the run to a small set of indexes, then widen to the full set for the real migration:
+  `indexAllowlist` — for Elasticsearch and OpenSearch snapshots, exact index names or regular-expression patterns prefixed with `regex:`. For Apache Solr backups, exact collection or core names only. An empty list migrates all eligible non-system indexes from the snapshot, or all discovered Solr collections and cores in the backup.
+  `indexTemplateAllowlist` — exact index template names or regular-expression patterns prefixed with `regex:`. An empty list migrates all eligible non-system index templates.
+  `componentTemplateAllowlist` — exact component template names or regular-expression patterns prefixed with `regex:`. An empty list migrates all eligible non-system component templates.

For Elasticsearch and OpenSearch `regex:` entries, the pattern must match the entire name. Use expressions such as `regex:logs-. ` for prefixes or `regex:.` for suffixes; `regex:logs` matches only the exact string `logs`. Solr collection and core allowlists do not use `regex:` patterns.

These metadata allowlists are evaluated client-side after the snapshot has been taken. To exclude indices from the snapshot itself, configure the snapshot `indexAllowlist` in `createSnapshotConfig`; that field uses the source cluster’s native snapshot index-expression syntax rather than `regex:` patterns.

Other useful `metadataMigrationConfig` settings include:
+  `allowLooseVersionMatching` — allows migration between non-identical but compatible source and target versions. The default is `true`.
+  `clusterAwarenessAttributes` — number of shard allocation awareness attributes to preserve when rewriting index settings. The default is `1`.
+  `output` — evaluation report format. Use `HUMAN_READABLE` for interactive review or `JSON` for automation.
+  `skipEvaluateApproval` and `skipMigrateApproval` — skip the workflow approval gates after evaluation or migration. Use these only when your review and rollback path are already automated.
+  `jvmArgs` and `loggingConfigurationOverrideConfigMap` — JVM and logging overrides for metadata migration pods.
+  `otelMetricsCollectorEndpoint` and `otelTraceCollectorEndpoint` — OpenTelemetry collector endpoints for metadata migration pods. Metrics default to `http://otel-collector:4317`; set the metrics endpoint to an empty string to disable metrics export. Trace export is disabled unless you configure a trace endpoint.

## Sourceless metadata evaluation
<a name="meta-sourceless"></a>

If a selected source index has `_source` disabled or partially filtered, metadata evaluation fails by default because document backfill cannot read a complete `_source` document. To opt in to sourceless migration, set `enableSourcelessMigrations` in both `metadataMigrationConfig` and `documentBackfillConfig`. This tells metadata evaluation to permit those indices and tells RFS to reconstruct documents from stored fields, `doc_values`, Lucene point values, indexed terms, and mapping-level constant values. RFS also strips `copy_to` target fields from reconstructed `_source` and can sometimes reverse-derive a missing source field from a less-lossy `copy_to` target.

If reconstruction from stored fields and `doc_values` is not sufficient, RFS can treat `_recovery_source` as `_source` when it exists in Elasticsearch 7 or OpenSearch snapshots with soft deletes. Configure that behavior with `documentBackfillConfig.useRecoverySource`. The metadata migration CLI accepts `--use-recovery-source` and the workflow schema accepts `metadataMigrationConfig.useRecoverySource` for parity with document backfill configuration, but metadata evaluation does not read document bodies and does not use `_recovery_source`. The field is transient and may not exist for every document, so use it only after validating representative documents.

The approval gates are the right place to decide whether this is acceptable for your data model. Stored fields are the closest replacement for `_source`; `doc_values` and indexed terms can change multi-value ordering, analyzed text surface form, and object-array field association.

## Verify metadata
<a name="meta-verify"></a>

Before proceeding to backfill, confirm the target details. Depending on your configuration, check the sharding strategy or verify that index mappings are correctly defined:

```
console clusters curl target /<index>/_mapping?pretty
console clusters curl target /<index>/_settings?pretty
```

## Built-in transformations
<a name="meta-builtin-transforms"></a>

When you migrate between major versions, some field types and index structures are deprecated, removed, or renamed. Migration Assistant applies built-in transformations automatically so that source definitions land in a shape the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection accepts.

| Transformation | What it does |
| --- | --- |
| Type mappings | Reconciles indexes that declare multiple mapping types (Elasticsearch versions before 7.0) into the single-type model that OpenSearch uses. See [Transform type mappings](transform-type-mappings.md). |
|  `string` to `text` and `keyword`  | Converts the deprecated `string` type (Elasticsearch 1.x–5.x) to `text` or `keyword` based on the original `index` property. See [Transform string fields to text and keyword](transform-string-text-keyword.md). |
|  `flattened` to `flat_object`  | Converts the `flattened` field type (Elasticsearch 7.3 and later) to `flat_object` (OpenSearch 2.7 and later). See [Transform flattened fields to flat\_object](transform-flattened-flat-object.md). |
|  `dense_vector` to `knn_vector`  | Converts the `dense_vector` field type (Elasticsearch 7.x) to `knn_vector` with appropriate similarity mappings and HNSW algorithm parameters. See [Transform dense\_vector fields to knn\_vector](transform-dense-vector-knn.md). |
| k-NN vector compatibility | Lifts legacy `index.knn.*` build parameters into field-level method configuration, converts `nmslib` engines to `faiss` for OpenSearch 3.x targets, and rewrites incompatible `knn_vector` definitions to Faiss HNSW for Amazon OpenSearch Serverless NextGen. |
| Analysis component compatibility | Strips or renames analyzer, tokenizer, char-filter, and token-filter names that the target version rejects, including direct Solr camelCase to OpenSearch snake\_case equivalents when available. |

For field types that the built-in transformations do not cover, you can supply a custom transformer. See [Transform field types](transform-field-types.md).

**Important**
Whenever you change the transformation configuration for a workflow-managed run, edit the workflow configuration and resubmit the workflow so the metadata migration, backfill, and replay phases use the same transformer settings. Previously migrated data and metadata may need to be cleared first to avoid an inconsistent state on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

## Troubleshoot metadata migration
<a name="meta-troubleshooting"></a>

### Access detailed logs
<a name="meta-logs"></a>

For workflow-managed metadata migrations on Amazon EKS, use the workflow logs and managed output artifacts instead of looking for files on the Migration Console filesystem:

```
workflow log resource snapshotmigration.<NAME> -- --tail=200
workflow show snapshotmigration.<NAME> evaluatemetadata
workflow show snapshotmigration.<NAME> migratemetadata
```

Use `workflow log resource --list` and `workflow show --list` if you need the exact `snapshotmigration.<NAME>` resource name.

### Amazon OpenSearch Service running in compatibility mode
<a name="meta-compatibility-mode"></a>

If you encounter an error about being unable to update an Elasticsearch 7.10.2 cluster, compatibility mode may be enabled on the Amazon OpenSearch Service domain. Disable compatibility mode to continue. See [Enable compatibility mode](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-upgrade) in the *Amazon OpenSearch Service Developer Guide*.

For broader diagnosis, see [Troubleshooting](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
