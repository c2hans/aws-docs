---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/introduction.html
---

# Backup and restore options for SQL Server on Amazon EC2
<a name="introduction"></a>

*Yogi Barot and Reghardt van Rooyen, Amazon Web Services*

Customers have asked for the right solution to safeguard their data on [Microsoft SQL Server on Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql.html) and meet their current requirements for Recovery Point Objective (RPO), the maximum acceptable amount of time since the last backup, and Recovery Time Objective (RTO), the maximum acceptable delay between the interruption of service and restoration of service. When you are running SQL Server on EC2 instances, you have multiple options for creating backups of the data and also restoring it.

 Backup strategies for safeguarding data for SQL Server on Amazon EC2 include the following:
+ Server-level backup using [Windows Volume Shadow Copy Service (VSS)](https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service)-enabled Amazon Elastic Block Store (Amazon EBS) snapshots or [AWS Backup](https://aws.amazon.com/backup/)
+ Database-level backup using [native backup and restore](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16)

When you choose database-level native backup, you have the following storage options:
+ An Amazon EBS volume
+ An Amazon FSx for Windows File Server file system
+ Amazon Simple Storage Service (Amazon S3), using AWS Storage Gateway

This guide compares these options, including the benefits and limitations of each. It will also compare the performance of each option for a sample 1 TB database.
