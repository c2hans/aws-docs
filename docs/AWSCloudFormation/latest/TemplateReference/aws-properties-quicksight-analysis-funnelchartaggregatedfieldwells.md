---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FunnelChartAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells"></a>

The field well configuration of a `FunnelChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-funnelchartaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-analysis-funnelchartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-funnelchartaggregatedfieldwells-category): {{
    - DimensionField}}
  [Values](#cfn-quicksight-analysis-funnelchartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-funnelchartaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-funnelchartaggregatedfieldwells-category"></a>
The category field wells of a funnel chart. Values are grouped by category fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-funnelchartaggregatedfieldwells-values"></a>
The value field wells of a funnel chart. Values are aggregated based on categories.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
