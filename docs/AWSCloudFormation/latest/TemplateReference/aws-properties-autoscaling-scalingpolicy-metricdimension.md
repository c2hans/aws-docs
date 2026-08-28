---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-metricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::ScalingPolicy MetricDimension
<a name="aws-properties-autoscaling-scalingpolicy-metricdimension"></a>

`MetricDimension` specifies a name/value pair that is part of the identity of a CloudWatch metric for the `Dimensions` property of the [AWS::AutoScaling::ScalingPolicy CustomizedMetricSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html) property type. Duplicate dimensions are not allowed.

## Syntax
<a name="aws-properties-autoscaling-scalingpolicy-metricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-scalingpolicy-metricdimension-syntax.json"></a>

```
{
  "[Name](#cfn-autoscaling-scalingpolicy-metricdimension-name)" : {{String}},
  "[Value](#cfn-autoscaling-scalingpolicy-metricdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-scalingpolicy-metricdimension-syntax.yaml"></a>

```
  [Name](#cfn-autoscaling-scalingpolicy-metricdimension-name): {{String}}
  [Value](#cfn-autoscaling-scalingpolicy-metricdimension-value): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-scalingpolicy-metricdimension-properties"></a>

`Name`  <a name="cfn-autoscaling-scalingpolicy-metricdimension-name"></a>
The name of the dimension.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-autoscaling-scalingpolicy-metricdimension-value"></a>
The value of the dimension.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
