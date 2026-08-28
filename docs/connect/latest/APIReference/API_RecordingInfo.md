---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RecordingInfo.html
---

# RecordingInfo
<a name="API_RecordingInfo"></a>

Information about a voice recording, chat transcript, or screen recording.

## Contents
<a name="API_RecordingInfo_Contents"></a>

 ** DeletionReason **   <a name="connect-Type-RecordingInfo-DeletionReason"></a>
If the recording/transcript was deleted, this is the reason entered for the deletion.
Type: String
Required: No

 ** FragmentStartNumber **   <a name="connect-Type-RecordingInfo-FragmentStartNumber"></a>
The number that identifies the Kinesis Video Streams fragment where the customer audio stream started.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** FragmentStopNumber **   <a name="connect-Type-RecordingInfo-FragmentStopNumber"></a>
The number that identifies the Kinesis Video Streams fragment where the customer audio stream stopped.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Location **   <a name="connect-Type-RecordingInfo-Location"></a>
The location, in Amazon S3, for the recording/transcript.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** MediaStreamType **   <a name="connect-Type-RecordingInfo-MediaStreamType"></a>
Information about the media stream used during the conversation.
Type: String
Valid Values: `AUDIO | VIDEO`
Required: No

 ** ParticipantType **   <a name="connect-Type-RecordingInfo-ParticipantType"></a>
Information about the conversation participant, whether they are an agent or contact. The participant types are as follows:
+ All
+ Manager
+ Agent
+ Customer
+ Thirdparty
+ Supervisor
Type: String
Valid Values: `ALL | MANAGER | AGENT | CUSTOMER | THIRDPARTY`
Required: No

 ** StartTimestamp **   <a name="connect-Type-RecordingInfo-StartTimestamp"></a>
When the conversation of the last leg of the recording started in UTC time.
Type: Timestamp
Required: No

 ** Status **   <a name="connect-Type-RecordingInfo-Status"></a>
The status of the recording/transcript.
Type: String
Valid Values: `AVAILABLE | DELETED`
Required: No

 ** StopTimestamp **   <a name="connect-Type-RecordingInfo-StopTimestamp"></a>
When the conversation of the last leg of recording stopped in UTC time.
Type: Timestamp
Required: No

 ** StorageType **   <a name="connect-Type-RecordingInfo-StorageType"></a>
Where the recording/transcript is stored.
Type: String
Valid Values: `S3 | KINESIS_VIDEO_STREAM | KINESIS_STREAM | KINESIS_FIREHOSE`
Required: No

 ** UnprocessedTranscriptLocation **   <a name="connect-Type-RecordingInfo-UnprocessedTranscriptLocation"></a>
 The location, in Amazon S3, for the unprocessed transcript if any media processing was performed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_RecordingInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RecordingInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RecordingInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RecordingInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
