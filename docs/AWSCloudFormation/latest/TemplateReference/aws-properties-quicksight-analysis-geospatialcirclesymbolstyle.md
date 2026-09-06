---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialcirclesymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialCircleSymbolStyle
<a name="aws-properties-quicksight-analysis-geospatialcirclesymbolstyle"></a>

The properties for a circle symbol style.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialcirclesymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialcirclesymbolstyle-syntax.json"></a>

```
{
  "[CircleRadius](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-circleradius)" : {{GeospatialCircleRadius}},
  "[FillColor](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[StrokeColor](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokecolor)" : {{GeospatialColor}},
  "[StrokeWidth](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialcirclesymbolstyle-syntax.yaml"></a>

```
  [CircleRadius](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-circleradius): {{
    GeospatialCircleRadius}}
  [FillColor](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-fillcolor): {{
    GeospatialColor}}
  [StrokeColor](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokecolor): {{
    GeospatialColor}}
  [StrokeWidth](#cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialcirclesymbolstyle-properties"></a>

`CircleRadius`  <a name="cfn-quicksight-analysis-geospatialcirclesymbolstyle-circleradius"></a>
The radius of the circle.
*Required*: No
*Type*: [GeospatialCircleRadius](aws-properties-quicksight-analysis-geospatialcircleradius.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FillColor`  <a name="cfn-quicksight-analysis-geospatialcirclesymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-analysis-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeColor`  <a name="cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokecolor"></a>
The color and opacity values for the stroke color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-analysis-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeWidth`  <a name="cfn-quicksight-analysis-geospatialcirclesymbolstyle-strokewidth"></a>
The width of the stroke (border).
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-analysis-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
