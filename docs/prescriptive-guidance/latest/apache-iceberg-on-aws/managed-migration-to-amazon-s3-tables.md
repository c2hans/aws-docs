---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/managed-migration-to-amazon-s3-tables.html
---

# Managed migration to Amazon S3 Tables

The `s3tables:StartTableMigration` API migrates an AWS Glue Data Catalog **Apache Hive-style table stored as Apache Parquet** in an Amazon S3 general purpose bucket into an Amazon S3 Tables Apache Iceberg table. Amazon S3 runs the migration end to end: no external compute needs to be provisioned, and the source table stays fully available for reads and writes throughout. During a migration, Amazon S3:
+ Runs source compatibility checks during planning and writes two **compatibility reports** to a general purpose S3 bucket that you specify. The **table compatibility report** (a single CSV file) lists issues with the table definition and shows how each column's data type maps to the destination. The **object compatibility report** (a manifest plus CSV files) lists every scanned source object, whether it's included in the migration, and any issue that prevents it from migrating, such as an archived storage class or unsupported encryption. Each finding has a `finding_type` (invalid or informational) and a `finding_category` (access, metadata, data, or internal).
+ Creates the read-only destination Iceberg table and copies the source data into it. Each commit adds an Iceberg snapshot, and queries return the data committed so far.
+ Applies the Hive-to-Iceberg **type conversions**, classifying each column as lossless, widened, converted, incompatible, or unsupported. For example, INT96 timestamps become timestamptz, and digits below a microsecond are dropped. You can let migration infer an Iceberg schema from the AWS Glue table, or specify a destination schema.
+ Applies your **migration policy** to schema mismatches. `unmatchedSourceFieldsPolicy` (`fail` or `drop`) controls source columns that aren't in the destination schema, and `incompatibleValuesPolicy` (`fail` or `setNull`) controls values that can't be converted. Both default to `fail` and can't be changed after the migration starts.
+ **Preserves the source table's partitioning**: the destination S3 Tables table uses **identity partitioning** on the same partition columns as the source. To use a different partition layout (for example, hidden-partition transforms such as *days(ts)* or *bucket(16, id))*, complete the migration first and then evolve the destination table's partition specification.
+ Recompresses data and compacts small files, so the migrated table is query-optimized without post-migration compaction. By default it uses **Zstandard (ZSTD)** and a **target file size of 512 MB**. You can choose zstd, snappy, gzip, or uncompressed, a target file size from 64 to 512 MB, a sort order, snapshot management settings, and Iceberg format version 2 (default) or 3.
+ Writes an **object migration report** when each start or sync finishes. The report lists every attempted source object with a *status* (*succeeded* or *failed*), an *http\_status\_code*, an *error\_code* for failed objects (for example, *sourceAccessDenied* or *schemaIncompatible*), and a *result\_message* describing the transformations applied or how to fix the failure.

**Migration lifecycle:**
+ **States**: each start and sync moves through `new`, `planning` (source enumeration and compatibility checks), optionally `pendingReview`, `queued`, and `migrating` (data copy) to one of the terminal states `succeeded`, `failed`, or `cancelled` (through `cancelling`). You can cancel in the `new`, `planning`, `pendingReview`, `queued`, or `migrating` state. If a migration fails, failureReason in the GetTableMigration response tells you which report or resource to check.
+ **While in progress**, the destination table is **read-only**. Queries against data that has already been committed work, but writes, file compaction, and unreferenced file removal are disabled. Snapshot management stays enabled with the settings you specify at start. Only one start or sync can run on a destination table at a time.
+ **Sync**: after the initial copy you can sync the destination as many times as needed to catch up with later changes in the source. Each sync copies only the objects and partitions that changed since the previous start or sync, removes data for source objects you deleted, and reuses the source, migration policy, and settings from the start. A sync fails any object that was overwritten (re-created with the same name) since the previous start or sync. You also use sync to resume a failed or cancelled migration.
+ **Complete**: completing the migration promotes the destination to **read-write** and turns on automatic table maintenance. Completing can't be undone, and no further migration operations are allowed afterward.

For sources outside managed migration's scope, use [self-managed full data migration](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md) instead. This includes Apache Hudi, Delta Lake, self-managed Apache Iceberg, non-Parquet data, Hive-style ACID (transactional) tables, views, tables registered with AWS Lake Formation, and any source bucket that is not in the same AWS account and Region as the destination table bucket. The managed migration API migrates only external Apache Hive tables stored as Parquet in a general-purpose S3 bucket in the same account and Region as the table bucket. If any of these conditions aren't met, the migration fails or the table can't be registered. See [Migrating existing tables to Iceberg](table-migration.md) for the full decision tree.

**CLI flow**

