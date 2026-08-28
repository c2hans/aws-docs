---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mysqldump-and-mysqlpump.html
---

# mysqldump and mysqlpump
<a name="mysqldump-and-mysqlpump"></a>

[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) and [mysqlpump](https://dev.mysql.com/doc/refman/8.0/en/mysqlpump.html) are native database backup tools for MySQL. MariaDB supports mysqldump but doesn't support mysqlpump. Both of these tools create logical backups and are part of the MySQL client programs. mysqldump supports single-threaded processing. mysqlpump supports parallel processing of databases and objects within databases, to speed up the dump process. It was introduced in MySQL version 5.7.8. mysqlpump was removed in MySQL version 8.4.

The following diagram shows the high-level steps involved in migrating a database by using a mysqldump or mysqlpump backup file.

![Diagram of migrating a mysqldump or mysqlpump backup file and restoring it on an Amazon DB instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/images/guide-img/49694e39-c5ff-41ab-af3d-e68e9b6e3ab5/images/5fefd2b1-1ee4-4eb7-a36e-7b7f4982b944.png)

The following are the steps for using mysqldump or mysqlpump to migrate a database to the AWS Cloud:

1. Install MySQL Shell on the on-premises server. For instructions, see [Installing MySQL Shell](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html) in the MySQL documentation. This installs both mysqldump and mysqlpump.

1. Using mysqldump or mysqlpump, create a backup of the source, on-premises database. For instructions, see [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) and [mysqlpump](https://dev.mysql.com/doc/refman/8.0/en/mysqlpump.html) in the MySQL documentation, or see [Making Backups with mysqldump](https://mariadb.com/kb/en/making-backups-with-mysqldump/) in the MariaDB documentation. For more information about invoking MySQL programs and specifying options, see [Using MySQL programs](https://dev.mysql.com/doc/refman/8.0/en/programs-using.html).

1. Move the backup file to an Amazon EC2 instance in the AWS Cloud by using one of the following approaches:

   **Approach** **3A** – Mount an [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html) or [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html) file system to the on-premises server that runs your database instance. You can use AWS Direct Connect or Site-to-Site VPN to establish the connection. You can directly back up the database to the mounted file share, or you can perform the backup in two steps by backing up the database to a local file system and then uploading it to the mounted FSx or EFS volume. Next, mount the Amazon FSx or Amazon EFS file system, which is also mounted on the on-premises server, on an EC2 instance.

   **Approach 3B** – Use the AWS CLI, AWS SDK, or Amazon S3 REST API to directly move the backup file from the on-premises server to an S3 bucket. If the target S3 bucket is in an AWS Region that is far away from the data center, you can use [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html) to transfer the file more quickly. Use the [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse) file system to mount the S3 bucket on the EC2 instance.

   **Approach 3C** – Install the AWS DataSync agent at the on-premises data center, and then use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) to move the backup file to an Amazon S3 bucket. Use the [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse) file system to mount the S3 bucket on the EC2 instance.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mysqldump-and-mysqlpump.html)

1. Use the native restore method to restore the backup on the target database. For instructions, see [Reloading SQL-Format Backups](https://dev.mysql.com/doc/refman/8.0/en/reloading-sql-format-dumps.html) in the MySQL documentation, or see [Restoring Data from Dump Files](https://mariadb.com/kb/en/restoring-data-from-dump-files/) in the MariaDB documentation.

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
<a name="advantages-mysqlpump-mysqldump"></a>
+ mysqldump and mysqlpump are included in the MySQL Server installation
+ The backup files generated by these tools are in a more readable format.
+ Before restoring the backup file, you can modify the resultant .sql file by using a standard text editor.
+ You can back up a specific table, database, or even a particular data selection.
+ mysqldump and mysqlpump are machine-architecture independent.

## Limitations
<a name="limitations-mysqlpump-mysqldump"></a>
+ mysqldump is a single-threaded backup process. Performance for taking a backup is good for small databases, but it can become inefficient when the backup size is larger than 10 GB.
+ Backup files in logical format are voluminous, especially when saved as text, and often slow to create and restore.
+ Data restoration can be slow because reapplying SQL statements in the target DB instance involves intensive disk I/O and CPU processing for insertion, index creation, and referential integrity constraints enforcement.
+ The mysqlpump utility is not supported for MySQL versions earlier than 5.7.8 or for versions 8.4 and later.
+ By default, mysqlpump does not take a backup of the system databases, such as `performance_schema` or `sys`. To backup part of the system database, explicitly name it in the command line.
+ mysqldump does not backup InnoDB `CREATE TABLESPACE` statements.

|
|
| Note: Backups of `CREATE TABLESPACE` statements and system databases are useful only when you are restoring MySQL or MariaDB database backups to an EC2 instance. These backups are not used for Amazon RDS or Aurora. |
| --- |

## Best practices
<a name="best-practices-mysqlpump-mysqldump"></a>
+ When you're restoring the database backup, disable the key checks, such as `FOREIGN_KEY_CHECKS`, at the session level in the target database . This increases the restoration speed.
+ Make sure the database user has sufficient [privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html) to create and restore the backup.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
