---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Message.html
---

# Message
<a name="API_Message"></a>

Represents the email message that you're sending. The `Message` object consists of a subject line and a message body.

## Contents
<a name="API_Message_Contents"></a>

 ** Body **   <a name="pinpoint-Type-Message-Body"></a>
The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.
Type: [Body](API_Body.md) object
Required: Yes

 ** Subject **   <a name="pinpoint-Type-Message-Subject"></a>
The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in [RFC 2047](https://tools.ietf.org/html/rfc2047).
Type: [Content](API_Content.md) object
Required: Yes

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/Message)
