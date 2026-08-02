---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/modernization.html
---

# Modernizing your SQL Server database
<a name="modernization"></a>

This section describes how to modernize your SQL Server workloads on AWS by switching from the Windows operating system to Linux. This change enables you to take advantage of open-source technologies and to save on Windows licensing costs without drastically altering your system architecture or retraining your users.

## Migrating your SQL Server workloads from Windows to Linux
<a name="windows-linux"></a>

Starting with SQL Server 2017, SQL Server is available to run on Linux operating systems. Moving your SQL Server workloads to Linux provides both cost savings and performance improvements.

Almost all SQL Server functions, applications, statements, and scripts that you use on Microsoft Windows are supported on Linux as well. You can also use tools such as SQL Server Management Studio (SSMS), SQL Server Data Tools (SSDT), and PowerShell module (sqlps) to manage SQL Server on Linux from a Windows instance.

You can use one of these three options to migrate your SQL Server workloads to Linux:
+ Native SQL Server backup and restore feature (see the [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-migrate-restore-database?view=sql-server-ver15))
+ Distributed availability groups (to change your operating system while you migrate to AWS)
+ The AWS replatforming assistant, which is a PowerShell-based scripting tool

The AWS replatforming assistant helps you migrate from your existing SQL Server workloads from Windows to a Linux operating system. When you run the PowerShell script for the replatforming assistant on a source SQL Server database, the Windows instance backs up the database to an encrypted Amazon S3 storage bucket. It then restores the backup to new or existing SQL Server database on an Amazon EC2 Linux instance. You can replicate your database and test your applications while your source SQL Server database remains online. After testing, you can schedule application downtime and rerun the PowerShell backup script to perform your final cutover.

For more information about using the replatforming assistant, see [Migrate your on-premises SQL Server Windows Workloads to Amazon EC2 Linux](https://aws.amazon.com/blogs/database/migrating-your-on-premises-sql-server-windows-workloads-to-amazon-ec2-linux/) on the AWS Database blog, and the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/replatform-sql-server.html).

## High availability on Linux
<a name="windows-linux-ha"></a>

[SQL Server 2017](https://www.microsoft.com/en-us/sql-server/sql-server-2017) supports Always On availability groups between Windows and Linux to create read-scale workloads without high availability. Unfortunately, you cannot achieve high availability between Windows and Linux, because there is no clustered solution that can manage that cross-platform configuration.

To use high availability with Always On availability groups, consider using a [Windows Server Failover Cluster (WSFC)](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/failover-clustering-and-always-on-availability-groups-sql-server?view=sql-server-2017) or [Pacemaker on Linux](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-availability-group-configure-ha?view=sql-server-2017). This solution is suitable for a migration path from SQL Server on Windows to Linux and vice versa, or for disaster recovery using manual failover. For more information about this scenario, see [Deploying Always On availability groups between Amazon EC2 Windows and Amazon Linux 2 instances](https://aws.amazon.com/blogs/database/deploying-always-on-availability-groups-between-amazon-ec2-windows-and-amazon-linux-2-instances/) on the AWS Database blog.
