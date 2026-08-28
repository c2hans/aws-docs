---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PanelConfiguration.html
---

# PanelConfiguration
<a name="API_PanelConfiguration"></a>

A collection of options that configure how each panel displays in a small multiples chart.

## Contents
<a name="API_PanelConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackgroundColor **   <a name="QS-Type-PanelConfiguration-BackgroundColor"></a>
Sets the background color for each panel.
Type: String
Pattern: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
Required: No

 ** BackgroundVisibility **   <a name="QS-Type-PanelConfiguration-BackgroundVisibility"></a>
Determines whether or not a background for each small multiples panel is rendered.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** BorderColor **   <a name="QS-Type-PanelConfiguration-BorderColor"></a>
Sets the line color of panel borders.
Type: String
Pattern: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
Required: No

 ** BorderStyle **   <a name="QS-Type-PanelConfiguration-BorderStyle"></a>
Sets the line style of panel borders.
Type: String
Valid Values: `SOLID | DASHED | DOTTED`
Required: No

 ** BorderThickness **   <a name="QS-Type-PanelConfiguration-BorderThickness"></a>
Sets the line thickness of panel borders.
Type: String
Required: No

 ** BorderVisibility **   <a name="QS-Type-PanelConfiguration-BorderVisibility"></a>
Determines whether or not each panel displays a border.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** GutterSpacing **   <a name="QS-Type-PanelConfiguration-GutterSpacing"></a>
Sets the total amount of negative space to display between sibling panels.
Type: String
Required: No

 ** GutterVisibility **   <a name="QS-Type-PanelConfiguration-GutterVisibility"></a>
Determines whether or not negative space between sibling panels is rendered.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Title **   <a name="QS-Type-PanelConfiguration-Title"></a>
Configures the title display within each small multiples panel.
Type: [PanelTitleOptions](API_PanelTitleOptions.md) object
Required: No

## See Also
<a name="API_PanelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PanelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PanelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PanelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
