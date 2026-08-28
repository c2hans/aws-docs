---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump.html
---

# Migrate an on-premises Oracle database to Amazon EC2 by using Oracle Data Pump
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump"></a>

*Navakanth Talluri, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-summary"></a>

When migrating databases, you must consider factors such as the source and target database engines and versions, migration tools and services, and acceptable downtime periods. If you’re migrating an on-premises Oracle database to Amazon Elastic Compute Cloud (Amazon EC2), you can use Oracle tools, such as Oracle Data Pump and Oracle Recovery Manager (RMAN). For more information about strategies, see [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html).

Oracle Data Pump helps you extract the logical, consistent backup of the database and restore it to the target EC2 instance. This pattern describes how to migrate an on-premises Oracle database to an EC2 instance by using Oracle Data Pump and the `NETWORK_LINK` parameter, with minimal downtime. The `NETWORK_LINK` parameter starts an import through a database link. The Oracle Data Pump Import (impdp) client on the target EC2 instance connects to the source database, retrieves data from it, and writes the data directly to the database on the target instance. There are no backup, or *dump*, files used in this solution.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An on-premises Oracle database that:
  + Isn’t an Oracle Real Application Clusters (RAC) database
  + Isn’t an Oracle Automatic Storage Management (Oracle ASM) database
  + Is in read-write mode.
+ You have created an AWS Direct Connect link between your on-premises data center and AWS. For more information, see [Create a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html) (Direct Connect documentation).

**Product versions**
+ Oracle Database 10g release 1 (10.1) and later

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-architecture"></a>

**Source technology stack**
+ A standalone (non-RAC and non-ASM) Oracle database server in an on-premises data center

**Target technology stack**
+ An Oracle database running on Amazon EC2

**Target architecture**

