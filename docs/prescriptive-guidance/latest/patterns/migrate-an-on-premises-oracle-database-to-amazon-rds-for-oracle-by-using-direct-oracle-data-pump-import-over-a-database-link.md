---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link.html
---

# Migrate an Oracle database to Amazon RDS using direct Oracle Data Pump Import over a database link
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link"></a>

*Rizwan Wangde, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-summary"></a>

Numerous patterns cover migrating on-premises Oracle databases to Amazon Relational Database Service (Amazon RDS) for Oracle by using Oracle Data Pump, a native Oracle utility that is the preferred way to migrate large Oracle workloads. These patterns typically involve exporting application schemas or tables into dump files, transferring the dump files to a database directory on Amazon RDS for Oracle, and then importing the application schemas and data from the dump files.

Using that approach, a migration can take longer depending on the size of the data and the time that it takes to transfer the dump files to the Amazon RDS instance. In addition, the dump files reside on the Amazon RDS instance's Amazon Elastic Block Store (Amazon EBS) volume, which must be large enough for the database and the dump files. When the dump files are deleted after import, the empty space cannot be retrieved, so you continue to pay for unused space.

This pattern mitigates those issues by performing a direct import on the Amazon RDS instance by using the Oracle Data Pump API (`DBMS_DATAPUMP`) over a database link. The pattern initiates a simultaneous export and import pipeline between the source and target databases. This pattern doesn't require sizing an EBS volume for the dump files because no dump files are created or stored on the volume. This approach saves** **the monthly cost of unused disk space.

## Prerequisites and limitations
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account.
+ A virtual private cloud (VPC) configured with private subnets across at least two Availability Zones, to provide the network infrastructure for the Amazon RDS instance.
+ An Oracle database in an on-premises data center, or self-managed on Amazon Elastic Compute Cloud (Amazon EC2).
+ An existing Amazon RDS for Oracle instance in a single Availability Zone. Using a single Availability Zone improves write performance during migration. A Multi-AZ deployment can be enabled 24–48 hours before cutover.

  This solution can also use Amazon RDS Custom for Oracle as a target.
+ AWS Direct Connect (recommended for large sized databases).
+ Network connectivity and firewall rules on premises configured to allow an inbound connection from the Amazon RDS instance to the on-premises Oracle database.

**Limitations **
+ The database size limit on Amazon RDS for Oracle is 64 tebibytes (TiB) as of December 2022.
+ The maximum size of a single file on an Amazon RDS for Oracle DB instances is 16 TiB. This is important to know because you might need to spread tables across multiple tablespaces.

**Product versions**
+ Source database: Oracle Database version 10g Release 1 and later.
+ Target database: For the latest list of supported versions and editions on Amazon RDS, see [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.database-versions.html) in the AWS documentation.

## Architecture
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-architecture"></a>

**Source technology stack  **
+ Self-managed Oracle database on premises or in the cloud

**Target technology stack  **
+ Amazon RDS for Oracle or Amazon RDS Custom for Oracle

**Target architecture **

The following diagram shows the architecture for migrating from an on-premises Oracle database to Amazon RDS for Oracle in a Single-AZ environment. The arrow directions depict the data flow in the architecture. The diagram doesn't show what component is initiating the connection.

![Full-load migration for an on-premises Oracle database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d54e7777-dcd2-4039-9b76-97e1019ef112/images/78429a29-e110-485a-a501-9764decd7e92.png)

1. The Amazon RDS for Oracle instance connects to the on-premises source Oracle database to perform a full-load migration over the database link.

1. AWS Database Migration Service (AWS DMS) connects to the on-premises source Oracle database to perform ongoing replication by using change data capture (CDC).

1. CDC changes are applied to the Amazon RDS for Oracle database.

## Tools
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups. This pattern uses CDC and the **Replicate data changes only** setting.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.

