---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/running-backfill.html
---

# Running backfill
<a name="running-backfill"></a>

After metadata has been migrated, use Reindex-from-Snapshot (RFS) to backfill documents from the source cluster snapshot into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

## Starting the backfill
<a name="start-backfill"></a>

Configure RFS under `snapshotMigrationConfigs[].perSnapshotConfig.<snapshot>[].documentBackfillConfig` and submit the workflow:

```
workflow configure edit
workflow submit
workflow manage
```

The workflow creates a `SnapshotMigration` resource for each configured snapshot migration. If `documentBackfillConfig` is present, the workflow starts RFS after snapshot and metadata dependencies are ready. If `documentBackfillConfig` is omitted, that migration pass skips document backfill.

The legacy `console backfill start` command starts a directly configured RFS deployment outside the workflow.

## Scaling the backfill
<a name="scale-backfill"></a>

To speed up workflow-managed backfill, increase `documentBackfillConfig.podReplicas` and resubmit the workflow. Each worker processes shards in parallel from the snapshot in Amazon S3, so scaling up does not add live read load to the source cluster — it only increases the indexing rate on the target.

```
documentBackfillConfig:
  podReplicas: 5
```

```
workflow configure edit
workflow submit
```

For a legacy directly configured RFS deployment, use:

```
console backfill scale 5
```

It may take a few minutes for additional workers to come online. Scale up gradually while monitoring the health metrics of the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection to avoid oversaturating it. Amazon OpenSearch Service provides [cluster health and performance metrics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring.html) that you can use for this monitoring.

## Monitoring the backfill
<a name="monitor-backfill"></a>

Check workflow-managed backfill status:

```
workflow status --resource-view
workflow log resource snapshotmigration.<NAME> -- --tail=100
```

Use `workflow manage` for the interactive view and approval gates. Use `workflow log resource --list` to find the exact `snapshotmigration.<NAME>` resource name.

For a legacy directly configured RFS deployment, use:

```
console backfill status
console backfill status --deep-check
```

Example output:

```
BackfillStatus.RUNNING
Running=9
Pending=1
Desired=10
Shards total: 62
Shards completed: 46
Shards incomplete: 16
Shards in progress: 11
Shards unclaimed: 5
```

## Amazon CloudWatch metrics and dashboard
<a name="backfill-cloudwatch"></a>

Migration Assistant creates two Amazon CloudWatch dashboards to visualize migration health and performance:
+  `MA-<STAGE>-<REGION>-ReindexFromSnapshot` — metrics for the RFS workers and, for Amazon OpenSearch Service targets, the domain’s cluster metrics.
+  `MA-<STAGE>-<REGION>-CaptureReplay` — metrics for the capture proxy and traffic replayer.

Replace `<STAGE>` and `<REGION>` with the values you used during deployment (for example, `MA-prod-us-east-1-ReindexFromSnapshot`).

Find the dashboards in the Amazon CloudWatch console in the AWS Region where you deployed Migration Assistant. The metric graphs for your target domain are blank until you select the Amazon OpenSearch Service domain you are migrating to from the dropdown menu at the top of the dashboard.

## Pausing the backfill
<a name="pause-backfill"></a>

The workflow path does not expose a separate `workflow backfill pause` command. To reduce or pause worker activity for a workflow-managed backfill, lower `documentBackfillConfig.podReplicas` and resubmit the workflow after considering whether the current run is actively writing to the target.

For a legacy directly configured RFS deployment, use:

```
console backfill pause
```

This stops all existing legacy workers while leaving the backfill operation in a resumable state. To restart:
+ Run `console backfill start`, or
+ Scale up the worker count with `console backfill scale <NUM_WORKERS>`.

## Stopping the backfill
<a name="stop-backfill"></a>

Workflow-managed backfill does not require a manual `console backfill stop`. The workflow’s RFS completion monitor marks the `SnapshotMigration` resource complete after the eligible shard work is finished, then the workflow proceeds to the next gate or dependent phase.

For a legacy directly configured RFS deployment, stop the migration only after status checks report that data has been completely migrated:

```
console backfill stop
```

Example output:

```
Backfill stopped successfully.
Archiving the working state of the backfill operation...
Backfill working state archived to: ./backfill_working_state/working_state_backup_20241115174822.json
```

**Warning**
You cannot restart a stopped legacy RFS migration. If you may need to resume later, use `console backfill pause` instead.

## Validating the backfill
<a name="validate-backfill"></a>

After the backfill completes and workers have stopped, verify the contents of your Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection:

```
console clusters cat-indices --refresh
```

This displays the document count for each index. Compare source and target counts to verify completeness:

```
SOURCE CLUSTER
health status index       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   my-index    -DqPQDrATw25hhe5Ss34bQ   1   0          3            0     12.7kb         12.7kb

TARGET CLUSTER
health status index       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   my-index    bGfGtYoeSU6U6p8leR5NAQ   1   0          3            0      5.5kb          5.5kb
```

### Verifying no failed documents
<a name="verify-failed-documents"></a>

Use the following Amazon CloudWatch Logs Insights query to identify failed documents:

```
fields @message
| filter @message like "Bulk request succeeded, but some operations failed."
| sort @timestamp desc
| limit 10000
```

Run this query against the Migration Assistant application log group `/migration-assistant-<STAGE>-<REGION>/logs` in Amazon CloudWatch. If failed documents are identified, you can index them directly rather than re-running the full backfill.
