---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms.html
---

# Migrate an Oracle JD Edwards EnterpriseOne database to AWS by using Oracle Data Pump and AWS DMS
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms"></a>

*Thanigaivel Thirumalai, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-summary"></a>

You can migrate and run your JD Edwards EnterpriseOne database on [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html). When you migrate your database to Amazon RDS, AWS can take care of backup tasks and high availability setup, so you can concentrate on maintaining your EnterpriseOne application and its functionality. For a comprehensive list of key factors to consider during the migration process, see [Oracle database migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/strategies.html) in AWS Prescriptive Guidance.

There are multiple ways to migrate an EnterpriseOne database, including:
+ Using Oracle Universal Batch Engine (UBE) R98403 for schema and table creation, and using AWS Database Migration Service (AWS DMS) for migration
+ Using DB native tools for schema and table creation and using AWS DMS for migration
+ Using DB native tools for the migration of existing data (full load) and using AWS DMS for change data capture (CDC) tasks

This pattern covers the third option. It explains how to migrate your on-premises EnterpriseOne databases to Amazon RDS for Oracle by using Oracle Data Pump with [AWS DMS](https://aws.amazon.com/dms) and its CDC feature.

[Oracle JD Edwards EnterpriseOne](https://www.oracle.com/applications/jd-edwards-enterpriseone/) is an enterprise resource planning (ERP) solution for organizations that manufacture, construct, distribute, service, or manage products or physical assets. JD Edwards EnterpriseOne supports various hardware, operating systems, and database platforms.

When you migrate critical ERP applications such as JD Edwards EnterpriseOne, minimizing downtime is key. AWS DMS minimizes downtime by supporting both full load and continuous replication from the source database to the target database. AWS DMS also provides real-time monitoring and logging for the migration, which can help you identify and resolve any issues that could cause downtime.

When you replicate changes with AWS DMS, you must specify a time or system change number (SCN) as the starting point for reading changes from the database logs. It's crucial to keep these logs accessible on the server for a designated amount of time (we recommend 15 days) to ensure that AWS DMS has access to these changes.

## Prerequisites and limitations
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-prereqs"></a>

**Prerequisites**
+ An Amazon RDS for Oracle database provisioned in your AWS Cloud environment as the target database. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html).
+ An EnterpriseOne database that’s running on premises or on an Amazon Elastic Compute Cloud (Amazon EC2) instance on AWS.
**Note**
This pattern is designed for migrating from on premises to AWS, but it was tested by using an EnterpriseOne database on an EC2 instance. If you plan to migrate from your on-premises environment, you must configure the appropriate network connectivity.
+ Schema details. Identify which Oracle database schema (for example, DV920) you plan to migrate for EnterpriseOne. Before you start the migration process, gather the following details about the schema:
  + Schema size
  + The number of objects per object type
  + The number of invalid objects

**Limitations**
+ You have to create any schemas you want on the target Amazon RDS for Oracle database―AWS DMS doesn't create these for you. (The [Epics](#migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-epics) section describes how to use Data Pump to export and import schemas.) The schema name must already exist for the target Oracle database. Tables from the source schema are imported to the user or the schema, and AWS DMS uses the administrator or system account to connect to the target instance. To migrate multiple schemas, you can create multiple replication tasks. You can also migrate data to different schemas on a target instance. To do this, use schema transformation rules on the AWS DMS table mappings.
+ This pattern has been tested with a demo dataset. We recommend that you validate compatibility for your dataset and customization.
+ This pattern uses an EnterpriseOne database that’s running on Microsoft Windows. However, you can use the same process with other operating systems that are supported by AWS DMS.

## Architecture
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-architecture"></a>

The following diagram shows a system that’s running EnterpriseOne on an Oracle database as the source database, and an Amazon RDS for Oracle database as the target database. The data is exported from the source Oracle database and imported into the target Amazon RDS for Oracle database by using Oracle Data Pump, and replicated for CDC updates by using AWS DMS.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c8ec3789-f80e-4f3a-a3f4-72a4541316b0/images/4e3e3477-2fe0-4a5d-b95e-05a8aafe8b68.png)

1. Oracle Data Pump extracts data from the source database, and the data is sent to the Amazon RDS for Oracle database target.

1. CDC data is sent from the source database to a source endpoint in AWS DMS.