**Other tools**
+ [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) helps you move data and metadata from one database to another at high speeds.
+ Client tools such as [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) or [SQL Developer](https://www.oracle.com/database/sqldeveloper/) are used to connect and run SQL queries on the database.

## Best practices
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-best-practices"></a>

Although Direct Connect uses dedicated, private network connections between the on-premises network and AWS, consider the following options for additional security and data encryption for data in transit:
+ [A virtual private network (VPN) using AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) or an IPsec VPN connection from the on-premises network to the AWS network
+ [Oracle Database Native Network Encryption](https://docs.oracle.com/en/database/oracle/oracle-database/18/dbseg/configuring-network-data-encryption-and-integrity.html#GUID-50817699-B199-49CA-8779-137EBC4B0564) configured on the on-premises Oracle database
+ Encryption using [TLS](https://docs.oracle.com/database/121/DBSEG/asossl.htm#DBSEG070)

## Epics
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-epics"></a>

### Prepare the on-premises source Oracle database
<a name="prepare-the-on-premises-source-oracle-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up network connectivity from the target database to the source database. | Configure the on-premises network and firewall to allow incoming connection from the target Amazon RDS instance to the on-premises source Oracle database. | Network administrator, Security engineer |
| Create a database user with the appropriate privileges. | Create a database user in the on-premises source Oracle database with privileges to migrate data between the source and target using Oracle Data Pump:<pre>GRANT CONNECT to <migration_user>;<br />GRANT DATAPUMP_EXP_FULL_DATABASE to <migration_user>;<br />GRANT SELECT ANY TABLE to <migration_user>;</pre> | DBA |
| Prepare the on-premises source database for AWS DMS CDC migration. | (Optional) Prepare the on-premises source Oracle database for AWS DMS CDC migration after completion of Oracle Data Pump Full Load:1. Configure the additional privileges required to manage FLASHBACK during Oracle Data Pump migration:<pre>GRANT FLASHBACK ANY TABLE to <migration_user>;<br />GRANT FLASHBACK ARCHIVE ADMINISTER to <migration_user>;</pre><br />2. To configure user account privileges required on a self-managed Oracle source for AWS DMS, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed).<br />3. To prepare an Oracle self-managed source database for CDC using AWS DMS, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed.Configuration). | DBA |
| Install and configure SQL Developer. | Install and configure [SQL Developer](https://www.oracle.com/database/sqldeveloper/) to connect and run SQL queries on the source and target databases. | DBA, Migration engineer |
| Generate a script to create the tablespaces. | Use the following example SQL query to generate the script on the source database:<pre>SELECT <br />     'CREATE TABLESPACE '   tablespace_name    ' DATAFILE SIZE 1G AUTOEXTEND ON MAXSIZE UNLIMITED;' <br />     from dba_tablespaces <br />     where tablespace_name not in ('SYSTEM', 'SYSAUX','TEMP','UNDOTBS1') <br />     order by 1;</pre><br />The script will be applied on the target database. | DBA |
| Generate a script to create users, profiles, roles, and privileges. | To generate a script to create the database users, profiles, roles, and privileges, use the scripts from the Oracle Support document [How to Extract DDL for User including Privileges and Roles Using dbms\_metadata.get\_ddl (Doc ID 2739952.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2739952.1) (Oracle account required).<br />The script will be applied on the target database. | DBA |

### Prepare the target Amazon RDS for Oracle instance
<a name="prepare-the-target-rdslongora-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a database link to the source database and verify connectivity. | To create a database link to the on-premises source database, you can use the following example command:<pre>CREATE DATABASE LINK link2src<br />  CONNECT TO <migration_user_account> IDENTIFIED BY <password><br />  USING '(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<dns or ip address of remote db>)<br />         (PORT=<listener port>))(CONNECT_DATA=(SID=<remote SID>)))';</pre><br />To verify connectivity, run the following SQL command:<pre>select * from dual@link2src;</pre><br />Connectivity is successful if the response is `X`. | DBA |
| Run the scripts to prepare the target instance. | Run the previously generated scripts to prepare the target Amazon RDS for Oracle instance:1. Tablespaces<br />2. Profiles<br />3. Roles<br />This helps ensure that the Oracle Data Pump migration can create the schemas and their objects. | DBA, Migration engineer |

### Perform a full-load migration by using Oracle Data Pump Import over a database link
<a name="perform-a-full-load-migration-by-using-oracle-data-pump-import-over-a-database-link"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the required schemas. | To migrate the required schemas from the source on-premises database to the target Amazon RDS instance, use the code in the [Additional information](#migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional) section:+ To migrate a single schema, run *Code 1* from the [Additional information](#migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional) section.<br />+ To migrate multiple schemas, run *Code 2* from the [Additional information](#migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional) section.<br />To tune the performance of the migration, you can adjust the number of parallel processes by running the following command:<pre>DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);</pre> | DBA |
| Gather schema statistics to improve performance. | The Gather Schema Statistics command returns the Oracle query optimizer statistics gathered for database objects. By using this information, the optimizer can select the best execution plan for any query against these objects:<pre>EXECUTE DBMS_STATS.GATHER_SCHEMA_STATS(ownname => '<schema_name>');</pre> | DBA |

### Perform a full-load migration and CDC replication by using Oracle Data Pump and AWS DMS
<a name="perform-a-full-load-migration-and-cdc-replication-by-using-oracle-data-pump-and-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Capture the SCN on the source on-premises Oracle database. | Capture the [system change number (SCN)](https://docs.oracle.com/cd/E11882_01/server.112/e40540/transact.htm) on the source on-premises Oracle database. You will use the SCN for full-load import and as the starting point for CDC replication.<br />To generate the current SCN on the source database, run the following SQL statement:<pre>SELECT current_scn FROM V$DATABASE;</pre> | DBA |
| Perform the full-load migration of the schemas. | To migrate the required schemas (`FULL LOAD`) from the source on-premises database to the target Amazon RDS instance, do the following:+ To migrate a single schema, run *Code 3* from the [Additional information](#migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional) section.<br />+ To migrate multiple schemas, run *Code 4* from the [Additional information](#migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional) section.<br />In the code, replace `<CURRENT_SCN_VALUE_IN_SOURCE_DATABASE>` with the SCN that you captured from the source database:<pre>    DBMS_DATAPUMP.SET_PARAMETER (handle => v_hdnl, name => 'FLASHBACK_SCN', value => <CURRENT_SCN_VALUE_IN_SOURCE_DATABASE>);</pre><br />To tune the performance of the migration, you can adjust the number of parallel processes:<pre>DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);</pre> | DBA |
| Disable the triggers under the migrated schemas. | Before you begin the AWS DMS CDC-only task, disable the `TRIGGERS` under the migrated schemas.  | DBA |
| Gather schema statistics to improve performance. | The Gather Schema Statistics command returns the Oracle query optimizer statistics gathered for database objects:<pre>EXECUTE DBMS_STATS.GATHER_SCHEMA_STATS(ownname => '<schema_name>');</pre><br />By using this information, the optimizer can select the best execution plan for any query against these objects. | DBA |
| Use AWS DMS to perform an ongoing replication from the source to target. | Use AWS DMS to perform an ongoing replication from the source Oracle database to the target Amazon RDS for Oracle instance.<br />For more information, see [Creating tasks for ongoing replication using AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) and the blog post [How to work with native CDC support in AWS DMS](https://aws.amazon.com/blogs/database/aws-dms-now-supports-native-cdc-support/). | DBA, Migration engineer |

### Cut over to Amazon RDS for Oracle
<a name="cut-over-to-rdslongora"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable Multi-AZ on the instance 48 hours before cutover. | If this is a production instance, we recommend enabling [Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) deployment on the Amazon RDS instance to provide the benefits of high availability (HA) and disaster recovery (DR). | DBA, Migration engineer |
| Stop the AWS DMS CDC-only task (if CDC was turned on). | 1. Ensure the source latency and target latency on the AWS DMS task's Amazon CloudWatch metrics show 0 seconds.<br />2. Stop the AWS DMS CDC-only task. | DBA |
| Enable the triggers. | Enable the `TRIGGERS` that you disabled before the CDC task was created. | DBA |

## Related resources
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-resources"></a>

**AWS**
+ [Preparing an Oracle self-managed source database for CDC using AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed.Configuration)
+ [Creating tasks for ongoing replication using AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html)
+ [Multi-AZ deployments for high availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
+ [How to work with native CDC support in AWS DMS](https://aws.amazon.com/blogs/database/aws-dms-now-supports-native-cdc-support/) (blog post)

**Oracle documentation**
+ [DBMS\_DATAPUMP](https://docs.oracle.com/database/121/ARPLS/d_datpmp.htm)

## Additional information
<a name="migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-by-using-direct-oracle-data-pump-import-over-a-database-link-additional"></a>

*Code 1: Full-load migration only, single application schema*

```
DECLARE
    v_hdnl NUMBER;
BEGIN
    v_hdnl := DBMS_DATAPUMP.OPEN(operation => 'IMPORT', job_mode  => 'SCHEMA', remote_link => '<DB LINK Name to Source Database>', job_name  => null);
    DBMS_DATAPUMP.ADD_FILE( handle => v_hdnl, filename  => 'import_01.log',  directory => 'DATA_PUMP_DIR', filetype  => dbms_datapump.ku$_file_type_log_file);
    DBMS_DATAPUMP.METADATA_FILTER(v_hdnl,'SCHEMA_EXPR','IN (''<schema_name>'')');  -- To migrate one selected schema
    DBMS_DATAPUMP.METADATA_FILTER (hdnl, 'EXCLUDE_PATH_EXPR','IN (''STATISTICS'')'); -- To prevent gathering Statistics during the import
    DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);  -- Number of parallel processes performing export and import
    DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

*Code 2: Full-load migration only, multiple application schemas*

```
DECLARE
    v_hdnl NUMBER;
BEGIN
    v_hdnl := DBMS_DATAPUMP.OPEN(operation => 'IMPORT', job_mode  => 'SCHEMA', remote_link => '<DB LINK Name to Source Database>', job_name  => null);
    DBMS_DATAPUMP.ADD_FILE( handle => v_hdnl, filename  => 'import_01.log',  directory => 'DATA_PUMP_DIR', filetype  => dbms_datapump.ku$_file_type_log_file);
    DBMS_DATAPUMP.METADATA_FILTER (v_hdnl, 'SCHEMA_LIST', '''<SCHEMA_1>'',''<SCHEMA_2>'', ''<SCHEMA_3>'''); -- To migrate multiple schemas
    DBMS_DATAPUMP.METADATA_FILTER (v_hdnl, 'EXCLUDE_PATH_EXPR','IN (''STATISTICS'')'); -- To prevent gathering Statistics during the import
    DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);  -- Number of parallel processes performing export and import
    DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

*Code 3: Full-load migration before CDC-only task, single application schema*

```
DECLARE
    v_hdnl NUMBER;
BEGIN
    v_hdnl := DBMS_DATAPUMP.OPEN(operation => 'IMPORT', job_mode  => 'SCHEMA', remote_link => '<DB LINK Name to Source Database>', job_name  => null);
    DBMS_DATAPUMP.ADD_FILE( handle => v_hdnl, filename  => 'import_01.log',  directory => 'DATA_PUMP_DIR', filetype  => dbms_datapump.ku$_file_type_log_file);
    DBMS_DATAPUMP.METADATA_FILTER(v_hdnl,'SCHEMA_EXPR','IN (''<schema_name>'')');  -- To migrate one selected schema
    DBMS_DATAPUMP.METADATA_FILTER (v_hdnl, 'EXCLUDE_PATH_EXPR','IN (''STATISTICS'')'); -- To prevent gathering Statistics during the import
    DBMS_DATAPUMP.SET_PARAMETER (handle => v_hdnl, name => 'FLASHBACK_SCN', value => <CURRENT_SCN_VALUE_IN_SOURCE_DATABASE>); -- SCN required for AWS DMS CDC only task.
    DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);  -- Number of parallel processes performing export and import
    DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

*Code 4: Full-load migration before CDC-only task, multiple application schemas*

```
DECLARE
    v_hdnl NUMBER;
BEGIN
    v_hdnl := DBMS_DATAPUMP.OPEN (operation => 'IMPORT', job_mode  => 'SCHEMA', remote_link => '<DB LINK Name to Source Database>', job_name  => null);
    DBMS_DATAPUMP.ADD_FILE (handle => v_hdnl, filename  => 'import_01.log',  directory => 'DATA_PUMP_DIR', filetype  => dbms_datapump.ku$_file_type_log_file);
    DBMS_DATAPUMP.METADATA_FILTER (v_hdnl, 'SCHEMA_LIST', '''<SCHEMA_1>'',''<SCHEMA_2>'', ''<SCHEMA_3>'''); -- To migrate multiple schemas
    DBMS_DATAPUMP.METADATA_FILTER (v_hdnl, 'EXCLUDE_PATH_EXPR','IN (''STATISTICS'')'); -- To prevent gathering Statistics during the import
    DBMS_DATAPUMP.SET_PARAMETER (handle => v_hdnl, name => 'FLASHBACK_SCN', value => <CURRENT_SCN_VALUE_IN_SOURCE_DATABASE>); -- SCN required for AWS DMS CDC only task.
    DBMS_DATAPUMP.SET_PARALLEL (handle => v_hdnl, degree => 4);  -- Number of parallel processes performing export and import
    DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

*Scenario where a mixed migration approach can work better*

In rare scenarios where the source database contains tables with millions of rows and very large-sized LOBSEGMENT columns, this pattern will slow down the migration. Oracle migrates LOBSEGMENTs over the network link one at a time. It extracts a single row (along with the LOB column data) from the source table, and inserts the row into the target table, repeating the process until all rows are migrated. Oracle Data Pump over the database link doesn’t support bulk load or direct path load mechanisms for LOBSEGMENTs.

In this situation, we recommend the following:
+ Skip the identified tables during the Oracle Data Pump migration by adding the following metadata filter:

  ```
  dbms_datapump.metadata_filter(handle =>h1, name=>'NAME_EXPR', value => 'NOT IN (''TABLE_1'',''TABLE_2'')');
  ```
+ Use an AWS DMS task (full-load migration, with CDC replication if required) to migrate the identified tables. AWS DMS will extract multiple rows from the source Oracle database, and insert them in a batch to the target Amazon RDS instance, which improves performance.
