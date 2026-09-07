---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms.html
---

# Migrate an Oracle database from Amazon EC2 to Amazon RDS for Oracle using AWS DMS
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms"></a>

*Chethan Gangadharaiah and Brian motzer, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-summary"></a>

This pattern describes the steps for migrating an Oracle database on Amazon Elastic Compute Cloud (Amazon EC2) to Amazon Relational Database Service (Amazon RDS) for Oracle by using AWS Database Migration Service (AWS DMS). The pattern also uses Oracle SQL Developer or SQL \*Plus to connect to your Oracle DB instance, and includes an AWS CloudFormation template that automates some of the tasks.

Migrating to Amazon RDS for Oracle enables you to focus on your business and applications while Amazon RDS takes care of database administration tasks such as provisioning databases, backup and recovery, security patches, version upgrades, and storage management.

## Prerequisites and limitations
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-prerequisites-and-limitations"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon Machine Image (AMI) for Oracle Database on Amazon EC2

**Product versions**
+ AWS DMS supports Oracle versions 11g (version 11.2.0.3.v1 and later), 12c, and 18c for Amazon RDS instance databases for the Enterprise, Standard, Standard One, and Standard Two editions. For the latest information about supported versions, see [Using an Oracle Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html) in the AWS documentation. (The attached AWS CloudFormation templates use Oracle version 12c as the source database.)
+ Oracle SQL Developer 4.0.3

## Architecture
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-architecture"></a>

**Source architecture**
+ Oracle Database on Amazon EC2

**Target architecture**
+ Amazon RDS for Oracle

**Migration architecture**

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4db0c731-0897-4eb8-a06f-b648c3d94b2c/images/636c2a69-5a78-482d-ae81-55e9ec975ead.png)

## Tools
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-tools"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/index.html) – AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. It supports both homogeneous and heterogeneous migrations. For information about the Oracle database versions and editions that are supported, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and [Using an Oracle Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html) in the AWS documentation.
+ **Oracle SQL Developer or SQL \*Plus** – These tools enable you to connect to the Amazon RDS for Oracle DB instance.

## Epics
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-epics"></a>

### Set up your target database
<a name="set-up-your-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon RDS for Oracle DB instance. | Sign in to the AWS Management Console and open the Amazon RDS console at https://console.aws.amazon.com/rds/. Create an Oracle DB instance by selecting the appropriate engine, template, database credentials setting, instance type, storage, Multi-AZ settings, virtual private cloud (VPC) and configuration, login credentials, and additional settings for the Oracle database. For instructions, view the links in the "Related resources" section. Or use the AWS CloudFormation template (Create\_RDS.yaml) in the attachment to create the Amazon RDS for Oracle DB instance. | Developer |
| Connect to Amazon RDS and grant privileges to the Oracle user. | Modify the security group to open the appropriate ports to connect from the local machine and the AWS DMS replication instance. When you configure connectivity, make sure that the "Publicly accessible" option is selected so you can connect to the database from outside the VPC. Connect to Amazon RDS with Oracle SQL Developer or SQL \*Plus by using the login credentials, create an AWS DMS user, and provide the required privileges to the AWS DMS user to modify the database. | Developer |

### Configure the security group of the source EC2 instance
<a name="configure-the-security-group-of-the-source-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check if the Oracle database is up and running. | Use Secure Shell (SSH) to connect to the EC2 instance, and try connecting to the Oracle database by using SQL \*Plus. | Developer |
| Modify the security group. | Modify the security group of the EC2 instance to open appropriate ports, so you can connect from your local machine and the AWS DMS replication instance. | Developer |

### Set up AWS DMS
<a name="set-up-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS DMS replication instance. | In AWS DMS, create a replication instance in the same VPC as your Amazon RDS for Oracle DB instance. Specify the name and description for the replication instance, choose the instance class and replication engine version (use the default), choose the VPC in which you created the Amazon RDS DB instance, set Multi-AZ settings if required, allocate storage, specify the Availability Zone, and configure additional settings. Alternatively, you can use the AWS CloudFormation template (DMS.yaml) in the attachment to implement this step. | DBA |
| Connect to the source and target database endpoints. | Create the source and target database endpoints by specifying the endpoint identifier, engine, server, port, login credentials, and extra connection attributes. For the source server, use the public DNS of the EC2 instance that's hosting the Oracle database. For the target server, use the endpoint of Amazon RDS for Oracle. Run a test to verify that the source and target connections are working. Alternatively, you can use the AWS CloudFormation template (DMS.yaml) in the attachment to implement this step. | DBA |
| Create an AWS DMS task. | Create an AWS DMS task to migrate data from the source endpoint to the target endpoint, to set up replication between the source and destination endpoint, or both. When creating the AWS DMS task, specify the replication instance, source endpoint, target endpoint, migration type (data only, replication only, or both), table mapping, and filter. Run the AWS DMS task, monitor the task, check the table statistics, and check logs in Amazon CloudWatch. Alternatively, you can use the AWS CloudFormation template (DMS.yaml) in the attachment to implement this step. | DBA |

## Related resources
<a name="migrate-an-oracle-database-from-amazon-ec2-to-amazon-rds-for-oracle-using-aws-dms-related-resources"></a>
+ [Creating an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateOracleInstance.html)
+ [Connecting to a DB Instance Running the Oracle Database Engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.html)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [AWS DMS Step-by-Step Walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html)
+ [Migrating Oracle Databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html)

## Attachments
<a name="attachments-4db0c731-0897-4eb8-a06f-b648c3d94b2c"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/4db0c731-0897-4eb8-a06f-b648c3d94b2c/attachments/attachment.zip)
