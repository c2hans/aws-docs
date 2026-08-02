---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayVpcAttachment.html
---

# TransitGatewayVpcAttachment
<a name="API_TransitGatewayVpcAttachment"></a>

Describes a VPC attachment.

## Contents
<a name="API_TransitGatewayVpcAttachment_Contents"></a>

 ** creationTime **
The creation time.
Type: Timestamp
Required: No

 ** options **
The VPC attachment options.
Type: [TransitGatewayVpcAttachmentOptions](API_TransitGatewayVpcAttachmentOptions.md) object
Required: No

 ** state **
The state of the VPC attachment. Note that the `initiating` state has been deprecated.
Type: String
Valid Values: `initiating | initiatingRequest | pendingAcceptance | rollingBack | pending | available | modifying | deleting | deleted | failed | rejected | rejecting | failing`
Required: No

 ** SubnetIds.N **
The IDs of the subnets.
Type: Array of strings
Required: No

 ** TagSet.N **
The tags for the VPC attachment.
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

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

 ** vpcOwnerId **
The ID of the AWS account that owns the VPC.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayVpcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayVpcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayVpcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayVpcAttachment)
