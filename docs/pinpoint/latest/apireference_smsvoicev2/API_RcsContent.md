---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsContent.html
---

# RcsContent
<a name="API_RcsContent"></a>

The message body of an RCS message. Exactly one content type must be specified.

## Contents
<a name="API_RcsContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Carousel **   <a name="pinpoint-Type-RcsContent-Carousel"></a>
A carousel of 2 to 10 scrollable cards, each with media, title, description, and suggested actions.
Type: [RcsCarousel](API_RcsCarousel.md) object
Required: No

 ** FileMessage **   <a name="pinpoint-Type-RcsContent-FileMessage"></a>
A file message containing a media file (image, video, audio, or PDF) with an optional thumbnail.
Type: [RcsFileMessage](API_RcsFileMessage.md) object
Required: No

 ** RichCard **   <a name="pinpoint-Type-RcsContent-RichCard"></a>
A standalone rich card with media, title, description, and suggested actions.
Type: [RcsStandaloneCard](API_RcsStandaloneCard.md) object
Required: No

 ** TextMessage **   <a name="pinpoint-Type-RcsContent-TextMessage"></a>
A plain text RCS message.
Type: [RcsTextMessage](API_RcsTextMessage.md) object
Required: No

## See Also
<a name="API_RcsContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsContent)
