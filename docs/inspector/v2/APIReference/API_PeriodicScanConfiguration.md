---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_PeriodicScanConfiguration.html
---

# PeriodicScanConfiguration
<a name="API_PeriodicScanConfiguration"></a>

Configuration settings for periodic scans that run on a scheduled basis.

## Contents
<a name="API_PeriodicScanConfiguration_Contents"></a>

 ** frequency **   <a name="inspector2-Type-PeriodicScanConfiguration-frequency"></a>
The frequency at which periodic scans are performed (such as weekly or monthly).
If you don't provide the `frequencyExpression` Amazon Inspector chooses day for the scan to run. If you provide the `frequencyExpression`, the schedule must match the specified `frequency`.
Type: String
Valid Values: `WEEKLY | MONTHLY | NEVER`
Required: No

 ** frequencyExpression **   <a name="inspector2-Type-PeriodicScanConfiguration-frequencyExpression"></a>
The schedule expression for periodic scans, in cron format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_PeriodicScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/PeriodicScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/PeriodicScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/PeriodicScanConfiguration)
