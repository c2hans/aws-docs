---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerAuthorizationConfig.html
---

# MCPServerAuthorizationConfig
<a name="API_MCPServerAuthorizationConfig"></a>

Authorization configuration options for MCP server, supporting OAuth, API key, bearer token, and authorization discovery methods.

## Contents
<a name="API_MCPServerAuthorizationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiKey **   <a name="devopsagent-Type-MCPServerAuthorizationConfig-apiKey"></a>
MCP server configuration with API key authentication.
Type: [MCPServerAPIKeyConfig](API_MCPServerAPIKeyConfig.md) object
Required: No

 ** authorizationDiscovery **   <a name="devopsagent-Type-MCPServerAuthorizationConfig-authorizationDiscovery"></a>
MCP server authorization discovery configuration.
Type: [MCPServerAuthorizationDiscoveryConfig](API_MCPServerAuthorizationDiscoveryConfig.md) object
Required: No

 ** bearerToken **   <a name="devopsagent-Type-MCPServerAuthorizationConfig-bearerToken"></a>
MCP server configuration with Bearer token (RFC 6750).
Type: [MCPServerBearerTokenConfig](API_MCPServerBearerTokenConfig.md) object
Required: No

 ** oAuth3LO **   <a name="devopsagent-Type-MCPServerAuthorizationConfig-oAuth3LO"></a>
MCP server configuration with OAuth 3LO.
Type: [MCPServerOAuth3LOConfig](API_MCPServerOAuth3LOConfig.md) object
Required: No

 ** oAuthClientCredentials **   <a name="devopsagent-Type-MCPServerAuthorizationConfig-oAuthClientCredentials"></a>
MCP server configuration with OAuth client credentials.
Type: [MCPServerOAuthClientCredentialsConfig](API_MCPServerOAuthClientCredentialsConfig.md) object
Required: No

## See Also
<a name="API_MCPServerAuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerAuthorizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerAuthorizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerAuthorizationConfig)
