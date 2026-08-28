---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RecoveryPointByBackupVault.html
---

# RecoveryPointByBackupVault
<a name="API_RecoveryPointByBackupVault"></a>

Contains detailed information about the recovery points stored in a backup vault.

## Contents
<a name="API_RecoveryPointByBackupVault_Contents"></a>

 ** AggregatedScanResult **   <a name="Backup-Type-RecoveryPointByBackupVault-AggregatedScanResult"></a>
Contains the latest scanning results against the recovery point and currently include `FailedScan`, `Findings`, `LastComputed`.
Type: [AggregatedScanResult](API_AggregatedScanResult.md) object
Required: No

 ** BackupSizeInBytes **   <a name="Backup-Type-RecoveryPointByBackupVault-BackupSizeInBytes"></a>
The size, in bytes, of a backup.
Type: Long
Required: No

 ** BackupVaultArn **   <a name="Backup-Type-RecoveryPointByBackupVault-BackupVaultArn"></a>
An ARN that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: No

 ** BackupVaultName **   <a name="Backup-Type-RecoveryPointByBackupVault-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: No

 ** CalculatedLifecycle **   <a name="Backup-Type-RecoveryPointByBackupVault-CalculatedLifecycle"></a>
A `CalculatedLifecycle` object containing `DeleteAt` and `MoveToColdStorageAt` timestamps.
Type: [CalculatedLifecycle](API_CalculatedLifecycle.md) object
Required: No

 ** CompletionDate **   <a name="Backup-Type-RecoveryPointByBackupVault-CompletionDate"></a>
The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CompositeMemberIdentifier **   <a name="Backup-Type-RecoveryPointByBackupVault-CompositeMemberIdentifier"></a>
The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the [ logical ID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax) within a stack.
Type: String
Required: No

 ** CreatedBy **   <a name="Backup-Type-RecoveryPointByBackupVault-CreatedBy"></a>
Contains identifying information about the creation of a recovery point, including the `BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`, and `BackupRuleId` of the backup plan that is used to create it.
Type: [RecoveryPointCreator](API_RecoveryPointCreator.md) object
Required: No

 ** CreationDate **   <a name="Backup-Type-RecoveryPointByBackupVault-CreationDate"></a>
The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** EncryptionKeyArn **   <a name="Backup-Type-RecoveryPointByBackupVault-EncryptionKeyArn"></a>
The server-side encryption key that is used to protect your backups; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
Type: String
Required: No

 ** EncryptionKeyType **   <a name="Backup-Type-RecoveryPointByBackupVault-EncryptionKeyType"></a>
The type of encryption key used for the recovery point. Valid values are CUSTOMER\_MANAGED\_KMS\_KEY for customer-managed keys or AWS\_OWNED\_KMS\_KEY for AWS-owned keys.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: No

 ** IamRoleArn **   <a name="Backup-Type-RecoveryPointByBackupVault-IamRoleArn"></a>
Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: No

 ** IndexStatus **   <a name="Backup-Type-RecoveryPointByBackupVault-IndexStatus"></a>
This is the current status for the backup index associated with the specified recovery point.
Statuses are: `PENDING` \| `ACTIVE` \| `FAILED` \| `DELETING`
A recovery point with an index that has the status of `ACTIVE` can be included in a search.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING`
Required: No

 ** IndexStatusMessage **   <a name="Backup-Type-RecoveryPointByBackupVault-IndexStatusMessage"></a>
A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.
Type: String
Required: No

 ** InitiationDate **   <a name="Backup-Type-RecoveryPointByBackupVault-InitiationDate"></a>
The date and time when the backup job that created this recovery point was initiated, in Unix format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** IsEncrypted **   <a name="Backup-Type-RecoveryPointByBackupVault-IsEncrypted"></a>
A Boolean value that is returned as `TRUE` if the specified recovery point is encrypted, or `FALSE` if the recovery point is not encrypted.
Type: Boolean
Required: No

 ** IsParent **   <a name="Backup-Type-RecoveryPointByBackupVault-IsParent"></a>
This is a boolean value indicating this is a parent (composite) recovery point.
Type: Boolean
Required: No

 ** LastRestoreTime **   <a name="Backup-Type-RecoveryPointByBackupVault-LastRestoreTime"></a>
The date and time a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of `LastRestoreTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** Lifecycle **   <a name="Backup-Type-RecoveryPointByBackupVault-Lifecycle"></a>
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.
Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. AWS Backup ignores this expression for other resource types.
Type: [Lifecycle](API_Lifecycle.md) object
Required: No

 ** ParentRecoveryPointArn **   <a name="Backup-Type-RecoveryPointByBackupVault-ParentRecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the parent (composite) recovery point.
Type: String
Required: No

 ** RecoveryPointArn **   <a name="Backup-Type-RecoveryPointByBackupVault-RecoveryPointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: No

 ** ResourceArn **   <a name="Backup-Type-RecoveryPointByBackupVault-ResourceArn"></a>
An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String
Required: No

 ** ResourceName **   <a name="Backup-Type-RecoveryPointByBackupVault-ResourceName"></a>
The non-unique name of the resource that belongs to the specified backup.
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-RecoveryPointByBackupVault-ResourceType"></a>
The type of AWS resource saved as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only supported resource type is Amazon EC2.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** SourceBackupVaultArn **   <a name="Backup-Type-RecoveryPointByBackupVault-SourceBackupVaultArn"></a>
The backup vault where the recovery point was originally copied from. If the recovery point is restored to the same account this value will be `null`.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-RecoveryPointByBackupVault-Status"></a>
A status code specifying the state of the recovery point.
Type: String
Valid Values: `COMPLETED | PARTIAL | DELETING | EXPIRED | AVAILABLE | STOPPED | CREATING`
Required: No

 ** StatusMessage **   <a name="Backup-Type-RecoveryPointByBackupVault-StatusMessage"></a>
A message explaining the current status of the recovery point.
Type: String
Required: No

 ** VaultType **   <a name="Backup-Type-RecoveryPointByBackupVault-VaultType"></a>
The type of vault in which the described recovery point is stored.
Type: String
Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`
Required: No

## See Also
<a name="API_RecoveryPointByBackupVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RecoveryPointByBackupVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByBackupVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByBackupVault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
