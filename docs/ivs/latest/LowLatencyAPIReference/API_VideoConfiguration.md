---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_VideoConfiguration.html
---

# VideoConfiguration
<a name="API_VideoConfiguration"></a>

Object specifying a stream’s video configuration, as set up by the broadcaster (usually in an encoder). This is part of the [IngestConfigurations](API_IngestConfigurations.md) object and the deprecated [IngestConfiguration](API_IngestConfiguration.md) object. It is used for monitoring stream health.

## Contents
<a name="API_VideoConfiguration_Contents"></a>

 ** avcLevel **   <a name="ivs-Type-VideoConfiguration-avcLevel"></a>
(Deprecated) Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. For details, see the H.264 specification. This is populated only when VideoConfiguration is part of the deprecated IngestConfiguration; otherwise, this is an empty string.
Type: String
Required: No

 ** avcProfile **   <a name="ivs-Type-VideoConfiguration-avcProfile"></a>
(Deprecated) Indicates to the decoder the requirements for decoding the stream. For definitions of the valid values, see the H.264 specification. This is populated only when VideoConfiguration is part of the deprecated IngestConfiguration; otherwise, this is an empty string.
Type: String
Required: No

 ** codec **   <a name="ivs-Type-VideoConfiguration-codec"></a>
Codec used for the video encoding.
Type: String
Required: No

 ** encoder **   <a name="ivs-Type-VideoConfiguration-encoder"></a>
Software or hardware used to encode the video.
Type: String
Required: No

 ** level **   <a name="ivs-Type-VideoConfiguration-level"></a>
Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. When an AVC codec is used, this field has the same value as `avcLevel`.
Type: String
Required: No

 ** profile **   <a name="ivs-Type-VideoConfiguration-profile"></a>
Indicates to the decoder the requirements for decoding the stream. When an AVC codec is used, this field has the same value as `avcProfile`.
Type: String
Required: No

 ** targetBitrate **   <a name="ivs-Type-VideoConfiguration-targetBitrate"></a>
The expected ingest bitrate (bits per second). This is configured in the encoder.
Type: Long
Required: No

 ** targetFramerate **   <a name="ivs-Type-VideoConfiguration-targetFramerate"></a>
The expected ingest framerate. This is configured in the encoder.
Type: Long
Required: No

 ** track **   <a name="ivs-Type-VideoConfiguration-track"></a>
Name of the video track. If multitrack is not enabled, this is Track0 (the sole track).
Type: String
Required: No

 ** videoHeight **   <a name="ivs-Type-VideoConfiguration-videoHeight"></a>
Video-resolution height in pixels.
Type: Long
Required: No

 ** videoWidth **   <a name="ivs-Type-VideoConfiguration-videoWidth"></a>
Video-resolution width in pixels.
Type: Long
Required: No

## See Also
<a name="API_VideoConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/VideoConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/VideoConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/VideoConfiguration)
