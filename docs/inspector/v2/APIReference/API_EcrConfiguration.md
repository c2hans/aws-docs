---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrConfiguration.html
---

# EcrConfiguration
<a name="API_EcrConfiguration"></a>

Details about the ECR automated re-scan duration setting for your environment.

## Contents
<a name="API_EcrConfiguration_Contents"></a>

 ** rescanDuration **   <a name="inspector2-Type-EcrConfiguration-rescanDuration"></a>
The rescan duration configured for image push date.
Type: String
Valid Values: `LIFETIME | DAYS_30 | DAYS_180 | DAYS_14 | DAYS_60 | DAYS_90 | DAYS_3 | DAYS_7`
Required: Yes

 ** pullDateRescanDuration **   <a name="inspector2-Type-EcrConfiguration-pullDateRescanDuration"></a>
The rescan duration configured for image pull date.
Type: String
Valid Values: `DAYS_14 | DAYS_30 | DAYS_60 | DAYS_90 | DAYS_180 | DAYS_3 | DAYS_7`
Required: No

 ** pullDateRescanMode **   <a name="inspector2-Type-EcrConfiguration-pullDateRescanMode"></a>
The pull date for the re-scan mode.
Type: String
Valid Values: `LAST_PULL_DATE | LAST_IN_USE_AT`
Required: No

## See Also
<a name="API_EcrConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/EcrConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/EcrConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/EcrConfiguration)
