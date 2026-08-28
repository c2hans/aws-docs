---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SpeakerSearchTask.html
---

# SpeakerSearchTask
<a name="API_media-pipelines-chime_SpeakerSearchTask"></a>

A representation of an asynchronous request to perform speaker search analysis on a media insights pipeline.

## Contents
<a name="API_media-pipelines-chime_SpeakerSearchTask_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_SpeakerSearchTask-CreatedTimestamp"></a>
The time at which a speaker search task was created.
Type: Timestamp
Required: No

 ** SpeakerSearchTaskId **   <a name="chimesdk-Type-media-pipelines-chime_SpeakerSearchTask-SpeakerSearchTaskId"></a>
The speaker search task ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** SpeakerSearchTaskStatus **   <a name="chimesdk-Type-media-pipelines-chime_SpeakerSearchTask-SpeakerSearchTaskStatus"></a>
The status of the speaker search task.
Type: String
Valid Values: `NotStarted | Initializing | InProgress | Failed | Stopping | Stopped`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_SpeakerSearchTask-UpdatedTimestamp"></a>
The time at which a speaker search task was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_SpeakerSearchTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/SpeakerSearchTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/SpeakerSearchTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/SpeakerSearchTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
