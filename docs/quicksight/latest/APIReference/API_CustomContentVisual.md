---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomContentVisual.html
---

# CustomContentVisual
<a name="API_CustomContentVisual"></a>

A visual that contains custom content.

For more information, see [Using custom visual content](https://docs.aws.amazon.com/quicksight/latest/user/custom-visual-content.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_CustomContentVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-CustomContentVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-CustomContentVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-CustomContentVisual-ChartConfiguration"></a>
The configuration of a `CustomContentVisual`.
Type: [CustomContentConfiguration](API_CustomContentConfiguration.md) object
Required: No

 ** DataSetIdentifier **   <a name="QS-Type-CustomContentVisual-DataSetIdentifier"></a>
The dataset that is used to create the custom content visual. You can't create a visual without a dataset or a topic.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Subtitle **   <a name="QS-Type-CustomContentVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-CustomContentVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** TopicIdentifier **   <a name="QS-Type-CustomContentVisual-TopicIdentifier"></a>
The topic that is used in the custom content visual. You can't create a visual without a dataset or a topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** VisualContentAltText **   <a name="QS-Type-CustomContentVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_CustomContentVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomContentVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomContentVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomContentVisual)
