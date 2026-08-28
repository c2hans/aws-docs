---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AggregationSortConfiguration.html
---

# AggregationSortConfiguration
<a name="API_AggregationSortConfiguration"></a>

The configuration options to sort aggregated values.

## Contents
<a name="API_AggregationSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-AggregationSortConfiguration-Column"></a>
The column that determines the sort order of aggregated values.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** SortDirection **   <a name="QS-Type-AggregationSortConfiguration-SortDirection"></a>
The sort direction of values.
+  `ASC`: Sort in ascending order.
+  `DESC`: Sort in descending order.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-AggregationSortConfiguration-AggregationFunction"></a>
The function that aggregates the values in `Column`.
Type: [AggregationFunction](API_AggregationFunction.md) object
Required: No

## See Also
<a name="API_AggregationSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AggregationSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AggregationSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AggregationSortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
