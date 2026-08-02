---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BoxPlotChartConfiguration.html
---

# BoxPlotChartConfiguration
<a name="API_BoxPlotChartConfiguration"></a>

The configuration of a `BoxPlotVisual`.

## Contents
<a name="API_BoxPlotChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BoxPlotOptions **   <a name="QS-Type-BoxPlotChartConfiguration-BoxPlotOptions"></a>
The box plot chart options for a box plot visual
Type: [BoxPlotOptions](API_BoxPlotOptions.md) object
Required: No

 ** CategoryAxis **   <a name="QS-Type-BoxPlotChartConfiguration-CategoryAxis"></a>
The label display options (grid line, range, scale, axis step) of a box plot category.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** CategoryLabelOptions **   <a name="QS-Type-BoxPlotChartConfiguration-CategoryLabelOptions"></a>
The label options (label text, label visibility and sort Icon visibility) of a box plot category.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-BoxPlotChartConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [BoxPlotFieldWells](API_BoxPlotFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-BoxPlotChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-BoxPlotChartConfiguration-Legend"></a>
The options for the legend setup of a visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** PrimaryYAxisDisplayOptions **   <a name="QS-Type-BoxPlotChartConfiguration-PrimaryYAxisDisplayOptions"></a>
The label display options (grid line, range, scale, axis step) of a box plot category.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** PrimaryYAxisLabelOptions **   <a name="QS-Type-BoxPlotChartConfiguration-PrimaryYAxisLabelOptions"></a>
The label options (label text, label visibility and sort icon visibility) of a box plot value.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ReferenceLines **   <a name="QS-Type-BoxPlotChartConfiguration-ReferenceLines"></a>
The reference line setup of the visual.
Type: Array of [ReferenceLine](API_ReferenceLine.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** SortConfiguration **   <a name="QS-Type-BoxPlotChartConfiguration-SortConfiguration"></a>
The sort configuration of a `BoxPlotVisual`.
Type: [BoxPlotSortConfiguration](API_BoxPlotSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-BoxPlotChartConfiguration-Tooltip"></a>
The tooltip display setup of the visual.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** VisualPalette **   <a name="QS-Type-BoxPlotChartConfiguration-VisualPalette"></a>
The palette (chart color) display setup of the visual.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

## See Also
<a name="API_BoxPlotChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BoxPlotChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BoxPlotChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BoxPlotChartConfiguration)
