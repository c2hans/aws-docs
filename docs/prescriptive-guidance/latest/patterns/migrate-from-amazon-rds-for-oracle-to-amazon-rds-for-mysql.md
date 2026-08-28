---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql.html
---

# Migrate from Amazon RDS for Oracle to Amazon RDS for MySQL
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql"></a>

*Jitender Kumar, Srini Ramaswamy, and Neha Sharma, Amazon Web Services*

## Summary
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-summary"></a>

This pattern provides guidance for migrating an Amazon Relational Database Service (Amazon RDS) for Oracle DB instance to an Amazon RDS for MySQL DB instance on Amazon Web Services (AWS). The pattern uses AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (AWS SCT).

The pattern provides best practices for handling the migration of stored procedures. It also covers and code changes to support the application layer.

## Prerequisites and limitations
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An Amazon RDS for Oracle source database.
+ An Amazon RDS for MySQL target database. Source and target databases should be in the same virtual private cloud (VPC). If you’re using multiple VPCs, or you must have the required access permissions.
+ Security groups that allow connectivity between the source and target databases, AWS SCT, the application server, and AWS DMS.
+ A user account with the required privilege to run AWS SCT on the source database.
+ Supplemental logging enabled for running AWS DMS on the source database.

**Limitations**
+ The source and target Amazon RDS database size limit is 64 TB. For Amazon RDS size information, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).
+ Oracle is case-insensitive for database objects, but MySQL is not. AWS SCT can handle this issue while creating an object. However, some manual work is required to support full case insensitivity.
+ This migration doesn't use MySQL extensions to enable Oracle-native functions. AWS SCT handles most of the conversion, but some work is required to change code manually.
+ Java Database Connectivity (JDBC) driver changes are required in the application.

**Product versions**
+ Amazon RDS for Oracle 12.2.0.1 and later. For currently supported RDS for Oracle versions, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.database-versions.html).
+ Amazon RDS for MySQL 8.0.15 and later. For currently supported RDS for MySQL versions, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html).
+ AWS DMS version 3.3.0 and later. See the AWS documentation for more information about AWS DMS supported [source endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html) and [target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html).
+ AWS SCT version 1.0.628 and later.  See the [AWS SCT source and target endpoint support matrix](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) in the AWS documentation.

## Architecture
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-architecture"></a>

**Source technology stack**
+ Amazon RDS for Oracle. For more information, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html).

**Target technology stack**
+ Amazon RDS for MySQL. For more information, see [Using a MySQL-Compatible database as a target for AWS DMS](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html).

**Migration architecture**

In the following diagram, AWS SCT copies and converts schema objects from the Amazon RDS for Oracle source database and sends the objects to the Amazon RDS for MySQL target database. AWS DMS replicates data from the source database and sends it to the Amazon RDS for MySQL instance.

![AWS SCT, AWS DMS, and Amazon RDS deployed in a private subnet.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e1efa7c2-47c1-4677-80bc-6b19250fc0d6/images/b54a8442-9ab9-4074-b8f6-a08f87fa2f52.jpeg)

## Tools
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-tools"></a>
+ [AWS Data Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud. This pattern uses [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) and [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html).
+ [AWS Schema Conversion Tool (AWS SCT)](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

## Epics
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-epics"></a>

### Prepare for migration
<a name="prepare-for-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions and engines. |  | DBA |
|  Identify hardware requirements for the target server instance. |  | DBA, SysAdmin |
| Identify storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Choose the proper instance type (capacity, storage features, network features). |  | DBA, SysAdmin |
| Identify network-access security requirements for the source and target databases. |  | DBA, SysAdmin  |
| Choose an application migration strategy. | Consider whether you want full downtime or partial downtime for cutover activities. | DBA, SysAdmin, App owner |

### Configure infrastructure
<a name="configure-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC and subnets. |  | SysAdmin |
| Create security groups and network access control lists (ACLs). |  | SysAdmin |
| Configure and start the Amazon RDS for Oracle instance. |  | DBA, SysAdmin |
| Configure and start the Amazon RDS for MySQL instance.  |  | DBA, SysAdmin |
| Prepare a test case for validation of code conversion. | This will help in unit-testing for the converted code. | DBA, Developer |
| Configure the AWS DMS instance. |  |  |
| Configure source and target endpoints in AWS DMS. |  |  |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate the target database script using AWS SCT. | Check the accuracy of the code that was converted by AWS SCT. Some manual work will be required. | DBA, Developer |
| In AWS SCT, choose the "Case Insensitive" setting. | In AWS SCT, choose Project Settings, Target Case Sensitivity, Case Insensitive. | DBA, Developer |
| In AWS SCT, choose not to use the Oracle native function. | In Project Settings, check the functions TO\_CHAR/TO\_NUMBER/TO\_DATE. | DBA, Developer |
| Make changes for "sql%notfound" code. | You might have to convert the code manually. |  |
| Query on tables and objects in stored procedures (use lowercase queries). |  | DBA, Developer |
| Create the primary script after all changes are made, and then deploy the primary script on the target database. |  | DBA, Developer |
| Unit-test stored procedures and application calls using sample data.  |  |  |
| Clean up data that was created during unit testing. |  | DBA, Developer |
| Drop foreign key constraints on the target database. | This step is required to load initial data. If you don't want to drop the foreign key constraints, you must create a migration task for data specific to the primary and secondary tables. | DBA, Developer |
| Drop primary keys and unique keys on the target database. | This step results in better performance for the initial load. | DBA, Developer |
| Enable supplemental logging on the source database.  |  | DBA |
| Create a migration task for the initial load in AWS DMS, and then run it. | Choose the option to migrate existing data. | DBA |
| Add the primary keys and foreign keys to the target database. | Constraints need to be added after the initial load. | DBA, Developer |
| Create a migration task for ongoing replication. | Ongoing replication keeps the target database synchronized with the source database. | DBA |

### Migrate applications
<a name="migrate-applications"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Replace Oracle native functions with MySQL native functions. |  | App owner |
| Make sure that only lowercase names are used for database objects in SQL queries. |  | DBA, SysAdmin, App owner |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the application server. |  | App owner |
| Validate that the source and target databases are in sync. |  | DBA, App owner |
| Stop the Amazon RDS for Oracle DB instance. |  | DBA |
| Stop the migration task. | This will stop automatically after you complete the previous step. | DBA |
| Change the JDBC connection from Oracle to MySQL. |  | App owner, DBA |
| Start the application. |  | DBA, SysAdmin, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review and validate the project documents. |  | DBA, SysAdmin |
| Gather metrics about time to migrate, percentage of manual versus tool tasks, cost savings, etc. |  | DBA, SysAdmin |
| Stop and delete AWS DMS instances. |  | DBA |
| Remove the source and target endpoints. |  | DBA |
| Remove migration tasks. |  | DBA |
| Take a snapshot of the Amazon RDS for Oracle DB instance. |  | DBA |
| Delete the Amazon RDS for Oracle DB instance. |  | DBA |
| Shut down and delete any other temporary AWS resources you used. |  | DBA, SysAdmin |
| Close the project and provide any feedback. |  | DBA |

## Related resources
<a name="migrate-from-amazon-rds-for-oracle-to-amazon-rds-for-mysql-resources"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/Welcome.html)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
