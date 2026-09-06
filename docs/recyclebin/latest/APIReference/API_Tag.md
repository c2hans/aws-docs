---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Information about the tags to assign to the retention rule.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="recyclebin-Type-Tag-Key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="recyclebin-Type-Tag-Value"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/Tag)
