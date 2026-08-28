---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-chartaxislabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ChartAxisLabelOptions
<a name="aws-properties-quicksight-analysis-chartaxislabeloptions"></a>

The label options for an axis on a chart.

## Syntax
<a name="aws-properties-quicksight-analysis-chartaxislabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-chartaxislabeloptions-syntax.json"></a>

```
{
  "[AxisLabelOptions](#cfn-quicksight-analysis-chartaxislabeloptions-axislabeloptions)" : {{[ AxisLabelOptions, ... ]}},
  "[SortIconVisibility](#cfn-quicksight-analysis-chartaxislabeloptions-sorticonvisibility)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-chartaxislabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-chartaxislabeloptions-syntax.yaml"></a>

```
  [AxisLabelOptions](#cfn-quicksight-analysis-chartaxislabeloptions-axislabeloptions): {{
    - AxisLabelOptions}}
  [SortIconVisibility](#cfn-quicksight-analysis-chartaxislabeloptions-sorticonvisibility): {{String}}
  [Visibility](#cfn-quicksight-analysis-chartaxislabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-chartaxislabeloptions-properties"></a>

`AxisLabelOptions`  <a name="cfn-quicksight-analysis-chartaxislabeloptions-axislabeloptions"></a>
The label options for a chart axis.
*Required*: No
*Type*: [Array](aws-properties-quicksight-analysis-axislabeloptions.md) of [AxisLabelOptions](aws-properties-quicksight-analysis-axislabeloptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortIconVisibility`  <a name="cfn-quicksight-analysis-chartaxislabeloptions-sorticonvisibility"></a>
The visibility configuration of the sort icon on a chart's axis label.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-chartaxislabeloptions-visibility"></a>
The visibility of an axis label on a chart. Choose one of the following options:
+ `VISIBLE`: Shows the axis.
+ `HIDDEN`: Hides the axis.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
