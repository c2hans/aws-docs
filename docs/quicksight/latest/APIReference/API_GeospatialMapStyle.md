---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeospatialMapStyle.html
---

# GeospatialMapStyle
<a name="API_GeospatialMapStyle"></a>

The map style properties for a map.

## Contents
<a name="API_GeospatialMapStyle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackgroundColor **   <a name="QS-Type-GeospatialMapStyle-BackgroundColor"></a>
The background color and opacity values for a map.
Type: String
Pattern: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
Required: No

 ** BaseMapStyle **   <a name="QS-Type-GeospatialMapStyle-BaseMapStyle"></a>
The selected base map style.
Type: String
Valid Values: `LIGHT_GRAY | DARK_GRAY | STREET | IMAGERY`
Required: No

 ** BaseMapVisibility **   <a name="QS-Type-GeospatialMapStyle-BaseMapVisibility"></a>
The state of visibility for the base map.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_GeospatialMapStyle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeospatialMapStyle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeospatialMapStyle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeospatialMapStyle)
