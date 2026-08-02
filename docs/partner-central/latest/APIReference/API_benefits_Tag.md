---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_Tag.html
---

# Tag
<a name="API_benefits_Tag"></a>

Represents a key-value pair used for categorizing and organizing AWS resources.

## Contents
<a name="API_benefits_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-benefits_Tag-Key"></a>
The tag key, which acts as a category or label for the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-benefits_Tag-Value"></a>
The tag value, which provides additional information or context for the tag key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## See Also
<a name="API_benefits_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/Tag)
