---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnEndpoint.html
---

# ClientVpnEndpoint
<a name="API_ClientVpnEndpoint"></a>

Describes a Client VPN endpoint.

## Contents
<a name="API_ClientVpnEndpoint_Contents"></a>

 ** AssociatedTargetNetwork.N **
 *This member has been deprecated.*
Information about the associated target networks. A target network is a subnet in a VPC.
Type: Array of [AssociatedTargetNetwork](API_AssociatedTargetNetwork.md) objects
Required: No

 ** AuthenticationOptions.N **
Information about the authentication method used by the Client VPN endpoint.
Type: Array of [ClientVpnAuthentication](API_ClientVpnAuthentication.md) objects
Required: No

 ** clientCidrBlock **
The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.
Type: String
Required: No

 ** clientConnectOptions **
The options for managing connection authorization for new client connections.
Type: [ClientConnectResponseOptions](API_ClientConnectResponseOptions.md) object
Required: No

 ** clientLoginBannerOptions **
Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Type: [ClientLoginBannerResponseOptions](API_ClientLoginBannerResponseOptions.md) object
Required: No

 ** clientRouteEnforcementOptions **
Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.
Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.
Type: [ClientRouteEnforcementResponseOptions](API_ClientRouteEnforcementResponseOptions.md) object
Required: No

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint.
Type: String
Required: No

 ** connectionLogOptions **
Information about the client connection logging options for the Client VPN endpoint.
Type: [ConnectionLogResponseOptions](API_ConnectionLogResponseOptions.md) object
Required: No

 ** creationTime **
The date and time the Client VPN endpoint was created.
Type: String
Required: No

 ** deletionTime **
The date and time the Client VPN endpoint was deleted, if applicable.
Type: String
Required: No

 ** description **
A brief description of the endpoint.
Type: String
Required: No

 ** devicePostureOptions **
The device trust providers configured for the Client VPN endpoint, if applicable.
Type: [DevicePostureResponseOptions](API_DevicePostureResponseOptions.md) object
Required: No

 ** disconnectOnSessionTimeout **
Indicates whether the client VPN session is disconnected after the maximum `sessionTimeoutHours` is reached. If `true`, users are prompted to reconnect client VPN. If `false`, client VPN attempts to reconnect automatically. The default value is `true`.
Type: Boolean
Required: No

 ** dnsName **
The DNS name to be used by clients when connecting to the Client VPN endpoint.
Type: String
Required: No

 ** DnsServer.N **
Information about the DNS servers to be used for DNS resolution.
Type: Array of strings
Required: No

 ** endpointIpAddressType **
The IP address type of the Client VPN endpoint. Possible values are `ipv4` for IPv4 addressing only, `ipv6` for IPv6 addressing only, or `dual-stack `for both IPv4 and IPv6 addressing.
Type: String
Valid Values: `ipv4 | ipv6 | dual-stack`
Required: No

 ** SecurityGroupIdSet.N **
The IDs of the security groups for the target network.
Type: Array of strings
Required: No

 ** selfServicePortalUrl **
The URL of the self-service portal.
Type: String
Required: No

 ** serverCertificateArn **
The ARN of the server certificate.
Type: String
Required: No

 ** sessionTimeoutHours **
The maximum VPN session duration time in hours.
Valid values: `8 | 10 | 12 | 24`
Default value: `24`
Type: Integer
Required: No

 ** splitTunnel **
Indicates whether split-tunnel is enabled in the AWS Client VPN endpoint.
For information about split-tunnel VPN endpoints, see [Split-Tunnel AWS Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the * AWS Client VPN Administrator Guide*.
Type: Boolean
Required: No

 ** status **
The current state of the Client VPN endpoint.
Type: [ClientVpnEndpointStatus](API_ClientVpnEndpointStatus.md) object
Required: No

 ** TagSet.N **
Any tags assigned to the Client VPN endpoint.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficIpAddressType **
The IP address type of the Client VPN endpoint. Possible values are either `ipv4` for IPv4 addressing only, `ipv6` for IPv6 addressing only, or `dual-stack` for both IPv4 and IPv6 addressing.
Type: String
Valid Values: `ipv4 | ipv6 | dual-stack`
Required: No

 ** transitGatewayConfiguration **
The Transit Gateway configuration for the Client VPN endpoint.
Type: [TransitGatewayConfigurationDescribeEndpointStructure](API_TransitGatewayConfigurationDescribeEndpointStructure.md) object
Required: No

 ** transportProtocol **
The transport protocol used by the Client VPN endpoint.
Type: String
Valid Values: `tcp | udp`
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

 ** vpnPort **
The port number for the Client VPN endpoint.
Type: Integer
Required: No

 ** vpnProtocol **
The protocol used by the VPN session.
Type: String
Valid Values: `openvpn`
Required: No

## See Also
<a name="API_ClientVpnEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnEndpoint)
