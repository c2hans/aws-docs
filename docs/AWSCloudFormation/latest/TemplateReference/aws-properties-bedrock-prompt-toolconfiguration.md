---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-toolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt ToolConfiguration
<a name="aws-properties-bedrock-prompt-toolconfiguration"></a>

Configuration information for the tools that you pass to a model. For more information, see [Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-prompt-toolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-toolconfiguration-syntax.json"></a>

```
{
  "[ToolChoice](#cfn-bedrock-prompt-toolconfiguration-toolchoice)" : {{ToolChoice}},
  "[Tools](#cfn-bedrock-prompt-toolconfiguration-tools)" : {{[ Tool, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-toolconfiguration-syntax.yaml"></a>

```
  [ToolChoice](#cfn-bedrock-prompt-toolconfiguration-toolchoice): {{
    ToolChoice}}
  [Tools](#cfn-bedrock-prompt-toolconfiguration-tools): {{
    - Tool}}
```

## Properties
<a name="aws-properties-bedrock-prompt-toolconfiguration-properties"></a>

`ToolChoice`  <a name="cfn-bedrock-prompt-toolconfiguration-toolchoice"></a>
If supported by model, forces the model to request a tool.
*Required*: No
*Type*: [ToolChoice](aws-properties-bedrock-prompt-toolchoice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tools`  <a name="cfn-bedrock-prompt-toolconfiguration-tools"></a>
An array of tools that you want to pass to a model.
*Required*: Yes
*Type*: Array of [Tool](aws-properties-bedrock-prompt-tool.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
