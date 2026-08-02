---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnectorItem.html
---

# VoiceConnectorItem
<a name="API_voice-chime_VoiceConnectorItem"></a>

For Amazon Chime SDK Voice Connector groups, the Amazon Chime SDK Voice Connectors to which you route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Voice Connector group.

## Contents
<a name="API_voice-chime_VoiceConnectorItem_Contents"></a>

 ** Priority **   <a name="chimesdk-Type-voice-chime_VoiceConnectorItem-Priority"></a>
The priority setting of a Voice Connector item. Calls are routed to hosts in priority order, with 1 as the highest priority. When hosts have equal priority, the system distributes calls among them based on their relative weight.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99.
Required: Yes

 ** VoiceConnectorId **   <a name="chimesdk-Type-voice-chime_VoiceConnectorItem-VoiceConnectorId"></a>
The Voice Connector ID.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_voice-chime_VoiceConnectorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceConnectorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceConnectorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceConnectorItem)
