---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_RecordingConfiguration.html
---

# RecordingConfiguration
<a name="API_RecordingConfiguration"></a>

An object representing a configuration to record a stage stream.

## Contents
<a name="API_RecordingConfiguration_Contents"></a>

 ** format **   <a name="ivsrealtimeeapireference-Type-RecordingConfiguration-format"></a>
The recording format for storing a recording in Amazon S3.
Type: String
Valid Values: `HLS`
Required: No

 ** hlsConfiguration **   <a name="ivsrealtimeeapireference-Type-RecordingConfiguration-hlsConfiguration"></a>
An HLS configuration object to return information about how the recording will be configured.
Type: [CompositionRecordingHlsConfiguration](API_CompositionRecordingHlsConfiguration.md) object
Required: No

## See Also
<a name="API_RecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/RecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/RecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/RecordingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
