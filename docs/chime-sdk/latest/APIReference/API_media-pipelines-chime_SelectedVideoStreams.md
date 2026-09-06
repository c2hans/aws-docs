---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SelectedVideoStreams.html
---

# SelectedVideoStreams
<a name="API_media-pipelines-chime_SelectedVideoStreams"></a>

The video streams for a specified media pipeline. The total number of video streams can't exceed 25.

## Contents
<a name="API_media-pipelines-chime_SelectedVideoStreams_Contents"></a>

 ** AttendeeIds **   <a name="chimesdk-Type-media-pipelines-chime_SelectedVideoStreams-AttendeeIds"></a>
The attendee IDs of the streams selected for a media pipeline.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** ExternalUserIds **   <a name="chimesdk-Type-media-pipelines-chime_SelectedVideoStreams-ExternalUserIds"></a>
The external user IDs of the streams selected for a media pipeline.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

## See Also
<a name="API_media-pipelines-chime_SelectedVideoStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/SelectedVideoStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/SelectedVideoStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/SelectedVideoStreams)
