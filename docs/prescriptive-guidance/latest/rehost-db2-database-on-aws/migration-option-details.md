---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/migration-option-details.html
---

# Migration option details
<a name="migration-option-details"></a>

The following sections provide details for the options that correspond to the diagram in the previous section.

## 1. Offline backup and restore
<a name="offline-backup-restore"></a>

Native Db2 backup backs up the whole database. It can be used to recreate (restore) the database to any host.
+ Offline backup and restore is the most basic way to migrate a database from on premises to AWS.
+ The Db2 on-premises database must be on the little-endian platform.
+ Downtime is required to take an offline backup, transfer the backup image to Amazon S3, and restore the database from the backup.

## 2. HADR failover
<a name="hadr-failover"></a>

Db2 HADR (high availability disaster recovery) provides a high availability solution by replicating data changes from a source database, called the primary database, to the target databases, called the standby databases. HADR supports up to three remote standby servers.
+ HADR failover is the best fit for a non-DPF instance that runs on the little-endian platform.
+ All transactions on the source database must be logged.
+ HADR supports replicating data changes from the source database (primary database) to the target database (standby database) through log streaming. HADR uses TCP/IP for communication between the primary and standby databases.
+ After full business validation, HADR can be taken down without outage, and the Db2 database on premises can be decommissioned.

## 3. Online backup and restore with transaction log shipping
<a name="online-backup-restore-with-log-shipping"></a>

Unlike offline backup and restore (option 1), online backup doesn't require downtime for the source database. It uses database transaction logs to apply changes to the target database after the backup on the source database is complete.
+ Using backup and restore with transaction log shipping is the best fit for a Db2 DPF instance that's on the little-endian platform. Because the size of a Db2 DPF databased tends to be large, the outage time for regular backup and restore (option 1) can exceed 12 hours. HADR isn't supported by Db2 DPF databases.
+ All transactions on the source database must be logged.
+ You can use backup and restore with transaction log shipping to minimize the outage window.
+ Backup and restore with log shipping can also be used for non-DPF instances. However, the HADR with failover option is easier to implement for non-DPF instances.
+ Unlike HADR failover (option 2), reverse sync isn't automatic. Set it up manually.
+ After full business validation, you can decommission the on-premises Db2 database.

## 4. Q Replication
<a name="q-replication"></a>

Q Replication is a high-volume, low-latency replication solution that uses IBM MQ message queues to transmit transactions between the source and target databases.

The most common configuration is shown in the following diagram.

![Architecture diagram showing showing Db2 on premises connect through IBM MQ and Site-to-Site VPN to Db2 on EC2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/images/guide-img/4110482b-c82b-44be-8423-7af4c399c9a0/images/870e1acf-8fa3-44c2-8328-d97d180ae600.png)

