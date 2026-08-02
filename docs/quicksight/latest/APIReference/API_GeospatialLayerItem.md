---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeospatialLayerItem.html
---

# GeospatialLayerItem
<a name="API_GeospatialLayerItem"></a>

The properties for a single geospatial layer.

## Contents
<a name="API_GeospatialLayerItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LayerId **   <a name="QS-Type-GeospatialLayerItem-LayerId"></a>
The ID of the layer.
Type: String
Required: Yes

 ** Actions **   <a name="QS-Type-GeospatialLayerItem-Actions"></a>
A list of custom actions for a layer.
Type: Array of [LayerCustomAction](API_LayerCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** DataSource **   <a name="QS-Type-GeospatialLayerItem-DataSource"></a>
The data source for the layer.
Type: [GeospatialDataSourceItem](API_GeospatialDataSourceItem.md) object
Required: No

 ** JoinDefinition **   <a name="QS-Type-GeospatialLayerItem-JoinDefinition"></a>
The join definition properties for a layer.
Type: [GeospatialLayerJoinDefinition](API_GeospatialLayerJoinDefinition.md) object
Required: No

 ** Label **   <a name="QS-Type-GeospatialLayerItem-Label"></a>
The label that is displayed for the layer.
Type: String
Required: No

 ** LayerDefinition **   <a name="QS-Type-GeospatialLayerItem-LayerDefinition"></a>
The definition properties for a layer.
Type: [GeospatialLayerDefinition](API_GeospatialLayerDefinition.md) object
Required: No

 ** LayerType **   <a name="QS-Type-GeospatialLayerItem-LayerType"></a>
The layer type.
Type: String
Valid Values: `POINT | LINE | POLYGON`
Required: No

 ** Tooltip **   <a name="QS-Type-GeospatialLayerItem-Tooltip"></a>
The display options for the visual tooltip.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** Visibility **   <a name="QS-Type-GeospatialLayerItem-Visibility"></a>
The state of visibility for the layer.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_GeospatialLayerItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeospatialLayerItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeospatialLayerItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeospatialLayerItem)
