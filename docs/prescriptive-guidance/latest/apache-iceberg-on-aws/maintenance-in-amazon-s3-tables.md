---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/maintenance-in-amazon-s3-tables.html
---

# Maintenance in Amazon S3 Tables

Amazon S3 Tables performs table maintenance for you. Compaction, snapshot expiration, and unreferenced-file removal all run automatically for every table in a table bucket — there is no code to author, no schedule to configure, and no `OPTIMIZE` or `VACUUM` procedure to invoke. See [Table maintenance in Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html) for the full service description.

The defaults are chosen to work well for typical analytics workloads. If you need different behavior for a specific table, you can override the defaults per table with the `PutTableMaintenanceConfiguration` API call.

## Configurable parameters and defaults
<a name="configurable-parameters-and-defaults"></a>

|
|
| **Parameter** | **Applies to** | **Scope** | **Purpose** | **Default** |
| --- |--- |--- |--- |--- |
| `minSnapshotsToKeep` | Snapshot expiration | Per table | Minimum number of most-recent snapshots to keep, even if older than `maxSnapshotAgeHours`. Minimum: **1** | **1** |
| `maxSnapshotAgeHours` | Snapshot expiration | Per table | Snapshots older than this are eligible for expiration. Minimum: **1** hour | **120** (5 days) |
| `targetFileSizeMB` | Compaction | Per table | Target size for compacted output files. Valid range: **64 to 512** MB | **512** MB |
| Compaction strategy | Compaction | Per table | `auto` (default; uses `sort` when the table has a sort order, otherwise `binpack`), `binpack`, `sort`, or `z-order`. `sort` and `z-order` require a sort order on the table and the `s3tables:GetTableData` permission | `auto` |
| `unreferencedDays` | Unreferenced-file removal | Per bucket | Files unreferenced for this many days are removed by the built-in unreferenced-file cleanup | **3** |
| `nonCurrentDays` | Unreferenced-file removal | Per bucket | Number of days a file is kept after the last snapshot that referenced it expires, before it is permanently deleted. During this window the file can be recovered only through AWS Support. After `nonCurrentDays`, the deletion is permanent and unrecoverable | **10** |

**Notes**:
+ In compaction strategy, `auto` follows the table's sort order, so setting one with `ALTER TABLE mydb.orders WRITE ORDERED BY customer_id` switches compaction to `sort` without further configuration. To force a strategy, or to use Z-order, set it explicitly (sample code below). Note that `sort` and `z-order` compaction cost more than `binpack`: they reorder the data as well as merging files, and S3 Tables bills the bytes they process at a higher rate.

```
aws s3tables put-table-maintenance-configuration \
--table-bucket-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name> \
--namespace sales \
--name orders \
--type icebergCompaction \
--value '{"status":"enabled","settings":{"icebergCompaction":{"strategy":"z-order"}}}'
```
+ `unreferencedDays` is a *per bucket* setting (all tables in the same table bucket share the same value), whereas the snapshot and compaction parameters are *per table*.
+ Lowering `maxSnapshotAgeHours` reduces the storage held by historical snapshots but also shortens the time travel window available for reads and rollbacks. Set it in line with your recovery-point objective.
+ Expiring a snapshot does not free storage immediately: its files become noncurrent and are deleted after `nonCurrentDays`. With the defaults, a file that only an old snapshot references is retained for 5 days (`maxSnapshotAgeHours`) plus 10 days (`nonCurrentDays`).

## Example — override defaults for a table
<a name="example-override-defaults-for-a-table"></a>

Using the AWS CLI to keep 3 snapshots for 30 days and compact 512MB files:

```
aws s3tables put-table-maintenance-configuration \
    --table-bucket-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name> \
    --namespace sales \
    --name orders \
    --type icebergSnapshotManagement \
    --value '{"status":"enabled","settings":{"icebergSnapshotManagement":{"minSnapshotsToKeep":3,"maxSnapshotAgeHours":720}}}'

aws s3tables put-table-maintenance-configuration \
    --table-bucket-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name> \
    --namespace sales \
    --name orders \
    --type icebergCompaction \
    --value '{"status":"enabled","settings":{"icebergCompaction":{"targetFileSizeMB":512}}}'
```

