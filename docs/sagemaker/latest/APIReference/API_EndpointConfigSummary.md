---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointConfigSummary.html
---

# EndpointConfigSummary
<a name="API_EndpointConfigSummary"></a>

Provides summary information for an endpoint configuration.

## Contents
<a name="API_EndpointConfigSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-EndpointConfigSummary-CreationTime"></a>
A timestamp that shows when the endpoint configuration was created.
Type: Timestamp
Required: Yes

 ** EndpointConfigArn **   <a name="sagemaker-Type-EndpointConfigSummary-EndpointConfigArn"></a>
The Amazon Resource Name (ARN) of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint-config/.*`
Required: Yes

 ** EndpointConfigName **   <a name="sagemaker-Type-EndpointConfigSummary-EndpointConfigName"></a>
The name of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_EndpointConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EndpointConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EndpointConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EndpointConfigSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
