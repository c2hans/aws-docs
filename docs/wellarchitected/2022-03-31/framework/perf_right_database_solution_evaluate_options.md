---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_right_database_solution_evaluate_options.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP02 Evaluate the available options
<a name="perf_right_database_solution_evaluate_options"></a>

 Understand the available database options and how it can optimize your performance before you select your data management solution. Use load testing to identify database metrics that matter for your workload. While you explore the database options, take into consideration various aspects such as the parameter groups, storage options, memory, compute, read replica, eventual consistency, connection pooling, and caching options. Experiment with these various configuration options to improve the metrics.

 **Desired outcome:** A workload could have one or more database solutions used based on data types. The database functionality and benefits optimally match the data characteristics, access patterns, and workload requirements. To optimize your database performance and cost, you must evaluate the data access patterns to determine the appropriate database options. Evaluate the acceptable query times to ensure that the selected database options can meet the requirements.

 **Common anti-patterns:**
+  Not identifying the data access patterns.
+  Not being aware of the configuration options of your chosen data management solution.
+  Relying solely on increasing the instance size without looking at other available configuration options.
+  Not testing the scaling characteristics of the chosen solution.

 **Benefits of establishing this best practice:** By exploring and experimenting with the database options you may be able to reduce the cost of infrastructure, improve performance and scalability and lower the effort required to maintain your workloads.

 **Level of risk exposed if this best practice is not established:** High
+  Having to optimize for a *one size fits all* database means making unnecessary compromises.
+  Higher costs as a result of not configuring the database solution to match the traffic patterns.
+  Operational issues may emerge from scaling issues.
+  Data may not be secured to the level required.

## Implementation guidance
<a name="implementation-guidance"></a>

 Understand your workload data characteristics so that you can configure your database options. Run load tests to identify your key performance metrics and bottlenecks. Use these characteristics and metrics to evaluate database options and experiment with different configurations.

|  AWS Services  |  Amazon RDS, Amazon Aurora  |  Amazon DynamoDB  |  Amazon DocumentDB  |  Amazon ElastiCache  |  Amazon Neptune  |  Amazon Timestream  |  Amazon Keyspaces  |  Amazon QLDB  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Scaling Compute  |  Increase instance size, Aurora Serverless instances autoscale in response to changes in load  |  Automatic read/write scaling with on-demand capacity mode or automatic scaling of provisioned read/write capacity in provisioned capacity mode  |  Increase instance size  |  Increase instance size, add nodes to cluster  |  Increase instance size  |  Automatically scales to adjust capacity  |  Automatic read/write scaling with on-demand capacity mode or automatic scaling of provisioned read/write capacity in provisioned capacity mode  |  Automatically scales to adjust capacity  |
|  Scaling-out reads  |  All engines support read replicas. Aurora supports automatic scaling of read replica instances  |  Increase provisioned read capacity units  |  Read replicas  |  Read replicas  |  Read replicas. Supports automatic scaling of read replica instances  |  Automatically scales  |  Increase provisioned read capacity units  |  Automatically scales up to documented concurrency limits  |
|  Scaling-out writes  |  Increasing instance size, batching writes in the application or adding a queue in front of the database. Horizontal scaling via application-level sharding across multiple instances  |  Increase provisioned write capacity units. Ensuring optimal partition key to prevent partition level write throttling  |  Increasing primary instance size  |  Using Redis in cluster mode to distribute writes across shards  |  Increasing instance size  |  Write requests may be throttled while scaling. If you encounter throttling exceptions, continue to send data at the same (or higher) throughput to automatically scale. Batch writes to reduce concurrent write requests  |  Increase provisioned write capacity units. Ensuring optimal partition key to prevent partition level write throttling  |  Automatically scales up to documented concurrency limits  |
|  Engine configuration  |  Parameter groups  |  Not applicable  |  Parameter groups  |  Parameter groups  |  Parameter groups  |  Not applicable  |  Not applicable  |  Not applicable  |
|  Caching  |  In-memory caching, configurable via parameter groups. Pair with a dedicated cache such as ElastiCache for Redis to offload requests for commonly accessed items  |  DAX (DAX) fully managed cache available  |  In-memory caching. Optionally, pair with a dedicated cache such as ElastiCache for Redis to offload requests for commonly accessed items  |  Primary function is caching  |  Use the query results cache to cache the result of a read-only query  |  Timestream has two storage tiers; one of these is a high-performance in-memory tier  |  Deploy a separate dedicated cache such as ElastiCache for Redis to offload requests for commonly accessed items  |  Not applicable  |
|  High availability / disaster recovery  |  Recommended configuration for production workloads is to run a standby instance in a second Availability Zone to provide resiliency within a Region.  For resiliency across Regions, Aurora Global Database can be used  |  Highly available within a Region. Tables can be replicated across Regions using DynanoDB global tables  |  Create multiple instances across Availability Zones for availability.  Snapshots can be shared across Regions and clusters can be replicated using DMS to provide Cross-Region Replication / disaster recovery  |  Recommended configuration for production clusters is to create at least one node in a secondary Availability Zone.  ElastiCache Global Datastore can be used to replicate clusters across Regions.  |  Read replicas in other Availability Zones serve as failover targets.  Snapshots can be shared across Region and clusters can be replicated using Neptune streams to replicate data between two clusters in two different Regions.  |  Highly available within a Region.  cross-Region replication requires custom application development using the Timestream SDK  |  Highly available within a Region.  Cross-Region Replication requires custom application logic or third-party tools  |  Highly available within a Region.  To replicate across Regions, export the contents of the Amazon QLDB journal to a S3 bucket and configure the bucket for Cross-Region Replication.  |

 **Implementation steps**

