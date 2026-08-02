---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatiallinesymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialLineSymbolStyle
<a name="aws-properties-quicksight-analysis-geospatiallinesymbolstyle"></a>

The symbol style for a line layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatiallinesymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatiallinesymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-analysis-geospatiallinesymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[LineWidth](#cfn-quicksight-analysis-geospatiallinesymbolstyle-linewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatiallinesymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-analysis-geospatiallinesymbolstyle-fillcolor): {{
    GeospatialColor}}
  [LineWidth](#cfn-quicksight-analysis-geospatiallinesymbolstyle-linewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatiallinesymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-analysis-geospatiallinesymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-analysis-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineWidth`  <a name="cfn-quicksight-analysis-geospatiallinesymbolstyle-linewidth"></a>
The width value for a line.
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-analysis-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
