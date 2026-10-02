---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair associated with a resource for cost allocation and access control.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="wellarchitected-Type-Tag-key"></a>
The key of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
Required: Yes

 ** value **   <a name="wellarchitected-Type-Tag-value"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Tag)
