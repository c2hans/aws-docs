---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_right_database_solution_understand_char.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP01 Understand data characteristics
<a name="perf_right_database_solution_understand_char"></a>

 Choose your data management solutions to optimally match the characteristics, access patterns, and requirements of your workload datasets. When selecting and implementing a data management solution, you must ensure that the querying, scaling, and storage characteristics support the workload data requirements. Learn how various database options match your data models, and which configuration options are best for your use-case.

 AWS provides numerous database engines including relational, key-value, document, in-memory, graph, time series, and ledger databases. Each data management solution has options and configurations available to you to support your use-cases and data models. Your workload might be able to use several different database solutions, based on the data characteristics. By selecting the best database solutions to a specific problem, you can break away from monolithic databases, with the one-size-fits-all approach that is restrictive and focus on managing data to meet your customer's need.

 **Desired outcome:** The workload data characteristics are documented with enough detail to facilitate selection and configuration of supporting database solutions, and provide insight into potential alternatives.

 **Common anti-patterns:**
+  Not considering ways to segment large datasets into smaller collections of data that have similar characteristics, resulting in missing opportunities to use more purpose-built databases that better match data and growth characteristics.
+  Not identifying the data access patterns up front, which leads to costly and complex rework later.
+  Limiting growth by using data storage strategies that don’t scale as quickly as is needed
+  Choosing one database type and vendor for all workloads.
+  Sticking to one database solution because there is internal experience and knowledge of one particular type of database solution.
+  Keeping a database solution because it worked well in an on-premises environment.

 **Benefits of establishing this best practice:** Be familiar with all of the AWS database solutions so that you can determine the correct database solution for your various workloads. After you select the appropriate database solution for your workload, you can quickly experiment on each of those database offerings to determine if they continue to meet your workload needs.

 **Level of risk exposed if this best practice is not established:** High
+  Potential cost savings may not be identified.
+  Data may not be secured to the level required.
+  Data access and storage performance may not be optimal.

## Implementation guidance
<a name="implementation-guidance"></a>

 Define the data characteristics and access patterns of your workload. Review all available database solutions to identify which solution supports your data requirements. Within a given workload, multiple databases may be selected. Evaluate each service or group of services and assess them individually. If potential alternative data management solutions are identified for part or all of the data, experiment with alternative implementations that might unlock cost, security, performance, and reliability benefits. Update existing documentation, should a new data management approach be adopted.

|  **Type**  |  **AWS Services**  |  **Key Characteristics**  |  **Common use-cases**  |
| --- | --- | --- | --- |
|  Relational  |  Amazon RDS, Amazon Aurora  |  Referential integrity, ACID transactions, schema on write  |  ERP, CRM, Commercial off-the-shelf software  |
|  Key Value  |  Amazon DynamoDB  |  High throughput, low latency, near-infinite scalability  |  Shopping carts (ecommerce), product catalogs, chat applications  |
|  Document  |  Amazon DocumentDB  |  Store JSON documents and query on any attribute  |  Content Management (CMS), customer profiles, mobile applications  |
|  In Memory  |  Amazon ElastiCache, Amazon MemoryDB  |  Microsecond latency  |  Caching, game leaderboards  |
|  Graph  |  Amazon Neptune  |  Highly relational data where the relationships between data have meaning  |  Social networks, personalization engines, fraud detection  |
|  Time Series  |  Amazon Timestream  |  Data where the primary dimension is time  |  DevOps, IoT, Monitoring  |
|  Wide column  |  Amazon Keyspaces  |  Cassandra workloads.  |  Industrial equipment maintenance, route optimization  |
|  Ledger  |  Amazon QLDB  |  Immutable and cryptographically verifiable ledger of changes  |  Systems of record, healthcare, supply chains, financial institutions  |

 **Implementation steps**

