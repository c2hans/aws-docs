---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ScatterPlotCategoricallyAggregatedFieldWells
<a name="aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells"></a>

The aggregated field well of a scatter plot.

## Syntax
<a name="aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Label](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-label)" : {{[ DimensionField, ... ]}},
  "[Size](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-size)" : {{[ MeasureField, ... ]}},
  "[XAxis](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-xaxis)" : {{[ MeasureField, ... ]}},
  "[YAxis](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-yaxis)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-category): {{
    - DimensionField}}
  [Label](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-label): {{
    - DimensionField}}
  [Size](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-size): {{
    - MeasureField}}
  [XAxis](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-xaxis): {{
    - MeasureField}}
  [YAxis](#cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-yaxis): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-category"></a>
The category field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-label"></a>
The label field well of a scatter plot.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-size"></a>
The size field well of a scatter plot.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxis`  <a name="cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-xaxis"></a>
The x-axis field well of a scatter plot.
The x-axis is aggregated by category.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxis`  <a name="cfn-quicksight-template-scatterplotcategoricallyaggregatedfieldwells-yaxis"></a>
The y-axis field well of a scatter plot.
The y-axis is aggregated by category.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
