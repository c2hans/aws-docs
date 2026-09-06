---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VoiceToneAnalysisTask.html
---

# VoiceToneAnalysisTask
<a name="API_media-pipelines-chime_VoiceToneAnalysisTask"></a>

A representation of an asynchronous request to perform voice tone analysis on a media insights pipeline.

## Contents
<a name="API_media-pipelines-chime_VoiceToneAnalysisTask_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_VoiceToneAnalysisTask-CreatedTimestamp"></a>
The time at which a voice tone analysis task was created.
Type: Timestamp
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_VoiceToneAnalysisTask-UpdatedTimestamp"></a>
The time at which a voice tone analysis task was updated.
Type: Timestamp
Required: No

 ** VoiceToneAnalysisTaskId **   <a name="chimesdk-Type-media-pipelines-chime_VoiceToneAnalysisTask-VoiceToneAnalysisTaskId"></a>
The ID of the voice tone analysis task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** VoiceToneAnalysisTaskStatus **   <a name="chimesdk-Type-media-pipelines-chime_VoiceToneAnalysisTask-VoiceToneAnalysisTaskStatus"></a>
The status of a voice tone analysis task.
Type: String
Valid Values: `NotStarted | Initializing | InProgress | Failed | Stopping | Stopped`
Required: No

## See Also
<a name="API_media-pipelines-chime_VoiceToneAnalysisTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/VoiceToneAnalysisTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/VoiceToneAnalysisTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/VoiceToneAnalysisTask)
