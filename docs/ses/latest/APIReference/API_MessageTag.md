---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_MessageTag.html
---

# MessageTag
<a name="API_MessageTag"></a>

Contains the name and value of a tag that you can provide to `SendEmail` or `SendRawEmail` to apply to an email.

Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_MessageTag_Contents"></a>

 ** Name **
The name of the tag. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Contain 256 characters or fewer.
Type: String
Required: Yes

 ** Value **
The value of the tag. The value must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Contain 256 characters or fewer.
Type: String
Required: Yes

## See Also
<a name="API_MessageTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/MessageTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/MessageTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/MessageTag)
