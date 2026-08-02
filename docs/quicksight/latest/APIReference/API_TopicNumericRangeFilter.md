---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicNumericRangeFilter.html
---

# TopicNumericRangeFilter
<a name="API_TopicNumericRangeFilter"></a>

A filter that filters topics based on the value of a numeric field. The filter includes only topics whose numeric field value falls within the specified range.

## Contents
<a name="API_TopicNumericRangeFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Aggregation **   <a name="QS-Type-TopicNumericRangeFilter-Aggregation"></a>
An aggregation function that specifies how to calculate the value of a numeric field for a topic, Valid values for this structure are `NO_AGGREGATION`, `SUM`, `AVERAGE`, `COUNT`, `DISTINCT_COUNT`, `MAX`, `MEDIAN`, `MIN`, `STDEV`, `STDEVP`, `VAR`, and `VARP`.
Type: String
Valid Values: `NO_AGGREGATION | SUM | AVERAGE | COUNT | DISTINCT_COUNT | MAX | MEDIAN | MIN | STDEV | STDEVP | VAR | VARP`
Required: No

 ** Constant **   <a name="QS-Type-TopicNumericRangeFilter-Constant"></a>
The constant used in a numeric range filter.
Type: [TopicRangeFilterConstant](API_TopicRangeFilterConstant.md) object
Required: No

 ** Inclusive **   <a name="QS-Type-TopicNumericRangeFilter-Inclusive"></a>
A Boolean value that indicates whether the endpoints of the numeric range are included in the filter. If set to true, topics whose numeric field value is equal to the endpoint values will be included in the filter. If set to false, topics whose numeric field value is equal to the endpoint values will be excluded from the filter.
Type: Boolean
Required: No

## See Also
<a name="API_TopicNumericRangeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicNumericRangeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicNumericRangeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicNumericRangeFilter)
