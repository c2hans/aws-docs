---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ConnectionInvitationSummary.html
---

# ConnectionInvitationSummary
<a name="API_account_ConnectionInvitationSummary"></a>

A summary view of a connection invitation containing key information without full details.

## Contents
<a name="API_account_ConnectionInvitationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-zA-Z0-9-]+:partnercentral:[a-z0-9\-]*::catalog/[a-zA-Z]+/connection-invitation/pacinv-[A-Za-z0-9]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-Catalog"></a>
The catalog identifier where the connection invitation exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** ConnectionType **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-ConnectionType"></a>
The type of connection being requested in the invitation.
Type: String
Valid Values: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`
Required: Yes

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-CreatedAt"></a>
The timestamp when the connection invitation was created.
Type: Timestamp
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-Id"></a>
The unique identifier of the connection invitation.
Type: String
Pattern: `pacinv-[A-Za-z0-9]{13}`
Required: Yes

 ** OtherParticipantIdentifier **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-OtherParticipantIdentifier"></a>
The identifier of the other participant in the connection invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** ParticipantType **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-ParticipantType"></a>
The type of participant (inviter or invitee) in the connection invitation.
Type: String
Valid Values: `SENDER | RECEIVER`
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-Status"></a>
The current status of the connection invitation.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | CANCELED | EXPIRED`
Required: Yes

 ** UpdatedAt **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-UpdatedAt"></a>
The timestamp when the connection invitation was last updated.
Type: Timestamp
Required: Yes

 ** ConnectionId **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-ConnectionId"></a>
The identifier of the connection associated with this invitation.
Type: String
Pattern: `pac-[A-Za-z0-9]{13}`
Required: No

 ** ExpiresAt **   <a name="AWSPartnerCentral-Type-account_ConnectionInvitationSummary-ExpiresAt"></a>
The timestamp when the connection invitation will expire.
Type: Timestamp
Required: No

## See Also
<a name="API_account_ConnectionInvitationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ConnectionInvitationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ConnectionInvitationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ConnectionInvitationSummary)
