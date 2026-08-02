---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html
---

# Migrate an on-premises PostgreSQL database to Aurora PostgreSQL
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql"></a>

*Baji Shaik and Jitender Kumar, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-summary"></a>

Amazon Aurora PostgreSQL-Compatible Edition combines the performance and availability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. Aurora provides these benefits by scaling storage across three Availability Zones in the same AWS Region, and supports up to 15 read replica instances for scaling out read workloads and providing high availability within a single Region. By using an Aurora global database, you can replicate PostgreSQL databases in up to five Regions for remote read access and disaster recovery in the event of a Region failure. This pattern describes the steps for migrating an on-premises PostgreSQL source database to an Aurora PostgreSQL-Compatible database. The pattern includes two migration options: using AWS Data Migration Service (AWS DMS) or using native PostgreSQL tools (such as [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html), [pg\_restore](https://www.postgresql.org/docs/current/app-pgrestore.html), and [psql](https://www.postgresql.org/docs/current/app-psql.html)) or third-party tools.

The steps described in this pattern also apply to target PostgreSQL databases on Amazon Relational Database Service (Amazon RDS) and Amazon Elastic Compute Cloud (Amazon EC2) instances.

## Prerequisites and limitations
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A PostgreSQL source database in an on-premises data center
+ [An Aurora PostgreSQL-Compatible DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html) or an [Amazon RDS for PostgreSQL DB instance](https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/)

**Limitations**
+ Database size limits are 64 TB for Amazon RDS for PostgreSQL and 128 TB for Aurora PostgreSQL-Compatible.
+ If you’re using the AWS DMS migration option, review [AWS DMS limitations on using a PostgreSQL database as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.Limitations).

**Product versions**
+ For PostgreSQL major and minor version support in Amazon RDS, see [Amazon RDS for PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html) in the Amazon RDS documentation.
+ For PostgreSQL support in Aurora, see [Amazon Aurora PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html) in the Aurora documentation.
+ If you’re using the AWS DMS migration option, see[ supported PostgreSQL versions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html) in the AWS DMS documentation.

## Architecture
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-architecture"></a>

**Source technology stack**
+ On-premises PostgreSQL database

**Target technology stack**
+ Aurora PostgreSQL-Compatible DB instance

**Source architecture**

![Source architecture for on-premises PostgreSQL database](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82114165-8102-44a2-8b12-485ac9eb8989/images/a8621ad3-781b-45a9-86a8-d0b0ec5c79ea.png)

**Target architecture**

![Target architecture for PostgreSQL database on Amazon Aurora](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82114165-8102-44a2-8b12-485ac9eb8989/images/fc2ec0cb-7b9b-4cc0-b70c-40e47c2f4c45.png)

**Data migration architecture**

*Using AWS DMS*

![Migrating an on-premises PostgreSQL database to Aurora by using AWS DMS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82114165-8102-44a2-8b12-485ac9eb8989/images/5336adb4-e9eb-47d0-a5b5-d149261b1638.png)

*Using native PostgreSQL tools*

![Migrating an on-premises PostgreSQL database to Aurora by using pg_dump and pg_restore](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82114165-8102-44a2-8b12-485ac9eb8989/images/3c6fb533-45ff-443e-bfb1-97e60cbdd583.png)

## Tools
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises configurations. This service supports different sources and target databases. For information about how to validate the PostgreSQL source and target database versions and editions supported for use with AWS DMS, see [Using a PostgreSQL database as an AWS DMS source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.
+ Native PostgreSQL tools include  [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html), [pg\_restore](https://www.postgresql.org/docs/current/app-pgrestore.html), and [psql](https://www.postgresql.org/docs/current/app-psql.html).

## Epics
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-epics"></a>

### Analyze the migration
<a name="analyze-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions. | If you are using AWS DMS, make sure that you’re using a [supported version of PostgreSQL](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html).  | DBA |
| Identify the storage type and capacity requirements. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA, Systems administrator |
| Choose the proper instance type, capacity, storage features, and network features. | Determine the compute requirements of the target database instance. Review known performance issues that might need additional attention. Consider the following factors to determine the appropriate instance type:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html)<br />For more information, see [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the Aurora documentation. | DBA, Systems administrator |
| Identify the network access security requirements for the source and target databases. | Determine the appropriate security groups that would enable the application to talk to the database. | DBA, Systems administrator |
| Identify the application migration strategy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA, App owner, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | Create a new virtual private cloud (VPC) for the target database instance. | Systems administrator |
| Create security groups. | Create a security group within the VPC (as determined in the previous epic) to allow inbound connections to the database instance.  | Systems administrator |
| Configure and start the Aurora DB cluster. | Create the target database instance with the new VPC and security group and start the instance. | Systems administrator |

### Migrate data ‒ option 1 (using AWS DMS)
<a name="migrate-data-option-1-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Complete pre-migration steps. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA |
| Complete migration steps. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA |
| Validate data. | To ensure that your data was migrated accurately from the source to the target, follow the [data validation steps](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html) in the AWS DMS documentation. | DBA |

### Migrate data ‒ option 2 (using pg\_dump and pg\_restore)
<a name="migrate-data-option-2-using-pg_dump-and-pg_restore"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the source database. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html)For more information, see the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) documentation and the [walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-pd_dump.html) in the AWS DMS documentation. | DBA |
| Prepare the target database. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html)For more information, see the [pg\_restore](https://www.postgresql.org/docs/current/app-pgrestore.html) documentation and the [walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-pd_dump.html) in the AWS DMS documentation. | DBA |
| Validate data. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. | Implement the application migration strategy that you created in the first epic. | DBA, App owner, Systems administrator |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients over to the new infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA, App owner, Systems administrator |
| If you need to roll back the migration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html) | DBA, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down resources. | Shut down the temporary AWS resources. | DBA, Systems administrator |
| Validate documents. | Review and validate the project documents. | DBA, App owner, Systems administrator |
| Gather metrics. | Gather metrics around time to migrate, percent of manual versus tool cost savings, and so on. | DBA, App owner, Systems administrator |
| Close the project. | Close the project and provide any feedback. | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-postgresql-database-to-aurora-postgresql-resources"></a>

**References**
+ [AWS Data Migration Service](https://aws.amazon.com/dms/)
+ [VPCs and Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.html)
+ [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/)
+ [Using a PostgreSQL database as an AWS DMS source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html)
+ [How to create an AWS DMS replication instance](https://aws.amazon.com/premiumsupport/knowledge-center/create-aws-dms-replication-instance/)
+ [How to create source and target endpoints using AWS DMS](https://aws.amazon.com/premiumsupport/knowledge-center/create-source-target-endpoints-aws-dms/)

**Additional resources**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Data migration step-by-step walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html)
+ [Amazon Aurora resources](https://aws.amazon.com/rds/aurora/getting-started/)
