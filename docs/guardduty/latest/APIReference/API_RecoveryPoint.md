---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RecoveryPoint.html
---

# RecoveryPoint
<a name="API_RecoveryPoint"></a>

Contains information about the recovery point configuration for scanning backup data from AWS Backup.

## Contents
<a name="API_RecoveryPoint_Contents"></a>

 ** backupVaultName **   <a name="guardduty-Type-RecoveryPoint-backupVaultName"></a>
The name of the AWS Backup vault that contains the name of the recovery point to be scanned.
Type: String
Required: Yes

 ** continuousScanDetails **   <a name="guardduty-Type-RecoveryPoint-continuousScanDetails"></a>
Contains information about the time range within the continuous backup in AWS Backup to scan.
Type: [ContinuousScanDetails](API_ContinuousScanDetails.md) object
Required: No

## See Also
<a name="API_RecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RecoveryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RecoveryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RecoveryPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
