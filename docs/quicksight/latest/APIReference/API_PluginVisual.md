---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PluginVisual.html
---

# PluginVisual
<a name="API_PluginVisual"></a>

A flexible visualization type that allows engineers to create new custom charts in Quick Sight.

## Contents
<a name="API_PluginVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PluginArn **   <a name="QS-Type-PluginVisual-PluginArn"></a>
The Amazon Resource Name (ARN) that reflects the plugin and version.
Type: String
Required: Yes

 ** VisualId **   <a name="QS-Type-PluginVisual-VisualId"></a>
The ID of the visual that you want to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-PluginVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** ChartConfiguration **   <a name="QS-Type-PluginVisual-ChartConfiguration"></a>
 A description of the plugin field wells and their persisted properties.
Type: [PluginVisualConfiguration](API_PluginVisualConfiguration.md) object
Required: No

 ** Subtitle **   <a name="QS-Type-PluginVisual-Subtitle"></a>
The subtitle label options for a visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-PluginVisual-Title"></a>
The title label options for a visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-PluginVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PluginVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PluginVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PluginVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PluginVisual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
