---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LineChartMarkerStyleSettings.html
---

# LineChartMarkerStyleSettings
<a name="API_LineChartMarkerStyleSettings"></a>

Marker styles options for a line series in `LineChartVisual`.

## Contents
<a name="API_LineChartMarkerStyleSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MarkerColor **   <a name="QS-Type-LineChartMarkerStyleSettings-MarkerColor"></a>
Color of marker in the series.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** MarkerShape **   <a name="QS-Type-LineChartMarkerStyleSettings-MarkerShape"></a>
Shape option for markers in the series.
+  `CIRCLE`: Show marker as a circle.
+  `TRIANGLE`: Show marker as a triangle.
+  `SQUARE`: Show marker as a square.
+  `DIAMOND`: Show marker as a diamond.
+  `ROUNDED_SQUARE`: Show marker as a rounded square.
Type: String
Valid Values: `CIRCLE | TRIANGLE | SQUARE | DIAMOND | ROUNDED_SQUARE`
Required: No

 ** MarkerSize **   <a name="QS-Type-LineChartMarkerStyleSettings-MarkerSize"></a>
Size of marker in the series.
Type: String
Required: No

 ** MarkerVisibility **   <a name="QS-Type-LineChartMarkerStyleSettings-MarkerVisibility"></a>
Configuration option that determines whether to show the markers in the series.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_LineChartMarkerStyleSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LineChartMarkerStyleSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LineChartMarkerStyleSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LineChartMarkerStyleSettings)
