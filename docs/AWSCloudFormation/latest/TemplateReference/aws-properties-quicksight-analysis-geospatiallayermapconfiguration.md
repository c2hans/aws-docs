---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatiallayermapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialLayerMapConfiguration
<a name="aws-properties-quicksight-analysis-geospatiallayermapconfiguration"></a>

The map definition that defines map state, map style, and geospatial layers.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatiallayermapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatiallayermapconfiguration-syntax.json"></a>

```
{
  "[Interactions](#cfn-quicksight-analysis-geospatiallayermapconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-analysis-geospatiallayermapconfiguration-legend)" : {{LegendOptions}},
  "[MapLayers](#cfn-quicksight-analysis-geospatiallayermapconfiguration-maplayers)" : {{[ GeospatialLayerItem, ... ]}},
  "[MapState](#cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstate)" : {{GeospatialMapState}},
  "[MapStyle](#cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstyle)" : {{GeospatialMapStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatiallayermapconfiguration-syntax.yaml"></a>

```
  [Interactions](#cfn-quicksight-analysis-geospatiallayermapconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-analysis-geospatiallayermapconfiguration-legend): {{
    LegendOptions}}
  [MapLayers](#cfn-quicksight-analysis-geospatiallayermapconfiguration-maplayers): {{
    - GeospatialLayerItem}}
  [MapState](#cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstate): {{
    GeospatialMapState}}
  [MapStyle](#cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstyle): {{
    GeospatialMapStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatiallayermapconfiguration-properties"></a>

`Interactions`  <a name="cfn-quicksight-analysis-geospatiallayermapconfiguration-interactions"></a>
Property description not available.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-analysis-geospatiallayermapconfiguration-legend"></a>
Property description not available.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-analysis-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapLayers`  <a name="cfn-quicksight-analysis-geospatiallayermapconfiguration-maplayers"></a>
The geospatial layers to visualize on the map.
*Required*: No
*Type*: Array of [GeospatialLayerItem](aws-properties-quicksight-analysis-geospatiallayeritem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapState`  <a name="cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstate"></a>
The map state properties for the map.
*Required*: No
*Type*: [GeospatialMapState](aws-properties-quicksight-analysis-geospatialmapstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapStyle`  <a name="cfn-quicksight-analysis-geospatiallayermapconfiguration-mapstyle"></a>
The map style properties for the map.
*Required*: No
*Type*: [GeospatialMapStyle](aws-properties-quicksight-analysis-geospatialmapstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
