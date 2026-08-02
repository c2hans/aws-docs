---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-purpose.html
---

# Consider purpose-built databases
<a name="net-purpose"></a>

## Overview
<a name="net-purpose-overview"></a>

One of the costliest aspects of running Microsoft-based workloads comes from the licensing of commercial databases, such as SQL Server. Businesses often standardize on SQL Server as the database platform of choice and it becomes ingrained in the development culture of the organization. Developers generally choose a relational SQL Server-based model regardless of the use case. Reasons include:
+ The business already has SQL Server instances and/or licenses available.
+ Teams have habituated to the SQL programming model through the use of shared libraries, ORMs, and business logic.
+ Management is not aware of alternatives.
+ Developers are not aware of alternatives.

Purpose-built databases can accommodate the data access patterns of your use case. These databases are increasingly adopted by businesses as they adopt more modern architectures (such as microservices) and as the scope of individual applications narrow.

A database being purpose-built does not preclude a relational model, or require a NoSQL (non-relational) model. In fact, a relational database is considered purpose-built when selected in response to a workload's specific needs. The use of purpose-built databases can help teams to reduce the database costs associated with their .NET applications, while also gaining standard cloud benefits, such as scalability, resilience, and the reduction of undifferentiated heavy lifting.

The following table shows the purpose-built databases offered by AWS.

