---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopBottomFilter.html
---

# TopBottomFilter
<a name="API_TopBottomFilter"></a>

A `TopBottomFilter` filters values that are at the top or the bottom.

## Contents
<a name="API_TopBottomFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AggregationSortConfigurations **   <a name="QS-Type-TopBottomFilter-AggregationSortConfigurations"></a>
The aggregation and sort configuration of the top bottom filter.
Type: Array of [AggregationSortConfiguration](API_AggregationSortConfiguration.md) objects
Array Members: Maximum number of 100 items.
Required: Yes

 ** Column **   <a name="QS-Type-TopBottomFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-TopBottomFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-TopBottomFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** Limit **   <a name="QS-Type-TopBottomFilter-Limit"></a>
The number of items to include in the top bottom filter results.
Type: Integer
Required: No

 ** ParameterName **   <a name="QS-Type-TopBottomFilter-ParameterName"></a>
The parameter whose value should be used for the filter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopBottomFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

## See Also
<a name="API_TopBottomFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopBottomFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopBottomFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopBottomFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
