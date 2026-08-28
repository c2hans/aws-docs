---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerBearerTokenConfig.html
---

# MCPServerBearerTokenConfig
<a name="API_MCPServerBearerTokenConfig"></a>

Bearer token configuration for MCP server (RFC 6750).

## Contents
<a name="API_MCPServerBearerTokenConfig_Contents"></a>

 ** tokenName **   <a name="devopsagent-Type-MCPServerBearerTokenConfig-tokenName"></a>
User friendly bearer token name specified by end user.
Type: String
Pattern: `[a-zA-Z0-9_\s-]+`
Required: Yes

 ** tokenValue **   <a name="devopsagent-Type-MCPServerBearerTokenConfig-tokenValue"></a>
Bearer token value in alphanumeric for authenticating with the service.
Type: String
Pattern: `[\S]+`
Required: Yes

 ** authorizationHeader **   <a name="devopsagent-Type-MCPServerBearerTokenConfig-authorizationHeader"></a>
HTTP header name to send the bearer token in requests to the service. Defaults to 'Authorization' per RFC 6750.
Type: String
Pattern: `[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_MCPServerBearerTokenConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerBearerTokenConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerBearerTokenConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerBearerTokenConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
