---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-barchartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard BarChartAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-barchartaggregatedfieldwells"></a>

The aggregated field wells of a bar chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-barchartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-barchartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Colors](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-colors)" : {{[ DimensionField, ... ]}},
  "[SmallMultiples](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-smallmultiples)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-barchartaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-category): {{
    - DimensionField}}
  [Colors](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-colors): {{
    - DimensionField}}
  [SmallMultiples](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-smallmultiples): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-barchartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-barchartaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-dashboard-barchartaggregatedfieldwells-category"></a>
The category (y-axis) field well of a bar chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Colors`  <a name="cfn-quicksight-dashboard-barchartaggregatedfieldwells-colors"></a>
The color (group/color) field well of a bar chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiples`  <a name="cfn-quicksight-dashboard-barchartaggregatedfieldwells-smallmultiples"></a>
The small multiples field well of a bar chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-barchartaggregatedfieldwells-values"></a>
The value field wells of a bar chart. Values are aggregated by category.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
