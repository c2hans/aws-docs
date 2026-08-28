---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-toolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion ToolConfiguration
<a name="aws-properties-bedrock-promptversion-toolconfiguration"></a>

Configuration information for the tools that you pass to a model. For more information, see [Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-promptversion-toolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-toolconfiguration-syntax.json"></a>

```
{
  "[ToolChoice](#cfn-bedrock-promptversion-toolconfiguration-toolchoice)" : {{ToolChoice}},
  "[Tools](#cfn-bedrock-promptversion-toolconfiguration-tools)" : {{[ Tool, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-toolconfiguration-syntax.yaml"></a>

```
  [ToolChoice](#cfn-bedrock-promptversion-toolconfiguration-toolchoice): {{
    ToolChoice}}
  [Tools](#cfn-bedrock-promptversion-toolconfiguration-tools): {{
    - Tool}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-toolconfiguration-properties"></a>

`ToolChoice`  <a name="cfn-bedrock-promptversion-toolconfiguration-toolchoice"></a>
If supported by model, forces the model to request a tool.
*Required*: No
*Type*: [ToolChoice](aws-properties-bedrock-promptversion-toolchoice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tools`  <a name="cfn-bedrock-promptversion-toolconfiguration-tools"></a>
An array of tools that you want to pass to a model.
*Required*: Yes
*Type*: Array of [Tool](aws-properties-bedrock-promptversion-tool.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
