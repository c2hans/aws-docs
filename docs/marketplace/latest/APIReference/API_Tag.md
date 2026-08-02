---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A list of objects specifying each key name and value.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSMarketplaceService-Type-Tag-Key"></a>
The key associated with the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="AWSMarketplaceService-Type-Tag-Value"></a>
The value associated with the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/Tag)
