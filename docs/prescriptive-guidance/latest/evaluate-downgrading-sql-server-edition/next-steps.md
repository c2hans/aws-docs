---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/next-steps.html
---

# Next steps
<a name="next-steps"></a>

After you determine that you can safely downgrade an instance from SQL Server Enterprise edition, the next step is to migrate to SQL Server Standard edition on Amazon RDS. To migrate the database, use one or a combination of the following tools:
+ **Native backup and restore** – You can use native backup and restore to move data in and out of SQL Server database instances. Amazon RDS supports [native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) for Microsoft SQL Server databases using full backup (.bak) files. When you use Amazon RDS, you access files stored in Amazon Simple Storage Service (Amazon S3) rather than using the local file system on the database server.
+ **AWS Database Migration Service (AWS DMS)** – AWS DMS helps you migrate relational databases, data warehouses, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises databases. The Change Data Capture option of AWS DMS offers continuous replication, so you can reduce the total downtime during migration. For information about SQL Server versions and editions that AWS DMS supports, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html).

Depending on your availability requirements during the downgrade, you can adopt any of the following options to safely downgrade your Enterprise edition instance to a Standard edition on Amazon RDS for SQL Server.

## Downgrading with downtime
<a name="downgrading-with-downtime.571bc34f-73be-5b72-aef6-bd05ab655605"></a>
+ [Use native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) to create a consistent copy from the Enterprise edition database and restoring to the Standard edition database.
+ [Use AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html) to perform a full load of data from the Enterprise edition to the Standard edition database.

## Downgrading with reduced downtime
<a name="downgrading-with-reduced-downtime.a88e6be1-d547-5b23-be89-0522033fbcf4"></a>
+ [Use AWS DMS](https://aws.amazon.com/blogs/database/migrating-your-sql-server-database-to-amazon-rds-for-sql-server-using-aws-dms/) for full load and data synchronization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
