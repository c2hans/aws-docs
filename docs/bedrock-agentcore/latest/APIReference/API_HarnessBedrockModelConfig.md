---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessBedrockModelConfig.html
---

# HarnessBedrockModelConfig
<a name="API_HarnessBedrockModelConfig"></a>

Configuration for an Amazon Bedrock model provider.

## Contents
<a name="API_HarnessBedrockModelConfig_Contents"></a>

 ** modelId **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-modelId"></a>
The Bedrock model ID.
Type: String
Required: Yes

 ** additionalParams **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-additionalParams"></a>
Provider-specific parameters passed through to the model provider unchanged.
Type: JSON value
Required: No

 ** apiFormat **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-apiFormat"></a>
The API format to use when calling the Bedrock provider.
Type: String
Valid Values: `converse_stream | responses | chat_completions`
Required: No

 ** maxTokens **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-maxTokens"></a>
The maximum number of tokens to allow in the generated response per iteration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** temperature **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-temperature"></a>
The temperature to set when calling the model.
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 2.0.
Required: No

 ** topP **   <a name="BedrockAgentCore-Type-HarnessBedrockModelConfig-topP"></a>
The topP set when calling the model.
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_HarnessBedrockModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessBedrockModelConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
