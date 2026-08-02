---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms.html
---

# Migrate from Oracle 8i or 9i to Amazon RDS for PostgreSQL using SharePlex and AWS DMS
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms"></a>

*Kumar Babu P G, Amazon Web Services*

## Summary
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-summary"></a>

This pattern describes how to migrate an on-premises Oracle 8i or 9i database to Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL. AWS Database Migration Service (AWS DMS) doesn't support Oracle 8i or 9i as a source, so Quest SharePlex replicates data from an on-premises 8i or 9i database to an intermediate Oracle database (Oracle 10g or 11g), which is compatible with AWS DMS.

From the intermediate Oracle instance, the schema and data are migrated to the PostgreSQL database on AWS by using AWS Schema Conversion Tool (AWS SCT) and AWS DMS. This method helps achieve continuous streaming of data from the source Oracle database to the target PostgreSQL DB instance with minimum replication lag. In this implementation, the downtime is limited to the length of time it takes to create or validate all the foreign keys, triggers, and sequences on the target PostgreSQL database.

The migration uses an Amazon Elastic Compute Cloud (Amazon EC2) instance with Oracle 10g or 11g installed to host the changes from the source Oracle database. AWS DMS uses this intermediate Oracle instance as the source to stream the data to Amazon RDS for PostgreSQL or Aurora PostgreSQL. Data replication can be paused and resumed from the on-premises Oracle database to the intermediate Oracle instance. It can also be paused and resumed from the intermediate Oracle instance to the target PostgreSQL database so you can validate the data by using either AWS DMS data validation or a custom data validation tool.

## Prerequisites and limitations
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A source Oracle 8i or 9i database in an on-premises data center
+ AWS Direct Connect configured between the on-premises data center and AWS
+ Java Database Connectivity (JDBC) drivers for AWS SCT connectors installed either on a local machine or on the EC2 instance where AWS SCT is installed
+ Familiarity with [using an Oracle database as an AWS DMS source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ Familiarity with [using a PostgreSQL database as an AWS DMS target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)
+ Familiarity with Quest SharePlex data replication

**Limitations**
+ The database size limit is 64 TB
+ The on-premises Oracle database must be Enterprise Edition

**Product versions**
+ Oracle 8i or 9i for the source database
+ Oracle 10g or 11g for the intermediate database
+ PostgreSQL 9.6 or later

## Architecture
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-architecture"></a>

**Source technology stack  **
+ Oracle 8i or 9i database
+ Quest SharePlex

**Target technology stack  **
+ Amazon RDS for PostgreSQL or Aurora PostgreSQL

** **

**Source and target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b6c30668-fc2e-4293-a59a-e01fd151f4bb/images/25082670-0bf3-4b20-8c80-99c6633b046f.png)

