---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/monitoring.html
---

# Monitoring Iceberg workloads

Monitoring is crucial for performance management and troubleshooting. It helps you understand the overall **shape** of your Iceberg tables — unbalanced partitions, small-file accumulation, snapshot growth, orphan files, and other symptoms of write patterns or maintenance gaps that would otherwise show up as slow queries. If you run **self-managed maintenance** on those tables, monitoring also drives the maintenance schedule itself: for example, when a partition reaches a certain percentage of small files, your workload can start a compaction job to consolidate the files into larger ones and prevent queries from slowing down beyond an acceptable level.

Iceberg exposes two built-in monitoring surfaces, and AWS layers a third on top of them for managed maintenance:
+ [Monitoring using metadata tables](#monitoring-using-metadata-tables) — periodic, snapshot-in-time views of a table's state (file counts, sizes, partitions, snapshot history) queried directly with SQL. Best for dashboards and for driving preventive maintenance jobs on a schedule.
+ [Monitoring using metrics reporters](#monitoring-using-metrics-reporters) — per-operation, real-time observability of each Iceberg read or write. Each operation produces a structured `CommitReport` or `ScanReport` (introduced in Iceberg 1.1 through the [Metrics Reporting](https://iceberg.apache.org/docs/latest/metrics-reporting/) API) that you can route into your own metrics or logging pipeline (for example, Amazon CloudWatch).
+ [Monitoring managed maintenance](#monitoring-managed-maintenance) — Amazon CloudWatch metrics that Amazon S3 Tables and the AWS Glue Iceberg table optimizer publish for the compaction, snapshot expiration, and orphan-file cleanup jobs they run for you.

## Monitoring using metadata tables
<a name="monitoring-using-metadata-tables"></a>

Every Iceberg table exposes a set of hidden [metadata tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) — `snapshots`, `files`, `partitions`, `history`, `refs`, `manifests`, `metadata_log_entries`, plus the `all_*` variants — that any Iceberg-capable engine can query with plain SQL. Both **self-managed Iceberg on Amazon S3** and **Amazon S3 Tables** expose the same set, so the query-based patterns below apply to both hosting options. You can either query the metadata tables directly from your BI tool for live dashboards, or persist the query results (into an AWS Glue table or a small Iceberg observability table) and drive scheduled dashboards and preventive maintenance from that copy. For a reference implementation that queries Iceberg metadata tables and stores metrics in Amazon CloudWatch, see the AWS blog post [Monitoring Apache Iceberg metadata layer using AWS Lambda, AWS Glue, and AWS CloudWatch](https://aws.amazon.com/blogs/big-data/monitoring-apache-iceberg-metadata-layer-using-aws-lambda-aws-glue-and-aws-cloudwatch/).

### Table-level monitoring
<a name="table-level-monitoring"></a>

The following example shows a table monitoring dashboard that was created in AWS Quick Sight. Behind the scenes, a Spark SQL pipeline queries the Iceberg metadata tables — capturing detailed metrics such as the number of active files and total storage — and persists the results in an AWS Glue table. The AWS Quick Sight dashboard, shown in the following illustration, then reads that Glue table through Amazon Athena. This information helps you identify and address specific problems in your systems.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/21f530c9-5ed7-4df6-ab61-7246d6e7478a.png)

The example AWS Quick Sight dashboard surfaces the following key performance indicators (KPIs) for an Iceberg table. The **Query** column shows the Spark SQL statement that the pipeline runs against the Iceberg metadata tables to compute each KPI; the results are persisted into the AWS Glue table that the dashboard reads through Amazon Athena.

|
|
| **KPI** | **Description** | **Query** |
| --- |--- |--- |
| **Number of files** | The number of files in the Iceberg table (for all snapshots) | <pre>select count(distinct file_path) from <catalog.database.table_name>.all_files</pre> |
| **Number of active files** | The number of active files in the last snapshot of the Iceberg table | <pre>select count(*) from <catalog.database.table_name>.files</pre> |
| **Average file size** | The average file size, in megabytes, for all files in the Iceberg table | <pre>select avg(file_size_in_bytes)/1000000<br />from (<br />  select file_path, min(file_size_in_bytes) as file_size_in_bytes<br />  from <catalog.database.table_name>.all_files<br />  group by file_path<br />)</pre> |
| **Average active file size** | The average file size, in megabytes, for  the active files in the Iceberg table | <pre>select avg(file_size_in_bytes)/1000000 from <catalog.database.table_name>.files</pre> |
| **Percentage of small files** | The percentage of active files that are smaller than 100 MB | <pre>select cast(sum(case when file_size_in_bytes < 100000000 then 1 else 0 end) * 100/count(*) as decimal(10,2)) from <catalog.database.table_name>.files</pre> |
| **Total storage size** | The total size of all the files in the table, excluding orphaned files and Amazon S3 object versions (if enabled) | <pre>select sum(file_size_in_bytes)/1000000<br />from (<br />  select file_path, min(file_size_in_bytes) as file_size_in_bytes<br />  from <catalog.database.table_name>.all_files<br />  group by file_path<br />)</pre> |
| **Total active storage size** | The total size of all files in the current snapshots of a given table | <pre>select sum(file_size_in_bytes)/1000000 from <catalog.database.table_name>.files</pre> |

To capture KPI changes **over time**, schedule the pipeline to run periodically (for example, once a day) and `INSERT` each run's KPI values into the AWS Glue table alongside a run timestamp. The AWS Quick Sight dashboard then reads that history and can plot trends — small-file percentage over time, total storage growth, active-file count month over month — instead of just the latest snapshot.

If you only need the **current** state and don't need history, the dashboard can skip the pipeline entirely and query the Iceberg metadata tables directly from Amazon Athena through their `$partitions`, `$files`, `$manifests`, and `$snapshots` suffixes. Each dashboard load then reflects the latest state of the table.

For more information about creating dashboards, see the [AWS Quick Sight documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html).

### Database-level monitoring
<a name="database-level-monitoring"></a>

The following example shows a monitoring dashboard that was created in AWS Quick Sight to provide an overview of database-level KPIs for a collection of Iceberg tables.

![Amazon QuickSight dashboard showing database-level Iceberg KPIs for 10 tables: active and total file counts (31 and 619), average file sizes (31.17 MB active, 18.07 MB total), a gauge showing 94.17% small files, active and total storage (1,083.64 MB and 44,061.53 MB), and two bar charts comparing active versus total number of files and average file size per table.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/a875622b-5782-4957-b7fb-ae7da113afe0.png)

This dashboard collects the following KPIs:

This dashboard uses the table-level queries from the previous section and consolidates their outcomes across all tables in the database:

|
|
| **KPI** | **Description** |
| --- |--- |
| **Number of files** | The number of files in the Iceberg database (for all snapshots) |
| **Number of active files** | The number of active files in the Iceberg database (based on the last snapshots of Iceberg tables) |
| **Average file size** | The average file size, in megabytes, for all files in the Iceberg database |
| **Average active file size** | The average file size, in megabytes, for all active files in the Iceberg database |
| **Percentage of small files** | The percentage of active files that are smaller than 100 MB in the Iceberg database |
| **Total storage size** | The total size of all files in the database, excluding orphaned files and Amazon S3 object versions (if enabled) |
| **Total active storage size** | The total size of all files in the current snapshots of all tables in the database |

### Preventive maintenance
<a name="preventive-maintenance"></a>

When you're **self-managing** Iceberg table maintenance (as opposed to relying on Amazon S3 Tables' built-in maintenance or the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md)), the monitoring capabilities discussed above let you approach maintenance from a preventive instead of reactive angle. Use the table-level and database-level metrics to schedule actions such as the following:
+ Use bin packing compaction to group small files when a table reaches N small files.
+ Use bin packing compaction to merge delete files when a table reaches N delete files in a given partition.
+ Remove small files that were already compacted by removing snapshots when the total storage is X times higher than active storage.

## Monitoring using metrics reporters
<a name="monitoring-using-metrics-reporters"></a>

Metrics reporters are the second built-in monitoring surface. Rather than querying metadata tables from SQL, each Iceberg operation emits a structured report through a `MetricsReporter` implementation that you register on the Iceberg catalog. See [Metrics Reporting](https://iceberg.apache.org/docs/latest/metrics-reporting/) in the Iceberg documentation for the full report schemas and the reporter interface.

**Default reporter (**`LoggingMetricsReporter`**)** — writes reports directly to the Iceberg logger. (When you use a REST catalog, the default is `RESTMetricsReporter` instead, which sends reports to the catalog service rather than the logs.) Raise the Spark app log level to `INFO` and you'll see two report types in the driver logs:
+ `CommitReport` — emitted on writes, with stats such as total commit duration, number of data files added and removed, records added and removed, and the target snapshot ID.
+ `ScanReport` — emitted on reads, with stats such as scan-planning duration, total data manifests scanned, matching data files, total file size scanned, and the snapshot ID the scan resolved to.

**Custom reporters** — implement the `org.apache.iceberg.metrics.MetricsReporter` interface with the logic you want (for example, a `CloudwatchMetricsReporter` that pushes each `CommitReport` / `ScanReport` field as an Amazon CloudWatch metric), and register the class on the Iceberg catalog through the `metrics-reporter-impl` property:

```
spark.sql.catalog.<catalog_name>.metrics-reporter-impl=com.example.CloudwatchMetricsReporter
```

Different catalogs can point at the same or different reporter implementations.

**What these reports can tell you** — a couple of patterns worth watching:
+ `CommitReport`** with a large **`totalDuration` — writes are running longer than usual. Correlate with the same report's `addedDataFiles` and `removedDataFiles`: if a lot of files were rewritten, it may be a good time to switch to merge-on-read (set `write.delete.mode` / `write.update.mode` / `write.merge.mode` to `merge-on-read`) so that batch updates and deletes stop rewriting the base files. If `addedRecords` is much larger than usual instead, the workload simply wrote more data than a normal run.
+ **Many **`ScanReport`**s with low **`skippedDataFiles`** and **`skippedDataManifests` — reads aren't benefiting much from file-level pruning, so the engine ends up opening most of the table on every query. Revisit the partitioning strategy so it aligns with the query predicates (or use [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning) transforms that derive partitions from those predicate columns), and consider declaring a global sort order with `WRITE ORDERED BY` on frequently filtered high-cardinality columns to make min/max column statistics more selective.

## Monitoring managed maintenance
<a name="monitoring-managed-maintenance"></a>

Amazon S3 Tables emits [CloudWatch metrics for table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-monitoring-overview.html) that cover storage, requests, and the built-in maintenance jobs — use those to monitor the automatic compaction and snapshot expiration that S3 Tables performs on your behalf. If you're running the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) on self-managed Iceberg tables, AWS Glue similarly emits [CloudWatch metrics for the optimizer's maintenance activities](https://docs.aws.amazon.com/glue/latest/dg/view-optimization-metrics.html) (compaction, snapshot expiration, orphan-file cleanup) — use those to monitor Glue-managed maintenance the same way.
