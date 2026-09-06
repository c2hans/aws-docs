---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/migration-options-for-large-my-sql-and-maria-db-databases.html
---

# Migration options for large MySQL and MariaDB databases
<a name="migration-options-for-large-my-sql-and-maria-db-databases"></a>

You can choose from an extensive range of options to migrate from on-premises MySQL or MariaDB databases to Amazon Relational Database Service (Amazon RDS) or Amazon Aurora MySQL-Compatible Edition databases instances. Choosing the right migration approach and tool is essential for a successful migration, and in this guide, you evaluate the options based on your usability, data size, and downtime requirements.

The following are the common migration tools and approaches that are available to migrate multi-terabyte self-managed MySQL databases efficiently to Amazon RDS, Aurora, or Amazon Elastic Compute Cloud (Amazon EC2) database instances:
+ [Percona XtraBackup](percona-xtrabackup.md) (Physical)
+ [MyDumper](mydumper.md) (Logical)
+ [mysqldump and mysqlpump](mysqldump-and-mysqlpump.md) (Logical)
+ [Split backup](split-backup.md) (Physical, logical, or both)

The following are the common migration tools and approaches that are available to migrate multi-terabyte MySQL-compatible (such as MariaDB) databases efficiently to Amazon RDS, Aurora, or Amazon EC2 database instances:
+ [MyDumper](mydumper.md) (Logical)
+ [mysqldump and mysqlpump](mysqldump-and-mysqlpump.md) (Logical)
+ [Split backup](split-backup.md) (Physical, logical, or both)

For each migration tool, there are several approaches you can use to transfer the large database backup file to the AWS CloudOptions are provided for each tool, and you can also use Amazon S3 File Gateway. For more information, see [Amazon S3 File Gateway](amazon-s3-file-gateway.md) in this guide.
