---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/split-backup.html
---

# Split backup
<a name="split-backup"></a>

A *split backup* strategy is when you migrate a large database server by dividing the backup into multiple parts. You might use different approaches to migrate each part of the backup. This can be the best option for the following use cases:
+ **Large database server but small individual databases** – This is a good approach when the size of the total database server is multiple TBs but the size of each individual, independent user database is less than 1 TB. To reduce the overall migration period, you can migrate individual database separately and in parallel.

  Let's use an example of an on-premises, 2 TB database server. This server consists of four databases that are each 0.5 TB. You can take backups of each individual database separately. When restoring the backup, you can either restore all databases on an instance in parallel, or if the databases are independent, you can restore each backup on a separate instance. It's a best practice to restore independent databases on separate instances, instead of restoring them on the same instance. For more information, see Best practices in this guide.
+ **Large database server but small individual database tables** – This is a good approach when the size of the total database server is multiple TBs but the size of each independent database table is less than 1 TB. To reduce the overall migration period, you can migrate independent tables individually.

  Let's use an example of a single user database that is 1 TB, and it is the only database in an on-premises database server. There are 10 tables in the database, and each is 100 GB. You can take backups of each individual table separately. When restoring the backup, you can restore all tables on an instance in parallel.
+ **A database contains both transactional and non-transactional workload tables** – Similar to the previous use case, you can use a split backup approach when you have both transactional and non-transactional workload tables in the same database.

  Let's use an example of a 2 TB database that consists of 0.5 TB of critical workload tables used for online transaction processing (OLTP) and a single 1.5 TB table used for archiving old data. You can take the backup of all database objects except the archive table as a single-transaction and consistent backup. Then, you take another, separate backup of the archive table only. For the archive table backup, you can also consider taking multiple, parallel backups by using conditions to split the number of rows in the backup file. The following is an example:

  ```
  mysqldump -p your_db1 --tables your_table1 --where="column1 between 1 and 1000000 " > your_table1_part1.sql
  mysqldump -p your_db1 --tables your_table1 --where="column1 between 1000001 and 2000000 " > your_table1_part2.sql
  mysqldump -p your_db1 --tables your_table1 --where="column1 > 2000000 " > your_table1_part3.sql
  ```

  When restoring the backup files, you can restore transactional workload backup and the archive table backup in parallel.
+ **Compute resource limitations** – If you have limited compute resources in the on-premises server, such as CPU, memory, or disk I/O, this can affect stability and performance when taking the backup. Instead of taking a complete backup, you can divide it into parts.

  For example, an on-premises production server might be heavily loaded with workloads and have limited CPU resources. If you take a single-run backup of a multi-terabyte database on this server, it can consume additional CPU resources and adversely affect the production server. Instead of taking the complete database backup, divide the backup into multiple parts, such as 2–3 tables each.
