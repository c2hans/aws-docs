---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-warehouse-technology-options.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data warehouse technology options
<a name="data-warehouse-technology-options"></a>

 In this section, we discuss options available for building a data warehouse: row-oriented databases, column-oriented databases, and massively parallel processing architectures.

## Row-oriented databases
<a name="row-oriented-databases"></a>

 Row-oriented databases typically store whole rows in a physical block. High performance for read operations is achieved through secondary indexes. Databases such as Oracle Database Server, Microsoft SQL Server, MySQL, and PostgreSQL are row-oriented database systems. These systems have been traditionally used for data warehousing, but they are better suited for transactional processing (OLTP) than for analytics.

 To optimize performance of a row-based system used as a data warehouse, developers use a number of techniques, including:
+  Building materialized views
+  Creating pre-aggregated rollup tables
+  Building indexes on every possible predicate combination
+  Implementing data partitioning to leverage partition pruning by query optimizer
+  Performing index-based joins

 Traditional row-based data stores are limited by the resources available on a single machine. Data marts alleviate the problem, to an extent, by using functional [sharding](https://www.digitalocean.com/community/tutorials/understanding-database-sharding). You can split your data warehouse into multiple data marts, each satisfying a specific functional area. However, when data marts grow large over time, data processing slows down.

 In a row-based data warehouse, every query has to read through all of the columns for all of the rows in the blocks that satisfy the query predicate, including columns you didn’t choose. This approach creates a significant performance bottleneck in data warehouses, where your tables have more columns, but your queries use only a few.

## Column-oriented databases
<a name="column-oriented-databases"></a>

 Column-oriented databases organize each column in its own set of physical blocks instead of packing the whole rows into a block. This functionality allows them to be more input/output (I/O) efficient for read-only queries, because they have to read only those columns accessed by a query from disk (or from memory). This approach makes column-oriented databases a better choice than row-oriented databases for data warehousing.

 Figure 3 illustrates the primary difference between row-oriented and column-oriented databases. Rows are packed into their own blocks in a row-oriented database, and columns are packed into their own blocks in a column-oriented database.

![Row-oriented vs. column-oriented databases](http://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/images/row-column-databases.jpg)

*Row-oriented vs. column-oriented databases*

 After faster I/O, the next biggest benefit to using a column-oriented database is improved compression. Because every column is packed into its own set of blocks, every physical block contains the same data type. When all the data is the same data type, the database can use extremely efficient compression algorithms. As a result, you need less storage compared to a row-oriented database. This approach also results in significantly lesser I/O, because the same data is stored in fewer blocks.

 Some column-oriented databases that are used for data warehousing include Amazon Redshift, [Vertica](https://www.vertica.com/), [Greenplum](https://greenplum.org/), [Teradata Aster](https://www.asterdata.com/), [Netezza](https://www.ibm.com/products/netezza), and [Druid](https://druid.apache.org/).

## Massively Parallel Processing (MPP) architectures
<a name="massively-parallel-processing-mpp-architectures"></a>

 An MPP architecture enables you to use all the resources available in the cluster for processing data, which dramatically increases performance of petabyte scale data warehouses. MPP data warehouses allow you improve performance by simply adding more nodes to the cluster. Amazon Redshift, Druid, Vertica, Greenplum, and Teradata Aster are some of the data warehouses built on an MPP architecture. Open-source frameworks such as [Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org/) also support MPP.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
