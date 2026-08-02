---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIRFilterOption.html
---

# TopicIRFilterOption
<a name="API_TopicIRFilterOption"></a>

The definition for a `TopicIRFilterOption`.

## Contents
<a name="API_TopicIRFilterOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AggMetrics **   <a name="QS-Type-TopicIRFilterOption-AggMetrics"></a>
The agg metrics for the `TopicIRFilterOption`.
Type: Array of [FilterAggMetrics](API_FilterAggMetrics.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** Aggregation **   <a name="QS-Type-TopicIRFilterOption-Aggregation"></a>
The aggregation for the `TopicIRFilterOption`.
Type: String
Valid Values: `SUM | MIN | MAX | COUNT | AVERAGE | DISTINCT_COUNT | STDEV | STDEVP | VAR | VARP | PERCENTILE | MEDIAN | PTD_SUM | PTD_MIN | PTD_MAX | PTD_COUNT | PTD_DISTINCT_COUNT | PTD_AVERAGE | COLUMN | CUSTOM`
Required: No

 ** AggregationFunctionParameters **   <a name="QS-Type-TopicIRFilterOption-AggregationFunctionParameters"></a>
The aggregation function parameters for the `TopicIRFilterOption`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Maximum length of 1024.
Required: No

 ** AggregationPartitionBy **   <a name="QS-Type-TopicIRFilterOption-AggregationPartitionBy"></a>
The `AggregationPartitionBy` for the `TopicIRFilterOption`.
Type: Array of [AggregationPartitionBy](API_AggregationPartitionBy.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** Anchor **   <a name="QS-Type-TopicIRFilterOption-Anchor"></a>
The anchor for the `TopicIRFilterOption`.
Type: [Anchor](API_Anchor.md) object
Required: No

 ** Constant **   <a name="QS-Type-TopicIRFilterOption-Constant"></a>
The constant for the `TopicIRFilterOption`.
Type: [TopicConstantValue](API_TopicConstantValue.md) object
Required: No

 ** FilterClass **   <a name="QS-Type-TopicIRFilterOption-FilterClass"></a>
The filter class for the `TopicIRFilterOption`.
Type: String
Valid Values: `ENFORCED_VALUE_FILTER | CONDITIONAL_VALUE_FILTER | NAMED_VALUE_FILTER`
Required: No

 ** FilterType **   <a name="QS-Type-TopicIRFilterOption-FilterType"></a>
The filter type for the `TopicIRFilterOption`.
Type: String
Valid Values: `CATEGORY_FILTER | NUMERIC_EQUALITY_FILTER | NUMERIC_RANGE_FILTER | DATE_RANGE_FILTER | RELATIVE_DATE_FILTER | TOP_BOTTOM_FILTER | EQUALS | RANK_LIMIT_FILTER | ACCEPT_ALL_FILTER`
Required: No

 ** Function **   <a name="QS-Type-TopicIRFilterOption-Function"></a>
The function for the `TopicIRFilterOption`.
Type: String
Valid Values: `CONTAINS | EXACT | STARTS_WITH | ENDS_WITH | CONTAINS_STRING | PREVIOUS | THIS | LAST | NEXT | NOW`
Required: No

 ** Inclusive **   <a name="QS-Type-TopicIRFilterOption-Inclusive"></a>
The inclusive for the `TopicIRFilterOption`.
Type: Boolean
Required: No

 ** Inverse **   <a name="QS-Type-TopicIRFilterOption-Inverse"></a>
The inverse for the `TopicIRFilterOption`.
Type: Boolean
Required: No

 ** LastNextOffset **   <a name="QS-Type-TopicIRFilterOption-LastNextOffset"></a>
The last next offset for the `TopicIRFilterOption`.
Type: [TopicConstantValue](API_TopicConstantValue.md) object
Required: No

 ** NullFilter **   <a name="QS-Type-TopicIRFilterOption-NullFilter"></a>
The null filter for the `TopicIRFilterOption`.
Type: String
Valid Values: `ALL_VALUES | NON_NULLS_ONLY | NULLS_ONLY`
Required: No

 ** OperandField **   <a name="QS-Type-TopicIRFilterOption-OperandField"></a>
The operand field for the `TopicIRFilterOption`.
Type: [Identifier](API_Identifier.md) object
Required: No

 ** Range **   <a name="QS-Type-TopicIRFilterOption-Range"></a>
The range for the `TopicIRFilterOption`.
Type: [TopicConstantValue](API_TopicConstantValue.md) object
Required: No

 ** SortDirection **   <a name="QS-Type-TopicIRFilterOption-SortDirection"></a>
The sort direction for the `TopicIRFilterOption`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopicIRFilterOption-TimeGranularity"></a>
The time granularity for the `TopicIRFilterOption`.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** TopBottomLimit **   <a name="QS-Type-TopicIRFilterOption-TopBottomLimit"></a>
The `TopBottomLimit` for the `TopicIRFilterOption`.
Type: [TopicConstantValue](API_TopicConstantValue.md) object
Required: No

## See Also
<a name="API_TopicIRFilterOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIRFilterOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIRFilterOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIRFilterOption)
