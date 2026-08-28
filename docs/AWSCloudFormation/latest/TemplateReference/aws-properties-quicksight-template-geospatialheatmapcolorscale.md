---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialheatmapcolorscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialHeatmapColorScale
<a name="aws-properties-quicksight-template-geospatialheatmapcolorscale"></a>

The color scale specification for the heatmap point style.

## Syntax
<a name="aws-properties-quicksight-template-geospatialheatmapcolorscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialheatmapcolorscale-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-template-geospatialheatmapcolorscale-colors)" : {{[ GeospatialHeatmapDataColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialheatmapcolorscale-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-template-geospatialheatmapcolorscale-colors): {{
    - GeospatialHeatmapDataColor}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialheatmapcolorscale-properties"></a>

`Colors`  <a name="cfn-quicksight-template-geospatialheatmapcolorscale-colors"></a>
The list of colors to be used in heatmap point style.
*Required*: No
*Type*: Array of [GeospatialHeatmapDataColor](aws-properties-quicksight-template-geospatialheatmapdatacolor.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
