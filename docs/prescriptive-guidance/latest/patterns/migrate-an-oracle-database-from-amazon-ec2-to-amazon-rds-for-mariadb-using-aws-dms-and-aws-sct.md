---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct.html
---

# Migrate an Oracle database from Amazon EC2 to Amazon RDS for MariaDB using AWS DMS and AWS SCT
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct"></a>

*Veeranjaneyulu Grandhi and vinod kumar, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-summary"></a>

This pattern walks you through the steps for migrating an Oracle database on an Amazon Elastic Compute Cloud (Amazon EC2) instance to an Amazon Relational Database Service (Amazon RDS) for MariaDB DB instance. The pattern uses AWS Data Migration Service (AWS DMS) for data migration and AWS Schema Conversion Tool (AWS SCT) for schema conversion.

Managing Oracle databases on EC2 instances requires more resources and is more costly than using a database on Amazon RDS. Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud. Amazon RDS provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

## Prerequisites and limitations
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A source Oracle database with instance and listener services up and running. This database should be in ARCHIVELOG mode.
+ Familiarity with [Using an Oracle Database as a Source for AWS DMS.](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ Familiarity with [Using Oracle as a Source for AWS SCT.](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html)

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ All Oracle database editions for versions 10.2 and later, 11g and up to 12.2, and 18c. For the latest list of supported versions, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and the [AWS SCT version table](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) in the AWS documentation.
+ Amazon RDS supports MariaDB Server Community Server versions 10.3, 10.4, 10.5, and 10.6. For the latest list of supported versions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html).

## Architecture
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack**
+ An Oracle database on an EC2 instance

**Target technology stack**
+ Amazon RDS for MariaDB

**Data migration architecture**

![Using AWS DMS for the migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0b4269c6-8ea3-4672-ad14-1ffac1dc14f3/images/ed191145-e5c2-4d61-8827-31f081450c03.png)

**Target architecture**

![Using AWS SCT for the migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0b4269c6-8ea3-4672-ad14-1ffac1dc14f3/images/0171f548-37dd-4110-851c-7e74dfff3732.png)

## Tools
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-tools"></a>
+ [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects—including views, stored procedures, and functions—to a format compatible with the target database. After converting your database schema and code objects using AWS SCT, you can use AWS DMS to migrate data from the source database to the target database to complete your migration projects. For more information, see [Using Oracle as a Source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html) in the AWS SCT documentation.
+ [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases. AWS DMS supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora. To learn more about migrating Oracle databases, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) in the AWS DMS documentation.

## Epics
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-epics"></a>

### Plan for the migration
<a name="plan-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify versions and database engines. | Identify the source and target database versions and engines. | DBA, Developer |
| Identify the replication instance. | Identify the AWS DMS replication instance. | DBA, Developer |
| Identify storage requirements. | Identify storage type and capacity. | DBA, Developer |
| Identify network requirements. | Identify network latency and bandwidth. | DBA, Developer |
| Identify hardware requirements. | Identify hardware requirements for the source and target server instances (based on the Oracle compatibility list and capacity requirements). | DBA, Developer |
| Identify security requirements. | Identify network-access security requirements for the source and target databases. | DBA, Developer |
| Install drivers. | Install the latest AWS SCT and Oracle drivers. | DBA, Developer |
| Determine a backup strategy. |  | DBA, Developer |
| Determine availability requirements. |  | DBA, Developer |
| Choose an application migration/switchover strategy. |  | DBA, Developer |
| Select the instance type. | Select the proper instance type based on capacity, storage, and network features. | DBA, Developer |

### Configure the environment
<a name="configure-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC).  | The source, target, and replication instances should be in the same VPC and in the same Availability Zone (recommended). | Developer |
| Create security groups. | Create the necessary security groups for database access. | Developer |
| Generate a key pair. | Generate and configure a key pair. | Developer |
| Configure other resources. | Configure subnets, Availability Zones, and CIDR blocks. | Developer |

### Configure the source
<a name="configure-the-source"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the EC2 instance. | For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html). | Developer |
| Install the Oracle database. | Install the Oracle database on the EC2 instance, with required users and roles. | DBA |
| Follow the steps in the task description to access Oracle from outside of the EC2 instance. | 1. Change the local host in `tnsnames` to the Amazon EC2 public DNS.<br />2. Change the local host in `listener` to the Amazon EC2 public DNS.<br />3. Stop and restart the listener. | DBA |
| Update the Amazon EC2 public DNS. | After the EC2 instance restarts, the public DNS changes. Make sure to update the Amazon EC2 public DNS in `tnsnames` and `listener`, or use an Elastic IP address. | DBA, Developer |
| Configure the EC2 instance security group. | Configure the EC2 instance security group so the replication instance and required clients can access the source database. | DBA, Developer |

