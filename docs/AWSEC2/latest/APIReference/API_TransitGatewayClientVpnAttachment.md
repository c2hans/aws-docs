---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayClientVpnAttachment.html
---

# TransitGatewayClientVpnAttachment
<a name="API_TransitGatewayClientVpnAttachment"></a>

Describes a Transit Gateway attachment for a Client VPN endpoint.

## Contents
<a name="API_TransitGatewayClientVpnAttachment_Contents"></a>

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint.
Type: String
Required: No

 ** clientVpnOwnerId **
The ID of the Amazon Web Services account that owns the Client VPN endpoint.
Type: String
Required: No

 ** creationTime **
The date and time the Transit Gateway attachment was created.
Type: String
Required: No

 ** state **
The state of the Transit Gateway attachment.
Type: String
Valid Values: `pending-acceptance | pending | rejected | available | deleting | deleted`
Required: No

 ** transitGatewayAttachmentId **
The ID of the Transit Gateway attachment.
Type: String
Required: No

 ** transitGatewayId **
The ID of the Transit Gateway.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayClientVpnAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayClientVpnAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayClientVpnAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayClientVpnAttachment)
