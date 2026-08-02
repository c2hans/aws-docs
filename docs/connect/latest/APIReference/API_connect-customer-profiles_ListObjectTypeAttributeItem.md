---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListObjectTypeAttributeItem.html
---

# ListObjectTypeAttributeItem
<a name="API_connect-customer-profiles_ListObjectTypeAttributeItem"></a>

Item that contains the attribute and when it was last updated.

## Contents
<a name="API_connect-customer-profiles_ListObjectTypeAttributeItem_Contents"></a>

 ** AttributeName **   <a name="connect-Type-connect-customer-profiles_ListObjectTypeAttributeItem-AttributeName"></a>
Name of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListObjectTypeAttributeItem-LastUpdatedAt"></a>
When the attribute was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ListObjectTypeAttributeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListObjectTypeAttributeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListObjectTypeAttributeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListObjectTypeAttributeItem)
