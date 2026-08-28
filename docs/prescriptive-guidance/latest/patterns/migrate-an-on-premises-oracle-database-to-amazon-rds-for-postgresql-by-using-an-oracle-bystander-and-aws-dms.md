---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms.html
---

# Migrate an on-premises Oracle database to Amazon RDS for PostgreSQL by using an Oracle bystander and AWS DMS
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms"></a>

*Cady Motyka, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-summary"></a>

This pattern describes how you can migrate an on-premises Oracle database to either of the following PostgreSQL-compatible AWS database services with minimal downtime:
+ Amazon Relational Database Service (Amazon RDS) for PostgreSQL
+ Amazon Aurora PostgreSQL-Compatible Edition

The solution uses AWS Database Migration Service (AWS DMS) to migrate the data, AWS Schema Conversion Tool (AWS SCT) to convert the database schema, and an Oracle bystander database to help manage the migration. In this implementation, the downtime is restricted to however long it takes to create or validate all of the foreign keys on the database.

The solution also uses Amazon Elastic Compute Cloud (Amazon EC2) instances with an Oracle bystander database to help control the stream of data through AWS DMS. You can temporarily pause streaming replication from the on-premises Oracle database to the Oracle bystander to activate AWS DMS to catch up on data validation, or to use another data validation tool. The Amazon RDS for PostgreSQL DB instance or Aurora PostgreSQL-Compatible DB instance and the bystander database will have the same data when AWS DMS finishes migrating current changes.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle database in an on-premises data center with an Active Data Guard standby database configured
+ AWS Direct Connect configured between the on-premises data center and AWS Secrets Manager for storing the database secrets
+ Java Database Connectivity (JDBC) drivers for AWS SCT connectors, installed either on a local machine or on the EC2 instance where AWS SCT is installed
+ Familiarity with [using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ Familiarity with [using a PostgreSQL database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ AWS DMS supports all Oracle database editions for versions 10.2 and later (for versions 10.x), 11g and up to 12.2, 18c, and 19c. For the latest list of supported versions, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support. For information about Oracle database versions supported by AWS SCT, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).
+ AWS DMS supports PostgreSQL versions 9.4 and later (for versions 9.x), 10.x, 11.x, 12.x, and 13.x. For the latest information, see [Using a PostgreSQL Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html) in the AWS documentation.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-architecture"></a>

**Source technology stack**
+ An on-premises Oracle database
+ An EC2 instance that holds a bystander for the Oracle database

**Target technology stack**
+ Amazon RDS for PostgreSQL or Aurora PostgreSQL instance, PostgreSQL 9.3 and later

**Target architecture**

The following diagram shows an example workflow for migrating an Oracle database to a PostgreSQL-compatible AWS database by using AWS DMS and an Oracle bystander:

![Migrating an on-premises Oracle database to PostgreSQL on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6f5d5500-8b09-4bd1-8ef9-e670d58d07f8/images/1de98abd-c143-481a-b55f-e8d00eb96a38.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-epics"></a>

### Convert the Oracle database schema to PostgreSQL
<a name="convert-the-oracle-database-schema-to-postgresql"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS SCT. | Create a new report, and connect to Oracle as the source and PostgreSQL as the target. In **Project Settings**, go to the **SQL Scripting** tab. Change the **Target SQL Script** to **Multiple Files**. These files will be used later and named the following:+ create\_database.sql<br />+ create\_sequence.sql <br />+ create\_table.sql <br />+ create\_view.sql <br />+ create\_function.sql | DBA |
| Convert the Oracle database schema. | In the **Action** tab, choose **Generate Report**. Then, choose **Convert Schema** and choose **Save as SQL**. | DBA |
| Modify the scripts. | For example, you might want to modify the script if a number in the source schema has been converted to numeric format in PostgreSQL, but you want to use **BIGINT **instead for better performance. | DBA |

### Create and configure the Amazon RDS DB instance
<a name="create-and-configure-the-amazon-rds-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Amazon RDS DB instance. | In the correct AWS Region, create a new PostgreSQL DB instance. For more information, see [Creating a PostgreSQL DB instance and connecting to a database on a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html) in the Amazon RDS documentation. | AWS SysAdmin, DBA |
| Configure DB instance specifications. | Specify the DB engine version, DB instance class, Multi-AZ deployment, storage type, and allocated storage. Enter the DB instance identifier, a primary user name, and a primary password. | AWS SysAdmin, DBA |
| Configure network and security. | Specify the virtual private cloud (VPC), subnet group, public accessibility, Availability Zone preference, and security groups. | DBA, SysAdmin |
| Configure database options. | Specify the database name, port, parameter group, encryption, and KMS key. | AWS SysAdmin, DBA |
| Configure backups. | Specify the backup retention period, backup window, start time, duration, and whether to copy tags to snapshots. | AWS SysAdmin, DBA |
| Configure monitoring options. | Activate or deactivate enhanced monitoring and performance insights. | AWS SysAdmin, DBA |
| Configure maintenance options. | Specify auto minor version upgrade, maintenance window, and start day, time, and duration. | AWS SysAdmin, DBA |
| Run the pre-migration scripts from AWS SCT. | On the Amazon RDS instance, run the following scripts generated by AWS SCT:+ create\_database.sql <br />+ create\_sequence.sql <br />+ create\_table.sql <br />+ create\_view.sql <br />+ create\_function.sql | AWS SysAdmin, DBA |

### Configure the Oracle bystander in Amazon EC2
<a name="configure-the-oracle-bystander-in-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the network for Amazon EC2. | Create the new VPC, subnets, internet gateway, route tables, and security groups. | AWS SysAdmin |
| Create the EC2 instance. | In the appropriate AWS Region, create a new EC2 instance. Select the Amazon Machine Image (AMI), choose the instance size, and configure instance details: number of instances (1), the VPC and subnet you created in the previous task, auto-assign public IP, and other options. Add storage, configure security groups, and launch. When prompted, create and save a key pair for the next step. | AWS SysAdmin |
| Connect the Oracle source database to the EC2 instance. | Copy the IPv4 public IP address and DNS to a text file and connect by using SSH as follows: **ssh -i "your\_file.pem" ec2-user@<your-IP-address-or-public-DNS>**. | AWS SysAdmin |
| Set up the initial host for a bystander in Amazon EC2. | Set up SSH keys, bash profile, ORATAB, and symbolic links. Create Oracle directories. | AWS SysAdmin, Linux Admin |
| Set up the database copy for a bystander in Amazon EC2 | Use RMAN to create a database copy, enable supplemental logging, and create the standby control file. After copying is complete, place the database in recovery mode. | AWS SysAdmin, DBA |
| Set up Oracle Data Guard. | Modify your **listener.ora** file and start the listener. Set up a new archive destination. Place the bystander in recovery mode, replace temporary files to avoid future corruption, install a crontab if necessary to prevent the archive directory from running out of space, and edit the **manage-trclog-files-oracle.cfg** file for the source and standby. | AWS SysAdmin, DBA |
| Prep the Oracle database to sync shipping. | Add the standby log files and change the recovery mode. Change the log shipping to **SYNC AFFIRM** on both the source primary and the source standby. Switch logs on primary, confirm via the Amazon EC2 bystander alert log that you are using the standby log files, and confirm that the redo stream is flowing in SYNC. | AWS SysAdmin, DBA |

### Migrate data with AWS DMS
<a name="migrate-data-with-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance in AWS DMS. | Complete the fields for the name, instance class, VPC (same as the Amazon EC2 instance), Multi-AZ, and public accessibility. Under **Advance**, specify allocated storage, subnet group, Availability Zone, VPC security groups, and AWS Key Management Service (AWS KMS) key. | AWS SysAdmin, DBA |
| Create the source database endpoint. | Specify the endpoint name, type, source engine (Oracle), server name (Amazon EC2 private DNS name), port, SSL mode, user name, password, SID, VPC (specify the VPC that has the replication instance), and replication instance. To test the connection, choose **Run Test**, and then create the endpoint. You can also configure the following advanced settings: **maxFileSize** and **numberDataTypeScale**. | AWS SysAdmin, DBA |
| Connect AWS DMS to Amazon RDS for PostgreSQL. | Create a migration security group for connections across VPCs. | AWS SysAdmin, DBA |
| Create the target database endpoint. | Specify the endpoint name, type, source engine (PostgreSQL), server name (Amazon RDS endpoint), port, SSL mode, user name, password, database name, VPC (specify the VPC that has the replication instance), and replication instance. To test the connection, choose **Run Test**, and then create the endpoint. You can also configure the following advanced settings: **maxFileSize **and **numberDataTypeScale**. | AWS SysAdmin, DBA |
| Create the AWS DMS replication task. | Specify the task name, replication instance, source and target endpoints, and replication instance. For migration type, choose **Migrate existing data and replicate ongoing changes**. Clear the **Start task on create** checkbox. | AWS SysAdmin, DBA |
| Configure the AWS DMS replication task settings. | For target table preparation mode, choose **Do nothing**. Stop task after full load completes (to create primary keys). Specify limited or full LOB mode, and activate control tables. Optionally, you can configure the **CommitRate** advance setting. | DBA |
| Configure table mappings. | In the **Table mappings** section, create an **Include** rule for all tables in all schemas included in the migration, and then create an **Exclude** rule. Add three transformation rules to convert the schema, table, and column names to lowercase, and add any other rules needed for this specific migration. | DBA |
| Start the task. | Start the replication task. Make sure that the full load is running. Run **ALTER SYSTEM SWITCH LOGFILE** on the primary Oracle database to kick-start the task. | DBA |
| Run the mid-migration scripts from AWS SCT. | In Amazon RDS for PostgreSQL, run the following scripts generated by AWS SCT: + create\_index.sql<br />+ create\_constraint.sql | DBA |
| Restart the task to continue change data capture (CDC). | Run **VACUUM **on the Amazon RDS for PostgreSQL DB instance, and restart the AWS DMS task to apply cached CDC changes. | DBA |

### Cut over to the PostgreSQL database
<a name="cut-over-to-the-postgresql-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review the AWS DMS logs and validation tables for any errors. | Check and fix any replication or validation errors. | DBA |
| Stop all Oracle dependencies. | Stop all Oracle dependencies, shut down listeners on the Oracle database, and run **ALTER SYSTEM SWITCH LOGFILE**. Stop the AWS DMS task when it shows no activity. | DBA |
| Run the post-migration scripts from AWS SCT. | In Amazon RDS for PostgreSQL, run the following scripts generated by AWS SCT:+ create\_foreign\_key\_constraint.sql<br />+ create\_triggers.sql | DBA |
| Complete additional Amazon RDS for PostgreSQL steps. | Increment sequences to match Oracle if needed, run **VACUUM** and **ANALYZE**, and take a snapshot for compliance. | DBA |
| Open the connections to Amazon RDS for PostgreSQL. | Remove the AWS DMS security groups from Amazon RDS for PostgreSQL, add production security groups, and point your applications to the new database. | DBA |
| Clean up AWS DMS objects. | Remove the endpoints, replication tasks, replication instances, and the EC2 instance. | SysAdmin, DBA |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-postgresql-by-using-an-oracle-bystander-and-aws-dms-resources"></a>
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon RDS for PostgreSQL pricing](https://aws.amazon.com/rds/postgresql/pricing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
