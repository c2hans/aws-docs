---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ComboChartConfiguration.html
---

# ComboChartConfiguration
<a name="API_ComboChartConfiguration"></a>

The configuration of a `ComboChartVisual`.

## Contents
<a name="API_ComboChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BarDataLabels **   <a name="QS-Type-ComboChartConfiguration-BarDataLabels"></a>
The options that determine if visual data labels are displayed.
The data label options for a bar in a combo chart.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** BarsArrangement **   <a name="QS-Type-ComboChartConfiguration-BarsArrangement"></a>
Determines the bar arrangement in a combo chart. The following are valid values in this structure:
+  `CLUSTERED`: For clustered bar combo charts.
+  `STACKED`: For stacked bar combo charts.
+  `STACKED_PERCENT`: Do not use. If you use this value, the operation returns a validation error.
Type: String
Valid Values: `CLUSTERED | STACKED | STACKED_PERCENT`
Required: No

 ** CategoryAxis **   <a name="QS-Type-ComboChartConfiguration-CategoryAxis"></a>
The category axis of a combo chart.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** CategoryLabelOptions **   <a name="QS-Type-ComboChartConfiguration-CategoryLabelOptions"></a>
The label options (label text, label visibility, and sort icon visibility) of a combo chart category (group/color) field well.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ColorLabelOptions **   <a name="QS-Type-ComboChartConfiguration-ColorLabelOptions"></a>
The label options (label text, label visibility, and sort icon visibility) of a combo chart's color field well.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** DefaultSeriesSettings **   <a name="QS-Type-ComboChartConfiguration-DefaultSeriesSettings"></a>
The options that determine the default presentation of all series in `ComboChartVisual`.
Type: [ComboChartDefaultSeriesSettings](API_ComboChartDefaultSeriesSettings.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-ComboChartConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [ComboChartFieldWells](API_ComboChartFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-ComboChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-ComboChartConfiguration-Legend"></a>
The legend display setup of the visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** LineDataLabels **   <a name="QS-Type-ComboChartConfiguration-LineDataLabels"></a>
The options that determine if visual data labels are displayed.
The data label options for a line in a combo chart.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** PrimaryYAxisDisplayOptions **   <a name="QS-Type-ComboChartConfiguration-PrimaryYAxisDisplayOptions"></a>
The label display options (grid line, range, scale, and axis step) of a combo chart's primary y-axis (bar) field well.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** PrimaryYAxisLabelOptions **   <a name="QS-Type-ComboChartConfiguration-PrimaryYAxisLabelOptions"></a>
The label options (label text, label visibility, and sort icon visibility) of a combo chart's primary y-axis (bar) field well.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ReferenceLines **   <a name="QS-Type-ComboChartConfiguration-ReferenceLines"></a>
The reference line setup of the visual.
Type: Array of [ReferenceLine](API_ReferenceLine.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** SecondaryYAxisDisplayOptions **   <a name="QS-Type-ComboChartConfiguration-SecondaryYAxisDisplayOptions"></a>
The label display options (grid line, range, scale, axis step) of a combo chart's secondary y-axis (line) field well.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** SecondaryYAxisLabelOptions **   <a name="QS-Type-ComboChartConfiguration-SecondaryYAxisLabelOptions"></a>
The label options (label text, label visibility, and sort icon visibility) of a combo chart's secondary y-axis(line) field well.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** Series **   <a name="QS-Type-ComboChartConfiguration-Series"></a>
The series item configuration of a `ComboChartVisual`.
Type: Array of [ComboSeriesItem](API_ComboSeriesItem.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** SingleAxisOptions **   <a name="QS-Type-ComboChartConfiguration-SingleAxisOptions"></a>
The settings of a chart's single axis configuration.
Type: [SingleAxisOptions](API_SingleAxisOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-ComboChartConfiguration-SortConfiguration"></a>
The sort configuration of a `ComboChartVisual`.
Type: [ComboChartSortConfiguration](API_ComboChartSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-ComboChartConfiguration-Tooltip"></a>
The legend display setup of the visual.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** VisualPalette **   <a name="QS-Type-ComboChartConfiguration-VisualPalette"></a>
The palette (chart color) display setup of the visual.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

## See Also
<a name="API_ComboChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ComboChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ComboChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ComboChartConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
