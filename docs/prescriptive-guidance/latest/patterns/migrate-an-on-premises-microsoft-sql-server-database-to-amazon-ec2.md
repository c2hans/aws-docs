---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon EC2
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2"></a>

*Senthil Ramasamy, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-summary"></a>

This pattern describes how to migrate an on-premises Microsoft SQL Server database to Microsoft SQL Server on an Amazon Elastic Compute Cloud (Amazon EC2) instance. It covers two options for migration: using AWS Database Migration Service (AWS DMS) or using native Microsoft SQL Server tools such as backup and restore, Copy Database Wizard, or copy and attach database.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An operating system supported by Amazon EC2 (for a complete list of supported operating system versions, see [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/))
+ A Microsoft SQL Server source database in an on-premises data center

**Product versions**
+ For on-premises and Amazon EC2 instance databases, AWS DMS supports:
  + SQL Server versions 2005, 2008, 2008R2, 2012, 2014, 2016, 2017, and 2019
  + Enterprise, Standard, Workgroup, Developer, and Web editions
+ For the latest list of supported versions, see [Using a Microsoft SQL Server Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html).

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-architecture"></a>

**Source technology stack**
+ On-premises Microsoft SQL Server database

**Target technology stack**
+ Microsoft SQL Server database on an EC2 instance

**Target architecture**

![Primary and standby Microsoft SQL Server instances on EC2 instances in two Availability Zones.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f0a155b3-4977-4e1f-8332-89eab29c1e25/images/53e2c27d-ceb4-4d88-a022-93dd0b343eaf.png)

**Data migration architecture**
+ Using AWS DMS

![Migrating on-premises SQL Server data to an EC2 instance by using AWS DMS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f0a155b3-4977-4e1f-8332-89eab29c1e25/images/1cbe32ea-e285-4cac-9153-4428bad9b229.png)

+ Using native SQL Server tools

![Migrating on-premises SQL Server data to an EC2 instance by using native SQL Server tools.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f0a155b3-4977-4e1f-8332-89eab29c1e25/images/ad2caf54-7399-4038-91a3-acba9fa7da29.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/) helps you migrate your data to and from widely used commercial and open-source databases, including Oracle, SQL Server, MySQL, and PostgreSQL. You can use AWS DMS to migrate your data into the AWS Cloud, between on-premises instances (through an AWS Cloud setup), or between combinations of cloud and on-premises setups.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.
+ Native Microsoft SQL Server tools include backup and restore, Copy Database Wizard, and copy and attach database.

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions. |  | DBA |
| Identify the target operating system version. |  | DBA, Systems administrator |
| Identify the hardware requirements for the target server instance based on the Microsoft SQL Server compatibility list and capacity requirements. |  | DBA, Systems administrator |
| Identify the storage requirements for type and capacity. |  | DBA, Systems administrator |
| Identify the network requirements, including latency and bandwidth. |  | DBA, Systems administrator |
| Choose the EC2 instance type based on capacity, storage features, and network features. |  | DBA, Systems administrator |
| Identify the network and host access security requirements for the source and target databases. |  | DBA, Systems administrator |
| Identify a list of users required for the Microsoft SQL Server software installation. |  | DBA, Systems administrator |
| Determine the backup strategy. |  | DBA |
| Determine the availability requirements. |  | DBA |
| Identify the application migration and cutover strategy. |  | DBA, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets. |  | Systems administrator |
| Create security groups and network access control list (ACL). |  | Systems administrator |
| Configure and start an EC2 instance. |  | Systems administrator |

### Install the software
<a name="install-the-software"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the users and groups required for Microsoft SQL Server software. |  | DBA, Systems administrator |
| Download the Microsoft SQL Server software. |  | DBA, Systems administrator |
| Install Microsoft SQL Server software on the EC2 instance and configure the server. |  | DBA, Systems administrator |

### Migrate the data - option 1
<a name="migrate-the-data---option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use native Microsoft SQL Server tools or third-party tools to migrate the database objects and data. | Tools include backup and restore, Copy Database Wizard, and copy and attach database. For more information, see the guide [Migrating Microsoft SQL Server databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/). | DBA |

### Migrate the data - option 2
<a name="migrate-the-data---option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the data by using AWS DMS. | For more information about using AWS DMS, see the links in the [Related resources](#migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-resources) section. | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. | Use AWS Schema Conversion Tool (AWS SCT) to analyze and modify SQL code that’s embedded in application source code. | DBA, App owner |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application switch-over strategy. |  | DBA, App owner, Systems administrator |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down all temporary AWS resources. | Temporary resources include the AWS DMS replication instance and the EC2 instance for AWS SCT. | DBA, Systems administrator |
| Review and validate the project documents. |  | DBA, App owner, Systems administrator |
| Gather metrics around time to migrate, percent of manual versus tool cost savings, and so on. |  | DBA, App owner, Systems administrator |
| Close the project and provide feedback. |  | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2-resources"></a>

**References**
+ [Migrating Microsoft SQL Server databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/)
+ [Amazon EC2](https://aws.amazon.com/ec2/)
+ [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/)
+ [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/)
+ [AWS Database Migration Service](https://aws.amazon.com/dms/)
+ [Microsoft Products on AWS](https://aws.amazon.com/windows/products/)
+ [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/)
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/windows/products/sql/)

**Tutorials and videos**
+ [Getting Started with ](https://aws.amazon.com/ec2/getting-started/)Amazon EC2
+ [Getting Started with ](https://aws.amazon.com/dms/getting-started/)AWS Database Migration Service
+ [Join an Amazon EC2 instance to your Simple AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_join_instance.html)
+ [Join an Amazon EC2 instance to your AWS Managed Microsoft AD Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_join_instance.html)
+ [AWS Database Migration Service ](https://www.youtube.com/watch?v=zb4GcjEdl8U)(video)
+ [Introduction to Amazon EC2 – Elastic Cloud Server & Hosting with AWS](https://www.youtube.com/watch?v=TsRBftzZsQo) (video)
