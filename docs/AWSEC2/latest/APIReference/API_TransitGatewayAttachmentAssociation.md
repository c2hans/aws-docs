---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayAttachmentAssociation.html
---

# TransitGatewayAttachmentAssociation
<a name="API_TransitGatewayAttachmentAssociation"></a>

Describes an association.

## Contents
<a name="API_TransitGatewayAttachmentAssociation_Contents"></a>

 ** state **
The state of the association.
Type: String
Valid Values: `associating | associated | disassociating | disassociated`
Required: No

 ** transitGatewayPolicyTableId **
The ID of the transit gateway policy table associated with the attachment.
Type: String
Required: No

 ** transitGatewayRouteTableId **
The ID of the route table for the transit gateway.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayAttachmentAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayAttachmentAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayAttachmentAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayAttachmentAssociation)
