---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RecoveryPointDetails.html
---

# RecoveryPointDetails
<a name="API_RecoveryPointDetails"></a>

Contains details about the backup recovery point.

## Contents
<a name="API_RecoveryPointDetails_Contents"></a>

 ** backupVaultName **   <a name="guardduty-Type-RecoveryPointDetails-backupVaultName"></a>
The name of the backup vault containing the recovery point.
Type: String
Required: No

 ** continuousScanDetails **   <a name="guardduty-Type-RecoveryPointDetails-continuousScanDetails"></a>
Contains information about the time range within the continuous backup in AWS Backup that was scanned for a point-in-time recovery resource.
Type: [ScanConfigurationContinuousScanDetails](API_ScanConfigurationContinuousScanDetails.md) object
Required: No

 ** recoveryPointArn **   <a name="guardduty-Type-RecoveryPointDetails-recoveryPointArn"></a>
The Amazon Resource Name (ARN) of the recovery point.
Type: String
Required: No

## See Also
<a name="API_RecoveryPointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RecoveryPointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RecoveryPointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RecoveryPointDetails)
