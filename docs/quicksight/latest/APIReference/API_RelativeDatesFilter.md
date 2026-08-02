---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RelativeDatesFilter.html
---

# RelativeDatesFilter
<a name="API_RelativeDatesFilter"></a>

A `RelativeDatesFilter` filters relative dates values.

## Contents
<a name="API_RelativeDatesFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnchorDateConfiguration **   <a name="QS-Type-RelativeDatesFilter-AnchorDateConfiguration"></a>
The date configuration of the filter.
Type: [AnchorDateConfiguration](API_AnchorDateConfiguration.md) object
Required: Yes

 ** Column **   <a name="QS-Type-RelativeDatesFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-RelativeDatesFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** NullOption **   <a name="QS-Type-RelativeDatesFilter-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: Yes

 ** RelativeDateType **   <a name="QS-Type-RelativeDatesFilter-RelativeDateType"></a>
The range date type of the filter. Choose one of the options below:
+  `PREVIOUS`
+  `THIS`
+  `LAST`
+  `NOW`
+  `NEXT`
Type: String
Valid Values: `PREVIOUS | THIS | LAST | NOW | NEXT`
Required: Yes

 ** TimeGranularity **   <a name="QS-Type-RelativeDatesFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-RelativeDatesFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** ExcludePeriodConfiguration **   <a name="QS-Type-RelativeDatesFilter-ExcludePeriodConfiguration"></a>
The configuration for the exclude period of the filter.
Type: [ExcludePeriodConfiguration](API_ExcludePeriodConfiguration.md) object
Required: No

 ** MinimumGranularity **   <a name="QS-Type-RelativeDatesFilter-MinimumGranularity"></a>
The minimum granularity (period granularity) of the relative dates filter.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** ParameterName **   <a name="QS-Type-RelativeDatesFilter-ParameterName"></a>
The parameter whose value should be used for the filter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** RelativeDateValue **   <a name="QS-Type-RelativeDatesFilter-RelativeDateValue"></a>
The date value of the filter.
Type: Integer
Required: No

## See Also
<a name="API_RelativeDatesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RelativeDatesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RelativeDatesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RelativeDatesFilter)
