---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="servicecatalog-Type-Tag-Key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="servicecatalog-Type-Tag-Value"></a>
The value for this key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/Tag)
