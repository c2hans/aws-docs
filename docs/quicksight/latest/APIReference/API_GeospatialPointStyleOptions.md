---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeospatialPointStyleOptions.html
---

# GeospatialPointStyleOptions
<a name="API_GeospatialPointStyleOptions"></a>

The point style of the geospatial map.

## Contents
<a name="API_GeospatialPointStyleOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterMarkerConfiguration **   <a name="QS-Type-GeospatialPointStyleOptions-ClusterMarkerConfiguration"></a>
The cluster marker configuration of the geospatial point style.
Type: [ClusterMarkerConfiguration](API_ClusterMarkerConfiguration.md) object
Required: No

 ** HeatmapConfiguration **   <a name="QS-Type-GeospatialPointStyleOptions-HeatmapConfiguration"></a>
The heatmap configuration of the geospatial point style.
Type: [GeospatialHeatmapConfiguration](API_GeospatialHeatmapConfiguration.md) object
Required: No

 ** SelectedPointStyle **   <a name="QS-Type-GeospatialPointStyleOptions-SelectedPointStyle"></a>
The selected point styles (point, cluster) of the geospatial map.
Type: String
Valid Values: `POINT | CLUSTER | HEATMAP`
Required: No

## See Also
<a name="API_GeospatialPointStyleOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeospatialPointStyleOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeospatialPointStyleOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeospatialPointStyleOptions)
