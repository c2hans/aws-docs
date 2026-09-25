---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallayerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLayerDefinition
<a name="aws-properties-quicksight-template-geospatiallayerdefinition"></a>

The definition properties for a geospatial layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallayerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallayerdefinition-syntax.json"></a>

```
{
  "[LineLayer](#cfn-quicksight-template-geospatiallayerdefinition-linelayer)" : {{GeospatialLineLayer}},
  "[PointLayer](#cfn-quicksight-template-geospatiallayerdefinition-pointlayer)" : {{GeospatialPointLayer}},
  "[PolygonLayer](#cfn-quicksight-template-geospatiallayerdefinition-polygonlayer)" : {{GeospatialPolygonLayer}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallayerdefinition-syntax.yaml"></a>

```
  [LineLayer](#cfn-quicksight-template-geospatiallayerdefinition-linelayer): {{
    GeospatialLineLayer}}
  [PointLayer](#cfn-quicksight-template-geospatiallayerdefinition-pointlayer): {{
    GeospatialPointLayer}}
  [PolygonLayer](#cfn-quicksight-template-geospatiallayerdefinition-polygonlayer): {{
    GeospatialPolygonLayer}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallayerdefinition-properties"></a>

`LineLayer`  <a name="cfn-quicksight-template-geospatiallayerdefinition-linelayer"></a>
The definition for a line layer.
*Required*: No
*Type*: [GeospatialLineLayer](aws-properties-quicksight-template-geospatiallinelayer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointLayer`  <a name="cfn-quicksight-template-geospatiallayerdefinition-pointlayer"></a>
The definition for a point layer.
*Required*: No
*Type*: [GeospatialPointLayer](aws-properties-quicksight-template-geospatialpointlayer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolygonLayer`  <a name="cfn-quicksight-template-geospatiallayerdefinition-polygonlayer"></a>
The definition for a polygon layer.
*Required*: No
*Type*: [GeospatialPolygonLayer](aws-properties-quicksight-template-geospatialpolygonlayer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
