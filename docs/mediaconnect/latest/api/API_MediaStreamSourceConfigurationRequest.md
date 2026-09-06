---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaStreamSourceConfigurationRequest.html
---

# MediaStreamSourceConfigurationRequest
<a name="API_MediaStreamSourceConfigurationRequest"></a>

The media stream that you want to associate with the source, and the parameters for that association.

## Contents
<a name="API_MediaStreamSourceConfigurationRequest_Contents"></a>

 ** encodingName **   <a name="mediaconnect-Type-MediaStreamSourceConfigurationRequest-encodingName"></a>
The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
Type: String
Valid Values: `jxsv | raw | smpte291 | pcm`
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-MediaStreamSourceConfigurationRequest-mediaStreamName"></a>
The name of the media stream.
Type: String
Required: Yes

 ** inputConfigurations **   <a name="mediaconnect-Type-MediaStreamSourceConfigurationRequest-inputConfigurations"></a>
The media streams that you want to associate with the source.
Type: Array of [InputConfigurationRequest](API_InputConfigurationRequest.md) objects
Required: No

## See Also
<a name="API_MediaStreamSourceConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaStreamSourceConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaStreamSourceConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaStreamSourceConfigurationRequest)
