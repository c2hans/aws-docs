---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantTimerConfiguration.html
---

# ParticipantTimerConfiguration
<a name="API_ParticipantTimerConfiguration"></a>

Configuration information for the timer. After the timer configuration is set, it persists for the duration of the chat. It persists across new contacts in the chain, for example, transfer contacts.

For more information about how chat timeouts work, see [Set up chat timeouts for human participants](https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html).

## Contents
<a name="API_ParticipantTimerConfiguration_Contents"></a>

 ** ParticipantRole **   <a name="connect-Type-ParticipantTimerConfiguration-ParticipantRole"></a>
The role of the participant in the chat conversation.
Type: String
Valid Values: `CUSTOMER | AGENT`
Required: Yes

 ** TimerType **   <a name="connect-Type-ParticipantTimerConfiguration-TimerType"></a>
The type of timer. `IDLE` indicates the timer applies for considering a human chat participant as idle. `DISCONNECT_NONCUSTOMER` indicates the timer applies to automatically disconnecting a chat participant due to idleness.
Type: String
Valid Values: `IDLE | DISCONNECT_NONCUSTOMER`
Required: Yes

 ** TimerValue **   <a name="connect-Type-ParticipantTimerConfiguration-TimerValue"></a>
The value of the timer. Either the timer action (Unset to delete the timer), or the duration of the timer in minutes. Only one value can be set.
Type: [ParticipantTimerValue](API_ParticipantTimerValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ParticipantTimerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantTimerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantTimerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantTimerConfiguration)
