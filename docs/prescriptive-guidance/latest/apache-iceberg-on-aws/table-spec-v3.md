---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-spec-v3.html
---

# Working with Iceberg table format specification version 3
<a name="table-spec-v3"></a>

The latest version of the Apache Iceberg table format specification is version 3. This version introduces advanced capabilities for building petabyte-scale data lakes with improved performance and reduced operational overhead. It addresses common performance bottlenecks encountered with version 2, particularly around batch updates and compliance delete operations.

AWS provides support for deletion vectors and row lineage as defined in the Iceberg version 3 specification. These features are available with Apache Spark on the following AWS services.

|
|
| AWS service | Version 3 support |
| --- |--- |
| [Amazon EMR for Apache Spark](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-emr.html) | Amazon EMR release 7.12 or later |
| [AWS Glue](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.html) | Yes |
| AWS Glue: [Iceberg REST API](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html), table maintenance | Yes |
| [Amazon SageMaker Unified Studio notebooks](https://docs.aws.amazon.com/next-generation-sagemaker/) | Yes |
| [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html): [Iceberg REST API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html), [table maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html) | Yes |
| [Amazon Athena (Trino)](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0003.html) | No |

## Key features in version 3
<a name="v3-features"></a>

**Deletion vectors** replace the positional delete files that were used in version 2 with an efficient binary format stored as Puffin files. This eliminates write amplification from random batch updates and General Data Protection Regulation (GDPR) compliance deletes, and significantly reduces the overhead of maintaining fresh data. Organizations that process high-frequency updates will see immediate improvements in write performance and reduced storage costs from fewer small files.

**Row lineage** enables precise change tracking at the row level. Your downstream systems can process changes incrementally, speeding up data pipelines and reducing compute costs for change data capture (CDC) workflows. This built-in capability eliminates the need for custom change tracking implementations.

## Version compatibility
<a name="v3-version-compatibility"></a>

Version 3 maintains backward compatibility with version 2 tables. AWS services support both version 2 and version 3 tables simultaneously, so you can:
+ Run queries across both version 2 and version 3 tables.
+ Upgrade existing version 2 tables to version 3 without data rewrites.
+ Run time travel queries that span version 2 and version 3 snapshots.
+ Use schema evolution and hidden partitioning across table versions.

## Getting started with version 3
<a name="v3-getting-started"></a>

### Prerequisites
<a name="prerequisites.b0395e19-ad4a-570b-bd3a-7695b4c9c368"></a>

Before working with version 3 tables, make sure that you have:
+ An AWS account with appropriate AWS Identity and Access Management (IAM) permissions.
+ Access to one or more AWS analytics services (Amazon EMR, AWS Glue, Amazon SageMaker Unified Studio notebooks, or Amazon S3 Tables).
+ An S3 bucket for storing table data and metadata.
+ A table bucket to get started with Amazon S3 Tables or a general-purpose S3 bucket if you are building your own Iceberg infrastructure.
+ A configured AWS Glue catalog.

### Creating version 3 tables
<a name="creating-version-3-tables.728f96fd-ca37-50f1-980e-512740d43c3e"></a>

#### Creating new tables
<a name="creating-new-tables.9ebbfacb-473d-5dae-aae8-6e43380f7c8e"></a>

To create a new Iceberg version 3 table, set the `format-version` table property to 3. Using Spark SQL:

```
CREATE TABLE IF NOT EXISTS myns.orders_v3 (
    order_id bigint,
    customer_id string,
    order_date date,
    total_amount decimal(10,2),
    status string,
    created_at timestamp
)
USING iceberg
TBLPROPERTIES (
    'format-version' = '3'
)
```

#### Upgrading version 2 tables to version 3
<a name="upgrading-version-2-tables-to-version-3.eaebbe1f-a3a9-5684-8a69-682dc7938a88"></a>

You can upgrade existing version 2 tables to version 3 atomically without rewriting data. Using Spark SQL:

```
ALTER TABLE myns.existing_table
SET TBLPROPERTIES ('format-version' = '3')
```

**Important**
Version 3 is a one-way upgrade. After a table is upgraded from version 2 to version 3, it cannot be downgraded back to version 2 through standard operations. What happens during upgrade:
+ A new metadata snapshot is created atomically.
+ Existing Parquet data files are reused.
+ Row lineage fields are added to the table metadata.

After the upgrade:
+ The next compaction will remove old version 2 delete files.
+ New modifications will use the version 3 deletion vector files.

The upgrade doesn't perform a historical backfill of row lineage change tracking records.

### Enabling deletion vectors
<a name="enabling-deletion-vectors.4cd313e3-ec43-58ce-b3f0-bcbd06089b02"></a>

To take advantage of deletion vectors for updates, deletes, and merges, configure your write mode. Using Spark SQL:

```
ALTER TABLE myns.orders_v3
SET TBLPROPERTIES ('format-version' = '3',
                   'write.delete.mode' = 'merge-on-read',
                   'write.update.mode' = 'merge-on-read',
                   'write.merge.mode' = 'merge-on-read'
                  )
```

These settings ensure that update, delete, and merge operations create deletion vector files instead of rewriting entire data files.

### Using row lineage for change tracking
<a name="using-row-lineage-for-change-tracking.7e04ee4a-f042-559e-962b-2ac4b562a659"></a>

Version 3 automatically adds row lineage metadata fields to track changes.

Using Spark SQL:

```
# Query with parameter value provided
last_processed_sequence = 47

SELECT
    id,
    data,
    _row_id,
    _last_updated_sequence_number
FROM myns.orders_v3
WHERE _last_updated_sequence_number > :last_processed_sequence
```

The `_row_id` field uniquely identifies each row, and  `_last_updated_sequence_number` tracks when the row was last modified. Use these fields to:
+ Identify changed rows for incremental processing.
+ Track data lineage for compliance.
+ Optimize CDC pipelines.
+ Reduce compute costs by processing only changes.

## Best practices for version 3
<a name="v3-best-practices"></a>

### When to use version 3
<a name="when-to-use-version-3.174e764b-b48c-516f-bc74-f637ffa9d476"></a>

Consider upgrading to, or starting with, version 3 when:
+ You perform frequent batch updates or deletes.
+ You need to meet GDPR or compliance delete requirements.
+ Your workloads involve high-frequency upserts.
+ You require efficient CDC workflows.
+ You want to reduce storage costs from small files.
+ You need better change tracking capabilities.

### Optimizing write performance
<a name="optimizing-write-performance.fd62b42d-1b75-5ce3-a4ff-e95490e0b62c"></a>
+ Enable deletion vectors for update-heavy workloads:

  ```
  SET TBLPROPERTIES (
  'write.delete.mode' = 'merge-on-read',
  'write.update.mode' = 'merge-on-read',
  'write.merge.mode' = 'merge-on-read'
  )
  ```
+ Configure appropriate file sizes:

  ```
  SET TBLPROPERTIES (
  'write.target-file-size-bytes' = '536870912'  — 512 MB
  )
  ```

### Optimizing read performance
<a name="optimizing-read-performance.df5c29ed-0a1c-5cbd-9a29-0bfaeb967011"></a>
+ Use row lineage for incremental processing.
+ Use time travel to access historical data without copying.
+ Enable statistics collection for better query planning.

## Migration strategy
<a name="v3-migration"></a>

When you migrate from version 2 to version 3, follow these best practices:
+ Test in a non-production environment first to validate the upgrade process and performance.
+ Upgrade during low-activity periods to minimize impact on concurrent operations.
+ Monitor initial performance, and track metrics after the upgrade.
+ Run compaction to consolidate delete files after the upgrade.
+ Update your team documentation to reflect version 3 features.

## Compatibility considerations
<a name="v3-compatibility"></a>
+ Engine versions – Make sure that all engines accessing the table support version 3.
+ Third-party tools – Verify your tool's version 3 compatibility before you upgrade.
+ Backup strategy – Test snapshot-based recovery procedures.
+ Monitoring – Update monitoring dashboards for version 3-specific metrics.

## Troubleshooting
<a name="v3-troubleshooting"></a>

### Common issues
<a name="common-issues.e9106706-e98e-582d-81f5-4a1d68e83de8"></a>

**Error: "format-version 3 is not supported"**
+ Verify that your engine version supports version 3.  For specifics, see the table at the beginning of this section.
+ Check catalog compatibility.
+ Make sure that you're using the latest versions of AWS services.

**Performance degradation after upgrade**
+ Verify that there are no compaction compaction failures. For more information, see [Logging and monitoring for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-monitoring-overview.html) in the Amazon S3 documentation.
+ Confirm that deletion vectors are enabled. The following properties should be set:

  ```
  SET TBLPROPERTIES (
  'write.delete.mode' = 'merge-on-read',
  'write.update.mode' = 'merge-on-read',
  'write.merge.mode' = 'merge-on-read'
  )
  ```

  You can verify table properties with the following code:

  ```
  DESCRIBE FORMATTED myns.orders_v3
  ```
+ Review your partition strategy. Over-partitioning can lead to small files. Run the following query to get the average file size for your table:

  ```
  SELECT avg(file_size_in_bytes) as avg_file_size_bytes
  FROM myns.orders_v3.files
  ```

**Incompatibility with third-party tools**
+ Verify that the tool supports the version 3 specification.
+ Consider maintaining version 2 tables for unsupported tools.
+ Contact the tool vendor for their version 3 support timeline.

### Getting help
<a name="getting-help.41c27363-299d-5c65-aea9-f17ac096e27e"></a>
+ For AWS service-specific issues, contact [AWS Support.](https://aws.amazon.com/contact-us/)
+ To get help from the Iceberg community, use the [Iceberg Slack channel](https://iceberg.apache.org/community/).
+ For information about using AWS services to manage your analytics workloads, see [Analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/).

## Pricing
<a name="v3-pricing"></a>
+ [Amazon EMR compute and storage pricing](https://aws.amazon.com/emr/pricing/)
+ [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/)
+ [AWS Glue job run and Data Catalog pricing](https://aws.amazon.com/glue/pricing/)
+ [S3 Tables storage and requests pricing](https://aws.amazon.com/s3/pricing/)

## Availability
<a name="v3-availability"></a>

Iceberg table format specification version 3 support is available in all AWS Regions where Amazon EMR, AWS Glue, AWS Glue Data Catalog, and S3 Tables operate. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## Additional resources
<a name="v3-resources"></a>
+ [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/)
+ [Apache Iceberg table spec](https://iceberg.apache.org/spec/)
+ [Guidance for migrating tabular data from ](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/)Amazon S3[ to S3 Tables](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/)
+ [Tutorial: Getting started with S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
