---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PieChartConfiguration.html
---

# PieChartConfiguration
<a name="API_PieChartConfiguration"></a>

The configuration of a pie chart.

## Contents
<a name="API_PieChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryLabelOptions **   <a name="QS-Type-PieChartConfiguration-CategoryLabelOptions"></a>
The label options of the group/color that is displayed in a pie chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ContributionAnalysisDefaults **   <a name="QS-Type-PieChartConfiguration-ContributionAnalysisDefaults"></a>
The contribution analysis (anomaly configuration) setup of the visual.
Type: Array of [ContributionAnalysisDefault](API_ContributionAnalysisDefault.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** DataLabels **   <a name="QS-Type-PieChartConfiguration-DataLabels"></a>
The options that determine if visual data labels are displayed.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** DonutOptions **   <a name="QS-Type-PieChartConfiguration-DonutOptions"></a>
The options that determine the shape of the chart. This option determines whether the chart is a pie chart or a donut chart.
Type: [DonutOptions](API_DonutOptions.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-PieChartConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [PieChartFieldWells](API_PieChartFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-PieChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-PieChartConfiguration-Legend"></a>
The legend display setup of the visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** SmallMultiplesOptions **   <a name="QS-Type-PieChartConfiguration-SmallMultiplesOptions"></a>
The small multiples setup for the visual.
Type: [SmallMultiplesOptions](API_SmallMultiplesOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-PieChartConfiguration-SortConfiguration"></a>
The sort configuration of a pie chart.
Type: [PieChartSortConfiguration](API_PieChartSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-PieChartConfiguration-Tooltip"></a>
The tooltip display setup of the visual.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** ValueLabelOptions **   <a name="QS-Type-PieChartConfiguration-ValueLabelOptions"></a>
The label options for the value that is displayed in a pie chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** VisualPalette **   <a name="QS-Type-PieChartConfiguration-VisualPalette"></a>
The palette (chart color) display setup of the visual.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

## See Also
<a name="API_PieChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PieChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PieChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PieChartConfiguration)
