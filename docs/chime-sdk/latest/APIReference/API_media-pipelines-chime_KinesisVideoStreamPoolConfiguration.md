---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.html
---

# KinesisVideoStreamPoolConfiguration
<a name="API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration"></a>

The video stream pool configuration object.

## Contents
<a name="API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-CreatedTimestamp"></a>
The time at which the configuration was created.
Type: Timestamp
Required: No

 ** PoolArn **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-PoolArn"></a>
The ARN of the video stream pool configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** PoolId **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-PoolId"></a>
The ID of the video stream pool in the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** PoolName **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-PoolName"></a>
The name of the video stream pool configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** PoolSize **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-PoolSize"></a>
The size of the video stream pool in the configuration.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PoolStatus **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-PoolStatus"></a>
The status of the video stream pool in the configuration.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: No

 ** StreamConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-StreamConfiguration"></a>
The Kinesis video stream pool configuration object.
Type: [KinesisVideoStreamConfiguration](API_media-pipelines-chime_KinesisVideoStreamConfiguration.md) object
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamPoolConfiguration-UpdatedTimestamp"></a>
The time at which the configuration was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamPoolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamPoolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamPoolConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
