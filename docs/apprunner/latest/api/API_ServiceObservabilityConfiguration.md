---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ServiceObservabilityConfiguration.html
---

# ServiceObservabilityConfiguration
<a name="API_ServiceObservabilityConfiguration"></a>

Describes the observability configuration of an AWS App Runner service. These are additional observability features, like tracing, that you choose to enable. They're configured in a separate resource that you associate with your service.

## Contents
<a name="API_ServiceObservabilityConfiguration_Contents"></a>

 ** ObservabilityEnabled **   <a name="apprunner-Type-ServiceObservabilityConfiguration-ObservabilityEnabled"></a>
When `true`, an observability configuration resource is associated with the service, and an `ObservabilityConfigurationArn` is specified.
Type: Boolean
Required: Yes

 ** ObservabilityConfigurationArn **   <a name="apprunner-Type-ServiceObservabilityConfiguration-ObservabilityConfigurationArn"></a>
The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when `ObservabilityEnabled` is `true`.
Specify an ARN with a name and a revision number to associate that revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3`
Specify just the name to associate the latest revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

## See Also
<a name="API_ServiceObservabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ServiceObservabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ServiceObservabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ServiceObservabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
