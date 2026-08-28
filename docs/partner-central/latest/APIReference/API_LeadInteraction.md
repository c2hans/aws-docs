---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInteraction.html
---

# LeadInteraction
<a name="API_LeadInteraction"></a>

Represents a specific interaction or touchpoint with a lead customer. This structure captures details about communications, meetings, or other engagement activities that help track the lead's progression and engagement history.

## Contents
<a name="API_LeadInteraction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Contact **   <a name="AWSPartnerCentral-Type-LeadInteraction-Contact"></a>
Contains contact information for the customer representative involved in the lead interaction, including their name, title, and contact details.
Type: [LeadContact](API_LeadContact.md) object
Required: Yes

 ** BusinessProblem **   <a name="AWSPartnerCentral-Type-LeadInteraction-BusinessProblem"></a>
Describes the business problem or challenge that the customer discussed during the interaction. This information helps qualify the lead and identify appropriate solutions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** CustomerAction **   <a name="AWSPartnerCentral-Type-LeadInteraction-CustomerAction"></a>
Describes the action taken by the customer during or as a result of the interaction, such as requesting information, scheduling a meeting, or expressing interest in a solution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** InteractionDate **   <a name="AWSPartnerCentral-Type-LeadInteraction-InteractionDate"></a>
The date and time when the lead interaction occurred, in ISO 8601 format (UTC). This timestamp helps track the chronology of lead engagement activities.
Type: Timestamp
Required: No

 ** SourceId **   <a name="AWSPartnerCentral-Type-LeadInteraction-SourceId"></a>
The unique identifier of the specific source that generated the lead interaction. This ID provides traceability back to the original lead generation activity.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** SourceName **   <a name="AWSPartnerCentral-Type-LeadInteraction-SourceName"></a>
The descriptive name of the source that generated the lead interaction, providing a human-readable identifier for the lead generation channel or activity.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** SourceType **   <a name="AWSPartnerCentral-Type-LeadInteraction-SourceType"></a>
Specifies the type of source that generated the lead interaction, such as "Event", "Website", "Referral", or "Campaign". This categorization helps track lead generation effectiveness across different channels.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** Usecase **   <a name="AWSPartnerCentral-Type-LeadInteraction-Usecase"></a>
Describes the specific use case or business scenario discussed during the lead interaction. This helps categorize the customer's interests and potential solutions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_LeadInteraction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInteraction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInteraction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInteraction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
