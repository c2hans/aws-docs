---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredMCPServerDetails.html
---

# RegisteredMCPServerDetails
<a name="API_RegisteredMCPServerDetails"></a>

Details specific to a registered MCP (Model Context Protocol) server.

## Contents
<a name="API_RegisteredMCPServerDetails_Contents"></a>

 ** authorizationMethod **   <a name="devopsagent-Type-RegisteredMCPServerDetails-authorizationMethod"></a>
The MCP server uses this authorization method.
Type: String
Valid Values: `oauth-client-credentials | oauth-3lo | api-key | bearer-token`
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-RegisteredMCPServerDetails-endpoint"></a>
The MCP server endpoint URL.
Type: String
Required: Yes

 ** name **   <a name="devopsagent-Type-RegisteredMCPServerDetails-name"></a>
The MCP server name.
Type: String
Required: Yes

 ** apiKeyHeader **   <a name="devopsagent-Type-RegisteredMCPServerDetails-apiKeyHeader"></a>
If the MCP server uses API key authentication, these details are provided.
Type: String
Required: No

 ** description **   <a name="devopsagent-Type-RegisteredMCPServerDetails-description"></a>
Optional description for the MCP server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_RegisteredMCPServerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredMCPServerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredMCPServerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredMCPServerDetails)
