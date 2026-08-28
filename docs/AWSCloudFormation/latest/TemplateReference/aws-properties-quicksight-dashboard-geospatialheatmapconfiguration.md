---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialheatmapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialHeatmapConfiguration
<a name="aws-properties-quicksight-dashboard-geospatialheatmapconfiguration"></a>

The heatmap configuration of the geospatial point style.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialheatmapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialheatmapconfiguration-syntax.json"></a>

```
{
  "[HeatmapColor](#cfn-quicksight-dashboard-geospatialheatmapconfiguration-heatmapcolor)" : {{GeospatialHeatmapColorScale}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialheatmapconfiguration-syntax.yaml"></a>

```
  [HeatmapColor](#cfn-quicksight-dashboard-geospatialheatmapconfiguration-heatmapcolor): {{
    GeospatialHeatmapColorScale}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialheatmapconfiguration-properties"></a>

`HeatmapColor`  <a name="cfn-quicksight-dashboard-geospatialheatmapconfiguration-heatmapcolor"></a>
The color scale specification for the heatmap point style.
*Required*: No
*Type*: [GeospatialHeatmapColorScale](aws-properties-quicksight-dashboard-geospatialheatmapcolorscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
