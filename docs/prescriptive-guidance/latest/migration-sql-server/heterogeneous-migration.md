---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/heterogeneous-migration.html
---

# Heterogeneous database migration for SQL Server
<a name="heterogeneous-migration"></a>

Because of the innovations and improvements in open-source databases and cloud computing platforms like AWS, many organizations are moving from proprietary (online transaction processing or OLTP) database engines such as SQL Server to open-source engines. SQL Server databases are mission-critical systems for any organization, but being locked into a particular vendor is a risky and costly situation. Low operating cost and no licensing fees are compelling reasons to consider switching the underlying database technology to open-source or AWS cloud-native databases.

Other reasons for migrating off SQL Server are vendor lock-in periods, licensing audits, expensive licensing, and cost. For this reason, many organizations choose to migrate their SQL Server databases to either open-source databases (such as PostgreSQL, MySQL, or MariaDB) or AWS cloud-native databases (such as Amazon Aurora or Amazon DynamoDB) when they migrate to AWS.

You can also migrate your SQL Server data warehouse database to Amazon Redshift, which is a fast, fully managed cloud data warehouse. Amazon Redshift is integrated with your data lake, offers up to three times faster performance than any other data warehouse, and costs up to 75 percent less than any other cloud data warehouse. For more information, see the pattern [Migrate an on-premises Microsoft SQL Server database to Amazon Redshift using AWS DMS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms.html) on the AWS Prescriptive Guidance website.

To migrate to an open-source or AWS native database, choose the right database depending on the type of data you have, the access model, scalability, application practicalities, and complexity. Migrating from SQL Server to PostgreSQL and to other open-source databases has often been difficult and time-consuming, and requires careful assessment, planning, and testing.

This process becomes easier with services like AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (AWS SCT), which help you migrate your commercial database to an open-source database on AWS with minimal downtime.

In heterogeneous database migrations, the source and target databases engines are different, as in SQL Server to Amazon Aurora, or SQL Server to MariaDB migrations. The schema structure, data types, and database code in the source and target databases can be quite different, so the schema and code must be transformed before the data migration starts. For this reason, heterogeneous migration is a two-step process:
+ Step 1. Convert the source schema and code to match that of the target database. You can use AWS SCT for this conversion.
+ Step 2. Migrate data from the source database to the target database.  You can use AWS DMS for this process.

![Heterogeneous database migration with &AWSSCT; and &DMS;](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/b4b0328f-e283-48c1-acac-f1673fada436.png)

AWS DMS handles the major data type conversions automatically during migration. The source database can be located in your own premises outside AWS, it can be a database that's running on an Amazon EC2 instance, or it can be an Amazon RDS database (see [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) in the AWS DMS documentation). The target can be a database in Amazon EC2, Amazon RDS, or Amazon Aurora. For information about using MySQL as a target database, see [Migrating a SQL Server Database to a MySQL-Compatible Database Engine](https://aws.amazon.com/blogs/database/migrating-a-sql-server-database-to-a-mysql-compatible-database-engine/) on the AWS Database blog.
