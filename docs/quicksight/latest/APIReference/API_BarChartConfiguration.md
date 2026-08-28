---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BarChartConfiguration.html
---

# BarChartConfiguration
<a name="API_BarChartConfiguration"></a>

The configuration of a `BarChartVisual`.

## Contents
<a name="API_BarChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BarsArrangement **   <a name="QS-Type-BarChartConfiguration-BarsArrangement"></a>
Determines the arrangement of the bars. The orientation and arrangement of bars determine the type of bar that is used in the visual.
Type: String
Valid Values: `CLUSTERED | STACKED | STACKED_PERCENT`
Required: No

 ** CategoryAxis **   <a name="QS-Type-BarChartConfiguration-CategoryAxis"></a>
The label display options (grid line, range, scale, axis step) for bar chart category.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** CategoryLabelOptions **   <a name="QS-Type-BarChartConfiguration-CategoryLabelOptions"></a>
The label options (label text, label visibility and sort icon visibility) for a bar chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ColorLabelOptions **   <a name="QS-Type-BarChartConfiguration-ColorLabelOptions"></a>
The label options (label text, label visibility and sort icon visibility) for a color that is used in a bar chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ContributionAnalysisDefaults **   <a name="QS-Type-BarChartConfiguration-ContributionAnalysisDefaults"></a>
The contribution analysis (anomaly configuration) setup of the visual.
Type: Array of [ContributionAnalysisDefault](API_ContributionAnalysisDefault.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** DataLabels **   <a name="QS-Type-BarChartConfiguration-DataLabels"></a>
The options that determine if visual data labels are displayed.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** DefaultSeriesSettings **   <a name="QS-Type-BarChartConfiguration-DefaultSeriesSettings"></a>
The options that determine the default presentation of all bar series in `BarChartVisual`.
Type: [BarChartDefaultSeriesSettings](API_BarChartDefaultSeriesSettings.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-BarChartConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [BarChartFieldWells](API_BarChartFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-BarChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-BarChartConfiguration-Legend"></a>
The legend display setup of the visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** Orientation **   <a name="QS-Type-BarChartConfiguration-Orientation"></a>
The orientation of the bars in a bar chart visual. There are two valid values in this structure:
+  `HORIZONTAL`: Used for charts that have horizontal bars. Visuals that use this value are horizontal bar charts, horizontal stacked bar charts, and horizontal stacked 100% bar charts.
+  `VERTICAL`: Used for charts that have vertical bars. Visuals that use this value are vertical bar charts, vertical stacked bar charts, and vertical stacked 100% bar charts.
Type: String
Valid Values: `HORIZONTAL | VERTICAL`
Required: No

 ** ReferenceLines **   <a name="QS-Type-BarChartConfiguration-ReferenceLines"></a>
The reference line setup of the visual.
Type: Array of [ReferenceLine](API_ReferenceLine.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Series **   <a name="QS-Type-BarChartConfiguration-Series"></a>
The series item configuration of a `BarChartVisual`.
Type: Array of [BarSeriesItem](API_BarSeriesItem.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** SmallMultiplesOptions **   <a name="QS-Type-BarChartConfiguration-SmallMultiplesOptions"></a>
The small multiples setup for the visual.
Type: [SmallMultiplesOptions](API_SmallMultiplesOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-BarChartConfiguration-SortConfiguration"></a>
The sort configuration of a `BarChartVisual`.
Type: [BarChartSortConfiguration](API_BarChartSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-BarChartConfiguration-Tooltip"></a>
The tooltip display setup of the visual.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** ValueAxis **   <a name="QS-Type-BarChartConfiguration-ValueAxis"></a>
The label display options (grid line, range, scale, axis step) for a bar chart value.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** ValueLabelOptions **   <a name="QS-Type-BarChartConfiguration-ValueLabelOptions"></a>
The label options (label text, label visibility and sort icon visibility) for a bar chart value.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** VisualPalette **   <a name="QS-Type-BarChartConfiguration-VisualPalette"></a>
The palette (chart color) display setup of the visual.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

## See Also
<a name="API_BarChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BarChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BarChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BarChartConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
