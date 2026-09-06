---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2.html
---

# Migrate an on-premises Oracle database to Oracle on Amazon EC2
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2"></a>

*Baji Shaik and Pankaj Choudhary, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-summary"></a>

This pattern walks you through the steps for migrating an on-premises Oracle database to Oracle on an Amazon Elastic Compute Cloud (Amazon EC2) instance. It describes two options for migration: using AWS Data Migration Service (AWS DMS) or using native Oracle tools such as RMAN, Data Pump import/export, transportable tablespaces, and Oracle GoldenGate.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle database in an on-premises data center

**Limitations**
+ The target operating system (OS) must be supported by Amazon EC2. For a complete list of supported systems, see [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/).

**Product versions**
+ Oracle versions 10.2 and later (for versions 10.x), 11g and up to 12.2, and 18c for the Enterprise, Standard, Standard One, and Standard Two editions. For the latest list of versions supported by AWS DMS, see "On-premises and Amazon EC2 instance databases" in [Sources for Data Migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html) in the AWS DMS documentation.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-architecture"></a>

**Source technology stack**
+ An on-premises Oracle database

**Target technology stack**
+ An Oracle database instance on Amazon EC2

**Target architecture**

![Setting up replication for an Oracle database on Amaozn EC2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/66c98694-6580-4ffb-9f16-84de58cf8b07/images/386d5b14-8633-4ecc-98fb-59872de99d41.png)

**Data migration architecture**

*Using AWS DMS:*

![Migrating an on-premises Oracle database to Amazon EC2 with AWS DMS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/66c98694-6580-4ffb-9f16-84de58cf8b07/images/14954066-d22b-486a-a432-265296752878.png)

*Using native Oracle tools:*

![Migrating an on-premises Oracle database to Amazon EC2 with Oracle tools.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/66c98694-6580-4ffb-9f16-84de58cf8b07/images/82ba5fcb-8640-45fa-b432-2702dedc0774.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-tools"></a>
+ **AWS DMS - **[AWS Database Migration Services](https://docs.aws.amazon.com/dms/index.html) (AWS DMS) supports several types of source and target databases. For information about the database versions and editions that are supported, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.
+ **Native Oracle tools - **RMAN, Data Pump import/export, transportable tablespaces, Oracle GoldenGate

## Epics
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Validate the versions of the source and target databases. |  | DBA |
|  Identify the version of the target OS. |  | DBA, SysAdmin |
| Identify hardware requirements for the target server instance based on the Oracle compatibility list and capacity requirements. |  | DBA, SysAdmin |
| Identify storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Identify network requirements (latency and bandwidth). |  | DBA, SysAdmin |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, SysAdmin |
| Identify network/host access security requirements for source and target databases. |  | DBA, SysAdmin |
| Identify a list of OS users required for Oracle software installation. |  | DBA, SysAdmin |
| Download AWS Schema Conversion Tool (AWS SCT) and drivers. |  | DBA |
| Create an AWS SCT project for the workload, and connect to the source database. |  | DBA |
| Generate SQL files for the creation of objects (tables, indexes, sequences, etc.). |  | DBA |
| Determine a backup strategy. |  | DBA, SysAdmin  |
| Determine availability requirements. |  | DBA |
| Identify the application migration/switch-over strategy. |  | DBA, SysAdmin, App owner |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets in your AWS account. |  | SysAdmin |
| Create security groups and network access control lists (ACLs). |  | SysAdmin |
| Configure and start the EC2 instance. |  | SysAdmin |

### Install the Oracle software
<a name="install-the-oracle-software"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the OS users and groups required for the Oracle software. |  | DBA, SysAdmin |
| Download the required version of Oracle software. |  |  |
| Install the Oracle software on the EC2 instance. |  | DBA, SysAdmin |
| Create objects like tables, primary keys, views, and sequences by using the scripts generated by AWS SCT. |  | DBA |

### Migrate data - option 1
<a name="migrate-data---option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use native Oracle tools or third-party tools to migrate database objects and data. | Oracle tools include Data Pump import/export, RMAN, transportable tablespaces, and GoldenGate. | DBA |

### Migrate data - option 2
<a name="migrate-data---option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the migration method. |  | DBA |
| Create a replication instance in the AWS DMS console. |  | DBA |
| Create source and target endpoints. |  | DBA |
| Create a replication task. |  | DBA |
| Enable change data capture (CDC) to capture changes for a continuous replication. |  | DBA |
| Run the replication task and monitor logs. |  | DBA |
| Create secondary objects like indexes and foreign keys when the full load is done. |  | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. |  | DBA, SysAdmin, App owner |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application cutover/switch-over strategy. |  | DBA, SysAdmin, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS Secrets Manager resources. |  | DBA, SysAdmin |
| Review and validate the project documents. |  | DBA, SysAdmin, App owner |
| Gather metrics around time to migrate, % of manual vs. tool, cost savings, etc. |  | DBA, SysAdmin, App owner |
| Close out the project and provide feedback. |  |  |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2-resources"></a>

**References**
+ [Strategies for Migrating Oracle Databases to AWS](https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/strategies-migrating-oracle-db-to-aws.html)
+ [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/)
+ [Amazon EC2 website](https://aws.amazon.com/ec2/)
+ [AWS DMS website](https://aws.amazon.com/dms/)
+ [AWS DMS blog posts](https://aws.amazon.com/blogs/database/category/dms/)
+ [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)
+ [Licensing Oracle Software in the Cloud Computing Environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf)

**Tutorials and videos**
+ [Getting Started with Amazon EC2](https://aws.amazon.com/ec2/getting-started/)
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Introduction to Amazon EC2 - Elastic Cloud Server & Hosting with AWS (video)](https://www.youtube.com/watch?v=TsRBftzZsQo)
