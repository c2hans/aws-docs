---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/compare-features.html
---

# Comparing Oracle Database EE and SE2 features
<a name="compare-features"></a>

The following table is a short version of the list of Oracle Database Enterprise Edition (EE) features and possible alternatives in Amazon RDS for Oracle Standard Edition 2 (SE2). For a comprehensive list, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/dblic/Licensing-Information.html#GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87).

|
|
| Functional area | Feature or option | EE | SE2 | Notes |
| --- |--- |--- |--- |--- |
| High availability | Oracle Data Guard (extra cost) | Yes | No | The [Multi-AZ (Availability Zone)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) feature of Amazon RDS replicates database updates across two Availability Zones to increase durability and availability. Amazon RDS will automatically fail over to the standby for planned maintenance and unplanned disruptions. |
| High availability | Oracle Active Data Guard | Yes | No | You can serve read-only traffic from a replica database instance by using the change data capture (CDC) feature of AWS Database Migration Service (AWS DMS) to replicate changes from your Amazon RDS for Oracle SE2 instance. |
| High availability | Oracle Real Application Clusters (RAC) One Node (extra cost) | Yes | No | The Amazon RDS Multi-AZ feature applies. |
| High availability | Rolling upgrades—patch set, database, and operating system | Yes | No | For [database software upgrades in Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.html#USER_UpgradeDBInstance.Oracle.Overview.multi-az), Amazon RDS simultaneously upgrades both the primary and standby database. For operating system (OS) upgrades in Multi-AZ deployments, Amazon RDS upgrades the standby instance first. It then fails over the primary to the standby before upgrading the primary instance. This reduces the downtime window for OS upgrades. |
| High availability | Block change tracking for fast incremental backup | Yes | No | With [Amazon RDS backups](https://aws.amazon.com/rds/features/backup/), the first snapshot of your DB instance is a full copy. Subsequent backups are incremental backups of blocks that have changed since the last full backup. You can restore your Amazon RDS for Oracle database instance from automated or manual snapshots. |
| High availability | Parallel backup and recovery | Yes | No |
| High availability | `FLASHBACK DATABASE` command | Yes | No | You can restore your DB instance to any specific time during the backup retention period by using the [point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) feature of Amazon RDS. |
| High availability | Online index rebuild | Yes | No | Where possible, plan for these activities during a downtime window. |
| High availability | Online table organization | Yes | No |
| High availability | Online table redefinition | Yes | No |
| High availability | Online datafile move | Yes | No |
| Manageability | Automatic Workload Repository (AWR) | Yes | No | You can use [Oracle Statspack](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Statspack.html), an option pack in Oracle SE2, in place of Oracle AWR.<br />[Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) is a database performance monitoring and tuning tool built for the cloud. You can use the tool dashboard to detect performance problems by evaluating top waits, top SQL statements, top hosts, and top users. |
| Manageability | SQL plan management | Yes | Yes | You can use stored outlines, hints, and SQL plan baselines to tune your queries in Amazon RDS for Oracle SE2. |
| Scalability | CPU restrictions | No | Yes | SE2 is capped at a maximum of two CPU sockets. Each SE2 database is automatically capped to use a maximum of 16 concurrent user threads. |
| Scalability | Oracle Real Application Clusters (RAC) (extra cost) | Yes | No | You can scale your Amazon RDS for Oracle SE2 instance vertically to address the growing demands of an application.<br />There is minimal downtime when you are scaling up in a Multi-AZ environment. The standby database gets upgraded first, then a failover will occur to the newly sized database. <br />When you scale up in a Single-AZ environment, the instance will be unavailable during the scale operation. |
| Security | Column-level and tablespace encryption | Yes | No | Amazon RDS can [encrypt your Amazon RDS DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html). Data that is encrypted at rest includes the underlying storage for DB instances, its automated backups, read replicas, and snapshots. |
| Snapshots and cloning | Storage Snapshot Optimization | Yes | No | Amazon RDS supports user-initiated snapshot creation. For more information, see [Amazon RDS backup and restore](https://aws.amazon.com/rds/features/backup/). |
| Data warehousing | Oracle Partitioning | Yes | No | Depending on your specific use case, you can implement a partitioning feature for tables in Oracle Database SE2 by using a single view accessing multiple subtables and the `INSTEAD OF` trigger. For more information, see the AWS Database blog post [Implementing table partitioning in Oracle Standard Edition: Part 1](https://aws.amazon.com/blogs/database/implementing-table-partitioning-in-oracle-standard-edition-part-1/). |
