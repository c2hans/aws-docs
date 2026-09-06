---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RecoveryPointByResource.html
---

# RecoveryPointByResource
<a name="API_RecoveryPointByResource"></a>

Contains detailed information about a saved recovery point.

## Contents
<a name="API_RecoveryPointByResource_Contents"></a>

 ** AggregatedScanResult **   <a name="Backup-Type-RecoveryPointByResource-AggregatedScanResult"></a>
Contains the latest scanning results against the recovery point and currently include `FailedScan`, `Findings`, `LastComputed`.
Type: [AggregatedScanResult](API_AggregatedScanResult.md) object
Required: No

 ** BackupSizeBytes **   <a name="Backup-Type-RecoveryPointByResource-BackupSizeBytes"></a>
The size, in bytes, of a backup.
Type: Long
Required: No

 ** BackupVaultName **   <a name="Backup-Type-RecoveryPointByResource-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: No

 ** CreationDate **   <a name="Backup-Type-RecoveryPointByResource-CreationDate"></a>
The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** EncryptionKeyArn **   <a name="Backup-Type-RecoveryPointByResource-EncryptionKeyArn"></a>
The server-side encryption key that is used to protect your backups; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
Type: String
Required: No

 ** EncryptionKeyType **   <a name="Backup-Type-RecoveryPointByResource-EncryptionKeyType"></a>
The type of encryption key used for the recovery point. Valid values are CUSTOMER\_MANAGED\_KMS\_KEY for customer-managed keys or AWS\_OWNED\_KMS\_KEY for AWS-owned keys.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: No

 ** IndexStatus **   <a name="Backup-Type-RecoveryPointByResource-IndexStatus"></a>
This is the current status for the backup index associated with the specified recovery point.
Statuses are: `PENDING` \| `ACTIVE` \| `FAILED` \| `DELETING`
A recovery point with an index that has the status of `ACTIVE` can be included in a search.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING`
Required: No

 ** IndexStatusMessage **   <a name="Backup-Type-RecoveryPointByResource-IndexStatusMessage"></a>
A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.
Type: String
Required: No

 ** IsParent **   <a name="Backup-Type-RecoveryPointByResource-IsParent"></a>
This is a boolean value indicating this is a parent (composite) recovery point.
Type: Boolean
Required: No

 ** ParentRecoveryPointArn **   <a name="Backup-Type-RecoveryPointByResource-ParentRecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the parent (composite) recovery point.
Type: String
Required: No

 ** RecoveryPointArn **   <a name="Backup-Type-RecoveryPointByResource-RecoveryPointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: No

 ** ResourceName **   <a name="Backup-Type-RecoveryPointByResource-ResourceName"></a>
The non-unique name of the resource that belongs to the specified backup.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-RecoveryPointByResource-Status"></a>
A status code specifying the state of the recovery point.
Type: String
Valid Values: `COMPLETED | PARTIAL | DELETING | EXPIRED | AVAILABLE | STOPPED | CREATING`
Required: No

 ** StatusMessage **   <a name="Backup-Type-RecoveryPointByResource-StatusMessage"></a>
A message explaining the current status of the recovery point.
Type: String
Required: No

 ** VaultType **   <a name="Backup-Type-RecoveryPointByResource-VaultType"></a>
The type of vault in which the described recovery point is stored.
Type: String
Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`
Required: No

## See Also
<a name="API_RecoveryPointByResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RecoveryPointByResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointByResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointByResource)
