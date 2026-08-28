---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-instant-access.html
---

# Backup instant access permissions
<a name="backup-instant-access"></a>

When using Amazon GuardDuty Malware Protection for AWS Backup with S3 backups, Amazon GuardDuty accesses your S3 backups through three APIs: CreateBackupAccessPoint, DescribeBackupAccessPoint, and DeleteBackupAccessPoint.

Amazon GuardDuty uses CreateBackupAccessPoint to access your encrypted backup data. During the scan job, GuardDuty uses DescribeBackupAccessPoint to verify successful access point creation. Once the scan completes, GuardDuty calls DeleteBackupAccessPoint to remove its access to your backup.

This workflow applies to both S3 backups and EC2/EBS backups stored in a logically air-gapped vault.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