1. From the source endpoint, the data is sent to the AWS DMS replication instance, where the replication task is performed.

1. After the replication task is complete, the data is sent to the target endpoint in AWS DMS.

1. From the target endpoint, the data is sent to the Amazon RDS for Oracle database instance.

## Tools
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.

**Other services**
+ [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) helps you move data and metadata from one database to another at high speed.

## Best practices
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-best-practices"></a>

**Migrating LOBs**

If your source database contains large binary objects (LOBs) that need to be migrated to the target database, AWS DMS provides the following options:
+ **Full LOB mode** – AWS DMS migrates all the LOBs from the source to the target database regardless of their size. Although the migration is slower than the other modes, the advantage is that data isn’t truncated. For better performance, you can create a separate task on the new replication instance to migrate the tables that have LOBs that are larger than a few megabytes.
+ **Limited LOB mode** – You specify the maximum size of LOB column data, which allows AWS DMS to pre-allocate resources and apply the LOBs in bulk. If the size of the LOB columns exceeds the size that is specified in the task, AWS DMS truncates the data and sends warnings to the AWS DMS log file. You can improve performance by using limited LOB mode if your LOB data size is within the limited LOB size.
+ **Inline LOB mode** – You can migrate LOBs without truncating the data or slowing the performance of your task by replicating both small and large LOBs. First, specify a value for the `InlineLobMaxSize` parameter, which is available only when full LOB mode is set to `true`. The AWS DMS task transfers the small LOBs inline, which is more efficient. Then, AWS DMS migrates the large LOBs by performing a lookup from the source table. However, inline LOB mode works only during the full load phase.

**Generating sequence values**

During the AWS DMS CDC process, incremental sequence numbers aren’t replicated from the source database. To avoid discrepancies in sequence values, you must generate the most recent sequence value from the source for all sequences, and apply it to the target Amazon RDS for Oracle database.

**AWS Secrets Manager**

