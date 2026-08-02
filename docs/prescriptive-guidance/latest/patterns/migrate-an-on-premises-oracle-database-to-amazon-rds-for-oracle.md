---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html
---

# Migrate an on-premises Oracle database to Amazon RDS for Oracle
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle"></a>

*Baji Shaik and Pavan Pusuluri, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-summary"></a>

This pattern describes the steps for migrating on-premises Oracle databases to Amazon Relational Database Service (Amazon RDS) for Oracle. As part of the migration process, you create a migration plan and consider important factors about your target database infrastructure based on your source database. You can choose one of two migration options based on your business requirements and use case:
+ AWS Database Migration Service (AWS DMS) – You can use AWS DMS to migrate databases to the AWS Cloud quickly and securely. Your source database remains fully operational during the migration, which minimizes downtime to applications that rely on the database. You can reduce migration time by using AWS DMS to create a task that captures ongoing changes after you complete an initial full-load migration through a process called [change data capture (CDC)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html).
+ Native Oracle tools – You can migrate databases by using native Oracle tools, such as Oracle and [Data Pump Export](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200) and [Data Pump Import](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_import.htm#SUTIL300) with [Oracle GoldenGate](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/introduction-oracle-goldengate.htm#GGCON-GUID-EF513E68-4237-4CB3-98B3-2E203A68CBD4) for CDC. You can also use native Oracle tools such as the original [Export utility](https://docs.oracle.com/cd/E11882_01/server.112/e22490/original_export.htm#SUTIL3634) and original [Import utility](https://docs.oracle.com/cd/E11882_01/server.112/e22490/original_import.htm#SUTIL001) to reduce the full-load time.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An on-premises Oracle database
+ An Amazon RDS Oracle database (DB) instance

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ Oracle versions 11g (versions 11.2.0.3.v1 and later) and up to 12.2 and 18c. For the latest list of supported versions and editions, see [Amazon RDS for Oracle ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)in the AWS documentation. For Oracle versions supported by AWS DMS, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) in the AWS DMS documentation.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-architecture"></a>

**Source technology stack**
+ On-premises Oracle databases

**Target technology stack**
+ Amazon RDS for Oracle

**Source and target architecture**

The following diagram shows how to migrate an on-premises Oracle database to Amazon RDS for Oracle by using AWS DMS.

![Workflow for migrating Oracle databases to Amazon RDS for Oracle by using AWS DMS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/25912997-0ac0-4303-9ce5-0621a7e12406/images/20f94a5c-1095-4182-b964-c379414c9a36.png)

The diagram shows the following workflow:

1. Create or use an existing database user, grant the required [AWS DMS permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed) to that user, turn on [ARCHIVELOG mode](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed.Configuration.ArchiveLogMode), and then set up [supplemental logging](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed.Configuration.SupplementalLogging).

1. Configure the internet gateway between the on-premises and AWS network.

1. Configure [source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) for AWS DMS.

1. Configure [AWS DMS replication tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) to migrate the data from the source database to the target database.

1. Complete the post-migration activities on the target database.

The following diagram shows how to migrate an on-premises Oracle database to Amazon RDS for Oracle by using native Oracle tools.

![Workflow for migrating Oracle databases to Amazon RDS for Oracle by using Oracle tools.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/25912997-0ac0-4303-9ce5-0621a7e12406/images/af8e0e1a-d4c8-4d99-9780-3e093ad9a257.png)

The diagram shows the following workflow:

1. Create or use an existing database user and grant the required permissions to back up the Oracle database by using Oracle Export (`exp`) and Import (`imp`) utilities.

1. Configure the internet gateway between the on-premises and AWS network.

1. Configure the Oracle client on the [Bastion](https://www.oracle.com/security/cloud-security/bastion/) host to take the backup database.

1. Upload the backup database to an Amazon Simple Storage Service (Amazon S3) bucket.

1. Restore the database backup from Amazon S3 to an Amazon RDS for Oracle database.

1. Configure Oracle GoldenGate for CDC.

1. Complete the post-migration activities on the target database.

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ Native Oracle tools help you perform a homogeneous migration. You can use [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) to migrate data between your source and target databases. This pattern uses Oracle Data Pump to perform the full load from the source database to the target database.
+ [Oracle GoldenGate](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/introduction-oracle-goldengate.htm#GGCON-GUID-EF513E68-4237-4CB3-98B3-2E203A68CBD4) helps you perform logical replication between two or more databases. This pattern uses GoldenGate to replicate the delta changes after the initial load by using Oracle Data Pump.

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create project documents and record database details. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA |
| Identify storage requirements. | Identify and document your storage requirements, including the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html)For [General Purpose (gp2) SSD volumes](https://aws.amazon.com/ebs/volume-types/), you get three IOPS per 1 GB of storage. Allocate storage by calculating the total number of read and write IOPS on the source database. | DBA, SysAdmin |
| Choose the proper instance type based on compute requirements. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | SysAdmin |
| Identify network access security requirements. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, SysAdmin |
| Identify the application migration strategy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, SysAdmin, App owner |
| Identify migration risks. | Assess the database and document migration specific risks and mitigations. For example:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | [Create a new Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html) for the target DB instance. | SysAdmin |
| Create security groups. | [Create a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#creating-security-group) in your new VPC to allow inbound connections to the DB instance. | SysAdmin |
| Create an Amazon RDS for Oracle DB instance. | [Create the target DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) with the new VPC and security group, and then start the instance. | SysAdmin |

### Option 1 - Use native Oracle or third-party tools to migrate data
<a name="option-1---use-native-oracle-or-third-party-tools-to-migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the source database. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, SysAdmin |
| Prepare the target database. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, SysAdmin |

### Option 2 - Use AWS DMS to migrate data
<a name="option-2---use-aws-dms-to-migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the data. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA |
| Migrate the data. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients to the new infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, SysAdmin, App owner |
| Implement your rollback plan. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) | DBA, App owner |

### Close out the migration project
<a name="close-out-the-migration-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | Shut down or remove the temporary AWS resources, such as the AWS DMS replication instance and S3 bucket. | DBA, SysAdmin |
| Review project documents. | Review your migration planning documents and goals, and then confirm that you completed all required migration steps. | DBA, SysAdmin, App owner |
| Gather metrics. | Record key migration metrics, including how long it took to complete the migration, the percentage of manual vs. tool-based tasks, cost savings, and other relevant metrics. | DBA, SysAdmin, App owner |
| Close out the project. | Close out the migration project and capture feedback about the effort. | DBA, SysAdmin, App owner |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-resources"></a>

**References**
+ [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html) (AWS Prescriptive Guidance)
+ [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS documentation)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/) (Amazon RDS documentation)

**Tutorials and videos**
+ [Getting Started with AWS Database Migration Service](https://aws.amazon.com/dms/getting-started/) (AWS DMS documentation)
+ [Amazon RDS resources](https://aws.amazon.com/rds/getting-started/) (Amazon RDS documentation)
+ [AWS Database Migration Service (DMS)](https://www.youtube.com/watch?v=zb4GcjEdl8U) (YouTube)
