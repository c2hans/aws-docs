---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/modernize-sql-server.html
---

# Modernize SQL Server databases
<a name="modernize-sql-server"></a>

## Overview
<a name="modernize-sql-server-overview"></a>

If you're starting on a journey toward modernizing legacy databases for scalability, performance, and cost optimization, you may be facing challenges with commercial databases like SQL Server. Commercial databases are expensive, lock customers in, and offer punitive licensing terms. This section provides a high-level overview of the options for migrating and modernizing from SQL Server to open-source databases and information about choosing the best option for your workload.

You can refactor your SQL Server databases to open-source databases like Amazon Aurora PostgreSQL to save on Windows and SQL Server licensing costs. Cloud-native modern databases like Aurora merge the flexibility and low cost of open-source databases with the robust, enterprise-grade features of commercial databases. If you have variable workloads or multi-tenant workloads, you can also migrate to [Aurora serverless V2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html). This can reduce costs by to 90 percent, depending on workload characteristics. Additionally, AWS offers capabilities like [Babelfish for Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/babelfish/), tools like [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/), and services like [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) to simplify the migration and modernization of SQL Server databases on AWS.

## Database offerings
<a name="modernize-sql-server-database"></a>

Migrating from SQL Server on Windows to open-source database like Amazon Aurora, Amazon RDS for MySQL, or Amazon RDS for PostgreSQL can offer significant cost savings without compromise on performance or features. Consider the following:
+ Switching from SQL Server Enterprise edition on Amazon EC2 to Amazon RDS for PostgreSQL or Amazon RDS for MySQL can result in cost savings up to 80 percent.
+ Switching from SQL Server Enterprise edition on Amazon EC2 to Amazon Aurora PostgreSQL-Compatible Edition or Amazon Aurora MySQL-Compatible Edition can result in cost savings up to 70 percent.

For traditional database workloads, Amazon RDS for PostgreSQL and Amazon RDS for MySQL address requirements and provide a cost-effective solution for relational databases. Aurora adds numerous availability and performance features previously limited to expensive commercial vendors. The resiliency features in Aurora are an added cost. However, in comparison to similar features by other commercial vendors, the resiliency costs of Aurora are still cheaper than what commercial software charges for the same type of features. Aurora architecture is optimized to deliver significant improvements in performance as compared to standard MySQL and PostgreSQL deployments.

Because Aurora is compatible with open-source PostgreSQL and MySQL databases, there is the additional benefit of portability. Whether the best option is Amazon RDS for PostgreSQL, Amazon RDS for MySQL, or Aurora comes down to understanding business requirements and mapping necessary features to the best option.

## Amazon RDS and Aurora comparison
<a name="modernize-sql-server-rds-aurora"></a>

The following table summarizes the key differences between Amazon RDS and Amazon Aurora.

|
|
| Category | Amazon RDS for PostgreSQL or Amazon RDS for MySQL | Aurora PostgreSQL or Aurora MySQL |
| --- |--- |--- |
| Performance | Good performance | 3x or better performance |
| Failover | Typically 60-120 seconds\* | Typically 30 seconds |
| Scalability | Up to 5 read replica<br />Lag in seconds | Up to 15 read replicas<br />Lag in milliseconds |
| Storage | Up to 64 TB | Up to 128 TB |
| Storage HA | Multi-AZ with one or two standby, each with database copy | 6 copies of data across 3 Availability Zones by default |
| Backup | Daily snapshot and log backups | Continuous, asynchronous backup to Amazon S3 |
| Innovations with Aurora | NA | 100 GB<br />Fast database cloning |
|   | Auto-scaling read replicas |   |
|   | Query plan management |   |
|   | Aurora Serverless |   |
|   | Cross-Region replicas with Global Database |   |
|   | Cluster cache management\*\* |   |
|   | Parallel Query |   |
|   | Database activity streams |   |

\*Large transactions can increase failover times