## What disables built-in snapshot management
<a name="what-disables-built-in-snapshot-management"></a>

Amazon S3 Tables reads snapshot retention only from the maintenance configuration set through `PutTableMaintenanceConfiguration`. It does not read Iceberg's own retention settings, and two conditions make the snapshot management job fail for the entire table, after which no snapshots are expired and no files are released:
+ **User-defined tags or branches** — if any tag or branch other than `main` exists on the table, snapshot management fails, even when the tag or branch has a short retention period. This includes tags created for point-in-time retention (see [Optimizing storage](best-practices-storage.md)).
+ **Iceberg retention table properties** — if `history.expire.max-snapshot-age-ms` or `history.expire.min-snapshots-to-keep` is set on the table, snapshot management fails regardless of the value. Remove them with:

  ```
  ALTER TABLE mydb.orders UNSET TBLPROPERTIES ('history.expire.max-snapshot-age-ms', 'history.expire.min-snapshots-to-keep')
  ```
+ **gc.enabled set to false** — if the Iceberg table property gc.enabled is set to false, both snapshot management and unreferenced-file removal fail for the table. Ensure this property is unset or explicitly set to true.

## Turning it off (fall back to self-managed maintenance)
<a name="turning-it-off-fall-back-to-spark-procedures"></a>

Each of the three built-in maintenance activities can be disabled by setting `status` to `disabled` on its configuration, but the API differs by scope:
+ **Compaction (**`icebergCompaction`**) and snapshot expiration (**`icebergSnapshotManagement`**)** are table-scoped and configured through `PutTableMaintenanceConfiguration`.
+ **Unreferenced-file removal (**`icebergUnreferencedFileRemoval`**)** is table-bucket-scoped and configured through `PutTableBucketMaintenanceConfiguration`.

For example, to disable compaction on a single table:

```
aws s3tables put-table-maintenance-configuration \
    --table-bucket-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name> \
    --namespace sales \
    --name orders \
    --type icebergCompaction \
    --value '{"status":"disabled"}'
```

If you disable one or more of the built-in activities, you can fall back to running the equivalent Iceberg system procedures yourself from Spark — see [Self-managed maintenance](self-managed-maintenance.md) for `rewrite_data_files`, `expire_snapshots`, and `remove_orphan_files`. Because S3 Tables tables are still ordinary Iceberg tables underneath, the same procedures work when invoked through a Spark session configured against the S3 Tables catalog (see [Amazon S3 Tables catalog configuration on Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) or [on AWS Glue](iceberg-glue.md)).

It's also fine to mix the two — for example, keep the built-in snapshot expiration and unreferenced-file removal enabled on S3 Tables, and disable only compaction so you can run `rewrite_data_files` yourself from Spark (with custom targets, filters, or a specific schedule).

## Observability
<a name="observability"></a>

Amazon S3 Tables publishes CloudWatch metrics in the AWS/S3/Tables namespace:
+ **Daily storage metrics** — bytes per access tier and file counts at the table bucket, namespace, and table level.
+ **Daily compaction metrics** — CompactionBytesProcessed and CompactionObjectsCount.
+ **Request metrics (optional**) — per-minute operation counts, bytes, latency, and error rates. These are billed as custom CloudWatch metrics.

**Snapshot management** and **unreferenced-file** removal have no CloudWatch metrics. To confirm they are running and catch failures (caused by tags, branches, or `history.expire.*` properties), use:

`aws s3tables get-table-maintenance-job-status`

This returns the status, last run time, and failure cause for each maintenance type. Also review maintenance events in AWS CloudTrail. A falling daily file count for a table is the indirect CloudWatch signal that compaction and file removal are working. For the metric list, see [Metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-metrics-dimensions.html).
