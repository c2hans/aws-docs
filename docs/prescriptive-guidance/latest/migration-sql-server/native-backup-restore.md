---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/native-backup-restore.html
---

# Native SQL Server backup/restore
<a name="native-backup-restore"></a>

Amazon Relational Database Service (Amazon RDS) supports native backup and restore operations for Microsoft SQL Server databases using full and differential backup (.bak) files. It also supports differential restore and log restore options on an Amazon RDS for SQL Server DB instance or Amazon EC2 SQL Server instance, to minimize downtime for your application.

**Note**
You can perform full, differential, and log restore operations on Amazon RDS for SQL Server. However, you can perform only full and differential backup (not log backup) at this time.

Using native .bak files is the simplest way to back up and restore SQL Server databases. You can use this method to migrate databases to or from Amazon RDS. You can back up and restore single databases instead of entire DB instances. You can also move databases between Amazon RDS for SQL Server DB instances.

When you use Amazon RDS, you can store and transfer backup files in Amazon Simple Storage Service (Amazon S3), for an added layer of protection for disaster recovery. For example:
+ You can create a full backup of your database from your local server, copy it to an Amazon S3 bucket, and then restore it onto an existing Amazon RDS for SQL Server DB instance.
+ You can take backups from an Amazon RDS for SQL Server DB instance, store them in Amazon S3, and then restore them wherever you want.
+ You can implement [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) configuration rules to archive or delete long-term backups.

Amazon RDS for SQL Server supports restoring SQL Server native backups onto SQL Server DB instances that have read replicas configured. This means that you don't have to remove the read replica before restoring the native backup file onto your Amazon RDS for SQL Server DB instance.

**Note**
You can use Migration Hub Orchestrator to automate and orchestrate your SQL Server database migrations to Amazon EC2 or Amazon RDS by using native backup and restore. For more information, see the [AWS Migration Hub Orchestrator section](mho.md).

The following diagram shows the native SQL Server backup/restore process. You can use Migration Hub Orchestrator to automate this process. You can use this process to back up and restore SQL Server databases to Amazon EC2 as well.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/d4be6875-264e-4b7c-a817-e4b66cbc92c9.png)

To automate backup and restore, see the [Migration Hub Orchestrator documentation](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html).

To set up native backup/restore using Amazon S3, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Enabling).

For limitations when using SQL Server native backup and restore, see [Limitations and recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Limitations) in the Amazon RDS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
