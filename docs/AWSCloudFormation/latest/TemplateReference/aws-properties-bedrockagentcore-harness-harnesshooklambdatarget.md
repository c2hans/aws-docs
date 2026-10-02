---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesshooklambdatarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessHookLambdaTarget
<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget"></a>

<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget-description"></a>The `HarnessHookLambdaTarget` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-arn)" : {{String}},
  "[FailureMode](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-failuremode)" : {{String}},
  "[TimeoutSeconds](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-timeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-arn): {{String}}
  [FailureMode](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-failuremode): {{String}}
  [TimeoutSeconds](#cfn-bedrockagentcore-harness-harnesshooklambdatarget-timeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesshooklambdatarget-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-harness-harnesshooklambdatarget-arn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureMode`  <a name="cfn-bedrockagentcore-harness-harnesshooklambdatarget-failuremode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `allow | deny`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutSeconds`  <a name="cfn-bedrockagentcore-harness-harnesshooklambdatarget-timeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
