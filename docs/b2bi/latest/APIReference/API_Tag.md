---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to capabilities, partnerships, profiles and transformers. A tag key can take more than one value. For example, to group capabilities for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="b2bi-Type-Tag-Key"></a>
Specifies the name assigned to the tag that you create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="b2bi-Type-Tag-Value"></a>
Contains one or more values that you assigned to the key name that you create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/Tag)
