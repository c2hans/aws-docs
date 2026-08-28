---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ScatterPlotCategoricallyAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells"></a>

The aggregated field well of a scatter plot.

## Syntax
<a name="aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Label](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-label)" : {{[ DimensionField, ... ]}},
  "[Size](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-size)" : {{[ MeasureField, ... ]}},
  "[XAxis](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-xaxis)" : {{[ MeasureField, ... ]}},
  "[YAxis](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-yaxis)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-category): {{
    - DimensionField}}
  [Label](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-label): {{
    - DimensionField}}
  [Size](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-size): {{
    - MeasureField}}
  [XAxis](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-xaxis): {{
    - MeasureField}}
  [YAxis](#cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-yaxis): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-category"></a>
The category field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-label"></a>
The label field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-size"></a>
The size field well of a scatter plot.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxis`  <a name="cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-xaxis"></a>
The x-axis field well of a scatter plot.
The x-axis is aggregated by category.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxis`  <a name="cfn-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells-yaxis"></a>
The y-axis field well of a scatter plot.
The y-axis is aggregated by category.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
