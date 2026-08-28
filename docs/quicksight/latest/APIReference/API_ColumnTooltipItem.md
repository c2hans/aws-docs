---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnTooltipItem.html
---

# ColumnTooltipItem
<a name="API_ColumnTooltipItem"></a>

The tooltip item for the columns that are not part of a field well.

## Contents
<a name="API_ColumnTooltipItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-ColumnTooltipItem-Column"></a>
The target column of the tooltip item.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** Aggregation **   <a name="QS-Type-ColumnTooltipItem-Aggregation"></a>
The aggregation function of the column tooltip item.
Type: [AggregationFunction](API_AggregationFunction.md) object
Required: No

 ** Label **   <a name="QS-Type-ColumnTooltipItem-Label"></a>
The label of the tooltip item.
Type: String
Required: No

 ** TooltipTarget **   <a name="QS-Type-ColumnTooltipItem-TooltipTarget"></a>
Determines the target of the column tooltip item in a combo chart visual.
Type: String
Valid Values: `BOTH | BAR | LINE`
Required: No

 ** Visibility **   <a name="QS-Type-ColumnTooltipItem-Visibility"></a>
The visibility of the tooltip item.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_ColumnTooltipItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnTooltipItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnTooltipItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnTooltipItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