IBM MQ runs on the same server as Db2. There are two IBM MQ instances, one on the on-premises server and the other one on Amazon EC2. The Capture program runs on the source database. It reads the transaction logs and sends committed changes (insert, update, or delete) to IBM MQ on premises. IBM MQ on premises sends the messages through AWS Site-to-Site VPN to IBM MQ on Amazon EC2. The Apply program runs on the EC2 instance with the target database. First, it does a full load on tables. Then, it reads change data messages from IBM MQ on Amazon EC2 and applies them to the target tables.
+ Db2 on premises is the source and Db2 on Amazon EC2 is the target. Both databases are online.
+ The on-premises Db2 database can be on any platform family.
+ All transactions on the source database must be logged.
+ IBM MQ provides high performance, high availability, and guaranteed message delivery.
+ Messages are deleted from IBM MQ after changes have been committed on the target database.
+ Two-way replication is a fallback option. However, it requires additional setup.
+ Schema migration is required. For details, see the [Schema migration](#schema-migration) section.
+ Q replication requires an [extra license starting with version 11.5](https://www.ibm.com/support/pages/ibm-db2-11-changes-data-replication).
+ After successful cutover, stop replication, and decommission the IBM MQ instances. You can also decommission the on-premises database if you want.

## 5. SQL Replication
<a name="5-sql-replication"></a>

SQL Replication consists of the following major components: Capture, Apply, GUI and CLI interface, and Alert monitor.

The Capture program runs on the source database. It reads the transaction logs and saves committed changes (insert, update, or delete) to changed data (CD) tables. There is one CD table for each source table.

The Db2 commit points for the units of work are stored in the unit of work (UOW) table. At a point in time specified by the user, the Capture program deletes data that is no longer needed in the CD and UOW tables. This is called pruning.

The Apply program runs on the target database. It connects to the source database, fetches the data stored in the CD tables, stores the fetched rows into one or more spill files, and then applies them into the target database.
+ The on-premises Db2 database can be on any platform family.
+ All transactions on the source database must be logged.
+ Overhead on the source database is considered high because each write must run multiple times (on the based table, the CD table, and the UOW table). In general, we recommend SQL Replication for systems that have low write traffic.
+ Two-way replication is a fallback option. However, it requires additional setup.
+ Schema migration is required. For details, see the [Schema migration](#schema-migration) section for details.
+ Unlike Q Replication, SQL Replication is included in all Db2 editions. It doesn't require an extra license.
+ After successful cutover, stop replication, and decommission the on-premises database if you want.

## 6. AWS DMS
<a name="cdc"></a>

[AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) is a managed migration and replication service that helps move your database and analytics workloads to AWS securely, and with minimal downtime and zero data loss.
+ An AWS DMS replication instance performs your database migration.
+ AWS DMS source and target endpoints enable the AWS DMS instance to connect the source and target database for migration.
+ An AWS DMS task connects to the source endpoint and replicates the data to the target endpoint.
+ You can turn on data validation to verify that the data is migrated accurately from the source to the target.
+ You can enable logging by using Amazon CloudWatch.

## 7. Third-party replication tools
<a name="third-party"></a>

Third-party replication tools such as [Infosphere CDC,](https://www.ibm.com/docs/da/iis/11.7?topic=sources-infosphere-change-data-capture) [Qlik Replicate](https://help.qlik.com/en-US/replicate/May2025/Content/Replicate/Main/Introduction/replicat_concepts.htm), [Precisely real-time CDC](https://www.precisely.com/solution/real-time-cdc-and-etl-solutions), and [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) can support data migration for Db2 for LUW as a target.

For Qlik Replicate, Db2 for LUW needs to be set up as an Open Database Connectivity (ODBC) target.

## 8. InfoSphere Optim High Performance Unload and load
<a name="hpu"></a>

InfoSphere Optim High Performance Unload bypasses the Db2 engine and unloads data directly from physical files.
+ Optim High Performance Unload can generally unload Db2 data several times faster than the Db2 `EXPORT` command. It can bypass the Db2 database manager by reading data files directly from disk. It also avoids scanning the Db2 table multiple times when specifying multiple `SELECT` statements or multiple file formats in a control file.
+ Optim High Performance Unload can also unload Db2 data from the backup image. This means you that can run Optim High Performance Unload on another machine to reduce the performance impact on the source database server. This is very useful for large historical tables or table partitions.
+ The data output files can be transferred to Amazon S3, which can be accessed by the Db2 EC2 server.
+ Db2 load supports direct access to Amazon S3. For example, you can use the following command:

  ```
  db2 load from DB2REMOTE://<storage access alias>//<storage-path>/<file-name> replace into mytable
  ```
+ Schema migration is required. For details, see the [Schema migration](#schema-migration) section.
+ InfoSphere Optim High Performance Unload requires an extra license.

## 9. LOAD FROM CURSOR
<a name="load-from-cursor"></a>

LOAD FROM CURSOR is a Db2 load utility option that uses a table on the target as the source, without unloading the data into a file.
+ A federated link needs to be created on the target database and linked to the source database.
+ For each table, a nickname is created linking to the on-premises source table. If many tables are involved, we recommend using an automation script to generate the nicknames and load statements.
+ LOAD FROM CURSOR bypasses staging storage, and tables can be separated into different steams to run in parallel. We recommend monitoring network congestion during large loads.
+ By manipulating the `SELECT` statement in the cursor definition, you can select the full table, skip data that you don't want to load, or split a range-based partition table into multiple load statements (for example, quarterly and monthly).
+ Schema migration is required. For details, see the [Schema migration](#schema-migration) section.

## 10. db2move
<a name="db2move"></a>

The `db2move` command, when used in the `EXPORT`, `IMPORT`, or `LOAD` modes, facilitates the movement of large numbers of tables between Db2 databases.
+ Schema migration is required. For details, see the [Schema migration](#schema-migration) section.
+ You can use the `db2move` command to unload the data from tables into files, and to load the data into Db2 tables. This is useful because the db2move utility can download all tables in the source database and load them to the target database with a few commands.

1. To export all tables in the source database with LOBs to `<lob-path>`, run the following command:

   ```
   db2move <db-name> export -l /<lob-path>/<lobfile>
   ```

1. Transfer the files to Amazon S3, where they can be retrieved by the Db2 EC2 server.

1. To load all tables into the target database, run the following command:

   ```
   db2move <db-name> load -l /<lob-path>/<lobfile>
   ```

## Schema migration
<a name="schema-migration"></a>

For backup and restore, HADR failover, and backup and restore with log shipping (options 1–3), schema migration is included in data migration. No additional step is required.

For logical replication and big-endian migration (options 4–10), you must manually create the database and schema on the target. We recommend avoiding schema changes on the source during migration. The migration can take multiple days, although the actual outage time is much shorter.

On the source server:

1. Extract the data definition language (DDL) by using the db2look utility, and save the output to `db2look.ddl`.

1. Transfer `db2look.ddl` to Amazon S3.

On the target server:

1. Get `db2look.ddl` from Amazon S3.

1. Take out the foreign key constraint, check constraint, and `CREATE TRIGGER` statements. Save them into separated files. This process isn't difficult because db2look output groups these statements together.

1. Create a database and schema without the foreign key, check constraint, and trigger.

1. Convert tables with identity columns that have `GENERATED ALWAYS` to `GENERATED BY DEFAULT`.

1. For logical replication options 4, 5, 6, and 7, start replication. You can recreate foreign keys and check constraints after the full load completes. However, you must recreate triggers before cutover.

1. For options 8, 9, and 10, after the data load is complete, recreate foreign keys, check constraints, and triggers.

1. Revert tables with identity columns that you changed in step 4 back to `GENERATED ALWAYS`.

1. Reseed identity columns and sequences before cutover.
