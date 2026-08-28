---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredGrafanaServerDetails.html
---

# RegisteredGrafanaServerDetails
<a name="API_RegisteredGrafanaServerDetails"></a>

Details specific to a registered Grafana server, used by the built-in MCP server.

## Contents
<a name="API_RegisteredGrafanaServerDetails_Contents"></a>

 ** authorizationMethod **   <a name="devopsagent-Type-RegisteredGrafanaServerDetails-authorizationMethod"></a>
The authz method used by the MCP server.
Type: String
Valid Values: `oauth-client-credentials | oauth-3lo | api-key | bearer-token`
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-RegisteredGrafanaServerDetails-endpoint"></a>
Grafana instance URL (e.g., https://your-instance.grafana.net)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

## See Also
<a name="API_RegisteredGrafanaServerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredGrafanaServerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredGrafanaServerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredGrafanaServerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
