---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscalingplans-scalingplan-applicationsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScalingPlans::ScalingPlan ApplicationSource
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource"></a>

`ApplicationSource` is a property of [ScalingPlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html) that specifies the application source to use with a scaling plan. You can create one scaling plan per application source.

## Syntax
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource-syntax.json"></a>

```
{
  "[CloudFormationStackARN](#cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn)" : {{String}},
  "[TagFilters](#cfn-autoscalingplans-scalingplan-applicationsource-tagfilters)" : {{[ TagFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource-syntax.yaml"></a>

```
  [CloudFormationStackARN](#cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn): {{String}}
  [TagFilters](#cfn-autoscalingplans-scalingplan-applicationsource-tagfilters): {{
    - TagFilter}}
```

## Properties
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource-properties"></a>

`CloudFormationStackARN`  <a name="cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn"></a>
The Amazon Resource Name (ARN) of a CloudFormation stack.
You must specify either a `CloudFormationStackARN` or `TagFilters`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagFilters`  <a name="cfn-autoscalingplans-scalingplan-applicationsource-tagfilters"></a>
A set of tag filters (keys and values). Each tag filter specified must contain a key with values as optional. Each scaling plan can include up to 50 keys, and each key can include up to 20 values.
Tags are part of the syntax that you use to specify the resources you want returned when configuring a scaling plan from the AWS Auto Scaling console. You do not need to specify valid tag filter values when you create a scaling plan with CloudFormation. The `Key` and `Values` properties can accept any value as long as the combination of values is unique across scaling plans. However, if you also want to use the AWS Auto Scaling console to edit the scaling plan, then you must specify valid values.
You must specify either a `CloudFormationStackARN` or `TagFilters`.
*Required*: No
*Type*: Array of [TagFilter](aws-properties-autoscalingplans-scalingplan-tagfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-autoscalingplans-scalingplan-applicationsource--seealso"></a>
+  [Scaling Plans User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
