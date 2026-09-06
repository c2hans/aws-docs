---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ContinuousIntegrationScanConfiguration.html
---

# ContinuousIntegrationScanConfiguration
<a name="API_ContinuousIntegrationScanConfiguration"></a>

Configuration settings for continuous integration scans that run automatically when code changes are made.

## Contents
<a name="API_ContinuousIntegrationScanConfiguration_Contents"></a>

 ** supportedEvents **   <a name="inspector2-Type-ContinuousIntegrationScanConfiguration-supportedEvents"></a>
The repository events that trigger continuous integration scans, such as pull requests or commits.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `PULL_REQUEST | PUSH`
Required: Yes

## See Also
<a name="API_ContinuousIntegrationScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ContinuousIntegrationScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ContinuousIntegrationScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ContinuousIntegrationScanConfiguration)
