---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupRecoveryPointDetails.html
---

# AwsBackupRecoveryPointDetails
<a name="API_AwsBackupRecoveryPointDetails"></a>

Contains detailed information about the recovery points stored in an AWS Backup backup vault. A backup, or recovery point, represents the content of a resource at a specified time.

## Contents
<a name="API_AwsBackupRecoveryPointDetails_Contents"></a>

 ** BackupSizeInBytes **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-BackupSizeInBytes"></a>
The size, in bytes, of a backup.
Type: Long
Required: No

 ** BackupVaultArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-BackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupVaultName **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the AWS account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CalculatedLifecycle **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-CalculatedLifecycle"></a>
A `CalculatedLifecycle` object containing `DeleteAt` and `MoveToColdStorageAt` timestamps.
Type: [AwsBackupRecoveryPointCalculatedLifecycleDetails](API_AwsBackupRecoveryPointCalculatedLifecycleDetails.md) object
Required: No

 ** CompletionDate **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-CompletionDate"></a>
The date and time that a job to create a recovery point is completed, in Unix format and UTC. The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedBy **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-CreatedBy"></a>
Contains identifying information about the creation of a recovery point, including the `BackupPlanArn`, `BackupPlanId`, `BackupPlanVersion`, and `BackupRuleId` of the backup plan that is used to create it.
Type: [AwsBackupRecoveryPointCreatedByDetails](API_AwsBackupRecoveryPointCreatedByDetails.md) object
Required: No

 ** CreationDate **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-CreationDate"></a>
The date and time a recovery point is created, in Unix format and UTC. The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionKeyArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-EncryptionKeyArn"></a>
The ARN for the server-side encryption key that is used to protect your backups.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IamRoleArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-IamRoleArn"></a>
Specifies the IAM role ARN used to create the target recovery point
Type: String
Pattern: `.*\S.*`
Required: No

 ** IsEncrypted **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-IsEncrypted"></a>
A Boolean value that is returned as `TRUE` if the specified recovery point is encrypted, or `FALSE` if the recovery point is not encrypted.
Type: Boolean
Required: No

 ** LastRestoreTime **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-LastRestoreTime"></a>
The date and time that a recovery point was last restored, in Unix format and UTC. The value of `LastRestoreTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Lifecycle **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-Lifecycle"></a>
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define
Type: [AwsBackupRecoveryPointLifecycleDetails](API_AwsBackupRecoveryPointLifecycleDetails.md) object
Required: No

 ** RecoveryPointArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-ResourceArn"></a>
An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceType **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-ResourceType"></a>
The type of AWS resource saved as a recovery point, such as an Amazon EBS volume or an Amazon RDS database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceBackupVaultArn **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-SourceBackupVaultArn"></a>
The ARN for the backup vault where the recovery point was originally copied from. If the recovery point is restored to the same account, this value will be null.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-Status"></a>
A status code specifying the state of the recovery point. Valid values are as follows:
+  `COMPLETED`
+  `DELETING`
+  `EXPIRED`
+  `PARTIAL`
Type: String
Pattern: `.*\S.*`
Required: No

 ** StatusMessage **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-StatusMessage"></a>
A message explaining the reason of the recovery point deletion failure.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StorageClass **   <a name="securityhub-Type-AwsBackupRecoveryPointDetails-StorageClass"></a>
Specifies the storage class of the recovery point. Valid values are as follows:
+  `COLD`
+  `DELETED`
+  `WARM`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupRecoveryPointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupRecoveryPointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupRecoveryPointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupRecoveryPointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
