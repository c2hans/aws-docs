---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualPalette.html
---

# VisualPalette
<a name="API_VisualPalette"></a>

The visual display options for the visual palette.

## Contents
<a name="API_VisualPalette_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChartColor **   <a name="QS-Type-VisualPalette-ChartColor"></a>
The chart color options for the visual palette.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** ColorMap **   <a name="QS-Type-VisualPalette-ColorMap"></a>
The color map options for the visual palette.
Type: Array of [DataPathColor](API_DataPathColor.md) objects
Array Members: Maximum number of 5000 items.
Required: No

## See Also
<a name="API_VisualPalette_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VisualPalette)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VisualPalette)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VisualPalette)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
