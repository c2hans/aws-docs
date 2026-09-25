---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallinesymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLineSymbolStyle
<a name="aws-properties-quicksight-template-geospatiallinesymbolstyle"></a>

The symbol style for a line layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallinesymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallinesymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-template-geospatiallinesymbolstyle-fillcolor)" : {{GeospatialColor}},
  "[LineWidth](#cfn-quicksight-template-geospatiallinesymbolstyle-linewidth)" : {{GeospatialLineWidth}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallinesymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-template-geospatiallinesymbolstyle-fillcolor): {{
    GeospatialColor}}
  [LineWidth](#cfn-quicksight-template-geospatiallinesymbolstyle-linewidth): {{
    GeospatialLineWidth}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallinesymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-template-geospatiallinesymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: [GeospatialColor](aws-properties-quicksight-template-geospatialcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineWidth`  <a name="cfn-quicksight-template-geospatiallinesymbolstyle-linewidth"></a>
The width value for a line.
*Required*: No
*Type*: [GeospatialLineWidth](aws-properties-quicksight-template-geospatiallinewidth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
