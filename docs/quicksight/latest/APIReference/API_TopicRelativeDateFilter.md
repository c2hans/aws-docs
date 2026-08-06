---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicRelativeDateFilter.html
---

# TopicRelativeDateFilter
<a name="API_TopicRelativeDateFilter"></a>

A structure that represents a relative date filter.

## Contents
<a name="API_TopicRelativeDateFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Constant **   <a name="QS-Type-TopicRelativeDateFilter-Constant"></a>
The constant used in a relative date filter.
Type: [TopicSingularFilterConstant](API_TopicSingularFilterConstant.md) object
Required: No

 ** NullFilter **   <a name="QS-Type-TopicRelativeDateFilter-NullFilter"></a>
The `null` filter that is applied to the relative date filter.
Type: String
Valid Values: `ALL_VALUES | NON_NULLS_ONLY | NULLS_ONLY`
Required: No

 ** RelativeDateFilterFunction **   <a name="QS-Type-TopicRelativeDateFilter-RelativeDateFilterFunction"></a>
The function to be used in a relative date filter to determine the range of dates to include in the results. Valid values for this structure are `BEFORE`, `AFTER`, and `BETWEEN`.
Type: String
Valid Values: `PREVIOUS | THIS | LAST | NEXT | NOW`
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopicRelativeDateFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

## See Also
<a name="API_TopicRelativeDateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicRelativeDateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicRelativeDateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicRelativeDateFilter)
