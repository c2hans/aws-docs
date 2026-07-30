---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-timebasedtriggerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory TimeBasedTriggerInput
<a name="aws-properties-bedrockagentcore-memory-timebasedtriggerinput"></a>

The memory trigger condition input for the time based trigger.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-timebasedtriggerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-timebasedtriggerinput-syntax.json"></a>

```
{
  "[IdleSessionTimeout](#cfn-bedrockagentcore-memory-timebasedtriggerinput-idlesessiontimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-timebasedtriggerinput-syntax.yaml"></a>

```
  [IdleSessionTimeout](#cfn-bedrockagentcore-memory-timebasedtriggerinput-idlesessiontimeout): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-timebasedtriggerinput-properties"></a>

`IdleSessionTimeout`  <a name="cfn-bedrockagentcore-memory-timebasedtriggerinput-idlesessiontimeout"></a>
The memory trigger condition input for the session timeout.
*Required*: No
*Type*: Integer
*Minimum*: `10`
*Maximum*: `3000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
