---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mydumper.html
---

# MyDumper
<a name="mydumper"></a>

[MyDumper](https://github.com/mydumper/mydumper#what-is-mydumper) (GitHub) is an open-source, logical migration tool that consists of two utilities:
+ MyDumper exports a consistent backup of MySQL databases. It supports backing up the database by using multiple parallel threads, up to one thread per available CPU core.
+ myloader reads the backup files created by MyDumper, connects to the target database instance, and then restores the database.

The following diagram shows the high-level steps involved in migrating a database by using a MyDumper backup file. This architecture diagram includes three options for migrating the backup file from the on-premises data center to an Amazon EC2 instance in the AWS Cloud.

![Diagram of migrating a MyDumper backup file and using myloader to restore it on the Amazon DB instance.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/images/guide-img/49694e39-c5ff-41ab-af3d-e68e9b6e3ab5/images/04675b8a-1ff5-4c83-ab23-c80a4189b1c4.png)

The following are the steps for using MyDumper to migrate a database to the AWS Cloud:

1. Install MyDumper and myloader. For instructions, see [How to install mydumper/myloader](https://github.com/mydumper/mydumper#how-to-install-mydumpermyloader) (GitHub).

1. Use MyDumper to create a backup of the source MySQL or MariaDB database. For instructions, see [How to use MyDumper](https://github.com/mydumper/mydumper#how-to-use-mydumper).

1. Move the backup file to an EC2 instance in the AWS Cloud by using one of the following approaches:

   **Approach 3A** – Mount an [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html) or [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html) file system to the on-premises server that runs your database instance. You can use AWS Direct Connect or Site-to-Site VPN to establish the connection. You can directly back up the database to the mounted file share, or you can perform the backup in two steps by backing up the database to a local file system and then uploading it to the mounted FSx or EFS volume. Next, mount the Amazon FSx or Amazon EFS file system, which is also mounted on the on-premises server, on an EC2 instance.

   **Approach 3B** – Use the AWS CLI, AWS SDK, or Amazon S3 REST API to directly move the backup file from the on-premises server to an S3 bucket. If the target S3 bucket is in an AWS Region that is far away from the data center, you can use [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html) to transfer the file more quickly. Use the [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse) file system to mount the S3 bucket on the EC2 instance.

   **Approach 3C** – Install the AWS DataSync agent at the on-premises data center, and then use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) to move the backup file to an Amazon S3 bucket. Use the [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse) file system to mount the S3 bucket on the EC2 instance.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mydumper.html)

1. Use myloader to restore the backup on the target database instance. For instructions, see [myloader usage](https://github.com/mydumper/mydumper_docs/blob/0e5cd71a5549c8a5de0105adf4d5f95953eadb67/myloader_usage.rst) (GitHub).

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
<a name="advantages-mydumper"></a>
+ MyDumper supports parallelism by using multi-threading, which improves the speed of backup and restore operations.
+ MyDumper avoids expensive character set conversion routines, which helps ensure the code is highly efficient.
+ MyDumper simplifies the data view and parsing by using dumping separate files for tables and metadata.
+ MyDumper maintains snapshots across all threads and provides accurate positions of primary and secondary logs.
+ You can use Perl Compatible Regular Expressions (PCRE) to specify whether to include or exclude tables or databases.

## Limitations
<a name="limitations-mydumper"></a>
+ You might choose a different tool if your data transformation processes require intermediate dump files in flat format instead of SQL format.
+ myloader doesn't import database user accounts automatically. If you are restoring the backup to Amazon RDS or Aurora, recreate the users with the required permissions. For more information, see [Master user account privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.MasterAccounts.html) in the Amazon RDS documentation. If you are restoring the backup to an Amazon EC2 database instance, you can manually export the source database user accounts and import them into the EC2 instance.

## Best practices
<a name="best-practices-mydumper"></a>
+ Configure MyDumper to divide each table into segments, such as 10,000 rows in each segment, and write each segment in a separate file. This makes it possible to import the data in parallel later.
+ If you are using the InnoDB engine, use the `--trx-consistency-only` option to minimize locking.
+ Using MyDumper to export the database can become read-intensive, and the process can impact overall performance of the production database. If you have a replica database instance, run the export process from the replica. Before you run the export from the replica, stop the replication SQL thread. This helps the export process run more quickly.
+ Don't export the database during peak business hours. Avoiding peak hours can stabilize the performance of your primary production database during the database export.
+ Amazon RDS for MySQL doesn't support the `keyring_aws` plugin. For more information, see [Known issues and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.KnownIssuesAndLimitations.html#MySQL.Concepts.Limits.KeyRing). To migrate the on-premises encrypted tables to the Amazon RDS instance, in the backup scripts, you need to remove `ENCRYPTION` or `DEFAULT ENCRYPTION` from the `CREATE TABLE` syntax. For encryption at rest, you can use an AWS Key Management Service (AWS KMS) key. For more information, see [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).
