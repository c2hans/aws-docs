---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayNetworkFunctionAttachment.html
---

# TransitGatewayNetworkFunctionAttachment
<a name="API_TransitGatewayNetworkFunctionAttachment"></a>

Contains information about a transit gateway network function attachment, including the attachment ID, the transit gateway, the endpoint service, the Availability Zones, and the state of the attachment.

## Contents
<a name="API_TransitGatewayNetworkFunctionAttachment_Contents"></a>

 ** AvailabilityZoneIdSet.N **
The IDs of the Availability Zones for the attachment.
Type: Array of strings
Required: No

 ** AvailabilityZoneSet.N **
The names of the Availability Zones for the attachment.
Type: Array of strings
Required: No

 ** creationTime **
The date and time the attachment was created.
Type: Timestamp
Required: No

 ** resourceId **
The name of the Gateway Load Balancer endpoint service.
Type: String
Required: No

 ** resourceOwnerId **
The ID of the AWS account that owns the attachment.
Type: String
Required: No

 ** state **
The state of the attachment.
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
<a name="API_TransitGatewayNetworkFunctionAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayNetworkFunctionAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayNetworkFunctionAttachment)
