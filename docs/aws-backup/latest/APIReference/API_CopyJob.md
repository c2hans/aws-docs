---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CopyJob.html
---

# CopyJob
<a name="API_CopyJob"></a>

Contains detailed information about a copy job.

## Contents
<a name="API_CopyJob_Contents"></a>

 ** AccountId **   <a name="Backup-Type-CopyJob-AccountId"></a>
The account ID that owns the copy job.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** BackupSizeInBytes **   <a name="Backup-Type-CopyJob-BackupSizeInBytes"></a>
The size, in bytes, of a copy job.
Type: Long
Required: No

 ** ChildJobsInState **   <a name="Backup-Type-CopyJob-ChildJobsInState"></a>
This returns the statistics of the included child (nested) copy jobs.
Type: String to long map
Valid Keys: `CREATED | RUNNING | COMPLETED | FAILED | PARTIAL`
Required: No

 ** CompletionDate **   <a name="Backup-Type-CopyJob-CompletionDate"></a>
The date and time a copy job is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CompositeMemberIdentifier **   <a name="Backup-Type-CopyJob-CompositeMemberIdentifier"></a>
The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the [ logical ID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax) within a stack.
Type: String
Required: No

 ** CopyJobId **   <a name="Backup-Type-CopyJob-CopyJobId"></a>
Uniquely identifies a copy job.
Type: String
Required: No

 ** CreatedBy **   <a name="Backup-Type-CopyJob-CreatedBy"></a>
Contains information about the backup plan and rule that AWS Backup used to initiate the recovery point backup.
Type: [RecoveryPointCreator](API_RecoveryPointCreator.md) object
Required: No

 ** CreatedByBackupJobId **   <a name="Backup-Type-CopyJob-CreatedByBackupJobId"></a>
The backup job ID that initiated this copy job. Only applicable to scheduled copy jobs and automatic copy jobs to logically air-gapped vault.
Type: String
Required: No

 ** CreationDate **   <a name="Backup-Type-CopyJob-CreationDate"></a>
The date and time a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** DestinationBackupVaultArn **   <a name="Backup-Type-CopyJob-DestinationBackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: No

 ** DestinationEncryptionKeyArn **   <a name="Backup-Type-CopyJob-DestinationEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the copied backup in the destination vault. This can be a customer-managed key or an AWS managed key.
Type: String
Required: No

 ** DestinationRecoveryPointArn **   <a name="Backup-Type-CopyJob-DestinationRecoveryPointArn"></a>
An ARN that uniquely identifies a destination recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: No

 ** DestinationRecoveryPointLifecycle **   <a name="Backup-Type-CopyJob-DestinationRecoveryPointLifecycle"></a>
Specifies the time period, in days, before a recovery point transitions to cold storage or is deleted.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the retention setting must be 90 days greater than the transition to cold after days setting. The transition to cold after days setting can't be changed after a backup has been transitioned to cold.
Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. AWS Backup ignores this expression for other resource types.
To remove the existing lifecycle and retention periods and keep your recovery points indefinitely, specify -1 for `MoveToColdStorageAfterDays` and `DeleteAfterDays`.
Type: [Lifecycle](API_Lifecycle.md) object
Required: No

 ** DestinationVaultLockState **   <a name="Backup-Type-CopyJob-DestinationVaultLockState"></a>
The lock state of the destination backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include `LOCKED` and `UNLOCKED`.
Type: String
Required: No

 ** DestinationVaultType **   <a name="Backup-Type-CopyJob-DestinationVaultType"></a>
The type of destination backup vault where the copied recovery point is stored. Valid values are `BACKUP_VAULT` for standard backup vaults and `LOGICALLY_AIR_GAPPED_BACKUP_VAULT` for logically air-gapped vaults.
Type: String
Required: No

 ** IamRoleArn **   <a name="Backup-Type-CopyJob-IamRoleArn"></a>
Specifies the IAM role ARN used to copy the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: No

 ** IsParent **   <a name="Backup-Type-CopyJob-IsParent"></a>
This is a boolean value indicating this is a parent (composite) copy job.
Type: Boolean
Required: No

 ** MessageCategory **   <a name="Backup-Type-CopyJob-MessageCategory"></a>
This parameter is the job count for the specified message category.
Example strings may include `AccessDenied`, `SUCCESS`, `AGGREGATE_ALL`, and `InvalidParameters`. See [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of MessageCategory strings.
The the value ANY returns count of all message categories.
 `AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum
Type: String
Required: No

 ** NumberOfChildJobs **   <a name="Backup-Type-CopyJob-NumberOfChildJobs"></a>
The number of child (nested) copy jobs.
Type: Long
Required: No

 ** ParentJobId **   <a name="Backup-Type-CopyJob-ParentJobId"></a>
This uniquely identifies a request to AWS Backup to copy a resource. The return will be the parent (composite) job ID.
Type: String
Required: No

 ** ResourceArn **   <a name="Backup-Type-CopyJob-ResourceArn"></a>
The AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
Type: String
Required: No

 ** ResourceName **   <a name="Backup-Type-CopyJob-ResourceName"></a>
The non-unique name of the resource that belongs to the specified backup.
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-CopyJob-ResourceType"></a>
The type of AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** SourceBackupVaultArn **   <a name="Backup-Type-CopyJob-SourceBackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: No

 ** SourceRecoveryPointArn **   <a name="Backup-Type-CopyJob-SourceRecoveryPointArn"></a>
An ARN that uniquely identifies a source recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: No

 ** State **   <a name="Backup-Type-CopyJob-State"></a>
The current state of a copy job.
Type: String
Valid Values: `CREATED | RUNNING | COMPLETED | FAILED | PARTIAL`
Required: No

 ** StatusMessage **   <a name="Backup-Type-CopyJob-StatusMessage"></a>
A detailed message explaining the status of the job to copy a resource.
Type: String
Required: No

## See Also
<a name="API_CopyJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CopyJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CopyJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CopyJob)
