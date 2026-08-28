---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupPlanAdvancedBackupSettingsDetails.html
---

# AwsBackupBackupPlanAdvancedBackupSettingsDetails
<a name="API_AwsBackupBackupPlanAdvancedBackupSettingsDetails"></a>

Provides a list of backup options for each resource type.

## Contents
<a name="API_AwsBackupBackupPlanAdvancedBackupSettingsDetails_Contents"></a>

 ** BackupOptions **   <a name="securityhub-Type-AwsBackupBackupPlanAdvancedBackupSettingsDetails-BackupOptions"></a>
Specifies the backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs. Valid values are as follows:
+ Set to `WindowsVSS: enabled` to enable the WindowsVSS backup option and create a Windows VSS backup.
+ Set to `WindowsVSS: disabled` to create a regular backup. The `WindowsVSS` option is not enabled by default.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** ResourceType **   <a name="securityhub-Type-AwsBackupBackupPlanAdvancedBackupSettingsDetails-ResourceType"></a>
The name of a resource type. The only supported resource type is Amazon EC2 instances with Windows VSS.
The only valid value is `EC2`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupBackupPlanAdvancedBackupSettingsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupPlanAdvancedBackupSettingsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupPlanAdvancedBackupSettingsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupPlanAdvancedBackupSettingsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
