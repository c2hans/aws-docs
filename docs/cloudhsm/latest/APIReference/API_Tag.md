---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Contains a tag. A tag is a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="CloudHSMV2-Type-Tag-Key"></a>
The key of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="CloudHSMV2-Type-Tag-Value"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Tag)
