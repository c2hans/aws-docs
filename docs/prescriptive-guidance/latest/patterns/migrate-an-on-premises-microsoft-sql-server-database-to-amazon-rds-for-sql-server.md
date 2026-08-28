---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon RDS for SQL Server
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server"></a>

*Henrique Lobao, Jonathan Pereira Cruz, and Vishal Singh, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-summary"></a>

This pattern provides guidance for migrating from an on-premises Microsoft SQL Server database to Amazon Relational Database Service (Amazon RDS) for SQL Server. It describes two options for migration: using AWS Data Migration Service (AWS DMS) or using native Microsoft SQL Server tools such as Copy Database Wizard.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Microsoft SQL Server database in an on-premises data center

**Limitations**
+ Database size limit: 16 TB

**Product versions**
+ For the latest list of supported versions and features, see [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport) in the AWS documentation. If you're using AWS DMS, see also [Using a Microsoft SQL Server Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html) for SQL Server versions supported by AWS DMS.

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-architecture"></a>

**Source technology stack**
+ An on-premises Microsoft SQL Server database

**Target technology stack**
+ An Amazon RDS for SQL Server DB instance

**Source and target architecture**

*Using AWS DMS: *

![Architecture for migration from on-premises SQL Server to Amazon RDS using AWS DMS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/27942833-c294-405c-90e6-32cc197e36ee/images/69b9877c-2d56-4d64-8475-a3dae789c5de.png)

*Using native SQL Server tools: *

![Architecture for migration from on-premises SQL Server to Amazon RDS using SQL Server tools](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/27942833-c294-405c-90e6-32cc197e36ee/images/45ee14e4-3c7e-4b35-a2c9-3e8e3c7e6cee.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-tools"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) supports several types of source and target databases. For details, see [AWS DMS Step-by-Step Walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html). If AWS DMS doesn't support the source database, select another method for migrating the data.
+ Native Microsoft SQL Server tools include backup and restore, Copy Database Wizard, copy and attach database.

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database version and engine. |  | DBA |
| Identify the hardware requirements for the target server instance. |  | DBA, Systems administrator |
| Identify the storage requirements (storage type and capacity). |  | DBA, Systems administrator |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, Systems administrator |
| Identify the network access security requirements for source and target databases. |  | DBA, Systems administrator |
| Identify the application migration strategy. |  | DBA, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). |  | Systems administrator |
| Create security groups. |  | Systems administrator |
| Configure and start an Amazon RDS DB instance. |  | DBA, Systems administrator |

### Migrate data - option 1
<a name="migrate-data---option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use native SQL Server tools or third-party tools to migrate database objects and data. |  | DBA |

### Migrate data - option 2
<a name="migrate-data---option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data with AWS DMS. |  | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. |  | DBA, App owner, Systems administrator |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients over to the new infrastructure. |  | DBA, App owner, Systems administrator |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the temporary AWS resources. |  | DBA, Systems administrator |
| Review and validate the project documents. |  | DBA, App owner, Systems administrator |
| Gather metrics such as time to migrate, percentage of manual versus automated tasks, and cost savings. |  | DBA, App owner, Systems administrator |
| Close out the project and provide feedback. |  | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-resources"></a>

**References**
+ [Deploying Microsoft SQL Server on Amazon Web Services](https://d1.awsstatic.com/whitepapers/RDS/Deploying_SQLServer_on_AWS.pdf)
+ [AWS DMS website](https://aws.amazon.com/dms/)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)
+ [Microsoft Products on AWS](https://aws.amazon.com/windows/products/)
+ [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/)
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/windows/products/sql/)
+ [Using Windows Authentication with a Microsoft SQL Server DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html)
+ [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)
+ [AWS DMS (video)](https://www.youtube.com/watch?v=zb4GcjEdl8U)
+ [Amazon RDS (video)](https://www.youtube.com/watch?v=igRfulrrYCo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
