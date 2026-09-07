---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/heterogeneous-migration.html
---

# Heterogeneous database migration
<a name="heterogeneous-migration"></a>

Because of the innovations and improvements in open-source databases and cloud computing platforms like AWS, many organizations are moving from proprietary (online transaction processing or OLTP) database engines such as Oracle to open-source engines. Oracle databases are mission-critical systems for any organization, but being locked into a particular vendor is a risky and costly situation. Low operating cost and no licensing fees are compelling reasons to consider switching the underlying database technology to open-source or AWS Cloud-native databases.

Other reasons for migrating off Oracle are vendor lock-in periods, licensing audits, expensive licensing, and cost. Oracle's list pricing is based on a per-core model with additional costs for features such as partitioning and high availability. For this reason, many organizations choose to migrate their Oracle databases to either open-source databases (such as PostgreSQL, MySQL, or MariaDB) or AWS Cloud-native databases (such as Amazon Aurora or Amazon DynamoDB) when they migrate to AWS.

You can also migrate your Oracle data warehouse database to Amazon Redshift, which is a fast, fully managed cloud data warehouse. Amazon Redshift is integrated with your data lake, offers up to three times faster performance than any other data warehouse, and costs up to 75 percent less than any other cloud data warehouse. For more information, see [Migrate from Oracle to Amazon Redshift](https://aws.amazon.com/getting-started/projects/migrate-oracle-to-amazon-redshift/) on the AWS website.

To migrate to an open-source or AWS-native database, choose the right database depending on the type of data you have, the access model, scalability, application practicalities, and complexity. For example, PostgreSQL databases have become very popular in recent years for their powerful functionality and high degree of compatibility with commercial databases, and they're the most common migration target for users who are refactoring their Oracle databases. But migrating from Oracle to PostgreSQL and to other open-source databases has often been difficult and time-consuming, and requires careful assessment, planning, and testing.

This process becomes easier with services like AWS DMS and AWS Schema Conversion Tool (AWS SCT), which help you migrate your commercial database to an open-source database on AWS with minimal downtime.

In heterogeneous database migrations, the source and target databases engines are different, as in Oracle to Amazon Aurora, or Oracle to PostgreSQL, MySQL, or MariaDB migrations. The schema structure, data types, and database code in the source and target databases can be quite different, so the schema and code must be transformed before the data migration starts. For this reason, heterogeneous migration is a two-step process:
+ Step 1. Convert the source schema and code to match that of the target database. You can use AWS SCT for this conversion.
+ Step 2. Migrate data from the source database to the target database.  You can use AWS DMS for this process.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/12887387-43a9-411a-96c5-34143e5075c4.png)

AWS DMS handles all required data type conversions automatically during migration. The source database can be located in your own premises outside AWS, it can be a database that's running on an EC2 instance, or it can be an Amazon RDS database (see [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) in the AWS DMS documentation). The target can be a database in Amazon EC2, Amazon RDS, or Amazon Aurora.

## Tools for heterogeneous database migrations
<a name="heterogeneous-migration-tools"></a>

The following chart provides a list of tools that you can use to migrate from Oracle Database to another database engine.

|
|
| Migration tool | Target database support | Used for |
| --- |--- |--- |
| AWS SCT | Amazon RDS for MySQL<br />Amazon RDS for PostgreSQL<br />Amazon Aurora MySQL<br />Amazon Aurora PostgreSQL | Schema conversion |
| AWS DMS | Amazon RDS for MySQL<br />Amazon RDS for PostgreSQL<br />Amazon Aurora MySQL<br />Amazon Aurora PostgreSQL | Data migration |

The following subsections provide more information about each tool.

### AWS SCT
<a name="aws-sct.e37c1e8d-e371-52a9-bb5f-3902b79aadc3"></a>

[AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) converts your existing commercial database schemas to an open-source engine or to an AWS Cloud-native database. AWS SCT makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format that's compatible with the target database. Any objects that can't be automatically converted are clearly marked for manual conversion. AWS SCT can also scan your application source code for embedded SQL statements and convert them as part of a database schema conversion project.

### AWS DMS
<a name="aws-dms.12fe06f9-84bd-5b32-bc3c-a8145f4323d4"></a>

[AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/) migrates your data rapidly and securely to AWS. During migration, the source database remains fully operational, minimizing application downtime. AWS DMS supports homogeneous migrations such as Oracle to Oracle as well as heterogeneous migrations between different database platforms, such as Oracle to an open-source database or to an AWS cloud-native database. AWS DMS manages the complexities of the migration process, including automatically replicating data changes that occur in the source database to the target database. After the database migration is complete, the target database remains synchronized with the source database for as long as you choose, and you can switch over to the target database at a convenient time.
