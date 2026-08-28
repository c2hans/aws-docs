---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociatedContactSummary.html
---

# AssociatedContactSummary
<a name="API_AssociatedContactSummary"></a>

Contact summary of a contact in contact tree associated with unique identifier.

## Contents
<a name="API_AssociatedContactSummary_Contents"></a>

 ** Channel **   <a name="connect-Type-AssociatedContactSummary-Channel"></a>
How the contact reached your contact center.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** ContactArn **   <a name="connect-Type-AssociatedContactSummary-ContactArn"></a>
The Amazon Resource Name (ARN) of the contact
Type: String
Required: No

 ** ContactId **   <a name="connect-Type-AssociatedContactSummary-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** DisconnectTimestamp **   <a name="connect-Type-AssociatedContactSummary-DisconnectTimestamp"></a>
The date and time that the customer endpoint disconnected from the current contact, in UTC time. In transfer scenarios, the DisconnectTimestamp of the previous contact indicates the date and time when that contact ended.
Type: Timestamp
Required: No

 ** InitialContactId **   <a name="connect-Type-AssociatedContactSummary-InitialContactId"></a>
If this contact is related to other contacts, this is the ID of the initial contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitiationMethod **   <a name="connect-Type-AssociatedContactSummary-InitiationMethod"></a>
Indicates how the contact was initiated.
Type: String
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: No

 ** InitiationTimestamp **   <a name="connect-Type-AssociatedContactSummary-InitiationTimestamp"></a>
The date and time this contact was initiated, in UTC time.
Type: Timestamp
Required: No

 ** PreviousContactId **   <a name="connect-Type-AssociatedContactSummary-PreviousContactId"></a>
If this contact is not the first contact, this is the ID of the previous contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** RelatedContactId **   <a name="connect-Type-AssociatedContactSummary-RelatedContactId"></a>
The contactId that is related to this contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AssociatedContactSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociatedContactSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociatedContactSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociatedContactSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
