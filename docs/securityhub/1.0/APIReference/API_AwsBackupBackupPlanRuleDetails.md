---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupBackupPlanRuleDetails.html
---

# AwsBackupBackupPlanRuleDetails
<a name="API_AwsBackupBackupPlanRuleDetails"></a>

Provides details about an array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.

## Contents
<a name="API_AwsBackupBackupPlanRuleDetails_Contents"></a>

 ** CompletionWindowMinutes **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-CompletionWindowMinutes"></a>
A value in minutes after a backup job is successfully started before it must be completed, or it is canceled by AWS Backup.
Type: Long
Required: No

 ** CopyActions **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-CopyActions"></a>
An array of `CopyAction` objects, each of which contains details of the copy operation.
Type: Array of [AwsBackupBackupPlanRuleCopyActionsDetails](API_AwsBackupBackupPlanRuleCopyActionsDetails.md) objects
Required: No

 ** EnableContinuousBackup **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-EnableContinuousBackup"></a>
Specifies whether AWS Backup creates continuous backups capable of point-in-time restore (PITR).
Type: Boolean
Required: No

 ** Lifecycle **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-Lifecycle"></a>
Defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you don't specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
Type: [AwsBackupBackupPlanLifecycleDetails](API_AwsBackupBackupPlanLifecycleDetails.md) object
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-RuleId"></a>
Uniquely identifies a rule that is used to schedule the backup of a selection of resources.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleName **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-RuleName"></a>
A display name for a backup rule. Must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ScheduleExpression **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-ScheduleExpression"></a>
A cron expression in UTC specifying when AWS Backup initiates a backup job.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StartWindowMinutes **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-StartWindowMinutes"></a>
A value in minutes after a backup is scheduled before a job will be canceled if it doesn't start successfully.
Type: Long
Required: No

 ** TargetBackupVault **   <a name="securityhub-Type-AwsBackupBackupPlanRuleDetails-TargetBackupVault"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the AWS account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupBackupPlanRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupBackupPlanRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupBackupPlanRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupBackupPlanRuleDetails)
