---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateChannelParameters.html
---

# UpdateChannelParameters
<a name="API_UpdateChannelParameters"></a>

The updated channel-specific parameters used only when you update a notify code configuration. When you omit a channel, that channel's parameters remain unchanged. When you supply a channel, you can clear individual fields by using the empty-string or empty-map sentinel on a member, or drop the whole channel's parameters by clearing every member. These sentinels apply only when you update a configuration; a create request rejects empty values with a validation error.

## Contents
<a name="API_UpdateChannelParameters_Contents"></a>

 ** notify **   <a name="endusermessaging-Type-UpdateChannelParameters-notify"></a>
The notify-template-route parameters to update. Omit this member to leave them unchanged.
Type: [UpdateNotifyParameters](API_UpdateNotifyParameters.md) object
Required: No

 ** text **   <a name="endusermessaging-Type-UpdateChannelParameters-text"></a>
The text-channel parameters to update. Omit this member to leave the text-channel parameters unchanged.
Type: [UpdateTextParameters](API_UpdateTextParameters.md) object
Required: No

 ** voice **   <a name="endusermessaging-Type-UpdateChannelParameters-voice"></a>
The voice-channel parameters to update. Omit this member to leave the voice-channel parameters unchanged.
Type: [UpdateVoiceParameters](API_UpdateVoiceParameters.md) object
Required: No

 ** whatsApp **   <a name="endusermessaging-Type-UpdateChannelParameters-whatsApp"></a>
The WhatsApp-channel parameters to update. Omit this member to leave the WhatsApp-channel parameters unchanged.
Type: [UpdateWhatsAppParameters](API_UpdateWhatsAppParameters.md) object
Required: No

## See Also
<a name="API_UpdateChannelParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateChannelParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateChannelParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateChannelParameters)
