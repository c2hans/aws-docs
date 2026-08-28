---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotTableCellConditionalFormatting.html
---

# PivotTableCellConditionalFormatting
<a name="API_PivotTableCellConditionalFormatting"></a>

The cell conditional formatting option for a pivot table.

## Contents
<a name="API_PivotTableCellConditionalFormatting_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-PivotTableCellConditionalFormatting-FieldId"></a>
The field ID of the cell for conditional formatting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Scope **   <a name="QS-Type-PivotTableCellConditionalFormatting-Scope"></a>
The scope of the cell for conditional formatting.
Type: [PivotTableConditionalFormattingScope](API_PivotTableConditionalFormattingScope.md) object
Required: No

 ** Scopes **   <a name="QS-Type-PivotTableCellConditionalFormatting-Scopes"></a>
A list of cell scopes for conditional formatting.
Type: Array of [PivotTableConditionalFormattingScope](API_PivotTableConditionalFormattingScope.md) objects
Array Members: Maximum number of 3 items.
Required: No

 ** TextFormat **   <a name="QS-Type-PivotTableCellConditionalFormatting-TextFormat"></a>
The text format of the cell for conditional formatting.
Type: [TextConditionalFormat](API_TextConditionalFormat.md) object
Required: No

## See Also
<a name="API_PivotTableCellConditionalFormatting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotTableCellConditionalFormatting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotTableCellConditionalFormatting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotTableCellConditionalFormatting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
