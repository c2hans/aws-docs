---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Invitation.html
---

# Invitation
<a name="API_Invitation"></a>

Details about an invitation.

## Contents
<a name="API_Invitation_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-Invitation-AccountId"></a>
The account ID of the Security Hub CSPM administrator account that the invitation was sent from.
Type: String
Required: No

 ** InvitationId **   <a name="securityhub-Type-Invitation-InvitationId"></a>
The ID of the invitation sent to the member account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InvitedAt **   <a name="securityhub-Type-Invitation-InvitedAt"></a>
The timestamp of when the invitation was sent.
Type: Timestamp
Required: No

 ** MemberStatus **   <a name="securityhub-Type-Invitation-MemberStatus"></a>
The current status of the association between the member and administrator accounts.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Invitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Invitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Invitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Invitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
