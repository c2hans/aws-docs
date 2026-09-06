---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_data_implement_strategies_to_improve_query_performance.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF03-BP04 Implement strategies to improve query performance in data store
<a name="perf_data_implement_strategies_to_improve_query_performance"></a>

 Implement strategies to optimize data and improve data query to enable more scalability and efficient performance for your workload.

 **Common anti-patterns:**
+  You do not partition data in your data store.
+  You store data in only one file format in your data store.
+  You do not use indexes in your data store.

 **Benefits of establishing this best practice:** Optimizing data and query performance results in more efficiency, lower cost, and improved user experience.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Data optimization and query tuning are critical aspects of performance efficiency in a data store, as they impact the performance and responsiveness of the entire cloud workload. Unoptimized queries can result in greater resource usage and bottlenecks, which reduce the overall efficiency of a data store.

Data optimization includes several techniques to ensure efficient data storage and access. This also help to improve the query performance in a data store. Key strategies include data partitioning, data compression, and data denormalization, which help data to be optimized for both storage and access.

### Implementation steps
<a name="implementation-steps"></a>
+  Understand and analyze the critical data queries which are performed in your data store.
+  Identify the slow-running queries in your data store and use query plans to understand their current state.
  +  [Analyzing the query plan in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c-analyzing-the-query-plan.html)
  +  [Using EXPLAIN and EXPLAIN ANALYZE in Athena](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement.html)
+  Implement strategies to improve the query performance. Some of the key strategies include:
  +  Using a [columnar file format](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html) (like Parquet or ORC).
  + Compressing data in the data store to reduce storage space and I/O operation.
  +  Data partitioning to split data into smaller parts and reduce data scanning time.
    + [ Partitioning data in Athena ](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)
    + [ Partitions and data distribution ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)
  +  Data indexing on the common columns in the query.
  +  Choose the right join operation for the query. When you join two tables, specify the larger table on the left side of join and the smaller table on the right side of the join.
  +  Distributed caching solution to improve latency and reduce the number of database I/O operation.
  +  Regular maintenance such as executing statistics.
+  Experiment and test strategies in a non-production environment.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
+  [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
+  [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
+  [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
+  [Best Practices for Implementing Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html)
+  [Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)

 **Related videos:**
+  [Optimize Data Pattern using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/)
+  [Optimize Amazon Athena Queries with New Query Analysis Tools ](https://www.youtube.com/watch?v=7JUyTqglmNU&ab_channel=AmazonWebServices)

 **Related examples:**
+  [Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver)
