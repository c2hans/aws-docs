---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/heterogeneous-migration-tools.html
---

# Tools for heterogeneous database migrations
<a name="heterogeneous-migration-tools"></a>

The following chart provides a list of tools that you can use to migrate from SQL Server to another database engine.

|
|
| **Migration tool** | **Target database support** | **Used for** |
| --- |--- |--- |
| [AWS SCT](#aws-sct) | Amazon RDS for MySQL<br />Amazon RDS for PostgreSQL<br />Amazon Aurora MySQL<br />Amazon Aurora PostgreSQL | Schema conversion |
| [AWS DMS](#aws-dms) | Amazon RDS for MySQL<br />Amazon RDS for PostgreSQL<br />Amazon Aurora MySQL<br />Amazon Aurora PostgreSQL | Data migration |
| [Babelfish](#babelfish) | Amazon Aurora PostgreSQL | Data access and migration |

The following subsections provide more information about each tool.

## AWS SCT
<a name="aws-sct"></a>

[AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) converts your existing commercial database schemas to an open-source engine or to an AWS cloud-native database. AWS SCT makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format that's compatible with the target database.

When you convert your database schema from one engine to another, you also need to update the SQL code in your applications to interact with the new database engine instead of the old one. AWS SCT also converts the SQL code in C\+\+, C\#, Java or other application code. Any objects that can't be automatically converted are clearly marked for manual conversion. AWS SCT can also scan your application source code for embedded SQL statements and convert them as part of a database schema conversion project. For more information, see [Using Microsoft SQL Server as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.html) in the AWS documentation.

## AWS DMS
<a name="aws-dms"></a>

[AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/) migrates your data rapidly and securely to AWS. During migration, the source database remains fully operational, minimizing application downtime. AWS DMS supports homogeneous migrations such as migrating data from one SQL Server database to another. It also supports heterogeneous migrations between different database platforms, such as migrating your SQL Server database to an open-source database or to an AWS cloud-native database. AWS DMS manages the complexities of the migration process, including automatically replicating data changes that occur in the source database to the target database. After the database migration is complete, the target database remains synchronized with the source database for as long as you choose, and you can switch over to the target database at a convenient time. For more information, see [Using a Microsoft SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html) in the AWS documentation.

## Babelfish
<a name="babelfish"></a>

Babelfish is a built-in capability of Amazon Aurora. Babelfish for Aurora PostgreSQL enables your Aurora PostgreSQL-Compatible Edition databases to understand commands from applications that were written for Microsoft SQL Server. Modifying SQL Server applications that have SQL Server database code written in Transact-SQL (T-SQL), SQL Server's proprietary SQL dialect, takes effort and is time-consuming. [Babelfish for Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/babelfish/) makes this process simpler and easier. Using Babelfish, you do not have to make changes to your application code. Instead, you can use Babelfish for Aurora PostgreSQL to migrate a SQL Server database to an Aurora PostgreSQL DB cluster.

With Babelfish, Aurora PostgreSQL-Compatible understands T-SQL and supports the same communications protocol, so you don't have to switch database drivers or rewrite your application queries. Your applications that were originally written for SQL Server can now work with Aurora with fewer code changes. This reduces the effort required to modify and move applications running on SQL Server or newer to Aurora, leading to faster, lower-risk, and more cost-effective migrations.

If you're migrating from legacy SQL Server databases, you can use Babelfish to run SQL Server code side by side with new functionality you built by using native PostgreSQL APIs. Babelfish enables Aurora PostgreSQL-Compatible to work with commonly used SQL Server tools, commands, and drivers.

Babelfish also provides access to data by using the native PostgreSQL connection. By default, both SQL dialects supported by Babelfish are available through their native wire protocols at the following ports:
+ For SQL Server dialect (T-SQL), connect to port 1433.
+ For PostgreSQL dialect (PL/pgSQL), connect to port 5432.

 Babelfish enables your legacy SQL Server applications to communicate with Aurora without extensive code rewrites, by providing connections from the SQL Server or PostgreSQL port. The following diagram illustrates this architecture.

![Communications between Babelfish and &AUR;.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/7779740b-c1a5-4482-a9f8-81ca8b995d1b.png)

You can enable Babelfish on your Aurora cluster from the Amazon RDS management console. For instructions, see [Creating a Babelfish for Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-create.html) in the Amazon RDS documentation.

For more information about migrating, see [Migrating a SQL Server database to Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html) in the Aurora documentation.

For additional information, see the following resources:
+ [Get started with Babelfish for Aurora PostgreSQL](https://aws.amazon.com/blogs/database/get-started-with-babelfish-for-aurora-postgresql/) (AWS Database blog)
+ [Migrate from SQL Server to Amazon Aurora using Babelfish](https://aws.amazon.com/blogs/database/migrate-from-sql-server-to-amazon-aurora-using-babelfish/) (AWS Database blog)
+ [Migrate from SQL Server to Aurora PostgreSQL using SSIS and Babelfish](https://aws.amazon.com/blogs/database/migrate-from-sql-server-to-aurora-postgresql-using-ssis-and-babelfish/) (AWS Database blog)
+ [Modify SSIS packages from SQL Server to Babelfish for Aurora PostgreSQL](https://aws.amazon.com/blogs/database/modify-ssis-packages-from-sql-server-to-babelfish-for-aurora-postgresql/) (AWS Database blog)
+ [Run SQL Server Reporting Services reports against Babelfish for Aurora PostgreSQL](https://aws.amazon.com/blogs/database/run-sql-server-reporting-services-reports-against-babelfish-for-aurora-postgresql/) (AWS Database blog)
+ [Prepare for Babelfish migration with the AWS SCT assessment report](https://aws.amazon.com/blogs/database/prepare-for-babelfish-migration-with-the-aws-sct-assessment-report/) (AWS Database blog)
