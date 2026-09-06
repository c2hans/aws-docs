---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StreamConfiguration.html
---

# StreamConfiguration
<a name="API_media-pipelines-chime_StreamConfiguration"></a>

The configuration settings for a stream.

## Contents
<a name="API_media-pipelines-chime_StreamConfiguration_Contents"></a>

 ** StreamArn **   <a name="chimesdk-Type-media-pipelines-chime_StreamConfiguration-StreamArn"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: Yes

 ** StreamChannelDefinition **   <a name="chimesdk-Type-media-pipelines-chime_StreamConfiguration-StreamChannelDefinition"></a>
The streaming channel definition in the stream configuration.
Type: [StreamChannelDefinition](API_media-pipelines-chime_StreamChannelDefinition.md) object
Required: Yes

 ** FragmentNumber **   <a name="chimesdk-Type-media-pipelines-chime_StreamConfiguration-FragmentNumber"></a>
The unique identifier of the fragment to begin processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_media-pipelines-chime_StreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/StreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/StreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/StreamConfiguration)
