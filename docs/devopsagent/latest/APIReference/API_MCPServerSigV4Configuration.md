---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerSigV4Configuration.html
---

# MCPServerSigV4Configuration
<a name="API_MCPServerSigV4Configuration"></a>

Configuration for SigV4-authenticated MCP server integration.

## Contents
<a name="API_MCPServerSigV4Configuration_Contents"></a>

 ** tools **   <a name="devopsagent-Type-MCPServerSigV4Configuration-tools"></a>
List of MCP tools available for the association.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** toolDetails **   <a name="devopsagent-Type-MCPServerSigV4Configuration-toolDetails"></a>
List of MCP tools with their access categorization. When provided, the tool names must match those in the tools member.
Type: Array of [MCPToolDetail](API_MCPToolDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

## See Also
<a name="API_MCPServerSigV4Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerSigV4Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerSigV4Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerSigV4Configuration)
