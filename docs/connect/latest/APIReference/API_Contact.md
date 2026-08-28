---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Contact.html
---

# Contact
<a name="API_Contact"></a>

Contains information about a contact.

## Contents
<a name="API_Contact_Contents"></a>

 ** AdditionalEmailRecipients **   <a name="connect-Type-Contact-AdditionalEmailRecipients"></a>
List of additional email addresses for an email contact.
Type: [AdditionalEmailRecipients](API_AdditionalEmailRecipients.md) object
Required: No

 ** AgentInfo **   <a name="connect-Type-Contact-AgentInfo"></a>
Information about the agent who accepted the contact.
Type: [AgentInfo](API_AgentInfo.md) object
Required: No

 ** AnsweringMachineDetectionStatus **   <a name="connect-Type-Contact-AnsweringMachineDetectionStatus"></a>
Indicates how an [outbound campaign](https://docs.aws.amazon.com/connect/latest/adminguide/how-to-create-campaigns.html) call is actually disposed if the contact is connected to Connect Customer.
Type: String
Valid Values: `ANSWERED | UNDETECTED | ERROR | HUMAN_ANSWERED | SIT_TONE_DETECTED | SIT_TONE_BUSY | SIT_TONE_INVALID_NUMBER | FAX_MACHINE_DETECTED | VOICEMAIL_BEEP | VOICEMAIL_NO_BEEP | AMD_UNRESOLVED | AMD_UNANSWERED | AMD_ERROR | AMD_NOT_APPLICABLE`
Required: No

 ** Arn **   <a name="connect-Type-Contact-Arn"></a>
The Amazon Resource Name (ARN) for the contact.
Type: String
Required: No

 ** Attributes **   <a name="connect-Type-Contact-Attributes"></a>
The attributes of the contact.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** Campaign **   <a name="connect-Type-Contact-Campaign"></a>
Information associated with a campaign.
Type: [Campaign](API_Campaign.md) object
Required: No

 ** Channel **   <a name="connect-Type-Contact-Channel"></a>
How the contact reached your contact center.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** ChatMetrics **   <a name="connect-Type-Contact-ChatMetrics"></a>
Information about how agent, bot, and customer interact in a chat contact.
Type: [ChatMetrics](API_ChatMetrics.md) object
Required: No

 ** ConnectedToSystemTimestamp **   <a name="connect-Type-Contact-ConnectedToSystemTimestamp"></a>
The timestamp when customer endpoint connected to Connect Customer.
Type: Timestamp
Required: No

 ** ContactAssociationId **   <a name="connect-Type-Contact-ContactAssociationId"></a>
This is the root contactId which is used as a unique identifier for all subsequent contacts in a contact tree.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ContactDetails **   <a name="connect-Type-Contact-ContactDetails"></a>
A map of string key/value pairs that contain user-defined attributes which are lightly typed within the contact. This object is used only for task contacts.
Type: [ContactDetails](API_ContactDetails.md) object
Required: No

 ** ContactEvaluations **   <a name="connect-Type-Contact-ContactEvaluations"></a>
Information about the contact evaluations where the key is the FormId, which is a unique identifier for the form.
Type: String to [ContactEvaluation](API_ContactEvaluation.md) object map
Required: No

 ** Customer **   <a name="connect-Type-Contact-Customer"></a>
Information about the Customer on the contact.
Type: [Customer](API_Customer.md) object
Required: No

 ** CustomerEndpoint **   <a name="connect-Type-Contact-CustomerEndpoint"></a>
The customer or external third party participant endpoint.
Type: [EndpointInfo](API_EndpointInfo.md) object
Required: No

 ** CustomerId **   <a name="connect-Type-Contact-CustomerId"></a>
The customer's identification number. For example, the `CustomerId` may be a customer number from your CRM. You can create a Lambda function to pull the unique customer ID of the caller from your CRM system. If you enable Connect Customer Voice ID capability, this attribute is populated with the `CustomerSpeakerId` of the caller.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** CustomerVoiceActivity **   <a name="connect-Type-Contact-CustomerVoiceActivity"></a>
Information about customer’s voice activity.
Type: [CustomerVoiceActivity](API_CustomerVoiceActivity.md) object
Required: No

 ** Description **   <a name="connect-Type-Contact-Description"></a>
The description of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** DisconnectDetails **   <a name="connect-Type-Contact-DisconnectDetails"></a>
Information about the call disconnect experience.
Type: [DisconnectDetails](API_DisconnectDetails.md) object
Required: No

 ** DisconnectReason **   <a name="connect-Type-Contact-DisconnectReason"></a>
The disconnect reason for the contact. For a list and description of all the possible disconnect reasons by channel, see DisconnectReason under [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) in the *Connect Customer Administrator Guide*.
Type: String
Required: No

 ** DisconnectTimestamp **   <a name="connect-Type-Contact-DisconnectTimestamp"></a>
The date and time that the customer endpoint disconnected from the current contact, in UTC time. In transfer scenarios, the DisconnectTimestamp of the previous contact indicates the date and time when that contact ended.
Type: Timestamp
Required: No

 ** GlobalResiliencyMetadata **   <a name="connect-Type-Contact-GlobalResiliencyMetadata"></a>
Information about the global resiliency configuration for the contact, including traffic distribution details.
Type: [GlobalResiliencyMetadata](API_GlobalResiliencyMetadata.md) object
Required: No

 ** Id **   <a name="connect-Type-Contact-Id"></a>
The identifier for the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitialContactId **   <a name="connect-Type-Contact-InitialContactId"></a>
If this contact is related to other contacts, this is the ID of the initial contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitiationMethod **   <a name="connect-Type-Contact-InitiationMethod"></a>
Indicates how the contact was initiated.
Type: String
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: No

 ** InitiationTimestamp **   <a name="connect-Type-Contact-InitiationTimestamp"></a>
The date and time this contact was initiated, in UTC time. For `INBOUND`, this is when the contact arrived. For `OUTBOUND`, this is when the agent began dialing. For `CALLBACK`, this is when the callback contact was created. For `TRANSFER` and `QUEUE_TRANSFER`, this is when the transfer was initiated. For `API`, this is when the request arrived. For `EXTERNAL_OUTBOUND`, this is when the agent started dialing the external participant. For `MONITOR`, this is when the supervisor started listening to a contact.
Type: Timestamp
Required: No

 ** LastPausedTimestamp **   <a name="connect-Type-Contact-LastPausedTimestamp"></a>
The timestamp when the contact was last paused.
Type: Timestamp
Required: No

 ** LastResumedTimestamp **   <a name="connect-Type-Contact-LastResumedTimestamp"></a>
The timestamp when the contact was last resumed.
Type: Timestamp
Required: No

 ** LastUpdateTimestamp **   <a name="connect-Type-Contact-LastUpdateTimestamp"></a>
The timestamp when contact was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-Contact-Name"></a>
The name of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** NextContacts **   <a name="connect-Type-Contact-NextContacts"></a>
 List of next contact entries for the contact.
Type: Array of [NextContactEntry](API_NextContactEntry.md) objects
Array Members: Maximum number of 24 items.
Required: No

 ** OutboundStrategy **   <a name="connect-Type-Contact-OutboundStrategy"></a>
Information about the outbound strategy.
Type: [OutboundStrategy](API_OutboundStrategy.md) object
Required: No

 ** PreviousContactId **   <a name="connect-Type-Contact-PreviousContactId"></a>
If this contact is not the first contact, this is the ID of the previous contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** QualityMetrics **   <a name="connect-Type-Contact-QualityMetrics"></a>
Information about the quality of the participant's media connection.
Type: [QualityMetrics](API_QualityMetrics.md) object
Required: No

 ** QueueInfo **   <a name="connect-Type-Contact-QueueInfo"></a>
If this contact was queued, this contains information about the queue.
Type: [QueueInfo](API_QueueInfo.md) object
Required: No

 ** QueuePriority **   <a name="connect-Type-Contact-QueuePriority"></a>
An integer that represents the queue priority to be applied to the contact (lower priorities are routed preferentially). Cannot be specified if the QueueTimeAdjustmentSeconds is specified. Must be statically defined, must be larger than zero, and a valid integer value. Default Value is 5.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 9223372036854775807.
Required: No

 ** QueueTimeAdjustmentSeconds **   <a name="connect-Type-Contact-QueueTimeAdjustmentSeconds"></a>
An integer that represents the queue time adjust to be applied to the contact, in seconds (longer / larger queue time are routed preferentially). Cannot be specified if the QueuePriority is specified. Must be statically defined and a valid integer value.
Type: Integer
Required: No

 ** Recordings **   <a name="connect-Type-Contact-Recordings"></a>
If recording was enabled, this is information about the recordings.
Type: Array of [RecordingInfo](API_RecordingInfo.md) objects
Required: No

 ** RelatedContactId **   <a name="connect-Type-Contact-RelatedContactId"></a>
The contactId that is [related](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html#relatedcontactid) to this contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** RingStartTimestamp **   <a name="connect-Type-Contact-RingStartTimestamp"></a>
The timestamp when ringing started for a campaign call.
Type: Timestamp
Required: No

 ** RoutingCriteria **   <a name="connect-Type-Contact-RoutingCriteria"></a>
Latest routing criteria on the contact.
Type: [RoutingCriteria](API_RoutingCriteria.md) object
Required: No

 ** ScheduledTimestamp **   <a name="connect-Type-Contact-ScheduledTimestamp"></a>
The timestamp, in Unix epoch time format, at which to start running the inbound flow.
Type: Timestamp
Required: No

 ** SegmentAttributes **   <a name="connect-Type-Contact-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes and can be accessed in flows. Attribute keys can include only alphanumeric, -, and \_ characters. This field can be used to show channel subtype. For example, `connect:Guide` or `connect:SMS`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SystemEndpoint **   <a name="connect-Type-Contact-SystemEndpoint"></a>
The system endpoint. For `INBOUND`, this is the phone number or email address that the customer dialed. For `OUTBOUND` and `EXTERNAL_OUTBOUND`, this is the outbound caller ID number assigned to the outbound queue that is used to dial the customer. For callback, this shows up as Softphone for calls handled by agents with softphone.
Type: [EndpointInfo](API_EndpointInfo.md) object
Required: No

 ** Tags **   <a name="connect-Type-Contact-Tags"></a>
Tags associated with the contact. This contains both AWS generated and user-defined tags.
Type: String to string map
Map Entries: Maximum number of 6 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TaskTemplateInfo **   <a name="connect-Type-Contact-TaskTemplateInfo"></a>
If this contact was created using a task template, this contains information about the task template.
Type: [TaskTemplateInfoV2](API_TaskTemplateInfoV2.md) object
Required: No

 ** TotalPauseCount **   <a name="connect-Type-Contact-TotalPauseCount"></a>
Total pause count for a contact.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** TotalPauseDurationInSeconds **   <a name="connect-Type-Contact-TotalPauseDurationInSeconds"></a>
Total pause duration for a contact in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** WisdomInfo **   <a name="connect-Type-Contact-WisdomInfo"></a>
Information about Connect Customer Wisdom.
Type: [WisdomInfo](API_WisdomInfo.md) object
Required: No

## See Also
<a name="API_Contact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Contact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Contact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Contact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
