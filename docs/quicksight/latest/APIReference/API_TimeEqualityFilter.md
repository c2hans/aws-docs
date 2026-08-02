---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TimeEqualityFilter.html
---

# TimeEqualityFilter
<a name="API_TimeEqualityFilter"></a>

A `TimeEqualityFilter` filters values that are equal to a given value.

## Contents
<a name="API_TimeEqualityFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-TimeEqualityFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-TimeEqualityFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-TimeEqualityFilter-DefaultFilterControlConfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

 ** ParameterName **   <a name="QS-Type-TimeEqualityFilter-ParameterName"></a>
The parameter whose value should be used for the filter value.
This field is mutually exclusive to `Value` and `RollingDate`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** RollingDate **   <a name="QS-Type-TimeEqualityFilter-RollingDate"></a>
The rolling date input for the `TimeEquality` filter.
This field is mutually exclusive to `Value` and `ParameterName`.
Type: [RollingDateConfiguration](API_RollingDateConfiguration.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-TimeEqualityFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** Value **   <a name="QS-Type-TimeEqualityFilter-Value"></a>
The value of a `TimeEquality` filter.
This field is mutually exclusive to `RollingDate` and `ParameterName`.
Type: Timestamp
Required: No

## See Also
<a name="API_TimeEqualityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TimeEqualityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TimeEqualityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TimeEqualityFilter)
