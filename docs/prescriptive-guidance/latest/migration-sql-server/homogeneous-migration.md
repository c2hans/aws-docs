---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/homogeneous-migration.html
---

# Homogeneous database migration for SQL Server
<a name="homogeneous-migration"></a>

AWS offers you the ability to run SQL Server databases in a cloud environment. For developers and database administrators, running SQL Server database in the AWS Cloud is very similar to running SQL Server database in a data center. This section describes options for migrating your SQL Server database from an on-premises environment or a data center to the AWS Cloud.

AWS offers three options for running SQL Server on AWS, as described in the following table.

|
|
| **Option** | **Highlights** | **More information** |
| --- |--- |--- |
| **SQL Server on Amazon RDS** | Managed service, provides easy provisioning and licensing, cost-effective, easy to set up, manage, and maintain. | [Amazon RDS for SQL Server section](rds-sql.md) |
| **SQL Server on Amazon RDS Custom** | Managed service, but you retain administrative rights to the database and the underlying operating system | [Amazon RDS Custom for SQL Server section](rdscustom-sql.md) |
| **SQL Server on Amazon EC2** | Self-managed, provides full control and flexibility. | [Amazon EC2 for SQL Server section](ec2-sql.md) |
| **SQL Server on VMware Cloud on AWS** | Set up, scale, and operate your SQL Server workloads on VMware Cloud on AWS and integrate with AWS Directory Service, AD Connector, and Amazon S3. | [VMware Cloud on AWS for SQL Server section](vmware-sql.md) |

**Notice**: As of April 30, 2024, VMware Cloud on AWS is no longer resold by AWS or its channel partners. The service will continue to be available through Broadcom. We encourage you to reach out to your AWS representative for details.

Your application requirements, database features, functionality, growth capacity, and overall architecture complexity will determine which option to choose. If you are migrating multiple SQL Server databases to AWS, some of them might be a great fit for Amazon RDS, whereas others might be better suited to run directly on Amazon EC2. You might have databases that are running on SQL Server Enterprise edition but are a good fit for SQL Server Standard edition. You might also want to modernize your SQL Server database running on Windows to run on a Linux operating system to save on cost and licenses. Many AWS customers run multiple SQL Server database workloads across Amazon RDS, Amazon EC2, and VMware Cloud on AWS.

**Note**
You can use Migration Hub Orchestrator to automate and orchestrate your SQL Server database migrations to Amazon EC2 or Amazon RDS by using native backup and restore. For more information, see the [AWS Migration Hub Orchestrator section](mho.md).
