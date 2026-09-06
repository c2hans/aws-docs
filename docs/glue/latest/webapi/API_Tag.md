---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

The `Tag` object represents a label that you can assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define.

For more information about tags, and controlling access to resources in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) and [Specifying AWS Glue Resource ARNs](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) in the developer guide.

## Contents
<a name="API_Tag_Contents"></a>

 ** key **   <a name="Glue-Type-Tag-key"></a>
The tag key. The key is required when you create a tag on an object. The key is case-sensitive, and must not contain the prefix aws.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** value **   <a name="Glue-Type-Tag-value"></a>
The tag value. The value is optional when you create a tag on an object. The value is case-sensitive, and must not contain the prefix aws.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Tag)
