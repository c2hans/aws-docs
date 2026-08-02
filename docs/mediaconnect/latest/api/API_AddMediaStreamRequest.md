---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddMediaStreamRequest.html
---

# AddMediaStreamRequest
<a name="API_AddMediaStreamRequest"></a>

 The media stream that you want to add to the flow.

## Contents
<a name="API_AddMediaStreamRequest_Contents"></a>

 ** mediaStreamId **   <a name="mediaconnect-Type-AddMediaStreamRequest-mediaStreamId"></a>
 A unique identifier for the media stream.
Type: Integer
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-AddMediaStreamRequest-mediaStreamName"></a>
 A name that helps you distinguish one media stream from another.
Type: String
Required: Yes

 ** mediaStreamType **   <a name="mediaconnect-Type-AddMediaStreamRequest-mediaStreamType"></a>
 The type of media stream.
Type: String
Valid Values: `video | audio | ancillary-data`
Required: Yes

 ** attributes **   <a name="mediaconnect-Type-AddMediaStreamRequest-attributes"></a>
 The attributes that you want to assign to the new media stream.
Type: [MediaStreamAttributesRequest](API_MediaStreamAttributesRequest.md) object
Required: No

 ** clockRate **   <a name="mediaconnect-Type-AddMediaStreamRequest-clockRate"></a>
 The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000.
Type: Integer
Required: No

 ** description **   <a name="mediaconnect-Type-AddMediaStreamRequest-description"></a>
 A description that can help you quickly identify what your media stream is used for.
Type: String
Required: No

 ** mediaStreamTags **   <a name="mediaconnect-Type-AddMediaStreamRequest-mediaStreamTags"></a>
 The key-value pairs that can be used to tag and organize the media stream.
Type: String to string map
Required: No

 ** videoFormat **   <a name="mediaconnect-Type-AddMediaStreamRequest-videoFormat"></a>
 The resolution of the video.
Type: String
Required: No

## See Also
<a name="API_AddMediaStreamRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AddMediaStreamRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AddMediaStreamRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AddMediaStreamRequest)
