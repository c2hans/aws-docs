---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupPlanInput.html
---

# BackupPlanInput
<a name="API_BackupPlanInput"></a>

Contains an optional backup plan display name and an array of `BackupRule` objects, each of which specifies a backup rule. Each rule in a backup plan is a separate scheduled task.

## Contents
<a name="API_BackupPlanInput_Contents"></a>

 ** BackupPlanName **   <a name="Backup-Type-BackupPlanInput-BackupPlanName"></a>
The display name of a backup plan. Must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: Yes

 ** Rules **   <a name="Backup-Type-BackupPlanInput-Rules"></a>
An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
Type: Array of [BackupRuleInput](API_BackupRuleInput.md) objects
Required: Yes

 ** AdvancedBackupSettings **   <a name="Backup-Type-BackupPlanInput-AdvancedBackupSettings"></a>
Specifies a list of `BackupOptions` for each resource type. These settings are only available for Windows Volume Shadow Copy Service (VSS) backup jobs.
Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md) objects
Required: No

 ** ScanSettings **   <a name="Backup-Type-BackupPlanInput-ScanSettings"></a>
Contains your scanning configuration for the backup rule and includes the malware scanner, and scan mode of either full or incremental.
Type: Array of [ScanSetting](API_ScanSetting.md) objects
Required: No

## See Also
<a name="API_BackupPlanInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupPlanInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupPlanInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupPlanInput)
