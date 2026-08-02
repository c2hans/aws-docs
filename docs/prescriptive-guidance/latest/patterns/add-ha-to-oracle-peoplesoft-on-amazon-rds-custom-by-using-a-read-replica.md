---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica.html
---

# Add HA to Oracle PeopleSoft on Amazon RDS Custom by using a read replica
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica"></a>

*sampath kathirvel, Amazon Web Services*

## Summary
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-summary"></a>

To run the [Oracle PeopleSoft](https://www.oracle.com/applications/peoplesoft/) enterprise resource planning (ERP) solution on Amazon Web Services (AWS), you can use [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) or [Amazon RDS Custom for Oracle](https://aws.amazon.com/rds/custom/), which supports legacy, custom, and packaged applications that require access to the underlying operating system and database environment. For key factors to consider when planning a migration, see [Oracle database migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/strategies.html) in AWS Prescriptive Guidance.

As of this writing, RDS Custom for Oracle doesn’t support the [Multi-AZ](https://aws.amazon.com/blogs/aws/multi-az-option-for-amazon-rds-oracle/) option, which is available for [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/) as an HA solution using storage replication. Instead, this pattern achieves HA by using a standby database that creates and maintains a physical copy of the primary database. The pattern focuses on the steps to run a PeopleSoft application database on Amazon RDS Custom with HA by using Oracle Data Guard to set up a read replica.

This pattern also changes the read replica to read-only mode. Having your read replica in read-only mode provides additional benefits:
+ Offloading read-only workloads from the primary database
+ Enabling automatic repair of corrupted blocks by retrieving healthy blocks from the standby database using the Oracle Active Data Guard feature
+ Using the Far Sync capability to keep the remote standby database in sync without the performance overhead associated with long-distance redo log transmission.

Using a replica in read-only mode requires the [Oracle Active Data Guard](https://www.oracle.com/assets/technology-price-list-070617.pdf) option, which comes at an extra cost because it is a separately licensed feature of Oracle Database Enterprise Edition.

## Prerequisites and limitations
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-prereqs"></a>

**Prerequisites **
+ An existing PeopleSoft application on Amazon RDS Custom. If you don’t have an application, see the pattern [Migrate Oracle PeopleSoft to Amazon RDS Custom](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-peoplesoft-to-amazon-rds-custom.html).
+ A single PeopleSoft application tier. However, you can adapt this pattern to work with multiple application tiers.
+ Amazon RDS Custom configured with at least 8 GB of swap space.
+ An Oracle Active Data Guard database license for converting the read replica into read-only mode and using it for offloading reporting tasks to the standby. For more information, see the [Oracle Technology Commercial Price List](https://www.oracle.com/corporate/pricing/#technology).

**Limitations**** **
+ General limitations and unsupported configurations for [RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.limits)
+ Limitations associated with [Amazon RDS Custom for Oracle read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.html#custom-rr.limitations)

**Product versions**
+ For Oracle Database versions supported by Amazon RDS Custom, see [RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.html#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora).
+ For Oracle Database instance classes supported by Amazon RDS Custom, see [DB instance class support for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.instances).

## Architecture
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-architecture"></a>

**Target technology stack**
+ Amazon RDS Custom for Oracle
+ AWS Secrets Manager
+ Oracle Active Data Guard
+ Oracle PeopleSoft application

**Target architecture**

The following diagram shows an Amazon RDS Custom DB instance and an Amazon RDS Custom read replica. The read replica uses Oracle Active Data Guard to replicate to another Availability Zone. You can also use the read replica to offload read traffic on the primary database and for reporting purposes.

![The VPC includes AWS Secrets Manager, Amazon EFS, an application tier, and the database tier.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7df4b2d0-b833-4ba3-98e4-a178db395d9d/images/463aefbe-70ad-4cd3-9ddc-0d8347e848c6.png)

For a representative architecture using Oracle PeopleSoft on AWS, see [Set up a highly available PeopleSoft architecture on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-a-highly-available-peoplesoft-architecture-on-aws.html).

## Tools
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-tools"></a>

**AWS services**
+ [Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) is a managed database service for legacy, custom, and packaged applications that require access to the underlying operating system and database environment.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. In this pattern, you retrieve the database user passwords from Secrets Manager for `RDS_DATAGUARD` with the secret name `do-not-delete-rds-custom-+<<RDS Resource ID>>+-dg`.

**Other Tools**
+ [Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/preface.html#GUID-B6209E95-9DA8-4D37-9BAD-3F000C7E3590) helps you create, maintain, manage, and monitor standby databases.

## Best practices
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-best-practices"></a>

To work toward a zero data loss (RPO=0) objective, use the `MaxAvailability` Data Guard protection mode, with the redo transport `SYNC+NOAFFIRM` setting for better performance. For more information about selecting the database protection mode, see the *Additional information* section.

## Epics
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-epics"></a>

### Create the read replica
<a name="create-the-read-replica"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the read replica. | To create a read replica of the Amazon RDS Custom DB instance, follow the instructions in the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create) and use the Amazon RDS Custom DB instance that you created (see the *Prerequisites* section) as the source database.<br />By default, the Amazon RDS Custom read replica is created as a physical standby and is in the mounted state. This is intentional to ensure compliance with the Oracle Active Data Guard license.<br />This pattern includes code for setting up a multitenant container database (CDB) or a non-CDB instance. | DBA |

### Change Oracle Data Guard protection mode to MaxAvailability
<a name="change-oracle-data-guard-protection-mode-to-maxavailability"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access the Data Guard broker configuration on the primary database. | In this example, the Amazon RDS Custom read replica is `RDS_CUSTOM_ORCL_D` for the Non-CDB instance and `RDS_CUSTOM_RDSCDB_B` for the CDB instance. The databases for Non-CDB are `orcl_a` (primary) and `orcl_d` (standby). The database names for CDB are `rdscdb_a` (primary) and `rdscdb_b` (standby).<br />You can connect to the RDS Custom read replica directly or through the primary database. You can find the net service name for your database in the `tnsnames.ora` file located in the `$ORACLE_HOME/network/admin` directory. RDS Custom for Oracle automatically populates these entries for your primary database and your read replicas.<br />The password for the `RDS_DATAGUARD` user is stored in AWS Secrets Manager, with secret name `do-not-delete-rds-custom-+<<RDS Resource ID>>+-dg`. For more information on how to connect to an RDS Custom instance using the SSH (Secure Shell) key retrieved from Secrets Manager, see [Connecting to your RDS Custom DB instance using SSH](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html#custom-creating.ssh).<br />To access the Oracle Data Guard broker configuration through the Data Guard command line (`dgmgrl`), use the following code.<br />**Non-CDB**<pre>$ dgmgrl RDS_DATAGUARD@RDS_CUSTOM_ORCL_D<br />DGMGRL for Linux: Release 19.0.0.0.0 - Production on Fri Sep 30 22:44:49 2022<br />Version 19.10.0.0.0<br />Copyright (c) 1982, 2019, Oracle and/or its affiliates. All rights reserved.<br />Welcome to DGMGRL, type "help" for information.<br />Password:<br />Connected to "ORCL_D"<br />Connected as SYSDG.<br />DGMGRL> <br />DGMGRL> show database orcl_d<br />Database - orcl_d<br />Role: PHYSICAL STANDBY<br />Intended State: APPLY-ON<br />Transport Lag: 0 seconds (computed 0 seconds ago)<br />Apply Lag: 0 seconds (computed 0 seconds ago)<br />Average Apply Rate: 11.00 KByte/s<br />Instance(s):<br />ORCL<br />SUCCESS<br />DGMGRL></pre><br />**CDB**<pre>-bash-4.2$ dgmgrl C##RDS_DATAGUARD@RDS_CUSTOM_RDSCDB_B<br />DGMGRL for Linux: Release 19.0.0.0.0 - Production on Wed Jan 11 20:24:11 2023<br />Version 19.16.0.0.0<br />Copyright (c) 1982, 2019, Oracle and/or its affiliates. All rights reserved.<br />Welcome to DGMGRL, type "help" for information.<br />Password:<br />Connected to "RDSCDB_B"<br />Connected as SYSDG.<br />DGMGRL><br />DGMGRL> show database rdscdb_b<br />Database - rdscdb_b<br />  Role:               PHYSICAL STANDBY<br />  Intended State:     APPLY-ON<br />  Transport Lag:      0 seconds (computed 1 second ago)<br />  Apply Lag:          0 seconds (computed 1 second ago)<br />  Average Apply Rate: 2.00 KByte/s<br />  Real Time Query:    OFF<br />  Instance(s):<br />    RDSCDB<br />Database Status:<br />SUCCESS<br />DGMGRL></pre> | DBA |
| Change the log transport setting by connecting to DGMGRL from the primary node. | Change the log transport mode to `FastSync`, corresponding to the redo transport setting `SYNC+NOAFFIRM`. To ensure that you have valid settings after the role switch, change it for both the primary database and the standby database.<br />**Non-CDB**<pre>DGMGRL><br />DGMGRL> edit database orcl_d set property logxptmode=fastsync;<br />Property "logxptmode" updated<br />DGMGRL> show database orcl_d LogXptMode;<br />LogXptMode = 'fastsync'<br />DGMGRL> edit database orcl_a set property logxptmode=fastsync;<br />Property "logxptmode" updated<br />DGMGRL> show database orcl_a logxptmode;<br />LogXptMode = 'fastsync'<br />DGMGRL>   </pre><br />**CDB**<pre>DGMGRL> edit database rdscdb_b set property logxptmode=fastsync;DGMGRL> edit database rdscdb_b set property logxptmode=fastsync;<br />Property "logxptmode" updated<br />DGMGRL> show database rdscdb_b LogXptMode;<br />  LogXptMode = 'fastsync'<br />DGMGRL> edit database rdscdb_a set property logxptmode=fastsync;<br />Property "logxptmode" updated<br />DGMGRL> show database rdscdb_a logxptmode;<br />  LogXptMode = 'fastsync'<br />DGMGRL></pre> | DBA |
| Change the protection mode to MaxAvailability. | Change the protection mode to `MaxAvailability` by connecting to `DGMGRL` from the primary node.<br />**Non-CDB**<pre>DGMGRL> edit configuration set protection mode as maxavailability;<br />Succeeded.<br />DGMGRL> show configuration;<br />Configuration - rds_dg<br />Protection Mode: MaxAvailability<br />Members:<br />orcl_a - Primary database<br />orcl_d - Physical standby database <br />Fast-Start Failover: Disabled<br />Configuration Status:<br />SUCCESS (status updated 38 seconds ago)<br />DGMGRL> </pre><br />**CDB**<pre>DGMGRL> show configuration<br />Configuration - rds_dg<br />  Protection Mode: MaxAvailability<br />  Members:<br />  rdscdb_a - Primary database<br />    rdscdb_b - Physical standby database <br />Fast-Start Failover:  Disabled<br />Configuration Status:<br />SUCCESS   (status updated 57 seconds ago)<br />DGMGRL></pre> | DBA |

### Change the replica status from mount to read-only and enable redo apply
<a name="change-the-replica-status-from-mount-to-read-only-and-enable-redo-apply"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop redo apply for the standby database. | The read replica is created in `MOUNT` mode by default. To open it in read-only mode, you first need to turn off redo apply by connecting to `DGMGRL` from the primary or standby node.<br />**Non-CDB**<pre>DGMGRL> show database orcl_dDGMGRL> show database orcl_d<br />Database - orcl_d<br />Role: PHYSICAL STANDBY<br />Intended State: APPLY-ON<br />Transport Lag: 0 seconds (computed 1 second ago)<br />Apply Lag: 0 seconds (computed 1 second ago)<br />Average Apply Rate: 11.00 KByte/s<br />Real Time Query: OFF<br />Instance(s):<br />ORCL<br />Database Status:<br />SUCCESS<br />DGMGRL> edit database orcl_d set state=apply-off;<br />Succeeded.<br />DGMGRL> show database orcl_d<br />Database - orcl_d<br />Role: PHYSICAL STANDBY<br />Intended State: APPLY-OFF<br />Transport Lag: 0 seconds (computed 1 second ago)<br />Apply Lag: 42 seconds (computed 1 second ago)<br />Average Apply Rate: (unknown)<br />Real Time Query: OFF<br />Instance(s):<br />ORCL<br />Database Status:<br />SUCCESS<br />DGMGRL></pre><br />**CDB**<pre>DGMGRL> show configurationDGMGRL> show configuration<br />Configuration - rds_dg<br />  Protection Mode: MaxAvailability<br />  Members:<br />  rdscdb_a - Primary database<br />    rdscdb_b - Physical standby database <br />Fast-Start Failover:  Disabled<br />Configuration Status:<br />SUCCESS   (status updated 57 seconds ago)<br />DGMGRL> show database rdscdb_b;<br />Database - rdscdb_b<br />  Role:               PHYSICAL STANDBY<br />  Intended State:     APPLY-ON<br />  Transport Lag:      0 seconds (computed 1 second ago)<br />  Apply Lag:          0 seconds (computed 1 second ago)<br />  Average Apply Rate: 2.00 KByte/s<br />  Real Time Query:    OFF<br />  Instance(s):<br />    RDSCDB<br />Database Status:<br />SUCCESS<br />DGMGRL> edit database rdscdb_b set state=apply-off;<br />Succeeded.<br />DGMGRL> show database rdscdb_b;<br />Database - rdscdb_b<br />  Role:               PHYSICAL STANDBY<br />  Intended State:     APPLY-OFF<br />  Transport Lag:      0 seconds (computed 1 second ago)<br />  Apply Lag:          0 seconds (computed 1 second ago)<br />  Average Apply Rate: (unknown)<br />  Real Time Query:    OFF<br />  Instance(s):<br />    RDSCDB<br />Database Status:<br />SUCCESS</pre> | DBA |
| Open the read replica instance in read-only mode. | Connect to the standby database by using the TNS entry, and open it in read-only mode by connecting to it from the primary or standby node.<br />**Non-CDB**<pre>$ sqlplus RDS_DATAGUARD@RDS_CUSTOM_ORCL_D as sysdg<br />-bash-4.2$ sqlplus RDS_DATAGUARD@RDS_CUSTOM_ORCL_D as sysdg<br />SQL*Plus: Release 19.0.0.0.0 - Production on Fri Sep 30 23:00:14 2022<br />Version 19.10.0.0.0<br />Copyright (c) 1982, 2020, Oracle. All rights reserved.<br />Enter password: <br />Last Successful login time: Fri Sep 30 2022 22:48:27 +00:00<br />Connected to:<br />Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production<br />Version 19.10.0.0.0<br />SQL> select open_mode from v$database;<br />OPEN_MODE<br />--------------------<br />MOUNTED<br />SQL> alter database open read only;<br />Database altered.<br />SQL> select open_mode from v$database;<br />OPEN_MODE<br />--------------------<br />READ ONLY<br />SQL> </pre><br />**CDB**<pre>-bash-4.2$ sqlplus C##RDS_DATAGUARD@RDS_CUSTOM_RDSCDB_B as sysdg<br />SQL*Plus: Release 19.0.0.0.0 - Production on Wed Jan 11 21:14:07 2023<br />Version 19.16.0.0.0<br />Copyright (c) 1982, 2022, Oracle.  All rights reserved.<br />Enter password: <br />Last Successful login time: Wed Jan 11 2023 21:12:05 +00:00<br />Connected to:<br />Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production<br />Version 19.16.0.0.0<br />SQL> select name,open_mode from v$database;<br />NAME   OPEN_MODE<br />--------- --------------------<br />RDSCDB   MOUNTED<br />SQL> alter database open read only;<br />Database altered.<br />SQL> select name,open_mode from v$database;<br />NAME   OPEN_MODE<br />--------- --------------------<br />RDSCDB   READ ONLY<br />SQL></pre> | DBA |
| Activate redo apply on the read replica instance. | Activate redo apply on the read replica instance by using `DGMGR`L from the primary or standby node.<br />**Non-CDB**<pre>$ dgmgrl RDS_DATAGUARD@RDS_CUSTOM_ORCL_D<br />DGMGRL for Linux: Release 19.0.0.0.0 - Production on Fri Sep 30 23:02:16 2022<br />Version 19.10.0.0.0<br />Copyright (c) 1982, 2019, Oracle and/or its affiliates. All rights reserved.<br />Welcome to DGMGRL, type "help" for information.<br />Password:<br />Connected to "ORCL_D"<br />Connected as SYSDG.<br />DGMGRL> <br />edit database orcl_d set state=apply-on;<br />DGMGRL> edit database orcl_d set state=apply-on;<br />Succeeded.<br />DGMGRL> show database orcl_d<br />Database - orcl_d<br />Role: PHYSICAL STANDBY<br />Intended State: APPLY-ON<br />Transport Lag: 0 seconds (computed 0 seconds ago)<br />Apply Lag: 0 seconds (computed 0 seconds ago)<br />Average Apply Rate: 496.00 KByte/s<br />Real Time Query: ON<br />Instance(s):<br />ORCL<br />Database Status:<br />SUCCESS<br />DGMGRL></pre><br />**CDB**<pre>-bash-4.2$ dgmgrl C##RDS_DATAGUARD@RDS_CUSTOM_RDSCDB_B-bash-4.2$ dgmgrl C##RDS_DATAGUARD@RDS_CUSTOM_RDSCDB_B<br />DGMGRL for Linux: Release 19.0.0.0.0 - Production on Wed Jan 11 21:21:11 2023<br />Version 19.16.0.0.0<br />Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.<br />Welcome to DGMGRL, type "help" for information.<br />Password:<br />Connected to "RDSCDB_B"<br />Connected as SYSDG.<br />DGMGRL> edit database rdscdb_b set state=apply-on;<br />Succeeded.<br />DGMGRL> show database rdscdb_b           <br />Database - rdscdb_b<br />  Role:               PHYSICAL STANDBY<br />  Intended State:     APPLY-ON<br />  Transport Lag:      0 seconds (computed 0 seconds ago)<br />  Apply Lag:          0 seconds (computed 0 seconds ago)<br />  Average Apply Rate: 35.00 KByte/s<br />  Real Time Query:    ON<br />  Instance(s):<br />    RDSCDB<br />Database Status:<br />SUCCESS<br />DGMGRL> show database rdscdb_b   <br />Database - rdscdb_b<br />  Role:               PHYSICAL STANDBY<br />  Intended State:     APPLY-ON<br />  Transport Lag:      0 seconds (computed 1 second ago)<br />  Apply Lag:          0 seconds (computed 1 second ago)<br />  Average Apply Rate: 16.00 KByte/s<br />  Real Time Query:    ON<br />  Instance(s):<br />    RDSCDB<br />Database Status:<br />SUCCESS<br />DGMGRL></pre> | DBA |

## Related resources
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-resources"></a>
+ [Configuring Amazon RDS as an Oracle PeopleSoft Database](https://d1.awsstatic.com/whitepapers/configuring-amazon-rds-as-peoplesoft-database.pdf) (AWS whitepaper)
+ [Oracle Data Guard Broker guide ](https://docs.oracle.com/en/database/oracle/oracle-database/19/dgbkr/index.html)(Oracle reference documentation)
+ [Data Guard Concepts and Administration ](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/index.html)(Oracle reference documentation)

## Additional information
<a name="add-ha-to-oracle-peoplesoft-on-amazon-rds-custom-by-using-a-read-replica-additional"></a>

**Select your database protection mode**

Oracle Data Guard provides three protection modes to configure your Data Guard environment based on your availability, protection, and performance requirements. The following table summarizes these three modes.

|
|
| Protection mode | Redo transport setting | Description |
| --- |--- |--- |
| ***MAXIMUM PERFORMANCE*** | `ASYNC` | For transactions happening on the primary database, redo data is asynchronously transmitted and written to the standby database redo log. Therefore, the performance impact is minimal.<br />`MaxPerformance` can’t provide RPO=0 because of asynchronous log shipping. |
| ***MAXIMUM PROTECTION*** | `SYNC+AFFIRM` | For transactions on the primary database, redo data is synchronously transmitted and written to the standby database redo log on disk before the transaction is acknowledged. If the standby database becomes unavailable, the primary database shuts itself down to ensure transactions are protected. |
| ***MAXIMUM AVAILABILITY*** | `SYNC+AFFIRM` | This is similar to `MaxProtection` mode, except when no acknowledgement is received from the standby database. In that case, it operates as if it were in `MaxPerformance` mode to preserve the primary database availability until it’s able to write its redo stream to a synchronized standby database again. |
| `SYNC+NOAFFIRM` | For transactions on the primary database, redo is synchronously transmitted to the standby database, and the primary waits only for acknowledgement that the redo has been received on the standby, not that it has been written to the standby disk. This mode, which is also known as `FastSync`, can provide a performance benefit at the expense of potential exposure to data loss in a special case of multiple simultaneous failures. |

Read replicas in RDS Custom for Oracle are created with maximum performance protection mode, which is also the default protection mode for Oracle Data Guard. The maximum performance mode provides the lowest performance impact on the primary database, which can help you meet the recovery point objective (RPO) requirement measured in seconds.

To work to achieve a zero data loss (RPO=0) objective, you can customize the Oracle Data Guard protection mode to `MaxAvailability` with the `SYNC+NOAFFIRM` setting for redo transport for better performance. Because commits on the primary database are acknowledged only after the corresponding redo vectors are successfully transmitted to the standby database, the network latency between the primary instance and replica can be crucial for commit-sensitive workloads. We recommend performing load testing for your workload to assess the performance impact when the read replica is customized to run in `MaxAvailability` mode.

Deploying the read replica in the same Availability Zone as the primary database provides lower network latency compared with deploying the read replica in a different Availability Zone. However, deploying the primary and read replicas in the same Availability Zone might not meet your HA requirements because, in the unlikely event of Availability Zone unavailability, both the primary instance and read replica instance are impacted.
