---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html
---

# S3RecordingSinkRuntimeConfiguration
<a name="API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration"></a>

A structure that holds the settings for transmitting media files to the Amazon S3 bucket. If specified, the settings in this structure override any settings in `S3RecordingSinkConfiguration`.

## Contents
<a name="API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration_Contents"></a>

 ** Destination **   <a name="chimesdk-Type-media-pipelines-chime_S3RecordingSinkRuntimeConfiguration-Destination"></a>
The URI of the S3 bucket used as the sink.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** RecordingFileFormat **   <a name="chimesdk-Type-media-pipelines-chime_S3RecordingSinkRuntimeConfiguration-RecordingFileFormat"></a>
The file format for the media files sent to the Amazon S3 bucket.
Type: String
Valid Values: `Wav | Opus`
Required: Yes

## See Also
<a name="API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkRuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkRuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/S3RecordingSinkRuntimeConfiguration)
