---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactSearchSummary.html
---

# ContactSearchSummary
<a name="API_ContactSearchSummary"></a>

Information of returned contact.

## Contents
<a name="API_ContactSearchSummary_Contents"></a>

 ** AgentInfo **   <a name="connect-Type-ContactSearchSummary-AgentInfo"></a>
Information about the agent who accepted the contact.
Type: [ContactSearchSummaryAgentInfo](API_ContactSearchSummaryAgentInfo.md) object
Required: No

 ** AiAgentInfo **   <a name="connect-Type-ContactSearchSummary-AiAgentInfo"></a>
Information about the AI agents involved in the contact.
Type: Array of [ContactSearchSummaryAiAgentInfo](API_ContactSearchSummaryAiAgentInfo.md) objects
Required: No

 ** Arn **   <a name="connect-Type-ContactSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the contact.
Type: String
Required: No

 ** Channel **   <a name="connect-Type-ContactSearchSummary-Channel"></a>
How the contact reached your contact center.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** DisconnectTimestamp **   <a name="connect-Type-ContactSearchSummary-DisconnectTimestamp"></a>
The timestamp when the customer endpoint disconnected from Connect Customer.
Type: Timestamp
Required: No

 ** GlobalResiliencyMetadata **   <a name="connect-Type-ContactSearchSummary-GlobalResiliencyMetadata"></a>
Additional routing information for contacts created in ACGR instances.
Type: [GlobalResiliencyMetadata](API_GlobalResiliencyMetadata.md) object
Required: No

 ** Id **   <a name="connect-Type-ContactSearchSummary-Id"></a>
The identifier of the contact summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitialContactId **   <a name="connect-Type-ContactSearchSummary-InitialContactId"></a>
If this contact is related to other contacts, this is the ID of the initial contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitiationMethod **   <a name="connect-Type-ContactSearchSummary-InitiationMethod"></a>
Indicates how the contact was initiated.
Type: String
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: No

 ** InitiationTimestamp **   <a name="connect-Type-ContactSearchSummary-InitiationTimestamp"></a>
The date and time this contact was initiated, in UTC time. For `INBOUND`, this is when the contact arrived. For `OUTBOUND`, this is when the agent began dialing. For `CALLBACK`, this is when the callback contact was created. For `TRANSFER` and `QUEUE_TRANSFER`, this is when the transfer was initiated. For API, this is when the request arrived. For `EXTERNAL_OUTBOUND`, this is when the agent started dialing the external participant. For `MONITOR`, this is when the supervisor started listening to a contact.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-ContactSearchSummary-Name"></a>
Indicates name of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** PreviousContactId **   <a name="connect-Type-ContactSearchSummary-PreviousContactId"></a>
If this contact is not the first contact, this is the ID of the previous contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** QueueInfo **   <a name="connect-Type-ContactSearchSummary-QueueInfo"></a>
If this contact was queued, this contains information about the queue.
Type: [ContactSearchSummaryQueueInfo](API_ContactSearchSummaryQueueInfo.md) object
Required: No

 ** RoutingCriteria **   <a name="connect-Type-ContactSearchSummary-RoutingCriteria"></a>
Latest routing criteria on the contact.
Type: [RoutingCriteria](API_RoutingCriteria.md) object
Required: No

 ** ScheduledTimestamp **   <a name="connect-Type-ContactSearchSummary-ScheduledTimestamp"></a>
The timestamp, in Unix epoch time format, at which to start running the inbound flow.
Type: Timestamp
Required: No

 ** SegmentAttributes **   <a name="connect-Type-ContactSearchSummary-SegmentAttributes"></a>
Set of segment attributes for a contact.
Type: String to [ContactSearchSummarySegmentAttributeValue](API_ContactSearchSummarySegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Tags **   <a name="connect-Type-ContactSearchSummary-Tags"></a>
Tags associated with the contact. This contains both AWS generated and user-defined tags.
Type: String to string map
Map Entries: Maximum number of 6 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ContactSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
