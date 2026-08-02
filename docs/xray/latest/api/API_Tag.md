---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A map that contains tag keys and tag values to attach to an AWS X-Ray group or sampling rule. For more information about ways to use tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.

The following restrictions apply to tags:
+ Maximum number of user-applied tags per resource: 50
+ Tag keys and values are case sensitive.
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use. You cannot edit or delete system tags.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="xray-Type-Tag-Key"></a>
A tag key, such as `Stage` or `Name`. A tag key cannot be empty. The key can be a maximum of 128 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="xray-Type-Tag-Value"></a>
An optional tag value, such as `Production` or `test-only`. The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Tag)
