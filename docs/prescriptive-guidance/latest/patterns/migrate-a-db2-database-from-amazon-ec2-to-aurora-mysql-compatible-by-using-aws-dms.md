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
| Create the database instance. | Create a new instance (user) and database (schema), or use the default `db2inst1` instance and sample database.1. Connect to the EC2 instance by using the terminal to connect to the Db2 database. Alternatively, you can install any DB client software that will connect to the Db2 database.<br />2. To set the password of the db2inst1 user, run the command `sudo passwd db2inst1`.<br />3. To connect to the db2inst1 instance, run the command `sudo su - db2inst1`.<br />4. To connect to the Db2 database, run the command `db2`.<br />5. To connect to the sample database, use the command `connect to sample`. Alternatively, connect to the database that you created.<br />6. After you connect to the database instance, create objects and insert data into these objects by using Db2 SQL statements. | DBA |
| Confirm that the Db2 DB instance is available. | To confirm that the Db2 database instance is up and running, use the `Db2pd -` command. | DBA |

### Configure the target Aurora MySQL-Compatible database
<a name="configure-the-target-aurora-mysql-compatible-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Aurora MySQL-Compatible database. | Create an Amazon Aurora with MySQL compatibility Database from AWS RDS service+ Create a database on Amazon Aurora with MySQL compatibility and version of your choice, e.g. Aurora (MySQL)–5.6.10a<br />+ Install MySQL Workbench application or your preferred DB client software which allows you to connect to MySQL database | DBA, General AWS |
| Configure security groups. | Configure the VPC security group inbound rules for SSH and TCP connections. | General AWS |
| Confirm that the Aurora database is available. | To make sure that the Aurora MySQL-Compatible database is up and running, do the following:1. Connect to the EC2 instance through SSH.<br />2. Configure and connect to the Aurora MySQL-Compatible instance from MySQL Workbench. Use the endpoint as the hostname, as shown in the following example.<pre> mysql-cluster-instance-1.cokmvis0v46q.us-east-1.rds.amazonaws.com</pre><br />3. Create and connect to the new schema (for example, `mysql-sample-db2`).<br />4. Run the MySQL statements to check the schemas and objects in the database. | DBA |

### Configure and run AWS SCT
<a name="configure-and-run-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SCT. | Download and install the latest version of [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html) (the current latest version 1.0.628). | General AWS |
| Configure AWS SCT. | 1. Download the Java Database Connectivity (JDBC) drivers for IBM Db2 (4.22.X version) and MySQL (8.x).<br />2. To configure the drivers in AWS SCT, choose **Settings**, **Global settings**, **Drivers**. | General AWS |
| Create an AWS SCT project. | Create an AWS SCT project and report that uses Db2 for LUW as the source DB engine and Aurora MySQL-Compatible for the target DB engine.<br />To identify the privileges needed to connect to a Db2 for LUW database, see [Using Db2 LUW as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.html). | General AWS |
| Validate the objects. | Choose **Load schema**, validate the objects. Update any incorrect objects on the target database:1. Connect to the Amazon Aurora MySQL-Compatible server by providing the connection details, and choose **Test connection**.<br />Both source and target connections must be successful before AWS SCT can start the migration report.<br />2. After the report is completed, enter the schema to be converted, and choose **Finish**.<br />AWS SCT lists any source and target objects that are converted and have errors.<br />3. Review the errors, and clear them manually.<br />4. After all errors are cleared, open the context (right-click) menu for the schema, and choose **Load schema**.<br />5. Choose **Apply to database**.<br />6. In MySQL Workbench, connect to the Aurora MySQL-Compatible database, and check the schema and objects. | DBA, General AWS |

