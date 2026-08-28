---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms.html
---

# Migrate from SAP ASE to Amazon RDS for SQL Server using AWS DMS
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms"></a>

*Amit Kumar, Amazon Web Services*

## Summary
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-summary"></a>

This pattern provides guidance for migrating an SAP Adaptive Server Enterprise (ASE) database to an Amazon Relational Database Service (Amazon RDS) DB instance that's running Microsoft SQL Server. The source database can be located in an on-premises data center or on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The pattern uses AWS Database Migration Service (AWS DMS) to migrate data and (optionally) computer-aided software engineering (CASE) tools to convert the database schema.

## Prerequisites and limitations
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An SAP ASE database in an on-premises data center or on an EC2 instance
+ A target Amazon RDS for SQL Server database that’s up and running

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ SAP ASE version 15.7 or 16.x only. For the latest information, see [Using an SAP Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html).
+ For Amazon RDS target databases, AWS DMS supports [Microsoft SQL Server versions on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) for the Enterprise, Standard, Web, and Express editions. For the latest information about supported versions, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.

## Architecture
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-architecture"></a>

**Source technology stack **
+ An SAP ASE database that's on premises or on an Amazon EC2 instance

**Target technology stack **
+ An Amazon RDS for SQL Server DB instance

**Source and target architecture**

*From an SAP ASE database on Amazon EC2 to an Amazon RDS for SQL Server DB instance:*

![Target architecture for SAP ASE on Amazon EC2 to Amazon RDS for SQL Server](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5ca697a2-9ca3-4231-b457-c1dc59ada5f1/images/957bdcf0-ab58-4b6d-a71a-d0ecbc31822c.png)

*From an on-premises SAP ASE database to an Amazon RDS for SQL Server DB instance:*

![Target architecture for on-premises SAP ASE to Amazon RDS for SQL Server](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5ca697a2-9ca3-4231-b457-c1dc59ada5f1/images/65aab2f5-0e63-4c34-97e2-cd4ac23751a4.png)

## Tools
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-tools"></a>
+ [AWS Database Migration Service](https://docs.aws.amazon.com/dms/) (AWS DMS) is a web service you can use to migrate data from your database that is on-premises, on an Amazon RDS DB instance, or in a database on an EC2 instance, to a database on an AWS service such as Amazon RDS for SQL Server or an EC2 instance. You can also migrate a database from an AWS service to an on-premises database. You can migrate data between heterogeneous or homogeneous database engines.
+ For schema conversions, you can optionally use [erwin Data Modeler](https://erwin.com/products/erwin-data-modeler/) or [SAP PowerDesigner](https://www.sap.com/products/technology-platform/powerdesigner-data-modeling-tools.html).

## Epics
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions. |  | DBA |
| Identify the storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, SysAdmin |
| Identify the network access security requirements for the source and target databases. |  | DBA, SysAdmin |
| Identify the application migration strategy. |  | DBA, SysAdmin, App owner |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets. |  | SysAdmin |
| Create security groups and network access control lists (ACLs). |  | SysAdmin |
| Configure and start an Amazon RDS DB instance. |  | SysAdmin |

### Migrate data - option 1
<a name="migrate-data---option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the database schema manually or use a CASE tool such as erwin Data Modeler or SAP PowerDesigner. |  | DBA |

### Migrate data - option 2
<a name="migrate-data---option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data using AWS DMS. |  | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. |  | DBA, SysAdmin, App owner |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients over to the new infrastructure. |  | DBA, SysAdmin, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the temporary AWS resources. |  | DBA, SysAdmin |
| Review and validate the project documents. |  | DBA, SysAdmin, App owner |
| Gather metrics such as time to migrate, percentage of manual versus automated tasks, and cost savings. |  | DBA, SysAdmin, App owner |
| Close out the project and provide feedback. |  | DBA, SysAdmin, App owner |

## Related resources
<a name="migrate-from-sap-ase-to-amazon-rds-for-sql-server-using-aws-dms-resources"></a>

**References**
+ [AWS DMS website](https://aws.amazon.com/dms/)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)
+ [Using a SAP ASE Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html)
+ [Limitations for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)
+ [AWS DMS (video)](https://www.youtube.com/watch?v=zb4GcjEdl8U)
+ [Amazon RDS (video)](https://www.youtube.com/watch?v=igRfulrrYCo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
