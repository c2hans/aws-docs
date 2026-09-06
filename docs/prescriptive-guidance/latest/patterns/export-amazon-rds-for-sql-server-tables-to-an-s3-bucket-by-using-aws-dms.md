---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms.html
---

# Export Amazon RDS for SQL Server tables to an S3 bucket by using AWS DMS
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms"></a>

*Subhani Shaik, Amazon Web Services*

## Summary
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-summary"></a>

Amazon Relational Database Service (Amazon RDS) for SQL Server doesn’t support loading data onto other database (DB) engine linked servers on the Amazon Web Services (AWS) Cloud. Instead, you can use AWS Database Migration Service (AWS DMS) to export Amazon RDS for SQL Server tables to an Amazon Simple Storage Service (Amazon S3) bucket, where the data is available to other DB engines.

AWS DMS helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases.

This pattern uses AWS Secrets Manager while configuring the AWS DMS endpoints. Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. You can use the service to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call to Secrets Manager, reducing the need to hardcode sensitive information. Secrets Manager offers secret rotation with built-in integration for Amazon RDS, Amazon Redshift, and Amazon DocumentDB (with MongoDB compatibility). Also, the service is extensible to other types of secrets, including API keys and OAuth tokens. With Secrets Manager, you can control access to secrets by using fine-grained permissions and audit secret rotation centrally for resources in the AWS Cloud, third-party services, and on premises.

## Prerequisites and limitations
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon S3 bucket
+ A virtual private cloud (VPC)
+ A DB subnet
+ Amazon RDS for SQL Server
+ An AWS Identity and Access Management (IAM) role with access (list, get, and put objects) to the S3 bucket on behalf of the Amazon RDS instance
+ Secrets Manager to store the Amazon RDS instance credentials

## Architecture
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-architecture"></a>

**Technology stack**
+ Amazon RDS for SQL Server
+ AWS DMS
+ Amazon S3
+ AWS Secrets Manager

**Target architecture**

The following diagram shows the architecture for exporting data from the Amazon RDS instance to the Amazon S3 bucket with the help of AWS DMS.

![Description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7ba5756d-44a5-4aa3-97b6-fa3684ae6ce6/images/90f918e1-3ec2-4434-82b8-3ff4ad340fb9.png)

1. The AWS DMS migration task connecting to the source Amazon RDS instance through the source endpoint

1. Copying data from the source Amazon RDS instance

1. The AWS DMS migration task connecting to the target Amazon S3 bucket through the target endpoint

1. Exporting copied data to the Amazon S3 bucket in comma-separated values (CSV) format

## Tools
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.

**Other tools**
+ [Microsoft SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components.

## Best practices
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-best-practices"></a>
+ Run a proof of concept with a subset of tables before the full migration to benchmark performance and identify issues.
+ Avoid running AWS DMS tasks during peak database hours to reduce load on the source Amazon RDS instance.
+ Follow the [best practices for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html).
+ Follow the [security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html).

## Epics
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-epics"></a>

### Configure the Amazon RDS for SQL Server instance
<a name="configure-the-rdslongms-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Amazon RDS for SQL Server instance. | 1. Open the AWS Management Console, choose **RDS**, and use the **Standard create** option to create an Amazon RDS instance with the required edition, such as SQL Server Express Edition, SQL Server Standard Edition, or SQL Server Enterprise Edition. For the version, choose 2016 or later.<br />2. Under **Templates**, choose **Dev/Test**. | DBA, DevOps engineer |
| Set up credentials for the instance. | 1. Enter a name for the instance.<br />2. Provide a username and password for the Amazon RDS instance. | DBA, DevOps engineer |
| Configure the instance class, storage, auto scaling, and availability. | 1. Select the **DB instance class** from the list: **Standard**, **Memory Optimized**, and **Burstable** classes. Choose the DB instance type that allocates the computational, network, and memory capacity required by the workloads planned for this DB instance. For more information, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.RegionSupport).<br />2. Select the **Storage Type** from the list: **General Purpose SSD**, **Provisioned IOPS SSD**, or **Magnetic**. Allocate the default storage size as required.<br />3. Choose **Enable storage autoscaling** to increase the Amazon RDS storage based on your capacity planning.<br />4. A Multi-AZ deployment with a replication instance is supported by AWS DMS. In the event of an outage in the Availability Zone, internal hardware, or network, AWS DMS will create a standby instance and provide high availability (HA) through automatic failover to the standby replicas. Depending on the size of your import, select the appropriate option. | DBA, DevOps engineer |
| Specify the VPC, subnet group, public access, and security group. | Select the **VPC**, **DB subnet groups**, and **VPC security group **as required to create the Amazon RDS instance. Follow the best practices, for example:+ Do not enable public access to the Amazon RDS instance.<br />+ Do not use the CIDR 0.0.0.0/0 in the security groups.<br />+ Use only the required IP address and port details to access the Amazon RDS instance. | DBA, DevOps engineer |
| Configure monitoring, backup, and maintenance. | 1. Specify the backup options that you want. By default, automated backups are enabled with a retention period of 7 days.<br />2. Choose the appropriate **auto minor version upgrade** and **Maintenance window** settings to apply the pending modifications or maintenance to the database by Amazon RDS.<br />3. Choose **Create database**.  | DBA, DevOps engineer |

