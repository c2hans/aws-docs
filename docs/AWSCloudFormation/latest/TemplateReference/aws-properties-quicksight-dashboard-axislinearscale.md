---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-axislinearscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard AxisLinearScale
<a name="aws-properties-quicksight-dashboard-axislinearscale"></a>

The liner axis scale setup.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-axislinearscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-axislinearscale-syntax.json"></a>

```
{
  "[StepCount](#cfn-quicksight-dashboard-axislinearscale-stepcount)" : {{Number}},
  "[StepSize](#cfn-quicksight-dashboard-axislinearscale-stepsize)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-axislinearscale-syntax.yaml"></a>

```
  [StepCount](#cfn-quicksight-dashboard-axislinearscale-stepcount): {{Number}}
  [StepSize](#cfn-quicksight-dashboard-axislinearscale-stepsize): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-axislinearscale-properties"></a>

`StepCount`  <a name="cfn-quicksight-dashboard-axislinearscale-stepcount"></a>
The step count setup of a linear axis.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepSize`  <a name="cfn-quicksight-dashboard-axislinearscale-stepsize"></a>
The step size setup of a linear axis.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
