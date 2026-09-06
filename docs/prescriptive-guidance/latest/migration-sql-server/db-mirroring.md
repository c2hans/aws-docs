---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/db-mirroring.html
---

# Database mirroring
<a name="db-mirroring"></a>

You can use database mirroring to set up a hybrid cloud environment for your SQL Server databases. This option requires SQL Server Enterprise edition. In this scenario, your principal SQL Server database runs on premises, and you create a warm standby in the cloud. You replicate your data asynchronously, and perform a manual failover when you're ready for cutover. After you have migrated the database to the AWS Cloud, you can add a secondary replica by using an Always On availability group for high availability and resiliency purposes.

For more information about using this method to achieve high availability, data protection, and disaster recovery for your SQL Server databases on Amazon EC2, see [Database mirroring](ec2-sql-ha.md#ec2-db-mirroring) in the *Amazon EC2 for SQL Server* section.
