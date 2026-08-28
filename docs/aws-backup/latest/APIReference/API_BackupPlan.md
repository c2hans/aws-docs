---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupPlan.html
---

# BackupPlan
<a name="API_BackupPlan"></a>

Contains an optional backup plan display name and an array of `BackupRule` objects, each of which specifies a backup rule. Each rule in a backup plan is a separate scheduled task and can back up a different selection of AWS resources.

## Contents
<a name="API_BackupPlan_Contents"></a>

 ** BackupPlanName **   <a name="Backup-Type-BackupPlan-BackupPlanName"></a>
The display name of a backup plan. Must contain only alphanumeric or '-\_.' special characters.
If this is set in the console, it can contain 1 to 50 characters; if this is set through CLI or API, it can contain 1 to 200 characters.
Type: String
Required: Yes

 ** Rules **   <a name="Backup-Type-BackupPlan-Rules"></a>
An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
Type: Array of [BackupRule](API_BackupRule.md) objects
Required: Yes

 ** AdvancedBackupSettings **   <a name="Backup-Type-BackupPlan-AdvancedBackupSettings"></a>
Contains a list of `BackupOptions` for each resource type.
Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md) objects
Required: No

 ** ScanSettings **   <a name="Backup-Type-BackupPlan-ScanSettings"></a>
Contains your scanning configuration for the backup plan and includes the Malware scanner, your selected resources, and scanner role.
Type: Array of [ScanSetting](API_ScanSetting.md) objects
Required: No

## See Also
<a name="API_BackupPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