\*\*Available in Aurora PostgreSQL

The following table shows the estimated monthly cost of the different database services covered in this section.

|
|
| Database service | Cost USD per month\* | AWS Pricing Calculator (requires AWS account) |
| --- |--- |--- |
| Amazon RDS for SQL Server Enterprise edition | $3,750 | [Estimate](https://calculator.aws/#/estimate?id=16f190d818045bb99fb59659cecca80f92db4bbc) |
| Amazon RDS for SQL Server Standard edition | $2,318 | [Estimate](https://calculator.aws/#/estimate?id=5a5e9832ae80fd9ad9e8010c9a17f57d5a0415ca) |
| SQL Server Enterprise edition on Amazon EC2 | $2,835 | [Estimate](https://calculator.aws/#/estimate?id=0976f53e9b1b55d5475dc394c8caae9d5581183b) |
| SQL Server Standard edition on Amazon EC2 | $1,345 | [Estimate](https://calculator.aws/#/estimate?id=3cada8ab6d72b68a2eb3bc92927990c9f7e264ca) |
| Amazon RDS for PostgreSQL | $742 | [Estimate](https://calculator.aws/#/estimate?id=bd825d40c79c0df8f0cf053d55ca39acc8a927fe) |
| Amazon RDS for MySQL | $712 | [Estimate](https://calculator.aws/#/estimate?id=c0f61d7b67652e58df5bf6cb244e9455ff4a8558) |
| Aurora PostgreSQL | $1,032 | [Estimate](https://calculator.aws/#/estimate?id=a557d7d740e5d87c9764bd369de81a5873dad053) |
| Aurora MySQL | $1,031 | [Estimate](https://calculator.aws/#/estimate?id=5924d827c98beadda65368c8e64eb249c001afd6) |

\* Storage price is included in instance pricing. Costs are based on the `us-east-1` Region. The throughput and IOPS are assumptions. The calculations are for r6i.2xlarge and r6g.2xlarge instances.

## Cost optimization recommendations
<a name="modernize-sql-server-opt-rec"></a>

Heterogenous database migrations typically require converting database schema from the source to the target database engine and migrating data from source to target database. The first step toward migration is to evaluate and convert SQL server schema and code objects to the target database engine.

You can use the [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) to evaluate and assess the database for compatibility with various target open-source database options like Amazon RDS for MySQL or Amazon RDS for PostgreSQL, Aurora MySQL, and PostgreSQL. You can also use the Babelfish Compass tool for assessing compatibility with Babelfish for Aurora PostgreSQL. This makes the AWS SCT and Compass powerful tools to understand the upfront work involved before deciding on a migration strategy. Should you decide to proceed, AWS SCT automates the changes required to the schema. The core philosophy behind Babelfish Compass is to allow the SQL database to move to Aurora with no, or very few, modifications. Compass will evaluate the existing SQL database to determine if this can be accomplished. This way, the outcome is known before any effort is spent on migrating data from SQL Server to Aurora.

AWS SCT automates conversion and migration of the database schema and code to the target database engine. You can use Babelfish for Aurora PostgreSQL to migrate your database and application from SQL Server to Aurora PostgreSQL with no or minimal schema changes. This can accelerate your migrations.

After the schema is migrated, you can use AWS DMS to migrate the data. AWS DMS can perform full data load and replicate changes to perform migration with minimal downtime.

This section explores the following tools in more detail:
+ AWS Schema Conversion Tool
+ Babelfish for Aurora PostgreSQL
+ Babelfish Compass
+ AWS Database Migration Service

### AWS Schema Conversion Tool
<a name="9999999999999999awssctlong-.35ae02d3-509b-568a-8399-7e6129a45681"></a>

You can use AWS SCT to evaluate your existing SQL Server databases and assess compatibility with Amazon RDS or Aurora. To simplify the migration process, you can also use AWS SCT to convert the schema from one database engine to another in a heterogeneous database migration. You can use AWS SCT to evaluate your application and convert embedded application code for applications written C\#, C\+\+, Java, and other languages. For more information, see [Converting application SQL using AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.html) in the AWS SCT documentation.

AWS SCT is a free AWS tool that supports many database [sources](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.html). To use AWS SCT, you point it to the source database and then run an assessment. Then, [AWS SCT](https://aws.amazon.com/blogs/database/convert-database-schemas-and-application-sql-using-the-aws-schema-conversion-tool-cli/) evaluates the schema and generates the assessment report. Assessment reports include an executive summary, complexity and migration effort, suitable target database engines, and recommendations for conversion. To download AWS SCT, see [Installing, verifying, and updating AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html) in the AWS SCT documentation.

The following table shows an example Executive Summary generated by AWS SCT to show the complexity involved with changing the database to different target platforms.

|
|
| Target platform | Auto or minimal changes | Complex actions |
| --- |--- |--- |
|  | **Storage objects** | **Code objects** | **Conversion actions** | **Storage objects** | **Code objects** |
| Amazon RDS for MySQL | 60 (98%) | 8 (35%) | 42 | 1 (2%) | 1 | 15 (65%) | 56 |
| Amazon Aurora MySQL-Compatible Edition | 60 (98%) | 8 (35%) | 42 | 1 (2%) | 1 | 15 (65%) | 56 |
| Amazon RDS for PostgreSQL | 60 (98%) | 12 (52%) | 54 | 1 (2%) | 1 | 11 (48%) | 26 |
| Amazon Aurora PostgreSQL-Compatible Edition | 60 (98%) | 12 (52%) | 54 | 1 (2%) | 1 | 11 (48%) | 26 |
| Amazon RDS for MariaDB | 60 (98%) | 7 (30%) | 42 | 1 (2%) | 1 | 16 (70%) | 58 |
| Amazon Redshift | 61 (100%) | 9 (39%) | 124 | 0 (0%) | 0 | 14 (61%) | 25 |
| AWS Glue | 0 (0%) | 17 (100%) | 0 | 0 (0%) | 0 | 0 (0%) | 0 |
| Babelfish | 59 (97%) | 10 (45%) | 20 | 2 (3%) | 2 | 12 (55%) | 30 |

An AWS SCT report also provides details on the schema elements that cannot be automatically converted. You can close the AWS SCT conversion gaps and optimize target schemas by referring to [AWS migration playbooks](https://aws.amazon.com/blogs/database/the-database-migration-playbook-has-landed/). There are many database migration playbooks to assist with heterogeneous migrations.

### Babelfish for Aurora PostgreSQL
<a name="babelfish-for-9999999999999999aurpostgres-.14e1bb22-5594-5a2d-b41d-7dd1f05c90d1"></a>

Babelfish for Aurora PostgreSQL extends Aurora PostgreSQL with the ability to accept database connections from SQL Server clients. Babelfish enables applications that were originally built for SQL Server to work directly with Aurora PostgreSQL, with few code changes and without changing database drivers. Babelfish turns Aurora PostgreSQL bilingual so that Aurora PostgreSQL can work with both the T-SQL and PL/pgSQL languages. Babelfish minimizes the efforts to migrate from SQL Server to Aurora PostgreSQL. This accelerates migrations, minimizes risk, and reduces migration costs significantly. You can continue to use T-SQL post migrations, but there is also an [option of using PostgreSQL native tools](https://aws.amazon.com/blogs/database/category/database/amazon-aurora/babelfish-for-aurora-postgresql/) for development.

The following diagram illustrates how an application using T-SQL connects to the default port 1433 in SQL Server and uses the Babelfish translator to communicate with the Aurora PostgreSQL database, while an application using PL/pgSQL can directly and simultaneously connect to the Aurora PostgreSQL database using the default port 5432 in Aurora PostgreSQL.

![Babelfish for Aurora PostgreSQL](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/25476077-5267-4265-bce6-adbe528d9e5b.png)

Babelfish doesn't support certain SQL Server T-SQL features. For this reason, Amazon provides assessment tools to do a line-by-line analysis of your SQL statements and determine if any of them are unsupported by Babelfish.

There are two options for Babelfish assessments. AWS SCT can assess the compatibility of your SQL Server database with Babelfish. Another option is the Babelfish Compass tool, which is a recommended solution because the Compass tool is updated in line with new releases of Babelfish for Aurora PostgreSQL.

### Babelfish Compass
<a name="babelfish-compass.efa51bcd-c058-5983-937d-6909a82c80cc"></a>

[Babelfish Compass](https://github.com/babelfish-for-postgresql/babelfish_compass) is a free downloadable tool that aligns with the latest release of Babelfish for Aurora PostgreSQL. In contrast, AWS SCT will support newer Babelfish versions after some time. [Babelfish Compass](https://github.com/babelfish-for-postgresql/babelfish_compass/blob/main/README.md) is run against the SQL Server database schema. You can also extract the source SQL Server database schema by using tools like SQL Server Management Studio (SSMS). Then, you can run the schema through Babelfish Compass. This generates the report detailing the compatibility of SQL Server schema with Babelfish and if any changes are needed before migrating. The Babelfish Compass tool can also automate many of these changes and ultimately accelerate your migrations.

After the assessment and changes are completed, you can migrate the schema to Aurora PostgreSQL by using SQL Server native tools like SSMS or sqlcmd. For instructions, see the [Migrate from SQL Server to Amazon Aurora using Babelfish](https://aws.amazon.com/blogs/database/migrate-from-sql-server-to-amazon-aurora-using-babelfish/) post on the AWS Database Blog.

### AWS Database Migration Service
<a name="9999999999999999dmslong-.1abd1dc1-1a82-50da-a458-00df6cd6e253"></a>

After the schema is migrated, you can use AWS Database Migration Service (AWS DMS) to migrate the data to AWS with minimal downtime. AWS DMS not only does a full data load, but also replicates changes from source to destination while the source system is up and running. After both source and target databases are in sync, the cutover activity can take place where the application is pointed to the target database completing the migration. AWS DMS currently only performs full data load with Babelfish for an Aurora PostgreSQL target and doesn't replicate changes. For more information, see [Using Babelfish as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Babelfish.html) in the AWS DMS documentation.

AWS DMS can do both homogeneous (across the same database engine) and heterogeneous (across different database engines) migrations. AWS DMS supports many source and destination database engines. For more information, see the [Migrating your SQL Server database to Amazon RDS for SQL Server using AWS DMS](https://aws.amazon.com/blogs/database/migrating-your-sql-server-database-to-amazon-rds-for-sql-server-using-aws-dms/) post in the AWS Database Blog.

## Additional resources
<a name="modernize-sql-server-resources"></a>
+ [Goodbye Microsoft SQL Server, Hello Babelfish](https://aws.amazon.com/blogs/aws/goodbye-microsoft-sql-server-hello-babelfish/) (AWS News Blog)
+ [Convert database schemas and application SQL using the AWS Schema Conversion Tool CLI](https://aws.amazon.com/blogs/database/convert-database-schemas-and-application-sql-using-the-aws-schema-conversion-tool-cli/) (AWS Database Blog)
+ [Migrate SQL Server to Amazon Aurora PostgreSQL using best practices and lessons learned from the field](https://aws.amazon.com/blogs/database/migrate-sql-server-to-amazon-aurora-postgresql-using-best-practices-and-lessons-learned-from-the-field/) (AWS Database Blog)
+ [Validate database objects post-migration from Microsoft SQL Server to Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/validate-database-objects-post-migration-from-microsoft-sql-server-to-amazon-rds-for-postgresql-and-amazon-aurora-postgresql/) (AWS Database Blog)