The following steps run the managed migration end to end from the AWS CLI, following the lifecycle described above: plan with a review pause, approve, monitor until the migration reaches succeeded, optionally sync to pick up later changes in the source, verify, then complete. Each step calls one of the `aws s3tables *-table-migration` commands.

1. **Start the migration** in review mode. Specify the migration role, the destination table, the source AWS Glue table, and where to write the reports. Adding `--review-migration-plan` tells Amazon S3 to plan the migration, write the compatibility reports, and create the empty destination table, and then pause in the pendingReview state instead of copying data. The command returns a migrationId you use for the rest of the flow. Replace `<aws_account_id>` with your AWS Account ID, `arn:aws:iam::<aws_account_id>:role/S3TablesMigrationRole` with the IAM role to be used for the migration, `<aws_region>` with your AWS region, `<table-bucket-name>` with your own table bucket name, `<target_namespace>` with the target namespace in the S3 Tables bucket where to create the target table, `<target_table>` with the target table name, `<source_database>` with the database containing the source table to migrate, `<source_table>` with the source table to migrate and `<bucket-name>` with your own bucket name:

```
aws s3tables start-table-migration \
--role-arn arn:aws:iam::<aws_account_id>:role/S3TablesMigrationRole \
--destination-table '{"tableBucketARN":"arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name>","namespace":"<target_namespace>","name":"<target_table>"}' \
--source-type glueTable \
--source '{"glueTable":{"catalogId":"<aws_account_id>","databaseName":"<source_database>","tableName":"<source_table>"}}' \
--migration-output '{"bucket":"arn:aws:s3:::<bucket-name>","prefixes":{"tableCompatibilityReport":"migration-reports","objectCompatibilityReport":"migration-reports","objectMigrationReport":"migration-reports"}}' \
--review-migration-plan
```

The command returns in output a `<migrationId>`. Omit `--review-migration-plan` to skip the review step and start copying data immediately. When `--review-migration-plan` is set, the migration waits in `pendingReview` and automatically fails if you neither promote it to `queued` nor cancel it within **30 days**. To set a destination schema, compression, or sort order, add `schema` or `properties` to `--destination-table`. To set compaction and snapshot management settings or migration policies, add `--data-migration`, for example:

`--data-migration '{"maintenanceSettings":{"icebergCompaction":{"targetFileSizeMB":128,"strategy":"binpack"},"icebergSnapshotManagement":{"minSnapshotsToKeep":10,"maxSnapshotAgeHours":168}},"migrationPolicies":{"unmatchedSourceFieldsPolicy":"drop","incompatibleValuesPolicy":"setNull"}}'`

1. **(Optional) Review the compatibility reports**, and then approve or cancel the migration. With the migration paused in *pendingReview*, you can inspect the reports and query the empty destination table. Approve to continue by setting the requested state to *queued*, or *cancel* it by setting `--requested-state cancelled`. Replace `<migrationId>` with the one returned by the previous command.

```
aws s3tables update-table-migration \
--migration-id <migrationId> \
--requested-state queued
```

1. **Monitor progress **until the migration reaches the succeeded state. The response includes the state, planning statistics (`planningStats`), migration statistics (`migrationStats`), the location of each report after it's written, and a `failureReason` if the migration fails. Replace `<migrationId>` with the one returned by `start-table-migration`.

```
aws s3tables get-table-migration \
--migration-id <migrationId>
```

1. **(Optional) Sync the target table** to copy any source data that changed since the previous start or sync. Specify the migration role, the destination table ARN, and where to write the reports. Each sync returns a new migrationId that you monitor the same way, and you can add `--review-migration-plan` to review before it copies data. Repeat as needed to validate readers and permissions before cutover. Replace `<aws_account_id>` with your AWS Account ID, `arn:aws:iam::<aws_account_id>:role/S3TablesMigrationRole` with the IAM role to be used for the migration, `arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name>/table/table-id` with the S3 Tables table ARN and `<bucket-name>` with your own bucket name:

```
aws s3tables sync-table-migration \
--role-arn arn:aws:iam::<aws_account_id>:role/S3TablesMigrationRole \
--table-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name>/table/table-id \
--migration-output '{"bucket":"arn:aws:s3:::<bucket-name>","prefixes":{"tableCompatibilityReport":"migration-reports","objectCompatibilityReport":"migration-reports","objectMigrationReport":"migration-reports"}}'
```

1. **Verify the destination table, then complete the migration** to promote it to read-write and turn on automatic table maintenance. This step can't be undone. Replace `arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name>/table/table-id` with the S3 Tables table ARN:

```
aws s3tables complete-table-migration \
--table-arn arn:aws:s3tables:<aws_region>:<aws_account_id>:bucket/<table-bucket-name>/table/table-id
```

For the full list of considerations (IAM permissions, source compatibility rules, report formats, quotas, supported Regions, and data type mappings), see [Migrating tables to Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-migrate.html) in the Amazon S3 documentation.
