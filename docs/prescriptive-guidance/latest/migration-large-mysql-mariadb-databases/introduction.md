---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/introduction.html
---

# Migrating large, multi-terabyte MySQL or MariaDB databases to AWS
<a name="introduction"></a>

*Babaiah Valluru and Ankur Bhanawat, Amazon Web Services*

Many organizations that have on-premises MySQL and MariaDB database servers are interested in migrating their database workloads to the AWS Cloud. Many choose Amazon Relational Database Service (Amazon RDS) for MariaDB, Amazon RDS for MySQL, or Amazon Aurora MySQL-Compatible Edition. [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) is designed to make it easy to set up, operate, and scale relational databases in the cloud. [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is part of Amazon RDS, and it offers built-in security, continuous backups, server-free computing, up to 15 read replicas, automated multi-Region replication, and integration with other AWS services.

Although migrating to one of these AWS services can provide many benefits, database migration is one of the most time-consuming and critical tasks that database administrators must perform. It requires precise planning and implementation to migrate large databases and make sure that the performance of the migrated workload is equivalent or improved. In this guide, *large* databases can refer to a single, multi-terabyte database or refer to many large databases that add up to multiple terabytes of data. Selecting the right migration services and tools is key to the success of the migration. There are two common approaches for migrating a database: logical and physical. For more information about these approaches, see the [MySQL](https://dev.mysql.com/doc/refman/8.0/en/backup-types.html) and [MariaDB](https://mariadb.com/kb/en/backup-and-restore-overview/) documentation.

This guide discusses various open-source or third-party tools that you can use to migrate large, on-premises, multi-terabyte MySQL and MariaDB databases to Amazon RDS for MariaDB, Amazon RDS for MySQL, or Amazon Aurora MySQL-Compatible Edition. The options discussed in this guide use logical or physical migration approaches, and each option includes multiple approaches for transferring the large database backup files from the on-premises data center to the cloud, where you can restore the database from the backup file.

## Intended audience
<a name="intended-audience"></a>

This guide is for program database administrators, database engineers, migration engineers, project managers, and operations or infrastructure managers who are planning to migrate their MySQL or MariaDB databases to the AWS Cloud.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The goal of this guide is to help you:
+ Choose a migration approach for a large database that best fits your use case and environment.
+ Avoid delays and financial losses that can occur when the migration strategy is flawed.
+ Learn about the advantages and limitations of each migration option.
+ Learn about different approaches you can use to transfer large database backup files from your on-premises data center to the AWS Cloud.
+ Review overall best practices for migrating large databases and also review best practices for each tool, which can help you more efficiently migrate the database.
