---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesshooksnstarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessHookSnsTarget
<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget"></a>

<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget-description"></a>The `HarnessHookSnsTarget` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Harness](aws-resource-bedrockagentcore-harness.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-harness-harnesshooksnstarget-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-harness-harnesshooksnstarget-arn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesshooksnstarget-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-harness-harnesshooksnstarget-arn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
