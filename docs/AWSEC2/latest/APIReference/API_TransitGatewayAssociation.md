---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayAssociation.html
---

# TransitGatewayAssociation
<a name="API_TransitGatewayAssociation"></a>

Describes an association between a resource attachment and a transit gateway route table.

## Contents
<a name="API_TransitGatewayAssociation_Contents"></a>

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceType **
The resource type. Note that the `tgw-peering` resource type has been deprecated.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** state **
The state of the association.
Type: String
Valid Values: `associating | associated | disassociating | disassociated`
Required: No

 ** transitGatewayAttachmentId **
The ID of the attachment.
Type: String
Required: No

 ** transitGatewayRouteTableId **
The ID of the transit gateway route table.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayAssociation)
