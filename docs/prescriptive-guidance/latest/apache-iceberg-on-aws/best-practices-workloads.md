---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-workloads.html
---

# Using Iceberg workloads in Amazon S3
<a name="best-practices-workloads"></a>

This section discusses Iceberg properties that you can use to optimize Iceberg's interaction with Amazon S3.

## Prevent hot partitioning (HTTP 503 errors)
<a name="workloads-503"></a>

Some data lake applications that run on Amazon S3 handle millions or billions of objects and process petabytes of data. This can lead to prefixes that receive a high volume of traffic, which are typically detected through HTTP 503 (service unavailable) errors. To prevent this issue, use the following Iceberg properties:
+ Set `write.distribution-mode` to `hash` or `range` so that Iceberg writes large files, which results in fewer Amazon S3 requests. This is the preferred configuration and should address the majority of cases.
+ If you continue to experience 503 errors due to an immense volume of data in your workloads, you can set `write.object-storage.enabled` to `true` in Iceberg. This instructs Iceberg to hash object names and distribute the load across multiple, randomized Amazon S3 prefixes.

For more information about these properties, see [Write properties](https://iceberg.apache.org/docs/latest/configuration/#write-properties) in the Iceberg documentation.

## Use Iceberg maintenance operations to release unused data
<a name="workloads-unused-data"></a>

To manage Iceberg tables, you can use the Iceberg core API, Iceberg clients (such as Spark), or managed services such as Amazon Athena. To delete old or unused files from Amazon S3, we recommend that you only use Iceberg native APIs to [remove snapshots](https://iceberg.apache.org/docs/latest/maintenance/#expire-snapshots), [remove old metadata files](https://iceberg.apache.org/docs/latest/maintenance/#remove-old-metadata-files), and [delete orphan files](https://iceberg.apache.org/docs/latest/maintenance/#delete-orphan-files).

Using Amazon S3 APIs through Boto3, the Amazon S3 SDK, or the AWS Command Line Interface (AWS CLI), or using any other, non-Iceberg methods to overwrite or remove Amazon S3 files for an Iceberg table leads to table corruption and query failures.

## Replicate data across AWS Regions
<a name="workloads-replication"></a>

When you store Iceberg tables in Amazon S3, you can use the built-in features in Amazon S3, such as [Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) and [Multi-Region Access Points (MRAP)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html), to replicate data across multiple AWS Regions. MRAP provides a global endpoint for applications to access S3 buckets that are located in multiple AWS Regions. Iceberg doesn't support relative paths, but you can use MRAP to perform Amazon S3 operations by mapping buckets to access points. MRAP also integrates seamlessly with the Amazon S3 Cross-Region Replication process, which introduces a lag of up to 15 minutes. You have to replicate both data and metadata files.

Important: Currently, Iceberg integration with MRAP works only with Apache Spark. If you need to fail over to the secondary AWS Region, you have to plan to redirect user queries to a Spark SQL environment (such as Amazon EMR) in the failover Region.

The CRR and MRAP features help you build a cross-Region replication solution for Iceberg tables, as illustrated in the following diagram.

![Cross-region replication for Iceberg tables](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/0ed52165-ab05-44d1-a171-0d9c663646a9.png)

To set up this cross-Region replication architecture:

1. Create tables by using the MRAP location. This ensures that Iceberg metadata files point to the MRAP location instead of the physical bucket location.

1. Replicate Iceberg files by using Amazon S3 MRAP.** **MRAP supports data replication with a service-level agreement (SLA) of 15 minutes. Iceberg prevents read operations from introducing inconsistencies during replication.

1. Make the tables available in the AWS Glue Data Catalog in the secondary Region. You can choose from two options:
   + Set up a pipeline for replicating Iceberg table metadata by using AWS Glue Data Catalog replication. This utility is available in the GitHub  [Glue Catalog and Lake Formation Permissions replication](https://github.com/aws-samples/lake-formation-pemissions-sync) repository. This event-driven mechanism replicates tables in the target Region based on event logs.
   + Register the tables in the secondary Region when you need to fail over. For this option, you can use the previous utility or the Iceberg [register\_table procedure](https://iceberg.apache.org/docs/latest/spark-procedures/#register_table) and point it to the latest `metadata.json` file.
