---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CustomTransformConfiguration.html
---

# CustomTransformConfiguration
<a name="API_CustomTransformConfiguration"></a>

The configuration for custom transformations applied to requests and responses through the gateway. This structure defines how the gateway transforms data.

## Contents
<a name="API_CustomTransformConfiguration_Contents"></a>

 ** lambda **   <a name="bedrockagentcorecontrol-Type-CustomTransformConfiguration-lambda"></a>
The Lambda configuration for custom transformations. This configuration defines how the gateway uses a Lambda function to transform data.
Type: [LambdaTransformConfiguration](API_LambdaTransformConfiguration.md) object
Required: No

## See Also
<a name="API_CustomTransformConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomTransformConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomTransformConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomTransformConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
