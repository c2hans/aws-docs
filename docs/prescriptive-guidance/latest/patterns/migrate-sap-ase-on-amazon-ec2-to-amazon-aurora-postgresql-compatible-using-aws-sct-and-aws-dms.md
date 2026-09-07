---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms.html
---

# Migrate SAP ASE on Amazon EC2 to Amazon Aurora PostgreSQL-Compatible using AWS SCT and AWS DMS
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms"></a>

*Amit Kumar and Ankit Gupta, Amazon Web Services*

## Summary
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-summary"></a>

This pattern describes how to migrate an SAP Adaptive Server Enterprise (SAP ASE) database that is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance to Amazon Aurora PostgreSQL-Compatible Edition by using AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS). The pattern focuses on both data definition language (DDL) conversions for stored objects and data migration.

Aurora PostgreSQL-Compatible supports online transaction processing (OLTP) workloads. This managed service provides configurations that automatically scale on demand. It can automatically start up, shut down, scale up, or scale down your database based on your application's needs. You can run your database in the cloud without managing any database instances. Aurora PostgreSQL-Compatible provides a cost-effective option for infrequent, intermittent, or unpredictable workloads.

The migration process consists of two main phases:
+ Converting the database schema by using AWS SCT
+ Migrating the data by using AWS DMS

Detailed instructions for both phases are provided in the *Epics* section. For information about troubleshooting issues that are specific to using AWS DMS with SAP ASE databases, see [Troubleshooting issues with SAP ASE](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.SAP) in the AWS DMS documentation.

## Prerequisites and limitations
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source SAP ASE database on an EC2 instance with server, database, and listener services up and running
+ A target Aurora PostgreSQL-Compatible database

**Limitations**
+ The port number for connections must be 5432.
+ The [huge\_pages](https://www.postgresql.org/docs/9.6/static/runtime-config-resource.html) feature is on by default but can be modified.
+ Point-in-time recovery (PITR) granularity is 5 minutes.
+ Cross-Region replication is currently not available.
+ The maximum storage size for an Aurora database is 128 TiB.
+ You can create up to 15 read replicas.
+ The table size limit is constrained only by the size of the Aurora cluster volume, so the maximum table size for an Aurora PostgreSQL-Compatible DB cluster is 32 TiB. We recommend that you follow best practices for table design, such as partitioning large tables.

**Product versions**
+ Source database: AWS DMS currently supports SAP ASE 15, 15.5, 15.7, and 16.x. See the [AWS DMS User Guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html) for the latest information about SAP ASE version support.
+ Target database: PostgreSQL 9.4 and later (for version 9.x), 10.x, 11.x, 12.x, 13.x, and 14.x. See the [AWS DMS User Guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html) for the latest supported PostgreSQL versions.
+ Amazon Aurora 1.x or later. For the latest information, see [Aurora PostgreSQL-Compatible releases and engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html) in the Aurora documentation.

## Architecture
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-architecture"></a>

**Source technology stack  **
+ SAP ASE database running on Amazon EC2

**Target technology stack  **
+ Aurora PostgreSQL-Compatible database

**Migration architecture **

![Migrating an SAP ASE database to Aurora PostgreSQL-Compatible by using AWS SCT and AWS DMS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/07fbdea1-0242-40ae-8e5f-2ce4a620a047/images/a3b018f3-2e7b-4c37-a218-870c56132acb.png)

## Tools
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-tools"></a>
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and most of the custom code to a format that’s compatible with the target database.
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) supports several different source and target databases. For more information, see [Sources for Data Migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) and [Targets for Data Migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html) in the AWS DMS documentation. For the most comprehensive version and feature support, we recommend that you use the latest version of AWS DMS.

