---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanConfiguration.html
---

# ScanConfiguration
<a name="API_ScanConfiguration"></a>

Contains information about the configuration used for the malware scan.

## Contents
<a name="API_ScanConfiguration_Contents"></a>

 ** incrementalScanDetails **   <a name="guardduty-Type-ScanConfiguration-incrementalScanDetails"></a>
Information about the incremental scan configuration, if applicable.
Type: [IncrementalScanDetails](API_IncrementalScanDetails.md) object
Required: No

 ** recoveryPoint **   <a name="guardduty-Type-ScanConfiguration-recoveryPoint"></a>
Information about the recovery point configuration used for the scan, if applicable.
Type: [ScanConfigurationRecoveryPoint](API_ScanConfigurationRecoveryPoint.md) object
Required: No

 ** role **   <a name="guardduty-Type-ScanConfiguration-role"></a>
Amazon Resource Name (ARN) of the IAM role that should contain the required permissions for the scan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** triggerDetails **   <a name="guardduty-Type-ScanConfiguration-triggerDetails"></a>
Information about the entity that triggered the malware scan.
Type: [TriggerDetails](API_TriggerDetails.md) object
Required: No

## See Also
<a name="API_ScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanConfiguration)
