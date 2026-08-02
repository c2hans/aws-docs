---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Invitation.html
---

# Invitation
<a name="API_Invitation"></a>

Contains information about the invitation to become a member account.

## Contents
<a name="API_Invitation_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Invitation-accountId"></a>
The ID of the account that the invitation was sent from.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** invitationId **   <a name="guardduty-Type-Invitation-invitationId"></a>
The ID of the invitation. This value is used to validate the inviter account to the member account.
Type: String
Required: No

 ** invitedAt **   <a name="guardduty-Type-Invitation-invitedAt"></a>
The timestamp when the invitation was sent.
Type: String
Required: No

 ** relationshipStatus **   <a name="guardduty-Type-Invitation-relationshipStatus"></a>
The status of the relationship between the inviter and invitee accounts.
Type: String
Required: No

## See Also
<a name="API_Invitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Invitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Invitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Invitation)
