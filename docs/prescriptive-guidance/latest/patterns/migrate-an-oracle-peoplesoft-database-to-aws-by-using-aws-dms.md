---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms.html
---

# Migrate an Oracle PeopleSoft database to AWS by using AWS DMS
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms"></a>

*sampath kathirvel, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-summary"></a>

[Oracle PeopleSoft](https://www.oracle.com/applications/peoplesoft/) is an enterprise resource planning (ERP) solution for enterprise-wide processes. PeopleSoft has a three-tier architecture: client, application, and database. PeopleSoft can be run on [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

If you migrate your Oracle database to Amazon RDS, Amazon Web Services (AWS) can take care of backup tasks and high availability, leaving you free to concentrate on maintaining your PeopleSoft application and its functionality. For a comprehensive list of key factors to consider during the migration process, see [Oracle database migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/strategies.html) in AWS Prescriptive Guidance.

This pattern provides a solution for migrating your on-premises Oracle databases to Amazon RDS for Oracle using Oracle Data Pump with [AWS Database Migration Service (AWS DMS)](http://aws.amazon.com/dms) and its change data capture (CDC) feature.

When migrating critical ERP applications such as Oracle PeopleSoft, minimizing the downtime is key. AWS DMS minimizes downtime by supporting both full load and continuous replication. from the source database to the target database. AWS DMS also provides real-time monitoring and logging of the migration, which can help you to identify and resolve any issues that could cause downtime.

When replicating changes with AWS DMS, you must specify a time or system change number (SCN) as the starting point for AWS DMS to read changes from the database logs. It's crucial to keep these logs accessible on the server for a designated amount of time to ensure that AWS DMS has access to these changes.

## Prerequisites and limitations
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-prereqs"></a>

**Prerequisites**
+ Provisioned Amazon RDS for Oracle database in your AWS Cloud environment as the target database.
+ An Oracle PeopleSoft database running on premises or on Amazon Elastic Compute Cloud (Amazon EC2) in the AWS Cloud.
**Note**
This pattern is designed for migrating from on premises to AWS, but it was tested by using Oracle Database on an Amazon EC2 instance. For migrating from on premises, you will need to configure the appropriate network connectivity.
+ Schema details. When migrating an Oracle PeopleSoft application to Amazon RDS for Oracle, it is necessary to identify which Oracle database schema (for example, `SYSADM`) to migrate. Before starting the migration process, gather the following details about the schema:
  + Size
  + The number of objects per object type
  + The number of invalid objects.

  This information will aid in the migration process.

**Limitations**
+ This scenario has been tested only with the PeopleSoft DEMO database. It hasn’t been tested with a large dataset.

## Architecture
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-architecture"></a>

The following diagram shows an instance running an Oracle database as the source database and an Amazon RDS for Oracle database as the target database. The data is exported and imported from the source Oracle database to the target Amazon RDS for Oracle database using Oracle Data Pump and replicated for CDC changes using AWS DMS.

![Five-step process from on-premises DB instance to Amazon RDS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c8ec3789-f80e-4f3a-a3f4-72a4541316b0/images/4e3e3477-2fe0-4a5d-b95e-05a8aafe8b68.png)

1. The initial step involves extracting data from the source database by using Oracle Data Pump, followed by sending it to the Amazon RDS for Oracle database target.

1. Data is sent from the source database to a source endpoint in AWS DMS.

1. From the source endpoint, the data is sent to the AWS DMS replication instance, where the replication task is performed.

1. After the replication task is completed, the data is sent to the target endpoint in AWS DMS.

1. From the target endpoint, the data is sent to the Amazon RDS for Oracle database instance.

## Tools
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.

**Other services**
+ [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) helps you move data and metadata from one database to another at high speeds.

## Best practices
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-best-practices"></a>

**Migrating LOBs**

If your source database contains large binary objects (LOBs) that need to be migrated to the target database, AWS DMS provides the following options:
+ **Full LOB mode** – AWS DMS migrates all the LOBs from the source to the target database regardless of their size. Although the migration is slower, the advantage is that data isn’t truncated. For better performance, you can create a separate task on the new replication instance to migrate the tables that have LOBs larger than a few megabytes.
+ **Limited LOB mode** – You specify the maximum size of LOB column data, which allows AWS DMS to pre-allocate resources and apply the LOBs in bulk. If the size of the LOB columns exceeds the size that is specified in the task, AWS DMS truncates the data and sends warnings to the AWS DMS log file. You can improve performance by using Limited LOB mode if your LOB data size is within the Limited LOB size.
+ **Inline LOB mode** – You can migrate LOBs without truncating the data or slowing the performance of your task by replicating both small and large LOBs. First, specify a value for the InlineLobMaxSize parameter, which is available only when Full LOB mode is set to true. The AWS DMS task transfers the small LOBs inline, which is more efficient. Then, AWS DMS migrates the large LOBs by performing a lookup from the source table. However, Inline LOB mode works only during the full load phase.

**Generating sequence values**

Keep in mind that during the change data capture process with AWS DMS, incremental sequence numbers are not replicated from the source database. To avoid discrepancies in sequence values, you must generate the most recent sequence value from the source for all sequences, and apply it to the target Amazon RDS for Oracle database.

**Credential management**

To help secure your AWS resources, we recommend following the [best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) for AWS Identity and Access Management (IAM).

## Epics
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-epics"></a>

### Provision an AWS DMS replication instance with the source and target endpoints
<a name="provision-an-aws-dms-replication-instance-with-the-source-and-target-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the template. | Download the [DMS\_instance.yaml](https://aws-database-blog.s3.amazonaws.com/artifacts/Migrating_oracle_using_DMS/DMS_Instance.yaml) AWS CloudFormation template to provision the AWS DMS replication instance and its source and target endpoints. | Cloud administrator, DBA |
| Start the stack creation. | 1. On the AWS Management Console, choose **CloudFormation**.<br />2. Choose **Create stack**.<br />3. For **Specify template**, choose **Upload a template file**.<br />4. Choose **Choose file**.<br />5. Choose the `DMS_instance.yaml` file.<br />6. Choose **Next**. | Cloud administrator, DBA |
| Specify the parameters. | 1. For **Stack name**, enter your stack name.<br />2. Under **AWS DMS Instance Parameters**, enter the following parameters:**DMSInstanceType** – Choose the required instance for the AWS DMS replication instance, based on your business needs.**DMSStorageSize** – Enter the storage size for the AWS DMS instance, based on the size of your migration.<br />3. Under **Source Oracle Database Configuration**, enter the following parameters:**SourceOracleEndpointID** – The source Oracle database server name**SourceOracleDatabaseName** – The source database service name or session ID (SID) as applicable**SourceOracleUserName** – The source database username (the default is system)**SourceOracleDBPassword** – The source database username’s password**SourceOracleDBPort** – The source database port<br />4. Under **Target RDS for Oracle Database Configuration**, enter the following parameters:**TargetRDSOracleEndpointID** – The target RDS database endpoint**TargetRDSOracleDatabaseName** – The target RDS database name**TargetRSOracleUserName** – The target RDS username**TargetRDSOracleDBPassword** – The target RDS password**TargetOracleDBPort** – The target RDS database port<br />5. Under **VPC, Subnet and Security Group Configuration**, enter the following parameters:**VPCID** – The VPC for the replication instance**VPCSecurityGroupId** – The VPC security group for the replication instance**DMSSubnet1** – The subnet for Availability Zone 1**DMSSubnet2** – The subnet for Availability Zone 2<br />6. Choose **Next**. | Cloud administrator, DBA |
| Create the stack. | 1. On the **Configure stack options** page, for **Tags**, enter any optional values.<br />2. Choose **Next**.<br />3. On the **Review** page, verify the details, and then choose **Submit**.The provisioning should complete in approximately 5–10 minutes. It is complete when the AWS CloudFormation Stacks page shows **CREATE\_COMPLETE**. | Cloud administrator, DBA |
| Set up the endpoints. | 1. From the AWS Management Console, choose **Database Migration Services**.<br />2. Under Resource management, choose **Replication instances**.<br />3. Under Resource management, choose **Endpoints**. | Cloud administrator, DBA |
| Test connectivity. | After the source and target endpoints shows status as Active, test the connectivity. Choose **Run test** for each endpoint (source and target) to make sure that the status shows as successful. | Cloud administrator, DBA |

### Export the PeopleSoft schema from the on-premises Oracle database by using Oracle Data Pump
<a name="export-the-peoplesoft-schema-from-the-on-premises-oracle-database-by-using-oracle-data-pump"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate the SCN. | When the source database is active and in use by the application, initiate the data export with Oracle Data Pump. You must first generate a system change number (SCN) from the source database for both data consistency during the export with Oracle Data Pump and as a starting point for change data capture in AWS DMS.<br />To generate the current SCN from your source database, enter the following SQL statement.<pre>SQL> select name from v$database;<br />SQL> select name from v$database;<br />NAME<br />---------<br />PSFTDMO<br />SQL> SELECT current_scn FROM v$database;<br />CURRENT_SCN<br />-----------<br />23792008</pre><br />Save the generated SCN to use when you export the data and for creating the AWS DMS replication task. | DBA |
| Create the parameter file. | To create a parameter file for exporting the schema, you can use the following code.<pre>$ cat exp_datapmp.par<br />userid=system/*******<br />directory=DATA_PUMP_DIR<br />logfile=export_dms_sample_user.log<br />dumpfile=export_dms_sample_data_%U.dmp<br />schemas=SYSADM<br />flashback_scn=23792008</pre>You can also define your own `DATA_PUMP_DIR` by using the following commands, based on your requirements.<pre>SQL> CREATE OR REPLACE DIRECTORY DATA_PUMP_DIR AS '/opt/oracle/product/19c/dbhome_1/dmsdump/';<br />Directory created.<br />SQL> GRANT READ, WRITE ON DIRECTORY DATA_PUMP_DIR TO system;<br />Grant succeeded.<br />SQL><br />SQL> SELECT owner, directory_name, directory_path FROM dba_directories WHERE directory_name='DATA_PUMP_DIR';<br />OWNER DIRECTORY_NAME DIRECTORY_PATH<br />------------------------------------------------------------------------------------------------------------------<br />SYS DATA_PUMP_DIR /opt/oracle/product/19c/dbhome_1/dmsdump/</pre> | DBA |
| Export the schema. | To perform the export, use the `expdp` utility.<pre>$ expdp parfile=exp_datapmp.par<br />.......................<br />Transferring the dump file with DBMS_FILE_TRANSFER to Target:<br />. . exported "SYSADM"."PS_XML_TEMPLT_LNG" 6.320 KB 0 rows<br />. . exported "SYSADM"."PS_XML_TEMPLT_LNK" 6.328 KB 0 rows<br />. . exported "SYSADM"."PS_XML_XLATDEF_LNG" 6.320 KB 0 rows<br />. . exported "SYSADM"."PS_XML_XLATITM_LNG" 7.171 KB 0 rows<br />. . exported "SYSADM"."PS_XPQRYRUNCNTL" 7.601 KB 0 rows<br />. . exported "SYSADM"."PS_XPQRYRUNPARM" 7.210 KB 0 rows<br />. . exported "SYSADM"."PS_YE_AMOUNTS" 9.351 KB 0 rows<br />. . exported "SYSADM"."PS_YE_DATA" 16.58 KB 0 rows<br />. . exported "SYSADM"."PS_YE_EE" 6.75 KB 0 rows<br />. . exported "SYSADM"."PS_YE_W2CP_AMOUNTS" 9.414 KB 0 rows<br />. . exported "SYSADM"."PS_YE_W2CP_DATA" 20.94 KB 0 rows<br />. . exported "SYSADM"."PS_YE_W2C_AMOUNTS" 10.27 KB 0 rows<br />. . exported "SYSADM"."PS_YE_W2C_DATA" 20.95 KB 0 rows<br />. . exported "SYSADM"."PS_ZBD_JOBCODE_TBL" 14.60 KB 0 rows<br />. . exported "SYSADM"."PTGRANTTBL" 5.468 KB 0 rows<br />Master table "SYSTEM"."SYS_EXPORT_SCHEMA_01" successfully loaded/unloaded<br />**<br />Dump file set for SYSTEM.SYS_EXPORT_SCHEMA_01 is:<br />/opt/oracle/product/19c/dbhome_1/dmsdump/export_dms_sample_data_01.dmp<br />Job "SYSTEM"."SYS_EXPORT_SCHEMA_01" successfully completed at Mon Dec 19 20:13:57 2022 elapsed 0 00:38:22</pre> | DBA |

### Import the PeopleSoft schema into the Amazon RDS for Oracle database by using Oracle Data Pump
<a name="import-the-peoplesoft-schema-into-the-amazon-rds-for-oracle-database-by-using-oracle-data-pump"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Transfer the dump file to the target instance. | To transfer your files using `DBMS_FILE_TRANSFER`, you need to create a database link from the source database to the Amazon RDS for Oracle instance. After the link is established, you can use the utility to transfer the Data Pump files directly to the RDS instance.<br />Alternatively, you can transfer the Data Pump files to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) and then import them into the Amazon RDS for Oracle instance. For more information about this option, see the Additional information section.<br />To create a database link `ORARDSDB` that connects to the Amazon RDS master user at the target DB instance, run the following commands on the source database.<pre>$sqlplus / as sysdba<br />$ SQL> create database link orardsdb connect to admin identified by "*****" using '(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = testpsft.*******.us-west-2.rds.amazonaws.com)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = orcl)))';<br />Database link created.</pre> | DBA |
| Test the database link. | Test the database link to make sure that you can connect using sqlplus to the Amazon RDS for Oracle target database.<pre>SQL><br />SQL> select name from v$database@orardsdb;<br />NAME<br />---------<br />ORCL<br />SQL></pre> | DBA |
| Transfer the dump file to the target database. | To copy the dump file over to Amazon RDS for Oracle database, you can either use the default `DATA_PUMP_DIR` directory or you can create your own directory using the following code.<pre>exec rdsadmin.rdsadmin_util.create_directory(p_directory_name => ‘TARGET_PUMP_DIR’);</pre><br />The following script copies a dump file named `export_dms_sample_data_01.dmp` from the source instance to a target Amazon RDS for Oracle database using the database link named `orardsdb`.<pre>$ sqlplus / as sysdba<br />SQL><br />BEGIN<br />DBMS_FILE_TRANSFER.PUT_FILE(<br />source_directory_object => 'DATA_PUMP_DIR',<br />source_file_name => 'export_dms_sample_data_01.dmp',<br />destination_directory_object => 'TARGET_PUMP_DIR’',<br />destination_file_name => 'export_dms_sample_data_01.dmp',<br />destination_database => 'orardsdb'<br />);<br />END;<br />/<br />PL/SQL procedure successfully completed.</pre> | DBA |
| List the dump file in the target database. | After the PL/SQL procedure is completed, you can list the data dump file in the Amazon RDS for Oracle database by using the following code.<pre>SQL> select * from table (rdsadmin.rds_file_util.listdir(p_directory => ‘TARGET_PUMP_DIR’));</pre> | DBA |
| Initiate the import on the target database. | Before you start the import process, set up the roles, schemas, and tablespaces on the target Amazon RDS for Oracle database by using the data dump file.<br />To perform the import, access the target database with the Amazon RDS master user account, and use the connection string name in the `tnsnames.ora` file, which includes the Amazon RDS for Oracle Database `tns-entry`. If necessary, you can include a remap option to import the data dump file into a different tablespace or under a different schema name.<br />To start the import, use the following code.<pre>impdp admin@orardsdb directory=TARGET_PUMP_DIR logfile=import.log dumpfile=export_dms_sample_data_01.dmp</pre><br />To ensure a successful import, check the import log file for any errors, and review details such as object count, row count, and invalid objects. If there are any invalid objects, recompile them. Additionally, compare the source and target database objects to confirm that they match. | DBA |

### Create an AWS DMS replication task using CDC to perform live replication
<a name="create-an-aws-dms-replication-task-using-cdc-to-perform-live-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the replication task. | Create the AWS DMS replication task by using the following steps:1. On the AWS DMS console, under **Conversion & migration**, choose **Database migration task**.<br />2. Under **Task configuration**, for **Task identifier**, enter your task identifier.<br />3. For **Replication instance**, choose the DMS replication instance that you created.<br />4. For **Source database endpoint**, choose your source endpoint.<br />5. For **Target database endpoint**, choose your target Amazon RDS for Oracle database.<br />6. For **Migration type**, choose **Replicate data changes only**. If you receive a message that supplemental logging needs to be turned on, follow the instructions in the *Additional information* section.<br />7. Under **Task settings**, select **Specify log sequence number**.<br />8. For **System change number**, enter the Oracle database SCN that you generated from the source Oracle database.<br />9. Choose **Enable validation**.<br />10. Choose **Enable CloudWatch Logs**.<br />By activating this feature, you can validate the data and [Amazon CloudWatch](http://aws.amazon.com/cloudwatch) logs to review the AWS DMS replication instance logs.<br />11. Under **Selection rules**, complete the following:For **Schema**, choose **Enter a schema**.For **Schema name**, enter **SYSADM**.For **Table name**, enter **%**.For **Action**, choose **Include**.<br />12. Under **Transformation rules**, complete the following:For **Target**, choose **Table**.For **Scheme name**, choose **Enter a schema**.For **Schema name**, enter SYSADM.For **Action**, choose **Rename to**.<br />13. Choose **Create task**.<br />After you create the task, it migrates the CDC to the Amazon RDS for Oracle database instance from the SCN that you provided under CDC start mode. You can also verify by reviewing the CloudWatch logs. | Cloud administrator, DBA |

### Validate the database schema on the target Amazon RDS for Oracle database
<a name="validate-the-database-schema-on-the-target-amazon-rds-for-oracle-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the data transfer. | After the AWS DMS task starts, you can check the **Table statistics** tab on the **Tasks** page to see the changes made to the data.<br />You can monitor the status of ongoing replication in the console on the **Database migration tasks** page.<br />For more information, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html). | Cloud administrator, DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop replication. | Discontinue the replication procedure and halt the source application services. | Cloud administrator, DBA |
| Launch the PeopleSoft middle tier. | Launch the target PeopleSoft middle tier application in AWS, and direct it to the recently migrated Amazon RDS for Oracle database.<br />When you access the application, you should notice that all app connections are now established with the Amazon RDS for Oracle database. | DBA, PeopleSoft administrator |
| Turn off the source database. | After you confirm that there are no more connections to the source database, it can be turned off. | DBA |

## Related resources
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-resources"></a>
+ [Getting started with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)
+ [Best Practices for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html)
+ [Migrating Oracle Databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html)

## Additional information
<a name="migrate-an-oracle-peoplesoft-database-to-aws-by-using-aws-dms-additional"></a>

**Transfer files using Amazon S3**

To transfer the files to Amazon S3, you can use the AWS CLI or the Amazon S3 console. After you transfer the files to Amazon S3, you can use the Amazon RDS for Oracle instance to import the Data Pump files from Amazon S3.

If you choose to transfer the dump file using Amazon S3 integration as an alternate method, perform the follow steps:

1. Create an S3 bucket.

1. Export the data from the source database using Oracle Data Pump.

1. Upload the Data Pump files to the S3 bucket.

1. Download the Data Pump files from the S3 bucket to the target Amazon RDS for Oracle database.

1. Perform the import using the Data Pump files.

**Note**
To transfer large data files between S3 and RDS instances, it is recommended to use the Amazon S3 Transfer Acceleration feature.

**Activate supplemental logging**

If you receive a warning message to enable [supplemental logging](https://docs.oracle.com/database/121/SUTIL/GUID-D2DDD67C-E1CC-45A6-A2A7-198E4C142FA3.htm#SUTIL1583) in the source database for on-going replication, use the following steps.

```
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (UNIQUE) COLUMNS;
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (FOREIGN KEY) COLUMNS;
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (UNIQUE) COLUMNS;
```
