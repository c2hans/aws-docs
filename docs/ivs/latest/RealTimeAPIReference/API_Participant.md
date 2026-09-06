---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Participant.html
---

# Participant
<a name="API_Participant"></a>

Object describing a participant that has joined a stage.

## Contents
<a name="API_Participant_Contents"></a>

 ** attributes **   <a name="ivsrealtimeeapireference-Type-Participant-attributes"></a>
Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information*.
Type: String to string map
Required: No

 ** browserName **   <a name="ivsrealtimeeapireference-Type-Participant-browserName"></a>
The participant’s browser.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** browserVersion **   <a name="ivsrealtimeeapireference-Type-Participant-browserVersion"></a>
The participant’s browser version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** firstJoinTime **   <a name="ivsrealtimeeapireference-Type-Participant-firstJoinTime"></a>
ISO 8601 timestamp (returned as a string) when the participant first joined the stage session.
Type: Timestamp
Required: No

 ** ingestConfigurationArn **   <a name="ivsrealtimeeapireference-Type-Participant-ingestConfigurationArn"></a>
The participant’s ingest configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: No

 ** ispName **   <a name="ivsrealtimeeapireference-Type-Participant-ispName"></a>
The participant’s Internet Service Provider.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** osName **   <a name="ivsrealtimeeapireference-Type-Participant-osName"></a>
The participant’s operating system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** osVersion **   <a name="ivsrealtimeeapireference-Type-Participant-osVersion"></a>
The participant’s operating system version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** participantId **   <a name="ivsrealtimeeapireference-Type-Participant-participantId"></a>
Unique identifier for this participant, assigned by IVS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** protocol **   <a name="ivsrealtimeeapireference-Type-Participant-protocol"></a>
Type of ingest protocol that the participant employs for broadcasting.
Type: String
Valid Values: `UNKNOWN | WHIP | RTMP | RTMPS`
Required: No

 ** published **   <a name="ivsrealtimeeapireference-Type-Participant-published"></a>
Whether the participant ever published to the stage session.
Type: Boolean
Required: No

 ** recordingS3BucketName **   <a name="ivsrealtimeeapireference-Type-Participant-recordingS3BucketName"></a>
Name of the S3 bucket to where the participant is being recorded, if individual participant recording is enabled, or `""` (empty string), if recording is not enabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-z0-9-.]*`
Required: No

 ** recordingS3Prefix **   <a name="ivsrealtimeeapireference-Type-Participant-recordingS3Prefix"></a>
S3 prefix of the S3 bucket where the participant is being recorded, if individual participant recording is enabled, or `""` (empty string), if recording is not enabled. If individual participant recording merge is enabled, and if a stage publisher disconnects from a stage and then reconnects, IVS tries to record to the same S3 prefix as the previous session. See [ Merge Fragmented Individual Participant Recordings](/ivs/latest/RealTimeUserGuide/rt-individual-participant-recording.html#ind-part-rec-merge-frag).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** recordingState **   <a name="ivsrealtimeeapireference-Type-Participant-recordingState"></a>
The participant’s recording state.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | STOPPED | FAILED | DISABLED`
Required: No

 ** redundantIngest **   <a name="ivsrealtimeeapireference-Type-Participant-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the participant.
Type: Boolean
Required: No

 ** replicationState **   <a name="ivsrealtimeeapireference-Type-Participant-replicationState"></a>
The participant's replication state.
Type: String
Valid Values: `ACTIVE | STOPPED`
Required: No

 ** replicationType **   <a name="ivsrealtimeeapireference-Type-Participant-replicationType"></a>
Indicates if the participant has been replicated to another stage or is a replica from another stage. Default: `NONE`.
Type: String
Valid Values: `SOURCE | REPLICA | NONE`
Required: No

 ** sdkVersion **   <a name="ivsrealtimeeapireference-Type-Participant-sdkVersion"></a>
The participant’s SDK version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.,:;\s]*`
Required: No

 ** sourceSessionId **   <a name="ivsrealtimeeapireference-Type-Participant-sourceSessionId"></a>
ID of the session within the source stage, if `replicationType` is `REPLICA`.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** sourceStageArn **   <a name="ivsrealtimeeapireference-Type-Participant-sourceStageArn"></a>
Source stage ARN from which this participant is replicated, if `replicationType` is `REPLICA`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: No

 ** state **   <a name="ivsrealtimeeapireference-Type-Participant-state"></a>
Whether the participant is connected to or disconnected from the stage.
Type: String
Valid Values: `CONNECTED | DISCONNECTED`
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-Participant-userId"></a>
Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_Participant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Participant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Participant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Participant)
