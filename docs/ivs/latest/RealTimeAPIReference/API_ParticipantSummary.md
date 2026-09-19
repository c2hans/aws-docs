---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantSummary.html
---

# ParticipantSummary
<a name="API_ParticipantSummary"></a>

Summary object describing a participant that has joined a stage.

## Contents
<a name="API_ParticipantSummary_Contents"></a>

 ** firstJoinTime **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-firstJoinTime"></a>
ISO 8601 timestamp (returned as a string) when the participant first joined the stage session.
Type: Timestamp
Required: No

 ** ingestConfigurationArn **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-ingestConfigurationArn"></a>
The participant’s ingest configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: No

 ** participantId **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-participantId"></a>
Unique identifier for this participant, assigned by IVS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** published **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-published"></a>
Whether the participant ever published to the stage session.
Type: Boolean
Required: No

 ** recordingState **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-recordingState"></a>
The participant’s recording state.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | STOPPED | FAILED | DISABLED`
Required: No

 ** redundantIngest **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the participant.
Type: Boolean
Required: No

 ** replicationState **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-replicationState"></a>
The participant's replication state.
Type: String
Valid Values: `ACTIVE | STOPPED`
Required: No

 ** replicationType **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-replicationType"></a>
Indicates if the participant has been replicated to another stage or is a replica from another stage. Default: `NONE`.
Type: String
Valid Values: `SOURCE | REPLICA | NONE`
Required: No

 ** sourceSessionId **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-sourceSessionId"></a>
ID of the session within the source stage, if `replicationType` is `REPLICA`.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** sourceStageArn **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-sourceStageArn"></a>
Source stage ARN from which this participant is replicated, if `replicationType` is `REPLICA`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: No

 ** state **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-state"></a>
Whether the participant is connected to or disconnected from the stage.
Type: String
Valid Values: `CONNECTED | DISCONNECTED`
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-ParticipantSummary-userId"></a>
Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_ParticipantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantSummary)
