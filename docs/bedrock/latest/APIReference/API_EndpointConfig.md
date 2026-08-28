---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_EndpointConfig.html
---

# EndpointConfig
<a name="API_EndpointConfig"></a>

Specifies the configuration for the endpoint.

## Contents
<a name="API_EndpointConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sageMaker **   <a name="bedrock-Type-EndpointConfig-sageMaker"></a>
The configuration specific to Amazon SageMaker for the endpoint.
Type: [SageMakerEndpoint](API_SageMakerEndpoint.md) object
Required: No

## See Also
<a name="API_EndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EndpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EndpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EndpointConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
