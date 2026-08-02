---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupVaultNotificationsDetails.html
---

# AwsBackupBackupVaultNotificationsDetails
<a name="API_AwsBackupBackupVaultNotificationsDetails"></a>

Provides details about the Amazon SNS event notifications for the specified backup vault.

## Contents
<a name="API_AwsBackupBackupVaultNotificationsDetails_Contents"></a>

 ** BackupVaultEvents **   <a name="securityhub-Type-AwsBackupBackupVaultNotificationsDetails-BackupVaultEvents"></a>
An array of events that indicate the status of jobs to back up resources to the backup vault. The following events are supported:
+  `BACKUP_JOB_STARTED | BACKUP_JOB_COMPLETED`
+  `COPY_JOB_STARTED | COPY_JOB_SUCCESSFUL | COPY_JOB_FAILED`
+  `RESTORE_JOB_STARTED | RESTORE_JOB_COMPLETED | RECOVERY_POINT_MODIFIED`
+  `S3_BACKUP_OBJECT_FAILED | S3_RESTORE_OBJECT_FAILED`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SnsTopicArn **   <a name="securityhub-Type-AwsBackupBackupVaultNotificationsDetails-SnsTopicArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the Amazon SNS topic for a backup vault's events.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupBackupVaultNotificationsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupVaultNotificationsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupVaultNotificationsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupVaultNotificationsDetails)
