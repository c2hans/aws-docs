---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantReplica.html
---

# ParticipantReplica
<a name="API_ParticipantReplica"></a>

Information about the replicated destination stage for a participant.

## Contents
<a name="API_ParticipantReplica_Contents"></a>

 ** destinationSessionId **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-destinationSessionId"></a>
ID of the session within the destination stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: Yes

 ** destinationStageArn **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-destinationStageArn"></a>
ARN of the stage where the participant is replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** participantId **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-participantId"></a>
Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by [CreateParticipantToken](API_CreateParticipantToken.md) or the `jti` (JWT ID) used to [ create a self signed token](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** replicationState **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-replicationState"></a>
Replica’s current replication state.
Type: String
Valid Values: `ACTIVE | STOPPED`
Required: Yes

 ** sourceSessionId **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-sourceSessionId"></a>
ID of the session within the source stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: Yes

 ** sourceStageArn **   <a name="ivsrealtimeeapireference-Type-ParticipantReplica-sourceStageArn"></a>
ARN of the stage from which this participant is replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## See Also
<a name="API_ParticipantReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantReplica)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
