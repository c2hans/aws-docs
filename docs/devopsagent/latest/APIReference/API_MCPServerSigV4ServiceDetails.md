---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerSigV4ServiceDetails.html
---

# MCPServerSigV4ServiceDetails
<a name="API_MCPServerSigV4ServiceDetails"></a>

Complete service details for SigV4-authenticated MCP server integration.

## Contents
<a name="API_MCPServerSigV4ServiceDetails_Contents"></a>

 ** authorizationConfig **   <a name="devopsagent-Type-MCPServerSigV4ServiceDetails-authorizationConfig"></a>
MCP Server SigV4 authorization configuration.
Type: [MCPServerSigV4AuthorizationConfig](API_MCPServerSigV4AuthorizationConfig.md) object
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-MCPServerSigV4ServiceDetails-endpoint"></a>
MCP server endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-MCPServerSigV4ServiceDetails-name"></a>
MCP server name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** description **   <a name="devopsagent-Type-MCPServerSigV4ServiceDetails-description"></a>
Optional description for the MCP server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_MCPServerSigV4ServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerSigV4ServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerSigV4ServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerSigV4ServiceDetails)
