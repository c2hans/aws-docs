---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/prepare.html
---

# Phase 1: Prepare
<a name="prepare"></a>

During the preparation phase, assess your existing database and identify its dependencies. The following sections cover the main items to evaluate before you plan the migration.

## Dependency analysis
<a name="dependency-analysis"></a>

When preparing for the Oracle migration, identify interdependencies and their impact on the interfacing applications. Answer the following initial questions:
+ **Dependency check** – Identify applications that connect to the database directly. To avoid any latency concerns, we recommend that you migrate the applications along with the database. For applications that access data indirectly through an API, identify the performance impact and the downtime requirement for migration.
+ **Access to other databases** – Oracle Database provides a mechanism for accessing data in another database over a network by using a [database link](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-DATABASE-LINK.html). The database link helps you read from, and write to, tables in a remote database. For example, a reporting application might fetch data from a centralized database that uses database links to fetch data from other databases in the same business unit. It's important to identify all such connections and recreate the database links after migration.
+ **External jobs** – Sometimes database jobs are scheduled and controlled outside the database. To avoid any downstream impact, make sure that those jobs continue to run during the database migration.
+ **Data center dependencies** – During migration there might be times when some of your systems are in the cloud whereas other systems are still in the on-premises data center. Network latency plays a big factor in these configurations. Decide whether you want to migrate applications and databases that are sensitive to latency together, or if you want to move the functionality to the migrating database. In either case, we recommend that you migrate your applications to the same Availability Zone as your migrated database to avoid any network latency.
+ **Access to host** – Some applications create reports that are stored in a file system on a database server. When you migrate your database, you can decide to modernize your report generation as well by saving the reports in cloud-native storage. Based on how complex it might be to change report generation, you can decide to use [Amazon EC2](https://aws.amazon.com/ec2/), [Amazon RDS](https://aws.amazon.com/rds/), or [Amazon RDS Custom](https://aws.amazon.com/rds/custom/) as a target for the Oracle database.
+ **Specific database options, features, and patch requirements** – Review the Oracle database features you use and your requirements after migration. Feature use and post-migration needs help determine the database setup in the cloud. One-off patches in the source Oracle database might require your database to be migrated to Amazon RDS Custom or an EC2 instance.

## Availability requirements
<a name="availability"></a>

Depending on business needs, some databases must be operational all day, every day. Other databases can afford downtime after business hours or during weekends. In the preparation phase of migration planning, it's important to understand the business impact of database downtime and choose the appropriate migration strategy. For example, online migration has minimal downtime, whereas offline migration involves a longer downtime period.

## Workload analysis
<a name="workload-analysis"></a>

Understanding the nature of your database workload helps you determine your database migration strategy. The window for migration and any downtime needed depend on the workload. Workloads can range from being highly transactional to consisting mostly of batch jobs and reporting. To help with your migration planning and strategy, identify where your workload lies in this spectrum.

Tools are available to help you qualify your database workload. The tools that you can use depend on your Oracle Database license and include the following:
+ Host metrics such as [CPU](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emadm/overview-performance-and-resource-metrics.html#GUID-9212FAF0-BFE1-4DB4-A346-F7039DE69113), I/O, and memory help you decide the instance and storage requirements for your databases in the cloud.
+ Oracle reports such as [Automatic Workload Repository (AWR)](https://www.oracle.com/technetwork/database/manageability/diag-pack-ow09-133950.pdf) for Oracle Database Enterprise Edition or [Statspack](https://www.oracle.com/technetwork/database/performance/statspack-129989.pdf) for Standard Edition help you determine the nature of transactions that occur in your database.
+ Redo and [archive log generation](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=427729352629787&parent=EXTERNAL_SEARCH&sourceId=HOWTO&id=2373477.1&_afrWindowMode=0&_adf.ctrl-state=e285gjpp6_4) help you determine the rate of change that occurs in your database.
