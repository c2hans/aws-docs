---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql-ha.html
---

# High availability
<a name="ec2-sql-ha"></a>

You can use any SQL Server-supported replication technology with your SQL Server database on Amazon Elastic Compute Cloud (Amazon EC2) to achieve high availability, data protection, and disaster recovery. Some of the common solutions are log shipping, database mirroring, Always On availability groups, and Always On Failover Cluster Instances.

The following diagram shows how you can use SQL Server on Amazon EC2 across multiple Availability Zones within a single AWS Region. The primary database is a read-write database, and the secondary database is configured with log shipping, database mirroring, or Always On availability groups for high availability. All the transaction data from the primary database is transferred and can be applied to the secondary database asynchronously for log shipping, and asynchronously for Always On availability groups and mirroring.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/8a86e6e1-85ce-4179-b63f-1023496252c7.png)

## Log shipping
<a name="ec2-log-shipping"></a>

Log shipping lets you automatically send transaction log backups from a primary database instance to one or more secondary databases (also known as *warm standby*) on separate DB instances. Log shipping uses SQL Server Agent jobs to automate the process of backing up, copying, and applying the transaction log backups. Although log shipping is typically considered a disaster recovery feature, it can also provide high availability by allowing secondary DB instances to be promoted if the primary DB instance fails. If your RTO and RPO are flexible, or your databases aren't considered highly mission-critical, consider using log shipping to provide better availability for your SQL Server databases.

Log shipping increases the availability of databases by providing access to secondary databases to use as read-only copies of the primary database when needed. You can configure a lag delay (a longer delay time) during which you can recover accidentally changed data on the primary database before these changes are shipped to the secondary database.

We recommend running the primary and secondary DB instances in separate Availability Zones, and deploying a monitor instance to track all the details of log shipping. Backup, copy, restore, and failure events for a log shipping group are available from the monitor instance.  A log shipping configuration doesn't automatically fail over from the primary server to the secondary server. However, any of the secondary databases can be brought online manually if the primary database becomes unavailable.

Log shipping is often used as a disaster recovery solution but also can be used as a high availability solution, depending on your application requirements. Use log shipping when:
+ You have flexible RTO and RPO requirements. Log shipping provides an RPO of minutes, and an RTO of minutes to hours.
+ You do not need an automatic failover to the secondary database.
+ You want to read from the secondary database, but you don't require readability during a restore operation.

For more information about log shipping, see the [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server).

## Database mirroring
<a name="ec2-db-mirroring"></a>

Database mirroring takes a database that's on an Amazon EC2 instance and provides a complete or almost complete read-only copy (mirror) of it on a separate DB instance. Amazon RDS uses database mirroring to provide Multi-AZ support for Amazon RDS for SQL Server. This feature increases the availability and protection of databases, and provides a mechanism to keep databases available during upgrades.