1.  How is the data structured? (for example, unstructured, key-value, semi-structured, relational)

   1.  If the data is unstructured, consider an object-store such as [Amazon S3](https://aws.amazon.com/products/storage/data-lake-storage/) or a NoSQL database such as [Amazon DocumentDB.](https://aws.amazon.com/documentdb/)

   1.  For key-value data, consider [DynamoDB](https://aws.amazon.com/documentdb/), [ElastiCache for Redis](https://aws.amazon.com/elasticache/redis/) or [MemoryDB.](https://aws.amazon.com/memorydb/)

   1.  If the data has a relational structure, what level of referential integrity is required?

      1.  For foreign key constraints, relational databases such as [Amazon RDS](https://aws.amazon.com/rds/) and [Aurora](https://aws.amazon.com/rds/aurora/) can provide this level of integrity.

      1.  Typically, within a NoSQL data-model, you would de-normalize your data into a single document or collection of documents to be retrieved in a single request rather than joining across documents or tables.

1.  Is ACID (atomicity, consistency, isolation, durability) compliance required?

   1.  If the ACID properties associated with relational databases are required, consider a relational database such as [Amazon RDS](https://aws.amazon.com/rds/) and [Aurora.](https://aws.amazon.com/rds/aurora/)

1.  What consistency model is required?

   1.  If your application can tolerate eventual consistency, consider a NoSQL implementation. Review the other characteristics to help choose which [NoSQL database](https://aws.amazon.com/nosql/) is most appropriate.

   1.  If strong consistency is required, you can use strongly consistent reads with [DynamoDB](https://aws.amazon.com/documentdb/) or a relational database such as [Amazon RDS](https://aws.amazon.com/rds/).

1.  What query and result formats must be supported? (for example, SQL, CSV, Parque, Avro, JSON, etc.)

1.  What data types, field sizes and overall quantities are present? (for example, text, numeric, spatial, time-series calculated, binary or blob, document)

1.  How will the storage requirements change over time? How does this impact scalability?

   1.  Serverless databases such as [DynamoDB](https://aws.amazon.com/documentdb/) and [Amazon Quantum Ledger Database](https://aws.amazon.com/qldb/) will scale dynamically up to near-unlimited storage.

   1.  Relational databases have upper bounds on provisioned storage, and often must be horizontally partitioned via mechanisms such as sharding once they reach these limits.

1.  What is the proportion of read queries in relation to write queries? Would caching be likely to improve performance?

   1.  Read-heavy workloads can benefit from a caching layer, this could be [ElastiCache](https://aws.amazon.com/elasticache/) or [DAX](https://aws.amazon.com/dynamodb/dax/) if the database is DynamoDB.

   1.  Reads can also be offloaded to read replicas with relational databases such as [Amazon RDS](https://aws.amazon.com/rds/).

1.  Does storage and modification (OLTP - Online Transaction Processing) or retrieval and reporting (OLAP - Online Analytical Processing) have a higher priority?

   1.  For high-throughput transactional processing, consider a NoSQL database such as DynamoDB or Amazon DocumentDB.

   1.  For analytical queries, consider a columnar database such as [Amazon Redshift](https://aws.amazon.com/redshift/) or exporting the data to Amazon S3 and performing analytics using [Athena](https://aws.amazon.com/athena/) or [QuickSight.](https://aws.amazon.com/quicksight/)

1.  How sensitive is this data and what level of protection and encryption does it require?

   1.  All Amazon RDS and Aurora engines support data encryption at rest using AWS KMS. Microsoft SQL Server and Oracle also support native Transparent Data Encryption (TDE) when using Amazon RDS.

   1.  For DynamoDB, you can use fine-grained access control with [IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-overview.html) to control who has access to what data at the key level.

1.  What level of durability does the data require?

   1.  Aurora automatically replicates your data across three Availability Zones within a Region, meaning your data is highly durable with less chance of data loss.

   1.  DynamoDB is automatically replicated across multiple Availability Zones, providing high availability and data durability.

   1.  Amazon S3 provides 11 9s of durability. Many database services such as Amazon RDS and DynamoDB support exporting data to Amazon S3 for long-term retention and archival.

1.  Do [Recovery Time Objective (RTO) or Recovery Point Objectives (RPO)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html) requirements influence the solution?

   1.  Amazon RDS, Aurora, DynamoDB, Amazon DocumentDB, and Neptune all support point in time recovery and on-demand backup and restore.

   1.  For high availability requirements, DynamoDB tables can be replicated globally using the [Global Tables](https://aws.amazon.com/dynamodb/global-tables/) feature and Aurora clusters can be replicated across multiple Regions using the Global database feature. Additionally, S3 buckets can be replicated across AWS Regions using cross-region replication.

1.  Is there a desire to move away from commercial database engines / licensing costs?

   1.  Consider open-source engines such as PostgreSQL and MySQL on Amazon RDS or Aurora

   1.  Leverage [AWS DMS](https://aws.amazon.com/dms/) and [AWS SCT](https://aws.amazon.com/dms/schema-conversion-tool/) to perform migrations from commercial database engines to open-source

1.  What is the operational expectation for the database? Is moving to managed services a primary concern?

   1.  Leveraging Amazon RDS instead of Amazon EC2, and DynamoDB or Amazon DocumentDB instead of self-hosting a NoSQL database can reduce operational overhead.

1.  How is the database currently accessed? Is it only application access, or are there Business Intelligence (BI) users and other connected off-the-shelf applications?

   1.  If you have dependencies on external tooling then you may have to maintain compatibility with the databases they support. Amazon RDS is fully compatible with the difference engine versions that it supports including Microsoft SQL Server, Oracle, MySQL, and PostgreSQL.

1.  The following is a list of potential data management services, and where these can best be used:

   1.  Relational databases store data with predefined schemas and relationships between them. These databases are designed to support ACID (atomicity, consistency, isolation, durability) transactions, and maintain referential integrity and strong data consistency. Many traditional applications, enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce use relational databases to store their data. You can run many of these database engines on Amazon EC2, or choose from one of the AWS-managed [database services](https://aws.amazon.com/products/databases/): [Amazon Aurora](https://aws.amazon.com/rds/aurora), [Amazon RDS](https://aws.amazon.com/rds), and [Amazon Redshift](https://aws.amazon.com/redshift).

   1.  Key-value databases are optimized for common access patterns, typically to store and retrieve large volumes of data. These databases deliver quick response times, even in extreme volumes of concurrent requests. High-traffic web apps, ecommerce systems, and gaming applications are typical use-cases for key-value databases. In AWS, you can utilize [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), a fully managed, multi-Region, multi-master, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.

   1.  In-memory databases are used for applications that require real-time access to data, lowest latency and highest throughput. By storing data directly in memory, these databases deliver microsecond latency to applications where millisecond latency is not enough. You may use in-memory databases for application caching, session management, gaming leaderboards, and geospatial applications. [Amazon ElastiCache](https://aws.amazon.com/elasticache/) is a fully managed in-memory data store, compatible with [Redis](https://aws.amazon.com/elasticache/redis/) or [Memcached](https://aws.amazon.com/elasticache/memcached). In case the applications also higher durability requirements, [Amazon MemoryDB for Redis](https://aws.amazon.com/memorydb/) offers this in combination being a durable, in-memory database service for ultra-fast performance.

   1.  A document database is designed to store semistructured data as JSON-like documents. These databases help developers build and update applications such as content management, catalogs, and user profiles quickly. [Amazon DocumentDB](https://aws.amazon.com/documentdb/) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.

   1.  A wide column store is a type of NoSQL database. It uses tables, rows, and columns, but unlike a relational database, the names and format of the columns can vary from row to row in the same table. You typically see a wide column store in high scale industrial apps for equipment maintenance, fleet management, and route optimization. [Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/mcs/) is a wide column scalable, highly available, and managed Apache Cassandra–compatible database service.

   1.  Graph databases are for applications that must navigate and query millions of relationships between highly connected graph datasets with millisecond latency at large scale. Many companies use graph databases for fraud detection, social networking, and recommendation engines. [Amazon Neptune](https://aws.amazon.com/neptune/) is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets.

   1.  Time-series databases efficiently collect, synthesize, and derive insights from data that changes over time. IoT applications, DevOps, and industrial telemetry can utilize time-series databases. [Amazon Timestream](https://aws.amazon.com/timestream/) is a fast, scalable, fully managed time series database service for IoT and operational applications that makes it easy to store and analyze trillions of events per day.

   1.  Ledger databases provide a centralized and trusted authority to maintain a scalable, immutable, and cryptographically verifiable record of transactions for every application. We see ledger databases used for systems of record, supply chain, registrations, and even banking transactions. [Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/qldb/) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. Amazon QLDB tracks every application data change and maintains a complete and verifiable history of changes over time.

 **Level of effort for the implementation plan: **If a workload is moving from one database solution to another, there could be a *high* level of effort involved in refactoring the data and application.

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
+  [Choose between EC2 and Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/comparison.html)
+  [Best Practices for Implementing Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html)

 **Related videos:**
+ [AWS purpose-built databases (DAT209-L) ](https://www.youtube.com/watch?v=q81TVuV5u28)
+ [Amazon Aurora storage demystified: How it all works (DAT309-R) ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+ [Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1) ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Optimize Data Pattern using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/)
+  [Database Migrations](https://github.com/aws-samples/aws-database-migration-samples)
+  [MS SQL Server - AWS Database Migration Service (DMS) Replication Demo](https://github.com/aws-samples/aws-dms-sql-server)
+  [Database Modernization Hands On Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop)
+  [Amazon Neptune Samples](https://github.com/aws-samples/amazon-neptune-samples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
