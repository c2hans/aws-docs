---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-considerations.html
---

# Considerations and limitations for maintenance jobs
<a name="s3-tables-considerations"></a>

Amazon S3 offers maintenance operations to enhance the performance of your S3 tables or table buckets. These options are file compaction, snapshot management, and unreferenced file removal. The following are limitations and consideration for these management options.

**Topics**
+ [Considerations for compaction](#s3-tables-compaction-considerations)
+ [Considerations for snapshot management](#s3-tables-snapshot-considerations)
+ [Considerations for unreferenced file removal](#s3-tables-unreferenced-file-removal-considerations)
+ [S3 table and table buckets maintenance operations limits and related APIs](#s3-tables-maintenance-limits)

## Considerations for compaction
<a name="s3-tables-compaction-considerations"></a>

The following considerations apply to compaction. For more information about compaction, see [Maintenance for tables](s3-tables-maintenance.md).
+ Compaction is supported on Apache Parquet, Avro, and ORC file types.
+ Compaction writes new files in Apache Parquet format by default. To compact files into Avro or ORC formats instead, set the `write.format.default` table property to `avro` or `orc`.
+ Compaction doesn’t support data type: `Fixed`.
+ Compaction doesn’t support compression types: `brotli`, `lz4`.
+ Compaction occurs on an automated schedule. If you want to prevent charges associated with compaction you can manually disable it for a table using the [PutTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableMaintenanceConfiguration.html) API operation.

**Note**
Apache Iceberg uses an optimistic concurrency model along with conflict detection to arbitrate write transactions. With optimistic concurrency, user and compaction transactions can conflict causing transactions to fail. If conflicts occur, compaction jobs will retry on failure. It is recommended that your pipelines also use retry logic to overcome transactions that fail from conflicting operations.

## Considerations for snapshot management
<a name="s3-tables-snapshot-considerations"></a>

The following considerations apply to snapshot management. For more information about snapshot management, see [Maintenance for tables](s3-tables-maintenance.md).
+ Snapshots will be preserved only when both criteria are satisfied: the minimum number of snapshots to keep and the specified retention period.
+ Snapshot management deletes expired snapshot metadata from Apache Iceberg, preventing time travel queries for expired snapshots and optionally deleting associated data files.
+ Snapshot management does not support retention values you configure as Iceberg table properties in the `metadata.json` file or through an `ALTER TABLE SET TBLPROPERTIES` SQL command, including branch or tag-based retention. Snapshot management is disabled when you configure a branch or tag-based retention policy, or configure a retention policy on the `metadata.json` file that is longer than the values configured through the `PutTableMaintenanceConfiguration` API. In these cases S3 will not expire or remove snapshots and you will need to manually delete snapshots or remove the properties from your Iceberg table to avoid storage charges.

## Considerations for unreferenced file removal
<a name="s3-tables-unreferenced-file-removal-considerations"></a>

The following considerations apply to unreferenced file removal. For more information about unreferenced file removal, see [Maintenance for table buckets](s3-table-buckets-maintenance.md).
+ Unreferenced file removal deletes data and metadata files that are no longer referenced by Iceberg metadata if their creation time is before the retention period.

## S3 table and table buckets maintenance operations limits and related APIs
<a name="s3-tables-maintenance-limits"></a>

| Maintenance operation | Property | Configurable at table bucket level? | Configurable at table level? | Default value | Minimum value | Related Iceberg maintenance routine | Controlling S3 Tables API |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Compaction | targetFileSizeMB | No | Yes | 512MB | 64MB | [https://iceberg.apache.org/docs/latest/maintenance/#compact-data-files](https://iceberg.apache.org/docs/latest/maintenance/#compact-data-files) | [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html) |
| Snapshot management | minimumSnapshots | No | Yes | 1 | 1 | [https://iceberg.apache.org/docs/latest/maintenance/#expire-snapshots](https://iceberg.apache.org/docs/latest/maintenance/#expire-snapshots) retainLast | [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html) |
| Snapshot management | maximumSnapshotAge | No | Yes | 120 hours | 1 hour | [https://iceberg.apache.org/docs/latest/maintenance/#expire-snapshots](https://iceberg.apache.org/docs/latest/maintenance/#expire-snapshots) expireOlderThan | [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableMaintenanceConfiguration.html) |
| Unreferenced file removal | unreferencedDays | Yes | No | 3 days | 1 days | [https://iceberg.apache.org/docs/latest/maintenance/#delete-orphan-files](https://iceberg.apache.org/docs/latest/maintenance/#delete-orphan-files) | [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableBucketMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableBucketMaintenanceConfiguration.html) |
| Unreferenced file removal | nonCurrentDays | Yes | No | 10 days | 1 days | N/A | [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableBucketMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3tables_PutTableBucketMaintenanceConfiguration.html) |

**Note**
S3 Tables applies the parquets row-group-default size of 128 MB.
