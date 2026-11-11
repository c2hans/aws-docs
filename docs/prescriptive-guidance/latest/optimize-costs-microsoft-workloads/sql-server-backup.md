---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-backup.html
---

# Optimize SQL Server backup strategies
<a name="sql-server-backup"></a>

## Overview
<a name="sql-server-backup-overview"></a>

Most organizations are looking for the right solution to safeguard their data on SQL Server on [Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql.html) to meet their current requirements for recovery point objective (RPO), the maximum acceptable amount of time since the last backup, and recovery time objective (RTO), the maximum acceptable delay between the interruption of service and restoration of service. If you're running SQL Server on EC2 instances, you have multiple options for creating backups of your data and restoring your data. Backup strategies for safeguarding data for SQL Server on Amazon EC2 include the following:
+ Server-level backup using Windows [Volume Shadow Copy Service](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) (VSS)-enabled [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) snapshots or [AWS Backup](https://aws.amazon.com/backup/)
+ Database-level backup using [native backup and restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16) in SQL Server

You have the following storage options for [database-level native backup](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/database-level-backup.html):
+ A local backup with an [Amazon EBS volume](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/database-level-backup.html#ebs-volumes)
+ A network file system backup with [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/database-level-backup.html#amazon-fsx) or Amazon FSx for NetApp ONTAP
+ A network backup to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) using [AWS Storage Gateway](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/database-level-backup.html#storage-gateway)
+ Direct backup to Amazon S3 for SQL Server 2022

This section does the following:
+ Highlights features to help you save on storage space
+ Compares the costs between different backend storage options
+ Provides links to in-depth documentation to help implement these recommendations

## Server-level backup using VSS-enabled snapshots
<a name="sql-server-backup-vss"></a>

A Volume Shadow Copy Service (VSS)-enabled snapshot architecture uses AWS Systems Manager [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) to install the VSS agent on your Microsoft SQL Server instances. You can also use Run Command to invoke the entire workflow of flushing operating system and application buffers to the disk, pausing I/O operations, taking a point-in-time snapshot of the [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) volumes, and then resuming I/O. For more information about Systems Manager, see [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/)

This Run Command creates automated snapshots of all EBS volumes attached to a target instance. You can also exclude the root volume, because user database files are usually stored on other volumes. If you stripe multiple EBS volumes to create a single file system for SQL Server files, Amazon EBS also supports crash-consistent multivolume snapshots using a single API command. For more information about application-consistent [VSS-enabled EBS snapshots](https://aws.amazon.com/blogs/mt/take-microsoft-vss-enabled-snapshots-using-amazon-ec2-systems-manager/), see [Create a VSS application-consistent snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots.html) in the Amazon EC2 documentation.

The following diagram shows an architecture for server-level backup using VSS-enabled snapshots.

![VSS-enabled snapshots architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/9ef868d8-ccf7-4a5e-b01c-23529d19554f.png)

Consider the following benefits of using VSS-enabled snapshots:
+ The first snapshot of a DB instance contains the data for the full DB instance. Subsequent snapshots of the same DB instance are [incremental](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html#how_snapshots_work), which means that only the data that has changed after your most recent snapshot is saved.
+ EBS snapshots provide point-in-time recovery.
+ You can [restore to a new SQL Server EC2 instance from a snapshot](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/restore.html).
+ If an instance is encrypted using Amazon EBS or if a database is encrypted in the instance using transparent data encryption (TDE), the restore process automatically applies the same encryption to that instance or database.
+ You can copy your [automated cross-Region backups](https://docs.aws.amazon.com/ebs/latest/userguide/event-policy.html).
+ When you restore an EBS volume from a snapshot, the volume becomes available to applications immediately. This means that you can bring SQL Server online right after you restore one or more of its underlying EBS volumes from snapshots.
+ By default, restored volumes fetch underlying blocks from Amazon S3 the first time an application tries to read them. This means that performance can lag after you restore an EBS volume from a snapshot. The volume eventually reaches its expected performance. However, you can avoid that lag by using [fast snapshot restore (FSR)](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html).
+ You can use [lifecycle management for EBS snapshots](https://aws.amazon.com/blogs/aws/new-lifecycle-management-for-amazon-ebs-snapshots/).

Consider the following limitations of using VSS-enabled snapshots:
+ You can't perform cross-Region point-in-time recovery with an encrypted snapshot for a SQL Server instance.
+ You can't create an encrypted snapshot of an unencrypted instance.
+ You can't restore an individual database because the snapshot operates at the EBS volume level.
+ You can't restore the instance to itself.
+ You must encrypt a snapshot of the DB instance by using the same AWS Key Management Service (AWS KMS) key as the DB instance.
+ The snapshot backup process suspends storage I/O for a fraction of a second (approximately 10 milliseconds).

## SQL Server backup using AWS Backup
<a name="sql-server-backup-aws-backup"></a>

You can use [AWS Backup](https://aws.amazon.com/backup/) to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that simplifies data protection at scale. AWS Backup also helps you support your regulatory compliance obligations and meet your business continuity goals. Together with AWS Organizations, AWS Backup enables you to centrally deploy data protection (backup) policies to configure, manage, and govern your backup activity across your organization's AWS accounts and resources.

The following diagram shows the architecture of a backup and restore solution for SQL Server on Amazon EC2 instances by using AWS Backup.

![AWS Backup architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/01c8cbc4-d3dc-4c54-aa47-2613da5ea86a.png)

Consider the following benefits of backing up SQL Server by using AWS Backup:
+ You can automate backup scheduling, retention management, and lifecycle management.
+ You can centralize your backup strategy across your organization, spanning multiple accounts and AWS Regions.
+ You can centrally monitor your backup activity and alerting across AWS services.
+ You can implement cross-Region backups for disaster recovery planning.
+ The solution supports cross-account backups.
+ You can perform secure backups with secondary backup encryption.
+ All backups support encryption by using AWS KMS encryption keys.
+ The solution works with Transparent Data Encryption (TDE).
+ You can restore to a specific recovery point from the AWS Backup console.
+ You can back up an entire SQL Server instance, which includes all SQL Server databases.

## Database-level backup
<a name="sql-server-backup-database"></a>

These approaches use native Microsoft SQL Server backup functionality. You can take backups of individual databases on the SQL Server instance and restore an individual database.

Each of these options for native SQL Server backup and restore also supports the following:
+ Compression and multiple-file backup
+ Full, differential, and transaction log backups
+ Databases encrypted with Transparent Data Encryption (TDE)

### SQL Server native backup and restore to Amazon S3
<a name="sql-server-native-backup-and-restore-to-9999999999999999s3-.afe96c02-276b-5458-adfd-184bc270c5dd"></a>

SQL Server on Amazon EC2 supports native backup and restore for SQL Server databases. You can take a backup of your SQL Server database and then restore the backup file to an existing database or to a new SQL Server EC2 instance, Amazon RDS for SQL Server, or an on-premises server.

[AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3) is a hybrid cloud storage service that provides on-premises applications with access to virtually unlimited cloud storage. You can use Storage Gateway to back up your Microsoft SQL Server databases directly to Amazon S3, reducing your on-premises storage footprint and using Amazon S3 for durable, scalable, and cost-effective storage.

The following diagram shows the architecture of a native backup and restore solution that uses Storage Gateway and Amazon S3.

![Storage Gateway and Amazon S3 architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/fe3f9001-43a5-49f8-939e-349c03514bc3.png)

Consider the following benefits of using native SQL Server backup with Storage Gateway:
+ You can map a storage gateway as a Server Message Block (SMB) file share on the EC2 instance and send the backup to Amazon S3.
+ The backup goes directly to the S3 bucket or through the Storage Gateway file cache.
+ You can use multiple-file backups.

Consider the following limitations of native backup using Storage Gateway:
+ You must set up backup and restore for each individual database.
+ You must manage the [Amazon S3 lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) for the backup files.

For more information about how to set up Storage Gateway, see the [Store SQL Server backups in Amazon S3 using AWS Storage Gateway](https://aws.amazon.com/blogs/database/storing-sql-server-backups-in-amazon-s3-using-aws-storage-gateway/) post on the AWS Blog.

### SQL Server native backup to EBS volumes
<a name="sql-server-native-backup-to-ebs-volumes.6846f588-e185-53ae-924e-752c97080a74"></a>

You can take a native backup of your SQL Server database and store the file in an Amazon EBS volume. Amazon EBS is a high-performance block storage service. EBS volumes are elastic and support encryption. You can detach them from and attach them to an EC2 instance. You can back up SQL Server on an EC2 instance to the same EBS volume type or to a different EBS volume type. One advantage of backing up to a different EBS volume type is potential cost savings.

The following diagram shows the architecture of a native backup to an EBS volume.

![EBS volume architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/526e295a-639b-4746-9fc9-5bbbb7d04821.png)

Consider the following benefits of using SQL Server native backup to EBS volumes:
+ You can take backups of individual databases on a SQL Server EC2 instance and restore an individual database instead of having to restore the complete instance.
+ You can use multiple-file backups.
+ You can schedule backup jobs by using SQL Server Agent and the SQL Server job engine.
+ You can get performance benefits through your hardware choices. For example, you can use st1 storage volumes to achieve higher throughput.

Consider the following limitations of using native backup to EBS volumes:
+ You must manually move backups to Amazon S3 from the EBS volume.
+ For large backups, you must manage disk space on Amazon EC2.
+ On the EC2 instance, Amazon EBS throughput can be a bottleneck.
+ Additional storage is required to store backups on Amazon EBS.

### SQL Server native backup to Amazon FSx for Windows File Server
<a name="sql-server-native-backup-to-9999999999999999fsxwindowslong-.e4c6d00f-4233-5f5c-9073-f0a717f6f7ce"></a>

[Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) is a fully managed native Windows file system that offers up to 64 TB of storage designed to deliver fast, predictable, and consistent performance. AWS introduced [native support for Multi-AZ file system deployments](https://aws.amazon.com/blogs/aws/amazon-fsx-for-windows-file-server-update-new-enterprise-ready-features/) on FSx for Windows File Server. Native support makes it easier to deploy Windows file storage on AWS with high availability and redundancy across multiple Availability Zones. AWS also introduced support for [SMB Continuously Available (CA) file shares](https://aws.amazon.com/about-aws/whats-new/2019/11/amazon-fsx-for-windows-file-server-adds-support-for-high-availability-microsoft-sql-server-deployments/). You can use FSx for Windows File Server as backup storage for a SQL Server database.

The following diagram shows the architecture of a native SQL Server backup to FSx for Windows File Server.

![FSx for Windows File Server backup architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/4e4f5d9a-7a9a-4747-b486-25a45df27528.png)

Consider the following benefits of using native SQL Server backup to FSx for Windows File Server:
+ You can back up your SQL Server database to an Amazon FSx file share.
+ You can take backups of individual databases on a SQL Server instance and restore an individual database instead of having to restore the complete instance.
+ You can use multi-part backups.
+ You can schedule backup jobs by using SQL Server Agent and the job engine.
+ The instances have higher network bandwidth compared to Amazon EBS.

Consider the following limitations of using native SQL Server backup to FSx for Windows File Server:
+ You must manually move backups to Amazon S3 from Amazon FSx by using AWS Backup or AWS DataSync.
+ Large backups might require additional overhead for disk space management on Amazon FSx.
+ EC2 instance network throughput can be a bottleneck.
+ Additional storage is required to store backups on FSx for Windows File Server.

### SQL Server backup to Amazon FSx for NetApp ONTAP
<a name="sql-server-backup-to-9999999999999999fsxontaplong-.9253d1bd-30c3-5db4-878b-d8203a9d78ad"></a>

Snapshots with FSx for ONTAP are crash consistent, but you must quiesce (or pause the I/O of) your database to create an application-consistent snapshot. You can use NetApp SnapCenter (an orchestration tool with plug-ins for specific applications, including SQL Server) with FSx for ONTAP to create application-consistent snapshots and to protect, replicate, and clone your databases.

#### NetApp SnapCenter
<a name="netapp-snapcenter.0f6de1d7-8391-5321-92c9-03722c3b9a26"></a>

NetApp SnapCenter is a unified tool for application-consistent data protection. SnapCenter refers to snapshots as backups, and this guide uses the same naming convention. SnapCenter provides a single interface for managing application-consistent backups, restores, and clones. You add a SnapCenter plug-in for your specific database application to create application-consistent backups. The SnapCenter plug-in for SQL Server provides the following functionality that simplifies your data protection workflow:
+ Backup and restore options with granularity for full and log backups
+ In-place restore and restore to an alternate location

For more information about SnapCenter, see the [Protect your SQL Server workloads using NetApp SnapCenter with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-netapp-snapcenter-with-amazon-fsx-for-netapp-ontap-to-protect-your-sql-server-workloads/) post on the AWS Storage Blog.

### Cost optimization for backups
<a name="cost-optimization-for-backups.e07643dc-9359-522e-93fe-e1eb5526c118"></a>

The following options can help you reduce the cost of storing SQL Server backups on AWS.
+ Enable [SQL Server compression](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-compression-sql-server?view=sql-server-ver16) when you create the backup file to send a smaller file to storage. For example, a 3:1 compression ratio indicates that you save about 66 percent on disk space. To query the compression ratio, you can use the following Transact-SQL statement: `SELECT backup_size/compressed_backup_size FROM msdb..backupset;` .
+ For backups going to S3 buckets, enable the [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) storage class to help reduce storage costs by up to 30 percent, depending on access patterns.
+ For backups going to FSx for Windows File Server or FSx for ONTAP, use a single Availability Zone for up to 50 percent cost savings (as compared to using multiple Availability Zones). For pricing information, see [Amazon FSx for Windows File Server Pricing](https://aws.amazon.com/fsx/windows/pricing/) and [Amazon FSx for NetApp ONTAP Pricing](https://aws.amazon.com/fsx/netapp-ontap/pricing/).
+ For SQL Server 2022, an efficient option is direct backup to Amazon S3. You can save additional costs by avoiding Storage Gateway.

### Benchmark test results for backups
<a name="benchmark-test-results-for-backups.063daab3-ac7e-5137-816c-cd3dd33fdb07"></a>

This section compares the following options from a cost and performance point of view for a sample 1 TB database, based on the results of performance benchmark testing on the backup solutions covered in this guide.
+ **EC2 instance specification **– r5d.8xlarge with Windows Server 2019 and SQL Server 2019 Developer edition
+ **Database specification** – 1 TB in size with TDE disabled

We performed the tests with an r5d.8xlarge instance and a 1 TB SQL Server database as the source. We configured the source system according to SQL Server best practices. The source database contained four data files (250 GB each) and one log file (50 GB) spread across separate gp3 volumes. The SQL Server native `BACKUP` command wrote to 10 backup files and used compression to improve backup performance and reduce the amount of data sent across the network and written to the target. In all test cases, storage performance was the bottleneck.

Many configurations are possible for these types of tests. This test focused on performance, cost, scalability, and real-world use cases. The following table shows the performance metrics that we captured for the backup target options.

|
|
| Backup options | Level | Run duration (approximate) | Backup rate | Cost USD per month\* |
| --- |--- |--- |--- |--- |
| Native backup to local EBS st1 HDD, 2 TB | Database | 00:30:46 min | 554.7 Mbps | $92.16 |
| Native backup to local EBS SSD gp3, 2 TB | Database | 00:22:00 min | 512 Mbps | $193.84 |
| Native backup to FSx for Windows File Server HDD, 2 TB @512 Mbps throughput | Database | 00:20:58 min | 814.0 Mbps | [$1,146](https://calculator.aws/#/estimate?id=e13d8a385d25b2d4f1320c5b1156b953355b7c13) |
| Native backup to FSx for Windows File Server SSD, 2 TB @512 Mbps throughput | Database | 00:20:00 min | 814.0 Mbps | [$1,326](https://calculator.aws/#/estimate?id=e13d8a385d25b2d4f1320c5b1156b953355b7c13) |
| Native backup to S3 File Gateway m6i.4xlarge (16 vCPU, 64 GB) with 2 TB gp3 | Database | 00:23:20 min | 731.5 Mbps | $470.42 |
| EBS Volume Shadow Copy Service (VSS) snapshot | EBS volume | 00:00:02 sec<br />00:00:53 sec | N/A snapshot | [$51](https://calculator.aws/#/estimate?id=e13d8a385d25b2d4f1320c5b1156b953355b7c13) |
| AWS Backup (AMI backup) | AMI | 00:00:04 sec<br />00:08:00 min | N/A snapshot | [$75](https://calculator.aws/#/estimate?id=e13d8a385d25b2d4f1320c5b1156b953355b7c13) |
| Native SQL Server backup directly to Amazon S3 (SQL Server 2022) | Database | 00:12:00 min | 731.5 Mbps | [First 50 TB / Month, $0.023 per GB $23.55 per month](https://calculator.aws/#/estimate?id=e13d8a385d25b2d4f1320c5b1156b953355b7c13) |
| Native backup to FSx for ONTAP (using SnapCenter) | Database | – | – | [$440.20](https://calculator.aws/#/estimate?id=8c9a0b2c296f9839f3ca16bdc2dcd9a6f52f1faf) |

The preceding table assumes the following:
+ Data transfer and Amazon S3 costs are not included.
+ Storage price is included in instance pricing.
+ The costs are based on the `us-east-1` Region.
+ Throughput and IOPS grow by 10 percent with multiple backups that have an overall rate of change of 10 percent over the month.

The test results show that a native SQL Server database backup to FSx for Windows File Server has fast performance. A backup to Storage Gateway or to locally attached EBS volumes is more cost-efficient but has slower performance. For server-level backups with Amazon Machine Images (AMIs), we recommend using AWS Backup for performance, cost, and manageability.

## Cost optimization recommendations
<a name="sql-server-backup-opt-rec"></a>

Understanding the possible solutions for backing up SQL Server on Amazon EC2 is key to safeguarding your data, ensuring that you meet your backup needs, and putting a plan in place to recover from critical events. The different ways to back up and restore your SQL Server instances and databases explored in this section can help you devise a backup and restore strategy that protects your data and meets your organization's requirements.

This section covers the following backup options:
+ Compression
+ Amazon S3 Intelligent-Tiering
+ Single Availability Zone
+ Backup to URL

The guidance provided for each of these options is high level. To implement any of these recommendations in your organization, contact your AWS account team. The team can engage a Microsoft Specialist Solutions Architect to lead the conversation.

In summary, we recommend the following:
+ If you're using SQL Server 2022, backing up to Amazon S3 is a cost-efficient option.
+ If you're using SQL Server 2019 or earlier, consider backing up to Storage Gateway backed by Amazon S3 as a cost-efficient option.

### Compression
<a name="compression.068ae988-5ea5-524a-904d-1226089544e4"></a>

The goal of compression is to have less storage consumed by each backup, which is beneficial for various storage options. You must enable compression for a SQL Server backup at the level of the [SQL Server instance](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/view-or-configure-the-backup-compression-default-server-configuration-option?view=sql-server-ver16). The following example shows how to add the compression keyword with a backup database:

`BACKUP DATABASE <database_name> TO DISK WITH COMPRESSION (ALGORITHM = QAT_DEFLATE)`

### Amazon S3 Intelligent-Tiering
<a name="9999999999999999s3--intelligent-tiering.35f3ca94-2581-5245-84e0-4a28bd61d2b2"></a>

For backups going to Amazon S3 buckets, you can enable [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) as your Amazon S3 File Gateway [storage class](https://docs.aws.amazon.com/filegateway/latest/files3/storage-classes.html#ia-file-gateway). This can reduce storage costs by up to 30 percent. You then mount S3 File Gateway to your SQL servers by using an SMB file share that can be integrated with your [Active Directory domain](https://docs.aws.amazon.com/filegateway/latest/files3/CreatingAnSMBFileShare.html#configure-SMB-settings). This provides you with access control for your share, the ability to use existing service accounts, and access to Amazon S3 through a common Microsoft-focused file protocol. For accounts that might not have direct connectivity to a domain controller, you can use [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) to facilitate communication with Active Directory on premises or in the cloud. To configure the Active Directory settings on the gateway, you must specify the AD Connector IP addresses for the domain controller to proxy requests to Active Directory.

The following diagram shows an architecture for a solution based on Amazon S3 Intelligent-Tiering.

![S3 Intelligent-Tiering architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/f478de02-0015-4f5b-9202-8f3da5218b50.png)

By default, the backup files written to the Amazon S3 bucket use the Standard tier. To convert the backup files from the Standard tier to Amazon S3 Intelligent-Tiering, you must [create a lifecycle rule](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html). You can also use the [AWS Management Console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html#enable-auto-archiving-int-tiering) to enable Amazon S3 Intelligent-Tiering. For more information, see [Getting Started Using Amazon S3 Intelligent-Tiering](https://aws.amazon.com/getting-started/hands-on/getting-started-using-amazon-s3-intelligent-tiering/) in the AWS documentation.

### Single Availability Zone
<a name="single-availability-zone.14c6a6db-f447-512f-a8e2-d1aef1642f5c"></a>

To create a Single Availability Zone file system, choose the Single-AZ option when you [create an FSx for Windows File Server file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html). Amazon FSx also takes highly durable daily backups of your file system (stored in Amazon S3) by using the Windows Volume Shadow Copy Service, and you can take additional backups at any point. Consider the limitations of using a single Availability Zone. For example, the SMB file share becomes inaccessible if the Availability Zone where the file system is provisioned experiences an extended outage. If you require access to the data, you must restore it from backups in an available Availability Zone within the source Region. For more information, see the [Use a single Availability Zone](storage-fsx-single-az.md) section of this guide.

### Backup to URL
<a name="backup-to-url.95077af3-d4dc-5b9b-8099-3ae3266d0b99"></a>

For SQL Server 2022, the [backup to URL](https://www.microsoft.com/en-us/sql-server/blog/2022/09/29/backup-and-restore-to-url-for-s3-compatible-object-storage/) feature allows direct backup to Amazon S3. This is a recommended backup approach for SQL Server 2022 running in AWS because you get the full feature set of Amazon S3 at the storage layer and remove the cost of the AWS Storage Gateway appliance that prior versions needed to provide this functionality. There are two primary costs to consider when you implement this feature: data transfer costs and the Amazon S3 storage class that you choose. If you want the native disaster recovery capabilities of Amazon S3, factor in that [cross-Region replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario) incurs cross-Region [data egress costs](https://aws.amazon.com/s3/pricing/?p=pm&c=s3&z=4). To learn more about how to configure this option, see the [Backup SQL Server databases to Amazon S3](https://aws.amazon.com/blogs/modernizing-with-aws/backup-sql-server-to-amazon-s3/) post on the Microsoft Workloads on AWS blog.

## Additional resources
<a name="sql-server-backup-resources"></a>
+ [Backup and restore options for SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/welcome.html) (AWS Prescriptive Guidance)
+ [Point-in-time recovery and continuous backup for Amazon RDS with AWS Backup](https://aws.amazon.com/blogs/storage/point-in-time-recovery-and-continuous-backup-for-amazon-rds-with-aws-backup/) (AWS Storage Blog)
+ [Protect your SQL Server workloads using NetApp SnapCenter with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-netapp-snapcenter-with-amazon-fsx-for-netapp-ontap-to-protect-your-sql-server-workloads/) (AWS Storage Blog)
+ [Getting Started Using Amazon S3 Intelligent-Tiering](https://aws.amazon.com/getting-started/hands-on/getting-started-using-amazon-s3-intelligent-tiering/) (AWS Getting Started Resource Center)
+ [Backup and Restore Strategies for Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/backup-and-restore-strategies-for-amazon-rds-for-sql-server/) (AWS Database Blog)
+ [Migrate an on-premises Microsoft SQL Server database to Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2.html) (AWS Prescriptive Guidance)
+ [Best Practices for Deploying Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/best-practices-for-deploying-microsoft-sql-server.html) (AWS Whitepaper)
