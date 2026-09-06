---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/next-steps-and-resources.html
---

# Next steps and resources
<a name="next-steps-and-resources"></a>

This guide covered best practices for quick disaster recovery of SQL Server databases. The recommendations include using images to restore the application instance and to use native SQL methods to restore the database, or, preferably, to fail over the database. In contrast to large database restores that can take hours, using Amazon Elastic Compute Cloud (Amazon EC2) Amazon Machine Image (AMI) backups in combination with the most recent transaction logs helps you meet your recovery point objective (RPO) and recovery time objective (RTO) requirements while keeping your overall costs low. The optimal approach depends on the size of your database, the number and nature of backups, and the frequency of transaction log backups for which a disaster recovery strategy needs to be designed. See the following links for more information, best practices, Quick Start guides, and prescriptive guidance on migrating and hosting SQL Server on Amazon EC2.

## AWS service documentation
<a name="service-documentation"></a>
+ [Best practices and recommendations for SQL Server clustering on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/aws-sql-clustering.html) (Amazon EC2 documentation)
+ [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) (Amazon EC2 documentation)
+ [Replicating objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) (Amazon S3 documentation)
+ [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html) (Amazon EC2 documentation)
+ [SQL Server with Always On replication on the AWS Cloud](https://aws-quickstart.github.io/quickstart-microsoft-sql/) (Quick Start reference deployment)
+ [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) (Amazon EC2 documentation)
+ [Using FSx for Windows File Server with Microsoft SQL Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/sql-server.html) (Amazon FSx documentation)
+ [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) (AWS Backup documentation)
+ [AWS Windows AMIs](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html#win-ami-config-fast-launch) (Amazon EC2 documentation)

## AWS Prescriptive Guidance
<a name="prescriptive-guidance"></a>
+ [Best practices for deploying Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/)
+ [Amazon EC2 backup and recovery with snapshots and AMIs](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/ec2-backup.html)
+ [Place tempdb in an instance store](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/tempdb.html)

## Blog posts and news
<a name="blog-posts-and-news"></a>
+ [Easily store your SQL Server backups in Amazon S3 using File Gateway](https://aws.amazon.com/blogs/storage/easily-store-your-sql-server-backups-in-amazon-s3-using-file-gateway/)
+ [Monitor data transfer costs related to Amazon S3 Replication](https://aws.amazon.com/blogs/storage/monitor-data-transfer-costs-related-to-amazon-s3-replication/)
+ [Multi-region SQL Server deployment using distributed availability groups](https://aws.amazon.com/blogs/database/multi-region-sql-server-deployment-using-distributed-availability-groups/)
+ [Field Notes: Building a Multi-Region Architecture for SQL Server using FCI and Distributed Availability Groups](https://aws.amazon.com/blogs/architecture/field-notes-building-a-multi-region-architecture-for-sql-server-using-fci-and-distributed-availability-groups/)

## SQL Server documentation
<a name="sql-server-documentation"></a>
+ [Editions and supported features of SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver15)
