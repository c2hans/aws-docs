---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerGrafanaConfiguration.html
---

# MCPServerGrafanaConfiguration
<a name="API_MCPServerGrafanaConfiguration"></a>

Configuration for Grafana MCP server integration, used with an AWS-hosted MCP server.

## Contents
<a name="API_MCPServerGrafanaConfiguration_Contents"></a>

 ** endpoint **   <a name="devopsagent-Type-MCPServerGrafanaConfiguration-endpoint"></a>
Grafana instance URL (e.g., https://your-instance.grafana.net)
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** enabledElevatedTools **   <a name="devopsagent-Type-MCPServerGrafanaConfiguration-enabledElevatedTools"></a>
The subset of elevated-access tools enabled for this integration.
Type: Array of [MCPToolDetail](API_MCPToolDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** organizationId **   <a name="devopsagent-Type-MCPServerGrafanaConfiguration-organizationId"></a>
The Grafana organization ID that can be used.
Type: String
Pattern: `[0-9]+`
Required: No

 ** tools **   <a name="devopsagent-Type-MCPServerGrafanaConfiguration-tools"></a>
List of MCP tools that can be used.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_MCPServerGrafanaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerGrafanaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerGrafanaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerGrafanaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
