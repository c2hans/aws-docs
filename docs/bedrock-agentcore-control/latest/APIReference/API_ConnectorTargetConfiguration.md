---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConnectorTargetConfiguration.html
---

# ConnectorTargetConfiguration
<a name="API_ConnectorTargetConfiguration"></a>

Configuration for a connector integration target. Connectors provide pre-built integrations with AWS services and third-party tools.

## Contents
<a name="API_ConnectorTargetConfiguration_Contents"></a>

 ** source **   <a name="bedrockagentcorecontrol-Type-ConnectorTargetConfiguration-source"></a>
The source configuration identifying which connector to use.
Type: [ConnectorSource](API_ConnectorSource.md) object
Required: Yes

 ** configurations **   <a name="bedrockagentcorecontrol-Type-ConnectorTargetConfiguration-configurations"></a>
A list of per-tool configurations for the connector.
Type: Array of [ConnectorConfiguration](API_ConnectorConfiguration.md) objects
Required: No

 ** enabled **   <a name="bedrockagentcorecontrol-Type-ConnectorTargetConfiguration-enabled"></a>
A list of tool names to enable from this connector. If absent, all tools provided by the connector are enabled.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ConnectorTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConnectorTargetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConnectorTargetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConnectorTargetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
