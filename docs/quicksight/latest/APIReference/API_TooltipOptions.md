---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TooltipOptions.html
---

# TooltipOptions
<a name="API_TooltipOptions"></a>

The display options for the visual tooltip.

## Contents
<a name="API_TooltipOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldBasedTooltip **   <a name="QS-Type-TooltipOptions-FieldBasedTooltip"></a>
The setup for the detailed tooltip. The tooltip setup is always saved. The display type is decided based on the tooltip type.
Type: [FieldBasedTooltip](API_FieldBasedTooltip.md) object
Required: No

 ** SelectedTooltipType **   <a name="QS-Type-TooltipOptions-SelectedTooltipType"></a>
The selected type for the tooltip. Choose one of the following options:
+  `BASIC`: A basic tooltip.
+  `DETAILED`: A detailed tooltip.
Type: String
Valid Values: `BASIC | DETAILED | SHEET`
Required: No

 ** SheetTooltip **   <a name="QS-Type-TooltipOptions-SheetTooltip"></a>
The configuration of the sheet tooltip.
Type: [SheetTooltip](API_SheetTooltip.md) object
Required: No

 ** TooltipVisibility **   <a name="QS-Type-TooltipOptions-TooltipVisibility"></a>
Determines whether or not the tooltip is visible.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_TooltipOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TooltipOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TooltipOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TooltipOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
