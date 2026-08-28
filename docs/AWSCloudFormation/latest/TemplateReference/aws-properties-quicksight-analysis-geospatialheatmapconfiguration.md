---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialheatmapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialHeatmapConfiguration
<a name="aws-properties-quicksight-analysis-geospatialheatmapconfiguration"></a>

The heatmap configuration of the geospatial point style.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialheatmapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialheatmapconfiguration-syntax.json"></a>

```
{
  "[HeatmapColor](#cfn-quicksight-analysis-geospatialheatmapconfiguration-heatmapcolor)" : {{GeospatialHeatmapColorScale}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialheatmapconfiguration-syntax.yaml"></a>

```
  [HeatmapColor](#cfn-quicksight-analysis-geospatialheatmapconfiguration-heatmapcolor): {{
    GeospatialHeatmapColorScale}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialheatmapconfiguration-properties"></a>

`HeatmapColor`  <a name="cfn-quicksight-analysis-geospatialheatmapconfiguration-heatmapcolor"></a>
The color scale specification for the heatmap point style.
*Required*: No
*Type*: [GeospatialHeatmapColorScale](aws-properties-quicksight-analysis-geospatialheatmapcolorscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
