---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_right_database_solution_access_patterns.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP04 Choose data storage based on access patterns
<a name="perf_right_database_solution_access_patterns"></a>

 Use the access patterns of the workload to decide which services and technologies to use. In addition to non-functional requirements such as performance and scale, access patterns heavily influence the choice of the database and storage solutions. The first dimension is the need for transactions, ACID compliance, and consistent reads. Not every database supports these and most of the NoSQL databases provide an eventual consistency model. The second important dimension would be the distribution of write and reads over time and space. Globally distributed applications need to consider the traffic patterns, latency and access requirements in order to identify the optimal storage solution. The third crucial aspect to choose is the query pattern flexibility, random access patterns, and one-time queries. Considerations around highly specialized query functionality for text and natural language processing, time series, and graphs must also be taken into account.

 **Desired outcome:** The data storage has been selected based on identified and documented data access patterns. This might include the most common read, write and delete queries, the need for ad-hoc calculations and aggregations, complexity of the data, the data interdependency, and the required consistency needs.

 **Common anti-patterns:**
+  You only select one database vendor to simplify operations management.
+  You assume that data access patterns will stay consistent over time.
+  You implement complex transactions, rollback, and consistency logic in the application.
+  The database is configured to support a potential high traffic burst, which results in the database resources remaining idle most of the time.
+  Using a shared database for transactional and analytical uses.

 **Benefits of establishing this best practice:** Selecting and optimizing your data storage based on access patterns will help decrease development complexity and optimize your performance opportunities. Understanding when to use read replicas, global tables, data partitioning, and caching will help you decrease operational overhead and scale based on your workload needs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify and evaluate your data access pattern to select the correct storage configuration. Each database solution has options to configure and optimize your storage solution. Use the collected metrics and logs and experiment with options to find the optimal configuration. Use the following table to review storage options per database service.

|  AWS Services  |  Amazon RDS, Amazon Aurora  |  Amazon DynamoDB  |  Amazon DocumentDB  |  Amazon ElastiCache  |  Amazon Neptune  |  Amazon Timestream  |  Amazon Keyspaces  |  Amazon QLDB  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Scaling Storage  |  Storage automatic scaling option available to automatically scale provisioned storage IOPS can also be scaled independently of provisioned storage when leveraging provisioned IOPs storage types  |  Automatically scales. Tables are unconstrained in terms of size.  |  Storage automatic scaling option available scale provisioned storage  |  Storage is in-memory, tied to instance type or count  |  Storage automatic scaling option available to automatically scale provisioned storage  |  Configure retention period for in-memory and magnetic tiers in days  |  Scales table storage up and down automatically  |  Automatically scales. Tables are unconstrained in terms of size.  |

 **Implementation steps:**

1.  Identify and document the anticipated growth of the data and traffic.

   1.  Amazon RDS and Aurora support storage automatic scaling up to documented limits. Beyond this, consider transitioning older data to Amazon S3 for archival, aggregating historical data for analytics or scaling horizontally via sharding.

   1.  DynamoDB and Amazon S3 will scale to near limitless storage volume automatically.

   1.  Amazon RDS instances and databases running on EC2 can be manually resized and EC2 instances can have new EBS volumes added at a later date for additional storage.

   1.  Instance types can be changed based on changes in activity. For example, you can start with a smaller instance while you are testing, then scale the instance as you begin to receive production traffic to the service. Aurora Serverless V2 automatically scales in response to changes in load.

1.  Document requirements around normal and peak performance (transactions per second TPS and queries per second QPS) and consistency (ACID and eventual consistency).

1.  Document solution deployment aspects and the database access requirements (global, Mult-AZ, read replication, multiple write nodes)

 **Level of effort for the implementation plan: **If you do not have logs or metrics for your data management solution, you will need to complete that before identifying and documenting your data access patterns. Once your data access pattern is understood, selecting, and configuring your data storage is a *low* level of effort.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/)
+ [Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
+ [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
+ [Amazon DynamoDB Accelerator ](https://aws.amazon.com/dynamodb/dax/)
+ [Amazon DynamoDB best practices ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
+ [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
+ [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
+  [Cloud Databases with AWS](https://aws.amazon.com/products/databases/)
+  [Amazon RDS Storage Types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)

 **Related videos:**
+ [AWS purpose-built databases (DAT209-L)](https://www.youtube.com/watch?v=q81TVuV5u28)
+  [Amazon Aurora storage demystified: How it all works (DAT309-R) ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+ [ Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1) ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Experiment and test with Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
