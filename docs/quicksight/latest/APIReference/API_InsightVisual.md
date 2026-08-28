---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InsightVisual.html
---

# InsightVisual
<a name="API_InsightVisual"></a>

An insight visual.

For more information, see [Working with insights](https://docs.aws.amazon.com/quicksight/latest/user/computational-insights.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_InsightVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-InsightVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-InsightVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** DataSetIdentifier **   <a name="QS-Type-InsightVisual-DataSetIdentifier"></a>
The dataset that is used in the insight visual.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** InsightConfiguration **   <a name="QS-Type-InsightVisual-InsightConfiguration"></a>
The configuration of an insight visual.
Type: [InsightConfiguration](API_InsightConfiguration.md) object
Required: No

 ** Subtitle **   <a name="QS-Type-InsightVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-InsightVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** TopicIdentifier **   <a name="QS-Type-InsightVisual-TopicIdentifier"></a>
The topic that is used in the insight visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** VisualContentAltText **   <a name="QS-Type-InsightVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_InsightVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InsightVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InsightVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InsightVisual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
