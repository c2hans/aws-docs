---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamSource.html
---

# MediaStreamSource
<a name="API_media-pipelines-chime_MediaStreamSource"></a>

Structure that contains the settings for media stream sources.

## Contents
<a name="API_media-pipelines-chime_MediaStreamSource_Contents"></a>

 ** SourceArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSource-SourceArn"></a>
The ARN of the meeting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** SourceType **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSource-SourceType"></a>
The type of media stream source.
Type: String
Valid Values: `ChimeSdkMeeting`
Required: Yes

## See Also
<a name="API_media-pipelines-chime_MediaStreamSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaStreamSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaStreamSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaStreamSource)
