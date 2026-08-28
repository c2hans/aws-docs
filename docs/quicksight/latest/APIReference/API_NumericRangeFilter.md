---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NumericRangeFilter.html
---

# NumericRangeFilter
<a name="API_NumericRangeFilter"></a>

A `NumericRangeFilter` filters values that are within the value range.

## Contents
<a name="API_NumericRangeFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-NumericRangeFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-NumericRangeFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** NullOption **   <a name="QS-Type-NumericRangeFilter-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-NumericRangeFilter-AggregationFunction"></a>
The aggregation function of the filter.
Type: [AggregationFunction](API_AggregationFunction.md) object
Required: No

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-NumericRangeFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** IncludeMaximum **   <a name="QS-Type-NumericRangeFilter-IncludeMaximum"></a>
Determines whether the maximum value in the filter value range should be included in the filtered results.
Type: Boolean
Required: No

 ** IncludeMinimum **   <a name="QS-Type-NumericRangeFilter-IncludeMinimum"></a>
Determines whether the minimum value in the filter value range should be included in the filtered results.
Type: Boolean
Required: No

 ** RangeMaximum **   <a name="QS-Type-NumericRangeFilter-RangeMaximum"></a>
The maximum value for the filter value range.
Type: [NumericRangeFilterValue](API_NumericRangeFilterValue.md) object
Required: No

 ** RangeMinimum **   <a name="QS-Type-NumericRangeFilter-RangeMinimum"></a>
The minimum value for the filter value range.
Type: [NumericRangeFilterValue](API_NumericRangeFilterValue.md) object
Required: No

 ** SelectAllOptions **   <a name="QS-Type-NumericRangeFilter-SelectAllOptions"></a>
Select all of the values. Null is not the assigned value of select all.
+  `FILTER_ALL_VALUES`
Type: String
Valid Values: `FILTER_ALL_VALUES`
Required: No

## See Also
<a name="API_NumericRangeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NumericRangeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NumericRangeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NumericRangeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
