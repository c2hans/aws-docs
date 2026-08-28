---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-axisscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis AxisScale
<a name="aws-properties-quicksight-analysis-axisscale"></a>

The scale setup options for a numeric axis display.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-axisscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-axisscale-syntax.json"></a>

```
{
  "[Linear](#cfn-quicksight-analysis-axisscale-linear)" : {{AxisLinearScale}},
  "[Logarithmic](#cfn-quicksight-analysis-axisscale-logarithmic)" : {{AxisLogarithmicScale}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-axisscale-syntax.yaml"></a>

```
  [Linear](#cfn-quicksight-analysis-axisscale-linear): {{
    AxisLinearScale}}
  [Logarithmic](#cfn-quicksight-analysis-axisscale-logarithmic): {{
    AxisLogarithmicScale}}
```

## Properties
<a name="aws-properties-quicksight-analysis-axisscale-properties"></a>

`Linear`  <a name="cfn-quicksight-analysis-axisscale-linear"></a>
The linear axis scale setup.
*Required*: No
*Type*: [AxisLinearScale](aws-properties-quicksight-analysis-axislinearscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logarithmic`  <a name="cfn-quicksight-analysis-axisscale-logarithmic"></a>
The logarithmic axis scale setup.
*Required*: No
*Type*: [AxisLogarithmicScale](aws-properties-quicksight-analysis-axislogarithmicscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
