---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialcirclesymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialCircleSymbolStyle
<a name="aws-properties-quicksight-template-geospatialcirclesymbolstyle"></a>

The properties for a circle symbol style.

## Syntax
<a name="aws-properties-quicksight-template-geospatialcirclesymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialcirclesymbolstyle-syntax.json"></a>

```
{
  "[CircleRadius](#cfn-quicksight-template-geospatialcirclesymbolstyle-circleradius)" : {{GeospatialCircleRadius}},
  "[FillColor](#cfn-quicksight-template-geospatialcirclesymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[StrokeColor](#cfn-quicksight-template-geospatialcirclesymbolstyle-strokecolor)" : {{GeospatialColor}},
  "[StrokeWidth](#cfn-quicksight-template-geospatialcirclesymbolstyle-strokewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialcirclesymbolstyle-syntax.yaml"></a>

```
  [CircleRadius](#cfn-quicksight-template-geospatialcirclesymbolstyle-circleradius): {{
    GeospatialCircleRadius}}
  [FillColor](#cfn-quicksight-template-geospatialcirclesymbolstyle-fillcolor): {{
    GeospatialColor}}
  [StrokeColor](#cfn-quicksight-template-geospatialcirclesymbolstyle-strokecolor): {{
    GeospatialColor}}
  [StrokeWidth](#cfn-quicksight-template-geospatialcirclesymbolstyle-strokewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialcirclesymbolstyle-properties"></a>

`CircleRadius`  <a name="cfn-quicksight-template-geospatialcirclesymbolstyle-circleradius"></a>
The radius of the circle.
*Required*: No
*Type*: [GeospatialCircleRadius](aws-properties-quicksight-template-geospatialcircleradius.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FillColor`  <a name="cfn-quicksight-template-geospatialcirclesymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-template-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeColor`  <a name="cfn-quicksight-template-geospatialcirclesymbolstyle-strokecolor"></a>
The color and opacity values for the stroke color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-template-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeWidth`  <a name="cfn-quicksight-template-geospatialcirclesymbolstyle-strokewidth"></a>
The width of the stroke (border).
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-template-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
