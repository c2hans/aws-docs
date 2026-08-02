---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/query-performance-factors.html
---

# Query performance factors for Amazon Redshift
<a name="query-performance-factors"></a>

A number of factors can affect query performance. The following aspects of your data, cluster, and database operations all play a part in how quickly your queries are processed:
+ [Table properties](#table-properties)
  + Sort keys (Amazon Redshift Advisor)
  + Data compression (automated)
  + Data distribution (automated)
  + Table maintenance (automated)
+ [Cluster configuration](#cluster-configuration)
  + Node type
  + Node size, number of nodes, and slices
  + Workload management (automated)
  + Short query acceleration (automated)
+ [SQL query](#query)
  + Query structure
  + Code compilation

## Table properties
<a name="table-properties"></a>

Amazon Redshift tables are the fundamental units for storing data in Amazon Redshift, and each table has a set of properties that determine its behavior and accessibility. These properties include sorting, distribution style, compression encoding, and many others. Understanding these properties is crucial for optimizing the performance, security, and cost-effectiveness of Amazon Redshift tables.

### Sort keys
<a name="sort-keys.b6d26c40-2bd4-55f5-9920-92d439163363"></a>

Amazon Redshift stores data on disk in sorted order according to a table's sort keys. The query optimizer and the query processor use the information about where the data is located within a compute node to reduce the number of blocks that must be scanned. This improves query speed significantly by reducing the amount of data to process. We recommend that you use sort keys to facilitate filters in the `WHERE` clause. For more information, see [Working with sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html) in the Amazon Redshift documentation.

### Data compression
<a name="data-compression.46d4e361-db26-5985-8754-195c5fc941a3"></a>

Data compression reduces storage requirements, which reduces disk I/O and improves query performance. When you run a query, the compressed data is read into memory and then uncompressed when the query runs. By loading less data into memory, Amazon Redshift can allocate more memory to analyzing the data. Because columnar storage stores similar data sequentially, Amazon Redshift can apply adaptive compression encodings specifically tied to columnar data types. The best way to enable data compression on table columns is by using the `AUTO` option in Amazon Redshift to apply optimal compression encodings when you load the table with data. To learn more about using automatic data compression, see [Loading tables with automatic compression](https://docs.aws.amazon.com/redshift/latest/dg/c_Loading_tables_auto_compress.html) in the Amazon Redshift documentation.

### Data distribution
<a name="data-distribution.1e056e95-9c1a-5116-8c3d-41b67369f4f4"></a>

Amazon Redshift stores data on the compute nodes according to a table's distribution style. When you run a query, the query optimizer redistributes the data to the compute nodes as needed to perform any joins and aggregations. Choosing the right distribution style for a table helps minimize the impact of the redistribution step by locating the data where it needs to be before the joins are performed. We recommend that you use distribution keys to facilitate the most common joins. For more information, see [Working with data distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html) in the Amazon Redshift documentation.

### Table maintenance
<a name="table-maintenance.9acf7cb6-eb5e-535e-afc8-f4ba6d16249b"></a>

Although Amazon Redshift provides industry-leading performance out of the box for most workloads, keeping Amazon Redshift clusters running well requires maintenance. Updating and deleting data creates dead rows that must be vacuumed, and even append-only tables must be resorted if the append order isn't consistent with the sort key.

#### Vacuum
<a name="vacuum.dd0ea9e7-6988-5c75-bab8-4de80389ae0e"></a>

The vacuuming process in Amazon Redshift is essential for the health and maintenance of your Amazon Redshift cluster. It also affects the performance of queries. Because deletes and updates both flag the old data but don't actually remove it, you must use vacuuming to reclaim the disk space that was occupied by table rows that were marked for deletion by the previous `UPDATE` and `DELETE` operations. Amazon Redshift can automatically sort and perform a `VACUUM DELETE` operation on tables in the background.

To clean up tables after a load or a series of incremental updates, you can also run the `VACUUM` command, either against the entire database or against individual tables. If tables have sort keys and table loads aren't optimized to sort as they insert, then you must use vacuums to resort the data (which can be crucial for performance). For more information, see [Vacuuming tables](https://docs.aws.amazon.com/redshift/latest/dg/t_Reclaiming_storage_space202.html) in the Amazon Redshift documentation.

#### Analyze
<a name="analyze.f2a1abd4-013f-5aac-a06f-3c169a7c4723"></a>

The `ANALYZE` operation updates statistical metadata on the tables in an Amazon Redshift database. Keeping statistics current improves query performance by enabling the query planner to choose optimal plans. Amazon Redshift continuously monitors your database and automatically performs analyze operations in the background. To minimize impact to your system performance, the `ANALYZE` operation automatically runs during periods when workloads are light. If you choose to explicitly run `ANALYZE`, do the following:
+ Run the `ANALYZE` command before running queries.
+ Run the `ANALYZE` command on the database routinely at the end of every regular load or update cycle.
+ Run the `ANALYZE` command on new tables that you create and existing tables or columns that undergo significant change.
+ Consider running `ANALYZE` operations on different schedules for different types of tables and columns, depending on their use in queries and their propensity to change.
+ To save time and cluster resources, use the `PREDICATE COLUMNS` clause when you run the `ANALYZE` command.

## Cluster configuration
<a name="cluster-configuration"></a>

A cluster is a collection of nodes which perform the actual storing and processing of data. Setting up your Amazon Redshift cluster the right way is critical if you want to achieve the following:
+ High scalability and concurrency
+ Efficient use of Amazon Redshift
+ Better performance
+ Lower cost

### Node type
<a name="node-type.9031d14a-69a1-5896-b208-d3f431e5cdbe"></a>

An Amazon Redshift cluster can use one of several node types (RA3, DC2, and DS2). Each node type offers different sizes and limits to help you scale your cluster appropriately. The node size determines the storage capacity, memory, CPU, and price of each node in the cluster. Cost and performance optimization starts with choosing the right node type and size. For more information about node types, see [Overview of Amazon Redshift clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#working-with-clusters-overview) in the Amazon Redshift documentation.

### Node size, number of nodes, and slices
<a name="node-size--number-of-nodes--and-slices.0691242d-210f-50a0-b9e8-07eb1d5e6bd5"></a>

A compute node is partitioned into slices. More nodes means more processors and slices, which enables your queries to process faster by running portions of the query concurrently across the slices. However, more nodes also means greater expense. This means that you must find the balance of cost and performance that is appropriate for your system. For more information on Amazon Redshift cluster architecture, see [Data warehouse system architecture](https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html) in the Amazon Redshift documentation.

### Workload management
<a name="workload-management.96d798fd-6b36-5f35-8cbf-01c96cab14d3"></a>

Amazon Redshift workload management (WLM) enables users to flexibly manage workload queues with priorities so that short, fast-running queries won't get stuck in queues behind long-running queries. Automatic WLM uses machine learning (ML) algorithms to profile queries and place them in the appropriate queue with the appropriate resources, while managing query concurrency and memory allocation. For more information about WLM, see [Implementing workload management](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-implementing-workload-management.html) in the Amazon Redshift documentation.

### Short query acceleration
<a name="short-query-acceleration.39294664-4735-587c-9728-4a9af2cf81b7"></a>

Short query acceleration (SQA) prioritizes short-running queries ahead of long-running queries. SQA runs queries in a dedicated space so that SQA queries aren't forced to wait in queues behind longer queries. SQA only prioritizes queries that are short-running and are in a user-defined queue. If you use SQA, short-running queries begin running more quickly and you can see results sooner. If you enable SQA, you can reduce or eliminate WLM queues that are dedicated to short-running queries. In addition, long-running queries don't need to contend for slots in a WLM queue. This means that you can configure your WLM queues to use fewer query slots. If you use lower concurrency, query throughput is increased and overall system performance is improved for most workloads. For more information about SQA, see [Working with short query acceleration](https://docs.aws.amazon.com/redshift/latest/dg/wlm-short-query-acceleration.html) in the Amazon Redshift documentation.

## SQL query
<a name="query"></a>

A database query is a request for data from a database. The request should come in an Amazon Redshift cluster using SQL. Amazon Redshift supports SQL client tools that connect through Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC). You can use most SQL client tools that support JDBC or ODBC drivers.

### Query structure
<a name="query-structure.0e0aae5b-4de9-5fc4-a800-0fb1799fddb9"></a>

How your query is written greatly affects its performance. We recommend that you write queries to process and return as little data as necessary to meet your needs. For more information on how to structure your queries, see the [Best practices for designing Amazon Redshift queries](best-practices-designing-queries.md) section of this guide.

### Code compilation
<a name="code-compilation.6480821a-7dde-5cb8-9cbf-c012e8f3ab20"></a>

Amazon Redshift generates and compiles optimized code for each query execution plan. The compiled code runs faster because it eliminates the overhead of using an interpreter. To minimize latency for new queries while preserving the performance benefits of compiled code, Amazon Redshift uses a technique called *composition*. Composition generates a lightweight arrangement of pre-existing logic to process new queries immediately, while simultaneously compiling highly optimized, query-specific code in the background. This removes compilation from the critical path of query execution. This means that new queries start faster and deliver performance consistent with subsequent runs.

Amazon Redshift also uses a serverless compilation service to scale query compilations beyond the compute resources of an Amazon Redshift cluster. Compiled code segments are cached both locally on the cluster and in a virtually unlimited remote cache that persists after cluster reboots. Subsequent executions of the same query run faster because they can skip the compilation phase. By using a scalable compilation service, Amazon Redshift compiles code in parallel to provide consistently fast performance.
