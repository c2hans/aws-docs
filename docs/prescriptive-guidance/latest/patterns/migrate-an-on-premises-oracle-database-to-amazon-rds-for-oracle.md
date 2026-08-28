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
| Create project documents and record database details. | 1. Document your migration goals, migration requirements, key project stakeholders, project milestones, project deadlines, key metrics, migration risks, and risk mitigation plans.<br />2. Document critical information about your source database, including RAM, IOPS, and CPUs. You will later use this information to determine the appropriate target DB instance.<br />3. Validate the versions of your source and target databases. | DBA |
| Identify storage requirements. | Identify and document your storage requirements, including the following:1. Calculate the storage allocated for the source DB instance.<br />2. Gather the historical growth metrics from the source DB instance.<br />3. Forecast future growth for the target DB instance.For [General Purpose (gp2) SSD volumes](https://aws.amazon.com/ebs/volume-types/), you get three IOPS per 1 GB of storage. Allocate storage by calculating the total number of read and write IOPS on the source database. | DBA, SysAdmin |
| Choose the proper instance type based on compute requirements. | 1. Determine the compute requirements of the target DB instance.<br />2. Identify performance issues.<br />3. Consider the factors for determining the appropriate instance type:CPU utilization of the source DB instanceIOPS (read and write) for the source DB instanceMemory footprint on the source DB instance | SysAdmin |
| Identify network access security requirements. | 1. Identify and document the network access security requirements for your source and target databases.<br />2. Configure the appropriate security groups for enabling the application to communicate with the database. | DBA, SysAdmin |
| Identify the application migration strategy. | 1. Determine and document the migration cutover strategy.<br />2. Determine and document your application’s recovery time objective (RTO) and recovery point objective (RPO), and then plan for the cutover accordingly. | DBA, SysAdmin, App owner |
| Identify migration risks. | Assess the database and document migration specific risks and mitigations. For example:+ Identify no-logging tables and highlight the risk of data loss in the event of recovery.<br />+ Extract the source database users and privileges, and highlight the conflicts with Amazon RDS privileges.<br />+ Review the alert log for any Oracle-specific errors and warnings.<br />+ Identify the supported and unsupported features of the target DB instance.<br />+ Review the deprecated features of the target DB version engine. | DBA |

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
| Prepare the source database. | 1. [Create a Data Pump directory](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html#GUID-EEB32B50-8A00-40B0-8787-CC2C8BA05DC5) or use an existing one.<br />2. Create a migration user and [grant permissions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html#GUID-EEB32B50-8A00-40B0-8787-CC2C8BA05DC5) to perform the Data Pump extract.<br />3. Extract roles, users, and tablespaces from the source database as a SQL script.<br />4. Transfer the extracted Data Pump dump to the target DB instance `data pump` directory. | DBA, SysAdmin |
| Prepare the target database. | 1. Confirm that all the database options (for example, text and Java) are installed or enabled on the target Amazon RDS for Oracle DB instance.<br />2. Create a Data Pump directory or use an existing one.<br />3. Create a migration user and grant permissions to perform the Data Pump import.<br />4. Create the required tablespaces, users, and roles on the target DB instance.<br />5. Import the transferred Data Pump export dump to the target database.<br />6. Create any indexes excluded during import or object creation.<br />7. Create any constraints excluded during import.<br />8. Validate or recompile invalid objects.<br />9. Rebuild the invalid indexes.<br />10. Validate the database object counts between the source and the target databases.<br />11. Resolve any discrepancies found between object counts. | DBA, SysAdmin |

### Option 2 - Use AWS DMS to migrate data
<a name="option-2---use-aws-dms-to-migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the data. | 1. Clean the data in the source database.<br />2. [Create a replication instance](https://aws.amazon.com/premiumsupport/knowledge-center/create-aws-dms-replication-instance/).<br />3. [Create a source endpoint and target endpoint](https://aws.amazon.com/premiumsupport/knowledge-center/create-source-target-endpoints-aws-dms/).<br />4. Identify the number of tables and objects to be migrated. | DBA |
| Migrate the data. | 1. Drop foreign key constraints and triggers on the target database.<br />2. Drop secondary indexes on the target database.<br />3. [Configure AWS DMS full-load task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.html) from the source database to the target database.<br />4. Enable foreign keys.<br />5. [Enable AWS DMS CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) to replicate ongoing changes.<br />6. Enable triggers.<br />7. Update the sequences.<br />8. Validate the source and target data. | DBA |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients to the new infrastructure. | 1. Stop all application services and client connections pointing to Oracle.<br />2. Run the AWS DMS tasks.<br />3. Set up a rollback task (for example, reverse CDC from the Amazon RDS database to the on-premises Oracle database).<br />4. Validate the data.<br />5. Start the application services on the new target database by configuring Amazon Route 53 to the new Amazon RDS for Oracle DB instance.<br />6. Add Amazon CloudWatch monitoring to your new Amazon RDS for Oracle DB instance. | DBA, SysAdmin, App owner |
| Implement your rollback plan. | 1. Stop all application services pointing to the Amazon RDS for Oracle DB instance.<br />2. Roll back the changes to the source on-premises Oracle database by using an AWS DMS task.<br />3. Stop the AWS DMS tasks running from the on-premises Oracle database to the Amazon RDS for Oracle database.<br />4. Configure the applications back on the source Oracle database.<br />5. Confirm the rollback deployment is complete. | DBA, App owner |

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