## Epics
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure network access in the source EC2 instance. | Set up security groups in the EC2 instance that hosts your source SAP ASE database.<br />For instructions, see [Amazon EC2 security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html?icmpid=docs_ec2_console) in the Amazon EC2 documentation. | Systems administrator |
| Create your target Aurora PostgreSQL-Compatible DB cluster. | Install, configure, and launch an Aurora PostgreSQL-Compatible cluster for your target database.<br />For more information, see [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the Aurora documentation. | DBA |
| Set up authorization for the target DB cluster. | Set up security groups and firewalls for the target database.<br />For instructions, see [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the Aurora documentation. | DBA, Systems administrator |

### Convert your database schema with AWS SCT
<a name="convert-your-database-schema-with-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch AWS SCT. | Launch AWS SCT by following the instructions in the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html).<br />AWS SCT provides a project-based user interface to automatically convert the database schema of your SAP ASE source database into a format that’s compatible with your target Aurora PostgreSQL-Compatible DB instance. | DBA |
| Create AWS SCT endpoints. | Create endpoints for the source SAP ASE and target PostgreSQL databases.<br />For instructions, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.AddServers). | DBA |
| Create an assessment report. | Create a database migration assessment report to evaluate the migration and detect any incompatible objects and functions.<br />For instructions, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.AssessmentReport). | DBA |
| Convert the schema. | Convert the database schema by following the instructions in the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.html). | DBA |
| Validate database objects. | If AWS SCT cannot convert a database object, it will identify its name and other details. You must convert these objects manually.<br />To identify these mismatches, follow the instructions in the AWS blog post [Validate database objects after migrating from SAP ASE to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/validate-database-objects-after-migrating-from-sap-ase-to-amazon-rds-for-postgresql-or-amazon-aurora-postgresql/). | DBA |

### Analyze the AWS DMS migration
<a name="analyze-the-aws-dms-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions. | Check the SAP ASE database versions for compatibility with AWS DMS. <br />For more information, see [Sources for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html#CHAP_Introduction.Sources.title) and [Targets for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html) in the AWS DMS documentation. | DBA |
| Identify the requirements for the storage type and capacity. | Choose the appropriate storage capacity for the target database based on the size of your source database. | DBA, Systems administrator |
| Choose the instance type, capacity, and other features of the replication instance. | Choose the instance type, capacity, storage features, and network features that meet your requirements.<br />For guidance, see [Choosing the right AWS DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html) in the AWS DMS documentation. | DBA, Systems administrator |
| Identify network access security requirements. | Identify the network access security requirements for the source and target databases.<br />Follow the guidance in [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the AWS DMS documentation. | DBA, Systems administrator |

### Migrate the data
<a name="migrate-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the data by creating a migration task in AWS DMS. | To migrate data, create a task and follow the instructions in the [AWS DMS documentation.](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html) <br />We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support. | DBA |
| Validate the data. | To validate that your data was migrated accurately from the source database to the target database, follow the [data validation guidelines](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html) provided in the AWS DMS documentation. | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the application migration strategy. | Choose one of the [seven strategies (7Rs)](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/planning-phase.html) for migrating applications to the cloud. | DBA, App owner, Systems administrator |
| Follow the application migration strategy. | Complete the database tasks identified by the application team, including updating DNS connection details for the target database and updating dynamic queries.  | DBA, App owner, Systems administrator |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients over to the new infrastructure. | Switch the connection from the source database to the target database. <br />For more information, see the [Cut over](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/cut-over.html) section of the *Migration strategy for relational databases*. | DBA, App owner, Systems administrator |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the temporary AWS resources. | Terminate all migration tasks, replication instances, endpoints, and other AWS SCT and AWS DMS resources. <br />For more information, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html#CHAP_GettingStarted.Replication.Deleting). | DBA, Systems administrator |
| Review and validate the project documents. | Validate all the steps in the project documentation to ensure that all tasks have been completed successfully. | DBA, App owner, Systems administrator |
| Close the project. | Close the migration project and provide any feedback. | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-sap-ase-on-amazon-ec2-to-amazon-aurora-postgresql-compatible-using-aws-sct-and-aws-dms-resources"></a>

**References**
+ [Enable encrypted connections for PostgreSQL DB instances in Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html) (AWS Prescriptive Guidance)
+ [Transport PostgreSQL databases between two Amazon RDS DB instances using pg\_transport](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg_transport.html) (AWS Prescriptive Guidance)
+ [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/)
+ [Best practices with Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.BestPractices.html) (Amazon Aurora documentation)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [Using an SAP ASE Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html)

**Tutorials and videos**
+ [Getting Started with AWS Database Migration Service](https://aws.amazon.com/dms/getting-started/)
+ [AWS Database Migration Service](https://www.youtube.com/watch?v=zb4GcjEdl8U) (video)
