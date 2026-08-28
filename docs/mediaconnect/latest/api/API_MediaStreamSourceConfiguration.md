---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaStreamSourceConfiguration.html
---

# MediaStreamSourceConfiguration
<a name="API_MediaStreamSourceConfiguration"></a>

The media stream that is associated with the source, and the parameters for that association.

## Contents
<a name="API_MediaStreamSourceConfiguration_Contents"></a>

 ** encodingName **   <a name="mediaconnect-Type-MediaStreamSourceConfiguration-encodingName"></a>
 The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
Type: String
Valid Values: `jxsv | raw | smpte291 | pcm`
Required: Yes

 ** mediaStreamName **   <a name="mediaconnect-Type-MediaStreamSourceConfiguration-mediaStreamName"></a>
A name that helps you distinguish one media stream from another.
Type: String
Required: Yes

 ** inputConfigurations **   <a name="mediaconnect-Type-MediaStreamSourceConfiguration-inputConfigurations"></a>
The media streams that you want to associate with the source.
Type: Array of [InputConfiguration](API_InputConfiguration.md) objects
Required: No

## See Also
<a name="API_MediaStreamSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaStreamSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaStreamSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaStreamSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