## Tools
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-tools"></a>
+ **AWS DMS** – [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) (AWS DMS) helps you migrate databases quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases.
+ **AWS SCT** – [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format compatible with the target database. Objects that cannot be automatically converted are clearly marked so that they can be manually converted to complete the migration. AWS SCT can also scan your application source code for embedded SQL statements and convert them as part of a database schema conversion project. During this process, AWS SCT performs cloud-native code optimization by converting legacy Oracle and SQL Server functions to their AWS equivalents, to help you modernize your applications while migrating your databases. When schema conversion is complete, AWS SCT can help migrate data from a range of data warehouses to Amazon Redshift by using built-in data migration agents.
+ **Quest SharePlex** – [Quest SharePlex](https://www.quest.com/register/120420/?gclid=Cj0KCQiA6IHwBRCJARIsALNjViVSt9fHqAsf9XbWkoCwKKyQqollR_5kSxNhBagh9s3spQT4IQCaVy0aAmCnEALw_wcB) is an Oracle-to-Oracle data replication tool for moving data with minimal downtime and no data loss.

## Epics
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-epics"></a>

### Create the EC2 instance and install Oracle
<a name="create-the-ec2-instance-and-install-oracle"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the network for Amazon EC2. | Create the virtual private cloud (VPC), subnets, internet gateway, route tables, and security groups. | AWS SysAdmin |
| Create the new EC2 instance. | Select the Amazon Machine Image (AMI) for the EC2 instance. Choose the instance size and configure instance details: the number of instances (1), the VPC and subnet from the previous step, auto-assign public IP, and other options. Add storage, configure security groups, and launch the instance. When prompted, create and save a key pair for the next step. | AWS SysAdmin |
| Install Oracle on the EC2 instance. | Acquire the licenses and the required Oracle binaries, and install Oracle 10g or 11g on the EC2 instance. | DBA |

### Set up SharePlex on an EC2 instance and configure data replication
<a name="set-up-shareplex-on-an-ec2-instance-and-configure-data-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up SharePlex. | Create an Amazon EC2 instance and install the SharePlex binaries that are compatible with Oracle 8i or 9i. | AWS SysAdmin, DBA |
| Configure data replication. | Follow SharePlex best practices to configure data replication from an on-premises Oracle 8i/9i database to an Oracle 10g/11g instance. | DBA |

### Convert the Oracle database schema to PostgreSQL
<a name="convert-the-oracle-database-schema-to-postgresql"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS SCT. | Create a new report, and then connect to Oracle as the source and PostgreSQL as the target. In project settings, open the SQL Scripting tab and change the target SQL script to Multiple Files. | DBA |
| Convert the Oracle database schema. | In the Action tab, choose Generate Report, Convert Schema, and then Save as SQL. | DBA |
| Modify the SQL scripts generated by AWS SCT. |  | DBA |

### Create and configure the Amazon RDS DB instance
<a name="create-and-configure-the-amazon-rds-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Amazon RDS DB instance. | In the Amazon RDS console, create a new PostgreSQL DB instance. | AWS SysAdmin, DBA |
| Configure the DB instance. | Specify the DB engine version, DB instance class, Multi-AZ deployment, storage type, and allocated storage. Enter the DB instance identifier, a master user name, and a master password. | AWS SysAdmin, DBA |
| Configure network and security. | Specify the VPC, subnet group, public accessibility, Availability Zone preference, and security groups. | AWS SysAdmin, DBA |
| Configure database options. | Specify the database name, port, parameter group, encryption, and master key. | AWS SysAdmin, DBA |
| Configure backups. | Specify the backup retention period, backup window, start time, duration, and whether to copy tags to snapshots. | AWS SysAdmin, DBA |
| Configure monitoring options. | Enable or disable enhanced monitoring and performance insights. | AWS SysAdmin, DBA |
| Configure maintenance options. | Specify auto minor version upgrade, maintenance window, and the start day, time, and duration. | AWS SysAdmin, DBA |
| Run the pre-migration scripts from AWS SCT. | On the Amazon RDS instance, run these scripts: create\_database.sql, create\_sequence.sql, create\_table.sql, create\_view.sql, and create\_function.sql. | AWS SysAdmin, DBA |

### Migrate data by using AWS DMS
<a name="migrate-data-by-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance in AWS DMS. | Complete the fields for the name, instance class, VPC (same as for the EC2 instance), Multi-AZ, and public accessibility. In the advanced configuration section, specify allocated storage, subnet group, Availability Zone, VPC security groups, and AWS Key Management Service (AWS KMS) root key. | AWS SysAdmin, DBA |
| Create the source database endpoint. | Specify the endpoint name, type, source engine (Oracle), server name (Amazon EC2 private DNS name), port, SSL mode, user name, password, SID, VPC (specify the VPC that has the replication instance), and replication instance. To test the connection, choose Run Test, and then create the endpoint. You can also configure the following advanced settings: maxFileSize and numberDataTypeScale. | AWS SysAdmin, DBA |
| Create the AWS DMS replication task. | Specify the task name, replication instance, source and target endpoints, and replication instance. For migration type, choose "Migrate existing data and replicate ongoing changes." Clear the "Start task on create" check box. | AWS SysAdmin, DBA |
| Configure the AWS DMS replication task settings. | For target table preparation mode, choose "Do nothing." Stop the task after the full load completes to create primary keys. Specify limited or full LOB mode, and enable control tables. Optionally, you can configure the CommitRate advanced setting. | DBA |
| Configure the table mappings. | In the table mappings section, create an Include rule for all tables in all schemas included in the migration, and then create an Exclude rule. Add three transformation rules to convert the schema, table, and column names to lowercase, and add any other rules needed for this specific migration. | DBA |
| Start the task. | Start the replication task. Make sure that the full load is running. Run ALTER SYSTEM SWITCH LOGFILE on the primary Oracle database to kick-start the task. | DBA |
| Run the mid-migration scripts from AWS SCT. | In Amazon RDS for PostgreSQL, run these scripts: create\_index.sql and create\_constraint.sql. | DBA |
| Restart the task to continue change data capture (CDC). | In the Amazon RDS for PostgreSQL DB instance, run VACUUM, and restart the AWS DMS task to apply the cached CDC changes. | DBA |

### Cut over to the PostgreSQL database
<a name="cut-over-to-the-postgresql-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the AWS DMS logs and metadata tables. | Validate any errors and fix if required. | DBA |
| Stop all Oracle dependencies. | Shut down listeners on the Oracle database and run ALTER SYSTEM SWITCH LOGFILE. Stop the AWS DMS task when it shows no activity. | DBA |
| Run the post-migration scripts from AWS SCT. | In Amazon RDS for PostgreSQL, run these scripts: create\_foreign\_key\_constraint.sql and create\_triggers.sql. | DBA |
| Complete any additional Amazon RDS for PostgreSQL steps. | Increment sequences to match Oracle if needed, run VACUUM and ANALYZE, and take a snapshot for compliance. | DBA |
| Open the connections to Amazon RDS for PostgreSQL. | Remove the AWS DMS security groups from Amazon RDS for PostgreSQL, add production security groups, and point your applications to the new database. | DBA |
| Clean up AWS DMS resources. | Remove the endpoints, replication tasks, replication instances, and the EC2 instance. | SysAdmin, DBA |

## Related resources
<a name="migrate-from-oracle-8i-or-9i-to-amazon-rds-for-postgresql-using-shareplex-and-aws-dms-resources"></a>
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon RDS for PostgreSQL pricing](https://aws.amazon.com/rds/postgresql/pricing/)
+ [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ [Using a PostgreSQL database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)
+ [Quest SharePlex documentation](https://support.quest.com/shareplex/9.0.2/technical-documents)
