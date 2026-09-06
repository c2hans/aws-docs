---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsMessageContent.html
---

# RcsMessageContent
<a name="API_RcsMessageContent"></a>

The content of an RCS message, containing the message body (text, file, rich card, or carousel) and optional message-level suggested actions.

## Contents
<a name="API_RcsMessageContent_Contents"></a>

 ** Content **   <a name="pinpoint-Type-RcsMessageContent-Content"></a>
The content of the RCS message. Exactly one content type must be specified: TextMessage, FileMessage, RichCard, or Carousel.
Type: [RcsContent](API_RcsContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Suggestions **   <a name="pinpoint-Type-RcsMessageContent-Suggestions"></a>
Message-level suggested actions displayed to the recipient. Maximum 11 suggestions per message.
Type: Array of [RcsSuggestedAction](API_RcsSuggestedAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Required: No

## See Also
<a name="API_RcsMessageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsMessageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsMessageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsMessageContent)
