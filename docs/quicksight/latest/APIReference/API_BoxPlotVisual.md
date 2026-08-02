---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BoxPlotVisual.html
---

# BoxPlotVisual
<a name="API_BoxPlotVisual"></a>

A box plot.

For more information, see [Using box plots](https://docs.aws.amazon.com/quicksight/latest/user/box-plots.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_BoxPlotVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-BoxPlotVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-BoxPlotVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-BoxPlotVisual-ChartConfiguration"></a>
The configuration settings of the visual.
Type: [BoxPlotChartConfiguration](API_BoxPlotChartConfiguration.md) object
Required: No

 ** ColumnHierarchies **   <a name="QS-Type-BoxPlotVisual-ColumnHierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
Type: Array of [ColumnHierarchy](API_ColumnHierarchy.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** Subtitle **   <a name="QS-Type-BoxPlotVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-BoxPlotVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-BoxPlotVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_BoxPlotVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BoxPlotVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BoxPlotVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BoxPlotVisual)
