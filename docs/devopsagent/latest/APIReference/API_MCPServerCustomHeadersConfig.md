---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerCustomHeadersConfig.html
---

# MCPServerCustomHeadersConfig
<a name="API_MCPServerCustomHeadersConfig"></a>

Configuration for authenticating to an MCP server with custom HTTP headers.

## Contents
<a name="API_MCPServerCustomHeadersConfig_Contents"></a>

 ** headers **   <a name="devopsagent-Type-MCPServerCustomHeadersConfig-headers"></a>
Custom headers map.
Type: String to string map
Map Entries: Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9-_]+`
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Pattern: `[!-~]([ \t]*[!-~])*`
Required: Yes

## See Also
<a name="API_MCPServerCustomHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerCustomHeadersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerCustomHeadersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerCustomHeadersConfig)
