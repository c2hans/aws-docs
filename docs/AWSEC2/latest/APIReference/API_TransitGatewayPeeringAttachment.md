---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPeeringAttachment.html
---

# TransitGatewayPeeringAttachment
<a name="API_TransitGatewayPeeringAttachment"></a>

Describes the transit gateway peering attachment.

## Contents
<a name="API_TransitGatewayPeeringAttachment_Contents"></a>

 ** accepterTgwInfo **
Information about the accepter transit gateway.
Type: [PeeringTgwInfo](API_PeeringTgwInfo.md) object
Required: No

 ** accepterTransitGatewayAttachmentId **
The ID of the accepter transit gateway attachment.
Type: String
Required: No

 ** creationTime **
The time the transit gateway peering attachment was created.
Type: Timestamp
Required: No

 ** options **
Details about the transit gateway peering attachment.
Type: [TransitGatewayPeeringAttachmentOptions](API_TransitGatewayPeeringAttachmentOptions.md) object
Required: No

 ** requesterTgwInfo **
Information about the requester transit gateway.
Type: [PeeringTgwInfo](API_PeeringTgwInfo.md) object
Required: No

 ** state **
The state of the transit gateway peering attachment. Note that the `initiating` state has been deprecated.
Type: String
Valid Values: `initiating | initiatingRequest | pendingAcceptance | rollingBack | pending | available | modifying | deleting | deleted | failed | rejected | rejecting | failing`
Required: No

 ** status **
The status of the transit gateway peering attachment.
Type: [PeeringAttachmentStatus](API_PeeringAttachmentStatus.md) object
Required: No

 ** TagSet.N **
The tags for the transit gateway peering attachment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayAttachmentId **
The ID of the transit gateway peering attachment.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPeeringAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPeeringAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPeeringAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPeeringAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
