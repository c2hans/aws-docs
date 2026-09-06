---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair that identifies or specifies metadata about an ACM resource.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="ACM-Type-Tag-Key"></a>
The key of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="ACM-Type-Tag-Value"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/Tag)
