---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VisibilityConditions.html
---

# VisibilityConditions
<a name="API_VisibilityConditions"></a>

The list of key-value pairs used to filter your search results. If a search result contains a key from your list, it is included in the final search response if the value associated with the key in the result matches the value you specified. If the value doesn't match, the result is excluded from the search response. Any resources that don't have a key from the list that you've provided will also be included in the search response.

## Contents
<a name="API_VisibilityConditions_Contents"></a>

 ** Key **   <a name="sagemaker-Type-VisibilityConditions-Key"></a>
The key that specifies the tag that you're using to filter the search results. It must be in the following format: `Tags.<key>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** Value **   <a name="sagemaker-Type-VisibilityConditions-Value"></a>
The value for the tag that you're using to filter the search results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_VisibilityConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/VisibilityConditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/VisibilityConditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/VisibilityConditions)
