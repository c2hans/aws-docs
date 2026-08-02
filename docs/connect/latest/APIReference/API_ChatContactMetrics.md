---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ChatContactMetrics.html
---

# ChatContactMetrics
<a name="API_ChatContactMetrics"></a>

Information about the overall participant interactions at the contact level.

## Contents
<a name="API_ChatContactMetrics_Contents"></a>

 ** AgentFirstResponseTimeInMillis **   <a name="connect-Type-ChatContactMetrics-AgentFirstResponseTimeInMillis"></a>
The time for an agent to respond after obtaining a chat contact.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** AgentFirstResponseTimestamp **   <a name="connect-Type-ChatContactMetrics-AgentFirstResponseTimestamp"></a>
The agent first response timestamp for a chat contact.
Type: Timestamp
Required: No

 ** ConversationCloseTimeInMillis **   <a name="connect-Type-ChatContactMetrics-ConversationCloseTimeInMillis"></a>
The time it took for a contact to end after the last customer message.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ConversationTurnCount **   <a name="connect-Type-ChatContactMetrics-ConversationTurnCount"></a>
The number of conversation turns in a chat contact, which represents the back-and-forth exchanges between customer and other participants.
Type: Integer
Required: No

 ** MultiParty **   <a name="connect-Type-ChatContactMetrics-MultiParty"></a>
A boolean flag indicating whether multiparty chat or supervisor barge were enabled on this contact.
Type: Boolean
Required: No

 ** TotalBotMessageLengthInChars **   <a name="connect-Type-ChatContactMetrics-TotalBotMessageLengthInChars"></a>
The total number of characters from bot and automated messages on a chat contact.
Type: Integer
Required: No

 ** TotalBotMessages **   <a name="connect-Type-ChatContactMetrics-TotalBotMessages"></a>
The total number of bot and automated messages on a chat contact.
Type: Integer
Required: No

 ** TotalMessages **   <a name="connect-Type-ChatContactMetrics-TotalMessages"></a>
The number of chat messages on the contact.
Type: Integer
Required: No

## See Also
<a name="API_ChatContactMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ChatContactMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ChatContactMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ChatContactMetrics)
