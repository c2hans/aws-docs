---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ContextResourceTag.html
---

# ContextResourceTag
<a name="API_ContextResourceTag"></a>

A key-value pair representing a resource tag used to scope context content.

## Contents
<a name="API_ContextResourceTag_Contents"></a>

 ** key **   <a name="wellarchitected-Type-ContextResourceTag-key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: Yes

 ** value **   <a name="wellarchitected-Type-ContextResourceTag-value"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])*`
Required: Yes

## See Also
<a name="API_ContextResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ContextResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ContextResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ContextResourceTag)
