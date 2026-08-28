---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_right_database_solution_access_patterns.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP04 Choose data storage based on access patterns
<a name="perf_right_database_solution_access_patterns"></a>

Use the access patterns of the workload and requirements of the applications to decide on optimal data services and technologies to use.

 **Desired outcome:** Data storage has been selected based on identiﬁed and documented data access patterns. This might include the most common read, write, and delete queries, the need for as necessary calculations and aggregations, complexity of the data, data interdependency, and the required consistency needs.

 **Common anti-patterns:**
+ You only select one database engine to simplify operations management.
+  You assume that data access patterns will stay consistent over time.
+  You implement complex transactions, rollback, and consistency logic in the application.
+  The database is configured to support a potential high traffic burst, which results in the database resources remaining idle most of the time.
+  Using a shared database for transactional and analytical uses.

 **Benefits of establishing this best practice:** Selecting and optimizing your data storage based on access patterns will help decrease development complexity and optimize your performance opportunities. Understanding when to use read replicas, global tables, data partitioning, and caching will help you decrease operational overhead and scale based on your workload needs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Identify and evaluate your data access pattern to select the correct storage conﬁguration. Each database solution has options to conﬁgure and optimize your storage solution. Use the collected metrics and logs and experiment with options to ﬁnd the optimal conﬁguration. Use the following table to review storage options per database service.

|  AWS Services  |  Amazon RDS  |  Amazon Aurora  |  Amazon DynamoDB  |  Amazon DocumentDB  |  Amazon ElastiCache  |  Amazon Neptune  |  Amazon Timestream  |  Amazon Keyspaces  |  Amazon QLDB  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Scaling Storage  | Storage can be scaled up manually or configured to scale automatically to a maximum of 64 TiB based on engine types. Provisioned storage cannot be decreased. |  Storage scales automatically up to maximum of 128 TiB and decreases when data is removed. Maximum storage size also depends upon specific Aurora MySQL or Aurora Postgres engine versions.  | Storage automatically scales. Tables are unconstrained in terms of size. | Storage scales automatically up to maximum of 64 TiB. Starting Amazon DocumentDB 4.0 storage can decrease by comparable amounts for data removal through dropping a collection or index. With Amazon DocumentDB 3.6 allocated space remains same and free space is reused when data volume increases. |  Storage is in-memory, tied to instance type or count.  |  Storage scales automatically can grow up to 128 TiB (or 64 TiB in few Regions). Upon data removal from, total allocated space remains same and is reused in the future.  | Organizes your time series data to optimize query processing and reduce storage costs. Retention period can be configured through in-memory and magnetic tiers. | Scales table storage up and down automatically as your application writes, updates, and deletes data. | Storage automatically scales. Tables are unconstrained in terms of size. |

 **Implementation steps:**

1.  Understand the requirement of transactions, atomicity, consistency, isolation, and durability (ACID) compliance, and consistent reads. Not every database supports these and most of the NoSQL databases provide an eventual consistency model.

1.  Consider the traffic patterns, latency, and access requirements for a globally distributed application in order to identify the optimal storage solution.

1.  Analyze query patterns, random access patterns and one-time queries. Considerations around highly specialized query functionality for text and natural language processing, time series, and graphs must also be taken into account.

1.  Identify and document the anticipated growth of the data and traffic.

   1.  Amazon RDS and Aurora support storage automatic scaling up to documented limits. Beyond this, consider transitioning older data to Amazon S3 for archival, aggregating historical data for analytics or scaling horizontally using sharding.

   1.  DynamoDB and Amazon S3 will scale to near limitless storage volume automatically.

   1.  Amazon RDS instances and databases running on EC2 can be manually resized and EC2 instances can have new EBS volumes added at a later date for additional storage.

   1.  Instance types can be changed based on changes in activity. For example, you can start with a smaller instance while you are testing, then scale the instance as you begin to receive production traffic to the service. Aurora Serverless V2 automatically scales in response to changes in load.

1. Baseline requirements around normal and peak performance (transactions per second TPS and queries per second QPS) and consistency (ACID and eventual consistency).

1.  Document solution deployment aspects and the database access requirements (like global replication, Multi-AZ, read replication, and multiple write nodes).

 **Level of effort for the implementation plan: ** Low. If you do not have logs or metrics for your data management solution, you will need to complete that before identifying and documenting your data access patterns. Once your data access pattern is understood, selecting and conﬁguring your data storage is a low level of eﬀort.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ Cloud Databases with AWS](https://aws.amazon.com/products/databases/)
+ [ Working with storage for Amazon RDS DB instances ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html)
+ [ Amazon DocumentDB Storage ](https://docs.aws.amazon.com/documentdb/latest/developerguide/how-it-works.html#how-it-works.storage)
+ [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/)
+ [ Amazon Timestream Storage ](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html)
+ [ Storage in Amazon Keyspaces ](https://docs.aws.amazon.com/keyspaces/latest/devguide/Storage.html)
+ [ Amazon ElastiCache FAQs ](https://aws.amazon.com/elasticache/faqs/)
+ [ Amazon Neptune storage, reliability, and availability ](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html)
+ [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
+ [Amazon DynamoDB Accelerator ](https://aws.amazon.com/dynamodb/dax/)
+ [Amazon DynamoDB best practices ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
+  [Amazon RDS Storage Types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)
+ [ Hardware specifications for Amazon RDS instance classes ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Types)
+ [ Aurora Storage limits ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html#RDS_Limits.FileSize.Aurora)

 **Related videos:**
+ [AWS purpose-built databases (DAT209-L)](https://www.youtube.com/watch?v=q81TVuV5u28)
+  [Amazon Aurora storage demystified: How it all works (DAT309-R) ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+ [ Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1) ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Experiment and test with Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
