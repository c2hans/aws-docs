---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WaterfallChartAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells"></a>

The field well configuration of a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Breakdowns](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-breakdowns)" : {{[ DimensionField, ... ]}},
  "[Categories](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-categories)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells-syntax.yaml"></a>

```
  [Breakdowns](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-breakdowns): {{
    - DimensionField}}
  [Categories](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-categories): {{
    - DimensionField}}
  [Values](#cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-waterfallchartaggregatedfieldwells-properties"></a>

`Breakdowns`  <a name="cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-breakdowns"></a>
The breakdown field wells of a waterfall visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Categories`  <a name="cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-categories"></a>
The category field wells of a waterfall visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-waterfallchartaggregatedfieldwells-values"></a>
The value field wells of a waterfall visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
