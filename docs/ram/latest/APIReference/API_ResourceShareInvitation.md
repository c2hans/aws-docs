---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareInvitation.html
---

# ResourceShareInvitation
<a name="API_ResourceShareInvitation"></a>

Describes an invitation for an AWS account to join a resource share.

## Contents
<a name="API_ResourceShareInvitation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** invitationTimestamp **   <a name="ram-Type-ResourceShareInvitation-invitationTimestamp"></a>
The date and time when the invitation was sent.
Type: Timestamp
Required: No

 ** receiverAccountId **   <a name="ram-Type-ResourceShareInvitation-receiverAccountId"></a>
The ID of the AWS account that received the invitation.
Type: String
Required: No

 ** receiverArn **   <a name="ram-Type-ResourceShareInvitation-receiverArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM user or role that received the invitation.
Type: String
Required: No

 ** resourceShareArn **   <a name="ram-Type-ResourceShareInvitation-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share
Type: String
Required: No

 ** resourceShareAssociations **   <a name="ram-Type-ResourceShareInvitation-resourceShareAssociations"></a>
 *This member has been deprecated.*
To view the resources associated with a pending resource share invitation, use [ListPendingInvitationResources](API_ListPendingInvitationResources.md).
Type: Array of [ResourceShareAssociation](API_ResourceShareAssociation.md) objects
Required: No

 ** resourceShareInvitationArn **   <a name="ram-Type-ResourceShareInvitation-resourceShareInvitationArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the invitation.
Type: String
Required: No

 ** resourceShareName **   <a name="ram-Type-ResourceShareInvitation-resourceShareName"></a>
The name of the resource share.
Type: String
Required: No

 ** senderAccountId **   <a name="ram-Type-ResourceShareInvitation-senderAccountId"></a>
The ID of the AWS account that sent the invitation.
Type: String
Required: No

 ** status **   <a name="ram-Type-ResourceShareInvitation-status"></a>
The current status of the invitation.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | EXPIRED`
Required: No

## See Also
<a name="API_ResourceShareInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ResourceShareInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ResourceShareInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ResourceShareInvitation)
