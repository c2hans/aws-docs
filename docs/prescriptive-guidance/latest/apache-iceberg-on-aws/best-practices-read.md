---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-read.html
---

# Optimizing read performance
<a name="best-practices-read"></a>

This section discusses table properties that you can tune to optimize read performance, independent of the engine.

## Partitioning
<a name="read-partitioning"></a>

As with Hive tables, Iceberg uses partitions as the primary layer of indexing to avoid reading unnecessary metadata files and data files. Column statistics are also taken into consideration as a secondary layer of indexing to further improve query planning, which leads to better overall execution time.

### Partition your data
<a name="partition-your-data.4af558c0-ab01-544c-897e-e3dce10c8b10"></a>

To reduce the amount of data that's scanned when querying Iceberg tables, choose a balanced partition strategy that aligns with your expected read patterns:
+ Identify columns that are frequently used in queries. These are ideal partitioning candidates. For example, if you typically query data from a particular day, a natural example of a partition column would be a date column.
+ Choose a low cardinality partition column to avoid creating an excessive number of partitions. Too many partitions can increase the number of files in the table, which can negatively impact query performance. As a rule of thumb, "too many partitions" can be defined as a scenario where the data size in the majority of partitions is less than 2-5 times the value set by `target-file-size-bytes`.

**Note**
If you typically query by using filters on a high cardinality column (for example, an `id` column that can have thousands of values), use Iceberg's hidden partitioning feature with bucket transforms, as explained in the next section.

### Use hidden partitioning
<a name="use-hidden-partitioning.9df81daf-ceb9-5bcb-9465-693c918a89dd"></a>

If your queries commonly filter on a derivative of a table column, use hidden partitions instead of explicitly creating new columns to work as partitions. For more information about this feature, see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning).

For example, in a dataset that has a timestamp column (for example, `2023-01-01 09:00:00`), instead of creating a new column with the parsed date (for example, `2023-01-01`), use partition transforms to extract the date part from the timestamp and create these partitions on the fly.

The most common use cases for hidden partitioning are:
+ **Partitioning on date or time**, when the data has a timestamp column. Iceberg offers multiple transforms to extract the date or time parts of a timestamp.
+ **Partitioning on a hash function of a column**, when the partitioning column has high cardinality and would result in too many partitions. Iceberg's bucket transform groups multiple partition values together into fewer, hidden (bucket) partitions by using hash functions on the partitioning column.

