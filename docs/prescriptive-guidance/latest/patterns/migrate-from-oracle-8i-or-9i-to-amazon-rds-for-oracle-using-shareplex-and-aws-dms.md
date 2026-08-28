---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms.html
---

# Migrate from Oracle 8i or 9i to Amazon RDS for Oracle using SharePlex and AWS DMS
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms"></a>

*Ramu Jagini, Amazon Web Services*

## Summary
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-summary"></a>

This pattern describes how to migrate an on-premises Oracle 8i or 9i database to an Amazon Relational Database Service (Amazon RDS) for Oracle database. You can use this pattern to complete your migration with reduced downtime by using Quest SharePlex for synchronous replication.

You must use an intermediate Oracle database instance for your migration because AWS Database Migration Service (AWS DMS) doesn’t support Oracle 8i or 9i as a source environment. You can use [SharePlex 7.6.3](https://www.quest.com/community/shareplex/f/forum/20700/where-can-download-7-6-3-or-support-9i-shareplex) to replicate from previous Oracle database versions to later Oracle database versions. The intermediate Oracle database instance is compatible as a target for SharePlex 7.6.3 and supported as a source for AWS DMS or newer releases of SharePlex. This support enables onward replication of data to the Amazon RDS for Oracle target environment.

Consider that several deprecated data types and features can impact a migration from Oracle 8i or 9i to the latest version of Oracle Database. To mitigate this impact, this pattern uses Oracle 11.2.0.4 as an intermediate database version to help optimize the schema code prior to migrating to the Amazon RDS for Oracle target environment.

## Prerequisites and limitations
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle 8i or 9i database in an on-premises environment
+ [Oracle Database 12c Release 2](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/index.html) (12CR2) for staging on Amazon Elastic Compute Cloud (Amazon EC2)
+ Quest SharePlex 7.6.3 (commercial grade)

**Limitations**
+ [RDS for Oracle limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.limitations.html)

**Product versions**
+ Oracle 8i or 9i for the source database
+ Oracle 12CR2 for the staging database (must match the Amazon RDS for Oracle version)
+ Oracle 12CR2 or later for the target database (Amazon RDS for Oracle)

## Architecture
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-architecture"></a>

**Source technology stack**
+ Oracle 8i or 9i database
+ SharePlex

**Target technology stack**
+ Amazon RDS for Oracle

**Migration architecture**

The following diagram shows how to migrate an Oracle 8i or 9i database from an on-premises environment to an Amazon RDS for Oracle DB instance in the AWS Cloud.

![Workflow for migrating an on-premises Oracle database to Amazon RDS on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6e07d586-fd74-4f3d-8e81-79dd55c445c3/images/36e1a5ff-908b-4cb7-96f7-997eb105f1d6.png)

The diagram shows the following workflow:

1. Enable the Oracle source database with archive log mode, force logging, and supplemental logging.

1. Restore the Oracle staging database from the Oracle source database by using Recovery Manager (RMAN) point-in-time recovery and [FLASHBACK\_SCN](https://docs.oracle.com/database/121/SUTIL/GUID-D408B112-1A81-4F68-BEFF-7403A9588DDB.htm#SUTIL849).

1. Configure SharePlex to read redo logs from the Oracle source database by using `FLASHBACK_SCN` (used in RMAN).

1. Start SharePlex replication to synchronize data from the Oracle source database to the Oracle staging database.

1. Restore the Amazon RDS for Oracle target database by using EXPDP and IMPDP with `FLASHBACK_SCN`.

1. Configure AWS DMS and its source tasks as the Oracle staging database and Amazon RDS for Oracle as the target database by using `FLASHBACK_SCN` (used in EXPDP).

1. Start AWS DMS tasks to synchronize data from the Oracle staging database to the Oracle target database.

## Tools
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-tools"></a>
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Quest SharePlex](https://support.quest.com/shareplex/11.0/technical-documents) is an Oracle-to-Oracle data replication tool for moving data with minimal downtime and no data loss.
+ [Recovery Manager (RMAN)](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmquick.htm) is an Oracle Database client that performs backup and recovery tasks on your databases. It greatly simplifies backing up, restoring, and recovering database files.
+ [Data Pump Export](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL823) helps you upload data and metadata into a set of operating system files called a dump file set. The dump file set can be imported only by the [Data Pump Import](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_import.htm#SUTIL300) utility or [DBMS\_DATAPUMP](https://docs.oracle.com/database/121/ARPLS/d_datpmp.htm#ARPLS356) package.

## Epics
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-epics"></a>

### Set up SharePlex and the Oracle staging database on Amazon EC2
<a name="set-up-shareplex-and-the-oracle-staging-database-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an EC2 instance. | 1. [Create an EC2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html). <br />2. Install Oracle 12CR2 on the EC2 instance to serve as the Oracle staging database. | Oracle administration |
| Prepare the staging database. | Prepare the Oracle staging database for restore as an upgrade on Oracle 12CR2 by taking the RMAN backup from the Oracle 8i or 9i database source environment.<br />For more information, see [Oracle 9i Recovery Manager User's Guide](https://docs.oracle.com/cd/B10500_01/server.920/a96566/toc.htm) and [Database Backup and Recovery User's Guide](https://docs.oracle.com/database/121/BRADV/rcmcomre.htm#BRADV8005) in the Oracle documentation. | Oracle administration |
| Configure SharePlex. | Configure the SharePlex source as an on-premises Oracle 8i or 9i database, and configure the target as the Oracle 12CR2 staging database hosted on Amazon EC2. | SharePlex, Oracle administration |

### Set up Amazon RDS for Oracle as your target environment
<a name="set-up-amazon-rds-for-oracle-as-your-target-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Oracle DB instance. | Create an Amazon RDS for Oracle database, and then connect Oracle 12CR2 to the database.<br />For more information, see [Creating an Oracle DB instance and connecting to a database on an Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html) in the Amazon RDS documentation. | DBA |
| Restore Amazon RDS for Oracle from the staging database. | 1. Take an EXPDP backup from the Oracle staging database server by using `FLASHBACK_SCN`.<br />2. Restore Amazon RDS for Oracle from the staging database.For more information, see [54 DBMS\_DATAPUMP](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_DATAPUMP.html#GUID-AEA7ED80-DB4A-4A70-B199-592287206348) in the Oracle documentation. | DBA |

### Set up AWS DMS
<a name="set-up-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create endpoints for the databases. | Create a source endpoint for the Oracle staging database and a target endpoint for the Amazon RDS for Oracle database.<br />For more information, see [How do I create source or target endpoints using AWS DMS?](https://aws.amazon.com/premiumsupport/knowledge-center/create-source-target-endpoints-aws-dms/) in the AWS Knowledge Center. | DBA |
| Create a replication instance. | Use AWS DMS to launch a replication instance for the Oracle staging database to the Amazon RDS for Oracle database.<br />For more information, see [How do I create an AWS DMS replication instance?](https://aws.amazon.com/premiumsupport/knowledge-center/create-aws-dms-replication-instance/) in the AWS Knowledge Center. | DBA |
| Create and start replication tasks. | Create AWS DMS replication tasks for change data capture (CDC) by using `FLASHBACK_SCN` from EXPDP (since the full load already happened through EXPDP).<br />For more information, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html) in the AWS DMS documentation. | DBA |

### Cut over to Amazon RDS for Oracle
<a name="cut-over-to-amazon-rds-for-oracle"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the application workload. | Stop the application servers and its applications during the planned cutover window. | App developer, DBA |
| Validate the synching of the on-premises Oracle staging database with the EC2 instance. | Confirm that all messages have been posted for replication tasks from the SharePlex replication instance to the Oracle staging database on Amazon EC2 by performing a few log switches on the on-premises source database.<br />For more information, see [6.4.2 Switching a Log File](https://docs.oracle.com/database/121/ADMQS/GUID-E30B4C65-2AC7-4A44-A58C-D3C121EB152F.htm#ADMQS12075) in the Oracle documentation. | DBA |
| Validate the synching of the Oracle staging database with the Amazon RDS for Oracle database. | Confirm that all your AWS DMS tasks have no lag and no errors, and then check the validation state of the tasks. | DBA |
| Stop the replication of SharePlex and Amazon RDS. | If both the SharePlex and AWS DMS replications are not showing any errors, then stop both replications. | DBA |
| Remap the application to Amazon RDS. | Share the Amazon RDS for Oracle endpoint details with the application server and its applications, and then start the application to resume business operations. | App developer, DBA |

### Test the AWS target environment
<a name="test-the-aws-target-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the Oracle staging database environment on AWS. | 1. Test the SharePlex replication and verify that there are no sync gaps or replication errors on the Oracle staging database.<br />2. Verify that the application behaves as expected through benchmarks defined in the on-premises environment. | SharePlex, Oracle administration |
| Test the Amazon RDS environment. | 1. Verify that all data propagated to Amazon RDS after replication is error free.<br />2. Point another application to the Amazon RDS DB instance, and then run performance tests to verify expected behavior.For more information, see [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) in the Amazon RDS documentation. | Oracle administration |

## Related resources
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-oracle-using-shareplex-and-aws-dms-resources"></a>
+ [Migrate with confidence](https://aws.amazon.com/cloud-migration/)
+ [Amazon EC2](https://aws.amazon.com/ec2/)
+ [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/)
+ [AWS Database Migration Service](https://aws.amazon.com/dms/)
+ [Debugging Your AWS DMS Migrations: What to Do When Things Go Wrong (Part 1)](https://aws.amazon.com/blogs/database/debugging-your-aws-dms-migrations-what-to-do-when-things-go-wrong-part-1/)
+ [Debugging Your AWS DMS Migrations: What to Do When Things Go Wrong (Part 2)](https://aws.amazon.com/blogs/database/debugging-your-aws-dms-migrations-what-to-do-when-things-go-wrong-part-2/)
+ [Debugging Your AWS DMS Migrations: What to Do When Things Go Wrong? (Part 3)](https://aws.amazon.com/blogs/database/debugging-your-aws-dms-migrations-what-to-do-when-things-go-wrong-part-3/)
+ [SharePlex for Database Replication](https://aws.amazon.com/marketplace/pp/B07943W4MJ)
+ [SharePlex: database replication for any environment](https://www.youtube.com/watch?v=ygS_ouUaNus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
