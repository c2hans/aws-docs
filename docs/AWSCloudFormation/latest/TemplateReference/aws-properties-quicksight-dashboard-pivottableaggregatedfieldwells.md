---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PivotTableAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells"></a>

The aggregated field well for the pivot table.

## Syntax
<a name="aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells-syntax.json"></a>

```
{
  "[Columns](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-columns)" : {{[ DimensionField, ... ]}},
  "[Rows](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-rows)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells-syntax.yaml"></a>

```
  [Columns](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-columns): {{
    - DimensionField}}
  [Rows](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-rows): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-pivottableaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-pivottableaggregatedfieldwells-properties"></a>

`Columns`  <a name="cfn-quicksight-dashboard-pivottableaggregatedfieldwells-columns"></a>
The columns field well for a pivot table. Values are grouped by columns fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rows`  <a name="cfn-quicksight-dashboard-pivottableaggregatedfieldwells-rows"></a>
The rows field well for a pivot table. Values are grouped by rows fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-pivottableaggregatedfieldwells-values"></a>
The values field well for a pivot table. Values are aggregated based on rows and columns fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
