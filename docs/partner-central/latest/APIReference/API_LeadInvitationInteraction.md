---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInvitationInteraction.html
---

# LeadInvitationInteraction
<a name="API_LeadInvitationInteraction"></a>

Represents interaction details included in a lead invitation payload. This structure provides context about how the lead was generated and the customer's engagement history to help partners assess the opportunity quality.

## Contents
<a name="API_LeadInvitationInteraction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContactBusinessTitle **   <a name="AWSPartnerCentral-Type-LeadInvitationInteraction-ContactBusinessTitle"></a>
The business title or job role of the customer contact involved in the lead interaction. This helps partners identify the decision-making level and engagement approach for the lead.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** SourceId **   <a name="AWSPartnerCentral-Type-LeadInvitationInteraction-SourceId"></a>
The unique identifier of the specific source that generated the lead interaction. This provides traceability to the original lead generation activity for reference and follow-up purposes.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** SourceName **   <a name="AWSPartnerCentral-Type-LeadInvitationInteraction-SourceName"></a>
The descriptive name of the source that generated the lead interaction. This human-readable identifier helps partners understand the specific lead generation channel or campaign that created the opportunity.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** SourceType **   <a name="AWSPartnerCentral-Type-LeadInvitationInteraction-SourceType"></a>
Specifies the type of source that generated the lead interaction, such as "Event", "Website", or "Campaign". This helps partners understand the lead generation channel and assess lead quality based on the source type.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** Usecase **   <a name="AWSPartnerCentral-Type-LeadInvitationInteraction-Usecase"></a>
Describes the specific use case or business scenario associated with the lead interaction. This information helps partners understand the customer's interests and potential solution requirements.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_LeadInvitationInteraction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInvitationInteraction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInvitationInteraction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInvitationInteraction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
