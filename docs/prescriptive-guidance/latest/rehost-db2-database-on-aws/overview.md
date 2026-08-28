---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/overview.html
---

# Overview
<a name="overview"></a>

The most basic way to move large amounts of data to AWS is by using database backup. However, a [Db2 for LUW](https://www.ibm.com/products/db2) database backup from one platform family can be restored only to a system within the same platform family. Db2 LUW supports the following three platform families:
+ Big-endian Linux and UNIX
+ Little-endian Linux and UNIX
+ Windows

When migrating Db2 from on premises to Amazon EC2, you have the following options:
+ Rehosting an on-premises Db2 database running on the little-endian Linux or Windows platforms is relatively easy because you can use regular backup and restore to move data. If you need a minimum-outage migration, you can use [IBM Db2 HADR (high availability and disaster recovery)](https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr) or backup and recovery with log shipping.
+ Rehosting an on-premises Db2 database running on the big-endian platform is much more challenging because the database backup and logs can't be used. Because IBM doesn't provide a native tool to convert data between platform families, a full unload and reload is required. These operations can be time-consuming, and they usually require a longer outage window.
+ If you have Db2 workloads on the big-endian platform but can't afford a long outage window, we recommend a logical replication solution.

This guide provides information about the following options:
+ Offline backup and restore
+ High availability disaster recovery (HADR) failover
+ Online backup and restore with log shipping
+ IBM Q Replication
+ IBM SQL Replication
+ AWS Database Migration Service (AWS DMS)
+ Other third-party replication tools, including IBM InfoSphere Change Data Capture (CDC)
+ IBM InfoSphere Optim High Performance Unload and load
+ LOAD FROM CURSOR
+ db2move utility

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
