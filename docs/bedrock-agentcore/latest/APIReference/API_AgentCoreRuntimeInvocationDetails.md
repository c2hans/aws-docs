---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AgentCoreRuntimeInvocationDetails.html
---

# AgentCoreRuntimeInvocationDetails

The details of the agent hosted on AgentCore Runtime that a batch evaluation invoked.

## Contents
<a name="API_AgentCoreRuntimeInvocationDetails_Contents"></a>

 ** agentRuntimeEndpointArn **   <a name="BedrockAgentCore-Type-AgentCoreRuntimeInvocationDetails-agentRuntimeEndpointArn"></a>
The Amazon Resource Name (ARN) of the agent runtime endpoint that the batch evaluation invoked.
Type: String
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}/runtime-endpoint/[a-zA-Z][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** agentRuntimeVersion **   <a name="BedrockAgentCore-Type-AgentCoreRuntimeInvocationDetails-agentRuntimeVersion"></a>
The version of the agent runtime that the endpoint pointed to when the batch evaluation started. If you update the endpoint after the batch evaluation starts, each later turn uses the version that the endpoint points to when the turn runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `([1-9][0-9]{0,4})`
Required: Yes

 ** requestTemplate **   <a name="BedrockAgentCore-Type-AgentCoreRuntimeInvocationDetails-requestTemplate"></a>
The request payload template that the batch evaluation used for each turn. If the request didn't specify a template, this is the default template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

## See Also
<a name="API_AgentCoreRuntimeInvocationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocationDetails)
