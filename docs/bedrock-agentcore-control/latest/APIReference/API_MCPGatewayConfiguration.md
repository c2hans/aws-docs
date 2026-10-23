---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_MCPGatewayConfiguration.html
---

# MCPGatewayConfiguration
<a name="API_MCPGatewayConfiguration"></a>

The configuration for a Model Context Protocol (MCP) gateway. This structure defines how the gateway implements the MCP protocol.

## Contents
<a name="API_MCPGatewayConfiguration_Contents"></a>

 ** disableMcpListToolsPagination **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-disableMcpListToolsPagination"></a>
Specifies whether the gateway disables pagination for the Model Context Protocol (MCP) `tools/list` operation. When set to `true`, the gateway returns the complete list of tools in a single response without a pagination cursor. When set to `false` or omitted, the gateway returns tools in paginated responses. For information about changing this value on an existing gateway, see [UpdateGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.html).
Type: Boolean
Required: No

 ** instructions **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-instructions"></a>
The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** searchType **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-searchType"></a>
The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.
Type: String
Valid Values: `SEMANTIC`
Required: No

 ** sessionConfiguration **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-sessionConfiguration"></a>
The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.
Type: [SessionConfiguration](API_SessionConfiguration.md) object
Required: No

 ** streamingConfiguration **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-streamingConfiguration"></a>
The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.
Type: [StreamingConfiguration](API_StreamingConfiguration.md) object
Required: No

 ** supportedVersions **   <a name="bedrockagentcorecontrol-Type-MCPGatewayConfiguration-supportedVersions"></a>
The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.
Type: Array of strings
Required: No

## See Also
<a name="API_MCPGatewayConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MCPGatewayConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MCPGatewayConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MCPGatewayConfiguration)
