---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSlidingWindowConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration"></a>

Configuration for sliding window truncation strategy.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration-syntax.json"></a>

```
{
  "[MessagesCount](#cfn-bedrockagentcore-harness-harnessslidingwindowconfiguration-messagescount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration-syntax.yaml"></a>

```
  [MessagesCount](#cfn-bedrockagentcore-harness-harnessslidingwindowconfiguration-messagescount): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration-properties"></a>

`MessagesCount`  <a name="cfn-bedrockagentcore-harness-harnessslidingwindowconfiguration-messagescount"></a>
The number of recent messages to retain in the context window.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
