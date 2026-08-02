---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicFilter.html
---

# TopicFilter
<a name="API_TopicFilter"></a>

A structure that represents a filter used to select items for a topic.

## Contents
<a name="API_TopicFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterName **   <a name="QS-Type-TopicFilter-FilterName"></a>
The name of the filter.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** OperandFieldName **   <a name="QS-Type-TopicFilter-OperandFieldName"></a>
The name of the field that the filter operates on.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** CategoryFilter **   <a name="QS-Type-TopicFilter-CategoryFilter"></a>
The category filter that is associated with this filter.
Type: [TopicCategoryFilter](API_TopicCategoryFilter.md) object
Required: No

 ** DateRangeFilter **   <a name="QS-Type-TopicFilter-DateRangeFilter"></a>
The date range filter.
Type: [TopicDateRangeFilter](API_TopicDateRangeFilter.md) object
Required: No

 ** FilterClass **   <a name="QS-Type-TopicFilter-FilterClass"></a>
The class of the filter. Valid values for this structure are `ENFORCED_VALUE_FILTER`, `CONDITIONAL_VALUE_FILTER`, and `NAMED_VALUE_FILTER`.
Type: String
Valid Values: `ENFORCED_VALUE_FILTER | CONDITIONAL_VALUE_FILTER | NAMED_VALUE_FILTER`
Required: No

 ** FilterDescription **   <a name="QS-Type-TopicFilter-FilterDescription"></a>
A description of the filter used to select items for a topic.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** FilterSynonyms **   <a name="QS-Type-TopicFilter-FilterSynonyms"></a>
The other names or aliases for the filter.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

 ** FilterType **   <a name="QS-Type-TopicFilter-FilterType"></a>
The type of the filter. Valid values for this structure are `CATEGORY_FILTER`, `NUMERIC_EQUALITY_FILTER`, `NUMERIC_RANGE_FILTER`, `DATE_RANGE_FILTER`, and `RELATIVE_DATE_FILTER`.
Type: String
Valid Values: `CATEGORY_FILTER | NUMERIC_EQUALITY_FILTER | NUMERIC_RANGE_FILTER | DATE_RANGE_FILTER | RELATIVE_DATE_FILTER | NULL_FILTER`
Required: No

 ** NullFilter **   <a name="QS-Type-TopicFilter-NullFilter"></a>
The null filter.
Type: [TopicNullFilter](API_TopicNullFilter.md) object
Required: No

 ** NumericEqualityFilter **   <a name="QS-Type-TopicFilter-NumericEqualityFilter"></a>
The numeric equality filter.
Type: [TopicNumericEqualityFilter](API_TopicNumericEqualityFilter.md) object
Required: No

 ** NumericRangeFilter **   <a name="QS-Type-TopicFilter-NumericRangeFilter"></a>
The numeric range filter.
Type: [TopicNumericRangeFilter](API_TopicNumericRangeFilter.md) object
Required: No

 ** RelativeDateFilter **   <a name="QS-Type-TopicFilter-RelativeDateFilter"></a>
The relative date filter.
Type: [TopicRelativeDateFilter](API_TopicRelativeDateFilter.md) object
Required: No

## See Also
<a name="API_TopicFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicFilter)