### Set up the database and example data
<a name="set-up-the-database-and-example-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a table and load the example data. | In the new database, create a table. Use the example code in the *Additional information* section to load data into the table. | DBA, DevOps engineer |

### Set up credentials
<a name="set-up-credentials"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the secret. | 1. On the console, choose **Secrets Manager**, and then choose **Store a new secret**. <br />2. Enter a username and password for the Amazon RDS for SQL Server database. This secret will be used for the AWS DMS source endpoint. | DBA, DevOps engineer |

### Set up access between the database and the Amazon S3 bucket
<a name="set-up-access-between-the-database-and-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role for access to Amazon RDS. | 1. On the console, choose **IAM**, and create an IAM role that gives an S3 bucket read/write access to Amazon RDS. <br />2. Under **Feature**, select **S3 Integration**. | DBA, DevOps engineer |

### Create the Amazon S3 bucket
<a name="create-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Amazon S3 bucket. | To save the data from Amazon RDS for SQL Server, on the console, choose **S3**, and then choose **Create bucket**. Make sure that the Amazon S3 bucket is not publicly available. | DBA, DevOps engineer |

### Set up access between AWS DMS and the Amazon S3 bucket
<a name="set-up-access-between-dms-and-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role for AWS DMS to access Amazon S3. | Create an IAM role that allows AWS DMS to list, get, and put objects from the Amazon S3 bucket. | DBA, DevOps engineer |

### Configure AWS DMS
<a name="configure-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS DMS source endpoint. | 1. On the console, choose **Database Migration Service**, and choose **Endpoints**. Create the **Source endpoint**, selecting the **Select RDS DB instance** check box.<br />2. For the Source engine, select **Microsoft SQL Server**.<br />3. Under **Access to endpoint database**, choose **AWS Secrets Manager**, and enter the secret and IAM role that you created earlier, and the database name.<br />4. Test the source endpoint. | DBA, DevOps engineer |
| Create the AWS DMS target endpoint. | Create the **Target endpoint,** selecting Amazon S3 as the **Target engine**.<br />Provide the Amazon S3 bucket name and folder name for the IAM role that you created previously. | DBA, DevOps engineer |
| Create the AWS DMS replication instance. | In the same VPC, subnet, and security group, create the AWS DMS replication instance. For more information about choosing an instance class, see the [AWS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html#CHAP_ReplicationInstance.Types.Deciding). | DBA, DevOps engineer |
| Create the AWS DMS migration task. | To export the data from Amazon RDS for SQL Server to the Amazon S3 bucket, create a database migration task. For the migration type, choose **Migrate existing data**. Select the AWS DMS endpoints and replication instance that you created. | DBA, DevOps engineer |

### Export the data to the Amazon S3 bucket
<a name="export-the-data-to-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the database migration task. | To export the SQL Server table data, start the database migration task. The task will export the data from Amazon RDS for SQL Server to the Amazon S3 bucket in CSV format. | DBA, DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the resources. | To avoid incurring extra costs, use the console to delete the resources in the following order:1. Migration task<br />2. Replication instance<br />3. Endpoints<br />4. Amazon S3 bucket<br />5. Database instance | DBA, DevOps engineer |

## Troubleshooting
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Troubleshooting issues with Microsoft SQL Server | For more information about resolving issues with Microsoft SQL Server while using AWS DMS, see [Troubleshooting issues with Microsoft SQL Server](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.SQLServer). |
| Troubleshooting migration tasks | For more information about resolving migration issues when using AWS DMS, see [Troubleshooting migration tasks in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html). |

## Related resources
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-resources"></a>
+ [AWS DMS](https://aws.amazon.com/dms/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/)
+ [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.Options.S3-integration.html)
+ [Using a Microsoft SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html)
+ [Using Amazon S3 as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)

## Additional information
<a name="export-amazon-rds-for-sql-server-tables-to-an-s3-bucket-by-using-aws-dms-additional"></a>

To create the database and table, and to load the example data, use the following code:

```
--Step1: Database creation in RDS SQL Server
CREATE DATABASE [Test_DB]
 ON  PRIMARY
( NAME = N'Test_DB', FILENAME = N'D:\rdsdbdata\DATA\Test_DB.mdf' , SIZE = 5120KB , FILEGROWTH = 10%)
 LOG ON
( NAME = N'Test_DB_log', FILENAME = N'D:\rdsdbdata\DATA\Test_DB_log.ldf' , SIZE = 1024KB , FILEGROWTH = 10%)
GO

--Step2: Create Table
USE Test_DB
GO
Create Table Test_Table(ID int, Company Varchar(30), Location Varchar(20))

--Step3: Load sample data.
USE Test_DB
GO
Insert into Test_Table values(1,'AnyCompany','India')
Insert into Test_Table values(2,'AnyCompany','USA')
Insert into Test_Table values(3,'AnyCompany','UK')
Insert into Test_Table values(4,'AnyCompany','Hyderabad')
Insert into Test_Table values(5,'AnyCompany','Banglore')
```
