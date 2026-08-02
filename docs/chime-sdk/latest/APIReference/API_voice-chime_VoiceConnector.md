---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnector.html
---

# VoiceConnector
<a name="API_voice-chime_VoiceConnector"></a>

The Amazon Chime SDK Voice Connector configuration, including outbound host name and encryption settings.

## Contents
<a name="API_voice-chime_VoiceConnector_Contents"></a>

 ** AwsRegion **   <a name="chimesdk-Type-voice-chime_VoiceConnector-AwsRegion"></a>
The AWS Region in which the Voice Connector is created. Default: us-east-1.
Type: String
Valid Values: `us-east-1 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-2 | ap-northeast-1 | ap-southeast-1 | ap-southeast-2`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceConnector-CreatedTimestamp"></a>
The Voice Connector's creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** IntegrationType **   <a name="chimesdk-Type-voice-chime_VoiceConnector-IntegrationType"></a>
The connectors for use with Connect Customer.
Type: String
Valid Values: `CONNECT_CALL_TRANSFER_CONNECTOR | CONNECT_ANALYTICS_CONNECTOR`
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_VoiceConnector-Name"></a>
The Voice Connector's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** NetworkType **   <a name="chimesdk-Type-voice-chime_VoiceConnector-NetworkType"></a>
The type of network for the Voice Connector.
Type: String
Valid Values: `IPV4_ONLY | DUAL_STACK`
Required: No

 ** OutboundHostName **   <a name="chimesdk-Type-voice-chime_VoiceConnector-OutboundHostName"></a>
The outbound host name for the Voice Connector.
Type: String
Required: No

 ** RequireEncryption **   <a name="chimesdk-Type-voice-chime_VoiceConnector-RequireEncryption"></a>
Enables or disables encryption for the Voice Connector.
Type: Boolean
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceConnector-UpdatedTimestamp"></a>
The Voice Connector's updated timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** VoiceConnectorArn **   <a name="chimesdk-Type-voice-chime_VoiceConnector-VoiceConnectorArn"></a>
The ARN of the Voice Connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VoiceConnectorId **   <a name="chimesdk-Type-voice-chime_VoiceConnector-VoiceConnectorId"></a>
The Voice Connector's ID.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceConnector)
