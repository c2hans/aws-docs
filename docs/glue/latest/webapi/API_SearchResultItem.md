---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchResultItem.html
---

# SearchResultItem
<a name="API_SearchResultItem"></a>

A single search result item representing a matched asset.

## Contents
<a name="API_SearchResultItem_Contents"></a>

 ** AssetDescription **   <a name="Glue-Type-SearchResultItem-AssetDescription"></a>
The description of the matched asset.
Type: String
Required: No

 ** AssetName **   <a name="Glue-Type-SearchResultItem-AssetName"></a>
The name of the matched asset.
Type: String
Required: No

 ** AssetTypeId **   <a name="Glue-Type-SearchResultItem-AssetTypeId"></a>
The identifier of the asset type for the matched asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Id **   <a name="Glue-Type-SearchResultItem-Id"></a>
The unique identifier of the matched asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: No

 ** UpdatedAt **   <a name="Glue-Type-SearchResultItem-UpdatedAt"></a>
The timestamp at which the matched asset was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_SearchResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchResultItem)
