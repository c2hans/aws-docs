---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AgentCoreRuntimeInvocation.html
---

# AgentCoreRuntimeInvocation

The configuration for invoking an agent hosted on AgentCore Runtime. Each scenario runs in its own runtime session, and the turns of a scenario are sent in order within that session. The batch evaluation uses your credentials to read the agent runtime endpoint and the dataset, invoke the agent runtime, and read the resulting traces. You must have permission for these actions.

## Contents
<a name="API_AgentCoreRuntimeInvocation_Contents"></a>

 ** agentRuntimeEndpointArn **   <a name="BedrockAgentCore-Type-AgentCoreRuntimeInvocation-agentRuntimeEndpointArn"></a>
The Amazon Resource Name (ARN) of the agent runtime endpoint to invoke. Specify an endpoint in the same account and Region as the batch evaluation. The service requires the endpoint and its agent runtime version to be ready. The agent runtime must use the HTTP protocol and IAM inbound authorization.
Type: String
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}/runtime-endpoint/[a-zA-Z][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** requestTemplate **   <a name="BedrockAgentCore-Type-AgentCoreRuntimeInvocation-requestTemplate"></a>
A JSON object template for the request payload sent to the agent for each turn. The template must contain the placeholder `{{turn.input}}` exactly once, as the complete value of a JSON string and not as a field name. The service replaces the placeholder with the input of the turn. If the input isn't a string, the service inserts it as a JSON value. If you don't specify a template, the service uses `{"prompt": "{{turn.input}}"}`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

## See Also
<a name="API_AgentCoreRuntimeInvocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentCoreRuntimeInvocation)
