---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/percona-xtrabackup.html
---

# Percona XtraBackup
<a name="percona-xtrabackup"></a>

**Important**
Percona XtraBackup is not supported for MariaDB versions 10.3 or later and is only partially supported for versions 10.1 and 10.2.

[Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/8.0/index.html) is a common open-source warm backup software for MySQL and MariaDB that makes non-blocking backups for InnoDB and XtraDB storage engines. It works with MySQL or MariaDB servers. For more information about the tool and some of its features and benefits, see [About Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/8.0/about-xtrabackup.html) in the Percona XtraBackup documentation.

This tool uses the physical migration approach. It directly copies the MySQL or MariaDB data directory and the files within it. For large databases, such as those larger than 100 GB, this can provide a significantly better restoration time than some other tools. You create a backup of the on-premises source database, migrate the backup files to the cloud, and then restore the backup on the new, target database instance.

The following diagram shows the high-level steps involved in migrating a database by using an Percona XtraBackup backup file. Depending on the size of the backup file, there are two options available for transferring the backup to an Amazon Simple Storage Service (Amazon S3) bucket in the AWS Cloud.

![Diagram of migrating a Percona XtraBackup file and restoring it on an Amazon DB instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/images/guide-img/49694e39-c5ff-41ab-af3d-e68e9b6e3ab5/images/fae4f7b5-34d2-43eb-a128-22c2182dd7ef.png)

The following are the steps for using Percona XtraBackup to migrate a database to the AWS Cloud:

1. Install Percona XtraBackup on the on-premises server. If you're using Amazon Aurora MySQL version 2 or Amazon RDS, see [Installing Percona XtraBackup 2.4](https://docs.percona.com/percona-xtrabackup/2.4/installation.html). If you're using Amazon Aurora MySQL version 3, see [Installing Percona XtraBackup 8.0](https://docs.percona.com/percona-xtrabackup/8.0/installation.html) in the Percona XtraBackup documentation.

1. Create a full backup of the source MySQL or MariaDB database. For instructions for Percona XtraBackup 2.4, see [Full backup](https://docs.percona.com/percona-xtrabackup/2.4/backup_scenarios/full_backup.html). For instructions for Percona XtraBackup 8.0, see [Create a full backup](https://docs.percona.com/percona-xtrabackup/8.0/create-full-backup.html).

1. Transfer the backup files over the internet by using an approved service or tool in your organization, such as the following:
   + [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
   + [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html)
   + [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
   + [Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) (For more information, see [Amazon S3 File Gateway](amazon-s3-file-gateway.md) in this guide.)
   + [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/getting-started/hands-on/backup-to-s3-cli/)

1. From the Amazon S3 bucket, restore the backup files to the target database instance. For instructions, see the following:
   + For Aurora MySQL-Compatible Edition, see [Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3.Restore) in the Amazon RDS documentation.
   + For Amazon RDS for MySQL or for Amazon EC2, see [Importing data into a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.Other.html).
   + For Amazon RDS for MariaDB or for Amazon EC2, see [Importing data into a MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Procedural.Importing.html).

1. (Optional) You can set up replication between the source database and the target database instance. You can use binary log (binlog) replication to reduce downtime. For more information, see the following:
   + [Setting the replication source configuration](https://dev.mysql.com/doc/refman/5.7/en/replication-howto-masterbaseconfig.html) in the MySQL documentation
   + For Amazon Aurora, see the following:
     + [Synchronizing the Amazon Aurora MySQL DB cluster with the MySQL database using replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3.RepSync) in the Aurora documentation
     + [Using binlog replication in Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html) in the Aurora documentation
   + For Amazon RDS, see the following:
     + [Working with MySQL replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.html) in the Amazon RDS documentation
     + [Working with MariaDB replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.html) in the Amazon RDS documentation
   + For Amazon EC2, see the following:
     + [Setting Up Binary Log File Position Based Replication](https://dev.mysql.com/doc/mysql-replication-excerpt/8.0/en/replication-howto.html) in the MySQL documentation
     + [Setting Up Replicas](https://dev.mysql.com/doc/refman/8.0/en/replication-setup-replicas.html) in the MySQL documentation
     + [Setting Up Replication](https://mariadb.com/kb/en/setting-up-replication/) in the MariaDB documentation

## Advantages
<a name="advantages-percona-xtrabackup"></a>
+ Because Percona XtraBackup uses a physical migration approach, the restore process is typically faster than tools that use a logical migration approach. This is because the performance is limited by the disk or network throughput rather than the compute resources necessary for data processing.
+ Because the restore process is a direct copy of the files from the S3 bucket to the target database instance, Percona XtraBackup files typically restore faster than backup files created with other tools.
+ Percona XtraBackup is adaptable. For example, it supports multiple threads to help you copy files faster and supports compression to reduce the size of the backup.

## Limitations
<a name="limitations-percona-xtrabackup"></a>
+ Offline backup is not possible because Percona XtraBackup must have access to the source database server.
+ Percona XtraBackup can be used only on systems with identical system architectures. For example, it is not possible to restore a backup of a source database running on Intel for Windows Server to an ARM for Linux target server.
+ Percona XtraBackup isn't supported for MariaDB version 10.3 or later, and it is only partially supported for MariaDB version 10.2 and version 10.1. For more information, see [Percona XtraBackup Overview: Compatibility with MariaDB](https://mariadb.com/kb/en/percona-xtrabackup-overview/#compatibility-with-mariadb) in the MariaDB knowledge base.
+ You cannot use Percona XtraBackup to restore a source MariaDB database to a target MySQL database instance, such as Amazon RDS for MySQL or Aurora MySQL-Compatible.
+ The total volume of data and number of objects you can store in an S3 bucket are unlimited, however, the maximum file size is 5 TB. If your backup file exceeds 5 TB, you can split it up into multiple, smaller files.
+ When the `innodb_file_per_table` setting is off, Percona XtraBackup doesn't support partial backups that use `--tables`, `--tables-exclude`, `--tables-file`, `--databases`, `--databases-exclude`, or `--databases-file`. For more information for Percona XtraBackup version 2.4, see [Partial backups](https://docs.percona.com/percona-xtrabackup/2.4/innobackupex/partial_backups_innobackupex.html). For more information for Percona XtraBackup version 8.0, see [Create a partial backup](https://docs.percona.com/percona-xtrabackup/8.0/create-partial-backup.html).

## Best practices
<a name="best-practices-percona-xtrabackup"></a>
+ To improve the performance of the backup process, do the following:
  + Copy multiple files in parallel by using [--parallel=<threads>](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#-parallel)
  + Compress multiple files in parallel by using [--compress-threads=<threads>](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#-compress-threads)
  + Increase memory by using [--use-memory=<size>](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#-use-memory)
  + Encrypt multiple files in parallel by using [--encrypt-threads=<threads>](https://docs.percona.com/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html#-encrypt-threads)
+ Ensure that there is sufficient space on the source server to take the database backup files.
+ Generate the database backup with the Percona xbstream (.xbstream) format file. For more information, see [The xbstream binary overview](https://docs.percona.com/percona-xtrabackup/8.0/xbstream-binary-overview.html) in the Percona XtraBackup documentation.
