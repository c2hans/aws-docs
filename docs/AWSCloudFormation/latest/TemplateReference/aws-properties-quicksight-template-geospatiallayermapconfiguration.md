---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallayermapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLayerMapConfiguration
<a name="aws-properties-quicksight-template-geospatiallayermapconfiguration"></a>

The map definition that defines map state, map style, and geospatial layers.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallayermapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallayermapconfiguration-syntax.json"></a>

```
{
  "[Interactions](#cfn-quicksight-template-geospatiallayermapconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-template-geospatiallayermapconfiguration-legend)" : {{LegendOptions}},
  "[MapLayers](#cfn-quicksight-template-geospatiallayermapconfiguration-maplayers)" : {{[ GeospatialLayerItem, ... ]}},
  "[MapState](#cfn-quicksight-template-geospatiallayermapconfiguration-mapstate)" : {{GeospatialMapState}},
  "[MapStyle](#cfn-quicksight-template-geospatiallayermapconfiguration-mapstyle)" : {{GeospatialMapStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallayermapconfiguration-syntax.yaml"></a>

```
  [Interactions](#cfn-quicksight-template-geospatiallayermapconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-template-geospatiallayermapconfiguration-legend): {{
    LegendOptions}}
  [MapLayers](#cfn-quicksight-template-geospatiallayermapconfiguration-maplayers): {{
    - GeospatialLayerItem}}
  [MapState](#cfn-quicksight-template-geospatiallayermapconfiguration-mapstate): {{
    GeospatialMapState}}
  [MapStyle](#cfn-quicksight-template-geospatiallayermapconfiguration-mapstyle): {{
    GeospatialMapStyle}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallayermapconfiguration-properties"></a>

`Interactions`  <a name="cfn-quicksight-template-geospatiallayermapconfiguration-interactions"></a>
Property description not available.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-template-geospatiallayermapconfiguration-legend"></a>
Property description not available.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-template-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapLayers`  <a name="cfn-quicksight-template-geospatiallayermapconfiguration-maplayers"></a>
The geospatial layers to visualize on the map.
*Required*: No
*Type*: Array of [GeospatialLayerItem](aws-properties-quicksight-template-geospatiallayeritem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapState`  <a name="cfn-quicksight-template-geospatiallayermapconfiguration-mapstate"></a>
The map state properties for the map.
*Required*: No
*Type*: [GeospatialMapState](aws-properties-quicksight-template-geospatialmapstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapStyle`  <a name="cfn-quicksight-template-geospatiallayermapconfiguration-mapstyle"></a>
The map style properties for the map.
*Required*: No
*Type*: [GeospatialMapStyle](aws-properties-quicksight-template-geospatialmapstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
