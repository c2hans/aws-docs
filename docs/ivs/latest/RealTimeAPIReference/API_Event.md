---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

An occurrence during a stage session.

## Contents
<a name="API_Event_Contents"></a>

 ** destinationSessionId **   <a name="ivsrealtimeeapireference-Type-Event-destinationSessionId"></a>
ID of the session within the destination stage. Applicable only if the event name is `REPLICATION_STARTED` or `REPLICATION_STOPPED`.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** destinationStageArn **   <a name="ivsrealtimeeapireference-Type-Event-destinationStageArn"></a>
ARN of the stage where the participant is replicated. Applicable only if the event name is `REPLICATION_STARTED` or `REPLICATION_STOPPED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: No

 ** errorCode **   <a name="ivsrealtimeeapireference-Type-Event-errorCode"></a>
If the event is an error event, the error code is provided to give insight into the specific error that occurred. If the event is not an error event, this field is null.
+  `B_FRAME_PRESENT` — The participant's stream includes B-frames. For details, see [ IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html).
+  `BITRATE_EXCEEDED` — The participant exceeded the maximum supported bitrate. For details, see [ Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html).
+  `INSUFFICIENT_CAPABILITIES` — The participant tried to take an action that the participant’s token is not allowed to do. For details on participant capabilities, see the `capabilities` field in [CreateParticipantToken](API_CreateParticipantToken.md).
+  `INTERNAL_SERVER_EXCEPTION` — The participant failed to publish to the stage due to an internal server error.
+  `INVALID_AUDIO_CODEC` — The participant is using an invalid audio codec. For details, see [ Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html).
+  `INVALID_INPUT` — The participant is using an invalid input stream.
+  `INVALID_PROTOCOL` — The participant's IngestConfiguration resource is configured for RTMPS but they tried streaming with RTMP. For details, see [ IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html).
+  `INVALID_STREAM_KEY` — The participant is using an invalid stream key. For details, see [ IVS RTMP Publishing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html).
+  `INVALID_VIDEO_CODEC` — The participant is using an invalid video codec. For details, see [ Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html).
+  `PUBLISHER_NOT_FOUND` — The participant tried to subscribe to a publisher that doesn’t exist.
+  `QUOTA_EXCEEDED` — The number of participants who want to publish/subscribe to a stage exceeds the quota. For details, see [ Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html).
+  `RESOLUTION_EXCEEDED` — The participant exceeded the maximum supported resolution. For details, see [ Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html).
+  `REUSE_OF_STREAM_KEY` — The participant tried to use a stream key that is associated with another active stage session.
+  `STREAM_DURATION_EXCEEDED` — The participant exceeded the maximum allowed stream duration. For details, see [ Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html).
Type: String
Valid Values: `INSUFFICIENT_CAPABILITIES | QUOTA_EXCEEDED | PUBLISHER_NOT_FOUND | BITRATE_EXCEEDED | RESOLUTION_EXCEEDED | STREAM_DURATION_EXCEEDED | INVALID_AUDIO_CODEC | INVALID_VIDEO_CODEC | INVALID_PROTOCOL | INVALID_STREAM_KEY | REUSE_OF_STREAM_KEY | B_FRAME_PRESENT | INVALID_INPUT | INTERNAL_SERVER_EXCEPTION`
Required: No

 ** eventTime **   <a name="ivsrealtimeeapireference-Type-Event-eventTime"></a>
ISO 8601 timestamp (returned as a string) for when the event occurred.
Type: Timestamp
Required: No

 ** name **   <a name="ivsrealtimeeapireference-Type-Event-name"></a>
The name of the event.
Type: String
Valid Values: `JOINED | LEFT | PUBLISH_STARTED | PUBLISH_STOPPED | SUBSCRIBE_STARTED | SUBSCRIBE_STOPPED | PUBLISH_ERROR | SUBSCRIBE_ERROR | JOIN_ERROR | REPLICATION_STARTED | REPLICATION_STOPPED | TOKEN_EXCHANGED`
Required: No

 ** newToken **   <a name="ivsrealtimeeapireference-Type-Event-newToken"></a>
Participant token created during `TOKEN_EXCHANGED` event.
Type: [ExchangedParticipantToken](API_ExchangedParticipantToken.md) object
Required: No

 ** participantId **   <a name="ivsrealtimeeapireference-Type-Event-participantId"></a>
Unique identifier for the participant who triggered the event. This is assigned by IVS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** previousToken **   <a name="ivsrealtimeeapireference-Type-Event-previousToken"></a>
Source participant token for `TOKEN_EXCHANGED` event.
Type: [ExchangedParticipantToken](API_ExchangedParticipantToken.md) object
Required: No

 ** remoteParticipantId **   <a name="ivsrealtimeeapireference-Type-Event-remoteParticipantId"></a>
Unique identifier for the remote participant. For a subscribe event, this is the publisher. For a publish or join event, this is null. This is assigned by IVS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** replica **   <a name="ivsrealtimeeapireference-Type-Event-replica"></a>
If true, this indicates the `participantId` is a replicated participant. If this is a subscribe event, then this flag refers to `remoteParticipantId`. Default: `false`.
Type: Boolean
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
