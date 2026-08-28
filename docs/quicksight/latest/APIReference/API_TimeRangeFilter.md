---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TimeRangeFilter.html
---

# TimeRangeFilter
<a name="API_TimeRangeFilter"></a>

A `TimeRangeFilter` filters values that are between two specified values.

## Contents
<a name="API_TimeRangeFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-TimeRangeFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-TimeRangeFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** NullOption **   <a name="QS-Type-TimeRangeFilter-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-TimeRangeFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** ExcludePeriodConfiguration **   <a name="QS-Type-TimeRangeFilter-ExcludePeriodConfiguration"></a>
The exclude period of the time range filter.
Type: [ExcludePeriodConfiguration](API_ExcludePeriodConfiguration.md) object
Required: No

 ** IncludeMaximum **   <a name="QS-Type-TimeRangeFilter-IncludeMaximum"></a>
Determines whether the maximum value in the filter value range should be included in the filtered results.
Type: Boolean
Required: No

 ** IncludeMinimum **   <a name="QS-Type-TimeRangeFilter-IncludeMinimum"></a>
Determines whether the minimum value in the filter value range should be included in the filtered results.
Type: Boolean
Required: No

 ** RangeMaximumValue **   <a name="QS-Type-TimeRangeFilter-RangeMaximumValue"></a>
The maximum value for the filter value range.
Type: [TimeRangeFilterValue](API_TimeRangeFilterValue.md) object
Required: No

 ** RangeMinimumValue **   <a name="QS-Type-TimeRangeFilter-RangeMinimumValue"></a>
The minimum value for the filter value range.
Type: [TimeRangeFilterValue](API_TimeRangeFilterValue.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-TimeRangeFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

## See Also
<a name="API_TimeRangeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TimeRangeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TimeRangeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TimeRangeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
