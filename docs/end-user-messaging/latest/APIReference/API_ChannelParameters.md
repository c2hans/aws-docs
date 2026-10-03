---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ChannelParameters.html
---

# ChannelParameters
<a name="API_ChannelParameters"></a>

The channel-specific parameters used to render and deliver a one-time passcode. Each member configures the parameters for one delivery route. Populate only the channels that a configuration or send request supports. A notify code configuration can carry every channel at once, and a send request resolves to a single route that selects the matching channel at send time.

## Contents
<a name="API_ChannelParameters_Contents"></a>

 ** notify **   <a name="endusermessaging-Type-ChannelParameters-notify"></a>
The parameters for the preapproved notify-template route over the SMS or voice channels.
Type: [NotifyParameters](API_NotifyParameters.md) object
Required: No

 ** text **   <a name="endusermessaging-Type-ChannelParameters-text"></a>
The parameters for the text channel, which delivers over SMS or RCS.
Type: [TextParameters](API_TextParameters.md) object
Required: No

 ** voice **   <a name="endusermessaging-Type-ChannelParameters-voice"></a>
The parameters for the voice channel.
Type: [VoiceParameters](API_VoiceParameters.md) object
Required: No

 ** whatsApp **   <a name="endusermessaging-Type-ChannelParameters-whatsApp"></a>
The parameters for the WhatsApp channel.
Type: [WhatsAppParameters](API_WhatsAppParameters.md) object
Required: No

## See Also
<a name="API_ChannelParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/ChannelParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/ChannelParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/ChannelParameters)
