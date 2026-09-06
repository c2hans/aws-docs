---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiMediaStreamInfo.html
---

# NdiMediaStreamInfo
<a name="API_NdiMediaStreamInfo"></a>

 Detailed information about a single media stream that is part of an NDI® source. This includes details about the stream type, codec, resolution, frame rate, audio channels, and sample rate.

## Contents
<a name="API_NdiMediaStreamInfo_Contents"></a>

 ** codec **   <a name="mediaconnect-Type-NdiMediaStreamInfo-codec"></a>
 The codec used for the media stream. For NDI sources, use `speed-hq`.
Type: String
Required: Yes

 ** streamId **   <a name="mediaconnect-Type-NdiMediaStreamInfo-streamId"></a>
 A unique identifier for the media stream.
Type: Integer
Required: Yes

 ** streamType **   <a name="mediaconnect-Type-NdiMediaStreamInfo-streamType"></a>
 The type of media stream (for example, `Video` or `Audio`).
Type: String
Required: Yes

 ** channels **   <a name="mediaconnect-Type-NdiMediaStreamInfo-channels"></a>
 The number of audio channels in the stream. Used when the `streamType` is `Audio`.
Type: Integer
Required: No

 ** frameRate **   <a name="mediaconnect-Type-NdiMediaStreamInfo-frameRate"></a>
 The number of video frames displayed per second. Used when the `streamType` is `Video`.
Type: String
Required: No

 ** frameResolution **   <a name="mediaconnect-Type-NdiMediaStreamInfo-frameResolution"></a>
 The width and height dimensions of the video frame in pixels. Used when the `streamType` is `Video`.
Type: [FrameResolution](API_FrameResolution.md) object
Required: No

 ** sampleRate **   <a name="mediaconnect-Type-NdiMediaStreamInfo-sampleRate"></a>
 The number of audio samples captured per second, measured in kilohertz (kHz). Used when the `streamType` is `Audio`.
Type: Integer
Required: No

 ** scanMode **   <a name="mediaconnect-Type-NdiMediaStreamInfo-scanMode"></a>
 The method used to display video frames. Used when the `streamType` is `Video`.
Type: String
Valid Values: `progressive | interlace | progressive-segmented-frame`
Required: No

## See Also
<a name="API_NdiMediaStreamInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiMediaStreamInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiMediaStreamInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiMediaStreamInfo)
