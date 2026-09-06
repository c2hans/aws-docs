---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationRecorderSummary.html
---

# ConfigurationRecorderSummary
<a name="API_ConfigurationRecorderSummary"></a>

A summary of a configuration recorder, including the `arn`, `name`, `servicePrincipal`, `recordingScope`, and `provider`.

## Contents
<a name="API_ConfigurationRecorderSummary_Contents"></a>

 ** arn **   <a name="config-Type-ConfigurationRecorderSummary-arn"></a>
The Amazon Resource Name (ARN) of the configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** name **   <a name="config-Type-ConfigurationRecorderSummary-name"></a>
The name of the configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** recordingScope **   <a name="config-Type-ConfigurationRecorderSummary-recordingScope"></a>
Indicates whether the [ConfigurationItems](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in scope for the configuration recorder are recorded for free (`INTERNAL`) or if you are charged a service fee for recording (`PAID`).
Type: String
Valid Values: `INTERNAL | PAID`
Required: Yes

 ** provider **   <a name="config-Type-ConfigurationRecorderSummary-provider"></a>
For service-linked configuration recorders that record resources from a third-party cloud service provider, indicates the cloud service provider. Currently, `AZURE` is supported.
Type: String
Valid Values: `AZURE`
Required: No

 ** servicePrincipal **   <a name="config-Type-ConfigurationRecorderSummary-servicePrincipal"></a>
For service-linked configuration recorders, indicates which AWS service the configuration recorder is linked to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_ConfigurationRecorderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationRecorderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationRecorderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationRecorderSummary)
