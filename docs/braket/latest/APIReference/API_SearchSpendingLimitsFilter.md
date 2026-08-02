---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchSpendingLimitsFilter.html
---

# SearchSpendingLimitsFilter
<a name="API_SearchSpendingLimitsFilter"></a>

Specifies filter criteria for searching spending limits. Use filters to narrow down results based on specific attributes.

## Contents
<a name="API_SearchSpendingLimitsFilter_Contents"></a>

 ** name **   <a name="braket-Type-SearchSpendingLimitsFilter-name"></a>
The name of the field to filter on. Currently supports `deviceArn` and `spendingLimitArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** operator **   <a name="braket-Type-SearchSpendingLimitsFilter-operator"></a>
The comparison operator to use when filtering.
Type: String
Valid Values: `EQUAL`
Required: Yes

 ** values **   <a name="braket-Type-SearchSpendingLimitsFilter-values"></a>
An array of values to match against the specified field.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SearchSpendingLimitsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchSpendingLimitsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchSpendingLimitsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchSpendingLimitsFilter)
