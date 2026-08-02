---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/restore-options.html
---

# Restore options for SQL Server databases on Amazon EC2
<a name="restore-options"></a>

The following sections provide several database restore options for SQL Server on Amazon Elastic Compute Cloud (Amazon EC2), when your backups are on premises.

## Using Amazon S3
<a name="s3"></a>

This approach uses Amazon Simple Storage Service (Amazon S3) commands for the AWS Command Line Interface (AWS CLI) or the Amazon S3 API to upload the backup files directly to an S3 bucket.

![Using Amazon S3 to restore your SQL Server database](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/images/guide-img/09ec13da-971b-4981-975f-0940015d7fc0/images/c098974a-7df7-402f-89a0-6e5d625e8dee.png)

The process consists of these steps:

1. Create an Amazon S3 bucket (or use an existing bucket) to store the backup files, and transfer backup (.bak) files from your on-premises database to the S3 bucket by using the AWS CLI or Amazon S3 API.

1. Deploy SQL Server on an EBS-optimized EC2 instance, using a SQL Server Amazon Machine Image (AMI). This AMI must contain EBS volumes that are configured with an OS partition, a DATA partition, a LOG partition, tempdb (NVMe) storage, and scratch space.

1. (Optional) Attach a non-root Amazon EBS volume to the Amazon EC2 instance.

1. Copy the backup files to the non-root EBS volume.

1. Restore the backup files from the EBS volume to SQL Server on the EC2 instance.

1. Use SQL Server management tools to manage your database.

## Using AWS DataSync and Amazon FSx
<a name="datasync-fsx"></a>

This SQL Server database restore approach uses AWS DataSync to transfer the backup files to Amazon FSx for Windows File Server.

![Using AWS DataSync and Amazon FSx to restore your SQL Server database](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/images/guide-img/09ec13da-971b-4981-975f-0940015d7fc0/images/d9f2af98-d4f0-4417-8381-87298f019ae9.png)

The process consists of these steps:

1. Deploy SQL Server on an EBS-optimized EC2 instance with attached NVMe, using an AMI that contains EBS volumes configured with OS, DATA, LOG, and tempdb. (For example, you can use the memory optimized `r5d.large` instance class.)

1. Use Amazon FSx for Windows File Server to create a file server. This can be used as a temporary storage location to download SQL Server backup (.bak) files from your on-premises environment.

1. Create a DataSync endpoint and agent for the Amazon FSx file server.

1. DataSync automates data synchronization between your on-premises storage and the Windows file server without requiring Amazon S3.

1. Restore the backup files from the Amazon FSx file server to SQL Server on the EC2 instance.

1. Use SQL Server management tools to manage your database.

**Note**
Amazon EC2 offers [Microsoft SQL Server on Microsoft Windows Server AMIs](https://aws.amazon.com/about-aws/whats-new/2021/10/amazon-ec2-microsoft-sql-server-windows-ami/) for multiple SQL Server editions.

## Using Amazon S3 File Gateway
<a name="s3-file-gateway"></a>

You can use [Amazon S3 File Gateway](https://aws.amazon.com/blogs/storage/easily-store-your-sql-server-backups-in-amazon-s3-using-file-gateway/) to store native SQL Server backups to Amazon S3, as illustrated in the following diagram. Alternatively, there are tools such as [Commvault](https://www.commvault.com/) and [LiteSpeed](https://www.quest.com/products/litespeed-for-sql-server/) that help you manage file-level backups at scale and store them directly in Amazon S3. You can also use tools such as [Actifio ](https://www.actifio.com/solutions/cloud/aws/)and [SIOS DataKeeper](https://aws.amazon.com/quickstart/architecture/sios-datakeeper/) for backup/recovery and DR configuration.

![Using S3 File Gateway to restore your SQL Server database](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/images/guide-img/09ec13da-971b-4981-975f-0940015d7fc0/images/4ecf9b41-fae6-4acd-b61b-a58a54351783.png)

The process consists of these steps:

1. Data is written on the file gateway's local cache disk.

1. After the data is safely persisted to the local cache, the file gateway acknowledges the completion of the write operation to the client application.

1. The file gateway transfers data to the S3 bucket asynchronously. It optimizes data transfer and uses HTTPS to encrypt data in transit.

1. After data is uploaded to the S3 bucket, it stays in the file gateway's local cache until it is evicted.
