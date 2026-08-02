---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupRecoveryPointCreatedByDetails.html
---

# AwsBackupRecoveryPointCreatedByDetails
<a name="API_AwsBackupRecoveryPointCreatedByDetails"></a>

Contains information about the backup plan and rule that AWS Backup used to initiate the recovery point backup.

## Contents
<a name="API_AwsBackupRecoveryPointCreatedByDetails_Contents"></a>

 ** BackupPlanArn **   <a name="securityhub-Type-AwsBackupRecoveryPointCreatedByDetails-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupPlanId **   <a name="securityhub-Type-AwsBackupRecoveryPointCreatedByDetails-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupPlanVersion **   <a name="securityhub-Type-AwsBackupRecoveryPointCreatedByDetails-BackupPlanVersion"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupRuleId **   <a name="securityhub-Type-AwsBackupRecoveryPointCreatedByDetails-BackupRuleId"></a>
Uniquely identifies a rule used to schedule the backup of a selection of resources.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupRecoveryPointCreatedByDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupRecoveryPointCreatedByDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupRecoveryPointCreatedByDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupRecoveryPointCreatedByDetails)
