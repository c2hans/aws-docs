---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupPlanRuleCopyActionsDetails.html
---

# AwsBackupBackupPlanRuleCopyActionsDetails
<a name="API_AwsBackupBackupPlanRuleCopyActionsDetails"></a>

An array of `CopyAction` objects, each of which contains details of the copy operation.

## Contents
<a name="API_AwsBackupBackupPlanRuleCopyActionsDetails_Contents"></a>

 ** DestinationBackupVaultArn **   <a name="securityhub-Type-AwsBackupBackupPlanRuleCopyActionsDetails-DestinationBackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Lifecycle **   <a name="securityhub-Type-AwsBackupBackupPlanRuleCopyActionsDetails-Lifecycle"></a>
Defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you don't specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
Type: [AwsBackupBackupPlanLifecycleDetails](API_AwsBackupBackupPlanLifecycleDetails.md) object
Required: No

## See Also
<a name="API_AwsBackupBackupPlanRuleCopyActionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupPlanRuleCopyActionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupPlanRuleCopyActionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupPlanRuleCopyActionsDetails)
