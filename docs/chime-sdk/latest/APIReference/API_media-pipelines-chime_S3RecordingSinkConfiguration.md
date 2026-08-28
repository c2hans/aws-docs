---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html
---

# S3RecordingSinkConfiguration
<a name="API_media-pipelines-chime_S3RecordingSinkConfiguration"></a>

The structure that holds the settings for transmitting media to the Amazon S3 bucket. These values are used as defaults if `S3RecordingSinkRuntimeConfiguration` is not specified.

## Contents
<a name="API_media-pipelines-chime_S3RecordingSinkConfiguration_Contents"></a>

 ** Destination **   <a name="chimesdk-Type-media-pipelines-chime_S3RecordingSinkConfiguration-Destination"></a>
The default URI of the Amazon S3 bucket used as the recording sink.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** RecordingFileFormat **   <a name="chimesdk-Type-media-pipelines-chime_S3RecordingSinkConfiguration-RecordingFileFormat"></a>
The default file format for the media files sent to the Amazon S3 bucket.
Type: String
Valid Values: `Wav | Opus`
Required: No

## See Also
<a name="API_media-pipelines-chime_S3RecordingSinkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