The [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) of the AWS Well-Architected Framework recommends creating data backups to help provide high availability and resiliency. For more information, see [Architecting for high availability](https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html#amazon-ec2) in *Best Practices for Running Oracle Database on AWS*. This pattern sets up primary and standby databases on EC2 instances by using Oracle Active Data Guard. For high availability, the EC2 instances should be in different Availability Zones. However, the Availability Zones can be in the same AWS Region or in different AWS Regions.

Active Data Guard provides read-only access to a physical standby database and applies redo changes continuously from the primary database. Based on your recovery point objective (RPO) and recovery time objective (RTO), you can choose between synchronous and asynchronous redo transport options.

The following image shows the target architecture if the primary and standby EC2 instances are in different AWS Regions.

![Application connecting to the new database on the primary EC2 instance](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bdd49395-2f99-43e2-ad1d-a1d09d90fb58/images/37fcd4dc-5516-416b-a280-0c5f002880de.png)

**Data migration architecture**

After you have finished setting up the target architecture, you use Oracle Data Pump to migrate the on-premises data and schemas to the primary EC2 instance. During cutover, applications can’t access the on-premises database or the target database. You shut down these applications until they can be connected to the new target database on the primary EC2 instance.

The following image shows the architecture during the data migration. In this sample architecture, the primary and standby EC2 instances are in different AWS Regions.

![The source DB connects to the target DB. Applications are disconnected from source and target DBs](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bdd49395-2f99-43e2-ad1d-a1d09d90fb58/images/c58b669b-b11f-4d78-8911-c07b81b7c6a0.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-tools"></a>

**AWS services**
+ [AWS Direct Connect](https://aws.amazon.com/directconnect/) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.

**Other tools and services**
+ [Oracle Active Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/introduction-to-oracle-data-guard-concepts.html#GUID-5E73667D-4A56-445E-911F-1E99092DD8D7) helps you create, maintain, manage, and monitor standby databases.
+ [Oracle Data Pump](https://www.oracle.com/technetwork/documentation/data-pump-overview-084963.html) helps you move data and metadata from one database to another at high speeds.

## Best practices
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-best-practices"></a>
+ [Best Practices for Running Oracle Database on AWS](https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-security-and-performance.html)
+ [Importing data using NETWORK\_LINK](https://docs.oracle.com/database/121/SUTIL/GUID-23E58D59-A477-4A87-BD0E-C82447581D0A.htm#SUTIL856)

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-epics"></a>

### Set up the EC2 instances on AWS
<a name="set-up-the-ec2-instances-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the source hardware configuration for the on-premises host and the kernel parameters. | Validate the on-premises configuration, including storage size, input/output operations per second (IOPS), and CPU. This is important for Oracle licensing, which is based on CPU cores. | DBA, SysAdmin |
| Create the infrastructure on AWS. | Create the virtual private clouds (VPCs), private subnets, security groups, network access control lists (ACLs), route tables, and internet gateway. For more information, see the following:+ [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)<br />+ [Tutorial: Create a VPC for use with a database instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html) | DBA, AWS systems administrator |
| Set up the EC2 instances by using Active Data Guard. | Configure AWS EC2 instances by using an Active Data Guard configuration, as described in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). The version of Oracle Database on the EC2 instance can be different from the on-premises version because this pattern uses logical backups. Note the following:+ Put the target database in read-write mode.<br />+ On the target database, provide the Transparent Network Substrate (TNS) detail for the source database.<br />For more information, see:+ [Starting Up a Database](https://docs.oracle.com/cd/B28359_01/server.111/b28310/start001.htm#ADMIN10063) (Oracle documentation)<br />+ [Creating and Configuring an Oracle Database](https://docs.oracle.com/cd/B28359_01/server.111/b28310/create.htm#i1017640) (Oracle documentation) | DBA, AWS systems administrator |

### Migrate the database to Amazon EC2
<a name="migrate-the-database-to-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a dblink to the on-premises database from the EC2 instance. | Create a database link (dblink) between the Oracle database on the EC2 instance and the on-premises Oracle database. For more information, see [Using Network Link Import to Move Data](https://docs.oracle.com/database/121/SUTIL/GUID-3E1D4B46-E856-4ABE-ACC5-977A898BB0F1.htm#SUTIL806) (Oracle documentation). | DBA |
| Verify the connection between the EC2 instance and the on-premises host. | Use the dblink to confirm that the connection between the EC2 instance and the on-premises database is functioning. For instructions, see [CREATE DATABASE LINK](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_5005.htm) (Oracle documentation). | DBA |
| Stop all applications connected to the on-premises database. | After the database downtime is approved, shut down any applications and dependent jobs that connent to your on-premises database. You can do this either from the application directly or from the database by using cron. For more information, see [Use the Crontab Utility to Schedule Tasks on Oracle Linux](https://docs.oracle.com/en/learn/oracle-linux-crontab/index.html). | DBA, App developer |
| Schedule the data migration job.  | On the target host, use the command `impdb` to schedule the Data Pump import. This connects the target database to the on-premises host and starts the data migration. For more information, see [Data Pump Import](https://docs.oracle.com/database/121/SUTIL/GUID-D11E340E-14C6-43B8-AB09-6335F0C1F71B.htm#SUTIL300) and [NETWORK\_LINK](https://docs.oracle.com/database/121/SUTIL/GUID-0871E56B-07EB-43B3-91DA-D1F457CF6182.htm#SUTIL919) (Oracle documentation). | DBA |
| Validate the data migration. | Data validation is a crucial step. For data validation, you can use custom tools or Oracle tools, such as a combination of dblink and SQL queries. | DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Put the source database in read-only mode. | Confirm that the application is shut down and no changes are being made to the source database. Open the source database in read-only mode. This helps you avoid any open transactions. For more information, see `ALTER DATABASE` in [SQL Statements](https://docs.oracle.com/database/121/SQLRF/statements_1006.htm#i2135540) (Oracle documentation). | DBA, DevOps engineer, App developer |
| Validate the object count and data. | To validate the data and object, use custom tools or Oracle tools, such as a combination of dblink and SQL queries. | DBA, App developer |
| Connect the applications to the database on the primary EC2 instance. | Change the application’s connection attribute to point to the new database you created on the primary EC2 instance. | DBA, App developer |
| Validate the application performance. | Start the application. Validate the functionality and performance of the application by using [Automated Workload Repository](https://docs.oracle.com/database/121/RACAD/GUID-C3CD2DCE-38BD-46BA-BC32-7A28CAC9A7FD.htm#RACAD951) (Oracle documentation). | App developer, DevOps engineer, DBA |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-ec2-by-using-oracle-data-pump-resources"></a>

**AWS references**
+ [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html)
+ [Amazon EC2 for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/ec2-oracle.html)
+ [Migrating bulky Oracle databases to AWS for cross-platform environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/welcome.html)
+ [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
+ [Tutorial: Create a VPC for use with a database instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html)

**Oracle references**
+ [Oracle Data Guard Configurations](https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/introduction-to-oracle-data-guard-concepts.html#GUID-AB9DF863-2C7E-4767-81F2-56AD0FA30B49)
+ [Data Pump Import](https://docs.oracle.com/database/121/SUTIL/GUID-D11E340E-14C6-43B8-AB09-6335F0C1F71B.htm#SUTIL300)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
