---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilledMapVisual.html
---

# FilledMapVisual
<a name="API_FilledMapVisual"></a>

A filled map.

For more information, see [Creating filled maps](https://docs.aws.amazon.com/quicksight/latest/user/filled-maps.html) in the *Amazon Quick Suite User Guide*.

## Contents
<a name="API_FilledMapVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-FilledMapVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-FilledMapVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-FilledMapVisual-ChartConfiguration"></a>
The configuration settings of the visual.
Type: [FilledMapConfiguration](API_FilledMapConfiguration.md) object
Required: No

 ** ColumnHierarchies **   <a name="QS-Type-FilledMapVisual-ColumnHierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
Type: Array of [ColumnHierarchy](API_ColumnHierarchy.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** ConditionalFormatting **   <a name="QS-Type-FilledMapVisual-ConditionalFormatting"></a>
The conditional formatting of a `FilledMapVisual`.
Type: [FilledMapConditionalFormatting](API_FilledMapConditionalFormatting.md) object
Required: No

 ** GeocodingPreferences **   <a name="QS-Type-FilledMapVisual-GeocodingPreferences"></a>
The geocoding prefences for filled map visual.
Type: Array of [GeocodePreference](API_GeocodePreference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** Subtitle **   <a name="QS-Type-FilledMapVisual-Subtitle"></a>
The subtitle that is displayed on the visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-FilledMapVisual-Title"></a>
The title that is displayed on the visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-FilledMapVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_FilledMapVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilledMapVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilledMapVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilledMapVisual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
