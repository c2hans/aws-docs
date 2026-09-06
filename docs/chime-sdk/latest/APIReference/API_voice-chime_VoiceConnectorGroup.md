---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnectorGroup.html
---

# VoiceConnectorGroup
<a name="API_voice-chime_VoiceConnectorGroup"></a>

The Amazon Chime SDK Voice Connector group configuration, including associated Voice Connectors. You can include Voice Connectors from different AWS Regions in a group. This creates a fault tolerant mechanism for fallback in case of availability events.

## Contents
<a name="API_voice-chime_VoiceConnectorGroup_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-CreatedTimestamp"></a>
The Voice Connector group's creation time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-Name"></a>
The name of a Voice Connector group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-UpdatedTimestamp"></a>
The Voice Connector group's creation time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** VoiceConnectorGroupArn **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-VoiceConnectorGroupArn"></a>
The ARN of the Voice Connector group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VoiceConnectorGroupId **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-VoiceConnectorGroupId"></a>
The ID of a Voice Connector group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VoiceConnectorItems **   <a name="chimesdk-Type-voice-chime_VoiceConnectorGroup-VoiceConnectorItems"></a>
The Voice Connectors to which you route inbound calls.
Type: Array of [VoiceConnectorItem](API_voice-chime_VoiceConnectorItem.md) objects
Required: No

## See Also
<a name="API_voice-chime_VoiceConnectorGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceConnectorGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceConnectorGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceConnectorGroup)
