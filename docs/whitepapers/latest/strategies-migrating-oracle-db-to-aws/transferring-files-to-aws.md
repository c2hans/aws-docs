---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/transferring-files-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Transferring files to AWS
<a name="transferring-files-to-aws"></a>

 Migrating databases to AWS requires the transfer of files to AWS. There are multiple methods of transferring files to AWS. This section describes the methods you can adopt during the migration process.

## AWS DataSync
<a name="aws-datasync"></a>

 AWS DataSync is an online data transfer service that can accelerate moving data between an on-premises storage system and AWS storage services such as Amazon S3, Amazon EFS, or FSx for Windows File Server. AWS DataSync agent connects to the on-premises storage and copies data and metadata securely to AWS. AWS DataSync is the recommended option when you have large volume of small files 100 MB or less.

## AWS Storage Gateway
<a name="aws-storage-gateway"></a>

 AWS Storage Gateway is a service connecting an on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organization’s on-premises IT environment and the AWS storage infrastructure. The service allows you to securely store data in the AWS Cloud for scalable and cost-effective storage. AWS Storage Gateway supports open standard storage protocols that work with your existing applications. It provides low-latency performance by maintaining frequently accessed data on-premises while securely storing all of your data encrypted in [Amazon S3](https://aws.amazon.com/s3/) or [Amazon Glacier](https://aws.amazon.com/s3/glacier/). AWS Storage Gateway works with moderate or large file sizes.

 AWS Storage Gateway S3 File Gateway interface provides a Network File System/Server Message Block (NFS/SMB) file share in your on-premises environment. They run a local VM in your on-premises data center. Files can be copied at the on-premises location to this local file-share. These files are copied to the designated S3 bucket in AWS. If your workload uses Windows OS, you can use [Amazon FSx File Gateway](https://aws.amazon.com/storagegateway/file/fsx/) to copy files from on-premises via SMB clients to the [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/).

## Amazon RDS integration with S3
<a name="amazon-rds-integration-with-s3"></a>

 You can use S3 integration to transfer files between an Amazon S3 bucket and an Amazon RDS instance. The Amazon RDS instance accesses S3 bucket via a defined IAM role, so you can have granular bucket or object level policies for the Amazon RDS instance. Amazon S3 integration is useful when you have to use Oracle utilities like `utl_file` or `datapump`. Amazon RDS Oracle `rdsadmin` package supports both upload and download from S3 buckets.

## Tsunami UDP
<a name="tsunami-udp"></a>

 [Tsunami UDP](http://tsunami-udp.sourceforge.net/) is an open-source, file transfer protocol that uses TCP control and UDP data for transfer over long-distance networks at a very fast rate. When you use UDP for transfer, you gain more throughput than is possible with TCP over the same networks.

 You can download Tsunami UDP from the [Tsunami UDP Protocol](https://sourceforge.net/projects/tsunami-udp/) page at SourceForge.net. For moderate to large databases between 100 GB to 5 TB, Tsunami UDP is an option, as described in Using Tsunami to Upload Files to EC2. You can achieve the same results using commercial third-party WAN acceleration tools. For very large databases over 5 TB, using AWS Snow Family devices might be a better option. For smaller databases, you can also use the [Amazon S3 multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) capability to keep it simple and efficient.

## AWS Snow Family
<a name="aws-snow-family"></a>

 [AWS Snow Family](https://aws.amazon.com/snow/) offers a number of physical devices and capacity points transport up to exabytes of data into and out of AWS. Snow Family devices are owned and managed by AWS and integrate with AWS security, monitoring, storage management, and computing capabilities. For example, [AWS Snowball Edge Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) has 80 TB of usable capacity and can be mounted as an NFS mount point in the on-premises location. For smaller capacity, [AWS Snowcone](https://aws.amazon.com/snowcone/) offers 8 TB of storage and has the capability to run the [AWS DataSync](https://aws.amazon.com/datasync/) agent.
