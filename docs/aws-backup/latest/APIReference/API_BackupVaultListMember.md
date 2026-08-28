---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupVaultListMember.html
---

# BackupVaultListMember
<a name="API_BackupVaultListMember"></a>

Contains metadata about a backup vault.

## Contents
<a name="API_BackupVaultListMember_Contents"></a>

 ** BackupVaultArn **   <a name="Backup-Type-BackupVaultListMember-BackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: No

 ** BackupVaultName **   <a name="Backup-Type-BackupVaultListMember-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: No

 ** CreationDate **   <a name="Backup-Type-BackupVaultListMember-CreationDate"></a>
The date and time a resource backup is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CreatorRequestId **   <a name="Backup-Type-BackupVaultListMember-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.
If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

 ** EncryptionKeyArn **   <a name="Backup-Type-BackupVaultListMember-EncryptionKeyArn"></a>
A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default.
To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup, see [ Encryption for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
Type: String
Required: No

 ** EncryptionKeyType **   <a name="Backup-Type-BackupVaultListMember-EncryptionKeyType"></a>
The type of encryption key used for the backup vault. Valid values are CUSTOMER\_MANAGED\_KMS\_KEY for customer-managed keys or AWS\_OWNED\_KMS\_KEY for AWS-owned keys.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: No

 ** LockDate **   <a name="Backup-Type-BackupVaultListMember-LockDate"></a>
The date and time when AWS Backup Vault Lock configuration becomes immutable, meaning it cannot be changed or deleted.
If you applied Vault Lock to your vault without specifying a lock date, you can change your Vault Lock settings, or delete Vault Lock from the vault entirely, at any time.
This value is in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** Locked **   <a name="Backup-Type-BackupVaultListMember-Locked"></a>
A Boolean value that indicates whether AWS Backup Vault Lock applies to the selected backup vault. If `true`, Vault Lock prevents delete and update operations on the recovery points in the selected vault.
Type: Boolean
Required: No

 ** MaxRetentionDays **   <a name="Backup-Type-BackupVaultListMember-MaxRetentionDays"></a>
The AWS Backup Vault Lock setting that specifies the maximum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock does not enforce a maximum retention period on the recovery points in the vault (allowing indefinite storage).
If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.
Type: Long
Required: No

 ** MinRetentionDays **   <a name="Backup-Type-BackupVaultListMember-MinRetentionDays"></a>
The AWS Backup Vault Lock setting that specifies the minimum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock does not enforce a minimum retention period.
If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.
Type: Long
Required: No

 ** NumberOfRecoveryPoints **   <a name="Backup-Type-BackupVaultListMember-NumberOfRecoveryPoints"></a>
The number of recovery points that are stored in a backup vault. Recovery point count value displayed in the console can be an approximation.
Type: Long
Required: No

 ** VaultState **   <a name="Backup-Type-BackupVaultListMember-VaultState"></a>
The current state of the vault.
Type: String
Valid Values: `CREATING | AVAILABLE | FAILED`
Required: No

 ** VaultType **   <a name="Backup-Type-BackupVaultListMember-VaultType"></a>
The type of vault in which the described recovery point is stored.
Type: String
Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`
Required: No

## See Also
<a name="API_BackupVaultListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupVaultListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupVaultListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupVaultListMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
