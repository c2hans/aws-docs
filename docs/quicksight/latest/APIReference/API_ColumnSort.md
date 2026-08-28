---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnSort.html
---

# ColumnSort
<a name="API_ColumnSort"></a>

The sort configuration for a column that is not used in a field well.

## Contents
<a name="API_ColumnSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Direction **   <a name="QS-Type-ColumnSort-Direction"></a>
The sort direction.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

 ** SortBy **   <a name="QS-Type-ColumnSort-SortBy"></a>
A column of a data set.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-ColumnSort-AggregationFunction"></a>
The aggregation function that is defined in the column sort.
Type: [AggregationFunction](API_AggregationFunction.md) object
Required: No

## See Also
<a name="API_ColumnSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnSort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
