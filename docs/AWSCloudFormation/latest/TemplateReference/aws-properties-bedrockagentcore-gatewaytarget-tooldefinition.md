---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ToolDefinition
<a name="aws-properties-bedrockagentcore-gatewaytarget-tooldefinition"></a>

A tool definition for a gateway target. This structure defines a tool that the target exposes through the Model Context Protocol.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-tooldefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-tooldefinition-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-description)" : {{String}},
  "[InputSchema](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-inputschema)" : {{SchemaDefinition}},
  "[Name](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-name)" : {{String}},
  "[OutputSchema](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-outputschema)" : {{SchemaDefinition}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-tooldefinition-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-description): {{String}}
  [InputSchema](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-inputschema): {{
    SchemaDefinition}}
  [Name](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-name): {{String}}
  [OutputSchema](#cfn-bedrockagentcore-gatewaytarget-tooldefinition-outputschema): {{
    SchemaDefinition}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-tooldefinition-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-tooldefinition-description"></a>
The description of the tool. This description provides information about the purpose and usage of the tool.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSchema`  <a name="cfn-bedrockagentcore-gatewaytarget-tooldefinition-inputschema"></a>
The input schema for the tool. This schema defines the structure of the input that the tool accepts.
*Required*: Yes
*Type*: [SchemaDefinition](aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewaytarget-tooldefinition-name"></a>
The name of the tool. This name identifies the tool in the Model Context Protocol.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputSchema`  <a name="cfn-bedrockagentcore-gatewaytarget-tooldefinition-outputschema"></a>
The output schema for the tool. This schema defines the structure of the output that the tool produces.
*Required*: No
*Type*: [SchemaDefinition](aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
