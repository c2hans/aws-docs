---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/database-level-backup.html
---

# Database-level backup options
<a name="database-level-backup"></a>

These approaches use native Microsoft SQL Server backup functionality. You can take backups of individual databases on the SQL Server instance and restore an individual database.

Each of these options for native SQL Server backup and restore also support the following:
+ Compression and multiple-file backup
+ Full, differential, and T-log backups
+ Transparent data encryption (TDE)-encrypted databases

## SQL Server native backup and restore to Amazon S3 using AWS Storage Gateway
<a name="storage-gateway"></a>

SQL Server on EC2 supports native backup and restore for SQL Server databases[.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Enabling) You can take a backup of your SQL Server database and then restore the backup file to an existing database or to a new SQL Server EC2 instance, Amazon RDS for SQL Server, or an on-premises server. You can use [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) to back up your Microsoft SQL Server databases directly to [Amazon S3](https://aws.amazon.com/s3/), reducing your on-premises storage footprint and using Amazon S3 for durable, scalable, and cost-effective storage. Storage Gateway is a hybrid cloud storage service that provides on-premises applications with access to virtually unlimited cloud storage.

The following diagram shows the architecture of a native backup and restore solution using Storage Gateway and Amazon S3.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/images/guide-img/465b5bfb-6afe-43d5-ad91-28d097c28a50/images/9b1c8752-3ab2-40cc-8a72-3c66e4353490.png)

Native SQL Server backup with Storage Gateway provides the following benefits:
+ You can map a storage gateway as a Server Message Block (SMB) file share on the EC2 instance and send the backup to Amazon S3.
+ The backup occurs directly to the S3 bucket or through the Storage Gateway file cache.
+ Multiple-file backups are supported.

Native backup using Storage Gateway has the following limitations:
+ You must set up backup and restore for each individual database.
+ You must manage the [Amazon S3 lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) for the backup files.

For more information about how to set up Storage Gateway, see [Store SQL Server backups in Amazon S3 using AWS Storage Gateway](https://aws.amazon.com/blogs/database/storing-sql-server-backups-in-amazon-s3-using-aws-storage-gateway/).

## SQL Server native backup to EBS volumes
<a name="ebs-volumes"></a>

You can take a native backup of your SQL Server database and store the file in an Amazon Elastic Block Store (Amazon EBS) volume. Amazon EBS is a highly performant block storage service. EBS volumes are elastic, which supports encryption, and they can be detached and attached to an EC2 instance. SQL Server on an EC2 instance can be backed up on same EBS volume type or on a different EBS volume type. One advantage of backing up to a different EBS volume is cost savings.

The following diagram shows the architecture of a native backup to an EBS volume.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/images/guide-img/465b5bfb-6afe-43d5-ad91-28d097c28a50/images/42216fa9-f793-4bbf-8036-a994734af275.png)

SQL Server native backup to EBS volumes provides the following benefits:
+ You can take backups of individual databases on a SQL Server EC2 instance and restore an individual database instead of having to restore the complete instance.
+ Multiple-file backups are supported.
+ You can schedule backup jobs by using SQL Server Agent and the SQL Server job engine.
+ You can get performance benefits through your hardware choices. For example, you can use st1 storage volumes to achieve higher throughput.

When using native backup to EBS volumes, consider the following points:
+ You must manually move backups to Amazon S3 from the EBS volume.
+ For large backups, you must manage disk space on EC2.
+ On the EC2 instance, Amazon EBS throughput can be a bottleneck.
+ Additional storage is required to store backups on Amazon EBS.

## SQL Server native backup to Amazon FSx for Windows File Server
<a name="amazon-fsx"></a>

[Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) is a fully managed native Windows file system that offers up to 64 TB of storage designed to deliver fast, predictable, and consistent performance. AWS introduced [native support for Multi-AZ file system deployments](https://aws.amazon.com/blogs/aws/amazon-fsx-for-windows-file-server-update-new-enterprise-ready-features/) on FSx for Windows File Server. Native support makes it easier to deploy Windows file storage on AWS with high availability and redundancy across multiple Availability Zones. Along with this launch, AWS also introduced support for [SMB Continuously Available (CA) file shares](https://aws.amazon.com/about-aws/whats-new/2019/11/amazon-fsx-for-windows-file-server-adds-support-for-high-availability-microsoft-sql-server-deployments/). You can use FSx for Windows File Server as backup storage for a SQL Server database.

The following diagram shows the architecture of a native SQL Server backup to FSx for Windows File Server.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/images/guide-img/465b5bfb-6afe-43d5-ad91-28d097c28a50/images/3e6f0296-5a3c-4cf6-ba67-68d8100cd57d.png)

This approach has the following benefits:
+ You can back up your SQL Server database to an Amazon FSx file share.
+ You can take backups of individual databases on a SQL Server instance and restore an individual database instead of having to restore the complete instance.
+ Multiple-part backups are supported.
+ You can schedule backup jobs by using SQL Server Agent and the job engine.
+ The instances have higher network bandwidth, compared with Amazon EBS.

Native backup to FSx for Windows File Server has the following limitations:
+ You must manually move backups to Amazon S3 from Amazon FSx by using [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) or [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).
+ Large backups might require additional overhead for disk space management on Amazon FSx.
+ EC2 instance network throughput can be a bottleneck.
+ Additional storage is required to store backups on FSx for Window File Server.
