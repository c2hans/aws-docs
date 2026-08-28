---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerConfiguration.html
---

# MCPServerConfiguration
<a name="API_MCPServerConfiguration"></a>

Configuration for Model Context Protocol (MCP) server integration.

## Contents
<a name="API_MCPServerConfiguration_Contents"></a>

 ** tools **   <a name="devopsagent-Type-MCPServerConfiguration-tools"></a>
List of MCP tools can be used with the association.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** toolDetails **   <a name="devopsagent-Type-MCPServerConfiguration-toolDetails"></a>
List of MCP tools with their access categorization. When provided, the tool names must match those in the tools member.
Type: Array of [MCPToolDetail](API_MCPToolDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

## See Also
<a name="API_MCPServerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
