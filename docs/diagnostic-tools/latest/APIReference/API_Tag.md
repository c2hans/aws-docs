---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Tag is key and value pair that act as metadata for organizing your AWS resources.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="diagnostictools-Type-Tag-key"></a>
Tag Key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!(?i)aws:).*`
Required: Yes

 ** value **   <a name="diagnostictools-Type-Tag-value"></a>
Value for the Tag key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/Tag)
