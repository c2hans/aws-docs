---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatiallinesymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialLineSymbolStyle
<a name="aws-properties-quicksight-dashboard-geospatiallinesymbolstyle"></a>

The symbol style for a line layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatiallinesymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatiallinesymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-dashboard-geospatiallinesymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[LineWidth](#cfn-quicksight-dashboard-geospatiallinesymbolstyle-linewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatiallinesymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-dashboard-geospatiallinesymbolstyle-fillcolor): {{
    GeospatialColor}}
  [LineWidth](#cfn-quicksight-dashboard-geospatiallinesymbolstyle-linewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatiallinesymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-dashboard-geospatiallinesymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-dashboard-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineWidth`  <a name="cfn-quicksight-dashboard-geospatiallinesymbolstyle-linewidth"></a>
The width value for a line.
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-dashboard-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
