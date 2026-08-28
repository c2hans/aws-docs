---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ToolSchema
<a name="aws-properties-bedrockagentcore-gatewaytarget-toolschema"></a>

A tool schema for a gateway target. This structure defines the schema for a tool that the target exposes through the Model Context Protocol.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-toolschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-toolschema-syntax.json"></a>

```
{
  "[InlinePayload](#cfn-bedrockagentcore-gatewaytarget-toolschema-inlinepayload)" : {{[ ToolDefinition, ... ]}},
  "[S3](#cfn-bedrockagentcore-gatewaytarget-toolschema-s3)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-toolschema-syntax.yaml"></a>

```
  [InlinePayload](#cfn-bedrockagentcore-gatewaytarget-toolschema-inlinepayload): {{
    - ToolDefinition}}
  [S3](#cfn-bedrockagentcore-gatewaytarget-toolschema-s3): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-toolschema-properties"></a>

`InlinePayload`  <a name="cfn-bedrockagentcore-gatewaytarget-toolschema-inlinepayload"></a>
The inline payload of the tool schema. This payload contains the schema definition directly in the request.
*Required*: No
*Type*: Array of [ToolDefinition](aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-bedrockagentcore-gatewaytarget-toolschema-s3"></a>
The Amazon S3 location of the tool schema. This location contains the schema definition file.
*Required*: No
*Type*: [S3Configuration](aws-properties-bedrockagentcore-gatewaytarget-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
