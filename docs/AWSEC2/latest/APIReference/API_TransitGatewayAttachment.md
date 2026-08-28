---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayAttachment.html
---

# TransitGatewayAttachment
<a name="API_TransitGatewayAttachment"></a>

Describes an attachment between a resource and a transit gateway.

## Contents
<a name="API_TransitGatewayAttachment_Contents"></a>

 ** association **
The association.
Type: [TransitGatewayAttachmentAssociation](API_TransitGatewayAttachmentAssociation.md) object
Required: No

 ** creationTime **
The creation time.
Type: Timestamp
Required: No

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceOwnerId **
The ID of the AWS account that owns the resource.
Type: String
Required: No

 ** resourceType **
The resource type. Note that the `tgw-peering` resource type has been deprecated.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** state **
The attachment state. Note that the `initiating` state has been deprecated.
Type: String
Valid Values: `initiating | initiatingRequest | pendingAcceptance | rollingBack | pending | available | modifying | deleting | deleted | failed | rejected | rejecting | failing`
Required: No

 ** TagSet.N **
The tags for the attachment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayAttachmentId **
The ID of the attachment.
Type: String
Required: No

 ** transitGatewayId **
The ID of the transit gateway.
Type: String
Required: No

 ** transitGatewayOwnerId **
The ID of the AWS account that owns the transit gateway.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
