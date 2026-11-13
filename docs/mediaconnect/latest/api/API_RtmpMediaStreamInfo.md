---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpMediaStreamInfo.html
---

# RtmpMediaStreamInfo
<a name="API_RtmpMediaStreamInfo"></a>

Information about a single audio or video stream that is part of an RTMP source. This includes details about the stream type, codec, resolution, frame rate, audio channels, and sample rate.

## Contents
<a name="API_RtmpMediaStreamInfo_Contents"></a>

 ** codec **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-codec"></a>
The codec used for the stream.
Type: String
Required: Yes

 ** streamId **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-streamId"></a>
A unique identifier for the stream.
Type: Integer
Required: Yes

 ** streamType **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-streamType"></a>
The type of stream (for example, `VIDEO` or `AUDIO`).
Type: String
Valid Values: `VIDEO | AUDIO | DATA | UNKNOWN`
Required: Yes

 ** channels **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-channels"></a>
The number of audio channels in the stream. Used when the `streamType` is `AUDIO`.
Type: Integer
Required: No

 ** color **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-color"></a>
The color signaling of the video stream. Used when the `streamType` is `VIDEO`.
Type: [ColorInformation](API_ColorInformation.md) object
Required: No

 ** frameRate **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-frameRate"></a>
The number of video frames displayed per second. Used when the `streamType` is `VIDEO`.
Type: String
Required: No

 ** frameResolution **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-frameResolution"></a>
The width and height dimensions of the video frame in pixels. Used when the `streamType` is `VIDEO`.
Type: [FrameResolution](API_FrameResolution.md) object
Required: No

 ** language **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-language"></a>
The language of the audio stream. Used when the `streamType` is `AUDIO`.
Type: String
Required: No

 ** sampleRate **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-sampleRate"></a>
The number of audio samples captured per second. Used when the `streamType` is `AUDIO`.
Type: Integer
Required: No

 ** sampleSize **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-sampleSize"></a>
The sample bit size used by the audio stream. Used when the `streamType` is `AUDIO`.
Type: Integer
Required: No

 ** scanMode **   <a name="mediaconnect-Type-RtmpMediaStreamInfo-scanMode"></a>
The method used to display video frames. Used when the `streamType` is `VIDEO`.
Type: String
Valid Values: `progressive | interlace | progressive-segmented-frame`
Required: No

## See Also
<a name="API_RtmpMediaStreamInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpMediaStreamInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpMediaStreamInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpMediaStreamInfo)
