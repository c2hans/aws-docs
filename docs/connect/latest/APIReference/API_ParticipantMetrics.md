---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantMetrics.html
---

# ParticipantMetrics
<a name="API_ParticipantMetrics"></a>

Information about a participant's interactions in a contact.

## Contents
<a name="API_ParticipantMetrics_Contents"></a>

 ** ConversationAbandon **   <a name="connect-Type-ParticipantMetrics-ConversationAbandon"></a>
A boolean flag indicating whether the chat conversation was abandoned by a Participant.
Type: Boolean
Required: No

 ** LastMessageTimestamp **   <a name="connect-Type-ParticipantMetrics-LastMessageTimestamp"></a>
Timestamp of last chat message by Participant.
Type: Timestamp
Required: No

 ** MaxResponseTimeInMillis **   <a name="connect-Type-ParticipantMetrics-MaxResponseTimeInMillis"></a>
Maximum chat response time by Participant.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MessageLengthInChars **   <a name="connect-Type-ParticipantMetrics-MessageLengthInChars"></a>
Number of chat characters sent by Participant.
Type: Integer
Required: No

 ** MessagesSent **   <a name="connect-Type-ParticipantMetrics-MessagesSent"></a>
Number of chat messages sent by Participant.
Type: Integer
Required: No

 ** NumResponses **   <a name="connect-Type-ParticipantMetrics-NumResponses"></a>
Number of chat messages sent by Participant.
Type: Integer
Required: No

 ** ParticipantId **   <a name="connect-Type-ParticipantMetrics-ParticipantId"></a>
The Participant's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ParticipantType **   <a name="connect-Type-ParticipantMetrics-ParticipantType"></a>
Information about the conversation participant. Following are the participant types: [Agent, Customer, Supervisor].
Type: String
Valid Values: `ALL | MANAGER | AGENT | CUSTOMER | THIRDPARTY`
Required: No

 ** TotalResponseTimeInMillis **   <a name="connect-Type-ParticipantMetrics-TotalResponseTimeInMillis"></a>
Total chat response time by Participant.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ParticipantMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantMetrics)
