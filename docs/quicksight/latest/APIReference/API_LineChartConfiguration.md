---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LineChartConfiguration.html
---

# LineChartConfiguration
<a name="API_LineChartConfiguration"></a>

The configuration of a line chart.

## Contents
<a name="API_LineChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContributionAnalysisDefaults **   <a name="QS-Type-LineChartConfiguration-ContributionAnalysisDefaults"></a>
The default configuration of a line chart's contribution analysis.
Type: Array of [ContributionAnalysisDefault](API_ContributionAnalysisDefault.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** DataLabels **   <a name="QS-Type-LineChartConfiguration-DataLabels"></a>
The data label configuration of a line chart.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** DefaultSeriesSettings **   <a name="QS-Type-LineChartConfiguration-DefaultSeriesSettings"></a>
The options that determine the default presentation of all line series in `LineChartVisual`.
Type: [LineChartDefaultSeriesSettings](API_LineChartDefaultSeriesSettings.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-LineChartConfiguration-FieldWells"></a>
The field well configuration of a line chart.
Type: [LineChartFieldWells](API_LineChartFieldWells.md) object
Required: No

 ** ForecastConfigurations **   <a name="QS-Type-LineChartConfiguration-ForecastConfigurations"></a>
The forecast configuration of a line chart.
Type: Array of [ForecastConfiguration](API_ForecastConfiguration.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** Interactions **   <a name="QS-Type-LineChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-LineChartConfiguration-Legend"></a>
The legend configuration of a line chart.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** PrimaryYAxisDisplayOptions **   <a name="QS-Type-LineChartConfiguration-PrimaryYAxisDisplayOptions"></a>
The series axis configuration of a line chart.
Type: [LineSeriesAxisDisplayOptions](API_LineSeriesAxisDisplayOptions.md) object
Required: No

 ** PrimaryYAxisLabelOptions **   <a name="QS-Type-LineChartConfiguration-PrimaryYAxisLabelOptions"></a>
The options that determine the presentation of the y-axis label.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ReferenceLines **   <a name="QS-Type-LineChartConfiguration-ReferenceLines"></a>
The reference lines configuration of a line chart.
Type: Array of [ReferenceLine](API_ReferenceLine.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** SecondaryYAxisDisplayOptions **   <a name="QS-Type-LineChartConfiguration-SecondaryYAxisDisplayOptions"></a>
The series axis configuration of a line chart.
Type: [LineSeriesAxisDisplayOptions](API_LineSeriesAxisDisplayOptions.md) object
Required: No

 ** SecondaryYAxisLabelOptions **   <a name="QS-Type-LineChartConfiguration-SecondaryYAxisLabelOptions"></a>
The options that determine the presentation of the secondary y-axis label.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** Series **   <a name="QS-Type-LineChartConfiguration-Series"></a>
The series item configuration of a line chart.
Type: Array of [SeriesItem](API_SeriesItem.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** SingleAxisOptions **   <a name="QS-Type-LineChartConfiguration-SingleAxisOptions"></a>
The settings of a chart's single axis configuration.
Type: [SingleAxisOptions](API_SingleAxisOptions.md) object
Required: No

 ** SmallMultiplesOptions **   <a name="QS-Type-LineChartConfiguration-SmallMultiplesOptions"></a>
The small multiples setup for the visual.
Type: [SmallMultiplesOptions](API_SmallMultiplesOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-LineChartConfiguration-SortConfiguration"></a>
The sort configuration of a line chart.
Type: [LineChartSortConfiguration](API_LineChartSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-LineChartConfiguration-Tooltip"></a>
The tooltip configuration of a line chart.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** Type **   <a name="QS-Type-LineChartConfiguration-Type"></a>
Determines the type of the line chart.
Type: String
Valid Values: `LINE | AREA | STACKED_AREA`
Required: No

 ** VisualPalette **   <a name="QS-Type-LineChartConfiguration-VisualPalette"></a>
The visual palette configuration of a line chart.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

 ** XAxisDisplayOptions **   <a name="QS-Type-LineChartConfiguration-XAxisDisplayOptions"></a>
The options that determine the presentation of the x-axis.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** XAxisLabelOptions **   <a name="QS-Type-LineChartConfiguration-XAxisLabelOptions"></a>
The options that determine the presentation of the x-axis label.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

## See Also
<a name="API_LineChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LineChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LineChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LineChartConfiguration)
