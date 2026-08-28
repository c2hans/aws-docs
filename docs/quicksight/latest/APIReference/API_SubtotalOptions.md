---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SubtotalOptions.html
---

# SubtotalOptions
<a name="API_SubtotalOptions"></a>

The subtotal options.

## Contents
<a name="API_SubtotalOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomLabel **   <a name="QS-Type-SubtotalOptions-CustomLabel"></a>
The custom label string for the subtotal cells.
Type: String
Required: No

 ** FieldLevel **   <a name="QS-Type-SubtotalOptions-FieldLevel"></a>
The field level (all, custom, last) for the subtotal cells.
Type: String
Valid Values: `ALL | CUSTOM | LAST`
Required: No

 ** FieldLevelOptions **   <a name="QS-Type-SubtotalOptions-FieldLevelOptions"></a>
The optional configuration of subtotal cells.
Type: Array of [PivotTableFieldSubtotalOptions](API_PivotTableFieldSubtotalOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** MetricHeaderCellStyle **   <a name="QS-Type-SubtotalOptions-MetricHeaderCellStyle"></a>
The cell styling options for the subtotals of header cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** StyleTargets **   <a name="QS-Type-SubtotalOptions-StyleTargets"></a>
The style targets options for subtotals.
Type: Array of [TableStyleTarget](API_TableStyleTarget.md) objects
Array Members: Maximum number of 3 items.
Required: No

 ** TotalCellStyle **   <a name="QS-Type-SubtotalOptions-TotalCellStyle"></a>
The cell styling options for the subtotal cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** TotalsVisibility **   <a name="QS-Type-SubtotalOptions-TotalsVisibility"></a>
The visibility configuration for the subtotal cells.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** ValueCellStyle **   <a name="QS-Type-SubtotalOptions-ValueCellStyle"></a>
The cell styling options for the subtotals of value cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

## See Also
<a name="API_SubtotalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SubtotalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SubtotalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SubtotalOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
