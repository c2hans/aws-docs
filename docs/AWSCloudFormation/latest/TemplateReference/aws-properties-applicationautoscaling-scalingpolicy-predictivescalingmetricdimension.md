---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingMetricDimension
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension"></a>

 Describes the dimension of a metric.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-syntax.json"></a>

```
{
  "[Name](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-name)" : {{String}},
  "[Value](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-syntax.yaml"></a>

```
  [Name](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-name): {{String}}
  [Value](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-value): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-properties"></a>

`Name`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-name"></a>
 The name of the dimension.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension-value"></a>
 The value of the dimension.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
