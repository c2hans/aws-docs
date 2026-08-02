---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-scalingaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig ScalingAction
<a name="aws-properties-emr-instancegroupconfig-scalingaction"></a>

`ScalingAction` is a subproperty of the `ScalingRule` property type. `ScalingAction` determines the type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-scalingaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-scalingaction-syntax.json"></a>

```
{
  "[Market](#cfn-emr-instancegroupconfig-scalingaction-market)" : {{String}},
  "[SimpleScalingPolicyConfiguration](#cfn-emr-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration)" : {{SimpleScalingPolicyConfiguration}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-scalingaction-syntax.yaml"></a>

```
  [Market](#cfn-emr-instancegroupconfig-scalingaction-market): {{String}}
  [SimpleScalingPolicyConfiguration](#cfn-emr-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration): {{
    SimpleScalingPolicyConfiguration}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-scalingaction-properties"></a>

`Market`  <a name="cfn-emr-instancegroupconfig-scalingaction-market"></a>
Not available for instance groups. Instance groups use the market type specified for the group.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SimpleScalingPolicyConfiguration`  <a name="cfn-emr-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration"></a>
The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
*Required*: Yes
*Type*: [SimpleScalingPolicyConfiguration](aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
