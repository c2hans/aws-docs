---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialPolygonSymbolStyle
<a name="aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle"></a>

The polygon symbol style for a polygon layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[StrokeColor](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokecolor)" : {{GeospatialColor}},
  "[StrokeWidth](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-fillcolor): {{
    GeospatialColor}}
  [StrokeColor](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokecolor): {{
    GeospatialColor}}
  [StrokeWidth](#cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialpolygonsymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-analysis-geospatialpolygonsymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-analysis-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeColor`  <a name="cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokecolor"></a>
The color and opacity values for the stroke color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-analysis-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeWidth`  <a name="cfn-quicksight-analysis-geospatialpolygonsymbolstyle-strokewidth"></a>
The width of the border stroke.
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-analysis-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
