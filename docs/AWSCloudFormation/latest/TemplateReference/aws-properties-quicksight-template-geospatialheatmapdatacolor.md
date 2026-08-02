---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialheatmapdatacolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialHeatmapDataColor
<a name="aws-properties-quicksight-template-geospatialheatmapdatacolor"></a>

The color to be used in the heatmap point style.

## Syntax
<a name="aws-properties-quicksight-template-geospatialheatmapdatacolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialheatmapdatacolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-geospatialheatmapdatacolor-color)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialheatmapdatacolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-geospatialheatmapdatacolor-color): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialheatmapdatacolor-properties"></a>

`Color`  <a name="cfn-quicksight-template-geospatialheatmapdatacolor-color"></a>
The hex color to be used in the heatmap point style.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