|
|
| Database | Type | Characteristics |
| --- |--- |--- |
| [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) or [Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html) | Relational | Use cases where data has a fixed structure<br />Relational databases naturally maintain data consistency through ACID transactions |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) | Key-value pair | NoSQL database that stores data using a hash table data structure<br />High performance storage and retrieval of unstructured data<br />Use cases include user profiles, session state, and shopping cart data |
| [Amazon ElastiCache](https://aws.amazon.com/elasticache/) | In-memory | High performance NoSQL database that stores unstructured data in memory with sub-millisecond access time<br />Used for frequently accessed, ephemeral data such as user sessions, and as a caching layer in front of other, slower, data stores<br />Includes support for both ElastiCache (Redis OSS) and ElastiCache (Memcached) |
| [Amazon MemoryDB](https://aws.amazon.com/memorydb/) | Durable in-memory | Redis compatible purpose-built database with durable storage |
| [Amazon Timestream](https://aws.amazon.com/timestream/) | Time series | Database designed for high throughput data ingestion in temporal order<br />Use cases include Internet of Things (IoT) applications and storing metrics or telemetry data |
| [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | Document | NoSQL database that stores data without a prescribed structure or enforced relationships to other data<br />Often used for read-intensive workloads such as product catalogs |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Graph | NoSQL database that holds both data and a representation of the connections among data items<br />Use cases include fraud detection, recommendation engines, and social applications |
| [Amazon Keyspaces](https://aws.amazon.com/keyspaces/) | Wide-column | High performance distributed database based on Apache Cassandra<br />Use cases include IoT applications, event processing, and game applications |

A significant driver of purpose-built database adoption can be attributed to the elimination of commercial licensing. However, the auto-scaling capability of databases such as [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) (including [on-demand mode](https://aws.amazon.com/blogs/aws/amazon-dynamodb-on-demand-no-capacity-planning-and-pay-per-request-pricing/)), [Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html), [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-autoscaling.html), and [Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) enable you to provision capacity for the average case, rather than for peak usage. Purpose-built databases, such as Timestream, are serverless and automatically scale to meet demand without any pre-provisioning.

AWS offers [Babelfish for Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/babelfish/) if you want to use a purpose-built, open-source compatible relational database, but are unable or unwilling to make significant code changes to your application. In some cases, Babelfish allows you to use an existing SQL Server access code, with almost no changes.

When choosing a purpose-built relational database for applications, it's important to retain the same (or functionally equivalent) features that you require for your applications. This recommendation addresses purpose-built databases as a primary data store for applications. Specific applications (such as caching) are addressed in other recommendations.

## Cost impact
<a name="net-purpose-cost"></a>

Adopting purpose-built databases for .NET workloads, while unlikely to affect compute consumption/cost directly, can directly influence the cost of the database services consumed by the .NET applications. In fact, cost savings may be a secondary goal, when compared with the added benefits of agility, scalability, resilience, and data durability.

It's outside the scope of this guide to explain the full process of choosing a purpose-built database for applications and rearchitecting a data strategy to use them effectively. For more information, see [Purpose-built databases](https://aws.amazon.com/tutorials/purpose-built-databases/) in the AWS Tutorials Directory.

The following tables show several examples of how the replacement of SQL Server with a purpose-built database can alter application costs. Note that these are simply rough estimates. Benchmarks and optimization of actual workloads is required to calculate the exact production cost.

These are some commonly used purpose-built database estimates that include on-demand compute and 100 GB SSD, single instance databases in `us-east-1`. License costs include SQL Server license plus software assurance.

The following table shows estimated costs for commercial database examples.

|
|
| Database engine | Licensing model | Instance type/specs | AWS compute \+ storage cost | License cost | Total monthly cost |
| --- |--- |--- |--- |--- |--- |
| SQL Server Standard edition on Amazon EC2 | License included | r6i.2xlarge (8 CPU/64 GB RAM) | $1,345.36 | $0.00 | $1,345.36 |
| SQL Server Enterprise edition on Amazon EC2 | License included | r6i.2xlarge (8 CPU/64 GB RAM) | $2,834.56 | $0.00 | $2,834.56 |
| SQL Server Standard edition on Amazon EC2 | BYOL | r6i.2xlarge (8 CPU/64 GB RAM) | $644.56 | $456.00 | $1,100.56 |
| SQL Server Enterprise edition on Amazon EC2 | BYOL | r6i.2xlarge (8 CPU/64 GB RAM) | $644.56 | $1,750.00 | $2,394.56 |
| SQL Server Standard edition on Amazon RDS |  | db.r6i.2xlarge (8 CPU/64 GB RAM) | $2,318.30 | $0.00 | $2,318.30 |
| SQL Server Enterprise edition on Amazon RDS |  | db.r6i.2xlarge (8 CPU/64 GB RAM) | $3,750.56 | $0.00 | $3,750.56 |

The following table shows estimated costs for purpose-built examples.

|
|
| Database engine | Instance type/specs | AWS compute \+ storage cost | License cost | Total monthly cost |
| --- |--- |--- |--- |--- |
| Amazon Aurora PostgreSQL | r6g.2xlarge (8 CPU/64 GB RAM) | $855.87 | $0.00 | $855.87 |
| DynamoDB | Provisioned base 100 WCU/400 RCU | $72.00 |  | $72.00 |
| Amazon DocumentDB | db.r6i.2xlarge (8 CPU/64 GB RAM) | $778.60 |  | $778.60 |

|
|
| Important: The table is based on estimated licensing costs for SQL Server with Software Assurance, during the first three years of purchase. For SQL Server Standard edition: $4,100, 2 core pack, 3 years. For SQL Server Enterprise edition: $15,700, 2 core pack, 3 years. |
| --- |

We recommend that you consider the cost implications before you adopt purpose-built databases. For example, the cost to update applications to use a purpose-built database is related to the complexity of the application and the source database. Be sure to factor in the total cost of ownership when planning this architecture switch. This includes refactoring your applications, upskilling staff on new technologies, and carefully planning the performance and consumption anticipated for each workload. From there, you can make the determination if the investment is worth the cost savings. In most cases, maintaining an end-of-support product is a security and compliance risk, and the cost of remediating it is worth the effort and initial investment.

## Cost optimization recommendations
<a name="net-purpose-rec"></a>

For .NET applications that are accessing SQL Server, there are replacement libraries for purpose-built relational databases. You can implement these libraries in your application to replace similar SQL Server application functionality.

The following table highlights some libraries that can be used in many common scenarios.

|
|
| Library | Database | Replacement for | Framework compatibility |
| --- |--- |--- |--- |
| [Npgsql Entity Framework Core Provider](https://www.npgsql.org/efcore/index.html) | Amazon Aurora PostgreSQL | Entity Framework Core SQL Server Provider | Modern .NET |
| [Npgsql Entity Framework 6 Provider](https://www.npgsql.org/ef6/index.html) | Amazon Aurora PostgreSQL | Entity Framework 6.0 SQL Server Provider | .NET Framework |
| [Npgsql](https://www.npgsql.org/doc/index.html) (ADO.NET compatible PostgreSQL library) | Amazon Aurora PostgreSQL | ADO.NET | .NET Framework/Modern .NET |
| [MySQL Entity Framework Core Provider](https://dev.mysql.com/doc/connector-net/en/connector-net-entityframework-core.html) | Amazon Aurora MySQL | Entity Framework Core SQL Server Provider | Modern .NET |
| [Pomelo.EntityFrameworkCore.MySql](https://www.nuget.org/packages/Pomelo.EntityFrameworkCore.MySql) | Amazon Aurora MySQL | Entity Framework Core SQL Server Provider | Modern .NET |

[Connecting to Amazon Aurora PostgreSQL by using Babelfish](https://babelfishpg.org/docs/client/csharp/) doesn't require any special coding to connect. However, all code should be thoroughly tested prior to use.

Other purpose-built databases have libraries for accessing .NET compatible libraries that enable you to access purpose built databases. Examples include:
+ [Using Amazon DynamoDB NoSQL databases](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html) (AWS SDK for .NET documentation)
+ [MongoDB C\# Driver](https://www.mongodb.com/docs/drivers/csharp/current/) (MongoDB documentation)
+ [.NET](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started.dot-net.html) (Timestream documentation)
+ [Using a Cassandra .NET Core client driver to access Amazon Keyspaces programmatically](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_dotnetcore_driver.html) (Amazon Keyspaces documentation)
+ [Using .NET to connect to a Neptune DB instance](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-dotnet.html) (Neptune documentation)

If you migrate to purpose built-databases, you can use these tools from AWS to help with the migration process:
+ [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/) can help you transform SQL Server schemas to Amazon Aurora and Amazon DynamoDB.
+ [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/schema-conversion-tool/) can help you migrate data, either one time or on an ongoing basis, from SQL Server to Aurora or DynamoDB.
+ [Babelfish Compass](https://github.com/babelfish-for-postgresql/babelfish_compass) can help you check the compatibility of your SQL Server database for use with Babelfish for Aurora PostgreSQL.

## Additional resources
<a name="net-purpose-resources"></a>
+ [Guidance for migrating SQL Server to Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/migrate-sql-server-to-amazon-aurora-postgresql-using-best-practices-and-lessons-learned-from-the-field/) (AWS Database Blog)
+ [Babelfish APP Modernization Immersion Day](https://catalog.workshops.aws/babelfish-app-modernization/en-US) (AWS Workshop Studio)
+ [.NET Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/02696107-09ac-4313-a6cb-3798048b07d7/en-US/3-choosing-a-cloud-native-database-for-my-net-application) (AWS Workshop Studio)
+ [Getting started with Amazon Timestream with .NET](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/sample_apps/dotnet) (GitHub)
+ [Purpose-built databases for modern .NET applications on AWS](https://d1.awsstatic.com/events/Summits/reinvent2022/XNT304_Purpose-built-databases-for-modern-NET-applications-on-AWS.pdf) (AWS presentation)
