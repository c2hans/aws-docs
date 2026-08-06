---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-peoplesoft-to-amazon-rds-custom.html
---

# Migrate Oracle PeopleSoft to Amazon RDS Custom
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom"></a>

*Gaurav Gupta, Amazon Web Services*

## Summary
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-summary"></a>

[Oracle PeopleSoft](https://www.oracle.com/applications/peoplesoft/) is an enterprise resource planning (ERP) solution for enterprise-wide processes. PeopleSoft has a three-tier architecture: client, application, and database. PeopleSoft can be run on [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html). Now, you can also run PeopleSoft on [Amazon RDS Custom](https://aws.amazon.com/rds/custom/), which provides access to the underlying operating system.

[Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) is a managed database service for legacy, custom, and packaged applications that require access to the underlying operating system and database environment. When you migrate your Oracle database to Amazon RDS Custom, Amazon Web Services (AWS) can manage backup tasks and high availability, while you can focus on maintaining your PeopleSoft application and functionality. For key factors to consider for a migration, see [Oracle database migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/strategies.html) in AWS Prescriptive Guidance.

This pattern focuses on the steps to migrate a PeopleSoft database on Amazon Elastic Compute Cloud (Amazon EC2) to Amazon RDS Custom by using an Oracle Recovery Manager (RMAN) backup. It uses an [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) shared file system between the EC2 instance and Amazon RDS Custom, although you can also use Amazon FSx or any shared drive. The pattern uses an RMAN full backup (sometimes referred to as a level 0 backup).

## Prerequisites and limitations
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-prereqs"></a>

**Prerequisites**
+ An Oracle version 19C source database that is running on Amazon EC2 with Oracle Linux 7, Oracle Linux 8, Red Hat Enterprise Linux (RHEL) 7, or RHEL 8. In the examples for this pattern, the source database name is `FSDMO92`, but this isn’t a requirement.
**Note**
You can also use this pattern with on-premises Oracle source databases. You must have the appropriate network connectivity between the on-premises network and a virtual private cloud (VPC).
+ A PeopleSoft 9.2 demo instance.
+ A single PeopleSoft application tier. However, you can adapt this pattern to work with multiple application tiers.
+ Amazon RDS Custom configured with at least 8 GB of swap space.

**Limitations **

This pattern doesn’t support the following configurations:
+ Setting the database `ARCHIVE_LAG_TARGET` parameter to a value outside the 60–7200 range
+ Disabling the DB instance log mode (`NOARCHIVELOG`)
+ Turning off the Amazon Elastic Block Store (Amazon EBS) optimized attribute of the EC2 instance
+ Modifying the original EBS volumes attached to the EC2 instance
+ Adding new EBS volumes or changing the volume type from gp2 to gp3
+ Changing the extension format for the `LOG_ARCHIVE_FORMAT` parameter (requires `*.arc`)
+ Multiplexing or changing the control file location and name (it has to be `/rdsdbdata/db/*DBNAME*/controlfile/control-01.ctl`)

For additional information about these and other unsupported configurations, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-troubleshooting.html#custom-troubleshooting.fix-unsupported).

**Product versions**

For Oracle Database versions and instance classes supported by Amazon RDS Custom, see [Requirements and limitations for Amazon RDS Custom for Oracle.](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/UserGuide/custom-reqs-limits.html)

## Architecture
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-architecture"></a>

**Target technology stack**
+ Application Load Balancer
+ Amazon EFS
+ Amazon RDS Custom for Oracle
+ AWS Secrets Manager
+ Amazon Simple Storage Service (Amazon S3)

**Target architecture**

The following architecture diagram represents a PeopleSoft system running in a single [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) on AWS. The application tier is accessed through an [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/). Both the application and the databases are in private subnets, and the Amazon RDS Custom and Amazon EC2 database instance use an Amazon EFS shared file system to store and access the RMAN backup files. Amazon S3 is used for creating the custom RDS Oracle engine and for storing the redo logs metadata.

![Webservers, app servers, Amazon RDS Custom, an EC2 DB instance, and Amazon EFS in private subnets.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bd423dfe-f3c8-42d9-ac84-bf3d093c52bc/images/0e9a6431-e6c7-4047-ae6c-85311938041f.jpeg)

## Tools
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-tools"></a>

**Tools**

*AWS services*
+ [Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) is a managed database service for legacy, custom, and packaged applications that require access to the underlying operating system and database environment. It automates database administration tasks, such as backups and high availability.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud. This pattern uses an Amazon EFS shared file system to store and access the RMAN backup files.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. In this pattern, you retrieve the database user passwords from Secrets Manager to create the `RDSADMIN` and `ADMIN` users and to change the `sys` and `system` passwords.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones. This pattern uses an Application Load Balancer.

*Other tools*
+ Oracle Recovery Manager (RMAN) provides backup and recovery support for Oracle databases. This pattern uses RMAN to perform a hot backup of the source Oracle database on Amazon EC2 that is restored on Amazon RDS Custom.

## Best practices
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-best-practices"></a>
+ For database initialization parameters, customize the standard pfile that’s provided by the Amazon RDS Custom DB instance for PeopleSoft instead of using the spfile from the Oracle source database. This is because white spaces and comments cause issues when creating read replicas in Amazon RDS Custom. For more information about database initialization parameters, see Oracle Support Note 1100831.1 (requires an [Oracle Support](https://support.oracle.com/portal/) account).
+ Amazon RDS Custom uses Oracle automatic memory management by default. If you want to use the Hugemem kernel, you can configure Amazon RDS Custom to use automatic shared memory management instead.
+ Leave the `memory_max_target` parameter enabled by default. The framework uses this in the background to create read replicas.
+ Enable Oracle Flashback Database. This feature is useful when reinstating the standby in failover (not switchover) testing scenarios.

## Epics
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-epics"></a>

### Set up the DB instance and file system
<a name="set-up-the-db-instance-and-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the DB instance. | In the Amazon RDS console, create an Amazon RDS Custom for Oracle DB instance with a DB name called FSDMO92 (or your source database name).<br />For instructions, see [Working with Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html) in the AWS documentation and the [Amazon RDS Custom for Oracle – New Control Capabilities in Database Environment](https://aws.amazon.com/blogs/aws/amazon-rds-custom-for-oracle-new-control-capabilities-in-database-environment/) blog post. This ensures that the database name is set to the same name as the source database. (If kept blank, the EC2 instance and database name will be set to `ORCL`.) | DBA |

### Perform an RMAN full backup of the source Amazon EC2 database
<a name="perform-an-rman-full-backup-of-the-source-amazon-ec2-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a backup script. | Create an RMAN backup script  to back up the database to the Amazon EFS file system that you mounted (`/efs` in the following example). You can use the example code or run one of your existing RMAN scripts.<pre>#!/bin/bash<br />Dt=`date +'%Y%m%d-%H%M'`<br />BACKUP_LOG="rman-${ORACLE_SID}-$Dt"<br />export TAGDATE=`date +%Y%m%d%H%M`;<br />LOGPATH=/u01/scripts/logs<br />rman target / >> $LOGPATH/rman-${ORACLE_SID}-$Dt << EOF<br />SQL "ALTER SYSTEM SWITCH LOGFILE";<br />SQL "ALTER SESSION SET NLS_DATE_FORMAT="DD.MM.YYYY HH24:MI:SS"";<br />RUN<br />{<br />  ALLOCATE CHANNEL ch11 TYPE DISK MAXPIECESIZE 5G;<br />  ALLOCATE CHANNEL ch12 TYPE DISK MAXPIECESIZE 5G;<br />  BACKUP AS COMPRESSED BACKUPSET FULL DATABASE FORMAT '/efs/rman_backup/FSCM/%d_%T_%s_%p_FULL' ;<br />  SQL "ALTER SYSTEM ARCHIVE LOG CURRENT";<br />  BACKUP FORMAT '/efs/rman_backup/FSCM/%d_%T_%s_%p_ARCHIVE' ARCHIVELOG ALL DELETE ALL INPUT ;<br />  BACKUP CURRENT CONTROLFILE FORMAT '/efs/rman_backup/FSCM/%d_%T_%s_%p_CONTROL';<br />}<br />EXIT;<br />EOF<br />  </pre> | DBA |
| Run the backup script. | To run the RMAN backup script, log in as the Oracle Home User, and run the script.<pre>$  chmod a+x rman_backup.sh<br />$ ./rman_backup.sh &</pre> | DBA |
| Check for errors and note the name of the backup file. | Check the RMAN log file for errors. If everything looks fine, list the backup of the control file by running the following command.<pre>RMAN> list backup of controlfile;<br /><br />using target database control file instead of recovery catalog<br /></pre><br />Note the name of the output file.<pre>List of Backup Sets<br />===================<br /><br />BS Key  Type LV Size       Device Type Elapsed Time Completion Time<br />------- ---- -- ---------- ----------- ------------ ---------------<br />12      Full    21.58M     DISK        00:00:01     13-JUL-22<br />        BP Key: 12   Status: AVAILABLE  Compressed: NO  Tag: TAG20220713T150155<br />        Piece Name: /efs/rman_backup/FSCM/FSDMO92_20220713_12_1_CONTROL<br /> Control File Included: Ckp SCN: 16559159985898   Ckp time: 13-JUL-22<br /></pre><br />You will use the backup control file `/efs/rman_backup/FSCM/FSDMO92_20220713_12_1_CONTROL` when you restore the database on Amazon RDS Custom. | DBA |

### Shut down the source application tier
<a name="shut-down-the-source-application-tier"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the application.  | To shut down the source application tier, use the `psadmin` utility or the `psadmin` command line utility.1. To shut down the webserver, run the following command.<pre>psadmin -w shutdown -d "webserver domain name"</pre><br />2. To shut down the application server, run the following command.<pre>psadmin -c shutdown -d "application server domain name"</pre><br />3. To shut down the process scheduler, run the following command.<pre>psadmin -p stop -d "process scheduler domain name"</pre> | DBA, PeopleSoft Administrator |

### Configure the target Amazon RDS Custom database
<a name="configure-the-target-amazon-rds-custom-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the nfs-utils rpm package. | To install the `nfs-utils rpm` package, run the following command.<pre>$ yum install -y nfs-utils<br /></pre> | DBA |
| Mount the EFS storage. | Get the Amazon EFS mount command from the Amazon EFS console page. Mount the EFS file system on the Amazon RDS instance by using a Network File System (NFS) client.<pre>sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-xxxxxxxxxx.efs.eu-west-1.amazonaws.com:/ /efs<br />sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-xxxxxxxxxx.efs.eu-west-1.amazonaws.com:/ /efs</pre> | DBA |

### Drop the starter database and create the directories to store the database files
<a name="drop-the-starter-database-and-create-the-directories-to-store-the-database-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Pause automation mode. | You have to pause [automation mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.html#custom-managing.pausing) on your Amazon RDS Custom DB instance before you proceed with the next steps, to make sure that automation doesn’t interfere with the RMAN restore activity.<br />You can pause the automation by using the AWS console or the AWS Command Line Interface (AWS CLI) command (make sure that you have [configured the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) first).<pre>aws rds modify-db-instance \<br />--db-instance-identifier peoplesoft-fscm-92 \<br />--automation-mode all-paused \<br />--resume-full-automation-mode-minute 360 \<br />--region eu-west-1<br /></pre><br />When you specify the duration of the pause, make sure that you leave enough time for the RMAN restore. This depends on the size of the source database, so modify the 360 value accordingly.<br />Also, make sure that the total time of the paused automation does not overlap with the backup or maintenance window of the database. | DBA |
| Create and modify the parameter file for PeopleSoft | To create and modify the pfile for PeopleSoft,  use the standard pfile created with the Amazon RDS Custom DB instance. Add the parameters you need for PeopleSoft.1. Switch to `rds user rdsdb` by running the following command.<pre>$ sudo su - rdsdb</pre><br />2. Log in to SQL\*Plus on the starter database, and create the pfile by running the following command.<pre>SQL> create pfile from spfile;</pre><br />This creates the pfile in `$ORACLE_HOME/dbs`.<br />3. Make a backup of this pfile.<br />4. Edit the pfile to add or update PeopleSoft parameters.<pre>*._gby_hash_aggregation_enabled=false<br /><br />*._unnest_subquery=false<br /><br />*.nls_language='AMERICAN'<br /><br />*.nls_length_semantics='CHAR'<br /><br />*.nls_territory='AMERICA'<br /><br />*.open_cursors=1000<br /><br />*.db_files=1200<br /><br />*.undo_tablespace='UNDOTBS1'</pre><br />PeopleSoft related parameters can be found in [Oracle Support](https://support.oracle.com/) Note 1100831.1.<br />5. Remove the spfile reference from the pfile.<pre>*.spfile='/rdsdbbin/oracle/dbs/spfileFSDMO92.ora'</pre> | DBA |
| Drop the starter database. | To drop the existing Amazon RDS Custom database, use the following code.<pre>$ sqlplus / as sysdba<br />SQL> shutdown immediate;<br />SQL> startup mount exclusive restrict;<br />SQL> drop database;<br />SQL> exit</pre> |  |
| Restore the Amazon RDS Custom database from the backup. | Restore the database by using the following script. The script will first restore the control file and then restore the entire database from the backup pieces stored on the EFS mount.<pre>#!/bin/bash<br />Dt=`date +'%Y%m%d-%H%M'`<br />BACKUP_LOG="rman-${ORACLE_SID}-$Dt"<br />export TAGDATE=`date +%Y%m%d%H%M`;<br />LOGPATH=/rdsdbdata/scripts/logs<br />rman target / >> $LOGPATH/rman-${ORACLE_SID}-$Dt << EOF<br />restore controlfile from "/efs/rman_backup/FSCM/FSDMO92_20220713_12_1_CONTROL";<br />alter database mount;<br />run<br />{<br />set newname for database to '/rdsdbdata/db/FSDMO92_A/datafile/%f_%b';<br />SET NEWNAME FOR TEMPFILE 1 TO '/rdsdbdata/db/FSDMO92_A/datafile/%f_%b';<br />RESTORE DATABASE;<br />SWITCH DATAFILE ALL;<br />SWITCH TEMPFILE ALL;<br />RECOVER DATABASE;<br />}<br />EOF<br />sqlplus / as sysdba >> $LOGPATH/rman-${ORACLE_SID}-$Dt<<-EOF<br />ALTER DATABASE RENAME FILE '/u01/psoft/db/oradata/FSDMO92/redo01.log' TO '/rdsdbdata/db/FSDMO92_A/onlinelog/redo01.log';<br />ALTER DATABASE RENAME FILE '/u01/psoft/db/oradata/FSDMO92/redo02.log' TO '/rdsdbdata/db/FSDMO92_A/onlinelog/redo02.log';<br />ALTER DATABASE RENAME FILE '/u01/psoft/db/oradata/FSDMO92/redo03.log' TO '/rdsdbdata/db/FSDMO92_A/onlinelog/redo03.log';<br />alter database clear unarchived logfile group 1;<br />alter database clear unarchived logfile group 2;<br />alter database clear unarchived logfile group 3;<br />alter database open resetlogs;<br />EXIT<br />EOF<br /></pre> | DBA |

### Retrieve passwords from Secrets Manager, create users, and change passwords
<a name="retrieve-passwords-from-secrets-manager-create-users-and-change-passwords"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Retrieve the password from Secrets Manager. | You can perform this step by using the AWS console or the AWS CLI. The following steps show instructions for the console.1. Sign in to the AWS Management Console and open the Amazon RDS console.<br />2. In the navigation pane, choose **Databases**, and then select the Amazon RDS database.<br />3. Choose the **Configuration** tab, and note the resource ID for the instance. It will be in the format `db-<ID>` (for example, `db-73GJNHLGDNZNDOXNWXSECUW6LE`).<br />4. Open the Secrets Manager console.<br />5. Choose the secret that has the same name as `do-not-delete-custom-<resource_id>`, where `resource-id` refers to the resource ID that you noted in step 3.<br />6. Choose **Retrieve secret value**.<br />This password will be same for the `sys`, `system`, `rdsadmin`, and `admin` users. | DBA |
| Create the RDSADMIN user. | `RDSADMIN` is the database user for monitoring and orchestrating the Amazon RDS Custom DB instance. Because the starter database was dropped and the target database was restored from the source using RMAN, you must recreate this user after the restore operation to make sure that Amazon RDS Custom monitoring works as expected. You also must create a separate profile and tablespace for the `RDSADMIN` user.1. Enter the following commands at a SQL prompt.<pre>SQL> set echo on feedback on serverout on<br />SQL> @?/rdbms/admin/utlpwdmg.sql<br />SQL> ALTER PROFILE DEFAULT<br />LIMIT<br />FAILED_LOGIN_ATTEMPTS UNLIMITED<br />PASSWORD_LIFE_TIME UNLIMITED<br />PASSWORD_VERIFY_FUNCTION NULL;</pre><br />2. Create the profile `RDSADMIN`.<pre>SQL> set echo on feedback on serverout on<br />SQL> alter session set "_oracle_script"=true;<br />SQL> CREATE PROFILE RDSADMIN<br />LIMIT<br />COMPOSITE_LIMIT UNLIMITED<br />SESSIONS_PER_USER UNLIMITED<br />CPU_PER_SESSION UNLIMITED<br />CPU_PER_CALL UNLIMITED<br />LOGICAL_READS_PER_SESSION UNLIMITED<br />LOGICAL_READS_PER_CALL UNLIMITED<br />IDLE_TIME UNLIMITED<br />CONNECT_TIME UNLIMITED<br />PRIVATE_SGA UNLIMITED<br />FAILED_LOGIN_ATTEMPTS 10<br />PASSWORD_LIFE_TIME UNLIMITED<br />PASSWORD_REUSE_TIME UNLIMITED<br />PASSWORD_REUSE_MAX UNLIMITED<br />PASSWORD_VERIFY_FUNCTION NULL<br />PASSWORD_LOCK_TIME 86400/86400<br />PASSWORD_GRACE_TIME 604800/86400;</pre><br />3. Create the `RDSADMIN` tablespace.<pre>SQL> CREATE BIGFILE TABLESPACE rdsadmin '/rdsdbdata/db/FSDMO92_A/datafile/rdsadmin.dbf' DATAFILE SIZE 7M<br />AUTOEXTEND ON NEXT 1m<br />LOGGING ONLINE PERMANENT BLOCKSIZE 8192 EXTENT MANAGEMENT LOCAL AUTOALLOCATE DEFAULT NOCOMPRESS SEGMENT SPACE MANAGEMENT AUTO;</pre><br />4. Create the `RDSADMIN` user. Replace the `RDSADMIN` password with the password you obtained earlier from Secrets Manager.<pre>SQL> CREATE USER rdsadmin IDENTIFIED BY xxxxxxxxxx<br />DEFAULT TABLESPACE rdsadmin<br />TEMPORARY TABLESPACE TEMP<br />profile rdsadmin ;</pre><br />5. Grant privileges to RDSADMIN.<pre>SQL> GRANT "CONNECT" TO RDSADMIN WITH ADMIN OPTION;<br />SQL> GRANT "RESOURCE" TO RDSADMIN WITH ADMIN OPTION;<br />SQL> GRANT "DBA" TO RDSADMIN;<br />SQL> GRANT "SELECT_CATALOG_ROLE" TO RDSADMIN WITH ADMIN OPTION;<br />SQL> GRANT ALTER SYSTEM TO RDSADMIN;<br />SQL> GRANT UNLIMITED TABLESPACE TO RDSADMIN;<br />SQL> GRANT SELECT ANY TABLE TO RDSADMIN;<br />SQL> GRANT ALTER DATABASE TO RDSADMIN;<br />SQL> GRANT ADMINISTER DATABASE TRIGGER TO RDSADMIN;<br />SQL> GRANT ANY OBJECT PRIVILEGE TO RDSADMIN WITH ADMIN OPTION;<br />SQL> GRANT INHERIT ANY PRIVILEGES TO RDSADMIN;<br />SQL> ALTER USER RDSADMIN DEFAULT ROLE ALL;</pre><br />6. `Set the SYS, SYSTEM, and DBSNMP user profiles to RDSADMIN.`<pre>SQL> set echo on feedback on serverout on<br />SQL> alter user SYS profile RDSADMIN;<br />SQL> alter user SYSTEM profile RDSADMIN;<br />SQL> alter user DBSNMP profile RDSADMIN;</pre> | DBA |
| Create the master user. | Because the starter database was dropped and the target database was restored from the source by using RMAN, you must recreate the master user. In this example, the master user name is `admin`.<pre>SQL> create user admin identified by <password>;<br />SQL> grant dba to admin</pre> | DBA |
| Change the system passwords. | Change the system passwords by using the password you retrieved from Secrets Manager.<pre>SQL> alter user sys identified by xxxxxxxxxxx;<br />SQL> alter user system identified by xxxxxxxxxx;</pre><br />If you don’t change these passwords, Amazon RDS Custom displays the error message, "The database monitoring user or user credentials have changed." | DBA |

### Configure the TNS entries for Amazon RDS Custom and PeopleSoft
<a name="configure-the-tns-entries-for-amazon-rds-custom-and-peoplesoft"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the tnsnames file. | To connect to the database from the application tier, configure the `tnsnames.ora` file so you can connect to the database from the application tier. In the following example, you can see that there is a soft link to the `tnsnames.ora` file, but the file is empty by default. <pre>$ cd /rdsdbbin/oracle/network/admin<br />$ ls -ltr<br />-rw-r--r-- 1 rdsdb database 1536 Feb 14  2018 shrept.lst<br />lrwxrwxrwx 1 rdsdb database   30 Apr  5 13:19 listener.ora -> /rdsdbdata/config/listener.ora<br />lrwxrwxrwx 1 rdsdb database   28 Apr  5 13:19 sqlnet.ora -> /rdsdbdata/config/sqlnet.ora<br />lrwxrwxrwx 1 rdsdb database   30 Apr  5 13:19 tnsnames.ora -> /rdsdbdata/config/tnsnames.ora</pre>1. Create the `tsnames.ora` entry. Because of the way Amazon RDS automation parses the files, you have to make sure that the entry doesn’t contain any white spaces, comments, or extra lines. Otherwise, you might run into issues when using some of the APIs, such [as create-db-instance-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance-read-replica.html).<br />2. Replace the port, host, and SID in accordance with your PeopleSoft database requirements. Use the following code as an example.<pre>$ vi tnsnames.ora <br /><br />FSDMO92=(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = x.x.x.x)(PORT = 1521))) (CONNECT_DATA = (SERVER = DEDICATED) (SID = FSDMO92)))</pre><br />3. To confirm that the PeopleSoft database can be reached, run the following command.<pre>$ tnsping FSDMO92<br /><br />TNS Ping Utility for Linux: Version 19.0.0.0.0 - Production on 14-JUL-2022 10:16:45<br /><br />Copyright (c) 1997, 2021, Oracle.  All rights reserved.<br /><br />Used parameter files:<br />/rdsdbbin/oracle/network/admin/sqlnet.ora<br /><br />Used TNSNAMES adapter to resolve the alias<br />Attempting to contact (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = x.x.x.x)(PORT = 1521))) (CONNECT_DATA = (SERVER = DEDICATED) (SID = FSDMO92)))<br />OK (0 msec)<br /></pre> | DBA |

