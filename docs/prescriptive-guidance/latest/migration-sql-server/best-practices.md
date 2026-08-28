---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/best-practices.html
---

# Best practices for migrating to RDS for SQL Server
<a name="best-practices"></a>

Based on the assessment of your database and your project requirements, if your goal is to migrate to Amazon RDS for SQL Server, follow the best practices in this section to provision your target database, perform the migration, and test, operate, and optimize your Amazon RDS for SQL Server database.

**Important**
Make sure that you have a rollback plan before you migrate your database.

**Note**
You can use Migration Hub Orchestrator to automate and orchestrate your SQL Server database migrations to Amazon EC2 or Amazon RDS by using native backup and restore. For more information, see the [AWS Migration Hub Orchestrator section](mho.md).

## Provisioning your target database
<a name="provision"></a>

After you finish assessing, planning, and preparing your database migration strategy, follow these best practices when provisioning your Amazon RDS for SQL Server database:
+ Right-size the Amazon RDS for SQL Server DB instance based on your requirements for CPU, memory, IOPS, and storage type. (If you're using SQL Server Standard edition, provision CPU and memory within the limitations of Standard edition.)
+ Set the correct time zone and collation.
+ Make sure to launch Amazon RDS in the correct virtual private cloud (VPC).
+ Create the security groups with correct port and IP addresses.
+ Provision your Amazon RDS database in a private subnet for security.
+ If possible, provision the SQL Server instance with the latest version of SQL Server.
+ Create a separate option group and parameter group for each Amazon RDS database.
+ Collect and extract logins, users, and roles for migration.
+ Review SQL Server Agent jobs for maintenance and applications that need to be migrated.

## Backing up from your source database
<a name="backup"></a>

There are many tools for migrating a SQL Server database to an Amazon RDS for SQL Server database. The most commonly used method is using SQL Server native backup and restore if your requirements allow downtime.

If you have limited downtime, you can use native SQL Server backup/restore with differential backup and log backup. Or you can use AWS DMS, which provides three options: full-load, full-load and CDC, or CDC only.

## Transferring data dump files to AWS
<a name="transfer-data"></a>
+ If you're using AWS Direct Connect, which provides high bandwidth connectivity between your on-premises environment and AWS, you can copy your SQL Server backups to Amazon S3 and set up [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.Options.S3-integration.html). You will have to set up an AWS Identity and Access Management (IAM) role to allow Amazon S3 bucket access to Amazon RDS.
+ If you don't have high bandwidth through AWS Direct Connect, use AWS Snowball to transfer large database backup files. You can also use AWS DMS to transfer the data when replication is required.

## Restoring data to your target database
<a name="restore-data"></a>
+ If you're migrating a very large database, we recommend that you provision a bigger [Amazon RDS instance type](https://aws.amazon.com/rds/instance-types/) initially, for the duration of the migration, for faster data loads.
+ Disable Multi-AZ. (This can be re-enabled after migration.)
+ Disable backup retention. (This can be re-enabled after migration.)
+ Restore the database by using the native SQL Server **restore** command.
+ Create logins and users, and fix orphaned users, if required.
+ Create SQL Server Agent jobs and review the schedule, as needed.

## Post-migration steps
<a name="post-migration"></a>

After the migration is complete, you can:
+ Change the DB instance to the right-sized instance type.
+ Enable Multi-AZ and backup retention.
+ Make sure that all jobs are created on secondary nodes (for Multi-AZ configuration).
+ Publish SQL Server error and agent logs to Amazon CloudWatch Logs, and use CloudWatch to view metrics and create alarms. For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.SQLServer.html).
+ Enable [enhanced monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) to get metrics for your DB instance in real time.
+ Set up Amazon Simple Notification Service (Amazon SNS) topics for alerts.

## Testing the migration
<a name="test-migration"></a>

We recommend the following tests to validate your application against your new Amazon RDS for SQL Server database:
+ Perform functional testing.
+ Compare the performance of SQL queries in your source and target databases, and tune the queries as needed. Some queries might perform more slowly in the target database, so we recommend that you capture the baselines of the SQL queries in the source database.

For additional validation during the proof-of-concept (POC) phase, we recommend the following supplemental tests:
+ Run performance tests to ensure that they meet your business expectations.
+ Test database failover, recovery, and restoration to make sure that you're meeting RPO and RTO requirements.
+ List all critical jobs and reports, and run them on Amazon RDS to evaluate their performance against your service-level agreements (SLAs).

## Operating and optimizing your Amazon RDS database
<a name="operate-optimize"></a>

When your database is on AWS, make sure that you are following best practices in areas such as monitoring, alerting, backups, and high availability in the cloud. For example:
+ Set up CloudWatch monitoring, and enable detailed monitoring.
+ Use [Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) and other third-party monitoring solutions like [SentryOne](https://www.sentryone.com/) or [Foglight for SQL Server](https://www.quest.com/products/foglight-for-sql-server/) to monitor your database.
+ Set up alerts by using Amazon SNS topics.
+ Set up automatic backups by using [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) or native SQL Server backups, and copy to Amazon S3.
+ For high availability, set up the Amazon RDS Multi-AZ feature.
+ If you need read-only databases, [set up a read replica](rds-sql.md#rds-sql-replicas) within the same or across AWS Regions according to your needs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
