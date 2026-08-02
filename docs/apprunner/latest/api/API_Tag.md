---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Describes a tag that is applied to an AWS App Runner resource. A tag is a metadata item consisting of a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="apprunner-Type-Tag-Key"></a>
The key of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:).+`
Required: No

 ** Value **   <a name="apprunner-Type-Tag-Value"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/Tag)