To help manage your credentials, we recommend that you follow the instructions in the blog post [Manage your AWS DMS endpoint credentials with AWS Secrets Manager](https://aws.amazon.com/blogs/database/manage-your-aws-dms-endpoint-credentials-with-aws-secrets-manager/).

**Performance**
+ **Replication instances** ‒ For guidance on choosing the best instance size, see [Selecting the best size for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html) in the AWS DMS documentation.
+ **Connectivity options** ‒ To avoid latency issues, we recommend that you choose the right connectivity option. AWS Direct Connect provides the shortest path to AWS resources, because it is a dedicated connection between your corporate data centers and AWS. While in transit, your network traffic remains on the AWS global network and never goes over the internet. This reduces the chance of hitting bottlenecks or unexpected increases in latency when compared with using VPN or the public internet.
+ **Network bandwidth** ‒ To optimize performance, verify that your network throughput is fast. If you are using a VPN tunnel between your on-premises source database and AWS DMS, ensure that the bandwidth is sufficient for your workload.
+ **Task parallelism** ‒ You can speed up data replication by loading multiple tables in parallel during full load. This pattern uses of RDBMS endpoints, so this option applies only to the full load process. Task parallelism is controlled by the `MaxFullLoadSubTasks` parameter, which determines how many full load sub-tasks are run in parallel. By default, this parameter is set to 8, which means that eight tables (if selected in table mapping) are loaded together during full mode. You can adjust this parameter in the full-load task settings section of the JSON script for the task.
+ **Table parallelism** ‒ AWS DMS also enables you to load a single large table by using multiple parallel threads. This is particularly useful for Oracle source tables that have billions of records as well as multiple partitions and subpartitions. If the source table isn’t partitioned, you can use column boundaries for parallel loads.
+ **Split loads** ‒ When you split loads across multiple tasks or AWS DMS instances, remember transaction boundaries when you capture changes.

## Epics
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-epics"></a>

### Use Oracle Data Pump to export the EnterpriseOne schema
<a name="use-oracle-data-pump-to-export-the-enterpriseone-schema"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate the SCN. | When the source database is active and in use by the EnterpriseOne application, initiate the data export with Oracle Data Pump. You must first generate a system change number (SCN) from the source database for both data consistency during the export with Oracle Data Pump and as a starting point for CDC in AWS DMS.<br />To generate the current SCN from your source database, use the following SQL statement:<pre>SQL> select current_scn from v$database;<br /><br />CURRENT_SCN<br />-----------<br />   30009727</pre><br />Save the generated SCN. You will use the SCN when you export the data and to create the AWS DMS replication task. | DBA |
| Create the parameter file. | To create a parameter file for exporting the schema, you can use the following code.<pre>directory=DMS_DATA_PUMP_DIR<br />logfile=export_dms.log<br />dumpfile=export_dms_data.dmp<br />schemas=<schema name><br />flashback_scn=<SCN from previous command></pre>You can also define your own `DATA_PUMP_DIR` by using the following commands, based on your requirements.<pre>SQL> CREATE OR REPLACE DIRECTORY DMS_DATA_PUMP_DIR AS '<Directory for dump>';<br />Directory created.<br /><br />SQL> GRANT READ, WRITE ON DIRECTORY DMS_DATA_PUMP_DIR TO SYSTEM;<br />Grant succeeded.</pre> | DBA |
| Export the schema. | To perform the export, use the `expdp` utility as follows:<pre>C:\Users\Administrator>expdp system/********@<DB Name> PARFILE='<Path to PAR file create above>'<br /><br />Export: Release 19.0.0.0.0 - Production on *** *** ** **:**:** ****<br />Version 19.3.0.0.0<br /><br />Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.<br /><br />Connected to: Oracle Database 19c Standard Edition 2 Release 19.0.0.0.0 - Production<br />Starting "SYSTEM"."SYS_EXPORT_SCHEMA_02":  system/********@<DB Name>PARFILE='E:\exp_dms_datapump.par'<br />Processing object type SCHEMA_EXPORT/TABLE/TABLE_DATA<br />Processing object type SCHEMA_EXPORT/TABLE/INDEX/STATISTICS/INDEX_STATISTICS<br />Processing object type SCHEMA_EXPORT/TABLE/STATISTICS/TABLE_STATISTICS<br />Processing object type SCHEMA_EXPORT/STATISTICS/MARKER<br />Processing object type SCHEMA_EXPORT/USER<br />Processing object type SCHEMA_EXPORT/ROLE_GRANT<br />Processing object type SCHEMA_EXPORT/DEFAULT_ROLE<br />Processing object type SCHEMA_EXPORT/TABLESPACE_QUOTA<br />Processing object type SCHEMA_EXPORT/PRE_SCHEMA/PROCACT_SCHEMA<br />Processing object type SCHEMA_EXPORT/TABLE/TABLE<br />Processing object type SCHEMA_EXPORT/TABLE/GRANT/OWNER_GRANT/OBJECT_GRANT<br />Processing object type SCHEMA_EXPORT/TABLE/INDEX/INDEX<br />Processing object type SCHEMA_EXPORT/TABLE/CONSTRAINT/CONSTRAINT<br />. . exported "<Schema Name>"."<Table Name>"                            228.9 MB  496397 rows</pre><pre>Master table "SYSTEM"."SYS_EXPORT_SCHEMA_02" successfully loaded/unloaded<br />******************************************************************************<br />Dump file set for SYSTEM.SYS_EXPORT_SCHEMA_02 is:<br />  E:\DMSDUMP\EXPORT_DMS_DATA.DMP<br />Job "SYSTEM"."SYS_EXPORT_SCHEMA_02" successfully completed at *** *** ** **:**:** **** elapsed 0 00:01:57</pre> | DBA |

### Use Oracle Data Pump to import the EnterpriseOne schema
<a name="use-oracle-data-pump-to-import-the-enterpriseone-schema"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Transfer the dump file to the target instance. | To transfer your files by using the `DBMS_FILE_TRANSFER` utility, you need to create a database link from the source database to the Amazon RDS for Oracle instance. After the link is established, you can use the utility to transfer the Data Pump files directly to the Amazon RDS instance.<br />Alternatively, you can transfer the Data Pump files to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) and then import them into the Amazon RDS for Oracle instance. For more information about this option, see the [Additional information](#migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-additional) section.<br />To create a database link `ORARDSDB` that connects to the Amazon RDS master user at the target DB instance, run the following commands on the source database:<pre>sqlplus / as sysdba<br /><br />SQL*Plus: Release 19.0.0.0.0 on *** *** ** **:**:** ****<br />Version 19.3.0.0.0<br /><br />Copyright (c) 1982, 2019, Oracle.  All rights reserved.<br /><br />Connected to:<br />Oracle Database 19c Standard Edition 2 Release 19.0.0.0.0<br />Version 19.3.0.0.0<br /><br />SQL> create database link orardsdb connect to admin identified by "******" using '(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = orcl.******.us-east-1.rds.amazonaws.com)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = orcl)))';<br /><br />Database link created.<br /><br />SQL></pre> | DBA |
| Test the database link. | Test the database link to make sure that you can connect to the Amazon RDS for Oracle target database by using `sqlplus`.<pre>SQL> select name from v$database@orardsdb;<br /><br />NAME<br />---------<br />ORCL<br /></pre> | DBA |
| Transfer the dump file to the target database. | To copy the dump file over to the Amazon RDS for Oracle database, you can either use the default `DATA_PUMP_DIR` directory or you can create your own directory by using the following code, which has to run on the target Amazon RDS instance:<pre>exec rdsadmin.rdsadmin_util.create_directory(p_directory_name => 'DMS_TARGET_PUMP_DIR');<br /><br />PL/SQL procedure successfully completed.</pre><br />The following script copies a dump file named `EXPORT_DMS_DATA.DMP` from the source instance to a target Amazon RDS for Oracle database by using the database link named `orardsdb`. You must run the script on the source database instance.<pre>BEGIN<br />DBMS_FILE_TRANSFER.PUT_FILE(<br />source_directory_object => 'DMS_DATA_PUMP_DIR',<br />source_file_name => 'EXPORT_DMS_DATA.DMP',<br />destination_directory_object => 'DMS_TARGET_PUMP_DIR',<br />destination_file_name => 'EXPORT_DMS_DATA.DMP',<br />destination_database => 'orardsdb');<br />END;<br /><br />PL/SQL procedure successfully completed.</pre> | DBA |
| List the dump file in the target database. | After the PL/SQL procedure is complete, you can list the data dump file in the Amazon RDS for Oracle database by using the following code:<pre>select * from table (rdsadmin.rds_file_util.listdir(p_directory => 'DMS_TARGET_PUMP_DIR'));</pre> | DBA |
| Create JDE-specific users in the target Instance. | Create a JD Edwards profile and role by using these commands in the target instance:<pre>SQL> CREATE PROFILE "JDEPROFILE" LIMIT IDLE_TIME 15;<br />Profile created.<br /><br />SQL> CREATE ROLE "JDE_ROLE";<br />Role created.<br /><br />SQL> CREATE ROLE "JDEADMIN";<br />CREATE ROLE "JDEUSER";<br />Role created.<br />Role created.</pre><br />Grant the required permissions to the role:<pre>SQL> GRANT CREATE ANY SEQUENCE TO JDE_ROLE;<br /> GRANT DROP ANY SEQUENCE TO JDE_ROLE;<br /> GRANT CREATE ANY TRIGGER TO JDE_ROLE;<br /> GRANT DROP ANY TRIGGER TO JDE_ROLE;<br /></pre> | DBA, JDE CNC |
| Create tablespaces in the target instance. | Create the required tablespaces in the target instance by using the following commands for the schemas that are involved in this migration:<pre>SQL> CREATE TABLESPACE <Tablespace Name for Tables>;<br />Tablespace created.<br /><br />SQL> CREATE TABLESPACE <Tablespace Name for Indexes>;<br />Tablespace created.</pre> | DBA, JDE CNC |
| Initiate the import on the target database. | Before you start the import process, set up the roles, schemas, and tablespaces on the target Amazon RDS for Oracle database by using the data dump file.<br />To perform the import, access the target database with the Amazon RDS primary user account, and use the connection string name in the `tnsnames.ora` file, which includes the Amazon RDS for Oracle Database `tns-entry`. If necessary, you can include a remap option to import the data dump file into a different tablespace or under a different schema name.<br />To start the import, use the following code:<pre>impdp admin@orardsdb directory=DMS_TARGET_PUMP_DIR logfile=import.log dumpfile=EXPORT_DMS_DATA.DMP</pre><br />To ensure a successful import, check the import log file for any errors, and review details such as object count, row count, and invalid objects. If there are any invalid objects, recompile them. Additionally, compare the source and target database objects to confirm that they match. | DBA |

### Provision an AWS DMS replication instance with the source and target endpoints
<a name="provision-an-aws-dms-replication-instance-with-the-source-and-target-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the template. | Download the AWS CloudFormation [DMS\_instance.yaml](https://aws-database-blog.s3.amazonaws.com/artifacts/Migrating_oracle_using_DMS/DMS_Instance.yaml) template to provision the AWS DMS replication instance and its source and target endpoints. | Cloud administrator, DBA |
| Start the stack creation. | 1. Sign in to the AWS Management Console, and open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation).<br />2. Choose **Create stack**.<br />3. For **Specify template**, choose **Upload a template file**.<br />4. Choose **Choose file**.<br />5. Choose the `DMS_instance.yaml` file.<br />6. Choose **Next**. | Cloud administrator, DBA |
| Specify the parameters. | 1. For **Stack name**, enter your stack name.<br />2. For **AWS DMS Instance Parameters**, enter the following parameters:**DMSInstanceType** – Choose the required instance for the AWS DMS replication instance, based on your business needs.**DMSStorageSize** – Enter the storage size for the AWS DMS instance, based on the size of your migration.<br />3. For **Source Oracle Database Configuration**, enter the following parameters:**SourceOracleEndpointID** – The source Oracle database server name**SourceOracleDatabaseName** – The source database service name or session ID (SID) as applicable**SourceOracleUserName** – The source database username (the default is `system`)**SourceOracleDBPassword** – The source database username’s password**SourceOracleDBPort** – The source database port<br />4. For **Target RDS for Oracle Database Configuration**, enter the following parameters:**TargetRDSOracleEndpointID** – The target RDS database endpoint**TargetRDSOracleDatabaseName** – The target RDS database name**TargetRSOracleUserName** – The target RDS username**TargetRDSOracleDBPassword** – The target RDS password**TargetOracleDBPort** – The target RDS database port<br />5. For **VPC, Subnet and Security Group Configuration**, enter the following parameters:**VPCID** – The VPC for the replication instance**VPCSecurityGroupId** – The VPC security group for the replication instance**DMSSubnet1** – The subnet for Availability Zone 1**DMSSubnet2** – The subnet for Availability Zone 2<br />6. Choose **Next**. | Cloud administrator, DBA |
| Create the stack. | 1. On the **Configure stack options** page, for **Tags**, enter any optional values.<br />2. Choose **Next**.<br />3. On the **Review** page, verify the details, and then choose **Submit**.The provisioning should complete in approximately 5–10 minutes. It is complete when the AWS CloudFormation Stacks page shows **CREATE\_COMPLETE**. | Cloud administrator, DBA |
| Set up the endpoints. | 1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).<br />2. For **Resource management**, choose **Replication instances**, and then review the replication instances.<br />3. For **Resource management**, choose **Endpoints**, and then review the endpoints. | Cloud administrator, DBA |
| Test connectivity. | After the source and target endpoints shows the status as **Active**, test the connectivity. Choose **Run test** for each endpoint (source and target) to make sure that the status shows as successful. | Cloud administrator, DBA |

### Create an AWS DMS replication task for live replication
<a name="create-an-aws-dms-replication-task-for-live-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the replication task. | Create the AWS DMS replication task by using the following steps:1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).<br />2. In the navigation pane, under **Migrate Data**, choose **Database migration task**.<br />3. In the **Task configuration** box, for **Task identifier**, enter your task identifier.<br />4. For **Replication instance**, choose the DMS replication instance that you created.<br />5. For **Source database endpoint**, choose your source endpoint.<br />6. For **Target database endpoint**, choose your target Amazon RDS for Oracle database.<br />7. For **Migration type**, choose **Replicate data changes only**. If you receive a message that supplemental logging needs to be turned on, follow the instructions in the [Troubleshooting](#migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-troubleshooting) section.<br />8. In the **Task settings** box, choose **Specify log sequence number**.<br />9. For **System change number**, enter the Oracle database SCN that you generated from the source Oracle database.<br />10. Choose **Enable validation**.<br />11. Choose **Enable CloudWatch Logs**.<br />By activating this feature, you can validate the data and [Amazon CloudWatch](http://aws.amazon.com/cloudwatch) logs to review the AWS DMS replication instance logs.<br />12. Under **Selection rules**, complete the following:For **Schema**, choose **Enter a schema**.For **Schema name**, enter the JDE Schema name (for example: **DV920**).For **Table name**, enter **%**.For **Action**, choose **Include**.<br />13. Choose **Create task**.<br />After you create the task, AWS DMS migrates ongoing changes to the Amazon RDS for Oracle database instance from the SCN that you provided under CDC start mode. You can also verify the migration by reviewing the CloudWatch logs. | Cloud administrator, DBA |
| Repeat the replication task. | Repeat the previous steps to create replication tasks for other JD Edwards schemas that are part of the migration. | Cloud administrator, DBA, JDE CNC administrator |

### Validate the database schema on the target Amazon RDS for Oracle database
<a name="validate-the-database-schema-on-the-target-amazon-rds-for-oracle-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the data transfer. | After the AWS DMS task starts, you can check the **Table statistics** tab on the **Tasks** page to see the changes made to the data.<br />You can monitor the status of ongoing replication in the console on the **Database migration tasks** page.<br />For more information, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html). | Cloud administrator, DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop replication. | Discontinue the replication procedure and stop the source application services. | Cloud administrator, DBA |
| Launch the JD Edwards application. | Launch the target JD Edwards presentation and logic tier application on AWS, and direct it to the Amazon RDS for Oracle database.<br />When you access the application, you should notice that all connections are now established with the Amazon RDS for Oracle database. | DBA, JDE CNC administrator |
| Turn off the source database. | After you confirm that there are no more connections, you can turn the source database off. | DBA |

## Troubleshooting
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| You receive a warning message to enable [supplemental logging](https://docs.oracle.com/database/121/SUTIL/GUID-D2DDD67C-E1CC-45A6-A2A7-198E4C142FA3.htm#SUTIL1583) in the source database for on-going replication | Enter these commands to enable supplemental logging:<pre>SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;<br />SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;<br />SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (UNIQUE) COLUMNS;<br />SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (FOREIGN KEY) COLUMNS;<br />SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;<br />SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (UNIQUE) COLUMNS;</pre> |
| AWS DMS has supplemental logging turned off. | Supplemental logging is turned off by default in AWS DMS. To turn it on for a source Oracle endpoint:1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).<br />2. Choose **Endpoints**.<br />3. Choose the Oracle source endpoint that you want to add supplemental logging to.<br />4. Choose **Modify**.<br />5. Choose **Advanced**, and then add the following code to the **Extra connection attributes** text box:<pre>addSupplementalLogging=Y</pre><br />6. Choose **Modify**. |
| Supplemental logging isn’t enabled at the CDB level. | 1. Enter this command:<pre>SQL> alter session set container = CDB$ROOT;<br /><br />Session altered.</pre><br />2. Repeat the steps to enable supplemental logging.  |
| You receive the error message: "Test Endpoint failed: Application-Status: 1020912, Application-Message: LogMiner is not supported in Oracle PDB environment Endpoint initialization failed." | If you encounter this error message, you can use Binary Reader instead of LogMiner.<br />Under **Endpoint settings**, add this line to the extra connection attributes for your source database:<pre>useLogMinerReader=N;useBfile=Y;</pre> |

## Related resources
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-resources"></a>
+ [Getting started with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)
+ [Best Practices for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html)
+ [Migrating Oracle Databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html)
+ [AWS Database Migration Service resource type reference for AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html)
+ [Manage your AWS DMS endpoint credentials with AWS Secrets Manager](https://aws.amazon.com/blogs/database/manage-your-aws-dms-endpoint-credentials-with-aws-secrets-manager/)
+ [Troubleshooting migration tasks in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.Oracle.RecordsMissing)
+ [Best practices for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html)

## Additional information
<a name="migrate-an-oracle-jd-edwards-enterpriseone-database-to-aws-by-using-oracle-data-pump-and-aws-dms-additional"></a>

**Transfer files using Amazon S3**

To transfer the files to Amazon S3, you can use the AWS CLI or the Amazon S3 console. After you transfer the files to Amazon S3, you can use the Amazon RDS for Oracle instance to import the Data Pump files from Amazon S3.

If you choose to transfer the dump file using Amazon S3 integration as an alternate method, perform the follow steps:

1. Create an S3 bucket.

1. Export the data from the source database using Oracle Data Pump.

1. Upload the Data Pump files to the S3 bucket.

1. Download the Data Pump files from the S3 bucket to the target Amazon RDS for Oracle database.

1. Perform the import using the Data Pump files.

**Note**
To transfer large data files between S3 and RDS instances, we recommend that you use the [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html) feature.
