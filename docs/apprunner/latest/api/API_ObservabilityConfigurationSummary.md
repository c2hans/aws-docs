---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ObservabilityConfigurationSummary.html
---

# ObservabilityConfigurationSummary
<a name="API_ObservabilityConfigurationSummary"></a>

Provides summary information about an AWS App Runner observability configuration resource.

This type contains limited information about an observability configuration. It includes only identification information, without configuration details. It's returned by the [ListObservabilityConfigurations](API_ListObservabilityConfigurations.md) action. Complete configuration information is returned by the [CreateObservabilityConfiguration](API_CreateObservabilityConfiguration.md), [DescribeObservabilityConfiguration](API_DescribeObservabilityConfiguration.md), and [DeleteObservabilityConfiguration](API_DeleteObservabilityConfiguration.md) actions using the [ObservabilityConfiguration](API_ObservabilityConfiguration.md) type.

## Contents
<a name="API_ObservabilityConfigurationSummary_Contents"></a>

 ** ObservabilityConfigurationArn **   <a name="apprunner-Type-ObservabilityConfigurationSummary-ObservabilityConfigurationArn"></a>
The Amazon Resource Name (ARN) of this observability configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** ObservabilityConfigurationName **   <a name="apprunner-Type-ObservabilityConfigurationSummary-ObservabilityConfigurationName"></a>
The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** ObservabilityConfigurationRevision **   <a name="apprunner-Type-ObservabilityConfigurationSummary-ObservabilityConfigurationRevision"></a>
The revision of this observability configuration. It's unique among all the active configurations (`"Status": "ACTIVE"`) that share the same `ObservabilityConfigurationName`.
Type: Integer
Required: No

## See Also
<a name="API_ObservabilityConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ObservabilityConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ObservabilityConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ObservabilityConfigurationSummary)
