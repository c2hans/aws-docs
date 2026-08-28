---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_S3DestinationConfiguration.html
---

# S3DestinationConfiguration
<a name="API_S3DestinationConfiguration"></a>

A complex type that describes an S3 location where recorded videos will be stored.

## Contents
<a name="API_S3DestinationConfiguration_Contents"></a>

 ** encoderConfigurationArns **   <a name="ivsrealtimeeapireference-Type-S3DestinationConfiguration-encoderConfigurationArns"></a>
ARNs of the [EncoderConfiguration](API_EncoderConfiguration.md) resource. The encoder configuration and stage resources must be in the same AWS account and region.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** storageConfigurationArn **   <a name="ivsrealtimeeapireference-Type-S3DestinationConfiguration-storageConfigurationArn"></a>
ARN of the [StorageConfiguration](API_StorageConfiguration.md) where recorded videos will be stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** recordingConfiguration **   <a name="ivsrealtimeeapireference-Type-S3DestinationConfiguration-recordingConfiguration"></a>
Array of maps, each of the form `string:string (key:value)`. This is an optional customer specification, currently used only to specify the recording format for storing a recording in Amazon S3.
Type: [RecordingConfiguration](API_RecordingConfiguration.md) object
Required: No

 ** thumbnailConfigurations **   <a name="ivsrealtimeeapireference-Type-S3DestinationConfiguration-thumbnailConfigurations"></a>
A complex type that allows you to enable/disable the recording of thumbnails for a [Composition](API_Composition.md) and modify the interval at which thumbnails are generated for the live session.
Type: Array of [CompositionThumbnailConfiguration](API_CompositionThumbnailConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_S3DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/S3DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/S3DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/S3DestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
