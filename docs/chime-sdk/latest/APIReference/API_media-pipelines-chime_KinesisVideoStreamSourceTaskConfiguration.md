---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration.html
---

# KinesisVideoStreamSourceTaskConfiguration
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration"></a>

The task configuration settings for the Kinesis video stream source.

## Contents
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration_Contents"></a>

 ** ChannelId **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration-ChannelId"></a>
The channel ID.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** StreamArn **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration-StreamArn"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: Yes

 ** FragmentNumber **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration-FragmentNumber"></a>
The unique identifier of the fragment to begin processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceTaskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceTaskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceTaskConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
