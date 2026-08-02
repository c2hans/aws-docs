---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/best-practices.html
---

# Best practices for migrating to Amazon RDS for Oracle
<a name="best-practices"></a>

Based on the assessment of your database and your project requirements, if your goal is to migrate to Amazon RDS for Oracle, follow the best practices in this section to provision your target database, perform the migration, and test, operate, and optimize your Amazon RDS for Oracle database.

**Important**
     Make sure that you have a rollback plan before you migrate your database.

## Provisioning your target database
<a name="provision"></a>

After you finish assessing, planning, and preparing your database migration strategy, follow these best practices when provisioning your Amazon RDS for Oracle database:
+ Right-size the Amazon RDS for Oracle DB instance based on your requirements for CPU, memory, IOPS, and storage type.
+ Set the correct time zone and character set.
+ Make sure to launch Amazon RDS in the correct virtual private cloud (VPC).
+ Create the security groups with correct port and IP addresses.
+ Provision your Amazon RDS database in a private subnet for security.
+ If possible, provision the DB instance by using the latest Oracle Database version, which is currently 19c. Earlier versions are nearing end of support. For more information, see [Amazon RDS support for Oracle Database 19c](https://aws.amazon.com/about-aws/whats-new/2019/11/amazon-rds-for-oracle-now-supports-oracle-database-19c/).
+ If you want to use encryption, always enable it while you are provisioning the Amazon RDS database.
+ Create a separate option group and parameter group for each Amazon RDS database.

## Exporting data from your source database
<a name="export-data"></a>

There are many tools for migrating an Oracle database to an Amazon RDS for Oracle database. The most commonly used tool is Oracle Data Pump. Before you export your source Oracle database, check the following to facilitate the export process:
+ Check the database size, to see if you can migrate it schema by schema, instead of migrating the full database. Migrating schemas individually is less error prone and more manageable than migrating them all at once.
+ Export data in parallel mode, by using the Oracle Data Pump PARALLEL parameter, for better performance.
+ Check if the tables have large objects (LOBs). If you have large tables with LOBs, we recommend that you export those tables separately.
+ During the export process, avoid running long database transactions on your source database to avoid Oracle read inconsistency errors.
+ If you are using replication tools such as AWS DMS, Oracle GoldenGate, or Quest SharePlex, make sure that you have enough space on your on-premises server to hold archive logs for 24-72 hours, depending on how long the migration takes.

## Transferring data dump files to AWS
<a name="transfer-data"></a>

If you're using AWS Direct Connect, which provides high bandwidth connectivity between your on-premises environment and AWS, you can copy the Data Pump files by using either the Oracle [DBMS\_FILE\_TRANSFER](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_FILE_TRANSFER.html) utility or the [Amazon S3 integration feature](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html). If you do not have high bandwidth through AWS Direct Connect, use AWS Snowball to transfer large database export dump files.

## Importing data to your target database
<a name="import-data"></a>
+ If you're migrating a very large database, we recommend that you provision a bigger [Amazon RDS instance type](https://aws.amazon.com/rds/instance-types/) initially, for the duration of the migration, for faster data loads. After the migration is complete, you can change the DB instance to the right-sized instance type.
+ Increase the size of redo log files, undo tablespaces, and temporary tablespaces to improve performance during migration, if needed.
+ Disable the Multi-AZ option during the import process, and enable it after migration is complete.
+ Disable the generation of archive logs by setting the backup retention to zero to achieve faster data load.
+ Prepare the target database by creating tablespaces, users, roles, profiles, and schemas in advance.
+ If you have large tables with LOBs, import each LOB table separately.

## Post-import steps
<a name="post-import"></a>
+ Check the import log files for errors, and fix any errors after the import is complete.
+ Check for invalid objects. If you find any, compile and fix them.
+ Some procedures might not compile due to lack of permissions on SYS objects that are not allowed or supported in Amazon RDS. These procedures have to be rewritten.
+ If you are using sequences, validate the sequence values against the source database to avoid sequence inconsistency.
+ Make sure that the object count in your Amazon RDS database is the same as in the source database. Validate tables, indexes, procedures, triggers, functions, packages, constraints, and other objects.
+ If your source database has database links to other databases, test the connectivity to confirm that the links still work.
+ Gather dictionary-level and schema-level statistics for optimal performance.

## Testing the migration
<a name="test-migration"></a>

We recommend the following tests to validate your application against your new Amazon RDS for Oracle database:
+ You might have to upgrade your Oracle client software or JDBC software based on the Amazon RDS for Oracle database version. If you've migrated to a newer version of Oracle Database, it might not support older versions of Oracle client software.
+ Perform functional testing.
+ Compare the performance of SQL queries in your source and target databases, and tune the queries as needed. Some queries might perform more slowly in the target database, so we recommend that you capture the baselines of the SQL queries in the source database.
+ When the application team finishes testing and confirms that your Amazon RDS database is functioning properly, you can:
  + Right-size the Amazon RDS DB instance based on your assessment.
  + Enable backup retentions.
  + Enable archive logs.
  + Reset the size of redo log files.
  + Enable the Multi-AZ option.
  + Create Amazon CloudWatch alarms and set up Amazon Simple Notification Service (Amazon SNS) topics for alerts.

For additional validation during the proof-of-concept (POC) phase, we recommend the following supplemental tests:
+ Run performance tests to ensure that they meet your business expectations.
+ Test database failover, recovery, and restoration to make sure that you're meeting RPO and RTO requirements.
+ List all critical jobs and reports, and run them on Amazon RDS to evaluate their performance against your service-level agreements (SLAs).

## Operating and optimizing your Amazon RDS database
<a name="operate-optimize"></a>

When your database is on AWS, make sure that you are following best practices in areas such as monitoring, alerting, backups, and high availability in the cloud. For example:
+ Set up CloudWatch monitoring, and enable detailed monitoring.
+ Use [Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) and the [Oracle Enterprise Manager (OEM) Management Agent](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OEMAgent.html) to monitor your database.
+ Set up alerts by using SNS topics.
+ Set up automatic backups using [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html). You can also use Oracle Data Pump backups or take manual snapshots.
+ For high availability, set up the Amazon RDS Multi-AZ feature.
+ If you need read-only databases, [set up a Read Replica](rds-oracle.md#rds-oracle-replicas) within the same or across AWS Regions according to your needs.
