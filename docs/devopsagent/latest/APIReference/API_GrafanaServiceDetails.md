---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GrafanaServiceDetails.html
---

# GrafanaServiceDetails
<a name="API_GrafanaServiceDetails"></a>

Complete service details for Grafana MCP server integration.

## Contents
<a name="API_GrafanaServiceDetails_Contents"></a>

 ** authorizationConfig **   <a name="devopsagent-Type-GrafanaServiceDetails-authorizationConfig"></a>
Grafana MCP server authorization configuration (experimental).
Type: [MCPServerAuthorizationConfig](API_MCPServerAuthorizationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-GrafanaServiceDetails-endpoint"></a>
MCP server endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-GrafanaServiceDetails-name"></a>
MCP server name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** description **   <a name="devopsagent-Type-GrafanaServiceDetails-description"></a>
Optional description for the MCP server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_GrafanaServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GrafanaServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GrafanaServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GrafanaServiceDetails)
