---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/snowball-edge.html
---

# AWS Snowball Edge
<a name="snowball-edge"></a>

You can use AWS Snowball Edge to migrate very large databases (up to 210 TB in size). Snowball has a 10 Gb Ethernet port that you plug into your on-premises server and place all database backups or data on the SnowballSnowball device. After the data is copied to Snowball, you send the appliance to AWS for placement in your designated Amazon S3 bucket. You can then download the backups from Amazon S3 and restore them on SQL Server on an Amazon EC2 instance, or run the `rds_restore_database` stored procedure to restore the database to Amazon RDS. You can also use [AWS Snowcone](https://aws.amazon.com/snowcone/) for databases up to 8 TB in size. For more information, see the [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) documentation and [Importing and exporting SQL Server databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Using), *Restoring a database* section, in the Amazon RDS documentation.

**Note**
AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/)for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
