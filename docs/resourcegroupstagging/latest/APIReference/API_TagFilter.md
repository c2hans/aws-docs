---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

A list of tags (keys and values) that are used to specify the associated resources.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** Key **   <a name="resourcegrouptagging-Type-TagFilter-Key"></a>
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: No

 ** Values **   <a name="resourcegrouptagging-Type-TagFilter-Values"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/TagFilter)
