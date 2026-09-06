---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentContactReference.html
---

# AgentContactReference
<a name="API_AgentContactReference"></a>

Information about the [contact](https://docs.aws.amazon.com/connect/latest/APIReference/API_Contact.html) associated to the user.

## Contents
<a name="API_AgentContactReference_Contents"></a>

 ** AgentContactState **   <a name="connect-Type-AgentContactReference-AgentContactState"></a>
The [state of the contact](https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html).
When `AgentContactState` is set to `CONNECTED_ONHOLD`, `StateStartTimestamp` is not changed. Instead, `StateStartTimestamp` reflects the time the contact was `CONNECTED` to the agent.
Type: String
Valid Values: `INCOMING | PENDING | CONNECTING | CONNECTED | CONNECTED_ONHOLD | MISSED | ERROR | ENDED | REJECTED`
Required: No

 ** Channel **   <a name="connect-Type-AgentContactReference-Channel"></a>
The channel of the contact.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** ConnectedToAgentTimestamp **   <a name="connect-Type-AgentContactReference-ConnectedToAgentTimestamp"></a>
The time at which the contact was connected to an agent.
Type: Timestamp
Required: No

 ** ContactId **   <a name="connect-Type-AgentContactReference-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitiationMethod **   <a name="connect-Type-AgentContactReference-InitiationMethod"></a>
How the contact was initiated.
Type: String
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: No

 ** Queue **   <a name="connect-Type-AgentContactReference-Queue"></a>
Contains information about a queue resource for which metrics are returned.
Type: [QueueReference](API_QueueReference.md) object
Required: No

 ** StateStartTimestamp **   <a name="connect-Type-AgentContactReference-StateStartTimestamp"></a>
The epoch timestamp when the contact state started.
Type: Timestamp
Required: No

## See Also
<a name="API_AgentContactReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentContactReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentContactReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentContactReference)