### Create the spfile softlink
<a name="create-the-spfile-softlink"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the spfile softlink. | 1. To create spfile in the location `/rdsdbdata/admin/FSDMO92/pfile`, run the following command.<pre>SQL> create spfile='/rdsdbdata/admin/FSDMO92/pfile/spfileFSDMO92.ora' from pfile;</pre><br />2. Navigate to `$ORACLE_HOME/dbs`, and create a soft link for the spfile.<pre>ln -s '/rdsdbdata/admin/FSDMO92/pfile/spfileFSDMO92.ora' spfileFSDMO92.ora</pre><br />3. After this file is created, you can shut down and start the database by using the spfile. | DBA |

### Perform post-migration steps
<a name="perform-post-migration-steps"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the schema, connections, and maintenance tasks. | To finalize the migration, perform the following tasks.+ Gather schema statistics. <br />+ Ensure that the PeopleSoft application tier can connect to the new Amazon RDS Custom database.<br />+ Set up your backup and maintenance schedules. | DBA |

## Related resources
<a name="migrate-oracle-peoplesoft-to-amazon-rds-custom-resources"></a>
+ [Working with Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html)
+ [Amazon RDS Custom for Oracle – New Control Capabilities in Database Environment](https://aws.amazon.com/blogs/aws/amazon-rds-custom-for-oracle-new-control-capabilities-in-database-environment/) (blog post)
+ [Integrate Amazon RDS Custom for Oracle with Amazon EFS](https://aws.amazon.com/blogs/database/integrate-amazon-rds-custom-for-oracle-with-amazon-efs/) (blog post)
+ [Configuring Amazon RDS as an Oracle PeopleSoft Database](https://d1.awsstatic.com/whitepapers/configuring-amazon-rds-as-peoplesoft-database.pdf) (AWS whitepaper)
