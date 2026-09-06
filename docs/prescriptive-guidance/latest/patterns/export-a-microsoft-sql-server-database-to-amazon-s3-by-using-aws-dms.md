---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms.html
---

# Export a Microsoft SQL Server database to Amazon S3 by using AWS DMS
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms"></a>

*Sweta Krishna, Amazon Web Services*

## Summary
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-summary"></a>

Organizations often need to copy databases to Amazon Simple Storage Service (Amazon S3) for database migration, backup and restore, data archiving, and data analytics. This pattern describes how you can export a Microsoft SQL Server database to Amazon S3. The source database can be hosted on premises or on Amazon Elastic Compute Cloud (Amazon EC2) or Amazon Relational Database Service (Amazon RDS) for Microsoft SQL Server on the Amazon Web Services (AWS) Cloud.

The data is exported by using AWS Database Migration Service (AWS DMS). By default, AWS DMS writes full load and change data capture (CDC) data in comma-separated value (.csv) format. For more compact storage and faster query options, this pattern uses the Apache Parquet (.parquet) format option.

## Prerequisites and limitations
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS Identity and Access Management (IAM) role for the account with write, delete, and tag access to the target S3 bucket, and AWS DMS (`dms.amazonaws.com`) added as a trusted entity to this IAM role
+ An on-premises Microsoft SQL Server database (or Microsoft SQL Server on an EC2 instance or an Amazon RDS for SQL Server database)
+ Network connectivity between the virtual private cloud (VPC) on AWS and the on-premises network provided by AWS Direct Connect or a virtual private network (VPN)

**Limitations**
+ A VPC-enabled (gateway VPC) S3 bucket isn't currently supported in AWS DMS versions earlier than 3.4.7.
+ Changes to the source table structure during full load are not supported.
+ AWS DMS full large binary object (LOB) mode is not supported.

**Product versions**
+ Microsoft SQL Server versions 2005 or later for the Enterprise, Standard, Workgroup, and Developer editions.
+ Support for Microsoft SQL Server version 2019 as a source is available in AWS DMS versions 3.3.2 and later.

## Architecture
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-architecture"></a>

**Source technology stack **
+ An on-premises Microsoft SQL Server database (or Microsoft SQL Server on an EC2 instance or an Amazon RDS for SQL Server database)** **

**Target technology stack  **
+ AWS Direct Connect
+ AWS DMS
+ Amazon S3

**Target architecture **

![Data migrates from SQL Server database through Direct Connect into AWS DMS and then to S3 bucket.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/75b8b20f-a1a8-4633-9816-1b370cc7e92c/images/85bd433c-4a0a-4825-8661-e53f53265191.png)

## Tools
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

## Epics
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the database version. | Validate the source database version and make sure that it’s supported by AWS DMS. For information about supported SQL Server database versions, see [Using a Microsoft SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html). | DBA |
| Create a VPC and security group. | In your AWS account, create a VPC and security group. For more information, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). | System Administrator |
| Create a user for the AWS DMS task. | Create an AWS DMS user in the source database and grant it READ permissions. This user will be used by AWS DMS. | DBA |
| Test the DB connectivity. | Test the connectivity to the SQL Server DB instance from the AWS DMS user. | DBA |
| Create an S3 bucket. | Create the target S3 bucket. This bucket will hold the migrated table data. | Systems administrator |
| Create an IAM policy and role. | 1. To create an IAM policy with bucket permissions, use the code in the *Additional information* section.<br />2. Create the role for AWS DMS, and attach the policy to the role.  | Systems administrator |

### Migrate data by using AWS DMS
<a name="migrate-data-by-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS DMS replication instance. | Sign in to the AWS Management Console, and open the AWS DMS console. In the navigation pane, choose **Replication instances**, **Create replication instance**. For instructions, see [step 1](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html#CHAP_GettingStarted.Replication.ReplicationInstance) in the AWS DMS documentation. | DBA |
| Create source and target endpoints. | Create source and target endpoints. Test the connection from the replication instance to both source and target endpoints. For instructions, see [step 2](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html#CHAP_GettingStarted.Replication.Endpoints) in the AWS DMS documentation. | DBA |
| Create a replication task. | Create a replication task, and select full load or full load with change data capture (CDC) to migrate data from SQL Server to the S3 bucket. For instructions, see [step 3](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html#CHAP_GettingStarted.Replication.Tasks) in the AWS DMS documentation. | DBA |
| Start the data replication. | Start the replication task, and monitor the logs for any errors. | DBA |

### Validate the data
<a name="validate-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the migrated data. | On the console, navigate to your target S3 bucket. Open the subfolder that has the same name as the source database. Confirm that the folder contains all the tables that were migrated from the source database. | DBA |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down and delete temporary AWS resources. | Shut down temporary AWS resources that you created for the data migration, such as the AWS DMS replication instance, and delete them after you validate the export. | DBA |

## Related resources
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-resources"></a>
+ [AWS Database Migration Service User Guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [Using a Microsoft SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html)
+ [Using Amazon S3 as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)
+ [Using an S3 bucket as an AWS DMS target](https://repost.aws/knowledge-center/s3-bucket-dms-target) (AWS re:Post)

## Additional information
<a name="export-a-microsoft-sql-server-database-to-amazon-s3-by-using-aws-dms-additional"></a>

Use the following code to add an IAM policy with S3 bucket permissions for the AWS DMS role. Replace `bucketname` with the name of your bucket.

```
{
     "Version": "2012-10-17",
     "Statement": [
         {
             "Effect": "Allow",
             "Action": [
                 "s3:PutObject",
                 "s3:DeleteObject"
             ],
             "Resource": [
                 "arn:aws:s3:::bucketname*"
             ]
         },
         {
             "Effect": "Allow",
             "Action": [
                 "s3:ListBucket"
             ],
             "Resource": [
                 "arn:aws:s3:::bucketname*"
             ]
         }
     ]
 }
```