### Configure the target Amazon RDS for MariaDB environment
<a name="configure-the-target-amazon-rds-for-mariadb-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the RDS DB instance. | Configure and start the Amazon RDS for MariaDB DB instance. | Developer |
| Create tablespaces. | Create any necessary tablespaces in the Amazon RDS MariaDB database. | DBA |
| Configure a security group. | Configure a security group so the replication instance and required clients can access the target database. | Developer |

### Configure AWS SCT
<a name="configure-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install drivers. | Install the latest AWS SCT and Oracle drivers. | Developer |
| Connect. | Enter appropriate parameters and then connect to the source and target. | Developer |
| Generate a schema conversion report. | Generate an AWS SCT schema conversion report. | Developer |
| Correct the code and schema as necessary. | Make any necessary corrections to the code and schema (especially tablespaces and quotation marks). | DBA, Developer |
| Validate the schema. | Validate the schema on the source versus the target before loading data. | Developer |

### Migrate data using AWS DMS
<a name="migrate-data-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set a connection attribute. | For full-load and change data capture (CDC) or just for CDC, set an extra connection attribute. For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html). | Developer |
| Enable supplemental logging. | Enable supplemental logging on the source database. | DBA, Developer |
| Enable archive log mode. | For full-load and CDC (or just for CDC), enable archive log mode on the source database. | DBA |
| Create and test endpoints. | Create source and target endpoints and test the connections. For more information, see the [Amazon DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html). | Developer |
| Create a replication task. | When the endpoints are connected successfully, create a replication task. For more information, see the [Amazon DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html). | Developer |
| Choose replication type. | Choose **CDC only** or **Full load plus CDC** in the task to capture changes for continuous replication only, or for full load and ongoing changes, respectively. | Developer |
| Start and monitor the task. | Start the replication task and monitor Amazon CloudWatch logs. For more information, see the [Amazon DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html). | Developer |
| Validate the data. | Validate the data in the source and target databases. | Developer |

### Migrate applications and cut over to the target database
<a name="migrate-applications-and-cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the chosen application migration strategy. |  | DBA, App owner, Developer |
| Follow the chosen application cutover/switchover strategy. |  | DBA, App owner, Developer |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the schema and data. | Ensure that the schema and data are validated successfully in the source versus the target before project closure. | DBA, Developer |
| Gather metrics. | Gather metrics for time to migrate, percentage of manual versus tool tasks, cost savings, and similar criteria. | DBA, App owner, Developer |
| Review documentation. | Review the project documents and artifacts. | DBA, App owner, Developer |
| Shut down resources. | Shut down temporary AWS resources. | DBA, Developer |
| Close the project. | Close the migration project and provide any feedback. | DBA, App owner, Developer |

## Related resources
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-mariadb-using-aws-dms-and-aws-sct-resources"></a>
+ [MariaDB Amazon RDS overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html)
+ [Amazon RDS for MariaDB product details](https://aws.amazon.com/rds/mariadb/features)
+ [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ [Strategies for Migrating Oracle Databases to AWS](https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/strategies-migrating-oracle-db-to-aws.html)
+ [Licensing Oracle Software in the Cloud Computing Environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf)
+ [Amazon RDS for Oracle FAQs](https://aws.amazon.com/rds/oracle/faqs/)
+ [AWS DMS overview](https://aws.amazon.com/dms/)
+ [AWS DMS blog posts](https://aws.amazon.com/blogs/database/tag/dms/)
+ [Amazon EC2 overview](https://aws.amazon.com/ec2/)
+ [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/)
+ [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
