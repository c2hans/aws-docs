---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StreamingConfiguration.html
---

# StreamingConfiguration
<a name="API_voice-chime_StreamingConfiguration"></a>

The streaming configuration associated with an Amazon Chime SDK Voice Connector. Specifies whether media streaming is enabled for sending to Amazon Kinesis, and shows the retention period for the Amazon Kinesis data, in hours.

## Contents
<a name="API_voice-chime_StreamingConfiguration_Contents"></a>

 ** DataRetentionInHours **   <a name="chimesdk-Type-voice-chime_StreamingConfiguration-DataRetentionInHours"></a>
The amount of time, in hours, to the Kinesis data.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Disabled **   <a name="chimesdk-Type-voice-chime_StreamingConfiguration-Disabled"></a>
When true, streaming to Kinesis is off.
Type: Boolean
Required: Yes

 ** MediaInsightsConfiguration **   <a name="chimesdk-Type-voice-chime_StreamingConfiguration-MediaInsightsConfiguration"></a>
The call analytics configuration.
Type: [MediaInsightsConfiguration](API_voice-chime_MediaInsightsConfiguration.md) object
Required: No

 ** StreamingNotificationTargets **   <a name="chimesdk-Type-voice-chime_StreamingConfiguration-StreamingNotificationTargets"></a>
The streaming notification targets.
Type: Array of [StreamingNotificationTarget](API_voice-chime_StreamingNotificationTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

## See Also
<a name="API_voice-chime_StreamingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/StreamingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/StreamingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/StreamingConfiguration)
