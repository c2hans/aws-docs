---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct.html
---

# Migrate from Oracle on Amazon EC2 to Amazon RDS for MySQL using AWS DMS and AWS SCT
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct"></a>

*Anil Kunapareddy, Amazon Web Services*

*Harshad Gohil, None*

## Summary
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-summary"></a>

Managing Oracle databases on Amazon Elastic Compute Cloud (Amazon EC2) instances requires resources and can be costly. Moving these databases to an Amazon Relational Database Service (Amazon RDS) for MySQL DB instance will ease your job by optimizing the overall IT budget. Amazon RDS for MySQL also provides features like Multi-AZ, scalability, and automatic backups.

This pattern walks you through the migration of a source Oracle database on Amazon EC2 to a target Amazon RDS for MySQL DB instance. It uses AWS Database Migration Service (AWS DMS) to migrate the data, and AWS Schema Conversion Tool (AWS SCT) to convert the source database schema and objects to a format that's compatible with Amazon RDS for MySQL.

## Prerequisites and limitations
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source database with instance and listener services running, in ARCHIVELOG mode
+ A target Amazon RDS for MySQL database, with sufficient storage for data migration

**Limitations**
+ AWS DMS does not create a schema on the target database; you have to do that. The schema name must already exist for the target. Tables from the source schema are imported to user/schema, which AWS DMS uses to connect to the target instance. You must create multiple replication tasks if you have to migrate multiple schemas.

**Product versions**
+ All Oracle database editions for versions 10.2 and later, 11g and up to 12.2, and 18c. For the latest list of supported versions, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and [Using a MySQL-Compatible Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support. For information about Oracle database versions supported by AWS SCT, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).
+ AWS DMS supports versions 5.5, 5.6, and 5.7 of MySQL.

## Architecture
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack**
+ An Oracle database on an EC2 instance

**Target technology stack**
+ Amazon RDS for MySQL DB instance

**Data migration architecture**

![Using AWS DMS to migrate from Oracle on Amazon EC2 to Amazon RDS for MySQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8a8e346e-7944-4999-bc11-208efead3792/images/c00f908c-f348-41dd-a31c-3931b990777a.png)

**Source and target architecture  **

![Using AWS DMS and AWS SCT to migrate from Oracle on Amazon EC2 to Amazon RDS for MySQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8a8e346e-7944-4999-bc11-208efead3792/images/e7ba7ac0-3094-4142-b355-fb192e242432.png)

