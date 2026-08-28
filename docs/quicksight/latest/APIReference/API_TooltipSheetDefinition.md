---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TooltipSheetDefinition.html
---

# TooltipSheetDefinition
<a name="API_TooltipSheetDefinition"></a>

A tooltip sheet is an object that contains a set of visuals that are used as a tooltip. Every analysis and dashboard must contain at least one non-tooltip sheet.

## Contents
<a name="API_TooltipSheetDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SheetId **   <a name="QS-Type-TooltipSheetDefinition-SheetId"></a>
The unique identifier of a tooltip sheet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Images **   <a name="QS-Type-TooltipSheetDefinition-Images"></a>
A list of images on a tooltip sheet.
Type: Array of [SheetImage](API_SheetImage.md) objects
Array Members: Maximum number of 5 items.
Required: No

 ** Layouts **   <a name="QS-Type-TooltipSheetDefinition-Layouts"></a>
Layouts define how the components of a tooltip sheet are arranged.
For more information, see [Types of layout](https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [Layout](API_Layout.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Name **   <a name="QS-Type-TooltipSheetDefinition-Name"></a>
The name of the tooltip sheet. This name is displayed on the sheet's tab in the Quick console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** TextBoxes **   <a name="QS-Type-TooltipSheetDefinition-TextBoxes"></a>
The text boxes that are on a tooltip sheet.
Type: Array of [SheetTextBox](API_SheetTextBox.md) objects
Array Members: Maximum number of 5 items.
Required: No

 ** Visuals **   <a name="QS-Type-TooltipSheetDefinition-Visuals"></a>
A list of the visuals that are on a tooltip sheet.
Type: Array of [Visual](API_Visual.md) objects
Array Members: Maximum number of 5 items.
Required: No

## See Also
<a name="API_TooltipSheetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TooltipSheetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TooltipSheetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TooltipSheetDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
