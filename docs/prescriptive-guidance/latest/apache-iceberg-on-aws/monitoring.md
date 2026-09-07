---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/monitoring.html
---

# Monitoring Iceberg workloads
<a name="monitoring"></a>

To monitor Iceberg workloads, you have two options: analyzing [metadata tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) or using [metrics reporters](https://iceberg.apache.org/javadoc/latest/index.html?org/apache/iceberg/metrics/MetricsReporter.html). Metrics reporters were introduced in Iceberg version 1.2 and are available only for REST and JDBC catalogs.

If you're using AWS Glue Data Catalog, you can gain insights into the health of your Iceberg tables by setting up monitoring on top of the metadata tables that Iceberg exposes.

Monitoring is crucial for performance management and troubleshooting. For example, when a partition in an Iceberg table reaches a certain percentage of small files, your workload can start a compaction job to consolidate the files into larger ones. This prevents queries from slowing down beyond an acceptable level.

## Table-level monitoring
<a name="table-level-monitoring"></a>

The following screen shows a table monitoring dashboard that was created in Amazon Quick Sight. This dashboard queries Iceberg metadata tables by using Spark SQL, and captures detailed metrics such as the number of active files and total storage. This information is then stored in AWS Glue tables for operational purposes. Finally, a Quick Sight dashboard, as shown in the following illustration, is created by using Amazon Athena. This information helps you identify and address specific problems in your systems.

![QuickSight dashboard for monitoring Iceberg tables](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/715cbc38-e0ea-461e-8c75-117b9aca3fe2.png)

The example Quick Sight dashboard collects the following key performance indicators (KPIs) for an Iceberg table:

|
|
| KPI | Description | Query |
| --- |--- |--- |
| **Number of files** | The number of files in the Iceberg table (for all snapshots) | <pre>select count(*) from <catalog.database.table_name>.all_files</pre> |
| **Number of active files** | The number of active files in the last snapshot of the Iceberg table | <pre>select count(*) from <catalog.database.table_name>.files</pre> |
| **Average file size** | The average file size, in megabytes, for all files in the Iceberg table | <pre>select avg(file_size_in_bytes)/1000000 from <catalog.database.table_name>.all_files</pre> |
| **Average active file size** | The average file size, in megabytes, for  the active files in the Iceberg table | <pre>select avg(file_size_in_bytes)/1000000 from <catalog.database.table_name>.files</pre> |
| **Percentage of small files** | The percentage of active files that are smaller than 100 MB | <pre>select cast(sum(case when file_size_in_bytes < 100000000 then 1 else 0 end)*100/count(*) as decimal(10,2)) from <catalog.database.table_name>.files</pre> |
| **Total storage size** | The total size of all the files in the table, excluding orphaned files and Amazon S3 object versions (if enabled) | <pre>select sum(file_size_in_bytes)/1000000 from <catalog.database.table_name>.all_files</pre> |
| **Total active storage size** | The total size of all files in the current snapshots of a given table | <pre>select sum(file_size_in_bytes)/1000000 from <catalog.database.table_name>.files</pre> |

For more information about creating dashboards, see the [Quick Sight documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html).

## Database-level monitoring
<a name="database-level-monitoring"></a>

The following example shows a monitoring dashboard that was created in Quick Sight to provide an overview of database-level KPIs for a collection of Iceberg tables.

![QuickSight dashboard for database-level monitoring for Iceberg](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/0ba002ef-2d8d-4be2-9e76-0fd8fe7aef57.png)

This dashboard collects the following KPIs:

|
|
| KPI | Description | Query |
| --- |--- |--- |
| **Number of files** | The number of files in the Iceberg database (for all snapshots) | This dashboard uses the table-level queries provided in the previous section and consolidates the outcomes. |
| **Number of active files** | The number of active files in the Iceberg database (based on the last snapshots of Iceberg tables) |
| **Average file size** | The average file size, in megabytes, for all files in the Iceberg database |
| **Average active file size** | The average file size, in megabytes, for all active files in the Iceberg database |
| **Percentage of small files** | The percentage of active files that are smaller than 100 MB in the Iceberg database |
| **Total Storage size** | The total size of all files in the database, excluding orphaned files and Amazon S3 object versions (if enabled) |
| **Total active storage size** | The total size of all files in the current snapshots of all tables in the database |

## Preventive maintenance
<a name="preventive-maintenance"></a>

By setting up the monitoring capabilities discussed in the previous sections, you can approach table maintenance from a preventive instead of reactive angle. For example, you can use the table-level and database-level metrics to schedule actions such as the following:
+ Use bin packing compaction to group small files when a table reaches N small files.
+ Use bin packing compaction to merge delete files when a table reaches N delete files in a given partition.
+ Remove small files that were already compacted by removing snapshots when the total storage is X times higher than active storage.
