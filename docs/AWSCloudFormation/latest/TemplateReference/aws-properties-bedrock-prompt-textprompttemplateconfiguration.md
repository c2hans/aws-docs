---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-textprompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt TextPromptTemplateConfiguration
<a name="aws-properties-bedrock-prompt-textprompttemplateconfiguration"></a>

Contains configurations for a text prompt template. To include a variable, enclose a word in double curly braces as in `{{variable}}`.

## Syntax
<a name="aws-properties-bedrock-prompt-textprompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-textprompttemplateconfiguration-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-prompt-textprompttemplateconfiguration-cachepoint)" : {{CachePointBlock}},
  "[InputVariables](#cfn-bedrock-prompt-textprompttemplateconfiguration-inputvariables)" : {{[ PromptInputVariable, ... ]}},
  "[Text](#cfn-bedrock-prompt-textprompttemplateconfiguration-text)" : {{String}},
  "[TextS3Location](#cfn-bedrock-prompt-textprompttemplateconfiguration-texts3location)" : {{TextS3Location}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-textprompttemplateconfiguration-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-prompt-textprompttemplateconfiguration-cachepoint): {{
    CachePointBlock}}
  [InputVariables](#cfn-bedrock-prompt-textprompttemplateconfiguration-inputvariables): {{
    - PromptInputVariable}}
  [Text](#cfn-bedrock-prompt-textprompttemplateconfiguration-text): {{String}}
  [TextS3Location](#cfn-bedrock-prompt-textprompttemplateconfiguration-texts3location): {{
    TextS3Location}}
```

## Properties
<a name="aws-properties-bedrock-prompt-textprompttemplateconfiguration-properties"></a>

`CachePoint`  <a name="cfn-bedrock-prompt-textprompttemplateconfiguration-cachepoint"></a>
A cache checkpoint within a template configuration.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-prompt-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputVariables`  <a name="cfn-bedrock-prompt-textprompttemplateconfiguration-inputvariables"></a>
An array of the variables in the prompt template.
*Required*: No
*Type*: Array of [PromptInputVariable](aws-properties-bedrock-prompt-promptinputvariable.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-prompt-textprompttemplateconfiguration-text"></a>
The message for the prompt.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextS3Location`  <a name="cfn-bedrock-prompt-textprompttemplateconfiguration-texts3location"></a>
The Amazon S3location of the prompt text.
*Required*: No
*Type*: [TextS3Location](aws-properties-bedrock-prompt-texts3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
