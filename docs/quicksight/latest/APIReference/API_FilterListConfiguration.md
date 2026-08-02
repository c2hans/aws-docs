---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterListConfiguration.html
---

# FilterListConfiguration
<a name="API_FilterListConfiguration"></a>

A list of filter configurations.

## Contents
<a name="API_FilterListConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MatchOperator **   <a name="QS-Type-FilterListConfiguration-MatchOperator"></a>
The match operator that is used to determine if a filter should be applied.
Type: String
Valid Values: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
Required: Yes

 ** CategoryValues **   <a name="QS-Type-FilterListConfiguration-CategoryValues"></a>
The list of category values for the filter.
Type: Array of strings
Array Members: Maximum number of 100000 items.
Length Constraints: Maximum length of 512.
Required: No

 ** NullOption **   <a name="QS-Type-FilterListConfiguration-NullOption"></a>
This option determines how null values should be treated when filtering data.
+  `ALL_VALUES`: Include null values in filtered results.
+  `NULLS_ONLY`: Only include null values in filtered results.
+  `NON_NULLS_ONLY`: Exclude null values from filtered results.
Type: String
Valid Values: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
Required: No

 ** SelectAllOptions **   <a name="QS-Type-FilterListConfiguration-SelectAllOptions"></a>
Select all of the values. Null is not the assigned value of select all.
+  `FILTER_ALL_VALUES`
Type: String
Valid Values: `FILTER_ALL_VALUES`
Required: No

## See Also
<a name="API_FilterListConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterListConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterListConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterListConfiguration)
