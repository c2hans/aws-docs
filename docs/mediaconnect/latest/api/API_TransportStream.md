---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_TransportStream.html
---

# TransportStream
<a name="API_TransportStream"></a>

 The metadata of an elementary transport stream.

## Contents
<a name="API_TransportStream_Contents"></a>

 ** pid **   <a name="mediaconnect-Type-TransportStream-pid"></a>
 The Packet ID (PID) as it is reported in the Program Map Table.
Type: Integer
Required: Yes

 ** streamType **   <a name="mediaconnect-Type-TransportStream-streamType"></a>
 The Stream Type as it is reported in the Program Map Table.
Type: String
Required: Yes

 ** channels **   <a name="mediaconnect-Type-TransportStream-channels"></a>
 The number of channels in the audio stream.
Type: Integer
Required: No

 ** codec **   <a name="mediaconnect-Type-TransportStream-codec"></a>
 The codec used by the stream.
Type: String
Required: No

 ** frameRate **   <a name="mediaconnect-Type-TransportStream-frameRate"></a>
 The frame rate used by the video stream.
Type: String
Required: No

 ** frameResolution **   <a name="mediaconnect-Type-TransportStream-frameResolution"></a>
The frame resolution used by the video stream.
Type: [FrameResolution](API_FrameResolution.md) object
Required: No

 ** sampleRate **   <a name="mediaconnect-Type-TransportStream-sampleRate"></a>
 The sample rate used by the audio stream.
Type: Integer
Required: No

 ** sampleSize **   <a name="mediaconnect-Type-TransportStream-sampleSize"></a>
 The sample bit size used by the audio stream.
Type: Integer
Required: No

## See Also
<a name="API_TransportStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/TransportStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/TransportStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/TransportStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
