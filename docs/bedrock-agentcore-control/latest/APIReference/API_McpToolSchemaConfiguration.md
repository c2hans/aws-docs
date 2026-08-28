---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_McpToolSchemaConfiguration.html
---

# McpToolSchemaConfiguration
<a name="API_McpToolSchemaConfiguration"></a>

The MCP tool schema configuration for an MCP server target. The tool schema must be aligned with the MCP specification.

## Contents
<a name="API_McpToolSchemaConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inlinePayload **   <a name="bedrockagentcorecontrol-Type-McpToolSchemaConfiguration-inlinePayload"></a>
The inline payload containing the MCP tool schema definition.
Type: String
Required: No

 ** s3 **   <a name="bedrockagentcorecontrol-Type-McpToolSchemaConfiguration-s3"></a>
The Amazon S3 location of the tool schema. This location contains the schema definition file.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

## See Also
<a name="API_McpToolSchemaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/McpToolSchemaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/McpToolSchemaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/McpToolSchemaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
