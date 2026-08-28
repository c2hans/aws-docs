---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_McpDescriptor.html
---

# McpDescriptor
<a name="API_McpDescriptor"></a>

The Model Context Protocol (MCP) descriptor for a registry record. Contains the server definition and tools definition for an MCP-compatible server. The schema is validated against the MCP protocol specification.

## Contents
<a name="API_McpDescriptor_Contents"></a>

 ** server **   <a name="bedrockagentcorecontrol-Type-McpDescriptor-server"></a>
The MCP server definition, containing the server configuration and schema as defined by the MCP protocol specification.
Type: [ServerDefinition](API_ServerDefinition.md) object
Required: No

 ** tools **   <a name="bedrockagentcorecontrol-Type-McpDescriptor-tools"></a>
The MCP tools definition, containing the tools available on the MCP server as defined by the MCP protocol specification.
Type: [ToolsDefinition](API_ToolsDefinition.md) object
Required: No

## See Also
<a name="API_McpDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/McpDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/McpDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/McpDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
