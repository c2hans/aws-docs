---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-contentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory ContentConfiguration
<a name="aws-properties-bedrockagentcore-memory-contentconfiguration"></a>

Defines what content to stream and at what level of detail.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-contentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-contentconfiguration-syntax.json"></a>

```
{
  "[Level](#cfn-bedrockagentcore-memory-contentconfiguration-level)" : {{String}},
  "[Type](#cfn-bedrockagentcore-memory-contentconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-contentconfiguration-syntax.yaml"></a>

```
  [Level](#cfn-bedrockagentcore-memory-contentconfiguration-level): {{String}}
  [Type](#cfn-bedrockagentcore-memory-contentconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-contentconfiguration-properties"></a>

`Level`  <a name="cfn-bedrockagentcore-memory-contentconfiguration-level"></a>
Level of detail for streamed content.
*Required*: No
*Type*: String
*Allowed values*: `METADATA_ONLY | FULL_CONTENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-memory-contentconfiguration-type"></a>
Type of content to stream.
*Required*: Yes
*Type*: String
*Allowed values*: `MEMORY_RECORDS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
