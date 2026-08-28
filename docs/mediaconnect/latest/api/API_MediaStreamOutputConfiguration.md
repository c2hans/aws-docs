---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaStreamOutputConfiguration.html
---

# MediaStreamOutputConfiguration
<a name="API_MediaStreamOutputConfiguration"></a>

 The media stream that is associated with the output, and the parameters for that association.

## Contents
<a name="API_MediaStreamOutputConfiguration_Contents"></a>

 ** encodingName **   <a name="mediaconnect-Type-MediaStreamOutputConfiguration-encodingName"></a>
 The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
Type: String
Valid Values: `jxsv | raw | smpte291 | pcm`
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-MediaStreamOutputConfiguration-mediaStreamName"></a>
 The name of the media stream.
Type: String
Required: Yes

 ** destinationConfigurations **   <a name="mediaconnect-Type-MediaStreamOutputConfiguration-destinationConfigurations"></a>
 The transport parameters that are associated with each outbound media stream.
Type: Array of [DestinationConfiguration](API_DestinationConfiguration.md) objects
Required: No

 ** encodingParameters **   <a name="mediaconnect-Type-MediaStreamOutputConfiguration-encodingParameters"></a>
A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.
Type: [EncodingParameters](API_EncodingParameters.md) object
Required: No

## See Also
<a name="API_MediaStreamOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaStreamOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaStreamOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaStreamOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
