---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SpeakerSearchTask.html
---

# SpeakerSearchTask
<a name="API_voice-chime_SpeakerSearchTask"></a>

A representation of an asynchronous request to perform speaker search analysis on a Voice Connector call.

## Contents
<a name="API_voice-chime_SpeakerSearchTask_Contents"></a>

 ** CallDetails **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-CallDetails"></a>
The call details of a speaker search task.
Type: [CallDetails](API_voice-chime_CallDetails.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-CreatedTimestamp"></a>
The time at which a speaker search task was created.
Type: Timestamp
Required: No

 ** SpeakerSearchDetails **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-SpeakerSearchDetails"></a>
The details of a speaker search task.
Type: [SpeakerSearchDetails](API_voice-chime_SpeakerSearchDetails.md) object
Required: No

 ** SpeakerSearchTaskId **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-SpeakerSearchTaskId"></a>
The speaker search task ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** SpeakerSearchTaskStatus **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-SpeakerSearchTaskStatus"></a>
The status of the speaker search task, `IN_QUEUE`, `IN_PROGRESS`, `PARTIAL_SUCCESS`, `SUCCEEDED`, `FAILED`, or `STOPPED`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StartedTimestamp **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-StartedTimestamp"></a>
The time at which the speaker search task began.
Type: Timestamp
Required: No

 ** StatusMessage **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-StatusMessage"></a>
A detailed message about the status of a speaker search.
Type: String
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_SpeakerSearchTask-UpdatedTimestamp"></a>
The time at which a speaker search task was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_voice-chime_SpeakerSearchTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SpeakerSearchTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SpeakerSearchTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SpeakerSearchTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
