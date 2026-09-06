---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_MessageTag.html
---

# MessageTag
<a name="API_MessageTag"></a>

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.

## Contents
<a name="API_MessageTag_Contents"></a>

 ** Name **   <a name="pinpoint-Type-MessageTag-Name"></a>
The name of the message tag. The message tag name has to meet the following criteria:
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String
Required: Yes

 ** Value **   <a name="pinpoint-Type-MessageTag-Value"></a>
The value of the message tag. The message tag value has to meet the following criteria:
+ It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String
Required: Yes

## See Also
<a name="API_MessageTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/MessageTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/MessageTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/MessageTag)
