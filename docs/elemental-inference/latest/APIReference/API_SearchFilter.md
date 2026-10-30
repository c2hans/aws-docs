---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_SearchFilter.html
---

# SearchFilter
<a name="API_SearchFilter"></a>

A filter for a fixture search. It is used in the filters array of a SearchFixtures request.

## Contents
<a name="API_SearchFilter_Contents"></a>

 ** name **   <a name="elementalinference-Type-SearchFilter-name"></a>
The dimension of the fixture to filter on. Valid values: COMPETITOR.
Type: String
Valid Values: `COMPETITOR`
Required: Yes

 ** values **   <a name="elementalinference-Type-SearchFilter-values"></a>
An array of values to match in the dimension that you specified in name. You can specify up to 10 values. A fixture appears in the results if it matches at least one of these values.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/SearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/SearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/SearchFilter)
