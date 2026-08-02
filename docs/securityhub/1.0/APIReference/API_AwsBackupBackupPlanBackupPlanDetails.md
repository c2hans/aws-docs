---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupPlanBackupPlanDetails.html
---

# AwsBackupBackupPlanBackupPlanDetails
<a name="API_AwsBackupBackupPlanBackupPlanDetails"></a>

Provides details about an AWS Backup backup plan and an array of `BackupRule` objects, each of which specifies a backup rule.

## Contents
<a name="API_AwsBackupBackupPlanBackupPlanDetails_Contents"></a>

 ** AdvancedBackupSettings **   <a name="securityhub-Type-AwsBackupBackupPlanBackupPlanDetails-AdvancedBackupSettings"></a>
A list of backup options for each resource type.
Type: Array of [AwsBackupBackupPlanAdvancedBackupSettingsDetails](API_AwsBackupBackupPlanAdvancedBackupSettingsDetails.md) objects
Required: No

 ** BackupPlanName **   <a name="securityhub-Type-AwsBackupBackupPlanBackupPlanDetails-BackupPlanName"></a>
The display name of a backup plan.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupPlanRule **   <a name="securityhub-Type-AwsBackupBackupPlanBackupPlanDetails-BackupPlanRule"></a>
An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
Type: Array of [AwsBackupBackupPlanRuleDetails](API_AwsBackupBackupPlanRuleDetails.md) objects
Required: No

## See Also
<a name="API_AwsBackupBackupPlanBackupPlanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupPlanBackupPlanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupPlanBackupPlanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupPlanBackupPlanDetails)
