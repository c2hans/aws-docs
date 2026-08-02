---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_Tag.html
---

# Tag
<a name="API_marketplace-metering_Tag"></a>

Metadata assigned to an allocation. Each tag is made up of a `key` and a `value`.

## Contents
<a name="API_marketplace-metering_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSMarketplaceService-Type-marketplace-metering_Tag-Key"></a>
One part of a key-value pair that makes up a `tag`. A `key` is a label that acts like a category for the specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9+ -=._:\/@]+$`
Required: Yes

 ** Value **   <a name="AWSMarketplaceService-Type-marketplace-metering_Tag-Value"></a>
One part of a key-value pair that makes up a `tag`. A `value` acts as a descriptor within a tag category (key). The value can be empty or null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9+ -=._:\/@]+$`
Required: Yes

## See Also
<a name="API_marketplace-metering_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/Tag)
