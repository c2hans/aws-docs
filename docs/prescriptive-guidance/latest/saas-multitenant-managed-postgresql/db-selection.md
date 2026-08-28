---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/db-selection.html
---

# Selecting a database for a SaaS application
<a name="db-selection"></a>

For many multi-tenant SaaS applications, selecting an operational database can be distilled into a choice between relational and non-relational databases, or a combination of the two. To make your decision, consider these high-level application data requirements and characteristics:
+ Data model of the application
+ Access patterns for the data
+ Database latency requirements
+ Data integrity and transactional integrity requirements (atomicity, consistency, isolation, and durability, or ACID)
+ Cross-Region availability and recovery requirements

The following table lists application data requirements and characteristics, and discusses them in the context of AWS database offerings: Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL (relational), and Amazon DynamoDB  (non-relational). You can reference this matrix when you're trying to decide between relational and non-relational operational database offerings.

The following table shows SaaS application data requirements and characteristics.

|
|
|  Databases | Data model | Access patterns | Latency requirements | Data and transactional integrity | Cross-Region availability and recovery |
| --- |--- |--- |--- |--- |--- |
| **Relational**<br />**(Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL) ** | Relational or highly normalized. | Doesn't have to be thoroughly planned beforehand. | Preferably higher latency tolerance; can achieve lower latencies by default with Aurora and by implementing read replicas, caching, and similar features. | High data and transactional integrity maintained by default. | In Amazon RDS, you can create a read replica for cross-Region scaling and failover. [Aurora mostly automates this process](https://aws.amazon.com/blogs/database/aurora-postgresql-disaster-recovery-solutions-using-amazon-aurora-global-database/). For active-active configurations across multiple AWS Regions, you can use [write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html) in conjunction with [Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html). |
| **Non-relational**<br />**(Amazon DynamoDB)** | Usually denormalized. These databases take advantage of patterns for modeling [many-to-many](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-adjacency-graphs.html) relationships, [large items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html), and [time series data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html). | All access patterns (queries) for data must be thoroughly understood before a data model is produced. | Very low latency with options such as Amazon DynamoDB Accelerator (DAX) able to improve performance even further. | Optional transactional integrity at the cost of performance. Data integrity concerns are shifted to the application. | Easy cross-Region recovery and active-active configuration with global tables. (ACID compliance is achievable only in a single AWS Region.) |

Some multi-tenant SaaS applications might have unique data models or special circumstances that are better served by databases not included in the previous table. For example, time series datasets, highly connected datasets, or maintaining a centralized transaction ledger might necessitate using a different type of database. Analyzing all possibilities is beyond the scope of this guide. For a comprehensive list of AWS database offerings and how they can fulfill different use cases at a high level, see the [Database](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html) section of the *Overview of Amazon Web Services* whitepaper.

The remainder of this guide focuses on AWS relational database services that support PostgreSQL: Amazon RDS and Amazon Aurora PostgreSQL-Compatible. DynamoDB requires a different approach to optimize for SaaS applications, which is beyond the scope of this guide. For more information about DynamoDB, see the AWS blog post [Partitioning Pooled Multi-Tenant SaaS Data with Amazon DynamoDB](https://aws.amazon.com/blogs/apn/partitioning-pooled-multi-tenant-saas-data-with-amazon-dynamodb/).

## Choosing between Amazon RDS and Aurora
<a name="relational"></a>

In most cases, we recommend using Aurora PostgreSQL-Compatible over Amazon RDS for PostgreSQL. The following table shows the factors that you should consider when deciding between these two options.

|
|
| DBMS component | Amazon RDS for PostgreSQL | Aurora PostgreSQL-Compatible |
| --- |--- |--- |
| **Scalability** | Replication lag of minutes,  maximum of 5 read replicas | Replication lag under a minute (typically less than 1 second with global databases), maximum of 15 read replicas |
| **Crash recovery** | Checkpoints 5 minutes apart (by default), can slow database performance | Asynchronous recovery with parallel threads for rapid recovery |
| **Failover** | 60-120 seconds in addition to crash recovery time | Usually about 30 seconds (including crash recovery) |
| **Storage** | Maximum IOPS of 256,000 | IOPS constrained only by Aurora instance size and capacity |
| **High availability and disaster recovery** | Two Availability Zones with a standby instance, cross-Region failover to read replica or copied backups | Three Availability Zones by default, cross-Region failover with Aurora global databases,[ write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html) across AWS Regions for active-active configuration |
| **Backup** | During backup window, can impact performance | Automatic incremental backups, no performance impact |
| **Database instance classes** | See [list of Amazon RDS instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) | See [list of Aurora instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) |

In all the categories described in the previous table, Aurora PostgreSQL-Compatible is usually the better option. However, Amazon RDS for PostgreSQL might still make sense for small to medium workloads, because it has a greater selection of instance classes that might provide a more cost-effective option at the expense of Aurora's more robust feature set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
