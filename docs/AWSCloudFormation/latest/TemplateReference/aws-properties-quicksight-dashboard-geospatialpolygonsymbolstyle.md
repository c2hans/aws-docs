---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialPolygonSymbolStyle
<a name="aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle"></a>

The polygon symbol style for a polygon layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[StrokeColor](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokecolor)" : {{GeospatialColor}},
  "[StrokeWidth](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-fillcolor): {{
    GeospatialColor}}
  [StrokeColor](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokecolor): {{
    GeospatialColor}}
  [StrokeWidth](#cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialpolygonsymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-dashboard-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeColor`  <a name="cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokecolor"></a>
The color and opacity values for the stroke color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-dashboard-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeWidth`  <a name="cfn-quicksight-dashboard-geospatialpolygonsymbolstyle-strokewidth"></a>
The width of the border stroke.
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-dashboard-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
