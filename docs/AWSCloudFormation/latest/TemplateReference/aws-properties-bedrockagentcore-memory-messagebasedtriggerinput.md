---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory MessageBasedTriggerInput
<a name="aws-properties-bedrockagentcore-memory-messagebasedtriggerinput"></a>

The message based trigger input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-messagebasedtriggerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-messagebasedtriggerinput-syntax.json"></a>

```
{
  "[MessageCount](#cfn-bedrockagentcore-memory-messagebasedtriggerinput-messagecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-messagebasedtriggerinput-syntax.yaml"></a>

```
  [MessageCount](#cfn-bedrockagentcore-memory-messagebasedtriggerinput-messagecount): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-messagebasedtriggerinput-properties"></a>

`MessageCount`  <a name="cfn-bedrockagentcore-memory-messagebasedtriggerinput-messagecount"></a>
The memory trigger condition input for the message based trigger message count.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
