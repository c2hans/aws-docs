---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html
---

# Migrate a Db2 database from Amazon EC2 to Aurora MySQL-Compatible by using AWS DMS
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms"></a>

*Pinesh Singal, Amazon Web Services*

## Summary
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-summary"></a>

After you migrate your [IBM Db2 for LUW database](https://www.ibm.com/docs/en/db2/11.5?topic=federation) to [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/), consider re-architecting the database by moving to an Amazon Web Services (AWS) cloud-native database. This pattern covers migrating an IBM [Db2](https://www.ibm.com/docs/en/db2/11.5) for LUW database running on an [Amazon](https://docs.aws.amazon.com/ec2/) EC2 instance to an [Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html) database on AWS.

The pattern describes an online migration strategy with minimal downtime for a multi-terabyte Db2 source database with a high number of transactions.

This pattern uses [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) to convert the Db2 database schema to an Aurora MySQL-Compatible schema. Then the pattern  uses [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) to migrate data from the Db2 database to the Aurora MySQL-Compatible database. Manual conversions will be required for the code that isn’t converted by AWS SCT.

## Prerequisites and limitations
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account with a virtual private cloud (VPC)
+ AWS SCT
+ AWS DMS

**Product versions**
+ AWS SCT latest version
+ Db2 for Linux version 11.1.4.4 and later

## Architecture
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-architecture"></a>

**Source technology stack**
+ DB2/Linux x86-64 bit mounted on an EC2 instance

** Target technology stack**
+ An Amazon Aurora MySQL-Compatible Edition database instance

**Source and target architecture**

The following diagram shows the data migration architecture between the source Db2 and target Aurora MySQL-Compatible databases. The architecture on the AWS Cloud includes a virtual private cloud (VPC) (Virtual Private Cloud), an Availability Zone, a public subnet for the Db2 instance and the AWS DMS replication instance, and a private subnet for the Aurora MySQL-Compatible database.

![Architecture of data migration between source Db2 and target Aurora MySQL-Compatible databases.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5abfccc4-148c-4794-8d80-e3c122679125/images/f30664f8-2d6a-4448-8d5c-cff3988a52c7.png)

## Tools
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-tools"></a>

**AWS services**
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database. AWS SCT supports as a source IBM Db2 for LUW versions 9.1, 9.5, 9.7, 10.1, 10.5, 11.1, and 11.5.

## Best practices
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-best-practices"></a>

For best practices, see [Best practices for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html).

## Epics
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-epics"></a>

### Configure the source IBM Db2 database
<a name="configure-the-source-ibm-db2-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IBM Db2 database on Amazon EC2. | You can create an IBM Db2 database on an EC2 instance by using an Amazon Machine Image (AMI) from AWS Marketplace or by installing Db2 software on an EC2 instance.<br />Launch an EC2 instance by selecting an AMI for IBM Db2 (for example, [IBM Db2 v11.5.7 RHEL 7.9](https://aws.amazon.com/marketplace/pp/prodview-aclrjj4hq2ols?sr=0-1&ref_=beagle&applicationId=AWS-EC2-Console)), which is similar to an on-premises database. | DBA, General AWS |
| Configure security groups. | Configure the VPC security group inbound rules for SSH (Secure Shell) and TCP with port 22 and 50000, respectively. | General AWS |
| Create the database instance. | Create a new instance (user) and database (schema), or use the default `db2inst1` instance and sample database.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | DBA |
| Confirm that the Db2 DB instance is available. | To confirm that the Db2 database instance is up and running, use the `Db2pd -` command. | DBA |

### Configure the target Aurora MySQL-Compatible database
<a name="configure-the-target-aurora-mysql-compatible-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Aurora MySQL-Compatible database. | Create an Amazon Aurora with MySQL compatibility Database from AWS RDS service[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | DBA, General AWS |
| Configure security groups. | Configure the VPC security group inbound rules for SSH and TCP connections. | General AWS |
| Confirm that the Aurora database is available. | To make sure that the Aurora MySQL-Compatible database is up and running, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | DBA |

### Configure and run AWS SCT
<a name="configure-and-run-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SCT. | Download and install the latest version of [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html) (the current latest version 1.0.628). | General AWS |
| Configure AWS SCT. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | General AWS |
| Create an AWS SCT project. | Create an AWS SCT project and report that uses Db2 for LUW as the source DB engine and Aurora MySQL-Compatible for the target DB engine.<br />To identify the privileges needed to connect to a Db2 for LUW database, see [Using Db2 LUW as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.html). | General AWS |
| Validate the objects. | Choose **Load schema**, validate the objects. Update any incorrect objects on the target database:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | DBA, General AWS |

### Configure and run AWS DMS
<a name="configure-and-run-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance. | Sign in to the AWS Management Console, navigate to the AWS DMS service, and create a replication instance with valid settings for the VPC security group that you configured for the source and target databases. | General AWS |
| Create endpoints. | Create the source endpoint for the Db2 database, and create the target endpoint for the Aurora MySQL-Compatible database:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | General AWS |
| Create migration tasks. | Create a single migration task or multiple migration tasks for full load and CDC or Data validation:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | General AWS |
| Plan the production run. | Confirm downtime with stakeholders such as application owners to run AWS DMS in production systems. | Migration lead |
| Run the migration tasks. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | General AWS |
| Validate the data. | Review migration task results and data in the source Db2 and target MySQL databases:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) | DBA |
| Stop migration tasks. | After data validation is successfully completed, stop the validation migration tasks. | General AWS |

## Troubleshooting
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS SCT source and target test connections are failing. | Configure JDBC driver versions and VPC security group inbound rules to accept the incoming traffic. |
| The Db2 source endpoint test run fails. | Configure the extra connection setting `CurrentLSN=<scan>;`. |
| The AWSDMS task fails to connect to the Db2 source, and the following error is returned.<br />`database is recoverable if either or both of the database configuration parameters LOGARCHMETH1 and LOGARCHMETH2 are set to ON` | To avoid the error, run the following commands:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms.html) |

## Related resources
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-resources"></a>

**Amazon EC2**
+ [Amazon EC2](https://aws.amazon.com/ec2/)
+ [Amazon EC2 User Guides](https://docs.aws.amazon.com/ec2/)

**Databases**
+ [IBM Db2 Database](https://www.ibm.com/products/db2-database)
+ [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
+ [Working with Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)

**AWS SCT**
+ [AWS DMS Schema Conversion](https://aws.amazon.com/dms/schema-conversion-tool/)
+ [AWS Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Using the AWS SCT user interface](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)
+ [Using IBM Db2 LUW as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.html)

**AWS DMS**
+ [AWS Database Migration Service](https://aws.amazon.com/dms/)
+ [AWS Database Migration Service User Guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html)
+ [Targets for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html)
+ [AWS Database Migration Service and AWS Schema Conversion Tool now support IBM Db2 LUW as a source](https://aws.amazon.com/blogs/database/aws-database-migration-service-and-aws-schema-conversion-tool-now-support-ibm-db2-as-a-source/) (blog post)
+ [Migrating Applications Running Relational Databases to AWS](https://d1.awsstatic.com/whitepapers/Migration/migrating-applications-to-aws.pdf)
