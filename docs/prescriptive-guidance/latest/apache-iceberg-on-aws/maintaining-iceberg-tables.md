---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/maintaining-iceberg-tables.html
---

# Maintaining Iceberg tables

An Iceberg table needs periodic maintenance to keep query performance high and storage costs low. Three maintenance activities cover most of the workload:
+ **Compaction** — merge many small data files into fewer larger ones (and, on tables that use merge-on-read, apply delete files into the corresponding data files).
+ **Snapshot expiration** — remove old snapshots from the table history, which allows the physical data files that only those snapshots referenced to be deleted.
+ **Unreferenced file removal** — scan the table's storage location for files that are no longer referenced by any snapshot metadata and delete them. These typically come from failed writes or from data written outside the Iceberg APIs.

On AWS you have three ways to run these three activities:

1. [**Self-managed maintenance**](self-managed-maintenance.md) — call the Iceberg `rewrite_data_files`, `expire_snapshots`, and `remove_orphan_files` system procedures on a schedule (from Amazon EMR, AWS Glue, or any Spark environment). Gives you the finest control over parameters and scheduling. Also applies to Athena via `OPTIMIZE` / `VACUUM`.

1. [**AWS Glue Data Catalog table optimizer**](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) — a managed feature of the AWS Glue Data Catalog that runs compaction, snapshot retention, and unreferenced-files deletion for Iceberg tables in the same account and Region registered in the catalog. You configure a small set of parameters per table (or catalog-wide) and AWS runs the maintenance for you. Applies to self-managed Iceberg tables that are cataloged in Glue.

1. [**Amazon S3 Tables built-in maintenance**](maintenance-in-amazon-s3-tables.md) — automatic maintenance for tables hosted in an S3 table bucket. Compaction, snapshot expiration, and unreferenced-file removal run continuously with no code and no schedule to author. Keep in mind that snapshot management fails for a table in S3 Tables that has user-defined tags or branches or the `history.expire.*` table properties; see [Maintenance in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md) .

The following table summarizes the three options.

|
|
| **Option** | **Applies to** | **Compaction** | **Snapshot expiration** | **Unreferenced file removal** | **You author** |
| --- |--- |--- |--- |--- |--- |
| Self-managed Spark procedures | Self-managed Iceberg on Amazon S3 | Yes (`rewrite_data_files`) | Yes (`expire_snapshots`) | Yes (`remove_orphan_files`) | The Spark session, the procedure calls, and the schedule |
| AWS Glue Data Catalog table optimizer | Self-managed Iceberg on Amazon S3 (tables cataloged in AWS Glue) | Yes (managed) | Yes (managed) | Yes (managed) | A one-time optimizer configuration per table (or catalog-wide) |
| Amazon S3 Tables built-in maintenance | Amazon S3 Tables | Yes (managed) | Yes (managed) | Yes (managed, per bucket) | Optional `PutTableMaintenanceConfiguration` per table to override defaults |

The sub-sections that follow describe each option in detail, including the tunable parameters, defaults, and typical workflows.
