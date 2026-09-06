---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) action. To remove a tag, call the [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html) action.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="privateca-Type-Tag-Key"></a>
Key (name) of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="privateca-Type-Tag-Value"></a>
Value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/Tag)
