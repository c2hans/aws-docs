---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialheatmapcolorscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialHeatmapColorScale
<a name="aws-properties-quicksight-dashboard-geospatialheatmapcolorscale"></a>

The color scale specification for the heatmap point style.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialheatmapcolorscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialheatmapcolorscale-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-dashboard-geospatialheatmapcolorscale-colors)" : {{[ GeospatialHeatmapDataColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialheatmapcolorscale-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-dashboard-geospatialheatmapcolorscale-colors): {{
    - GeospatialHeatmapDataColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialheatmapcolorscale-properties"></a>

`Colors`  <a name="cfn-quicksight-dashboard-geospatialheatmapcolorscale-colors"></a>
The list of colors to be used in heatmap point style.
*Required*: No
*Type*: Array of [GeospatialHeatmapDataColor](aws-properties-quicksight-dashboard-geospatialheatmapdatacolor.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
