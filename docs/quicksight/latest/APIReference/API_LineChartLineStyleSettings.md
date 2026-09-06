---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LineChartLineStyleSettings.html
---

# LineChartLineStyleSettings
<a name="API_LineChartLineStyleSettings"></a>

Line styles options for a line series in `LineChartVisual`.

## Contents
<a name="API_LineChartLineStyleSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LineInterpolation **   <a name="QS-Type-LineChartLineStyleSettings-LineInterpolation"></a>
Interpolation style for line series.
+  `LINEAR`: Show as default, linear style.
+  `SMOOTH`: Show as a smooth curve.
+  `STEPPED`: Show steps in line.
Type: String
Valid Values: `LINEAR | SMOOTH | STEPPED`
Required: No

 ** LineStyle **   <a name="QS-Type-LineChartLineStyleSettings-LineStyle"></a>
Line style for line series.
+  `SOLID`: Show as a solid line.
+  `DOTTED`: Show as a dotted line.
+  `DASHED`: Show as a dashed line.
Type: String
Valid Values: `SOLID | DOTTED | DASHED`
Required: No

 ** LineVisibility **   <a name="QS-Type-LineChartLineStyleSettings-LineVisibility"></a>
Configuration option that determines whether to show the line for the series.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** LineWidth **   <a name="QS-Type-LineChartLineStyleSettings-LineWidth"></a>
Width that determines the line thickness.
Type: String
Required: No

## See Also
<a name="API_LineChartLineStyleSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LineChartLineStyleSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LineChartLineStyleSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LineChartLineStyleSettings)
