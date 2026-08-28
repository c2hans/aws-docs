---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscalingplans-scalingplan-metricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScalingPlans::ScalingPlan MetricDimension
<a name="aws-properties-autoscalingplans-scalingplan-metricdimension"></a>

`MetricDimension` is a subproperty of [CustomizedScalingMetricSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html) that specifies a dimension for a customized metric to use with a scaling plan. Dimensions are arbitrary name/value pairs that can be associated with a CloudWatch metric. Duplicate dimensions are not allowed.

## Syntax
<a name="aws-properties-autoscalingplans-scalingplan-metricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscalingplans-scalingplan-metricdimension-syntax.json"></a>

```
{
  "[Name](#cfn-autoscalingplans-scalingplan-metricdimension-name)" : {{String}},
  "[Value](#cfn-autoscalingplans-scalingplan-metricdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscalingplans-scalingplan-metricdimension-syntax.yaml"></a>

```
  [Name](#cfn-autoscalingplans-scalingplan-metricdimension-name): {{String}}
  [Value](#cfn-autoscalingplans-scalingplan-metricdimension-value): {{String}}
```

## Properties
<a name="aws-properties-autoscalingplans-scalingplan-metricdimension-properties"></a>

`Name`  <a name="cfn-autoscalingplans-scalingplan-metricdimension-name"></a>
The name of the dimension.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-autoscalingplans-scalingplan-metricdimension-value"></a>
The value of the dimension.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
