---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-prompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion PromptTemplateConfiguration
<a name="aws-properties-bedrock-flowversion-prompttemplateconfiguration"></a>

Contains the message for a prompt. For more information, see [Construct and store reusable prompts with Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html).

## Syntax
<a name="aws-properties-bedrock-flowversion-prompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-prompttemplateconfiguration-syntax.json"></a>

```
{
  "[Text](#cfn-bedrock-flowversion-prompttemplateconfiguration-text)" : {{TextPromptTemplateConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-prompttemplateconfiguration-syntax.yaml"></a>

```
  [Text](#cfn-bedrock-flowversion-prompttemplateconfiguration-text): {{
    TextPromptTemplateConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-prompttemplateconfiguration-properties"></a>

`Text`  <a name="cfn-bedrock-flowversion-prompttemplateconfiguration-text"></a>
Contains configurations for the text in a message for a prompt.
*Required*: Yes
*Type*: [TextPromptTemplateConfiguration](aws-properties-bedrock-flowversion-textprompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
