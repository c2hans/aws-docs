---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementInvitationSummary.html
---

# EngagementInvitationSummary
<a name="API_EngagementInvitationSummary"></a>

Provides a summarized view of the Engagement Invitation, including details like the identifier, status, and sender. This summary helps partners track and manage AWS originated opportunities.

## Contents
<a name="API_EngagementInvitationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-Catalog"></a>
Specifies the catalog in which the Engagement Invitation resides. This can be either the `AWS` or `Sandbox` catalog, indicating whether the opportunity is live or being tested.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-Id"></a>
Represents the unique identifier of the Engagement Invitation. This identifier is used to track the invitation and to manage responses like acceptance or rejection.
Type: String
Pattern: `(?=.{1,255}$)(arn:.*|engi-[0-9a-z]{13})`
Required: Yes

 ** Arn **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the Engagement Invitation. The ARN is a unique identifier that allows partners to reference the invitation in their system and manage its lifecycle.
Type: String
Required: No

 ** EngagementId **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-EngagementId"></a>
 The identifier of the Engagement associated with this invitation. This links the invitation to its parent Engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** EngagementTitle **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-EngagementTitle"></a>
Provides a short title or description of the Engagement Invitation. This title helps partners quickly identify and differentiate between multiple engagement opportunities.
Type: String
Pattern: `(?s).{0,40}`
Required: No

 ** ExpirationDate **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-ExpirationDate"></a>
Indicates the date and time when the Engagement Invitation will expire. After this date, the invitation can no longer be accepted, and the opportunity will be unavailable to the partner.
Type: Timestamp
Required: No

 ** InvitationDate **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-InvitationDate"></a>
Indicates the date when the Engagement Invitation was sent to the partner. This provides context for when the opportunity was shared and helps in tracking the timeline for engagement.
Type: Timestamp
Required: No

 ** ParticipantType **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-ParticipantType"></a>
Identifies the role of the caller in the engagement invitation.
Type: String
Valid Values: `SENDER | RECEIVER`
Required: No

 ** PayloadType **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-PayloadType"></a>
Describes the type of payload associated with the Engagement Invitation, such as `Opportunity` or `MarketplaceOffer`. This helps partners understand the nature of the engagement request from AWS.
Type: String
Valid Values: `OpportunityInvitation | LeadInvitation`
Required: No

 ** Receiver **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-Receiver"></a>
Specifies the partner company or individual that received the Engagement Invitation. This field is important for tracking who the invitation was sent to within the partner organization.
Type: [Receiver](API_Receiver.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** SenderAwsAccountId **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-SenderAwsAccountId"></a>
Specifies the AWS account ID of the sender who initiated the Engagement Invitation. This allows the partner to identify the AWS entity or representative responsible for sharing the opportunity.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** SenderCompanyName **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-SenderCompanyName"></a>
Indicates the name of the company or AWS division that sent the Engagement Invitation. This information is useful for partners to know which part of AWS is requesting engagement.
Type: String
Pattern: `(?s).{0,120}`
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-EngagementInvitationSummary-Status"></a>
Represents the current status of the Engagement Invitation, such as `Pending`, `Accepted`, or `Rejected`. The status helps track the progress and response to the invitation.
Type: String
Valid Values: `ACCEPTED | PENDING | REJECTED | EXPIRED`
Required: No

## See Also
<a name="API_EngagementInvitationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementInvitationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementInvitationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementInvitationSummary)
