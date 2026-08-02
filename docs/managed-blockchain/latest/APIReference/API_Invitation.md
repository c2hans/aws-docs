---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Invitation.html
---

# Invitation
<a name="API_Invitation"></a>

An invitation to an AWS account to create a member and join the network.

Applies only to Hyperledger Fabric.

## Contents
<a name="API_Invitation_Contents"></a>

 ** Arn **   <a name="ManagedBlockchain-Type-Invitation-Arn"></a>
The Amazon Resource Name (ARN) of the invitation. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: No

 ** CreationDate **   <a name="ManagedBlockchain-Type-Invitation-CreationDate"></a>
The date and time that the invitation was created.
Type: Timestamp
Required: No

 ** ExpirationDate **   <a name="ManagedBlockchain-Type-Invitation-ExpirationDate"></a>
The date and time that the invitation expires. This is the `CreationDate` plus the `ProposalDurationInHours` that is specified in the `ProposalThresholdPolicy`. After this date and time, the invitee can no longer create a member and join the network using this `InvitationId`.
Type: Timestamp
Required: No

 ** InvitationId **   <a name="ManagedBlockchain-Type-Invitation-InvitationId"></a>
The unique identifier for the invitation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NetworkSummary **   <a name="ManagedBlockchain-Type-Invitation-NetworkSummary"></a>
A summary of network configuration properties.
Type: [NetworkSummary](API_NetworkSummary.md) object
Required: No

 ** Status **   <a name="ManagedBlockchain-Type-Invitation-Status"></a>
The status of the invitation:
+  `PENDING` - The invitee hasn't created a member to join the network, and the invitation hasn't yet expired.
+  `ACCEPTING` - The invitee has begun creating a member, and creation hasn't yet completed.
+  `ACCEPTED` - The invitee created a member and joined the network using the `InvitationID`.
+  `REJECTED` - The invitee rejected the invitation.
+  `EXPIRED` - The invitee neither created a member nor rejected the invitation before the `ExpirationDate`.
Type: String
Valid Values: `PENDING | ACCEPTED | ACCEPTING | REJECTED | EXPIRED`
Required: No

## See Also
<a name="API_Invitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/Invitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/Invitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/Invitation)
