---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

**Important**
Do not include confidential or sensitive information in this field.

For more information, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *AWS Billing and Cost Management User Guide*.

## Contents
<a name="API_Tag_Contents"></a>

 ** TagKey **   <a name="qdevinchatapps-Type-Tag-TagKey"></a>
The key of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** TagValue **   <a name="qdevinchatapps-Type-Tag-TagValue"></a>
The value of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/Tag)
