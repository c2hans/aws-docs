---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/database-configuration-backup-and-failover.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database configuration, backup, and failover
<a name="database-configuration-backup-and-failover"></a>

Many web applications contain some form of persistence, usually in the form of a relational or non-relational [database](https://aws.amazon.com/products/databases/). AWS offers both relational and non-relational database services. Alternatively, you can deploy your own database software on an EC2 instance. The following table summarizes these options, which are discussed in greater detail in this section.

*Table 1 — Relational and non-relational database solutions*

|   |  Relational Database Solutions  |  NoSQL Solutions  |
| --- | --- | --- |
|  Managed database service  |  [Amazon RDS for MySQL](https://aws.amazon.com/rds/mysql/), [Oracle,](https://www.oracle.com/index.html) [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads), [MariaDB](https://mariadb.org/), [PostgreSQL](https://www.postgresql.org/), [Amazon Aurora](https://aws.amazon.com/rds/aurora/)  |  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) , [Amazon Keyspaces](https://aws.amazon.com/keyspaces/), [Amazon Neptune](https://aws.amazon.com/neptune/), [Amazon QLDB](https://aws.amazon.com/qldb/), [Amazon Timestream](https://aws.amazon.com/timestream/) |
|  Self-managed  |  Hosting a relational database management system (DBMS) on an [Amazon EC2](https://aws.amazon.com/ec2/) instance |  Hosting a non-relational database solution on an EC2 instance |

## Amazon RDS
<a name="amazon-rds"></a>

 [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) gives you access to the capabilities of a familiar MySQL, PostgreSQL, Oracle, and Microsoft SQL Server database engine. The code, applications, and tools that you already use can be used with Amazon RDS. Amazon RDS automatically patches the database software and backs up your database, and it stores backups for a user-defined retention period. It also supports point-in-time recovery. You benefit from the flexibility of being able to scale the compute resources or storage capacity associated with your relational database instance by making a single API call.

Amazon RDS Multi-AZ deployments increase your database availability and protect your database against unplanned outages. Amazon RDS Read Replicas provide read-only replicas of your database, so you can scale out beyond the capacity of a single database deployment for read-heavy database workloads. As with all AWS services, no upfront investments are required, and you pay only for the resources you use.

## Hosting a relational database management system (RDBMS) on an Amazon EC2 instance
<a name="hosting-a-relational-database-management-system-rdbms-on-an-amazon-ec2-instance"></a>

In addition to the managed Amazon RDS offering, you can install your choice of RDBMS (such as MySQL, Oracle, SQL Server, or DB2) on an EC2 instance and manage it yourself. AWS customers hosting a database on Amazon EC2 successfully use a variety of primary/standby and replication models, including mirroring for read-only copies and log shipping for always-ready passive replicas.

When managing your own database software directly on Amazon EC2, you should also consider the availability of fault-tolerant and persistent storage. For this purpose, we recommend that databases running on Amazon EC2 use [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volumes, which are similar to network-attached storage.

For EC2 instances running a database, you should place all database data and logs on EBS volumes. These will remain available even if the database host fails. This configuration allows for a simple failover scenario, in which a new EC2 instance can be launched if a host fails, and the existing EBS volumes can be attached to the new instance. The database can then pick up where it left off.

EBS volumes automatically provide redundancy within the Availability Zone. If the performance of a single EBS volume is not sufficient for your databases needs, volumes can be striped to increase input/output operations per second (IOPS) performance for your database.

For demanding workloads, you can also use EBS Provisioned IOPS, where you specify the IOPS required. If you use Amazon RDS, the service manages its own storage so you can focus on managing your data.

## Non-relational databases
<a name="nosql-solutions"></a>

In addition to support for relational databases, AWS also offers a number of managed non-relational databases:
+ **[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)** is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Using the [AWS Management Console](https://aws.amazon.com/console/) or the [DynamoDB API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html), you can scale capacity up or down without downtime or performance degradation. Because DynamoDB handles the administrative burdens of operating and scaling distributed databases to AWS, you don’t have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.
+ **[Amazon DocumentDB](https://aws.amazon.com/documentdb/)** (with [MongoDB](https://aws.amazon.com/documentdb/what-is-mongodb/) compatibility) is a database service that is purpose-built for JSON data management at scale, fully managed and runs on AWS, and enterprise-ready with high durability.
+ **[Amazon Keyspaces](https://aws.amazon.com/keyspaces/)** (for [Apache Cassandra](https://cassandra.apache.org/_/index.html)) is a scalable, highly available, and managed Apache Cassandra-compatible database service. With Amazon Keyspaces, you can run your Cassandra workloads on AWS using the same Cassandra application code and developer tools that you use today.
+ **[Amazon Neptune](https://aws.amazon.com/neptune)** is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Amazon Neptune is a purpose-built, high-performance graph database engine optimized for storing billions of relationships and querying the graph with milliseconds latency.
+ **[Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/qldb/)** (QLDB) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. QLDB can be used to track each and every application data change and maintains a complete and verifiable history of changes over time.
+ **[Amazon Timestream](https://aws.amazon.com/timestream)** is a fast, scalable, and serverless time series database service for IoT and operational applications that makes it easy to store and analyze trillions of events per day up to 1,000 times faster and at as little as 1/10th the cost of relational databases.

Additionally, you can use Amazon EC2 to host other non-relational database technologies you may be working with.
