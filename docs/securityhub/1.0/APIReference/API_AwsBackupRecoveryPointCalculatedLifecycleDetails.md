---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsBackupRecoveryPointCalculatedLifecycleDetails.html
---

# AwsBackupRecoveryPointCalculatedLifecycleDetails
<a name="API_AwsBackupRecoveryPointCalculatedLifecycleDetails"></a>

Specifies how long in days before a recovery point transitions to cold storage or is deleted.

## Contents
<a name="API_AwsBackupRecoveryPointCalculatedLifecycleDetails_Contents"></a>

 ** DeleteAt **   <a name="securityhub-Type-AwsBackupRecoveryPointCalculatedLifecycleDetails-DeleteAt"></a>
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus `MoveToColdStorageAfterDays`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MoveToColdStorageAt **   <a name="securityhub-Type-AwsBackupRecoveryPointCalculatedLifecycleDetails-MoveToColdStorageAt"></a>
Specifies the number of days after creation that a recovery point is moved to cold storage.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsBackupRecoveryPointCalculatedLifecycleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsBackupRecoveryPointCalculatedLifecycleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsBackupRecoveryPointCalculatedLifecycleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsBackupRecoveryPointCalculatedLifecycleDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
