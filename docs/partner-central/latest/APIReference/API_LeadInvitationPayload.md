---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInvitationPayload.html
---

# LeadInvitationPayload
<a name="API_LeadInvitationPayload"></a>

Represents the data payload of an engagement invitation for a lead opportunity. This contains detailed information about the customer and interaction history that partners use to evaluate whether to accept the lead engagement invitation.

## Contents
<a name="API_LeadInvitationPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-LeadInvitationPayload-Customer"></a>
Contains information about the customer associated with the lead invitation. This data helps partners understand the customer's profile, industry, and business context to assess the lead opportunity.
Type: [LeadInvitationCustomer](API_LeadInvitationCustomer.md) object
Required: Yes

 ** Interaction **   <a name="AWSPartnerCentral-Type-LeadInvitationPayload-Interaction"></a>
Describes the interaction details associated with the lead, including the source of the lead generation and customer engagement information. This context helps partners evaluate the lead quality and engagement approach.
Type: [LeadInvitationInteraction](API_LeadInvitationInteraction.md) object
Required: Yes

## See Also
<a name="API_LeadInvitationPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInvitationPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInvitationPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInvitationPayload)
