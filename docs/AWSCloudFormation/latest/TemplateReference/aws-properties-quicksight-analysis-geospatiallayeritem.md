---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatiallayeritem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialLayerItem
<a name="aws-properties-quicksight-analysis-geospatiallayeritem"></a>

The properties for a single geospatial layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatiallayeritem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatiallayeritem-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-analysis-geospatiallayeritem-actions)" : {{[ LayerCustomAction, ... ]}},
  "[DataSource](#cfn-quicksight-analysis-geospatiallayeritem-datasource)" : {{GeospatialDataSourceItem}},
  "[JoinDefinition](#cfn-quicksight-analysis-geospatiallayeritem-joindefinition)" : {{GeospatialLayerJoinDefinition}},
  "[Label](#cfn-quicksight-analysis-geospatiallayeritem-label)" : {{String}},
  "[LayerDefinition](#cfn-quicksight-analysis-geospatiallayeritem-layerdefinition)" : {{GeospatialLayerDefinition}},
  "[LayerId](#cfn-quicksight-analysis-geospatiallayeritem-layerid)" : {{String}},
  "[LayerType](#cfn-quicksight-analysis-geospatiallayeritem-layertype)" : {{String}},
  "[Tooltip](#cfn-quicksight-analysis-geospatiallayeritem-tooltip)" : {{TooltipOptions}},
  "[Visibility](#cfn-quicksight-analysis-geospatiallayeritem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatiallayeritem-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-analysis-geospatiallayeritem-actions): {{
    - LayerCustomAction}}
  [DataSource](#cfn-quicksight-analysis-geospatiallayeritem-datasource): {{
    GeospatialDataSourceItem}}
  [JoinDefinition](#cfn-quicksight-analysis-geospatiallayeritem-joindefinition): {{
    GeospatialLayerJoinDefinition}}
  [Label](#cfn-quicksight-analysis-geospatiallayeritem-label): {{String}}
  [LayerDefinition](#cfn-quicksight-analysis-geospatiallayeritem-layerdefinition): {{
    GeospatialLayerDefinition}}
  [LayerId](#cfn-quicksight-analysis-geospatiallayeritem-layerid): {{String}}
  [LayerType](#cfn-quicksight-analysis-geospatiallayeritem-layertype): {{String}}
  [Tooltip](#cfn-quicksight-analysis-geospatiallayeritem-tooltip): {{
    TooltipOptions}}
  [Visibility](#cfn-quicksight-analysis-geospatiallayeritem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatiallayeritem-properties"></a>

`Actions`  <a name="cfn-quicksight-analysis-geospatiallayeritem-actions"></a>
A list of custom actions for a layer.
*Required*: No
*Type*: Array of [LayerCustomAction](aws-properties-quicksight-analysis-layercustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSource`  <a name="cfn-quicksight-analysis-geospatiallayeritem-datasource"></a>
The data source for the layer.
*Required*: No
*Type*: [GeospatialDataSourceItem](aws-properties-quicksight-analysis-geospatialdatasourceitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinDefinition`  <a name="cfn-quicksight-analysis-geospatiallayeritem-joindefinition"></a>
The join definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerJoinDefinition](aws-properties-quicksight-analysis-geospatiallayerjoindefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-analysis-geospatiallayeritem-label"></a>
The label that is displayed for the layer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerDefinition`  <a name="cfn-quicksight-analysis-geospatiallayeritem-layerdefinition"></a>
The definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerDefinition](aws-properties-quicksight-analysis-geospatiallayerdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerId`  <a name="cfn-quicksight-analysis-geospatiallayeritem-layerid"></a>
The ID of the layer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerType`  <a name="cfn-quicksight-analysis-geospatiallayeritem-layertype"></a>
The layer type.
*Required*: No
*Type*: String
*Allowed values*: `POINT | LINE | POLYGON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-geospatiallayeritem-tooltip"></a>
Property description not available.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-analysis-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-geospatiallayeritem-visibility"></a>
The state of visibility for the layer.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