## Tools
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-tools"></a>
+ **AWS DMS** - [AWS Database Migration Service](https://docs.aws.amazon.com/dms/) (AWS DMS) is a web service you can use to migrate data from your database that is on-premises, on an Amazon RDS DB instance, or in a database on an EC2 instance, to a database on an AWS service such as Amazon RDS for MySQL or an EC2 instance. You can also migrate a database from an AWS service to an on-premises database. You can migrate data between heterogeneous or homogeneous database engines.
+ **AWS SCT** - [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format that's compatible with the target database. After converting your database schema and code objects using AWS SCT, you can use AWS DMS to migrate data from the source database to the target database to complete your migration projects.

## Epics
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the source and target database versions and engines. |  | DBA/Developer |
| Identify the DMS replication instance. |  | DBA/Developer |
| Identify storage requirements such as storage type and capacity. |  | DBA/Developer |
| Identify network requirements such as latency and bandwidth. |  |  DBA/Developer |
| Identify hardware requirements for the source and target server instances (based on Oracle compatibility list and capacity requirements). |  | DBA/Developer |
| Identify network access security requirements for source and target databases. |  | DBA/Developer |
| Install AWS SCT and Oracle drivers. |  | DBA/Developer |
| Determine a backup strategy. |  | DBA/Developer |
| Determine availability requirements. |  | DBA/Developer |
| Identify application migration and switch-over strategy. |  | DBA/Developer |
| Select the proper DB instance type based on capacity, storage, and network features. |  | DBA/Developer |

### Configure the environment
<a name="configure-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). The source, target, and replication instance should be in the same VPC. It is also good to have these in the same Availability Zone. |  | Developer |
| Create the necessary security groups for database access. |  |  Developer |
| Generate and configure a key pair. |  | Developer |
| Configure subnets, Availability Zones, and CIDR blocks. |  | Developer |

### Configure the source: Oracle database on EC2 instance
<a name="configure-the-source-oracle-database-on-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Oracle Database on Amazon EC2 with required users and roles. |  | DBA |
|  Perform the three steps in the next column to access Oracle from outside the EC2 instance. | 1. Change the local host in `tnsnames` to the Amazon EC2 public DNS.<br />2. Change the local host in `listener` to the Amazon EC2 public DNS.<br />3. Stop and restart the listener. | DBA |
| When Amazon EC2 is restarted, the public DNS changes. Make sure to update Amazon EC2 public DNS in 'tnsnames' and 'listener' or use an Elastic IP address. |  | DBA/Developer |
| Configure the EC2 instance security group so that the replication instance and required clients can access the source database. |  | DBA/Developer |

### Configure the target: Amazon RDS for MySQL
<a name="configure-the-target-amazon-rds-for-mysql"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure and start the Amazon RDS for MySQL DB instance. |  | Developer |
| Create the necessary tablespace in the Amazon RDS for MySQL DB instance. |  | DBA |
| Configure the security group so that the replication instance and required clients can access the target database. |  | Developer |

### Configure AWS SCT and create a schema in the target database
<a name="configure-aws-sct-and-create-a-schema-in-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SCT and Oracle drivers. |  | Developer |
| Enter the appropriate parameters and connect to the source and target. |  | Developer |
| Generate a schema conversion report. |  | Developer |
| Correct the code and schema as necessary, especially tablespaces and quotes, and run on the target database. |  |  Developer |
| Validate the schema on source vs. target before migrating data. |  | Developer |

### Migrate data using AWS DMS
<a name="migrate-data-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| For full-load and change data capture (CDC) or just CDC, you must set an extra connection attribute. |  | Developer |
| The user specified in the AWS DMS source Oracle database definitions must be granted all the required privileges. For a complete list, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Source.Oracle.html\#CHAP\_Source.Oracle.Self-Managed. |  | DBA/Developer |
| Enable supplemental logging in the source database. |  | DBA/Developer |
| For full-load and change data capture (CDC) or just CDC, enable ARCHIVELOG mode in the source database. |  | DBA |
| Create source and target endpoints, and test the connections. |  | Developer |
| When the endpoints are connected successfully, create a replication task. |  | Developer |
| Select CDC only (or) full load plus CDC in the task to capture changes for continuous replication only (or) full load plus ongoing changes, respectively. |  | Developer |
| Run the replication task and monitor Amazon CloudWatch logs. |  |  Developer |
| Validate the data in the source and target databases. |  | Developer |

### Migrate your application and cut over
<a name="migrate-your-application-and-cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the steps for your application migration strategy. |  | DBA, Developer, App owner |
| Follow the steps for your application cutover/switch-over strategy. |  | DBA, Developer, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the schema and data in source vs. target databases. |  | DBA/Developer |
| Gather metrics around time to migrate, percent of manual vs. tool, cost savings, etc. |  |  DBA/Developer/AppOwner |
| Review the project documents and artifacts. |  | DBA/Developer/AppOwner |
| Shut down temporary AWS resources. |  | DBA/Developer |
| Close out the project and provide feedback. |  | DBA/Developer/AppOwner |

## Related resources
<a name="migrate-from-oracle-on-amazon-ec2-to-amazon-rds-for-mysql-using-aws-dms-and-aws-sct-resources"></a>
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [AWS DMS website](https://aws.amazon.com/dms/)
+ [AWS DMS blog posts](https://aws.amazon.com/blogs/database/tag/dms/)
+ [Strategies for Migrating Oracle Database to AWS](https://d1.awsstatic.com/whitepapers/strategies-for-migrating-oracle-database-to-aws.pdf)
+ [Amazon RDS for Oracle FAQs](https://aws.amazon.com/rds/oracle/faqs/)
+ [Oracle FAQ](https://aws.amazon.com/oracle/faq/)
+ [Amazon EC2](https://aws.amazon.com/ec2/)
+ [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/)
+ [Licensing Oracle Software in the Cloud Computing Environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf)
