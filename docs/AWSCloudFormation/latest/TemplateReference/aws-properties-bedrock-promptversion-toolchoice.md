---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-toolchoice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion ToolChoice
<a name="aws-properties-bedrock-promptversion-toolchoice"></a>

Determines which tools the model should request in a call to `Converse` or `ConverseStream`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-promptversion-toolchoice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-toolchoice-syntax.json"></a>

```
{
  "[Any](#cfn-bedrock-promptversion-toolchoice-any)" : {{Json}},
  "[Auto](#cfn-bedrock-promptversion-toolchoice-auto)" : {{Json}},
  "[Tool](#cfn-bedrock-promptversion-toolchoice-tool)" : {{SpecificToolChoice}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-toolchoice-syntax.yaml"></a>

```
  [Any](#cfn-bedrock-promptversion-toolchoice-any): {{Json}}
  [Auto](#cfn-bedrock-promptversion-toolchoice-auto): {{Json}}
  [Tool](#cfn-bedrock-promptversion-toolchoice-tool): {{
    SpecificToolChoice}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-toolchoice-properties"></a>

`Any`  <a name="cfn-bedrock-promptversion-toolchoice-any"></a>
The model must request at least one tool (no text is generated).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Auto`  <a name="cfn-bedrock-promptversion-toolchoice-auto"></a>
(Default). The Model automatically decides if a tool should be called or whether to generate text instead.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tool`  <a name="cfn-bedrock-promptversion-toolchoice-tool"></a>
The Model must request the specified tool. Only supported by Anthropic Claude 3 and Amazon Nova models.
*Required*: No
*Type*: [SpecificToolChoice](aws-properties-bedrock-promptversion-specifictoolchoice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
