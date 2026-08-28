---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LegendOptions.html
---

# LegendOptions
<a name="API_LegendOptions"></a>

The options for the legend setup of a visual.

## Contents
<a name="API_LegendOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Height **   <a name="QS-Type-LegendOptions-Height"></a>
The height of the legend. If this value is omitted, a default height is used when rendering.
Type: String
Required: No

 ** Position **   <a name="QS-Type-LegendOptions-Position"></a>
The positions for the legend. Choose one of the following options:
+  `AUTO`
+  `RIGHT`
+  `BOTTOM`
+  `LEFT`
Type: String
Valid Values: `AUTO | RIGHT | BOTTOM | TOP`
Required: No

 ** Title **   <a name="QS-Type-LegendOptions-Title"></a>
The custom title for the legend.
Type: [LabelOptions](API_LabelOptions.md) object
Required: No

 ** ValueFontConfiguration **   <a name="QS-Type-LegendOptions-ValueFontConfiguration"></a>
Configures the display properties of the given text.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** Visibility **   <a name="QS-Type-LegendOptions-Visibility"></a>
Determines whether or not the legend is visible.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Width **   <a name="QS-Type-LegendOptions-Width"></a>
The width of the legend. If this value is omitted, a default width is used when rendering.
Type: String
Required: No

## See Also
<a name="API_LegendOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LegendOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LegendOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LegendOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
