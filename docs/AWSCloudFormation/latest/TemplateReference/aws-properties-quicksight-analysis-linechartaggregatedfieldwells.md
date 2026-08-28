---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-linechartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LineChartAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-linechartaggregatedfieldwells"></a>

The field well configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-analysis-linechartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-linechartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-linechartaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Colors](#cfn-quicksight-analysis-linechartaggregatedfieldwells-colors)" : {{[ DimensionField, ... ]}},
  "[SmallMultiples](#cfn-quicksight-analysis-linechartaggregatedfieldwells-smallmultiples)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-analysis-linechartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-linechartaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-linechartaggregatedfieldwells-category): {{
    - DimensionField}}
  [Colors](#cfn-quicksight-analysis-linechartaggregatedfieldwells-colors): {{
    - DimensionField}}
  [SmallMultiples](#cfn-quicksight-analysis-linechartaggregatedfieldwells-smallmultiples): {{
    - DimensionField}}
  [Values](#cfn-quicksight-analysis-linechartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-linechartaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-linechartaggregatedfieldwells-category"></a>
The category field wells of a line chart. Values are grouped by category fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Colors`  <a name="cfn-quicksight-analysis-linechartaggregatedfieldwells-colors"></a>
The color field wells of a line chart. Values are grouped by category fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiples`  <a name="cfn-quicksight-analysis-linechartaggregatedfieldwells-smallmultiples"></a>
The small multiples field well of a line chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-linechartaggregatedfieldwells-values"></a>
The value field wells of a line chart. Values are aggregated based on categories.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
