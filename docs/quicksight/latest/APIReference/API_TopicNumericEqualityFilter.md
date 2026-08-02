---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicNumericEqualityFilter.html
---

# TopicNumericEqualityFilter
<a name="API_TopicNumericEqualityFilter"></a>

A filter that filters topics based on the value of a numeric field. The filter includes only topics whose numeric field value matches the specified value.

## Contents
<a name="API_TopicNumericEqualityFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Aggregation **   <a name="QS-Type-TopicNumericEqualityFilter-Aggregation"></a>
An aggregation function that specifies how to calculate the value of a numeric field for a topic. Valid values for this structure are `NO_AGGREGATION`, `SUM`, `AVERAGE`, `COUNT`, `DISTINCT_COUNT`, `MAX`, `MEDIAN`, `MIN`, `STDEV`, `STDEVP`, `VAR`, and `VARP`.
Type: String
Valid Values: `NO_AGGREGATION | SUM | AVERAGE | COUNT | DISTINCT_COUNT | MAX | MEDIAN | MIN | STDEV | STDEVP | VAR | VARP`
Required: No

 ** Constant **   <a name="QS-Type-TopicNumericEqualityFilter-Constant"></a>
The constant used in a numeric equality filter.
Type: [TopicSingularFilterConstant](API_TopicSingularFilterConstant.md) object
Required: No

## See Also
<a name="API_TopicNumericEqualityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicNumericEqualityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicNumericEqualityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicNumericEqualityFilter)
