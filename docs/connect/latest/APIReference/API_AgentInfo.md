---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentInfo.html
---

# AgentInfo
<a name="API_AgentInfo"></a>

Information about the agent who accepted the contact.

## Contents
<a name="API_AgentInfo_Contents"></a>

 ** AcceptedByAgentTimestamp **   <a name="connect-Type-AgentInfo-AcceptedByAgentTimestamp"></a>
The timestamp when the contact was accepted by the agent.
Type: Timestamp
Required: No

 ** AfterContactWorkDuration **   <a name="connect-Type-AgentInfo-AfterContactWorkDuration"></a>
The difference in time, in whole seconds, between `AfterContactWorkStartTimestamp` and `AfterContactWorkEndTimestamp`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** AfterContactWorkEndTimestamp **   <a name="connect-Type-AgentInfo-AfterContactWorkEndTimestamp"></a>
The date and time when the agent ended After Contact Work for the contact, in UTC time. In cases when agent finishes doing `AfterContactWork` for chat contacts and switches their activity status to offline or equivalent without clearing the contact in CCP, discrepancies may be noticed for `AfterContactWorkEndTimestamp`.
Type: Timestamp
Required: No

 ** AfterContactWorkStartTimestamp **   <a name="connect-Type-AgentInfo-AfterContactWorkStartTimestamp"></a>
The date and time when the agent started doing After Contact Work for the contact, in UTC time.
Type: Timestamp
Required: No

 ** AgentInitiatedHoldDuration **   <a name="connect-Type-AgentInfo-AgentInitiatedHoldDuration"></a>
The total hold duration in seconds initiated by the agent.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** AgentPauseDurationInSeconds **   <a name="connect-Type-AgentInfo-AgentPauseDurationInSeconds"></a>
Agent pause duration for a contact in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Capabilities **   <a name="connect-Type-AgentInfo-Capabilities"></a>
The configuration for the allowed video and screen sharing capabilities for participants present over the call. For more information, see [Set up in-app, web, video calling, and screen sharing capabilities](https://docs.aws.amazon.com/connect/latest/adminguide/inapp-calling.html) in the *Connect Customer Administrator Guide*.
Type: [ParticipantCapabilities](API_ParticipantCapabilities.md) object
Required: No

 ** ConnectedToAgentTimestamp **   <a name="connect-Type-AgentInfo-ConnectedToAgentTimestamp"></a>
The timestamp when the contact was connected to the agent.
Type: Timestamp
Required: No

 ** DeviceInfo **   <a name="connect-Type-AgentInfo-DeviceInfo"></a>
Information regarding Agent’s device.
Type: [DeviceInfo](API_DeviceInfo.md) object
Required: No

 ** HierarchyGroups **   <a name="connect-Type-AgentInfo-HierarchyGroups"></a>
The agent hierarchy groups for the agent.
Type: [HierarchyGroups](API_HierarchyGroups.md) object
Required: No

 ** Id **   <a name="connect-Type-AgentInfo-Id"></a>
The identifier of the agent who accepted the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** PreviewEndTimestamp **   <a name="connect-Type-AgentInfo-PreviewEndTimestamp"></a>
The timestamp when the agent finished previewing the contact.
Type: Timestamp
Required: No

 ** StateTransitions **   <a name="connect-Type-AgentInfo-StateTransitions"></a>
List of `StateTransition` for a supervisor.
Type: Array of [StateTransition](API_StateTransition.md) objects
Required: No

 ** VoiceEnhancementMode **   <a name="connect-Type-AgentInfo-VoiceEnhancementMode"></a>
The voice enhancement mode used by the agent as the call is ending. Valid values: VOICE\_ISOLATION \| NOISE\_SUPPRESSION \| NONE. A value of null indicates this mode has not yet been set for this user.
Type: String
Valid Values: `VOICE_ISOLATION | NOISE_SUPPRESSION | NONE`
Required: No

## See Also
<a name="API_AgentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentInfo)
