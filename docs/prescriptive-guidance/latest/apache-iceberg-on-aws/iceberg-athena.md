---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-athena.html
---

# Working with Iceberg tables by using Athena SQL
<a name="iceberg-athena"></a>

Amazon Athena provides built-in support for Apache Iceberg, and doesn't require additional steps or configuration. This section provides a detailed overview of supported features and high-level guidance for using Athena to interact with Iceberg tables.

## Version and feature compatibility
<a name="athena-version"></a>

### Iceberg table specification support
<a name="iceberg-table-specification-support.bf8c0bac-0018-5f77-9a59-737e6761313f"></a>

The Apache Iceberg table specification specifies how Iceberg tables should behave. Athena supports table format version 2, so any Iceberg table that you create with the console, CLI, or SDK inherently uses that version.

If you use an Iceberg table that was created with another engine, such as Apache Spark on Amazon EMR or AWS Glue, make sure to set the table format version by using [table properties](https://iceberg.apache.org/docs/latest/configuration/#reserved-table-properties). As a reference, see the section [Creating and writing Iceberg tables](iceberg-spark.md#spark-create-data) earlier in this guide.

### Iceberg feature support
<a name="iceberg-feature-support.29d4c9a8-461f-5861-87c7-d99da614fdeb"></a>

You can use Athena to read from and write to Iceberg tables. When you change data by using the `UPDATE`, `MERGE INTO`, and `DELETE FROM` statements, Athena supports merge-on-read mode only. This property cannot be changed. In order to update or delete data with copy-on-write, you have to use other engines such as Apache Spark on Amazon EMR or AWS Glue. The following table summarizes Iceberg feature support in Athena.

|
|
|   |   | DDL support | DML support | AWS Lake Formation for security (optional) |
| --- |--- |--- |--- |--- |
|  | **Table format** | **Create table** | **Schema evolution** | **Reading data** | **Writing data** | **Row/column access control** |
| **Amazon Athena** | Version 2<br />  | **** | **** | **** | **X** Copy-on-write | **** |
| ** **Merge-on-read | **** |

**Notes**:
+ Athena doesn't support Incremental queries.
+ In Athena, update, delete, and merge operations always default to merge on read (MoR), regardless of any copy on write (CoW) settings in the table properties, because CoW isn't supported.

## Working with Iceberg tables
<a name="athena-tables"></a>

For a quick start to using Iceberg in Athena, see the section [Getting started with Iceberg tables in Athena SQL](getting-started.md) earlier in this guide.

The following table lists limitations and recommendations.

|
|
| Scenario | Limitation | Recommendation |
| --- |--- |--- |
| Table DDL generation | Iceberg tables created with other engines can have properties that are not exposed in Athena. For these tables, it's not possible to generate the DDL. | Use the equivalent statement in the engine that created the table (for example, the `SHOW CREATE TABLE` statement for Spark). |
| Random Amazon S3 prefixes in objects that are written to an Iceberg table | By default, Iceberg tables that are created with Athena have the `write.object-storage.enabled` property enabled. | To disable this behavior and gain full control over Iceberg table properties, create an Iceberg table with another engine such as Spark on Amazon EMR or AWS Glue. |
| Incremental queries | Not currently supported in Athena. | To use incremental queries to enable incremental data ingestion pipelines, use Spark on Amazon EMR or AWS Glue. |
