---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration AutoScalingGroup
<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup"></a>

<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup-description"></a>The `AutoScalingGroup` property type specifies Property description not available. for an [AWS::ImageBuilder::InfrastructureConfiguration](aws-resource-imagebuilder-infrastructureconfiguration.md).

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup-syntax.json"></a>

```
{
  "[CapacityWaitTimeoutSeconds](#cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-capacitywaittimeoutseconds)" : {{Integer}},
  "[Name](#cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup-syntax.yaml"></a>

```
  [CapacityWaitTimeoutSeconds](#cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-capacitywaittimeoutseconds): {{Integer}}
  [Name](#cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-name): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-autoscalinggroup-properties"></a>

`CapacityWaitTimeoutSeconds`  <a name="cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-capacitywaittimeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-infrastructureconfiguration-autoscalinggroup-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
