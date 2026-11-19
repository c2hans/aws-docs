---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiConfigurationState.html
---

# AmiConfigurationState

The current state of the Amazon Machine Image (AMI) scan configuration for an account.

## Contents
<a name="API_AmiConfigurationState_Contents"></a>

 ** createdWithin **   <a name="inspector2-Type-AmiConfigurationState-createdWithin"></a>
Restricts scanning to AMIs that were created within the specified duration.
Type: String
Valid Values: `DAYS_180 | DAYS_90 | DAYS_60 | DAYS_30 | DAYS_14 | DAYS_7`
Required: No

 ** lastLaunchedWithin **   <a name="inspector2-Type-AmiConfigurationState-lastLaunchedWithin"></a>
Restricts scanning to AMIs that were last launched within the specified duration.
Type: String
Valid Values: `DAYS_180 | DAYS_90 | DAYS_60 | DAYS_30 | DAYS_14 | DAYS_7`
Required: No

 ** scanModeConfiguration **   <a name="inspector2-Type-AmiConfigurationState-scanModeConfiguration"></a>
The scan mode configuration that determines which AMIs are scanned.
Type: [AmiScanModeConfiguration](API_AmiScanModeConfiguration.md) object
Required: No

 ** status **   <a name="inspector2-Type-AmiConfigurationState-status"></a>
The status of the AMI scan configuration.
Type: String
Valid Values: `SUCCESS | PENDING | FAILED`
Required: No

 ** updatedAt **   <a name="inspector2-Type-AmiConfigurationState-updatedAt"></a>
The date and time when the AMI scan configuration was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_AmiConfigurationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiConfigurationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiConfigurationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiConfigurationState)
