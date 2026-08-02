---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="ecrpublic-Type-Tag-Key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Value **   <a name="ecrpublic-Type-Tag-Value"></a>
The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/Tag)
