---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-textprompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow TextPromptTemplateConfiguration
<a name="aws-properties-bedrock-flow-textprompttemplateconfiguration"></a>

Contains configurations for a text prompt template. To include a variable, enclose a word in double curly braces as in `{{variable}}`.

## Syntax
<a name="aws-properties-bedrock-flow-textprompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-textprompttemplateconfiguration-syntax.json"></a>

```
{
  "[InputVariables](#cfn-bedrock-flow-textprompttemplateconfiguration-inputvariables)" : {{[ PromptInputVariable, ... ]}},
  "[Text](#cfn-bedrock-flow-textprompttemplateconfiguration-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-textprompttemplateconfiguration-syntax.yaml"></a>

```
  [InputVariables](#cfn-bedrock-flow-textprompttemplateconfiguration-inputvariables): {{
    - PromptInputVariable}}
  [Text](#cfn-bedrock-flow-textprompttemplateconfiguration-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-textprompttemplateconfiguration-properties"></a>

`InputVariables`  <a name="cfn-bedrock-flow-textprompttemplateconfiguration-inputvariables"></a>
An array of the variables in the prompt template.
*Required*: No
*Type*: Array of [PromptInputVariable](aws-properties-bedrock-flow-promptinputvariable.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-flow-textprompttemplateconfiguration-text"></a>
The message for the prompt.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
