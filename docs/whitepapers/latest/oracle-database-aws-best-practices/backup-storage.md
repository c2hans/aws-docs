---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/backup-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Backup storage
<a name="backup-storage"></a>

 Most Oracle Database users take regular hot and cold backups. Cold backups are taken while the database is shut down, whereas hot backups are taken while the database is active. AWS native storage services offer a choice of solutions for your needs.

## Amazon S3
<a name="amazon-s3"></a>

 Store your hot and cold backups in Amazon Simple Storage Service (Amazon S3) for high durability and easy access. You can use the [AWS Storage Gateway file interface](https://aws.amazon.com/storagegateway) to directly back up the database to Amazon S3. AWS Storage Gateway file interface provides an NFS mount for S3 buckets. Oracle Recovery Manager (RMAN) backups written into the Network File System (NFS) mount are automatically copied to S3 buckets by the AWS Storage Gateway instance.

## Amazon S3 Glacier
<a name="amazon-s3-glacier"></a>

 Amazon Glacier is a secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup. You can use lifecycle policies in Amazon S3 to move older backups to Amazon Glacier for long-term archiving. Amazon Glacier offers three options for data retrieval with varying access times and costs: Expedited, Standard, and Bulk retrievals. For more information about these options, refer to [Amazon S3 Glacier FAQs](https://aws.amazon.com/glacier/faqs/#dataretrievals).

## Amazon S3 Glacier Deep Archive
<a name="amazon-s3-glacier-deep-archive"></a>

 Amazon S3 Glacier Deep Archive is designed for long-term retention and digital preservation for the data that might be accessed once or twice a year. All objects stored in S3 Glacier Deep Archive are replicated and stored across at least three geographically dispersed Availability Zones, protected by 99.999999999% of durability, and can be restored within 12 hours.

## Amazon EFS
<a name="amazon-efs"></a>

 Amazon Elastic File System (Amazon EFS) provides a simple, serverless, set-and-forget, elastic file system. With Amazon EFS, you can grow and shrink your file systems automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth.

Backups stored in Amazon EFS can be shared with NFS options (read/write, read-only) to other EC2 instances. Amazon EFS uses bursting model for EFS performance. Accumulated burst credits give the file system the capability to drive throughput above its baseline rate. A file system can drive throughput continuously at its baseline rate.

 Whenever it's inactive or throughput is below its baseline rate, the file system accumulates burst credits. Amazon EFS is useful when you have to refresh dev and test databases from production database Recovery Manager (RMAN) backups regularly. Amazon EFS can also be mounted in on-premises data centers when connected to your Amazon VPC with AWS Direct Connect. This option is useful when the source Oracle database is in AWS and the databases that need to be refreshed are in on-premises data centers. Backups stored in Amazon EFS can be copied to an S3 bucket using AWS CLI commands. Refer to [Getting started with Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html) for more information.

## Amazon EBS Snapshots
<a name="amazon-ebs-snapshots"></a>

 You can back up the data on your Amazon Elastic Block Store volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. When you create an Amazon EBS volume based on a snapshot, the new volume begins as an exact replica of the original volume that was used to create the snapshot. The replicated volume utilizes lazy loading for data in the background so that you can begin using it immediately. If you access data that hasn't been loaded yet, the volume immediately downloads the requested data from Amazon S3, and then continues loading the rest of the volume's data in the background. Refer to [Create Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
