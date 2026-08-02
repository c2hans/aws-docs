---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomFilterConfiguration.html
---

# CustomFilterConfiguration
<a name="API_CustomFilterConfiguration"></a>

A custom filter that filters based on a single value. This filter can be partially matched.

## Contents
<a name="API_CustomFilterConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MatchOperator **   <a name="QS-Type-CustomFilterConfiguration-MatchOperator"></a>
The match operator that is used to determine if a filter should be applied.
Type: String
Valid Values: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
Required: Yes

 ** NullOption **   <a name="QS-Type-CustomFilterConfiguration-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: Yes

 ** CategoryValue **   <a name="QS-Type-CustomFilterConfiguration-CategoryValue"></a>
The category value for the filter.
This field is mutually exclusive to `ParameterName`.
Type: String
Length Constraints: Maximum length of 512.
Required: No

 ** ParameterName **   <a name="QS-Type-CustomFilterConfiguration-ParameterName"></a>
The parameter whose value should be used for the filter value.
This field is mutually exclusive to `CategoryValue`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** SelectAllOptions **   <a name="QS-Type-CustomFilterConfiguration-SelectAllOptions"></a>
Select all of the values. Null is not the assigned value of select all.
+  `FILTER_ALL_VALUES`
Type: String
Valid Values: `FILTER_ALL_VALUES`
Required: No

## See Also
<a name="API_CustomFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomFilterConfiguration)
