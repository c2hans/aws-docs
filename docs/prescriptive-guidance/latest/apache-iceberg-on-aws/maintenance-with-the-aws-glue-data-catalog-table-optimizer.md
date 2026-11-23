---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/maintenance-with-the-aws-glue-data-catalog-table-optimizer.html
---

# Maintenance with the AWS Glue Data Catalog table optimizer

For self-managed Iceberg tables that are registered in the AWS Glue Data Catalog, you can offload compaction, snapshot expiration, and unreferenced-file deletion to the **table optimizer**. Once enabled, the AWS Glue Data Catalog runs the corresponding maintenance jobs on your behalf without any code or scheduler on your side. The optimizer can be configured per table or catalog-wide (so that every new or updated Iceberg table inherits the configuration). See [Optimizing Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/table-optimizers.html) and [Catalog-level table optimizers](https://docs.aws.amazon.com/glue/latest/dg/catalog-level-optimizers.html) in the AWS Glue documentation for setup steps and IAM requirements.

This section documents the customizable parameters, their defaults, and where each optimizer reads its inputs from.

## Compaction optimizer
<a name="compaction-optimizer"></a>

The compaction optimizer merges small data files into larger ones and can apply delete files on merge-on-read tables. It runs continuously: the Data Catalog starts a compaction job for a table or partition when it holds more than `minInputFiles` (default 100) files that are each smaller than 75% of `write.target-file-size-bytes`.

|
|
| **Parameter** | **Purpose** | **Default** |
| --- |--- |--- |
| `strategy` | Rewrite strategy. For `sort` or `z-order` you must also set a table-level sort order (via `ALTER TABLE ... WRITE ORDERED BY ...` or the `sort_order` table property) so the optimizer knows what to sort on | `binpack` |
| `minInputFiles` | Minimum number of small files in a partition before the optimizer triggers a compaction for that partition | `100` |
| `deleteFileThreshold` | On merge-on-read tables, compact a data file if it has at least this many associated delete files | `1` |
| Target file size | Target size for compacted output files. The optimizer reads this from the table property `write.target-file-size-bytes`, so change it there rather than in the optimizer configuration | 512 MB (`write.target-file-size-bytes` default) |

**Notes**:
+ To use the `sort` or `z-order` strategy, set the table's sort order first (for example, `ALTER TABLE mydb.orders WRITE ORDERED BY customer_id`). The optimizer will use that sort order for the rewrite; without a sort order defined on the table, both `sort` and `z-order` fall back to the equivalent of `binpack`.
+ To change the target file size, update the table property: `ALTER TABLE mydb.orders SET TBLPROPERTIES ('write.target-file-size-bytes' = '536870912')`.

## Snapshot retention optimizer
<a name="snapshot-retention-optimizer"></a>

The snapshot retention optimizer runs `expire_snapshots` on a schedule to trim the table history.

|
|
| **Parameter** | **Purpose** | **Default** |
| --- |--- |--- |
| `snapshotRetentionPeriodInDays` | Only expire snapshots older than this many days | If not specified, the optimizer uses (1) the table property `history.expire.max-snapshot-age-ms` if present, otherwise (2) **5 days** |
| `numberOfSnapshotsToRetain` | Minimum number of most-recent snapshots to keep, even if they exceed the retention period | If not specified, the optimizer uses (1) the table property `history.expire.min-snapshots-to-keep` if present, otherwise (2) **1** |
| `runRateInHours` | How often the retention job runs, between **3** and **168** hours | **24** hours |
| `cleanExpiredFiles` | Delete the data and metadata files of expired snapshots. If false, snapshots leave the metadata but their files stay on Amazon S3 as unreferenced files. | true |

**Notes**:
+ You can control the retention policy centrally by setting the table properties `history.expire.max-snapshot-age-ms` and `history.expire.min-snapshots-to-keep` (self-managed tables only; do not set these on tables in Amazon S3 Tables). Any manual Spark `expire_snapshots` invocation will pick up the same values, so the policy stays consistent whether the Data Catalog optimizer or a Spark job is doing the work.
+ Keep at least enough snapshots (or a long enough retention period) to meet your recovery point objective for time travel and rollback.

## Unreferenced files deletion optimizer
<a name="orphan-file-deletion-optimizer"></a>

The unreferenced-files deletion optimizer scans the table's storage location and deletes files that are no longer referenced by any snapshot metadata.

|
|
| **Parameter** | **Purpose** | **Default** |
| --- |--- |--- |
| `orphanFileRetentionPeriodInDays` | Only consider files older than this many days as candidates for deletion (protects concurrent writers) | **3** days |
| `runRateInHours` | How often the unreferenced-files deletion job runs, between **3** and **168** hours | **24** hours |

**Notes**:
+ The retention period is a safety buffer against files that are currently being written but not yet committed. Do not lower it below the maximum realistic duration of a write job against the table.
+ On tables with concurrent writers or with data written outside Iceberg (for example, by a Amazon Data Firehose that lands files then commits), keep the default 3-day retention or increase it further.

## Turning it off (fall back to self-managed maintenance)
<a name="turning-it-off-fall-back-to-spark-procedures"></a>

You can disable any of the three optimizers per table at any time (through the AWS Glue console, AWS CLI, or `UpdateTableOptimizer` API). If you do, you can fall back to running the equivalent Iceberg system procedures yourself — see [Self-managed maintenance](self-managed-maintenance.md). It's also fine to use the optimizer for some activities (for example, compaction and snapshot retention) and run others manually (for example, `remove_orphan_files` on demand from Spark).

## Observability
<a name="observability"></a>

AWS Glue publishes Amazon CloudWatch metrics after each successful optimizer run: bytes and files compacted, DPUs allocated, and job duration for compaction; data files, manifest files, and manifest lists deleted for snapshot retention; files deleted for unreferenced file deletion. To see failed runs and their error messages, use `ListTableOptimizerRuns` or the optimizer history in the AWS Glue console. For the metric list, see [Viewing Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/view-optimization-metrics.html).
