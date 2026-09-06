---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filledmapaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilledMapAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-filledmapaggregatedfieldwells"></a>

The aggregated field well of the filled map.

## Syntax
<a name="aws-properties-quicksight-analysis-filledmapaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filledmapaggregatedfieldwells-syntax.json"></a>

```
{
  "[Geospatial](#cfn-quicksight-analysis-filledmapaggregatedfieldwells-geospatial)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-analysis-filledmapaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filledmapaggregatedfieldwells-syntax.yaml"></a>

```
  [Geospatial](#cfn-quicksight-analysis-filledmapaggregatedfieldwells-geospatial): {{
    - DimensionField}}
  [Values](#cfn-quicksight-analysis-filledmapaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filledmapaggregatedfieldwells-properties"></a>

`Geospatial`  <a name="cfn-quicksight-analysis-filledmapaggregatedfieldwells-geospatial"></a>
The aggregated location field well of the filled map. Values are grouped by location fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-analysis-filledmapaggregatedfieldwells-values"></a>
The aggregated color field well of a filled map. Values are aggregated based on location fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
