---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaStream.html
---

# MediaStream
<a name="API_MediaStream"></a>

 A media stream represents one component of your content, such as video, audio, or ancillary data. After you add a media stream to your flow, you can associate it with sources and outputs that use the ST 2110 JPEG XS or CDI protocol.

## Contents
<a name="API_MediaStream_Contents"></a>

 ** fmt **   <a name="mediaconnect-Type-MediaStream-fmt"></a>
 The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.
Type: Integer
Required: Yes

 ** mediaStreamId **   <a name="mediaconnect-Type-MediaStream-mediaStreamId"></a>
 A unique identifier for the media stream.
Type: Integer
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-MediaStream-mediaStreamName"></a>
 A name that helps you distinguish one media stream from another.
Type: String
Required: Yes

 ** mediaStreamType **   <a name="mediaconnect-Type-MediaStream-mediaStreamType"></a>
 The type of media stream.
Type: String
Valid Values: `video | audio | ancillary-data`
Required: Yes

 ** attributes **   <a name="mediaconnect-Type-MediaStream-attributes"></a>
 Attributes that are related to the media stream.
Type: [MediaStreamAttributes](API_MediaStreamAttributes.md) object
Required: No

 ** clockRate **   <a name="mediaconnect-Type-MediaStream-clockRate"></a>
 The sample rate for the stream. This value is measured in Hz.
Type: Integer
Required: No

 ** description **   <a name="mediaconnect-Type-MediaStream-description"></a>
 A description that can help you quickly identify what your media stream is used for.
Type: String
Required: No

 ** videoFormat **   <a name="mediaconnect-Type-MediaStream-videoFormat"></a>
 The resolution of the video.
Type: String
Required: No

## See Also
<a name="API_MediaStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
