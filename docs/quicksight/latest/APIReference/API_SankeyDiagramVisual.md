---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SankeyDiagramVisual.html
---

# SankeyDiagramVisual
<a name="API_SankeyDiagramVisual"></a>

A sankey diagram.

For more information, see [Using Sankey diagrams](https://docs.aws.amazon.com/quicksight/latest/user/sankey-diagram.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_SankeyDiagramVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-SankeyDiagramVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-SankeyDiagramVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-SankeyDiagramVisual-ChartConfiguration"></a>
The configuration of a sankey diagram.
Type: [SankeyDiagramChartConfiguration](API_SankeyDiagramChartConfiguration.md) object
Required: No

 ** Subtitle **   <a name="QS-Type-SankeyDiagramVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-SankeyDiagramVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-SankeyDiagramVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_SankeyDiagramVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SankeyDiagramVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SankeyDiagramVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SankeyDiagramVisual)
