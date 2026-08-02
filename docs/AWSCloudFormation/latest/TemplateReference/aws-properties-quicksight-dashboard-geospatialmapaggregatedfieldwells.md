---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialMapAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells"></a>

The aggregated field wells for a geospatial map.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-colors)" : {{[ DimensionField, ... ]}},
  "[Geospatial](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-geospatial)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-colors): {{
    - DimensionField}}
  [Geospatial](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-geospatial): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialmapaggregatedfieldwells-properties"></a>

`Colors`  <a name="cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-colors"></a>
The color field wells of a geospatial map.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Geospatial`  <a name="cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-geospatial"></a>
The geospatial field wells of a geospatial map. Values are grouped by geospatial fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-geospatialmapaggregatedfieldwells-values"></a>
The size field wells of a geospatial map. Values are aggregated based on geospatial fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
