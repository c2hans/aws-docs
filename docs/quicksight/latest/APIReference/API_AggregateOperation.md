---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AggregateOperation.html
---

# AggregateOperation
<a name="API_AggregateOperation"></a>

A transform operation that groups rows by specified columns and applies aggregation functions to calculate summary values.

## Contents
<a name="API_AggregateOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Aggregations **   <a name="QS-Type-AggregateOperation-Aggregations"></a>
The list of aggregation functions to apply to the grouped data, such as `SUM`, `COUNT`, or `AVERAGE`.
Type: Array of [Aggregation](API_Aggregation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Required: Yes

 ** Alias **   <a name="QS-Type-AggregateOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Source **   <a name="QS-Type-AggregateOperation-Source"></a>
The source transform operation that provides input data for the aggregation.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

 ** GroupByColumnNames **   <a name="QS-Type-AggregateOperation-GroupByColumnNames"></a>
The list of column names to group by when performing the aggregation. Rows with the same values in these columns will be grouped together.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AggregateOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AggregateOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AggregateOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AggregateOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
