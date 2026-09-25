---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallayeritem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLayerItem
<a name="aws-properties-quicksight-template-geospatiallayeritem"></a>

The properties for a single geospatial layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallayeritem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallayeritem-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-geospatiallayeritem-actions)" : {{[ LayerCustomAction, ... ]}},
  "[DataSource](#cfn-quicksight-template-geospatiallayeritem-datasource)" : {{GeospatialDataSourceItem}},
  "[JoinDefinition](#cfn-quicksight-template-geospatiallayeritem-joindefinition)" : {{GeospatialLayerJoinDefinition}},
  "[Label](#cfn-quicksight-template-geospatiallayeritem-label)" : {{String}},
  "[LayerDefinition](#cfn-quicksight-template-geospatiallayeritem-layerdefinition)" : {{GeospatialLayerDefinition}},
  "[LayerId](#cfn-quicksight-template-geospatiallayeritem-layerid)" : {{String}},
  "[LayerType](#cfn-quicksight-template-geospatiallayeritem-layertype)" : {{String}},
  "[Tooltip](#cfn-quicksight-template-geospatiallayeritem-tooltip)" : {{TooltipOptions}},
  "[Visibility](#cfn-quicksight-template-geospatiallayeritem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallayeritem-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-geospatiallayeritem-actions): {{
    - LayerCustomAction}}
  [DataSource](#cfn-quicksight-template-geospatiallayeritem-datasource): {{
    GeospatialDataSourceItem}}
  [JoinDefinition](#cfn-quicksight-template-geospatiallayeritem-joindefinition): {{
    GeospatialLayerJoinDefinition}}
  [Label](#cfn-quicksight-template-geospatiallayeritem-label): {{String}}
  [LayerDefinition](#cfn-quicksight-template-geospatiallayeritem-layerdefinition): {{
    GeospatialLayerDefinition}}
  [LayerId](#cfn-quicksight-template-geospatiallayeritem-layerid): {{String}}
  [LayerType](#cfn-quicksight-template-geospatiallayeritem-layertype): {{String}}
  [Tooltip](#cfn-quicksight-template-geospatiallayeritem-tooltip): {{
    TooltipOptions}}
  [Visibility](#cfn-quicksight-template-geospatiallayeritem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallayeritem-properties"></a>

`Actions`  <a name="cfn-quicksight-template-geospatiallayeritem-actions"></a>
A list of custom actions for a layer.
*Required*: No
*Type*: Array of [LayerCustomAction](aws-properties-quicksight-template-layercustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSource`  <a name="cfn-quicksight-template-geospatiallayeritem-datasource"></a>
The data source for the layer.
*Required*: No
*Type*: [GeospatialDataSourceItem](aws-properties-quicksight-template-geospatialdatasourceitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinDefinition`  <a name="cfn-quicksight-template-geospatiallayeritem-joindefinition"></a>
The join definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerJoinDefinition](aws-properties-quicksight-template-geospatiallayerjoindefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-template-geospatiallayeritem-label"></a>
The label that is displayed for the layer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerDefinition`  <a name="cfn-quicksight-template-geospatiallayeritem-layerdefinition"></a>
The definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerDefinition](aws-properties-quicksight-template-geospatiallayerdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerId`  <a name="cfn-quicksight-template-geospatiallayeritem-layerid"></a>
The ID of the layer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerType`  <a name="cfn-quicksight-template-geospatiallayeritem-layertype"></a>
The layer type.
*Required*: No
*Type*: String
*Allowed values*: `POINT | LINE | POLYGON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-template-geospatiallayeritem-tooltip"></a>
Property description not available.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-template-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-geospatiallayeritem-visibility"></a>
The state of visibility for the layer.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
