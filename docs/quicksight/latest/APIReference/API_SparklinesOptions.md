---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SparklinesOptions.html
---

# SparklinesOptions
<a name="API_SparklinesOptions"></a>

The options for sparklines in a table.

## Contents
<a name="API_SparklinesOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-SparklinesOptions-FieldId"></a>
The field ID of the value column that the sparkline is applied to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** XAxisField **   <a name="QS-Type-SparklinesOptions-XAxisField"></a>
The dimension type field.
Type: [DimensionField](API_DimensionField.md) object
Required: Yes

 ** AllPointsMarker **   <a name="QS-Type-SparklinesOptions-AllPointsMarker"></a>
Marker styles options for a line series in `LineChartVisual`.
Type: [LineChartMarkerStyleSettings](API_LineChartMarkerStyleSettings.md) object
Required: No

 ** LineColor **   <a name="QS-Type-SparklinesOptions-LineColor"></a>
The color of the sparkline line.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** LineInterpolation **   <a name="QS-Type-SparklinesOptions-LineInterpolation"></a>
The interpolation style for the sparkline line.
Type: String
Valid Values: `LINEAR | SMOOTH | STEPPED`
Required: No

 ** MaxValueMarker **   <a name="QS-Type-SparklinesOptions-MaxValueMarker"></a>
Marker styles options for a line series in `LineChartVisual`.
Type: [LineChartMarkerStyleSettings](API_LineChartMarkerStyleSettings.md) object
Required: No

 ** MinValueMarker **   <a name="QS-Type-SparklinesOptions-MinValueMarker"></a>
Marker styles options for a line series in `LineChartVisual`.
Type: [LineChartMarkerStyleSettings](API_LineChartMarkerStyleSettings.md) object
Required: No

 ** VisualType **   <a name="QS-Type-SparklinesOptions-VisualType"></a>
The type of the sparkline. Valid values are `LINE` and `AREA_LINE`.
Type: String
Valid Values: `LINE | AREA_LINE`
Required: No

 ** YAxisBehavior **   <a name="QS-Type-SparklinesOptions-YAxisBehavior"></a>
Determines whether the Y axis is shared across all sparklines or independent for each sparkline.
Type: String
Valid Values: `SHARED | INDEPENDENT`
Required: No

## See Also
<a name="API_SparklinesOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SparklinesOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SparklinesOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SparklinesOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
