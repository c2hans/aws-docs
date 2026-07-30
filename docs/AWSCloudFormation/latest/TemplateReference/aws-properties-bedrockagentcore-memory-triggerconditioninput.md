---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-triggerconditioninput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory TriggerConditionInput
<a name="aws-properties-bedrockagentcore-memory-triggerconditioninput"></a>

The memory trigger condition input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-triggerconditioninput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-triggerconditioninput-syntax.json"></a>

```
{
  "[MessageBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-messagebasedtrigger)" : {{MessageBasedTriggerInput}},
  "[TimeBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-timebasedtrigger)" : {{TimeBasedTriggerInput}},
  "[TokenBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-tokenbasedtrigger)" : {{TokenBasedTriggerInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-triggerconditioninput-syntax.yaml"></a>

```
  [MessageBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-messagebasedtrigger): {{
    MessageBasedTriggerInput}}
  [TimeBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-timebasedtrigger): {{
    TimeBasedTriggerInput}}
  [TokenBasedTrigger](#cfn-bedrockagentcore-memory-triggerconditioninput-tokenbasedtrigger): {{
    TokenBasedTriggerInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-triggerconditioninput-properties"></a>

`MessageBasedTrigger`  <a name="cfn-bedrockagentcore-memory-triggerconditioninput-messagebasedtrigger"></a>
The memory trigger condition input for the message based trigger.
*Required*: No
*Type*: [MessageBasedTriggerInput](aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeBasedTrigger`  <a name="cfn-bedrockagentcore-memory-triggerconditioninput-timebasedtrigger"></a>
The memory trigger condition input.
*Required*: No
*Type*: [TimeBasedTriggerInput](aws-properties-bedrockagentcore-memory-timebasedtriggerinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenBasedTrigger`  <a name="cfn-bedrockagentcore-memory-triggerconditioninput-tokenbasedtrigger"></a>
The trigger condition information for a token based trigger.
*Required*: No
*Type*: [TokenBasedTriggerInput](aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
