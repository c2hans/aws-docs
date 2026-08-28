---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscalingplans-scalingplan-tagfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScalingPlans::ScalingPlan TagFilter
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter"></a>

`TagFilter` is a subproperty of [ApplicationSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html) that specifies a tag for an application source to use with a scaling plan.

## Syntax
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter-syntax.json"></a>

```
{
  "[Key](#cfn-autoscalingplans-scalingplan-tagfilter-key)" : {{String}},
  "[Values](#cfn-autoscalingplans-scalingplan-tagfilter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter-syntax.yaml"></a>

```
  [Key](#cfn-autoscalingplans-scalingplan-tagfilter-key): {{String}}
  [Values](#cfn-autoscalingplans-scalingplan-tagfilter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter-properties"></a>

`Key`  <a name="cfn-autoscalingplans-scalingplan-tagfilter-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-autoscalingplans-scalingplan-tagfilter-values"></a>
The tag values (0 to 20).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-autoscalingplans-scalingplan-tagfilter--seealso"></a>
+  [Scaling Plans User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
