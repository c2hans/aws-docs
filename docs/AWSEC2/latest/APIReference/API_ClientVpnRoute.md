---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnRoute.html
---

# ClientVpnRoute
<a name="API_ClientVpnRoute"></a>

Information about a Client VPN endpoint route.

## Contents
<a name="API_ClientVpnRoute_Contents"></a>

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint with which the route is associated.
Type: String
Required: No

 ** description **
A brief description of the route.
Type: String
Required: No

 ** destinationCidr **
The IPv4 address range, in CIDR notation, of the route destination.
Type: String
Required: No

 ** origin **
Indicates how the route was associated with the Client VPN endpoint. `associate` indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. `add-route` indicates that the route was manually added using the **CreateClientVpnRoute** action.
Type: String
Required: No

 ** status **
The current state of the route.
Type: [ClientVpnRouteStatus](API_ClientVpnRouteStatus.md) object
Required: No

 ** targetSubnet **
The ID of the subnet through which traffic is routed.
Type: String
Required: No

 ** transitGatewayAttachmentId **
The ID of the Transit Gateway attachment, if the route targets a Transit Gateway.
Type: String
Required: No

 ** type **
The route type.
Type: String
Required: No

## See Also
<a name="API_ClientVpnRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnRoute)
