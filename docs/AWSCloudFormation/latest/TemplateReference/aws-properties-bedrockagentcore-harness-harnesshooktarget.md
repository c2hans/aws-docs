---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesshooktarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessHookTarget
<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget"></a>

<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget-description"></a>The `HarnessHookTarget` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget-syntax.json"></a>

```
{
  "[EventBridge](#cfn-bedrockagentcore-harness-harnesshooktarget-eventbridge)" : {{HarnessHookEventBridgeTarget}},
  "[Lambda](#cfn-bedrockagentcore-harness-harnesshooktarget-lambda)" : {{HarnessHookLambdaTarget}},
  "[Sns](#cfn-bedrockagentcore-harness-harnesshooktarget-sns)" : {{HarnessHookSnsTarget}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget-syntax.yaml"></a>

```
  [EventBridge](#cfn-bedrockagentcore-harness-harnesshooktarget-eventbridge): {{
    HarnessHookEventBridgeTarget}}
  [Lambda](#cfn-bedrockagentcore-harness-harnesshooktarget-lambda): {{
    HarnessHookLambdaTarget}}
  [Sns](#cfn-bedrockagentcore-harness-harnesshooktarget-sns): {{
    HarnessHookSnsTarget}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesshooktarget-properties"></a>

`EventBridge`  <a name="cfn-bedrockagentcore-harness-harnesshooktarget-eventbridge"></a>
Property description not available.
*Required*: No
*Type*: [HarnessHookEventBridgeTarget](aws-properties-bedrockagentcore-harness-harnesshookeventbridgetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lambda`  <a name="cfn-bedrockagentcore-harness-harnesshooktarget-lambda"></a>
Property description not available.
*Required*: No
*Type*: [HarnessHookLambdaTarget](aws-properties-bedrockagentcore-harness-harnesshooklambdatarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sns`  <a name="cfn-bedrockagentcore-harness-harnesshooktarget-sns"></a>
Property description not available.
*Required*: No
*Type*: [HarnessHookSnsTarget](aws-properties-bedrockagentcore-harness-harnesshooksnstarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
