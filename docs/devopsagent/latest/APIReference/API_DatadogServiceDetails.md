---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DatadogServiceDetails.html
---

# DatadogServiceDetails
<a name="API_DatadogServiceDetails"></a>

Complete service details for Datadog MCP server integration.

## Contents
<a name="API_DatadogServiceDetails_Contents"></a>

 ** authorizationConfig **   <a name="devopsagent-Type-DatadogServiceDetails-authorizationConfig"></a>
Datadog MCP server authorization configuration (only authorization discovery is supported).
Type: [DatadogAuthorizationConfig](API_DatadogAuthorizationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-DatadogServiceDetails-endpoint"></a>
MCP server endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-DatadogServiceDetails-name"></a>
MCP server name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** description **   <a name="devopsagent-Type-DatadogServiceDetails-description"></a>
Optional description for the MCP server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_DatadogServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/DatadogServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/DatadogServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/DatadogServiceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
