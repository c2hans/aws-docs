---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/apache-iceberg-on-aws-self-managed-vs-s3-tables.html
---

# Apache Iceberg on AWS: self-managed vs. S3 Tables

On AWS, you host Apache Iceberg tables in two ways: self-managed on Amazon Simple Storage Service (Amazon S3), or in Amazon S3 Tables. Both use the same Apache Iceberg table format, so the read and write DML surface—SQL queries, inserts, updates, deletes, and time travel—is nearly identical. The differences are in **responsibility** (who runs maintenance and controls file layout), **integration** (which catalogs and services are pre-wired), and **features** (native replication, transaction throughput, and storage-tiering behavior). The following section compares the two options so that you can choose the right one for a workload

## At-a-glance comparison
<a name="at-a-glance-comparison"></a>

|
|
| **Aspect** | **Self-managed Iceberg on Amazon S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Storage | Standard S3 bucket | S3 table bucket (purpose-built) |
| Catalog | AWS Glue Data Catalog, the Iceberg REST catalog, and any Iceberg-compatible catalog such as Hive Metastore, JDBC, Nessie, or Polaris. This breadth of catalog choice supports multi-cloud and hybrid architectures. | Glue Data Catalog `s3tablescatalog` catalog, with each table bucket as a subcatalog; also the Iceberg REST catalog |
| Compaction | Manual (Athena `OPTIMIZE`, Spark `rewrite_data_files`) or automated with the AWS Glue Data Catalog table optimizer | Automated (managed by the service) |
| Snapshot management | Manual (Spark `expire_snapshots`, Athena `VACUUM`) or automated with the AWS Glue Data Catalog snapshot-retention optimizer | Automated (managed by the service) |
| Unreferenced file removal | Manual (Spark `remove_orphan_files`) or automated with the AWS Glue Data Catalog orphan-file-deletion optimizer | Automated (managed by the service) |
| Table replication (backup and recovery) | Custom implementation. For example, use the Iceberg `rewrite_table_path` procedure to prepare the copy and rewrite Iceberg metadata, copy data and metadata files with Apache Spark or [Amazon S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html), and then update the catalog metadata pointer in the backup destination. | Native table replication. Managed same-Region and cross-Region, same-account and cross-account. S3 Tables maintains read-only replica tables automatically. See [Replicating S3 tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-replication-tables.html). |
| Transaction throughput | [3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per second per partitioned prefix, with no limit on the number of prefixes per bucket (see Best practices design patterns: optimizing Amazon S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)) | Up to 10x higher transactions per second compared to Iceberg tables stored in general purpose buckets (see [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/)) |
| Storage tiering | Any S3 storage class, including S3 Intelligent-Tiering | S3 Standard or S3 Intelligent-Tiering only (compaction-aware); other storage classes aren't supported currently |
| Access control | IAM policies on the bucket and Glue objects; optional Lake Formation grants for fine-grained access | `s3tables` IAM policies on the table bucket; optional Lake Formation grants for fine-grained access |
| Cost model | You pay for S3 storage, API requests, and the compute you use to run maintenance jobs, either the engine you run the Iceberg procedures on (Amazon EMR, AWS Glue, or Amazon Athena) or the AWS Glue Data Catalog table optimizer (billed in Glue DPU-hours). See [AWS Glue pricing](https://aws.amazon.com/glue/pricing/). | You pay for S3 Tables storage and requests. Compaction and other maintenance are billed as part of S3 Tables usage rather than as separate compute jobs that you provision. See [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). |

## How the options differ
<a name="how-the-options-differ"></a>

**Catalog.** When you integrate S3 Tables with AWS analytics services, Amazon S3 adds a catalog named `s3tablescatalog` to the AWS Glue Data Catalog in the Region. Each table bucket is populated as a subcatalog, each namespace as a database, and each table as a table. Self-managed tables can use the Glue Data Catalog, the Iceberg REST catalog, or any Iceberg-compatible catalog such as Hive Metastore, JDBC, Nessie, or Polaris.

**Transaction throughput.** S3 table buckets are purpose-built for tabular data and deliver [up to 10x higher transactions per second](https://aws.amazon.com/s3/features/tables/) compared to Iceberg tables stored in general purpose S3 buckets. These are S3 API-level limits; end-to-end Iceberg commit throughput also depends on catalog locking and metadata file contention. Self-managed tables on general purpose buckets require deliberate partition and prefix design for high-throughput workloads.

**Storage tiering.** Self-managed tables can use any S3 storage class. S3 Tables support only S3 Standard or S3 Intelligent-Tiering, which you specify at table creation. Both options can use S3 Intelligent-Tiering to move data to lower-cost tiers based on access patterns. In S3 Tables, compaction runs only on files in the Frequent Access tier, so maintenance doesn't read files in colder tiers back into warmer tiers. For self-managed tables, S3 Intelligent-Tiering tiers files based on access, so read operations from maintenance jobs such as compaction reset a file's access timer and can keep frequently maintained files in higher-cost tiers.

### Note
<a name="note"></a>

For self-managed tables, files smaller than 128 KB aren't eligible for S3 Intelligent-Tiering auto-tiering and remain in the Frequent Access tier.

**Access control.** For both options, you use AWS Identity and Access Management (IAM) for coarse-grained access and AWS Lake Formation for fine-grained access at the database, table, column, row, and cell level. All Amazon S3 Block Public Access settings are always enabled for table buckets and can't be disabled.

### Note
<a name="note"></a>

S3 Tables integration with AWS analytics services uses IAM-based access controls in a subset of AWS Regions. In all other Regions, the integration also requires AWS Lake Formation. For the current list of Regions, see [Amazon S3 Tables integration with AWS analytics services overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integration-overview.html).

### Important
<a name="important"></a>

When you use S3 Tables with the AWS Glue Data Catalog integration, table names and table definitions, including column names, must be lowercase. Names that contain uppercase letters aren't supported by the Data Catalog or Lake Formation and aren't visible to analytics services such as Amazon Athena.

## Choosing between the options
<a name="choosing-between-the-options"></a>

Use Amazon S3 Tables when you want compaction, snapshot expiration, and unreferenced-file cleanup handled for you, want managed table replication, and can let the service control file layout and storage tiering. Use self-managed Iceberg on Amazon S3 when you need control over file layout, compaction timing, or catalog choice; when you must colocate table data with an existing S3-based data lake; or when you need engine versions or configurations that S3 Tables doesn't yet support. Because both use the same table format, you can migrate between them later, although the migration requires re-cataloging and data movement.
