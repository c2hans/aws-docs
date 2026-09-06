---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_WordCloudVisual.html
---

# WordCloudVisual
<a name="API_WordCloudVisual"></a>

A word cloud.

For more information, see [Using word clouds](https://docs.aws.amazon.com/quicksight/latest/user/word-cloud.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_WordCloudVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-WordCloudVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-WordCloudVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-WordCloudVisual-ChartConfiguration"></a>
The configuration settings of the visual.
Type: [WordCloudChartConfiguration](API_WordCloudChartConfiguration.md) object
Required: No

 ** ColumnHierarchies **   <a name="QS-Type-WordCloudVisual-ColumnHierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
Type: Array of [ColumnHierarchy](API_ColumnHierarchy.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** Subtitle **   <a name="QS-Type-WordCloudVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-WordCloudVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-WordCloudVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_WordCloudVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/WordCloudVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/WordCloudVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/WordCloudVisual)
