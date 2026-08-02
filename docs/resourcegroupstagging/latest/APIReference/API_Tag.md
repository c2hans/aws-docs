---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="resourcegrouptagging-Type-Tag-Key"></a>
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="resourcegrouptagging-Type-Tag-Value"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/Tag)
