---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation.html
---

# Migrate Amazon RDS for Oracle to Amazon RDS for PostgreSQL with AWS SCT and AWS DMS using AWS CLI and CloudFormation
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation"></a>

*Pinesh Singal, Amazon Web Services*

## Summary
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-summary"></a>

This pattern shows how to migrate a multi-terabyte [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) DB instance to an [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) DB instance by using the AWS Command Line Interface (AWS CLI). The approach provides minimal downtime and doesn’t require signing in to the AWS Management Console.

This pattern helps avoid manual configurations and individual migrations by using the AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS) consoles. The solution sets up a one-time configuration for multiple databases and performs the migrations by using AWS SCT and AWS DMS in the AWS CLI.

The pattern uses AWS SCT to convert database schema objects from Amazon RDS for Oracle to Amazon RDS for PostgreSQL, and then uses AWS DMS to migrate the data. Using Python scripts in AWS CLI, you create AWS SCT objects and AWS DMS tasks with an CloudFormation template.

## Prerequisites and limitations
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing Amazon RDS for Oracle DB instance.
+ An existing Amazon RDS for PostgreSQL DB instance.
+ An Amazon Elastic Compute Cloud (Amazon EC2) instance or local machine with Windows or Linux OS for running scripts.
+ An understanding of the following AWS DMS migration task types: `full-load`, `cdc`, `full-load-and-cdc`.  For more information, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html) in the AWS DMS documentation.
+ AWS SCT, installed and configured with Java Database Connectivity (JDBC) drivers for Oracle and PostgreSQL database engines. For more information, see [Installing and configuring AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html#CHAP_Installing.Procedure) in the AWS SCT documentation.
+ The `AWSSchemaConversionToolBatch.jar` file from the installed AWS SCT folder, copied to your working directory.
+ The `cli-sct-dms-cft.zip` file (attached), downloaded and extracted in your working directory.
+ The most recent AWS DMS replication instance engine version. For more information, see [How do I create an AWS DMS replication instance](https://aws.amazon.com/premiumsupport/knowledge-center/create-aws-dms-replication-instance/) in the AWS Support documentation and [AWS DMS release notes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html).
+ AWS CLI version 2, installed and configured with your access key ID, secret access key, and default AWS Region name for the EC2 instance or OS where the scripts are run. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the AWS CLI documentation.
+ Familiarity with CloudFormation templates. For more information, see [How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html) in the CloudFormation documentation.
+ Python version 3, installed and configured on the EC2 instance or OS where the scripts are run. For more information, see the [Python documentation](https://docs.python.org/3/).

**Limitations **
+ The minimum requirements for your source Amazon RDS for Oracle DB instance are:
  + Oracle versions 12c (12.1.0.2, 12.2.0.1), 18c (18.0.0.0), and 19c (19.0.0.0) for the Enterprise, Standard, Standard One, and Standard Two editions.
  + Although Amazon RDS supports Oracle 18c (18.0.0.0), this version is on a deprecation path because Oracle no longer provides patches for 18c after the end-of-support date. For more information, see [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html#Oracle.Concepts.Deprecate.11204) in the Amazon RDS documentation.
  + Amazon RDS for Oracle 11g is no longer supported.
+ The minimum requirements for your target Amazon RDS for PostgreSQL DB instance are:
  + PostgreSQL versions 9 (9.5 and 9.6), 10.x, 11.x, 12.x, and 13.x

**Product versions**
+ Amazon RDS for Oracle DB instance version 12.1.0.2 and later
+ Amazon RDS for PostgreSQL DB instance version 11.5 and later
+ AWS CLI version 2
+ The latest version of AWS SCT
+ The latest version of Python 3

## Architecture
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-architecture"></a>

**Source technology stack  **
+ Amazon RDS for Oracle

**Target technology stack  **
+ Amazon RDS for PostgreSQL

**Source and target architecture **

The following diagram shows the migration of an Amazon RDS for Oracle DB instance to an Amazon RDS for PostgreSQL DB instance using AWS DMS and Python scripts.

![Migrating RDS for Oracle DB instance to RDS for PostgreSQL DB instance using AWS DMS and Python.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5e041494-2e64-4f09-b6ec-0e0cba3a4972/images/77022e13-46fb-4aa8-ab49-85b0ca4c317a.png)

The diagram shows the following migration workflow:

1. The Python script uses AWS SCT to connect to the source and target DB instances.

1. The user starts AWS SCT with the Python script, converts the Oracle code to PostgreSQL code, and runs it on the target DB instance.

1. The Python script creates AWS DMS replication tasks for the source and target DB instances.

1. The user deploys Python scripts to start the AWS DMS tasks and then stops the tasks after the data migration is complete.

**Automation and scale**

You can automate this migration by adding parameters and security-related changes to your Python script, to provide additional functionality.

## Tools
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command line shell.
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions. This pattern converts the `.csv` input file to a `.json` input file by using a Python script. The `.json` file is used in AWS CLI commands to create an CloudFormation stack that creates multiple AWS DMS replication tasks with Amazon Resource Names (ARNs), migration types, task settings, and table mappings.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores to the AWS Cloud or between combinations of cloud and on-premises setups. This pattern uses AWS DMS to create, start, and stop tasks with a Python script that runs on the command line, and to create the CloudFormation template.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database. This patterns requires the `AWSSchemaConversionToolBatch.jar` file from the installed AWS SCT directory.

**Code**

The `cli-sct-dms-cft.zip` file (attached) contains the complete source code for this pattern.

## Epics
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-epics"></a>

### Configure AWS SCT and create database objects in the AWS CLI
<a name="configure-awssct-and-create-database-objects-in-the-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS SCT to run from the AWS CLI. | 1. Configure the source and target environment configuration details in the `database_migration.txt` file by using the following format:<pre>#source_vendor,source_hostname,source_dbname,source_user,source_pwd,source_schema,source_port,source_sid,target_vendor,target_hostname,target_user,target_pwd,target_dbname,target_port<br />ORACLE,myoracledb.cokmvis0v46q.us-east-1.rds.amazonaws.com,ORCL,orcl,orcl1234,orcl,1521,ORCL,POSTGRESQL,mypgdbinstance.cokmvis0v46q.us-east-1.rds.amazonaws.com,pguser,pgpassword,pgdb,5432</pre><br />2. Modify the AWS SCT configuration parameters according to your requirements in the following files: `project_settings.xml`, `Oracle_PG_Test_Batch.xml`, and `ORACLE-orcl-to-POSTGRESQL.xml`. | DBA |
| Run the `run_aws_sct.py` Python script. | Run the `run_aws_sct.py` Python script by using the following command:<br />`$ python run_aws_sct.py database_migration.txt`<br />The Python script converts the database objects from Oracle to PostgreSQL and creates SQL files in PostgreSQL format. The script also creates the PDF file `Database migration assessment report`, which provides you with detailed recommendations and conversion statistics for database objects. | DBA |
| Create objects in Amazon RDS for PostgreSQL. | 1. Manually modify the SQL files generated by AWS SCT, if required.<br />2. Run the SQL files and create objects in your Amazon RDS for PostgreSQL DB instance. | DBA |

### Configure and create AWS DMS tasks by using the AWS CLI and CloudFormation
<a name="configure-and-create-dms-tasks-by-using-the-cli-and-cfn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS DMS replication instance. | Sign in to the AWS Management Console, open the [AWS DMS console](https://console.aws.amazon.com/dms/v2/), and create a replication instance that is configured according to your requirements.<br />For more information, see [Creating a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html) in the AWS DMS documentation and [How do I create an AWS DMS replication instance](https://aws.amazon.com/premiumsupport/knowledge-center/create-aws-dms-replication-instance/) in the AWS Support documentation. | DBA |
| Create the source endpoint. | On the AWS DMS console, choose **Endpoints** and then create a source endpoint for the Oracle database according to your requirements. The extra connection attribute must be `numberDataTypeScale` with a `-2` value.<br />For more information, see [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the AWS DMS documentation. | DBA |
| Create the target endpoint. | On the AWS DMS console, choose **Endpoints** and then create a target endpoint for the PostgreSQL database according to your requirements.  <br />For more information, see [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the AWS DMS documentation. | DevOps engineer |
| Configure the AWS DMS replication details to run from the AWS CLI. | Configure the AWS DMS source and target endpoints and replication details in the `dms-arn-list.txt` file with the source endpoint ARN, target endpoint ARN, and the replication instance ARN by using the following format:<pre>#sourceARN,targetARN,repARN<br />arn:aws:dms:us-east-1:123456789012:endpoint:EH7AINRUDZ5GOYIY6HVMXECMCQ<br />arn:aws:dms:us-east-1:123456789012:endpoint:HHJVUV57N7O3CQF4PJZKGIOYY5<br />arn:aws:dms:us-east-1:123456789012:rep:LL57N77AQQAHHJF4PJFHNEDZ5G</pre> | DBA |
| Run the `dms-create-task.py` Python script to create the AWS DMS tasks. | 1. Run the `dms-create-task.py` Python script by using the following command:<pre>$ python dms-create-task.py database_migration.txt dms-arn-list.txt <cft-stack-name> <migration-type></pre><br />where:`database_migration.txt` is the database migration text file.`dms-arn-list.txt` is the ARN list for AWS DMS.`<cft-stack-name>` is the user-defined CloudFormation stack name.`<migration-type>` is `full-load`, `cdc`, or `full-load-and-cdc`.<br />2. Depending on your migration type, you can use the following commands to create three types of AWS DMS tasks:`$ python dms-create-task.py database_migration.txt dms-arn-list.txt dms-cli-cft-stack full-load``$ python dms-create-task.py database_migration.txt dms-arn-list.txt dms-cli-cft-stack cdc``$ python dms-create-task.py database_migration.txt dms-arn-list.txt dms-cli-cft-stack full-load-and-cdc` | DBA |
| Verify that AWS DMS tasks are ready. | On the AWS DMS console, check that your AWS DMS tasks are in `Ready` status in the **Status **section. | DBA |

### Start and stop the AWS DMS tasks by using the AWS CLI
<a name="start-and-stop-the-dms-tasks-by-using-the-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the AWS DMS tasks. | Run the `dms-start-task.py` Python script by using the following command:<pre>$ python dms-start-task.py start '<cdc-start-datetime>'</pre>The start date and time must be in the `'DD-MON-YYYY'` or `'YYYY-MM-DDTHH:MI:SS'` format (for example, `'01-Dec-2019'` or `'2018-03-08T12:12:12'`).<br />You can review the AWS DMS task status in the **Table statistics** tab on the **Tasks **page of the AWS DMS console. | DBA |
| Validate the data. | 1. After the full-load migration is complete, the task is continuously kept running for CDC.<br />2. When CDC is complete or no more changes need to be migrated, review and validate the migration task results and data in your Oracle and PostgreSQL databases.<br />You can validate your data by checking status and count columns (`Validation state`, `Validation pending`, `Validation failed`, `Validation suspended`, and `Validation details`) in the **Table statistics** tab of your database migration task on the **Tasks **page of the AWS DMS console. For more information, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html) in the AWS DMS documentation. | DBA |
| Stop the AWS DMS tasks. | Run the Python script by using the following command:<pre>$ python dms-start-task.py stop</pre>AWS DMS tasks might stop with a `failed`status, depending on the validation status. For more information, see the next section. | DBA |

## Troubleshooting
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS SCT source and target test connections fail. | Configure the JDBC driver versions and VPC security group inbound rules to accept the incoming traffic. |
| Source or target endpoint test run fails. | Check if the endpoint settings and replication instance are in `Available` status. Check if the endpoint connection status is `Successful`. <br />For more information, see [How do I troubleshoot AWS DMS endpoint connectivity failures](https://aws.amazon.com/premiumsupport/knowledge-center/dms-endpoint-connectivity-failures/) in the AWS Support documentation. |
| Full-load run fails. | Check if the source and target databases have matching data types and sizes. <br />For more information, see [Troubleshooting migration tasks in AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html) in the AWS DMS documentation. |
| You encounter validation run errors. | Check if the table has a primary key because non-primary key tables are not validated.<br />If the table has a primary key and errors, check that the extra connection attribute in the source endpoint has `numberDataTypeScale=-2`.<br />For more information, see [Endpoint settings when using Oracle as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib), [OracleSettings](https://docs.aws.amazon.com/dms/latest/APIReference/API_OracleSettings.html), and [Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html#CHAP_Validating.Troubleshooting) in the AWS DMS documentation. |

## Related resources
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-with-aws-sct-and-aws-dms-using-aws-cli-and-aws-cloudformation-resources"></a>
+ [Installing and configuring AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html#CHAP_Installing.Procedure)
+ [Introduction to AWS DMS](https://www.youtube.com/watch?v=ouia1Sc5QGo) (video)
+ [Examples of CloudFormation stack operation commands for the AWS CLI and PowerShell](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-cli.html)
+ [Navigating the user interface of the AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)
+ [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ [Connecting to Oracle databases with AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html)
+ [Using a PostgreSQL database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)
+ [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html)
+ [Targets for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html)
+ [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html) (AWS CLI documentation)
+ [create-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html) (AWS CLI documentation)
+ [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html) (AWS CLI documentation)

## Attachments
<a name="attachments-5e041494-2e64-4f09-b6ec-0e0cba3a4972"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/5e041494-2e64-4f09-b6ec-0e0cba3a4972/attachments/attachment.zip)
