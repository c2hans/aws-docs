---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/best-practices-redshift-spectrum.html
---

# Best practices for using Amazon Redshift Spectrum
<a name="best-practices-redshift-spectrum"></a>

This section provides an overview of best practices for using [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html). We recommend that you follow these best practices to achieve optimal performance when you use Redshift Spectrum:
+ Consider that file types have a significant influence on Redshift Spectrum query performance. To improve performance, use columnar encoded files such as ORC or Parquet, and use CSV format only for very small dimension tables.
+ Use prefix-based partitioning to take advantage of partition pruning. This means using filters that are keyed to the partitions in your data lake.
+ Redshift Spectrum scales automatically to process large requests, so do as much as possible in Redshift Spectrum (for example, predicate pushdown).
+ Pay attention to partition files on frequently filtered columns. If data is partitioned by one or more filtered columns, Redshift Spectrum can take advantage of partition pruning and skip scanning unneeded partitions and files. A common practice is to partition the data based on time.
+ You can check the effectiveness of your partitions and efficiency of your Redshift Spectrum query by using the following query.

  ```
  Select query,
             segment,
             max(assigned_partitions) as total_partitions,
             max(qualified_partitions) as qualified_partitions
  From svl_s3partition
  Where query=pg_last_query_id()
  Group by 1,2;
  ```

  The preceding query shows the following:
  + **total\_partitions** – The number of partitions recognized by the AWS Glue Data Catalog
  + **qualified\_partitions** – The number of prefixes on Amazon Simple Storage Service (Amazon S3) that are accessed for the Redshift Spectrum query
+ You can also check the `SVL_S3QUERY_SUMMARY` system table to learn about the effectiveness of your partitions and efficiency of your Redshift Spectrum query. To do so, use the following statement.

  ```
  Select *
  From svl_s3query_summary
  Where query=pg_last_query_id();
  ```

  The preceding query returns even more information, including `is_partitioned`, `s3_scanned_rows/bytes`, and `s3_returned_rows/bytes` values in addition to files showing the efficiency of partition pruning.

## Predicate pushdown in Redshift Spectrum
<a name="predicate-pushdown"></a>

Using predicate pushdown avoids consuming resources in the Amazon Redshift cluster. You can push many SQL operations down to the Redshift Spectrum layer. We recommend taking advantage of this wherever possible.

Keep in mind the following:
+ You can evaluate some types of SQL operations completely within the Redshift Spectrum layer, including the following:
  + `GROUP BY` clauses
  + Comparison and pattern-matching conditions (for example, `LIKE`)
  + Aggregate functions (for example, `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`)
  + `regex_replace`, `to_upper`, `date_trunc`, and other functions
+ You can't push some operations to the Redshift Spectrum layer, including `DISTINCT` and `ORDER BY`. Perform `ORDER BY` only at the top level of the query if possible, since sorting is done in the leader node.
+ Examine your query `EXPLAIN` plan to verify if predicate pushdown is effective. To find Redshift Spectrum portions in an `EXPLAIN` command, look for these steps:
  + S3 Seq Scan
  + S3 HashAggregate
  + S3 Query Scan
  + Seq Scan PartitionInfo
  + Partition Loop
+ Use the fewest number of columns in your query. Redshift Spectrum can eliminate columns for scanning if data is in Parquet or ORC format.
+ Make extensive use of partitions for parallel processing and partition elimination, and keep file sizes to at least 64 MB if possible.
+ Set the `TABLE PROPERTIES` `'numRows'='nnn'` if you use `CREATE EXTERNAL TABLE` or `ALTER TABLE`. Amazon Redshift doesn't analyze external tables to generate table statistics that the query optimizer uses to generate a query plan. If the statistics aren't set, then Amazon Redshift assumes that external tables are the larger tables and local tables are the smaller tables.

## Query tuning tips for Redshift Spectrum
<a name="query-tuning-spectrum"></a>

We recommend that you keep the following in mind when you tune your queries:
+ The number of Redshift Spectrum nodes that your Amazon Redshift cluster can engage for a query is tied to the number of slices in your cluster.
+ Resizing your cluster up can benefit your cluster's local compute profiles, storage profiles, and the query capabilities of the Amazon S3 data lake query.
+ The Amazon Redshift query planner pushes predicates and aggregations to the Redshift Spectrum query layer whenever possible.
+ When large amounts of data are returned from Amazon S3, the processing is limited by your cluster's resources.
+ Because Redshift Spectrum scales automatically to process large requests, your overall performance improves whenever you can push processing to the Redshift Spectrum layer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
