---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct.html
---

# Migrate an on-premises Oracle database to Amazon RDS for MySQL using AWS DMS and AWS SCT
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct"></a>

*Sergey Dmitriev and Naresh Damera, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-summary"></a>

This pattern walks you through the migration of an on-premises Oracle database to an Amazon Relational Database Service (Amazon RDS) for MySQL DB instance. It uses AWS Database Migration Service (AWS DMS) to migrate the data, and AWS Schema Conversion Tool (AWS SCT) to convert the source database schema and objects to a format that's compatible with Amazon RDS for MySQL.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-prerequisites-and-limitations"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle database in an on-premises data center

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ All Oracle database editions for versions 11g (versions 11.2.0.3.v1 and later) and up to 12.2, and 18c. For the latest list of supported versions, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support. For information about Oracle database versions supported by AWS SCT, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).
+ AWS DMS currently supports MySQL versions 5.5, 5.6, and 5.7. For the latest list of supported versions, see [Using a MySQL-Compatible Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html) in the AWS documentation.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack**
+ On-premises Oracle database

**Target technology stack**
+ Amazon RDS for MySQL DB instance

**Data migration architecture**

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0385e5ad-a1ca-4c29-945b-592321d95f9d/images/c872e033-b13a-4436-b503-0632b5d437ae.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-tools"></a>
+ **AWS DMS** - [AWS Database Migration Services](https://docs.aws.amazon.com/dms/latest/userguide/) (AWS DMS) helps you migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud, between on-premises instances (through an AWS Cloud setup), or between combinations of cloud and on-premises setups.
+ **AWS SCT** - [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) is used to convert your database schema from one database engine to another. The custom code that the tool converts includes views, stored procedures, and functions. Any code that the tool cannot convert automatically is clearly marked so that you can convert it yourself.

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database version and engine. |  | DBA |
|  Identify the hardware requirements for the target server instance. |  | DBA, SysAdmin |
| Identify the storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, SysAdmin |
| Identify the network access security requirements for the source and target databases. |  | DBA, SysAdmin  |
| Identify the application migration strategy. |  | DBA, SysAdmin, App owner |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets. |  | SysAdmin |
| Create the security groups and network access control lists (ACLs). |  | SysAdmin |
| Configure and start an Amazon RDS DB instance. |  | DBA, SysAdmin |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the database schema by using AWS SCT. |  | DBA |
| Migrate data by using AWS DMS. |  | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use AWS SCT to analyze and convert the SQL code inside the application code. | For more information, see https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP\_Converting.App.html. | App owner |
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
| Review and validate the project documents. |  | DBA, SysAdmin |
| Gather metrics around time to migrate, % of manual vs. tool, cost savings, etc. |  | DBA, SysAdmin |
| Close out the project and provide feedback. |  |  |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-related-resources"></a>

**References**
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)

**Tutorial and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)
+ [AWS DMS (video)](https://www.youtube.com/watch?v=zb4GcjEdl8U)
+ [Amazon RDS (video)](https://www.youtube.com/watch?v=igRfulrrYCo)
