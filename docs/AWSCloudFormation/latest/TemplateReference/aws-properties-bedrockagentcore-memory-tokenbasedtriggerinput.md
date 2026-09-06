---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory TokenBasedTriggerInput
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput"></a>

The token based trigger input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax.json"></a>

```
{
  "[TokenCount](#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax.yaml"></a>

```
  [TokenCount](#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-properties"></a>

`TokenCount`  <a name="cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount"></a>
The token based trigger token count.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `500000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
