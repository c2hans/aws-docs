---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump.html
---

# Migrate an on-premises Oracle database to Amazon RDS for Oracle using Oracle Data Pump
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump"></a>

*Mohan Annam and Brian motzer, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-summary"></a>

This pattern describes how to migrate an Oracle database from an on-premises data center to an Amazon Relational Database Service (Amazon RDS) for Oracle DB instance by using Oracle Data Pump.

The pattern involves creating a data dump file from the source database, storing the file in an Amazon Simple Storage Service (Amazon S3) bucket, and then restoring the data to an Amazon RDS for Oracle DB instance. This pattern is useful when you encounter limitations using AWS Database Migration Service (AWS DMS) for the migration.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ The required permissions to create roles in AWS Identity and Access Management (IAM) and for an Amazon S3 multipart upload
+ The required permissions to export data from the source database
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Product versions**
+ Oracle Data Pump is available only for Oracle Database 10g Release 1 (10.1) and later versions.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-architecture"></a>

**Source technology stack**
+ On-premises Oracle databases

**Target technology stack**
+ Amazon RDS for Oracle
+ SQL client (Oracle SQL Developer)
+ An S3 bucket

**Source and target architecture**

![Amazon S3 multipart upload from an on-premises Oracle DB to Amazon RDS by using Oracle Data Pump.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d8d6e00f-753e-4ecc-80e5-e60e279a699b/images/1bb6095a-0a95-4469-be0e-7b7bd59b35ae.png)

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. In this pattern, IAM is used to create the roles and policies necessary for migrating data from Amazon S3 to Amazon RDS for Oracle.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) helps you move data and metadata from one database to another at high speeds. In this pattern, Oracle Data Pump is used to export the data dump (.dmp) file to the Oracle server, and to import it into Amazon RDS for Oracle. For more information, see [Importing data into Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.html#Oracle.Procedural.Importing.DataPump.S3) in the Amazon RDS documentation.
+ [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments. It interacts with both the on-premises Oracle database and Amazon RDS for Oracle to run the SQL commands required for exporting and importing data.

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-epics"></a>

### Create an S3 bucket
<a name="create-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the bucket. | To create the S3 bucket, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). | AWS systems administrator |

### Create the IAM role and assign policies
<a name="create-the-iam-role-and-assign-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure IAM permissions. | To configure permissions, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html#oracle-s3-integration.preparing). | AWS systems administrator |

### Create the target Amazon RDS for Oracle DB instance and associate the Amazon S3 integration role
<a name="create-the-target-amazon-rds-for-oracle-db-instance-and-associate-the-amazon-s3-integration-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the target Amazon RDS for Oracle DB instance. | To create the Amazon RDS for Oracle instance, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html). | AWS systems administrator |
| Associate the role with the DB instance. | To associate the role with the instance, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html#oracle-s3-integration.preparing.instance). | DBA |

### Create the database user on the target database
<a name="create-the-database-user-on-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the user. | Connect to the target Amazon RDS for Oracle database from Oracle SQL Developer or SQL\*Plus, and run the following SQL command to create the user to import the schema into.<pre>create user SAMPLE_SCHEMA identified by <PASSWORD>;<br />grant create session, resource to <USER NAME>;<br />alter user <USER NAME> quota 100M on users;</pre> | DBA |

### Create the export file from the source Oracle database
<a name="create-the-export-file-from-the-source-oracle-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a data dump file. | To create a dump file named `sample.dmp` in the `DATA_PUMP_DIR` directory for exporting the `SAMPLE_SCHEMA` user, use the following script.<pre>DECLARE<br />    hdnl NUMBER;<br />BEGIN<br />    hdnl := dbms_datapump.open(operation => 'EXPORT', <br />                                job_mode => 'SCHEMA', <br />                                job_name => NULL);<br /><br />    dbms_datapump.add_file( handle => hdnl, <br />                            filename => 'sample.dmp', <br />                            directory => 'DATA_PUMP_DIR', <br />                            filetype => dbms_datapump.ku$_file_type_dump_file);<br /><br />    dbms_datapump.add_file(handle => hdnl, <br />                            filename => 'export.log', <br />                            directory => 'DATA_PUMP_DIR', <br />                            filetype => dbms_datapump.ku$_file_type_log_file);<br /><br />    dbms_datapump.metadata_filter(hdnl, 'SCHEMA_EXPR', 'IN (''SAMPLE_SCHEMA'')');  <br /><br />    dbms_datapump.start_job(hdnl);<br />END;<br />/</pre><br />Review the export details by reviewing the `export.log` file in your local `DATA_PUMP_DIR` directory.  | DBA |

### Upload the dump file to the S3 bucket
<a name="upload-the-dump-file-to-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the data dump file from the source to the S3 bucket. | Using AWS CLI, run the following command.<pre>aws s3 cp sample.dmp s3://<bucket_created_epic_1>/</pre> | DBA |

### Download the export file from the S3 bucket to the RDS instance
<a name="download-the-export-file-from-the-s3-bucket-to-the-rds-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the data dump file to Amazon RDS | To copy the dump file `sample.dmp` from the S3 bucket to the Amazon RDS for Oracle database, run the following SQL command. In this example, the `sample.dmp` file is downloaded from the S3 bucket `my-s3-integration1` to the Oracle directory `DATA_PUMP_DIR`. Make sure that you have sufficient disk space allocated to your RDS instance to accommodate both the database and the export file.<pre>-- If you want to download all the files in the S3 bucket remove the p_s3_prefix line.<br /><br />SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(<br />      p_bucket_name    =>  'my-s3-integration',    <br />      p_s3_prefix => 'sample.dmp',<br />      p_directory_name =>  'DATA_PUMP_DIR') <br />   AS TASK_ID FROM DUAL;</pre><br />The previous command outputs a task ID. To review the status of the download by reviewing the data in the task ID, run the following command.<pre>SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-<task_id>.log'));<br /><br /></pre><br />To see the files in the `DATA_PUMP_DIR` directory, run the following command.<pre>SELECT filename,type,filesize/1024/1024 size_megs,to_char(mtime,'DD-MON-YY HH24:MI:SS') timestamp<br />FROM TABLE(rdsadmin.rds_file_util.listdir(p_directory => upper('DATA_PUMP_DIR'))) order by 4;</pre> | AWS systems administrator |

### Import the dump file into the target database
<a name="import-the-dump-file-into-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restore the schema and data to Amazon RDS. | To import the dump file into the `sample_schema` database schema, run the following SQL command from SQL Developer or SQL\*Plus.<pre>DECLARE<br />hdnl NUMBER;<br />BEGIN<br /><br />hdnl := DBMS_DATAPUMP.OPEN( operation => 'IMPORT', job_mode => 'SCHEMA', job_name=>null);<br /><br />DBMS_DATAPUMP.ADD_FILE( handle => hdnl, filename => 'sample.dmp', directory => 'DATA_PUMP_DIR', filetype => dbms_datapump.ku$_file_type_dump_file);<br /><br />DBMS_DATAPUMP.ADD_FILE( handle    => hdnl, filename  => 'import.log', directory => 'DATA_PUMP_DIR', filetype  => dbms_datapump.ku$_file_type_log_file);<br /><br />DBMS_DATAPUMP.METADATA_FILTER(hdnl,'SCHEMA_EXPR','IN (''SAMPLE_SCHEMA'')');<br /><br />DBMS_DATAPUMP.START_JOB(hdnl);<br /><br />END;<br />/</pre><br />To see the log file from the import, run the following command.<pre>SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('DATA_PUMP_DIR','import.log'));</pre> | DBA |

### Remove the dump file from the DATA\_PUMP\_DIR directory
<a name="remove-the-dump-file-from-the-data_pump_dir-directory"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| List and clean up the export files. | List and remove the export files in the `DATA_PUMP_DIR` directory, run the following commands.<pre>-- List the files<br />SELECT filename,type,filesize/1024/1024 size_megs,to_char(mtime,'DD-MON-YY HH24:MI:SS') timestamp FROM TABLE(rdsadmin.rds_file_util.listdir(p_directory => upper('DATA_PUMP_DIR'))) order by 4;</pre><pre>-- Remove the files<br />EXEC UTL_FILE.FREMOVE('DATA_PUMP_DIR','sample.dmp');<br />EXEC UTL_FILE.FREMOVE('DATA_PUMP_DIR','import.log');</pre> | AWS systems administrator |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump-resources"></a>
+ [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html#oracle-s3-integration.preparing)
+ [Create a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)
+ [Importing data into Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.html#Oracle.Procedural.Importing.DataPump.S3)
+ [Amazon S3 documentation](https://docs.aws.amazon.com/s3/index.html)
+ [IAM documentation](https://docs.aws.amazon.com/iam/index.html)
+ [Amazon RDS documentation](https://docs.aws.amazon.com/rds/index.html)
+ [Oracle Data Pump documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html)
+ [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/)
