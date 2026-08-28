---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialpointstyleoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialPointStyleOptions
<a name="aws-properties-quicksight-dashboard-geospatialpointstyleoptions"></a>

The point style of the geospatial map.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialpointstyleoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialpointstyleoptions-syntax.json"></a>

```
{
  "[ClusterMarkerConfiguration](#cfn-quicksight-dashboard-geospatialpointstyleoptions-clustermarkerconfiguration)" : {{ClusterMarkerConfiguration}},
  "[HeatmapConfiguration](#cfn-quicksight-dashboard-geospatialpointstyleoptions-heatmapconfiguration)" : {{GeospatialHeatmapConfiguration}},
  "[SelectedPointStyle](#cfn-quicksight-dashboard-geospatialpointstyleoptions-selectedpointstyle)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialpointstyleoptions-syntax.yaml"></a>

```
  [ClusterMarkerConfiguration](#cfn-quicksight-dashboard-geospatialpointstyleoptions-clustermarkerconfiguration): {{
    ClusterMarkerConfiguration}}
  [HeatmapConfiguration](#cfn-quicksight-dashboard-geospatialpointstyleoptions-heatmapconfiguration): {{
    GeospatialHeatmapConfiguration}}
  [SelectedPointStyle](#cfn-quicksight-dashboard-geospatialpointstyleoptions-selectedpointstyle): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialpointstyleoptions-properties"></a>

`ClusterMarkerConfiguration`  <a name="cfn-quicksight-dashboard-geospatialpointstyleoptions-clustermarkerconfiguration"></a>
The cluster marker configuration of the geospatial point style.
*Required*: No
*Type*: [ClusterMarkerConfiguration](aws-properties-quicksight-dashboard-clustermarkerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeatmapConfiguration`  <a name="cfn-quicksight-dashboard-geospatialpointstyleoptions-heatmapconfiguration"></a>
The heatmap configuration of the geospatial point style.
*Required*: No
*Type*: [GeospatialHeatmapConfiguration](aws-properties-quicksight-dashboard-geospatialheatmapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedPointStyle`  <a name="cfn-quicksight-dashboard-geospatialpointstyleoptions-selectedpointstyle"></a>
The selected point styles (point, cluster) of the geospatial map.
*Required*: No
*Type*: String
*Allowed values*: `POINT | CLUSTER | HEATMAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
