---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotTotalOptions.html
---

# PivotTotalOptions
<a name="API_PivotTotalOptions"></a>

The optional configuration of totals cells in a `PivotTableVisual`.

## Contents
<a name="API_PivotTotalOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomLabel **   <a name="QS-Type-PivotTotalOptions-CustomLabel"></a>
The custom label string for the total cells.
Type: String
Required: No

 ** MetricHeaderCellStyle **   <a name="QS-Type-PivotTotalOptions-MetricHeaderCellStyle"></a>
The cell styling options for the total of header cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** Placement **   <a name="QS-Type-PivotTotalOptions-Placement"></a>
The placement (start, end) for the total cells.
Type: String
Valid Values: `START | END | AUTO`
Required: No

 ** ScrollStatus **   <a name="QS-Type-PivotTotalOptions-ScrollStatus"></a>
The scroll status (pinned, scrolled) for the total cells.
Type: String
Valid Values: `PINNED | SCROLLED`
Required: No

 ** TotalAggregationOptions **   <a name="QS-Type-PivotTotalOptions-TotalAggregationOptions"></a>
The total aggregation options for each value field.
Type: Array of [TotalAggregationOption](API_TotalAggregationOption.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** TotalCellStyle **   <a name="QS-Type-PivotTotalOptions-TotalCellStyle"></a>
The cell styling options for the total cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** TotalsVisibility **   <a name="QS-Type-PivotTotalOptions-TotalsVisibility"></a>
The visibility configuration for the total cells.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** ValueCellStyle **   <a name="QS-Type-PivotTotalOptions-ValueCellStyle"></a>
The cell styling options for the totals of value cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

## See Also
<a name="API_PivotTotalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotTotalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotTotalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotTotalOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
