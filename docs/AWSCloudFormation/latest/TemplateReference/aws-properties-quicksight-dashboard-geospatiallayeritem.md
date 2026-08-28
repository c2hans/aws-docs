---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatiallayeritem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialLayerItem
<a name="aws-properties-quicksight-dashboard-geospatiallayeritem"></a>

The properties for a single geospatial layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatiallayeritem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatiallayeritem-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-dashboard-geospatiallayeritem-actions)" : {{[ LayerCustomAction, ... ]}},
  "[DataSource](#cfn-quicksight-dashboard-geospatiallayeritem-datasource)" : {{GeospatialDataSourceItem}},
  "[JoinDefinition](#cfn-quicksight-dashboard-geospatiallayeritem-joindefinition)" : {{GeospatialLayerJoinDefinition}},
  "[Label](#cfn-quicksight-dashboard-geospatiallayeritem-label)" : {{String}},
  "[LayerDefinition](#cfn-quicksight-dashboard-geospatiallayeritem-layerdefinition)" : {{GeospatialLayerDefinition}},
  "[LayerId](#cfn-quicksight-dashboard-geospatiallayeritem-layerid)" : {{String}},
  "[LayerType](#cfn-quicksight-dashboard-geospatiallayeritem-layertype)" : {{String}},
  "[Tooltip](#cfn-quicksight-dashboard-geospatiallayeritem-tooltip)" : {{TooltipOptions}},
  "[Visibility](#cfn-quicksight-dashboard-geospatiallayeritem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatiallayeritem-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-dashboard-geospatiallayeritem-actions): {{
    - LayerCustomAction}}
  [DataSource](#cfn-quicksight-dashboard-geospatiallayeritem-datasource): {{
    GeospatialDataSourceItem}}
  [JoinDefinition](#cfn-quicksight-dashboard-geospatiallayeritem-joindefinition): {{
    GeospatialLayerJoinDefinition}}
  [Label](#cfn-quicksight-dashboard-geospatiallayeritem-label): {{String}}
  [LayerDefinition](#cfn-quicksight-dashboard-geospatiallayeritem-layerdefinition): {{
    GeospatialLayerDefinition}}
  [LayerId](#cfn-quicksight-dashboard-geospatiallayeritem-layerid): {{String}}
  [LayerType](#cfn-quicksight-dashboard-geospatiallayeritem-layertype): {{String}}
  [Tooltip](#cfn-quicksight-dashboard-geospatiallayeritem-tooltip): {{
    TooltipOptions}}
  [Visibility](#cfn-quicksight-dashboard-geospatiallayeritem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatiallayeritem-properties"></a>

`Actions`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-actions"></a>
A list of custom actions for a layer.
*Required*: No
*Type*: Array of [LayerCustomAction](aws-properties-quicksight-dashboard-layercustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSource`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-datasource"></a>
The data source for the layer.
*Required*: No
*Type*: [GeospatialDataSourceItem](aws-properties-quicksight-dashboard-geospatialdatasourceitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinDefinition`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-joindefinition"></a>
The join definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerJoinDefinition](aws-properties-quicksight-dashboard-geospatiallayerjoindefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-label"></a>
The label that is displayed for the layer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerDefinition`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-layerdefinition"></a>
The definition properties for a layer.
*Required*: No
*Type*: [GeospatialLayerDefinition](aws-properties-quicksight-dashboard-geospatiallayerdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerId`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-layerid"></a>
The ID of the layer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LayerType`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-layertype"></a>
The layer type.
*Required*: No
*Type*: String
*Allowed values*: `POINT | LINE | POLYGON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-tooltip"></a>
Property description not available.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-dashboard-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-geospatiallayeritem-visibility"></a>
The state of visibility for the layer.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
