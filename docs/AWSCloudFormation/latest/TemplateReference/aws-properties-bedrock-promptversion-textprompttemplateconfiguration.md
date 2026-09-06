---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-textprompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion TextPromptTemplateConfiguration
<a name="aws-properties-bedrock-promptversion-textprompttemplateconfiguration"></a>

Contains configurations for a text prompt template. To include a variable, enclose a word in double curly braces as in `{{variable}}`.

## Syntax
<a name="aws-properties-bedrock-promptversion-textprompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-textprompttemplateconfiguration-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-promptversion-textprompttemplateconfiguration-cachepoint)" : {{CachePointBlock}},
  "[InputVariables](#cfn-bedrock-promptversion-textprompttemplateconfiguration-inputvariables)" : {{[ PromptInputVariable, ... ]}},
  "[Text](#cfn-bedrock-promptversion-textprompttemplateconfiguration-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-textprompttemplateconfiguration-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-promptversion-textprompttemplateconfiguration-cachepoint): {{
    CachePointBlock}}
  [InputVariables](#cfn-bedrock-promptversion-textprompttemplateconfiguration-inputvariables): {{
    - PromptInputVariable}}
  [Text](#cfn-bedrock-promptversion-textprompttemplateconfiguration-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-textprompttemplateconfiguration-properties"></a>

`CachePoint`  <a name="cfn-bedrock-promptversion-textprompttemplateconfiguration-cachepoint"></a>
A cache checkpoint within a template configuration.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-promptversion-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputVariables`  <a name="cfn-bedrock-promptversion-textprompttemplateconfiguration-inputvariables"></a>
An array of the variables in the prompt template.
*Required*: No
*Type*: Array of [PromptInputVariable](aws-properties-bedrock-promptversion-promptinputvariable.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-promptversion-textprompttemplateconfiguration-text"></a>
The message for the prompt.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
