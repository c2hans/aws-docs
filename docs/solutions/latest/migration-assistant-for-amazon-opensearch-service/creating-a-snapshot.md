---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/creating-a-snapshot.html
---

# Creating a snapshot
<a name="creating-a-snapshot"></a>

Once you have your change data capture solution in place or have disabled indexing to your source cluster, create a snapshot. The snapshot captures all the metadata and documents to be migrated to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

## Create a snapshot
<a name="create-snapshot-command"></a>

Define the snapshot under `sourceClusters.<source>.snapshotInfo.snapshots` and submit the workflow:

```
workflow configure edit
workflow submit
workflow manage
```

When a snapshot entry uses `createSnapshotConfig`, the workflow creates the source snapshot before metadata migration and document backfill that depend on it. Migration Assistant generates the concrete snapshot name from the source label, the snapshot entry key or `snapshotPrefix`, and the workflow run value. Alternatively, configure an existing snapshot by using `externallyManagedSnapshotName` for that snapshot entry.

The legacy `console snapshot create` command starts a manually configured snapshot outside the workflow. Use it only for direct component operation or troubleshooting.

## Snapshot configuration
<a name="snapshot-configuration"></a>

Snapshot creation settings are configured under `createSnapshotConfig` for the snapshot entry in `sourceClusters.<source>.snapshotInfo.snapshots.<snapshot>.config`. These settings affect what is written into the snapshot and therefore constrain every later migration phase that reads from it.
+  `indexAllowlist` - filters indices at snapshot creation time. This field uses the source cluster’s native `_snapshot` index expression syntax, not the `regex:` syntax used by metadata migration and RFS. Use exact names such as `orders-2026`, wildcards such as `orders- `, and leading `-` exclusions such as `-orders-archive-`. Indices excluded here are not present in the snapshot and cannot be recovered by metadata migration or RFS.
+  `snapshotPrefix` - middle component for auto-generated snapshot names. Generated names include the source label, this component, and a unique run value: `<sourceLabel>_<snapshotPrefix>_<uniqueId>`. When omitted or empty, Migration Assistant uses the snapshot entry key, such as `snap1`, as the middle component.
+  `maxSnapshotRateMbPerNode` - maximum snapshot throughput in MB/s per source data node. The default `0` means no Migration Assistant rate limit. Lower it if snapshot creation is affecting source cluster I/O; raise it gradually if the source cluster and repository can handle more throughput.
+  `includeGlobalState` - includes cluster global state such as persistent settings and templates in the snapshot. The default is `true`. Disable it only when metadata migration hits template or global-state issues that cannot be resolved with metadata allowlists.
+  `compressionEnabled` - enables compressed snapshot metadata. Leave this `false` for Elasticsearch 1.x sources because the snapshot reader does not support compressed snapshot metadata for that version.
+  `jvmArgs` - additional JVM arguments for the snapshot creation pod.
+  `loggingConfigurationOverrideConfigMap` - ConfigMap name for a custom snapshot creation logging configuration.
+  `otelMetricsCollectorEndpoint` and `otelTraceCollectorEndpoint` - optional OpenTelemetry collector endpoints for the snapshot creation pod. Metrics default to `http://otel-collector:4317`; set the metrics endpoint to an empty string to disable metrics export. Trace export is disabled unless you configure a trace endpoint.

Repository settings are configured under `sourceClusters.<source>.snapshotInfo.repos.<repoName>`:
+  `awsRegion` - AWS Region of the Amazon S3 bucket.
+  `s3RepoPathUri` - repository base URI in the form `s3://<BUCKET>/<OPTIONAL_PATH>`.
+  `s3RoleArn` - IAM role ARN the source cluster assumes to write snapshots to Amazon S3. Workflow validation requires this when the source uses SigV4 authentication and `createSnapshotConfig`. Leave it empty only for source clusters that use their own S3 permissions and do not need a role passed during repository registration.
+  `endpoint` - optional custom S3 endpoint, primarily for LocalStack or nonstandard S3-compatible environments. The workflow schema accepts `http://`, `https://`, `localstack://`, and `localstacks://` endpoint forms; LocalStack endpoints are resolved during workflow configuration transformation.

If one source creates multiple snapshots, `sourceClusters.<source>.snapshotInfo.serializeSnapshotCreation` controls whether those snapshot creation steps run one at a time or in parallel. When omitted, the workflow serializes snapshot creation for legacy sources (`ES 1.x` through `ES 7.x` and `OS 1.x`) and allows parallel creation for other source versions, including Solr. Set it to `true` when the source cluster, Solr deployment, or storage tier only supports one snapshot or backup operation at a time for the selected indices or collections.

**Important**
Snapshot `indexAllowlist` is the earliest and most restrictive filter. Use metadata migration and RFS allowlists when you want a reversible pilot scope, because those filters run client-side against indices that are already present in the snapshot.

## Check snapshot status
<a name="check-snapshot-status"></a>

To check workflow-managed snapshot creation status:

```
workflow status --resource-view
workflow log resource datasnapshot.<NAME> -- --tail=100
```

Use `workflow log resource --list` to find the exact `datasnapshot.<NAME>` resource name. The resource view shows the snapshot resource phase and the current snapshot creation status when the workflow has status details from the source cluster.

For a legacy manually configured snapshot, use:

```
console snapshot status
console snapshot status --deep-check
```

Wait for snapshot creation to complete before document backfill starts. A completed manual snapshot status returns output similar to:

```
SUCCESS
Snapshot is SUCCESS.
Percent completed: 100.00%
Data GiB done: 29.211/29.211
Total shards: 40
Successful shards: 40
Failed shards: 0
Start time: 2024-07-22 18:21:42
Duration: 0h 13m 4s
Anticipated duration remaining: 0h 0m 0s
Throughput: 38.13 MiB/sec
```

## Managing slow snapshot speeds
<a name="managing-snapshot-speed"></a>

Depending on the data size in the source cluster and the bandwidth allocated for snapshots, the process can take some time. Set `createSnapshotConfig.maxSnapshotRateMbPerNode` in the workflow configuration, or use the `--max-snapshot-rate-mb-per-node` option for a manual snapshot command, to adjust the maximum rate at which the source cluster’s nodes create the snapshot. Increasing the snapshot rate consumes more source node resources, which may affect the cluster’s ability to handle normal traffic.
