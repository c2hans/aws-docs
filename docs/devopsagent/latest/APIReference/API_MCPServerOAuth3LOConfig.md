---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerOAuth3LOConfig.html
---

# MCPServerOAuth3LOConfig
<a name="API_MCPServerOAuth3LOConfig"></a>

OAuth 3-legged authorization configuration for MCP server.

## Contents
<a name="API_MCPServerOAuth3LOConfig_Contents"></a>

 ** authorizationUrl **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-authorizationUrl"></a>
OAuth authorization URL for 3LO authentication.
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** clientId **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-clientId"></a>
OAuth client ID for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\u007E]+`
Required: Yes

 ** exchangeUrl **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-exchangeUrl"></a>
OAuth token exchange URL.
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** returnToEndpoint **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-returnToEndpoint"></a>
The endpoint to return to after OAuth flow completes (must be AWS console domain)
Type: String
Pattern: `https://[a-zA-Z0-9.-]*\.(console\.(aws|aws-dev)|awsc-(integ|preprod)\.aws)\.amazon\.com(/.*)?`
Required: Yes

 ** clientName **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-clientName"></a>
User friendly OAuth client name specified by end user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\p{L}\p{N}\p{Z}._-]+`
Required: No

 ** clientSecret **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-clientSecret"></a>
OAuth client secret for authenticating with the service. Required for confidential clients or when PKCE is not supported. Optional for public clients using PKCE.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\S]*`
Required: No

 ** exchangeParameters **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-exchangeParameters"></a>
OAuth token exchange parameters for authenticating with the service.
Type: String to string map
Required: No

 ** scopes **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-scopes"></a>
OAuth scopes for 3LO authentication. The service will always request scope offline\_access.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!#-\[\]-~]+`
Required: No

 ** supportCodeChallenge **   <a name="devopsagent-Type-MCPServerOAuth3LOConfig-supportCodeChallenge"></a>
Whether the service supports PKCE (Proof Key for Code Exchange) for enhanced security during the OAuth flow.
Type: Boolean
Required: No

## See Also
<a name="API_MCPServerOAuth3LOConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerOAuth3LOConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerOAuth3LOConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerOAuth3LOConfig)
