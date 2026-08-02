---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PieChartVisual.html
---

# PieChartVisual
<a name="API_PieChartVisual"></a>

A pie or donut chart.

The `PieChartVisual` structure describes a visual that is a member of the pie chart family.

The following charts can be described by using this structure:
+ Pie charts
+ Donut charts

For more information, see [Using pie charts](https://docs.aws.amazon.com/quicksight/latest/user/pie-chart.html) in the *Amazon Quick Suite User Guide*.

For more information, see [Using donut charts](https://docs.aws.amazon.com/quicksight/latest/user/donut-chart.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_PieChartVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-PieChartVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-PieChartVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-PieChartVisual-ChartConfiguration"></a>
The configuration of a pie chart.
Type: [PieChartConfiguration](API_PieChartConfiguration.md) object
Required: No

 ** ColumnHierarchies **   <a name="QS-Type-PieChartVisual-ColumnHierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
Type: Array of [ColumnHierarchy](API_ColumnHierarchy.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** Subtitle **   <a name="QS-Type-PieChartVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-PieChartVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-PieChartVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PieChartVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PieChartVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PieChartVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PieChartVisual)
