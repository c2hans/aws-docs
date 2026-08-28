---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html
---

# Backing up your Amazon S3 data
<a name="backup-for-s3"></a>

Amazon S3 is natively integrated with AWS Backup, a fully managed, policy-based service that you can use to centrally define backup policies to protect your data in Amazon S3. After you define your backup policies and assign Amazon S3 resources to the policies, AWS Backup automates the creation of Amazon S3 backups and securely stores the backups in an encrypted backup vault that you designate in your backup plan.

When using AWS Backup for Amazon S3, you can perform the following actions:
+ Create continuous backups and periodic backups. Continuous backups are useful for point-in-time restore, and periodic backups are useful to meet your long-term data-retention needs.
+ Automate backup scheduling and retention by centrally configuring backup policies.
+ Restore backups of Amazon S3 data to a point in time that you specify.
+ Access backup data directly through S3 access points without initiating a restore, enabling targeted file recovery, data validation, and compliance auditing.

Along with AWS Backup, you can use S3 Versioning and S3 Replication to help recover from accidental deletions and perform your own self-recovery operations.

**Accessing backup data**
AWS Backup lets you read Amazon S3 backup data directly through S3 access points without initiating a full restore. You create a backup access point for a specific S3 recovery point, and AWS Backup provisions an S3 access point that you can use with standard S3 read operations such as `GetObject`, `HeadObject`, and `ListObjectsV2`.

For more information, see [Backup access points](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-access-points.html) in the *AWS Backup Developer Guide*.

**Prerequisites**
You must activate [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) on your bucket before AWS Backup can back it up.

**Note**
We recommend that you [ set a lifecycle expiration rule for versioning-enabled buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lifecycle-config-conceptual-ex6) that are being backed up. If you do not set a lifecycle expiration period, your Amazon S3 storage costs might increase because AWS Backup retains all versions of your Amazon S3 data.

**Getting started**
To get started with AWS Backup for Amazon S3, see [ Creating Amazon S3 backups ](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) in the *AWS Backup Developer Guide*.

**Restrictions and limitations**
To learn about the limitations, see [ Creating Amazon S3 backups ](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) in the *AWS Backup Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
