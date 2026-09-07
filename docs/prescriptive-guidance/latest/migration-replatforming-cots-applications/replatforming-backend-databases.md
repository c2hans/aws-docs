---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/replatforming-backend-databases.html
---

# Replatforming backend databases
<a name="replatforming-backend-databases"></a>

The approach for replatforming backend databases is different for COTS and in-house applications. This is because the source code is typically only available for in-house applications. The following illustration shows the replatforming options available for your application's backend databases.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/images/guide-img/1c80030e-7c77-405d-a255-8740ee2bb30b/images/155322b8-d05d-4eb0-8571-a5c96f7a3067.png)

The following sections explain the replatforming approaches for backend databases belonging to COTS or in-house applications.

## Replatforming backend databases for COTS applications
<a name="replatforming-backend-databases-cots"></a>

We recommend that you use an Aurora database if your COTS application supports open-source databases. Using an open-source database helps reduce licensing costs, and you can also use tools such as AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS) to achieve a cutover with minimal downtime during your migration.

If your COTS application doesn't support open-source databases, we recommend replatforming to a commercial database on Amazon Relational Database Service (Amazon RDS) such as [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) or [Amazon RDS for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html). You should evaluate the database features used by your application and make sure that they are supported in Amazon RDS before you begin your migration. For more information, see [Limits for Microsoft SQL Server database instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport.Limits) in the Amazon RDS documentation.

You can also use your remaining database licensing and run self-managed commercial databases on EC2 instances. If you choose this approach, we recommend that you begin the license verification process with your database's vendor. After the license verification process is complete, you should design a self-managed database solution on Amazon EC2 for your application's required recovery time objective (RTO) or recovery point objective (RPO).

Finally, we recommend replatforming security-sensitive, high-performance COTS applications that use SQL Server databases to SQL Server running on Amazon EC2 Linux instances. For more information about this, see [Migrating your on-premises SQL Server Windows workloads to Amazon EC2 Linux](https://aws.amazon.com/blogs/database/migrating-your-on-premises-sql-server-windows-workloads-to-amazon-ec2-linux/).

## Replatforming backend databases for in-house applications
<a name="replatforming-backend-databases-inhouse"></a>

You can reduce your database licensing costs and increase scalability by replatforming your in-house application's backend databases to AWS managed databases (for example, [Amazon RDS for PostgreSQL, ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)[Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html), [Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html), or [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)).

AWS managed databases help you reduce recurring administrative tasks for your databases (for example, performing backups or patching databases and OSs). If you use Amazon RDS Multi-AZ deployments, you can also increase your application's availability by preventing outages from database hardware failures. Multi-AZ databases are continuously replicated to a different Availability Zone and the application transparently fails over to the replicated database during outages.

You can use [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) and [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) to convert commercial databases to Aurora and Amazon RDS. AWS SCT automates the database schema conversion process, and AWS DMS enables data replication from on-premises databases to Amazon RDS. AWS DMS also helps achieve a minimal downtime cutover when you migrate on-premises applications to the AWS Cloud.
