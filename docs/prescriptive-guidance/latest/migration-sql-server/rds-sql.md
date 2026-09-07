---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/rds-sql.html
---

# Amazon RDS for SQL Server
<a name="rds-sql"></a>

Amazon RDS for SQL Server is a managed database service that simplifies the provisioning and management of SQL Server on AWS. Amazon RDS makes it easy to set up, operate, and scale SQL Server deployments in the cloud. With Amazon RDS, you can deploy multiple versions of SQL Server (2014, 2016, 2017, 2019, and 2022) and editions (including Express, Web, Standard and Enterprise) in minutes, with cost-efficient and resizable compute capacity. You can provision Amazon RDS for SQL Server DB instances with either General Purpose SSD or Provisioned IOPS SSD storage. (For details, see [Amazon RDS Storage Types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#Concepts.Storage) in the AWS documentation.) Provisioned IOPS SSD is designed to deliver fast, predictable, and consistent I/O performance, and is optimized for I/O-intensive, transactional (OLTP) database workloads.

Amazon RDS frees you to focus on application development, because it manages time-consuming database administration tasks, including provisioning, backups, software patching, monitoring, and hardware scaling. Amazon RDS for SQL Server also offers Multi-AZ deployments and read replicas (for SQL Server Enterprise edition) to provide high availability, performance, scalability, and reliability for production workloads.

## When to choose Amazon RDS
<a name="rds-sql-choosing"></a>

Amazon RDS for SQL Server is a migration option when:
+ You want to focus on your business and applications, and you want AWS to take care of undifferentiated heavy lifting tasks such as the provisioning of the database, management of backup and recovery tasks, management of security patches, minor SQL Server version upgrades, and storage management.
+ You need a highly available database solution, and you want to take advantage of the push-button, synchronous Multi-AZ replication offered by Amazon RDS, without having to manually set up and maintain database mirroring, failover clusters, or Always On availability groups.
+ You want to pay for the SQL Server license as part of the instance cost on an hourly basis instead of making a large, upfront investment.
+ Your database size and IOPS needs are supported by Amazon RDS for SQL Server. See [Amazon RDS DB Instance Storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the AWS documentation for the current maximum limits.
+ You don't want to manage backups or point-in-time recoveries of your database.
+ You want to focus on high-level tasks, such as performance tuning and schema optimization, instead of the daily administration of the database.
+ You want to scale the instance type up or down based on your workload patterns without being concerned about licensing complexities.

After assessing your database and project requirements, if you decide to migrate to Amazon RDS for SQL Server, see the details provided in the following sections, and review the [migration best practices](best-practices.md) we discuss later in this guide.

For currently supported SQL Server features, versions, and options, see [Amazon RDS for SQL Server features](https://aws.amazon.com/rds/sqlserver/features/) on the AWS website, [Choosing between Amazon EC2 and Amazon RDS](comparison.md) later in this guide, and [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html) in the AWS documentation. If you're moving to Amazon RDS Custom, make sure to review the [requirements and limitations for Amazon RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html).

## High availability
<a name="rds-sql-ha"></a>

Amazon RDS provides high availability and failover support for databases that are deployed with the Multi-AZ option. When you provision your database with the Multi-AZ option, Amazon RDS automatically provisions and maintains a synchronous standby instance in a different Availability Zone. The primary database synchronously replicates the data to the standby instance. If problems occur, Amazon RDS automatically repairs the unhealthy instance and re-establishes synchronization. In case of infrastructure failure or Availability Zone disruption, Amazon RDS performs an automatic failover to the standby instance. Failover occurs only if the standby and primary databases are fully synchronized. Because the endpoint remains the same for the primary and standby instances, you can resume database operations as soon as the failover is complete, without performing a manual intervention. The failover time depends on the time it takes to complete the recovery process. Large transactions increase the failover time.

The following diagram illustrates the Amazon RDS for SQL Server Multi-AZ deployment option.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/94a305ee-57ca-43c4-abeb-2b5e76b01d3e.png)

When you set up SQL Server in a Multi-AZ configuration, Amazon RDS automatically configures standby database instance using database mirroring or Always On availability groups, based on the version of SQL Server that you deploy. The specific SQL Server versions and editions are listed in the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html).

In Multi-AZ deployments, operations such as instance scaling or system upgrades such as operating system (OS) patching are applied first on the standby instance, before the automatic failover of the primary instance, for enhanced availability.

Because of failover optimization of SQL Server, certain workloads can generate greater I/O load on the standby instance than they do on the primary instance, particularly in database mirroring deployments. This functionality can result in higher IOPS on the standby instance. We recommend that you consider the maximum IOPS needs of both the primary and standby instances when you provision the storage type and IOPS of your Amazon RDS for SQL Server DB instance. You can also specify `MultiSubnetFailover=True`, if your client driver supports it, to significantly reduce the failover time.

**Limitations**
+ The Multi-AZ option isn't available for SQL Server Express and Web editions. It's available only for SQL Server Standard and Enterprise editions.
+ You can't configure the standby DB instance to accept database read activity.
+ Cross-Region Multi-AZ isn't supported.
+ In Amazon RDS you can issue a stop command to a standalone DB instance and keep the instance in a stopped state to avoid incurring compute charges. You can't stop an Amazon RDS for SQL Server DB instance in a Multi-AZ configuration. Instead, you can terminate the instance, take a final snapshot before termination, and recreate a new Amazon RDS instance from the snapshot when you need it. Or, you can remove the Multi-AZ configuration first and then stop the instance. After seven days, your stopped instance will restart so that any pending maintenance can be applied.

For additional limitations, see [Microsoft SQL Server Multi-AZ deployment notes and recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html#USER_SQLServerMultiAZ.Recommendations) in the Amazon RDS documentation.

## Read replicas
<a name="rds-sql-replicas"></a>

Read replicas provide scalability and load balancing. A SQL Server read replica is a physical copy of an Amazon RDS for SQL Server DB instance that is used for read-only purposes. Amazon RDS helps reduces the load on the primary DB instance by offloading read-only workloads to the read replica DB instance. Updates made to your primary DB instance are asynchronously copied to the read replica instance.

When you request a read replica, Amazon RDS takes a snapshot of the source DB instance, and this snapshot becomes the read replica. There is no outage while creating and deleting a read replica. Amazon RDS for SQL Server upgrades the primary database immediately after upgrading the read replicas, regardless of the maintenance window. Every read replica comes with a separate endpoint that you use to connect to the read replica database.

Amazon RDS for SQL Server makes it easy to create read replicas by configuring Always On availability groups, and maintaining secure network connections between a primary DB instance and its read replicas.

You can set up a read replica in the same AWS Region as your primary database, or in another Region. You can create up to five read replicas for one source DB instance.

**Note**
Read replicas are available only with the following SQL Server versions and editions: SQL Server 2017 Enterprise edition 14.00.3049.1 or later and SQL Server 2016 Enterprise edition 13.00.5216.0 or later. SQL Server versions and editions that support database mirroring for Multi-AZ environments do not offer read replicas.

The following diagram illustrates an Amazon RDS for SQL Server DB instance in a Multi-AZ environment with a read replica in another Availability Zone within the same AWS Region. Not all AWS Regions offer more than two Availability Zones, so you should [check the Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) you're planning to use before adopting this strategy.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/20fe96ca-d2f4-4573-a23c-101ef248c0d7.png)

A SQL Server read replica doesn't allow write operations. However, you can promote the read replica to make it writable. After you promote it, you cannot revert it back to a read replica. It will become a single, standalone DB instance that has no relationships with its original primary database instance. The data in the promoted read replica will match the data in the source DB instance up to the point when the request was made to promote it. The SQL Server DB engine version of the source DB instance and all of its read replicas will be the same.

For efficient replication, we recommend the following:
+ Set up each read replica with the same compute and storage resources as the source DB instance.
+ You must enable automatic backups on the source DB instance by setting the backup retention period to a value other than 0 (zero).
+ The source DB instance must be deployed in a Multi-AZ environment with Always On availability groups.

For SQL Server version support, editions, and limitations, see [Read replica limitations with SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html#SQLServer.ReadReplicas.Limitations) in the Amazon RDS documentation.

For more information about using read replicas, see [Working with read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) and [Working with SQL Server read replicas for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html) in the AWS documentation. For more information about data transfer pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

## Disaster recovery
<a name="rds-sql-dr"></a>

With Amazon RDS for SQL Server, you can create a reliable, cross-Region disaster recovery (DR) strategy. The main reasons for creating a DR solution are business continuity and compliance:
+ An effective DR strategy helps you keep your systems up and running with minimal or no interruptions during a catastrophic event. A reliable and effective cross-Region DR strategy keeps your business in operation even if an entire Region goes offline.
+ A cross-Region DR solution helps you meet auditing and compliance requirements.

Recovery point objective (RPO), recovery time objective (RTO), and cost are three key metrics to consider when developing your DR strategy. For other options for providing cross-Region replicas, see [AWS Marketplace](https://aws.amazon.com/marketplace/). For more information about these approaches, see [Cross-Region disaster recovery of Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/cross-region-disaster-recovery-of-amazon-rds-for-sql-server/) on the AWS Database blog.
