---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerNewRelicConfiguration.html
---

# MCPServerNewRelicConfiguration
<a name="API_MCPServerNewRelicConfiguration"></a>

Mixin for webhook update support.

## Contents
<a name="API_MCPServerNewRelicConfiguration_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-MCPServerNewRelicConfiguration-accountId"></a>
New Relic Account ID
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `[0-9]+`
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-MCPServerNewRelicConfiguration-endpoint"></a>
MCP server endpoint URL (e.g., https://mcp.newrelic.com/mcp/)
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

## See Also
<a name="API_MCPServerNewRelicConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerNewRelicConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerNewRelicConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerNewRelicConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
