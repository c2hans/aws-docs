---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupPlanDetails.html
---

# AwsBackupBackupPlanDetails
<a name="API_AwsBackupBackupPlanDetails"></a>

Provides details about an AWS Backup backup plan and an array of `BackupRule` objects, each of which specifies a backup rule.

## Contents
<a name="API_AwsBackupBackupPlanDetails_Contents"></a>

 ** BackupPlan **   <a name="securityhub-Type-AwsBackupBackupPlanDetails-BackupPlan"></a>
Uniquely identifies the backup plan to be associated with the selection of resources.
Type: [AwsBackupBackupPlanBackupPlanDetails](API_AwsBackupBackupPlanBackupPlanDetails.md) object
Required: No

 ** BackupPlanArn **   <a name="securityhub-Type-AwsBackupBackupPlanDetails-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the backup plan.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupPlanId **   <a name="securityhub-Type-AwsBackupBackupPlanDetails-BackupPlanId"></a>
A unique ID for the backup plan.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VersionId **   <a name="securityhub-Type-AwsBackupBackupPlanDetails-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings. Version IDs cannot be edited.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupBackupPlanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupPlanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupPlanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupPlanDetails)
