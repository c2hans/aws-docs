---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConflictingItem.html
---

# ConflictingItem
<a name="API_ConflictingItem"></a>

Information about a conflicting query used across different sets of featured results. When you create a featured results set, you must check that the queries are unique per featured results set for each index.

## Contents
<a name="API_ConflictingItem_Contents"></a>

 ** QueryText **   <a name="kendra-Type-ConflictingItem-QueryText"></a>
The text of the conflicting query.
Type: String
Required: No

 ** SetId **   <a name="kendra-Type-ConflictingItem-SetId"></a>
The identifier of the set of featured results that the conflicting query belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** SetName **   <a name="kendra-Type-ConflictingItem-SetName"></a>
The name for the set of featured results that the conflicting query belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ConflictingItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ConflictingItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ConflictingItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ConflictingItem)
