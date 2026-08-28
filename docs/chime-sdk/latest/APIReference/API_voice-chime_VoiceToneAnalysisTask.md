---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceToneAnalysisTask.html
---

# VoiceToneAnalysisTask
<a name="API_voice-chime_VoiceToneAnalysisTask"></a>

A representation of an asynchronous request to perform voice tone analysis on a Voice Connector call.

## Contents
<a name="API_voice-chime_VoiceToneAnalysisTask_Contents"></a>

 ** CallDetails **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-CallDetails"></a>
The call details of a voice tone analysis task.
Type: [CallDetails](API_voice-chime_CallDetails.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-CreatedTimestamp"></a>
The time at which a voice tone analysis task was created.
Type: Timestamp
Required: No

 ** StartedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-StartedTimestamp"></a>
The time at which a voice tone analysis task started.
Type: Timestamp
Required: No

 ** StatusMessage **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-StatusMessage"></a>
The status of a voice tone analysis task.
Type: String
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-UpdatedTimestamp"></a>
The time at which a voice tone analysis task was updated.
Type: Timestamp
Required: No

 ** VoiceToneAnalysisTaskId **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-VoiceToneAnalysisTaskId"></a>
The ID of the voice tone analysis task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** VoiceToneAnalysisTaskStatus **   <a name="chimesdk-Type-voice-chime_VoiceToneAnalysisTask-VoiceToneAnalysisTaskStatus"></a>
The status of a voice tone analysis task, `IN_QUEUE`, `IN_PROGRESS`, `PARTIAL_SUCCESS`, `SUCCEEDED`, `FAILED`, or `STOPPED`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceToneAnalysisTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceToneAnalysisTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceToneAnalysisTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceToneAnalysisTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