See [partition transforms](https://iceberg.apache.org/spec/#partition-transforms) in the Iceberg documentation for an overview of all available partition transforms.

Columns that are used for hidden partitioning can become part of query predicates through the use of regular SQL functions such as `year()` and `month()`. Predicates can also be combined with operators such as `BETWEEN` and `AND`.

**Note**
Iceberg cannot perform partition pruning for functions that yield a different data type; for example, `substring(event_time, 1, 10) = '2022-01-01'`.

### Use partition evolution
<a name="use-partition-evolution.a006779c-cead-58a7-98d6-c010826c6c6f"></a>

Use [Iceberg's partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) when the existing partition strategy isn't optimal. For example, if you choose hourly partitions that turn out to be too small (just a few megabytes each), consider shifting to daily or monthly partitions.

You can use this approach when the best partition strategy for a table is initially unclear, and you want to refine your partitioning strategy as you gain more insights. Another effective use of partition evolution is when data volumes change and the current partitioning strategy becomes less effective over time.

For instructions on how to evolve partitions, see [ALTER TABLE SQL extensions](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table-sql-extensions) in the Iceberg documentation.

## Tuning file sizes
<a name="read-file-size"></a>

Optimizing query performance involves minimizing the number of small files in your tables. For good query performance, we generally recommend keeping Parquet and ORC files larger than 100 MB.

File size also impacts query planning for Iceberg tables. As the number of files in a table increases, so does the size of the metadata files. Larger metadata files can result in slower query planning. Therefore, when the table size grows*,* increase the file size** **to alleviate the exponential expansion of metadata.

Use the following best practices to create properly sized files in Iceberg tables.

### Set target file and row group size
<a name="set-target-file-and-row-group-size.052c2e05-d9fc-5f3c-a5bb-3efd0d1b3d3e"></a>

Iceberg offers the following key configuration parameters for tuning the data file layout. We recommend that you use these parameters to set the target file size and row group or strike size.

|
|
| Parameter | Default value | Comment |
| --- |--- |--- |
| `write.target-file-size-bytes` | 512 MB | This parameter specifies the maximum file size that Iceberg will create. However, certain files might be written with a smaller size than this limit. |
| `write.parquet.row-group-size-bytes` | 128 MB | Both Parquet and ORC store data in chunks so that engines can avoid reading the entire file for some operations. |
| `write.orc.stripe-size-bytes` | 64 MB |
| `write.distribution-mode` | None, for Iceberg version 1.1 and lower<br />Hash, starting with Iceberg version 1.2<br />  | Iceberg requests Spark to sort data between its tasks before writing to storage. |
+ Based on your expected table size, follow these general guidelines:
  + **Small tables** (up to few gigabytes) – Reduce the target file size to 128 MB. Also reduce the row group or stripe size (for example, to 8 or 16 MB).
  + **Medium to large tables** (from a few gigabytes to hundreds of gigabytes) – The default values are a good starting point for these tables. If your queries are very selective, adjust the row group or stripe size (for example, to 16 MB).
  + **Very large tables** (hundreds of gigabytes or terabytes) – Increase the target file size to 1024 MB or more, and consider increasing the row group or stripe size if your queries usually pull large sets of data.
+ To ensure that Spark applications that write to Iceberg tables create appropriately sized files, set the `write.distribution-mode` property to either `hash` or `range`. For a detailed explanation of the difference between these modes, see [Writing Distribution Modes](https://iceberg.apache.org/docs/latest/spark-writes/#writing-distribution-modes) in the Iceberg documentation.

These are general guidelines. We recommend that you run tests to identify the most suitable values for your specific tables and workloads.

### Run regular compaction
<a name="run-regular-compaction.04911f11-b169-5657-8315-12bc5aba547a"></a>

The configurations in the previous table set a maximum file size that write tasks can create, but do not guarantee that files will have that size. To ensure proper file sizes, run compaction regularly to combine small files into larger files. For detailed guidance on running compaction, see [Iceberg compaction](best-practices-compaction.md) later in this guide.

## Optimize column statistics
<a name="read-column-statistics"></a>

Iceberg uses column statistics to perform file pruning, which improves query performance by reducing the amount of data that's scanned by queries. To benefit from column statistics, make sure that Iceberg collects statistics for all columns that are frequently used in query filters.

By default, Iceberg collects statistics only for the [first 100 columns in each table](https://github.com/apache/iceberg/blob/ae15c7e36973501b40443e75816d3eac39eddc90/core/src/main/java/org/apache/iceberg/TableProperties.java#L276), as defined by the table property `write.metadata.metrics.max-inferred-column-defaults`. If your table has more than 100 columns and your queries frequently reference columns outside of the first 100 columns (for example, you might have  queries that filter on column 132), make sure that Iceberg collects statistics on those columns. There are two options to achieve this:
+ When you create the Iceberg table, reorder columns so that the columns you need for queries fall within the column range set by `write.metadata.metrics.max-inferred-column-defaults` (default is 100).
**Note**
If you don't need statistics on 100 columns, you can adjust the `write.metadata.metrics.max-inferred-column-defaults` configuration to a desired value (for example, 20) and reorder the columns so that the columns you need to read and write queries fall within the first 20 columns on the left side of the dataset.
+ If you use only a few columns in query filters, you can disable the overall property for metrics collection and selectively choose individual columns to collect statistics for, as shown in this example:

  ```
  .tableProperty("write.metadata.metrics.default", "none")
  .tableProperty("write.metadata.metrics.column.my_col_a", "full")
  .tableProperty("write.metadata.metrics.column.my_col_b", "full")
  ```

**Note**
Column statistics are most effective when data is sorted on those columns. For more information, see the [Set the sort order](#read-sort-order) section later in this guide.

## Choose the right update strategy
<a name="read-update"></a>

Use a copy-on-write strategy to optimize read performance, when slower write operations are acceptable for your use case. This is the default strategy used by Iceberg.

Copy-on-write results in better read performance, because files are directly written to storage in a read-optimized fashion. However, compared with merge-on-read, each write operation takes longer and consumes more compute resources. This presents a classic trade-off between read and write latency. Typically, copy-on-write is ideal for use cases where most updates are collocated in the same table partitions (for example, for daily batch loads).

Copy-on-write configurations (`write.update.mode`, `write.delete.mode`, and `write.merge.mode`) can be set at the table level or independently on the application side.

## Use ZSTD compression
<a name="read-compression"></a>

You can modify the compression codec used by Iceberg by using the table property `write.<file_type>.compression-codec`. We recommend that you use the ZSTD compression codec to improve overall performance on tables.

By default, Iceberg versions 1.3 and earlier use GZIP compression, which provides slower read/write performance compared with ZSTD.

**Note**
Some engines might use different default values. This is the case for [Iceberg tables that are created with Athena](https://docs.aws.amazon.com/athena/latest/ug/compression-support-iceberg.html) or Amazon EMR version 7.x.

## Set the sort order
<a name="read-sort-order"></a>

To improve read performance on Iceberg tables, we recommend that you sort your table based on one or more columns that are frequently used in query filters. Sorting, combined with Iceberg's column statistics, can make file pruning significantly more efficient, which results in faster read operations. Sorting also reduces the number of Amazon S3 requests for queries that use the sort columns in query filters.

You can set a hierarchical sort order at the table level by running a data definition language (DDL) statement with Spark. For available options, see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table--write-ordered-by). After you set the sort order, writers will apply this sorting to subsequent data write operations in the Iceberg table.

For example, in tables that are partitioned by date (`yyyy-mm-dd`) where most of the queries filter by `uuid`, you can use the DDL option `Write Distributed By Partition Locally Ordered` to make sure that Spark writes files with non-overlapping ranges.

The following diagram illustrates how the efficiency of column statistics improves when tables are sorted. In the example, the sorted table needs to open only a single file, and maximally benefits from Iceberg's partition and file. In the unsorted table, any `uuid` can potentially exist in any data file, so the query has to open all data files.

![Setting sort order in Iceberg tables](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/511015a2-4318-4282-9d1b-a91b243c9302.png)

Changing the sort order doesn't affect existing data files. You can use Iceberg compaction to apply the sort order on those.

Using Iceberg sorted tables might decrease costs for your workload, as illustrated in the following graph.

![Comparison costs for Iceberg and Parquet tables](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/670693e0-7f83-4b76-beff-745cf6e59310.png)

![Results of TPC-H benchmark for Parquet vs. Iceberg tables](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/f2f2ef7d-e926-4bb9-a547-2f3d2557e259.png)

These graphs summarize the results of running the TPC-H benchmark for Hive (Parquet) tables compared with Iceberg sorted tables. However, the results might be different for other datasets or workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
