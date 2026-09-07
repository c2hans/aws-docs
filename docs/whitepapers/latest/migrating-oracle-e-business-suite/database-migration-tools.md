---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/database-migration-tools.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database migration tools
<a name="database-migration-tools"></a>

 Various database migration techniques previously mentioned are briefly discussed here.

## Oracle RMAN backup and restore
<a name="oracle-rman-backup-and-restore"></a>

 RMAN is a backup/restore tool for Oracle database. The Oracle Secure Backup (OSB) plugin allows you to copy your backup directly to Amazon S3 and restore it to an Amazon EC2, or RDS Custom instance. Refer the following figure.

![Reference architecture diagram showing Oracle RMAN backup and restore](https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/oracle-rman-backup-restore.jpg)

## Oracle Data Guard
<a name="oracle-data-guard"></a>

 Oracle Data Guard is a feature used for HA and DR of Oracle databases. This is achieved by setting up a standby database instance in the same or different location, and mirroring the changes from the primary database instance to a standby instance in synchronous or asynchronous mode. Oracle Data Guard can also be used for database migrations. You can set up an Oracle Data Guard standby database for your on-premises or co-location Oracle instance on Amazon EC2 or Amazon RDS Custom.

 Data Guard standby is synchronized, effectively mirroring the live database on the new instance running on Amazon EC2, or RDS Custom. Lastly, a switchover to the new database instance can be performed during a suitable maintenance window. It is recommended to have a dedicated bandwidth between on-premises or co-location to the AWS Cloud through [AWS Direct Connect](https://aws.amazon.com/directconnect/).

## Oracle Data Pump
<a name="oracle-data-pump"></a>

 The Data Pump utilities allow you to move existing data in Oracle format to and from Oracle databases. For example, Data Pump export files can move data among different Oracle databases that run on the same or different OSs. This is a logical replication (data is extracted and imported into target), so it can be used for homogeneous as well as heterogeneous database migrations.

 For migrating Oracle E-Business Suite using Oracle Data Pump, refer to the [Oracle Support Note \#1926203.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140462594952288&id=1926203.1&_adf.ctrl-state=ss7c2i22z_363) - Export/Import Process for Oracle E-Business Suite 12.2 Using Oracle Database 12c (sign-in required). Similar notes exist for other database versions.

## Logical Hostnames
<a name="logical-hostnames"></a>

To reduce the number of migration steps, its recommended to use logical hostnames to reduce the complexity of the migration process. This is also useful for DR purposes. For information about the advantages of using logical hostnames, see the following support notes (sign-in required):
+ For 12c, Oracle Support Note [2246690.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2246690.1)
+ For 19c, Oracle Support Note [2617788.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2617788.1)

## Oracle transportable tablespaces
<a name="oracle-transportable-tablespaces"></a>

 The Oracle transportable tablespace feature enables you to move a set of tablespaces from one Oracle database to another. To move or copy a set of tablespaces, you must make the tablespaces read-only, copy the data files of these tablespaces, and use Export and Import to move the database information (metadata) stored in the data dictionary. After copying the data files and exporting the metadata, you can optionally put the tablespaces in read/write mode.