### Configure and run AWS DMS
<a name="configure-and-run-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance. | Sign in to the AWS Management Console, navigate to the AWS DMS service, and create a replication instance with valid settings for the VPC security group that you configured for the source and target databases. | General AWS |
| Create endpoints. | Create the source endpoint for the Db2 database, and create the target endpoint for the Aurora MySQL-Compatible database:1. Create an endpoint for IBM Db2 as the source by choosing **Select RDS DB instance** and then choosing the Db2 instance that you created. The endpoint configuration details will be automatically populated.<br />2. In the endpoint-specific settings, add the following extra connection attributes.<pre>CurrentLSN=<scan>; MaxKBytesPerRead=64; SetDataCaptureChanges=true</pre><br />If you don’t mention these attributes, the source endpoint test connection will not be successful. For more information, see [Using IBM Db2 LUW as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html).<br />3. Create an endpoint for Aurora MySQL-Compatible as the target by choosing **Select RDS DB instance** and then choosing the Aurora MySQL-Compatible instance that you created. The endpoint configuration details will be automatically populated. For more information, see [Using a MySQL-compatible database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html).<br />4. Test the source and target endpoints. Confirm that both are successful and available<br />5. If the test fails, make sure that the security group inbound rules are valid. | General AWS |
| Create migration tasks. | Create a single migration task or multiple migration tasks for full load and CDC or Data validation:1. To create a database migration task, choose the replication instance, source database endpoint, target database endpoint. Specify the migration type as **Migrate existing data** (full load), **Replicate data changes only (CDC)**, or **Migrate existing data and replicate ongoing changes** (full load and CDC).<br />2. Under **Table mappings**, you can configure selection rules and transformation rules in GUI or JSON formats.<br />3. Under **Selection rules**, select the schema, enter table name, and select Action (Include/Exclude) to be configured (for example, Schema: SAMPLE; Table name: %, Action: Include).<br />4. Under **Transformation rules**, select the target (Schema, Table, or Column). Select the schema name, and choose the action (case, prefix, suffix); for example, Target: Schema; `mysql-sample-db`; Action: Make lowercase.<br />5. Turn on Amazon CloudWatch Logs monitoring. | General AWS |
| Plan the production run. | Confirm downtime with stakeholders such as application owners to run AWS DMS in production systems. | Migration lead |
| Run the migration tasks. | 1. Start the AWS DMS task that has a status of **Ready**.<br />2. Monitor the migration task logs in Amazon CloudWatch Logs for any errors. | General AWS |
| Validate the data. | Review migration task results and data in the source Db2 and target MySQL databases:1. If the status is **Load complete ongoing replication**, the full load with CDC data migration is completed, and validation is ongoing.<br />2. Connect to the Aurora MySQL-Compatible database, and check the data.<br />3. Check the ongoing changes by inserting or updating data in the Db2 database. | DBA |
| Stop migration tasks. | After data validation is successfully completed, stop the validation migration tasks. | General AWS |

## Troubleshooting
<a name="migrate-a-db2-database-from-amazon-ec2-to-aurora-mysql-compatible-by-using-aws-dms-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS SCT source and target test connections are failing. | Configure JDBC driver versions and VPC security group inbound rules to accept the incoming traffic. |
| The Db2 source endpoint test run fails. | Configure the extra connection setting `CurrentLSN=<scan>;`. |
| The AWSDMS task fails to connect to the Db2 source, and the following error is returned.<br />`database is recoverable if either or both of the database configuration parameters LOGARCHMETH1 and LOGARCHMETH2 are set to ON` | To avoid the error, run the following commands:1. `$ db2 update db cfg for sample using LOGARCHMETH1 DISK:/home/db2inst1/logs`<br />2. `$ db2stop`<br />3. `$ db2start`<br />4. `$ db2 connect to sample` <pre>SQL1116N A connection to or activation of database "SAMPLE" cannot be made because of BACKUP PENDING.  SQLSTATE=57019</pre><br />5. `$ db2 backup database sample to ../logs`<pre>SQL2036N The path for the file or device "../logs" is not valid</pre><br />6. `$ cd`<br />7. `$ pwd` <pre> /home/db2inst1</pre><br />8. `$ mkdir /tmp/backup`<br />9. `$ db2 backup database sample to /tmp/backup`<pre>Backup successful. The timestamp for this backup image is : 20190530084921</pre><br />10. `$ db2 connect to sample`<pre>Database Connection Information<br />Database server        = DB2/LINUX 9.7.1<br />SQL authorization ID   = DB2INST1<br />Local database alias   = SAMPLE<br /></pre> |

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
