---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/introduction.html
---

# Migrating bulky Oracle databases to AWS for cross-platform environments
<a name="introduction"></a>

*Incheol Roh, Amazon Web Services*

When migrating an Oracle database larger than 100 TB from on premises to the Amazon Web Services (AWS) Cloud, migration downtime is a serious factor. In particular, if the system is a mission-critical system, such as global enterprise resource planning (ERP) or a manufacturing execution system (MES), you want to reduce the downtime as much as possible for business continuity.

There are many ways to migrate Oracle databases between systems that have different endian formats, as mentioned in [Strategies for Migrating Oracle Databases to AWS](https://d1.awsstatic.com/whitepapers/strategies-for-migrating-oracle-database-to-aws.pdf). One of these approaches is Oracle cross-platform transportable tablespaces (XTTS), which you can use to reduce the migration downtime from days to hours.

Combining Oracle XTTS with Oracle Recovery Manager (RMAN) incremental backups can significantly reduce the amount of downtime required to move data between platforms running different endian formats.

This guide introduces how to use [AWS Snowball](https://aws.amazon.com/snowball/), [AWS Direct Connect](https://aws.amazon.com/directconnect/), and [Amazon FSx for Lustre](https://aws.amazon.com/fsx/) with Oracle XTTS with RMAN incremental backups . The goal of this approach is to minimize migration downtime in environments that have very large datasets.
