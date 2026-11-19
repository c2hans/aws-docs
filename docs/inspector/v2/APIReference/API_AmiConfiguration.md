---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiConfiguration.html
---

# AmiConfiguration

The configuration that controls how Amazon Machine Images (AMIs) are scanned for an account.

## Contents
<a name="API_AmiConfiguration_Contents"></a>

 ** scanModeConfiguration **   <a name="inspector2-Type-AmiConfiguration-scanModeConfiguration"></a>
The scan mode configuration that determines which AMIs are scanned.
Type: [AmiScanModeConfiguration](API_AmiScanModeConfiguration.md) object
Required: Yes

 ** createdWithin **   <a name="inspector2-Type-AmiConfiguration-createdWithin"></a>
Restricts scanning to AMIs that were created within the specified duration.
Type: String
Valid Values: `DAYS_180 | DAYS_90 | DAYS_60 | DAYS_30 | DAYS_14 | DAYS_7`
Required: No

 ** lastLaunchedWithin **   <a name="inspector2-Type-AmiConfiguration-lastLaunchedWithin"></a>
Restricts scanning to AMIs that were last launched within the specified duration.
Type: String
Valid Values: `DAYS_180 | DAYS_90 | DAYS_60 | DAYS_30 | DAYS_14 | DAYS_7`
Required: No

## See Also
<a name="API_AmiConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiConfiguration)
