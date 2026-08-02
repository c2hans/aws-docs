---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A tag is a key-value pair that can be used to manage, search for, or filter resources in AWS CodeArtifact.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="codeartifact-Type-Tag-key"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\P{C}+`
Required: Yes

 ** value **   <a name="codeartifact-Type-Tag-value"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\P{C}*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/Tag)
