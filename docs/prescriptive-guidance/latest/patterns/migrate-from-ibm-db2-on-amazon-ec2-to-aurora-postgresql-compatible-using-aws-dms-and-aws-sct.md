---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html
---

# Migrate from IBM Db2 on Amazon EC2 to Aurora PostgreSQL-Compatible using AWS DMS and AWS SCT
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct"></a>

*Sirsendu Halder and Abhimanyu Chhabra, Amazon Web Services*

## Summary
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-summary"></a>

This pattern provides guidance for migrating an IBM Db2 database on an Amazon Elastic Compute Cloud (Amazon EC2) instance to an Amazon Aurora PostgreSQL-Compatible Edition DB instance. This pattern uses AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (AWS SCT) for data migration and schema conversion.

The pattern targets an online migration strategy with little or no downtime for a multi-terabyte IBM Db2 database that has a high number of transactions. We recommend that you convert the columns in primary keys (PKs) and foreign keys (FKs) with the data type `NUMERIC` to `INT` or `BIGINT` in PostgreSQL for better performance.

## Prerequisites and limitations
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source IBM Db2 database on an EC2 instance

**Product versions**
+ DB2/LINUXX8664 version 11.1.4.4 and later

## Architecture
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack**** **
+ A Db2 database on an EC2 instance

**Target technology stack**
+ An Aurora PostgreSQL-Compatible version 10.18 or later DB instance

**Database migration architecture**** **

![Using AWS DMS to migrate from IMB Db2 on Amazon EC2 to Aurora PostgreSQL-Compatible.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5e737fab-3e04-4887-9fb0-d1c88503b57d/images/789fabcc-8052-40d5-a746-986d799576e9.png)

## Tools
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate databases into the AWS Cloud or between combinations of cloud and on-premises setups. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. You can use AWS DMS to migrate your data to and from the most widely used commercial and open-source databases. AWS DMS supports heterogeneous migrations between different database platforms, such as IBM Db2 to Aurora PostgreSQL-Compatible version 10.18 or higher. For details, see [Sources for Data Migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) and [Targets for Data Migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html) in the AWS DMS documentation.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format that's compatible with the target database. Any objects that are not automatically converted are clearly marked so that they can be manually converted to complete the migration. AWS SCT can also scan the application source code for embedded SQL statements and convert them.

## Epics
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Aurora PostgreSQL-Compatible DB instance. | To create the DB instance, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html). For engine type, choose **Amazon Aurora**. For edition, choose **Amazon Aurora PostgreSQL-Compatible Edition**.<br />The Aurora PostgreSQL-Compatible version 10.18 or later DB instance should be in the same virtual private cloud (VPC) as the source IBM Db2 database. | Amazon RDS |

### Convert your database schema
<a name="convert-your-database-schema"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install and verify AWS SCT. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html) | AWS administrator, DBA, Migration engineer |
| Start AWS SCT and create a project. | To start the AWS SCT tool and create a new project to run a database migration assessment report, follow the instructions in the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.Launching). | Migration engineer |
| Add database servers and create a mapping rule. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html) | Migration engineer |
| Create a database migration assessment report.  | Create the database migration assessment report by following the steps in the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.AssessmentReport). | Migration engineer |
| View the assessment report. | Use the **Summary** tab of the database migration assessment report to view the report and analyze the data. This analysis will help you determine the complexity of the migration. For more information, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.View.html). | Migration engineer |
| Convert the schema. | To convert your source database schemas:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html)<br />For more information, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.Converting). | Migration engineer |
| Apply the converted database schema to the target DB instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html)For more information, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.ApplyingConversion). | Migration engineer |

### Migrate your data
<a name="migrate-your-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a VPC and DB parameter groups.  | Set up a VPC and DB parameter groups, and configure the inbound rules and parameters required for migration. For instructions, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Prerequisites.html).<br />For the VPC security group, select both the EC2 instance for Db2 and the Aurora PostgreSQL-Compatible DB instance. This replication instance must be in the same VPC as the source and target DB instances. | Migration engineer |
| Prepare source and target DB instances. | Prepare the source and target DB instances for migration. In a production environment, the source database will already exist.<br />For the source database, the server name must be the public Domain Name System (DNS) of the EC2 instance where Db2 is running. For user name, you can use `db2inst1` followed by the port, which will be 5000 for IBM Db2.  | Migration engineer |
| Create an Amazon EC2 client and endpoints. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html) | Migration engineer |
| Create a replication instance. | Create a replication instance by using the AWS DMS console and specify the source and target endpoints. The replication instance performs the data migration between the endpoints. For more information, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html).  | Migration engineer |
| Create an AWS DMS task to migrate the data. | Create a task to load the source IBM Db2 tables to the target PostgreSQL DB instance by following the steps in the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html#CHAP_GettingStarted.Replication.Tasks).[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct.html) | Migration engineer |

## Related resources
<a name="migrate-from-ibm-db2-on-amazon-ec2-to-aurora-postgresql-compatible-using-aws-dms-and-aws-sct-resources"></a>

**References**
+ [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
+ [PostgreSQL foreign data wrapper (FDW) documentation](https://www.postgresql.org/docs/10/postgres-fdw.html)
+ [PostgreSQL IMPORT FOREIGN SCHEMA documentation ](https://www.postgresql.org/docs/10/sql-importforeignschema.html)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/index.html)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/) (walkthrough)
+ [Introduction to Amazon EC2 - Elastic Cloud Server & Hosting with AWS](https://www.youtube.com/watch?v=TsRBftzZsQo) (video)
