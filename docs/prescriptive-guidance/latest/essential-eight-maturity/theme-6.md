---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-6.html
---

# Theme 6: Automate backups
<a name="theme-6"></a>

**Essential Eight strategy covered**: Regular backups

"Failures are a given and everything will eventually fail over time: from routers to hard disks, from operating systems to memory units corrupting TCP packets, from transient errors to permanent failures. This is a given, whether you are using the highest-quality hardware or lowest cost components." —Werner Vogels, CTO, Amazon, [All Things Distributed](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html)

Data backup and recovery is a critical part of the reliability of a system. AWS is designed to make it easier to create backups, maintain durability of backed-up data, and mak*e *sure that backed-up data remains recoverable.

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully managed service that centralises and automates the backup of data across AWS services. It supports multiple AWS resource types and helps you implement and maintain a backup strategy for workloads that use multiple AWS resources that must be backed up collectively. AWS Backup also helps you to collectively monitor a backup and restore operation of multiple AWS resources.

[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) is an optional feature of a backup vault, and it can provide additional security and control. When a lock is active in Compliance mode and the grace time is over, the vault configuration cannot be altered or deleted by a user, account or data owner, or AWS. Each vault can have one vault lock in place. This provides *write-once, read-many (WORM*) configuration and enforcement of retention periods.

If you follow the current configuration guidance, AWS Backup can provide 99.999999999% annual durability, also known as *11 nines*. It uses the AWS global infrastructure to replicate your backups across multiple Availability Zones. For more information, see [Resilience in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/disaster-recovery-resiliency.html).

AWS Backup helps you automate the recovery and testing of backed-up data to verify backup integrity and processes.

## Related best practices in the AWS Well-Architected Framework
<a name="theme-6-best-practices"></a>
+ [SEC09-BP01 Implement secure key and certificate management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html)
+ [SEC09-BP02 Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html)
+ [SEC09-BP03 Authenticate network communications](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_authentication.html)

## Implementing this theme
<a name="theme-6-implementation"></a>

### Automate data backup and recovery
<a name="automate-data-backup-and-recovery.8f3a9eaf-57dc-5f6f-9898-f3ea51aafc3a"></a>
+ [Implement data backup on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/welcome.html)
+ [Automate data backup at scale](https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/) (AWS blog post)
+ [Automate data recovery validation with AWS Backup](https://aws.amazon.com/blogs/storage/automate-data-recovery-validation-with-aws-backup/) (AWS blog post)

### Implement governance across your AWS Backup outcomes
<a name="implement-governance-across-your-9999999999999999bkp--outcomes.1e9e6878-64cf-5052-a4cf-933fc0a8e30c"></a>
+ [Top 10 security best practices for securing backups in AWS](https://aws.amazon.com/blogs/security/top-10-security-best-practices-for-securing-backups-in-aws/) (AWS blog post)
+ [Use AWS Backup Vault Lock to improve the security of your backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)
+ [Use AWS Backup Audit Manager to audit the compliance of your AWS Backup policies](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html)

## Monitoring this theme
<a name="theme-6-monitoring"></a>

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.accb5d3c-9610-5230-800f-1c30e4c37a21"></a>
+ `RDS_IN_BACKUP_PLAN`
+ `RDS_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `RDS_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `REDSHIFT_BACKUP_ENABLED`
+ `AURORA_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `AURORA_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK`
+ `BACKUP_RECOVERY_POINT_ENCRYPTED`
+ `BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED`
+ `BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK`
+ `DB_INSTANCE_BACKUP_ENABLED`
+ `DYNAMODB_IN_BACKUP_PLAN`
+ `DYNAMODB_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `DYNAMODB_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `EBS_IN_BACKUP_PLAN`
+ `EBS_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `EBS_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `EC2_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `S3_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `S3_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `STORAGEGATEWAY_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
+ `VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED`
+ `VIRTUALMACHINE_RESOURCES_PROTECTED_BY_BACKUP_PLAN`