**Note**
According to the [Microsoft documentation](https://docs.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server), database mirroring will be removed in a future version of SQL Server. You should plan to use Always On availability groups instead.

In database mirroring, SQL servers can take one of three roles:
+ The principal server, which hosts the primary read/write version of the database.
+ The mirror server, which hosts a copy of the principal database.
+ An optional witness server. This server is available only in high-safety mode. It monitors the state of the database mirror and automates the failover from the primary database to the mirror database.

A mirroring session is established between the principal and mirror servers. During mirroring, all database changes that are performed in the principal database are also performed on the mirror database. Database mirroring can be either a synchronous or an asynchronous operation. This is determined by two mirroring operating modes: high-safety mode and high-performance mode.
+ **High-safety mode:** This mode uses synchronous operations. In this mode, the database mirroring session synchronizes the insert, update, and delete operations from the principal database to the mirror database as quickly as possible. As soon as the database is synchronized, the transaction is committed in both the principal and the mirror databases. We recommend that you use this operating mode when the mirror databases are in the same or different Availability Zones, but hosted within the same AWS Region.
+ **High-performance mode:** This mode uses asynchronous operations. In this mode, the database mirroring session synchronizes the insert, update, and delete operations from the principal database to the mirror database, but there can be a lag between the time the principal database commits transactions and the time the mirror database commits transactions. We recommend that you use this mode when the mirror databases are in different AWS Regions.

Use database mirroring when:
+ You have strict RTO and RPO requirements, and cannot have delays between the primary and secondary databases. Database mirroring provides an RPO of zero seconds (with synchronous commit) and an RTO of seconds to minutes.
+ You do not have a requirement to read from the secondary database.
+ You want to perform automatic failover when you have a witness server configured in synchronization mode.
+ You cannot use Always On availability groups, which is the preferred option.

Limitations:
+ Only one-to-one failover is supported. You cannot have multiple database destinations sync with the primary database.

For more information about mirroring, see [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-sql-server).

## Always On availability groups
<a name="ec2-always-on"></a>

SQL Server Always On availability groups provide high availability and disaster recovery solutions for SQL Server databases. An availability group consists of a set of user databases that fail over together. It includes a single set of primary read/write databases and multiple (one to eight) sets of related, secondary databases. You can make the secondary databases available to the application tier as read-only copies of the primary databases (SQL Server Enterprise edition only), to provide a scale-out architecture for read workloads. You can also use the secondary databases for backup operations.

SQL Server Always On availability groups support both synchronous and asynchronous commit modes. In synchronous mode, the primary replica commits database transactions after the changes are committed or written to the log of the secondary replica. Using this mode, you can perform planned manual failover and automatic failover if the replicas are in sync.  You can use synchronous commit mode between SQL Server instances within the same environment (for example, if all instances are on-premises or all instances are in AWS).

In asynchronous commit mode, the primary replica commits database transactions without waiting for the secondary replica. You can use asynchronous commit mode between SQL Server instances that are in different environments (for example, if you have instances on premises and in AWS).

You can use Always On availability groups for high availability or disaster recovery. Use this method when:
+ You have strict RTO and RPO requirements. Always On availability groups provide an RPO of seconds, and an RTO of seconds to minutes.
+ You want to manage and fail over a group of databases. Always On availability groups support 0-4 secondary replicas in synchronous commit mode for SQL Server 2019.
+ You want to use automatic failover in synchronous commit mode, and you don't need a witness server.
+ You want to read from the secondary database.
+ You want to synchronize multiple database destinations with your primary database.

Starting with SQL Server 2016 SP1, SQL Server Standard edition provides basic high availability for a single, non-readable secondary database and listener per availability group. It also supports a maximum of two nodes per availability group.

## Always On Failover Cluster Instances
<a name="ec2-fci"></a>

SQL Server Always On Failover Cluster Instances (FCIs) use Windows Server Failover Clustering (WSFC) to provide high availability at the server instance level. An FCI is a single instance of SQL Server that is installed across WSFC nodes to provide high availability for the entire installation of SQL Server. If the underlying node experiences hardware, operating system, application, or service failures, everything inside the SQL Server instance is moved to another WSFC node. This includes system databases, SQL Server logins, SQL Server Agent jobs, and certificates.

An FCI is generally preferable over an Always on availability group when:
+ You're using SQL Server Standard edition instead of Enterprise edition.
+ You have a large number of small databases per instance.
+ You're constantly modifying instance-level objects such as SQL Server Agent jobs, logins, and so on.

There are four options for deploying FCIs on AWS:
+ Amazon EBS Multi-Attach with persistent reservations
+ Amazon FSx for Windows File Server
+ Amazon FSx for NetApp ONTAP
+ Solutions from AWS Partners

### Using Amazon EBS Multi-Attach with persistent reservations
<a name="using-9999999999999999ebs--multi-attach-with-persistent-reservations.0478daf0-3baa-56ff-b993-4ef6df2146b1"></a>

Amazon EBS Multi-Attach with [NVMe reservations](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-reservations.html) supports the creation of SQL Server FCIs with Amazon EBS io2 volumes as the shared storage on Windows Server failover clusters. This feature simplifies the failover cluster setup process by enabling you to build a failover cluster by using Amazon EBS io2 volumes. These volumes can be attached only to instances that are in the same Availability Zone. To deploy Windows Server failover clusters by using Amazon EBS io2 volumes, you must use the latest AWS NVMe drivers.

Amazon EBS volumes and instance store volumes are exposed as NVMe block devices on [Nitro-based instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances). You must have the [AWS NVMe driver](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/aws-nvme-drivers.html) installed with the [SCSI persistent reservation feature](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/aws-nvme-drivers.html#configure-scsi-persistent-reservations) configured when you use Amazon EBS io2 volumes to form WSFC and SQL Server FCIs.

For more information about this feature, see the AWS blog post [How to deploy a SQL Server failover cluster with Amazon EBS Multi-Attach on Windows Server.](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-deploy-a-sql-server-failover-cluster-with-amazon-ebs-multi-attach-on-windows-server/)

### Using Amazon FSx for Windows File Server
<a name="using-9999999999999999fsxwindowslong-.147068b6-fafd-529b-994e-5bd74319178f"></a>

[Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) provides fully managed shared file storage. It automatically replicates the storage synchronously across two Availability Zones to provide high availability. Using FSx for Windows File Server for file storage helps simplify and optimize SQL Server high availability deployments on Amazon EC2.

With Microsoft SQL Server, high availability is typically deployed across multiple database nodes in an WSFC, and each node has access to shared file storage. You can use FSx for Windows File Server as shared storage for SQL Server high availability deployments in two ways: as storage for active data files and as an SMB file share witness.

For information about how you can reduce the complexity and cost of running SQL Server FCI deployments by using FSx for Windows File Server, see the blog post [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/). The blog post also provides step-by-step instructions for deploying SQL Server FCIs by using an Amazon FSx Multi-AZ file system as the shared storage solution. For more information, see the [Amazon FSx for Windows File Server documentation](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).

### Using Amazon FSx for NetApp ONTAP
<a name="using-9999999999999999fsxontaplong-.1979209d-5c9c-5e9e-adbc-1d2df821b5e2"></a>

[Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html) is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage that's built on the NetApp ONTAP file system.

FSx for ONTAP combines the familiar features, performance, capabilities, and API operations of NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service.

FSx for ONTAP provides multi-protocol access to data over the NFS, SMB, and iSCSI protocols for Windows and Linux systems. You can build a highly available SQL Server Always-On FCI architecture, as explained in detail in the blog post [SQL Server High Availability Deployments Using Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/modernizing-with-aws/sql-server-high-availability-amazon-fsx-for-netapp-ontap/). FSx for ONTAP can also provide a quick way to fail over your SQL Server environment to a different AWS Region in order to meet recovery time objective (RTO) and recovery point objective (RPO) requirements. For more information, see the blog post [Implementing HA and DR for SQL Server Always-On Failover Cluster Instance using Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/implementing-ha-and-dr-for-sql-server-always-on-failover-cluster-instance-using-amazon-fsx-for-netapp-ontap/).

You can also use [AWS Launch Wizard ](https://aws.amazon.com/launchwizard/)to deploy SQL Server solutions on AWS, with support for Always On Availability Groups and single-node deployments. Launch Wizard supports the deployment for SQL Server Always on FCIs on Amazon EC2 with FSx for ONTAP as the shared storage. This service saves you time and effort by replacing a complex manual deployment process with a guided, console-based wizard that accelerates the migration of your on-premises SQL Server workloads that rely on shared storage. For more information about how Launch Wizard can help you provision and configure SQL Server FCIs solution in hours, see the blog post [Simplify SQL Server Always On deployments with AWS Launch Wizard and Amazon FSx](https://aws.amazon.com/blogs/storage/simplify-sql-server-always-on-deployments-with-the-aws-launch-wizard-and-amazon-fsx/). Launch Wizard also supports deployment for SQL Server Always On FCIs by using [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) as the shared storage solution.

### Using solutions from AWS Partners
<a name="using-solutions-from-9999999999999999aws--partners.f9ed299e-60db-5336-a26a-a02f8776d5f8"></a>
+ [SIOS DataKeeper](https://us.sios.com/) provides high availability cluster failover support across AWS Regions and Availability Zones.  SIOS DataKeeper is available in [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=3c91e2f7-fc8d-4cce-a8aa-1e37abcb4408).
+ [DxEnterprise from DH2i](https://dh2i.com/dxenterprise-high-availability/) enables fully automatic failover of SQL Server Availability Groups in Kubernetes and unified instance failover for Windows and Linux. D2HI is available in [AWS Marketplace.](https://aws.amazon.com/marketplace/seller-profile?id=4e97d4b7-3366-42fd-8be8-732d38c9e24b)

## FSx for Windows File Server
<a name="fsx-windows"></a>

Amazon FSx for Windows File Server provides fully managed, highly reliable, and scalable file storage that is accessible by using the Server Message Block (SMB) protocol. It is built on Windows Server and delivers a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration. It offers Single-AZ and Multi-AZ deployment options, fully managed backups, and encryption of data at rest and in transit. You can optimize cost and performance for your workloads with solid-state drives (SSD) and hard disk drives (HDD) storage options, and you can scale storage and change the throughput performance of your file system at any time. Amazon FSx file storage is accessible from Windows, Linux compute instances running on AWS, and on premises.

Amazon FSx makes it easier to deploy shared Windows storage for high availability SQL Server deployments through its support for continuously available (CA) file shares and smaller file systems.  This option is suitable for these use cases:
+ As shared storage used by SQL Server nodes in a WSFC instance.
+ As an SMB file share witness that can be used with any SQL Server cluster with WSFC.

Amazon FSx provides fast performance with baseline throughput up to 2 GB/second per file system, hundreds of thousands of IOPS, and consistent sub-millisecond latencies.

To provide the right performance for your SQL instances, you can choose a throughput level that is independent of your file system size. Higher levels of throughput capacity also come with higher levels of IOPS that the file server can serve to the SQL Server instances accessing it.

The storage capacity determines not only how much data you can store, but also how many IOPS you can perform on the storage. Each gigabyte of storage provides 3 IOPS. You can provision each file system to be up to 64 TB in size.

For information about configuring and using Amazon FSx to reduce the complexity and costs of your SQL Server high availability deployments, see [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/) on the AWS Storage blog. To learn more about creating a new CA share, see the [Amazon FSx for Windows File Server documentation](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-file-shares.html#create-ca-share).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
