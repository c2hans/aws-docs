---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaStreamOutputConfigurationRequest.html
---

# MediaStreamOutputConfigurationRequest
<a name="API_MediaStreamOutputConfigurationRequest"></a>

 The media stream that you want to associate with the output, and the parameters for that association.

## Contents
<a name="API_MediaStreamOutputConfigurationRequest_Contents"></a>

 ** encodingName **   <a name="mediaconnect-Type-MediaStreamOutputConfigurationRequest-encodingName"></a>
 The format that will be used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
Type: String
Valid Values: `jxsv | raw | smpte291 | pcm`
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-MediaStreamOutputConfigurationRequest-mediaStreamName"></a>
 The name of the media stream that is associated with the output.
Type: String
Required: Yes

 ** destinationConfigurations **   <a name="mediaconnect-Type-MediaStreamOutputConfigurationRequest-destinationConfigurations"></a>
 The media streams that you want to associate with the output.
Type: Array of [DestinationConfigurationRequest](API_DestinationConfigurationRequest.md) objects
Required: No

 ** encodingParameters **   <a name="mediaconnect-Type-MediaStreamOutputConfigurationRequest-encodingParameters"></a>
 A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.
Type: [EncodingParametersRequest](API_EncodingParametersRequest.md) object
Required: No

## See Also
<a name="API_MediaStreamOutputConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaStreamOutputConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaStreamOutputConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaStreamOutputConfigurationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
