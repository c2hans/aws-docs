---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_IngestConfiguration.html
---

# IngestConfiguration
<a name="API_IngestConfiguration"></a>

Object specifying the ingest configuration set up by the broadcaster, usually in an encoder.

 **Note:** IngestConfiguration is deprecated in favor of [IngestConfigurations](API_IngestConfigurations.md) but retained to ensure backward compatibility. If multitrack is not enabled, IngestConfiguration and IngestConfigurations contain the same data, namely information about Track0 (the sole track). If multitrack is enabled, IngestConfiguration contains data for only the first track (Track0) and IngestConfigurations contains data for all tracks.

## Contents
<a name="API_IngestConfiguration_Contents"></a>

 ** audio **   <a name="ivs-Type-IngestConfiguration-audio"></a>
Encoder settings for audio.
Type: [AudioConfiguration](API_AudioConfiguration.md) object
Required: No

 ** video **   <a name="ivs-Type-IngestConfiguration-video"></a>
Encoder settings for video.
Type: [VideoConfiguration](API_VideoConfiguration.md) object
Required: No

## See Also
<a name="API_IngestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/IngestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/IngestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/IngestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
