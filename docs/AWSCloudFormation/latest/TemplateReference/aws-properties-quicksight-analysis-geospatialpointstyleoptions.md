---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialpointstyleoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialPointStyleOptions
<a name="aws-properties-quicksight-analysis-geospatialpointstyleoptions"></a>

The point style of the geospatial map.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialpointstyleoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialpointstyleoptions-syntax.json"></a>

```
{
  "[ClusterMarkerConfiguration](#cfn-quicksight-analysis-geospatialpointstyleoptions-clustermarkerconfiguration)" : {{ClusterMarkerConfiguration}},
  "[HeatmapConfiguration](#cfn-quicksight-analysis-geospatialpointstyleoptions-heatmapconfiguration)" : {{GeospatialHeatmapConfiguration}},
  "[SelectedPointStyle](#cfn-quicksight-analysis-geospatialpointstyleoptions-selectedpointstyle)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialpointstyleoptions-syntax.yaml"></a>

```
  [ClusterMarkerConfiguration](#cfn-quicksight-analysis-geospatialpointstyleoptions-clustermarkerconfiguration): {{
    ClusterMarkerConfiguration}}
  [HeatmapConfiguration](#cfn-quicksight-analysis-geospatialpointstyleoptions-heatmapconfiguration): {{
    GeospatialHeatmapConfiguration}}
  [SelectedPointStyle](#cfn-quicksight-analysis-geospatialpointstyleoptions-selectedpointstyle): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialpointstyleoptions-properties"></a>

`ClusterMarkerConfiguration`  <a name="cfn-quicksight-analysis-geospatialpointstyleoptions-clustermarkerconfiguration"></a>
The cluster marker configuration of the geospatial point style.
*Required*: No
*Type*: [ClusterMarkerConfiguration](aws-properties-quicksight-analysis-clustermarkerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeatmapConfiguration`  <a name="cfn-quicksight-analysis-geospatialpointstyleoptions-heatmapconfiguration"></a>
The heatmap configuration of the geospatial point style.
*Required*: No
*Type*: [GeospatialHeatmapConfiguration](aws-properties-quicksight-analysis-geospatialheatmapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedPointStyle`  <a name="cfn-quicksight-analysis-geospatialpointstyleoptions-selectedpointstyle"></a>
The selected point styles (point, cluster) of the geospatial map.
*Required*: No
*Type*: String
*Allowed values*: `POINT | CLUSTER | HEATMAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