1.  What configuration options are available for the selected databases?

   1.  Parameter Groups for Amazon RDS and Aurora allow you to adjust common database engine level settings such as the memory allocated for the cache or adjusting the time zone of the database

   1.  For provisioned database services such as Amazon RDS, Aurora, Neptune, Amazon DocumentDB and those deployed on Amazon EC2 you can change the instance type, provisioned storage and add read replicas.

   1.  DynamoDB allows you to specify two capacity modes: on-demand and provisioned. To account for differing workloads, you can change between these modes and increase the allocated capacity in provisioned mode at any time.

1.  Is the workload read or write heavy?

   1.  What solutions are available for offloading reads (read replicas, caching, etc.)?

      1.  For DynamoDB tables, you can offload reads using DAX for caching.

      1.  For relational databases, you can create an ElastiCache for Redis cluster and configure your application to read from the cache first, falling back to the database if the requested item is not present.

      1.  Relational databases such as Amazon RDS and Aurora, and provisioned NoSQL databases such as Neptune and Amazon DocumentDB all support adding read replicas to offload the read portions of the workload.

      1.  Serverless databases such as DynamoDB will scale automatically. Ensure that you have enough read capacity units (RCU) provisioned to handle the workload.

   1.  What solutions are available for scaling writes (partition key sharding, introducing a queue, etc.)?

      1.  For relational databases, you can increase the size of the instance to accommodate an increased workload or increase the provisioned IOPs to allow for an increased throughput to the underlying storage.
         +  You can also introduce a queue in front of your database rather than writing directly to the database. This pattern allows you to decouple the ingestion from the database and control the flow-rate so the database does not get overwhelmed.
         +  Batching your write requests rather than creating many short-lived transactions can help improve throughput in high-write volume relational databases.

      1.  Serverless databases like DynamoDB can scale the write throughput automatically or by adjusting the provisioned write capacity units (WCU) depending on the capacity mode.
         +  You can still run into issues with *hot* partitions though, when you reach the throughput limits for a given partition key. This can be mitigated by choosing a more evenly distributed partition key or by write-sharding the partition key.

1.  What are the current or expected peak transactions per second (TPS)? Test using this volume of traffic and this volume \+X% to understand the scaling characteristics.

   1.  Native tools such as pg\_bench for PostgreSQL can be used to stress-test the database and understand the bottlenecks and scaling characteristics.

   1.  Production-like traffic should be captured so that it can be replayed to simulate real-world conditions in addition to synthetic workloads.

1.  If using serverless or elastically scalable compute, test the impact of scaling this on the database. If appropriate, introduce connection management or pooling to lower impact on the database.

   1.  RDS Proxy can be used with Amazon RDS and Aurora to manage connections to the database.

   1.  Serverless databases such as DynamoDB do not have connections associated with them, but consider the provisioned capacity and automatic scaling policies to deal with spikes in load.

1.  Is the load predictable, are there spikes in load and periods of inactivity?

   1.  If there are periods of inactivity consider scaling down the provisioned capacity or instance size during these times. Aurora Serverless V2 will automatically scale up and down based on load.

   1.  For non-production instances, consider pausing or stopping these during non-work hours.

1.  Do you need to segment and break apart your data models based on access patterns and data characteristics?

   1.  Consider using AWS DMS or AWS SCT to move your data to other services.

## Level of effort for the implementation plan:
<a name="level-of-effort-for-the-implementation-plan-to-establish-this-best-practice-you-must-be-aware-of-your-current-data-characteristics-and-metrics.-gathering-those-metrics-establishing-a-baseline-and-then-using-those-metrics-to-identify-the-ideal-database-configuration-options-is-a-low-to-moderate-level-of-effort.-this-is-best-validated-by-load-tests-and-experimentation."></a>

To establish this best practice, you must be aware of your current data characteristics and metrics. Gathering those metrics, establishing a baseline and then using those metrics to identify the ideal database configuration options is a *low* to *moderate* level of effort. This is best validated by load tests and experimentation.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Databases with AWS ](https://aws.amazon.com/products/databases/?ref=wellarchitected)
+  [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
+  [Amazon DynamoDB Accelerator ](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected)
+  [Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
+  [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
+  [Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
+  [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected)
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected)

 **Related videos:**
+  [AWS purpose-built databases (DAT209-L) ](https://www.youtube.com/watch?v=q81TVuV5u28)
+ [Amazon Aurora storage demystified: How it all works (DAT309-R) ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+  [Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1) ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Amazon DynamoDB Examples](https://github.com/aws-samples/aws-dynamodb-examples)
+  [AWS Database migration samples](https://github.com/aws-samples/aws-database-migration-samples)
+  [Database Modernization Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop)
+  [Working with parameters on your Amazon RDS for Postgress DB](https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
