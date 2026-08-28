---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricDimension
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension"></a>

`TargetTrackingMetricDimension` specifies a name/value pair that is part of the identity of a CloudWatch metric for the `Dimensions` property of the [AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetric](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html) property type. Duplicate dimensions are not allowed.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-syntax.json"></a>

```
{
  "[Name](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-name)" : {{String}},
  "[Value](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-syntax.yaml"></a>

```
  [Name](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-name): {{String}}
  [Value](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-value): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-properties"></a>

`Name`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-name"></a>
The name of the dimension.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-value"></a>
The value of the dimension.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
