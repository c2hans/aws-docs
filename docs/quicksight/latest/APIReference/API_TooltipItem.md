---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TooltipItem.html
---

# TooltipItem
<a name="API_TooltipItem"></a>

The tooltip.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_TooltipItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnTooltipItem **   <a name="QS-Type-TooltipItem-ColumnTooltipItem"></a>
The tooltip item for the columns that are not part of a field well.
Type: [ColumnTooltipItem](API_ColumnTooltipItem.md) object
Required: No

 ** FieldTooltipItem **   <a name="QS-Type-TooltipItem-FieldTooltipItem"></a>
The tooltip item for the fields.
Type: [FieldTooltipItem](API_FieldTooltipItem.md) object
Required: No

## See Also
<a name="API_TooltipItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TooltipItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TooltipItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TooltipItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
