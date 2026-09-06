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
