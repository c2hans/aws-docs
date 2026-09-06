---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/migrating-file-servers-workloads.html
---

# Migrating file servers
<a name="migrating-file-servers-workloads"></a>

Storage is an essential component to any workload you run. AWS has a number of options to store files in the cloud, including block, file, and object storage. For Microsoft workloads the most common options are block and file storage options. This section provides strategies to help you migrate your storage for Microsoft workloads to the AWS Cloud and guides you through the migration of your file servers.

## Assess
<a name="migrating-file-servers-workloads-assess"></a>

There are three major storage types: object, block, and file storage. AWS offers a wide portfolio of storage services that can be categorized under each of these. A successful migration depends on understanding your current needs and then [comparing](https://aws.amazon.com/blogs/storage/comparing-your-on-premises-storage-patterns-with-aws-storage-services/) them with various AWS storage services to gauge what works best for you. Choosing the right technology for your workload is key to long-term success. We recommend that you avoid trying to match exactly what you use currently for storage. Instead, we recommend that you look into what all the available options are and select the option that makes the most sense to optimize the cost and performance of your Microsoft workloads. For example, consider a large on-premises file server that requires local block storage. On AWS, the optimal choice could be to move it to [Amazon FSx](https://aws.amazon.com/fsx/) to get the same performance you had for your file server, while removing the undifferentiated heavy lifting of administering the file server and backend storage.

TCO is a key item to evaluate as you assess which storage option works best for you. Keep in mind that using an AWS managed service to help reduce operation costs can help you choose the right overall storage solution on AWS. To request a storage assessment, contact us at `migration-evaluator@amazon.com`. A storage specialist will help you assess your workloads, map your workloads to the most appropriate AWS storage service, and provide you with directional cost estimates. The storage assessment has three phases:

1. You start the discovery process by installing an agentless collector or receiving output from an existing tool set in a flat file.

1. You let the discovery process run for 7–60 days.

1. The storage collector analyzes the data from the discovery tool, and then proposes a target storage solution and provides directional cost estimates for the solution.

If the cost is slightly higher for a storage option, consider if that storage option reduces the overall cost in the long term and find out what your teams must do to maintain the security and reliability of your storage. It could be the right long-term solution for your workload.

When you're assessing the right solution it's important to look at performance and costs. You can use tools like [Windows Performance Monitor](https://techcommunity.microsoft.com/blog/askperf/windows-performance-monitor-overview/375481) to identify the IOPS, throughput, and other performance needs of your workload and then implement the same testing on the AWS solution that you choose for your workload. Additionally, you can use the Amazon CloudWatch agent to [view metrics for Performance Monitor on a Windows server](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows) and analyze the metrics of your workloads before putting those workloads into production.

### Identify the AWS storage service that best meets your needs
<a name="identify-the-9999999999999999aws--storage-service-that-best-meets-your-needs.978104c8-910d-5b39-b3bc-28e25781afdd"></a>

The choice of storage service typically depends on your use case, application needs, familiarity, performance profiles, and data management capabilities. Consider the following:
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon S3 is object storage built to store and retrieve any amount of data from anywhere. Amazon S3 offers a range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads. You can implement file-based access to Amazon S3 by using [AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/CreatingAnSMBFileShare.html). This enables you to take advantage of the low cost storage of Amazon S3, while not having to completely rewrite an application that uses a Server Message Block (SMB).
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) – Amazon EBS provides block-level storage volumes for use with Amazon EC2 instances. Amazon EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances. Amazon EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance.
+ [Amazon FSx](https://docs.aws.amazon.com/fsx/)** **– Amazon FSx offers four different file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre. For guidance about choosing the right system, see [Choosing an Amazon FSx file system](https://aws.amazon.com/fsx/when-to-choose-fsx/). Amazon FSx offers a managed file storage solution in various file system types to enable you to migrate your Microsoft workloads to AWS and remove some of the operational overhead from your IT staff. This enables IT to focus on other critical business drivers.
+ [AWS Snow Family](https://aws.amazon.com/snowball/)** **– If you have petabyte scales of data to move into AWS, consider using a storage solution from the Snow Family. While your storage won't rely on the Snow Family device for the long-term life of your data, it can help you seed large data sets to AWS offline by using an AWS Snowball Edge, AWS Snowball, or AWS Snowmobile device. For more information, see the [Seamlessly migrate large SQL databases using AWS Snowball and AWS DataSync](https://aws.amazon.com/blogs/storage/seamlessly-migrate-large-sql-databases-using-aws-snowball-and-aws-datasync/) post on the AWS Storage Blog.

We recommend that you conduct tests by using stress/load testing tools before moving production data, after you identify the storage service for your workloads. For example, if you're moving your SQL databases on Amazon FSx for Windows File Server, you can use [Microsoft SQL Server Distributed Replay](https://learn.microsoft.com/en-us/sql/tools/distributed-replay/sql-server-distributed-replay?view=sql-server-ver16). Similarly, you can use [DISKSPD](https://learn.microsoft.com/en-us/azure-stack/hci/manage/diskspd-overview) for general IOPS and throughput.

## Mobilize
<a name="migrating-file-servers-workloads-mobilize"></a>

After you identify a storage service, the next step is to select a tool for data transfer. Several tools are available, including older solutions like [Robocopy](https://learn.microsoft.com/en-us/archive/technet-wiki/1073.robocopy-and-a-few-examples) and more modern tools like [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html). DataSync includes a number of controls that aren't available in tools like Robocopy, such as scheduled transfer and easier control of network throttling to help migrate your data without impacting your overall network traffic. For more information about successful migrations completed with DataSync, see the [customer testimonials](https://aws.amazon.com/datasync/customers/) in DataSync customers.

If you're more comfortable with Robocopy, you can use it to migrate your data to AWS. We recommend that you review this guide on how to optimize [file transfer performance](https://repost.aws/knowledge-center/direct-connect-file-transfer). The guide can help you avoid running into issues during your migration. If you use Robocopy with a file system that has deduplication enabled, see [Data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html#using-data-dedup) in the Amazon FSx for Windows File Server documentation and [Troubleshooting Data Deduplication Corruptions](https://learn.microsoft.com/en-us/archive/technet-wiki/31038.troubleshooting-data-deduplication-corruptions) in the Microsoft documentation to avoid issues with data corruption.

[AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/index.html) can migrate data to AWS in three ways: files, volumes, and virtual tapes. You can install Storage Gateway on a VMware or Hyper-V hypervisor running on-premises, an Amazon EC2 instance in your Amazon VPC, or a dedicated hardware appliance.

Storage Gateway can help you bridge the gap from on-premises to AWS and help you reduce your costs. You can use Storage Gateway to implement your migration in phases and use it to replace an on-premises backup device and tapes with a virtual tape library (VTL). You could also use Storage Gateway as an archival storage solution to start migrating only your local unused files to AWS as the first phase of your migration. There are a number of options for using Storage Gateway to host your Microsoft workload on AWS.

## Migrate
<a name="migrating-file-servers-workloads-migrate"></a>

DataSync and Robocopy are both equipped to preserve network access control lists (ACLs, also known as Windows ACLs). Before you begin migration, we recommend that you take a backup copy of ACLs by using [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) and review the following resources:
+ [Migrating on-premises file shares to Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/migrating-on-premises-file-shares-to-amazon-fsx-for-netapp-ontap/) (AWS Storage Blog)
+ [Migrating existing file storage to Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-to-fsx.html) (Amazon FSx for Windows File Server documentation)
+ [Transferring files from on premises to AWS and back without leaving your VPC using AWS DataSync](https://aws.amazon.com/blogs/storage/transferring-files-from-on-premises-to-aws-and-back-without-leaving-your-vpc-using-aws-datasync/) (AWS Storage Blog)
+ [Migrate small sets of data from on premises to Amazon S3 using AWS SFTP](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp.html) (AWS Prescriptive Guidance)
