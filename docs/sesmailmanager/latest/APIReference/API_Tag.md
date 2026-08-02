---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair (the value is optional), that you can define and assign to AWS resources.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="sesmailmanager-Type-Tag-Key"></a>
The key of the key-value tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9/_\+=\.:@\-]+`
Required: Yes

 ** Value **   <a name="sesmailmanager-Type-Tag-Value"></a>
The value of the key-value tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9/_\+=\.:@\-]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Tag)
