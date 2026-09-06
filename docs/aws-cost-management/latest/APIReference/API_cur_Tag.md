---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_Tag.html
---

# Tag
<a name="API_cur_Tag"></a>

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a report definition.

## Contents
<a name="API_cur_Tag_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-cur_Tag-Key"></a>
The key of the tag. Tag keys are case sensitive. Each report definition can only have up to one tag with the same key. If you try to add an existing tag with the same key, the existing tag value will be updated to the new value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*`
Required: Yes

 ** Value **   <a name="awscostmanagement-Type-cur_Tag-Value"></a>
The value of the tag. Tag values are case-sensitive. This can be an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_cur_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/Tag)
