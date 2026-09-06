---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPToolDetail.html
---

# MCPToolDetail
<a name="API_MCPToolDetail"></a>

An MCP tool together with its access categorization.

## Contents
<a name="API_MCPToolDetail_Contents"></a>

 ** name **   <a name="devopsagent-Type-MCPToolDetail-name"></a>
The name of the MCP tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** toolClassification **   <a name="devopsagent-Type-MCPToolDetail-toolClassification"></a>
The access categorization of the MCP tool.
Type: String
Valid Values: `READ_ONLY | MUTATIVE | DESTRUCTIVE`
Required: No

## See Also
<a name="API_MCPToolDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPToolDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPToolDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPToolDetail)
