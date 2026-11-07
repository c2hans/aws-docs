---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ProtocolConfiguration.html
---

# ProtocolConfiguration
<a name="API_ProtocolConfiguration"></a>

The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.

## Contents
<a name="API_ProtocolConfiguration_Contents"></a>

 ** serverProtocol **   <a name="bedrockagentcorecontrol-Type-ProtocolConfiguration-serverProtocol"></a>
The server protocol for the agent runtime. This field specifies which protocol the agent runtime uses to communicate with clients.
Type: String
Valid Values: `MCP | HTTP | A2A | AGUI`
Required: Yes

 ** path **   <a name="bedrockagentcorecontrol-Type-ProtocolConfiguration-path"></a>
The path on which the agent server accepts requests. The path must begin with `/`. When this field is omitted, the default is `/invocations` for `HTTP` and `AGUI`, `/mcp` for `MCP`, and `/` for `A2A`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `/[A-Za-z0-9\-._~/%]*`
Required: No

 ** port **   <a name="bedrockagentcorecontrol-Type-ProtocolConfiguration-port"></a>
The port on which the agent server listens. The port must be between `8000` and `12000`, excluding the reserved port `8443`. When this field is omitted, the default is `8080` for `HTTP` and `AGUI`, `8000` for `MCP`, and `9000` for `A2A`.
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 12000.
Required: No

## See Also
<a name="API_ProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ProtocolConfiguration)
