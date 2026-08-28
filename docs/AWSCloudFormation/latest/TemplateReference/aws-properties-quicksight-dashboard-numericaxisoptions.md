---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-numericaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard NumericAxisOptions
<a name="aws-properties-quicksight-dashboard-numericaxisoptions"></a>

The options for an axis with a numeric field.

## Syntax
<a name="aws-properties-quicksight-dashboard-numericaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-numericaxisoptions-syntax.json"></a>

```
{
  "[Range](#cfn-quicksight-dashboard-numericaxisoptions-range)" : {{AxisDisplayRange}},
  "[Scale](#cfn-quicksight-dashboard-numericaxisoptions-scale)" : {{AxisScale}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-numericaxisoptions-syntax.yaml"></a>

```
  [Range](#cfn-quicksight-dashboard-numericaxisoptions-range): {{
    AxisDisplayRange}}
  [Scale](#cfn-quicksight-dashboard-numericaxisoptions-scale): {{
    AxisScale}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-numericaxisoptions-properties"></a>

`Range`  <a name="cfn-quicksight-dashboard-numericaxisoptions-range"></a>
The range setup of a numeric axis.
*Required*: No
*Type*: [AxisDisplayRange](aws-properties-quicksight-dashboard-axisdisplayrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scale`  <a name="cfn-quicksight-dashboard-numericaxisoptions-scale"></a>
The scale setup of a numeric axis.
*Required*: No
*Type*: [AxisScale](aws-properties-quicksight-dashboard-axisscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
