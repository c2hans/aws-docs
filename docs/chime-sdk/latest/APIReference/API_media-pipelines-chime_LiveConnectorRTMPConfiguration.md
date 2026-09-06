---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_LiveConnectorRTMPConfiguration.html
---

# LiveConnectorRTMPConfiguration
<a name="API_media-pipelines-chime_LiveConnectorRTMPConfiguration"></a>

The media pipeline's RTMP configuration object.

## Contents
<a name="API_media-pipelines-chime_LiveConnectorRTMPConfiguration_Contents"></a>

 ** Url **   <a name="chimesdk-Type-media-pipelines-chime_LiveConnectorRTMPConfiguration-Url"></a>
The URL of the RTMP configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** AudioChannels **   <a name="chimesdk-Type-media-pipelines-chime_LiveConnectorRTMPConfiguration-AudioChannels"></a>
The audio channels set for the RTMP configuration
Type: String
Valid Values: `Stereo | Mono`
Required: No

 ** AudioSampleRate **   <a name="chimesdk-Type-media-pipelines-chime_LiveConnectorRTMPConfiguration-AudioSampleRate"></a>
The audio sample rate set for the RTMP configuration. Default: 48000.
Type: String
Pattern: `44100|48000`
Required: No

## See Also
<a name="API_media-pipelines-chime_LiveConnectorRTMPConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/LiveConnectorRTMPConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/LiveConnectorRTMPConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/LiveConnectorRTMPConfiguration)
