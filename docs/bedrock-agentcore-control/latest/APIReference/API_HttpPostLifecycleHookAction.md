---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HttpPostLifecycleHookAction.html
---

# HttpPostLifecycleHookAction
<a name="API_HttpPostLifecycleHookAction"></a>

A lifecycle hook action that sends an HTTP `POST` request to the agent's container. The path and port can't conflict with a path that your agent already serves for AgentCore Runtime, such as the protocol's invocation path or the health check path.

## Contents
<a name="API_HttpPostLifecycleHookAction_Contents"></a>

 ** path **   <a name="bedrockagentcorecontrol-Type-HttpPostLifecycleHookAction-path"></a>
The path in the agent's container that AgentCore Runtime sends the `POST` request to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `/[A-Za-z0-9._~/-]*`
Required: Yes

 ** port **   <a name="bedrockagentcorecontrol-Type-HttpPostLifecycleHookAction-port"></a>
The port in the agent's container that AgentCore Runtime sends the `POST` request to. If you don't specify a port, the default is the runtime's server port: the port in the protocol configuration if one is set, otherwise the protocol's default port.
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 12000.
Required: No

## See Also
<a name="API_HttpPostLifecycleHookAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HttpPostLifecycleHookAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HttpPostLifecycleHookAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HttpPostLifecycleHookAction)
