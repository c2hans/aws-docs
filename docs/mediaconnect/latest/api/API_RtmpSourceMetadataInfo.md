---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpSourceMetadataInfo.html
---

# RtmpSourceMetadataInfo
<a name="API_RtmpSourceMetadataInfo"></a>

Information about the RTMP (Real-Time Messaging Protocol) source. This includes the application name, the stream name, and metadata about the audio and video streams.

## Contents
<a name="API_RtmpSourceMetadataInfo_Contents"></a>

 ** mediaInfo **   <a name="mediaconnect-Type-RtmpSourceMetadataInfo-mediaInfo"></a>
Information about the audio and video streams that are part of the RTMP source.
Type: [RtmpMediaInfo](API_RtmpMediaInfo.md) object
Required: Yes

 ** applicationName **   <a name="mediaconnect-Type-RtmpSourceMetadataInfo-applicationName"></a>
The name of the RTMP application.
Type: String
Required: No

 ** streamName **   <a name="mediaconnect-Type-RtmpSourceMetadataInfo-streamName"></a>
The name of the RTMP stream.
Type: String
Required: No

## See Also
<a name="API_RtmpSourceMetadataInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpSourceMetadataInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpSourceMetadataInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpSourceMetadataInfo)
