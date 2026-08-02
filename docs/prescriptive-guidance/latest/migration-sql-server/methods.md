---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/methods.html
---

# SQL Server database migration methods
<a name="methods"></a>

There are various methods to migrate your SQL Server databases to AWS. You can choose from AWS services and SQL Server native features based on your assessment and requirements. This section describes some of the most common methods, which are summarized in the following two tables. Detailed discussions of some of these methods are included in the sections on Amazon EC2 and Amazon RDS later in this guide.

## AWS services
<a name="methods-services"></a>

|
|
| **Migration method** | **Target ** | **Features and limitations** | **More information** |
| --- |--- |--- |--- |
| AWS DMS | Amazon EC2 Amazon RDS Amazon Aurora Amazon RDS Custom | Supports full load and CDCSupports all database sizes | [AWS DMS section](heterogeneous-migration-tools.md#aws-sct) |
| AWS Migration Hub Orchestrator | Amazon EC2 Amazon RDS | Provides predefined, step-by-step workflow templatesAutomates native backup and restoreSupports all SQL Server editions and versionsCan be applied to one or many databases at one timeSupports all database sizes | [AWS Migration Hub Orchestrator section](mho.md) |
| AWS Transform MGN | Amazon EC2 | Highly automated lift-and-shift solutionAgent-based, block-level replication | Not covered in this guide (see [MGN documentation](https://docs.aws.amazon.com/mgn/index.html)) |
| AWS Snowball Edge | Amazon EC2 Amazon RDS Amazon RDS Custom | Supports very large databases (up to 210 TB)Uses Amazon Simple Storage Service (Amazon S3) for storing and restoring data | [AWS Snowball Edge section](snowball-edge.md) |

## SQL Server native methods
<a name="methods-sql-server"></a>

|
|
| **Migration method** | **Target ** | **Features and limitations** | **More information** |
| --- |--- |--- |--- |
| **Native backup and restore** | Amazon EC2 Amazon RDS Amazon RDS Custom | Can be applied to one or many databases at one timeRequires downtimeSupports all database sizes | [Native SQL Server backup/restore](native-backup-restore.md) section (you can use [AWS Migration Hub Orchestrator](mho.md) to automate native backup and restore) |
| **Log shipping ** | Amazon EC2 Amazon RDS Amazon RDS Custom | Applied per databaseCan be delayed | [Log shipping section](log-shipping.md) |
| **Database mirroring** | Amazon EC2 | Applied per databaseCan be synchronous or asynchronous, based on the SQL Server editionSecondary database isn't readable; it acts as a standbySupports both automatic and manual failover | [Database mirroring section](db-mirroring.md) |
| **Always On availability groups** | Amazon EC2 Amazon RDS Custom | Applied to a set of user databasesCan be synchronous or asynchronousSecondary database is readable (SQL Server Enterprise edition only)Supports both automatic and manual failoverFailover can be initiated for multiple databases at a time, at the database group level | [Always On availability groups section](always-on.md) |
| **Basic Always On availability groups** | Amazon EC2 Amazon RDS Custom | Supported in SQL Server Standard editionApplied to a single user database per availability groupCan be synchronous or asynchronousSupports both automatic and manual failoverFailover can be initiated at the availability group levelCan be used as a hybrid environment between on premises and AWS | Not covered in this guide (see [Basic Always On availiability groups for a single database](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/basic-availability-groups-always-on-availability-groups) in the Microsoft documentation) |
| **Distributed availability groups** | Amazon EC2 Amazon RDS Custom | Can be used for multi-Region SQL Server deploymentsCan fail over to a later version of SQL ServerDoesn't require Windows Server Failover Clustering (WSFC) to be extended to the target AWS environmentCan be used between Windows-based (source) and Linux-based (target) SQL Server databasesCan be used as a hybrid SQL Server deployment between on premises and AWS | [Distributed availability groups section](distributed-groups.md) |
| **Transactional replication** | Amazon EC2 Amazon RDS Amazon RDS Custom | Supports migration of a set of objects (tables, view, stored procedures)Supports asynchronous replication with near real-time dataSubscriber database is readableRequires close monitoring of SQL Server replication jobs that perform the replication | [Transaction replication section](trans-rep.md) |
| **Bulk copy program (bcp)** | Amazon EC2 Amazon RDS Custom | Supports small databasesRequires downtimeSchema is pre-created at the destinationUsed for moving data, but not metadata | Not covered in this guide (see [Importing and exporting SQL Server data using other methods](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Snapshots.html), *Bulk copy* section in the Amazon RDS documentation) |
| **Detach and attach** | Amazon EC2 Amazon RDS Custom | No backup neededRequires downtimeInvolves stopping, detaching, copying files, and attaching to Amazon EC2 console | Not covered in this guide (see [Database Detach and Attach](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-detach-and-attach-sql-server) in the Microsoft documentation) |
| **Import/export** | Amazon EC2 Amazon RDS Custom | Supports small databasesRequires downtimeSchema is pre-created at the destinationUsed for moving data, but not metadata | Not covered in this guide (see [SQL Server Import and Export Wizard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Snapshots.html#SQLServer.Procedural.Exporting.SSIEW) in the Amazon RDS documentation) |
