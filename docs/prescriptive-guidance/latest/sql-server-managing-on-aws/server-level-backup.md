---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/server-level-backup.html
---

# Server-level backup options
<a name="server-level-backup"></a>

Server-level backup covers backing up your whole SQL Server EC2 instance, which includes all system and user databases on the EC2 instance. If you have multiple SQL Server instances on Amazon EC2, that is also included in the server-level backup.

## SQL Server backup using VSS-enabled EBS snapshots
<a name="vss-enabled"></a>

Windows Volume Shadow Copy Service (VSS) orchestrates operating system and application access to underlying inputs and outputs (I/O), enabling an application-consistent snapshot of underlying storage without any application down-time. SQL Server is [VSS-aware](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/application-consistent-snapshots.html), so you can use VSS agent to take EBS snapshots of SQL Server instances.

The following diagram shows the architecture of a backup and restore solution using VSS-enabled EBS snapshots.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/images/guide-img/465b5bfb-6afe-43d5-ad91-28d097c28a50/images/6278c649-86ff-4b92-9026-924adba8af7d.png)

This architecture uses the AWS Systems Manager Run Command to install the VSS agent on your SQL Server instances. You can also use the Run Command to invoke the entire workflow of flushing operating system and application buffers to the disk, pausing I/O operations, taking a point-in-time snapshot of the EBS volumes, and then resuming I/O.

This Run Command creates automated snapshots of all EBS volumes attached to a target instance. You also have the option to exclude the root volume, because user database files are usually stored on other volumes. In case you stripe multiple EBS volumes to create a single file system for SQL Server files, Amazon EBS also supports crash-consistent multivolume snapshots using a single API command.

The process for taking application-consistent, [VSS-enabled EBS snapshots](https://aws.amazon.com/blogs/mt/take-microsoft-vss-enabled-snapshots-using-amazon-ec2-systems-manager/) is covered in the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/application-consistent-snapshots.html).

Using this method provides the following benefits:
+ The first snapshot of a DB instance contains the data for the full DB instance. Subsequent snapshots of the same DB instance are [incremental](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html#how_snapshots_work), which means that only the data that has changed after your most recent snapshot is saved.
+ You can [restore to a new SQL Server EC2 instance from a snapshot](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/restore.html).
+ If an instance is encrypted using Amazon EBS or if a database is encrypted in the instance using transparent data encryption (TDE), that instance or database is automatically restored with the same encryption.
+ You can copy your [automated cross-Region backups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-policy.html).
+ When you restore an EBS volume from a snapshot, it becomes immediately available for applications to access it. This means that you can immediately bring SQL Server online after restoring one or more of its underlying EBS volumes from snapshots.
+ By default, restored volumes fetch underlying blocks from Amazon S3 the first time an application tries to read them. This means that there can be a lag in performance after an EBS volume is restored from a snapshot. The volume eventually catches up with the nominal performance. However, you can avoid that lag by using [fast snapshot-restore](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html) (FSR) snapshots. This feature enables you to get full performance immediately after restoring a volume.
+ You can use [life cycle management for EBS snapshots](https://aws.amazon.com/blogs/aws/new-lifecycle-management-for-amazon-ebs-snapshots/).

However, using automated snapshots has certain limitations:
+ You can't perform cross-Region point-in-time recovery (PITR) with an encrypted snapshot for a SQL Server instance.
+ You can't create an encrypted snapshot of an unencrypted instance.
+ You can't restore an individual database because the snapshot is taken at the EBS volume level.
+ You can't restore the instance to itself.
+ A snapshot of the DB instance must be encrypted using the same AWS Key Management System (AWS KMS) key as the DB instance.
+ Storage I/O is suspended for a fraction of a second (approximately 10 milliseconds) during the snapshot backup process.

## SQL Server backup using AWS Backup
<a name="aws-backup"></a>

Using AWS Backup, you can centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale. AWS Backup also helps you support your regulatory compliance obligations and meet your business continuity goals. Together with [AWS Organizations](https://aws.amazon.com/organizations/), AWS Backup enables you to centrally deploy data protection (backup) policies to configure, manage, and govern your backup activity across your organization's AWS accounts and resources.

The following diagram shows the architecture of a backup and restore solution for SQL Server on EC2 using AWS Backup.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/images/guide-img/465b5bfb-6afe-43d5-ad91-28d097c28a50/images/e4fa5e37-201d-42ed-9cca-dc903a3547ad.png)

 This solution has the following benefits:
+ You can automate backup scheduling, retention management, and lifecycle management.
+ You can centralize your backup strategy across your organization, spanning multiple accounts and AWS Regions.
+ You can centralize monitoring your backup activity and alerting across AWS services.
+ You can implement cross-Region backups for disaster recovery planning.
+ The solution supports cross-account backups.
+ You can perform secure backups with secondary backup encryption.
+ All backups support encryption using AWS KMS encryption keys.
+ The solution works with TDE.
+ You can restore to a specific recovery point from the AWS Backup console.
+ You can back up an entire SQL Server instance, which includes all SQL Server databases.

Using AWS Backup has certain limitations:
+ You can't perform native SQL backup and restore.
+ You can't do cross-Region point-in-time recovery (PITR).
+ You must enable the EC2 instance for Systems Manager access.
+ You must configure the instance with VSS and enable VSS backups in the backup job.

 For more information about using AWS Backup for SQL Server backups, see the blog post [How to simplify Microsoft SQL Server backup using AWS Backup and VSS](https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/).

 For information about using AWS Backup to do point-in-time recovery for Amazon RDS for SQL Server, see the blog post [Point-in-time recovery and continuous backup for Amazon RDS with AWS Backup](https://aws.amazon.com/blogs/storage/point-in-time-recovery-and-continuous-backup-for-amazon-rds-with-aws-backup/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
