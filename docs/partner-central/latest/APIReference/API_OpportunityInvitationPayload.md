---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunityInvitationPayload.html
---

# OpportunityInvitationPayload

Represents the data payload of an Engagement Invitation for a specific opportunity. This contains detailed information that partners use to evaluate the engagement.

## Contents
<a name="API_OpportunityInvitationPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-OpportunityInvitationPayload-Customer"></a>
Contains information about the customer related to the opportunity in the Engagement Invitation. This data helps partners understand the customer’s profile and requirements.
Type: [EngagementCustomer](API_EngagementCustomer.md) object
Required: Yes

 ** Project **   <a name="AWSPartnerCentral-Type-OpportunityInvitationPayload-Project"></a>
Describes the project details associated with the opportunity, including the customer’s needs and the scope of work expected to be performed.
Type: [ProjectDetails](API_ProjectDetails.md) object
Required: Yes

 ** ReceiverResponsibilities **   <a name="AWSPartnerCentral-Type-OpportunityInvitationPayload-ReceiverResponsibilities"></a>
Outlines the responsibilities or expectations of the receiver in the context of the invitation.
Type: Array of strings
Valid Values: `Distributor | Reseller | Hardware Partner | Managed Service Provider | Software Partner | Services Partner | Training Partner | Co-Sell Facilitator | Facilitator`
Required: Yes

 ** OpportunityType **   <a name="AWSPartnerCentral-Type-OpportunityInvitationPayload-OpportunityType"></a>
The type of the opportunity being shared. The sender of the invitation sets it. Valid values:
+  `Net New Business`: A new business opportunity with a potential customer that's not previously engaged with your solutions or services.
+  `Flat Renewal`: An opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.
+  `Expansion`: An opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`
Required: No

 ** SenderContacts **   <a name="AWSPartnerCentral-Type-OpportunityInvitationPayload-SenderContacts"></a>
Represents the contact details of the AWS representatives involved in sending the Engagement Invitation. These contacts are opportunity stakeholders.
Type: Array of [SenderContact](API_SenderContact.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

## See Also
<a name="API_OpportunityInvitationPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunityInvitationPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunityInvitationPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunityInvitationPayload)
