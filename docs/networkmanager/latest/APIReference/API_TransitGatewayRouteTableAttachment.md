---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_TransitGatewayRouteTableAttachment.html
---

# TransitGatewayRouteTableAttachment
<a name="API_TransitGatewayRouteTableAttachment"></a>

Describes a transit gateway route table attachment.

## Contents
<a name="API_TransitGatewayRouteTableAttachment_Contents"></a>

 ** Attachment **   <a name="networkmanager-Type-TransitGatewayRouteTableAttachment-Attachment"></a>
Describes a core network attachment.
Type: [Attachment](API_Attachment.md) object
Required: No

 ** PeeringId **   <a name="networkmanager-Type-TransitGatewayRouteTableAttachment-PeeringId"></a>
The ID of the peering attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^peering-([0-9a-f]{8,17})$`
Required: No

 ** TransitGatewayRouteTableArn **   <a name="networkmanager-Type-TransitGatewayRouteTableAttachment-TransitGatewayRouteTableArn"></a>
The ARN of the transit gateway attachment route table. For example, `"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_TransitGatewayRouteTableAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment)
