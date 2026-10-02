---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessHookEventBridgeTarget
<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget"></a>

<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget-description"></a>The `HarnessHookEventBridgeTarget` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-harness-harnesshookeventbridgetarget-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-harness-harnesshookeventbridgetarget-arn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-harness-harnesshookeventbridgetarget-arn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
