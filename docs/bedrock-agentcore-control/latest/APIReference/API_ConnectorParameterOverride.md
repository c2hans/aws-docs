---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConnectorParameterOverride.html
---

# ConnectorParameterOverride
<a name="API_ConnectorParameterOverride"></a>

Specifies a parameter override for a connector tool, allowing you to control parameter visibility and descriptions.

## Contents
<a name="API_ConnectorParameterOverride_Contents"></a>

 ** path **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-path"></a>
A JSON Pointer path identifying the parameter (for example, `/numberOfResults` or `/filter`).
Type: String
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-description"></a>
An agent-facing description override for this parameter.
Type: String
Required: No

 ** visible **   <a name="bedrockagentcorecontrol-Type-ConnectorParameterOverride-visible"></a>
Whether this parameter is visible to the agent. If not specified, uses the service default.
Type: Boolean
Required: No

## See Also
<a name="API_ConnectorParameterOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConnectorParameterOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
