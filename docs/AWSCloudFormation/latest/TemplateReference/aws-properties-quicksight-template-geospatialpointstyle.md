---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialpointstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialPointStyle
<a name="aws-properties-quicksight-template-geospatialpointstyle"></a>

The point style for a point layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatialpointstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialpointstyle-syntax.json"></a>

```
{
  "[CircleSymbolStyle](#cfn-quicksight-template-geospatialpointstyle-circlesymbolstyle)" : {{GeospatialCircleSymbolStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialpointstyle-syntax.yaml"></a>

```
  [CircleSymbolStyle](#cfn-quicksight-template-geospatialpointstyle-circlesymbolstyle): {{
    GeospatialCircleSymbolStyle}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialpointstyle-properties"></a>

`CircleSymbolStyle`  <a name="cfn-quicksight-template-geospatialpointstyle-circlesymbolstyle"></a>
The circle symbol style for a point layer.
*Required*: No
*Type*: [GeospatialCircleSymbolStyle](aws-properties-quicksight-template-geospatialcirclesymbolstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
