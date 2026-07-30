---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-prompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion PromptTemplateConfiguration
<a name="aws-properties-bedrock-promptversion-prompttemplateconfiguration"></a>

Contains the message for a prompt. For more information, see [Construct and store reusable prompts with Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html).

## Syntax
<a name="aws-properties-bedrock-promptversion-prompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-prompttemplateconfiguration-syntax.json"></a>

```
{
  "[Chat](#cfn-bedrock-promptversion-prompttemplateconfiguration-chat)" : {{ChatPromptTemplateConfiguration}},
  "[Text](#cfn-bedrock-promptversion-prompttemplateconfiguration-text)" : {{TextPromptTemplateConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-prompttemplateconfiguration-syntax.yaml"></a>

```
  [Chat](#cfn-bedrock-promptversion-prompttemplateconfiguration-chat): {{
    ChatPromptTemplateConfiguration}}
  [Text](#cfn-bedrock-promptversion-prompttemplateconfiguration-text): {{
    TextPromptTemplateConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-prompttemplateconfiguration-properties"></a>

`Chat`  <a name="cfn-bedrock-promptversion-prompttemplateconfiguration-chat"></a>
Contains configurations to use the prompt in a conversational format.
*Required*: No
*Type*: [ChatPromptTemplateConfiguration](aws-properties-bedrock-promptversion-chatprompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-promptversion-prompttemplateconfiguration-text"></a>
Contains configurations for the text in a message for a prompt.
*Required*: No
*Type*: [TextPromptTemplateConfiguration](aws-properties-bedrock-promptversion-textprompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
