---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value*, both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: \_ . : / = \+ -. The following additional restrictions apply to tags:
+ Tag keys and values are case sensitive.
+ For each associated resource, each tag key must be unique and it can have only one value.
+ The `aws:` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can't edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
+ You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="SES-Type-Tag-Key"></a>
One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
Type: String
Required: Yes

 ** Value **   <a name="SES-Type-Tag-Value"></a>
The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don't want a resource to have a specific tag value, don't specify a value for this parameter. If you don't specify a value, Amazon SES sets the value to an empty string.
Type: String
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Tag)
