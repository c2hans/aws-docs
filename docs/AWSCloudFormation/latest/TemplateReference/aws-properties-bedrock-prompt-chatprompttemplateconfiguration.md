---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-chatprompttemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt ChatPromptTemplateConfiguration
<a name="aws-properties-bedrock-prompt-chatprompttemplateconfiguration"></a>

Contains configurations to use a prompt in a conversational format. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Syntax
<a name="aws-properties-bedrock-prompt-chatprompttemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-chatprompttemplateconfiguration-syntax.json"></a>

```
{
  "[InputVariables](#cfn-bedrock-prompt-chatprompttemplateconfiguration-inputvariables)" : {{[ PromptInputVariable, ... ]}},
  "[Messages](#cfn-bedrock-prompt-chatprompttemplateconfiguration-messages)" : {{[ Message, ... ]}},
  "[System](#cfn-bedrock-prompt-chatprompttemplateconfiguration-system)" : {{[ SystemContentBlock, ... ]}},
  "[ToolConfiguration](#cfn-bedrock-prompt-chatprompttemplateconfiguration-toolconfiguration)" : {{ToolConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-chatprompttemplateconfiguration-syntax.yaml"></a>

```
  [InputVariables](#cfn-bedrock-prompt-chatprompttemplateconfiguration-inputvariables): {{
    - PromptInputVariable}}
  [Messages](#cfn-bedrock-prompt-chatprompttemplateconfiguration-messages): {{
    - Message}}
  [System](#cfn-bedrock-prompt-chatprompttemplateconfiguration-system): {{
    - SystemContentBlock}}
  [ToolConfiguration](#cfn-bedrock-prompt-chatprompttemplateconfiguration-toolconfiguration): {{
    ToolConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-prompt-chatprompttemplateconfiguration-properties"></a>

`InputVariables`  <a name="cfn-bedrock-prompt-chatprompttemplateconfiguration-inputvariables"></a>
An array of the variables in the prompt template.
*Required*: No
*Type*: Array of [PromptInputVariable](aws-properties-bedrock-prompt-promptinputvariable.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Messages`  <a name="cfn-bedrock-prompt-chatprompttemplateconfiguration-messages"></a>
Contains messages in the chat for the prompt.
*Required*: Yes
*Type*: Array of [Message](aws-properties-bedrock-prompt-message.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`System`  <a name="cfn-bedrock-prompt-chatprompttemplateconfiguration-system"></a>
Contains system prompts to provide context to the model or to describe how it should behave.
*Required*: No
*Type*: Array of [SystemContentBlock](aws-properties-bedrock-prompt-systemcontentblock.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolConfiguration`  <a name="cfn-bedrock-prompt-chatprompttemplateconfiguration-toolconfiguration"></a>
Configuration information for the tools that the model can use when generating a response.
*Required*: No
*Type*: [ToolConfiguration](aws-properties-bedrock-prompt-toolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
