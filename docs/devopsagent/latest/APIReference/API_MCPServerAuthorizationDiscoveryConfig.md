---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerAuthorizationDiscoveryConfig.html
---

# MCPServerAuthorizationDiscoveryConfig
<a name="API_MCPServerAuthorizationDiscoveryConfig"></a>

Authorization discovery configuration for MCP server.

## Contents
<a name="API_MCPServerAuthorizationDiscoveryConfig_Contents"></a>

 ** returnToEndpoint **   <a name="devopsagent-Type-MCPServerAuthorizationDiscoveryConfig-returnToEndpoint"></a>
The endpoint to return to after OAuth flow completes (must be AWS console domain)
Type: String
Pattern: `https://[a-zA-Z0-9.-]*\.(console\.(aws|aws-dev)|awsc-(integ|preprod)\.aws)\.amazon\.com(/.*)?`
Required: Yes

## See Also
<a name="API_MCPServerAuthorizationDiscoveryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerAuthorizationDiscoveryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerAuthorizationDiscoveryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerAuthorizationDiscoveryConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
