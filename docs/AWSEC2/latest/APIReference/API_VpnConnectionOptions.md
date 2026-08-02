---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnConnectionOptions.html
---

# VpnConnectionOptions
<a name="API_VpnConnectionOptions"></a>

Describes VPN connection options.

## Contents
<a name="API_VpnConnectionOptions_Contents"></a>

 ** enableAcceleration **
Indicates whether acceleration is enabled for the VPN connection.
Type: Boolean
Required: No

 ** localIpv4NetworkCidr **
The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.
Type: String
Required: No

 ** localIpv6NetworkCidr **
The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.
Type: String
Required: No

 ** outsideIpAddressType **
The type of IPv4 address assigned to the outside interface of the customer gateway.
Valid values: `PrivateIpv4` \| `PublicIpv4` \| `Ipv6`
Default: `PublicIpv4`
Type: String
Required: No

 ** remoteIpv4NetworkCidr **
The IPv4 CIDR on the AWS side of the VPN connection.
Type: String
Required: No

 ** remoteIpv6NetworkCidr **
The IPv6 CIDR on the AWS side of the VPN connection.
Type: String
Required: No

 ** staticRoutesOnly **
Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.
Type: Boolean
Required: No

 ** transportTransitGatewayAttachmentId **
The transit gateway attachment ID in use for the VPN tunnel.
Type: String
Required: No

 ** tunnelBandwidth **
 The configured bandwidth for the VPN tunnel. Represents the current throughput capacity setting for the tunnel connection. `standard` tunnel bandwidth supports up to 1.25 Gbps per tunnel while `large` supports up to 5 Gbps per tunnel. If no tunnel bandwidth was specified for the connection, `standard` is used as the default value.
Type: String
Valid Values: `standard | large`
Required: No

 ** tunnelInsideIpVersion **
Indicates whether the VPN tunnels process IPv4 or IPv6 traffic.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** TunnelOptionSet.N **
Indicates the VPN tunnel options.
Type: Array of [TunnelOption](API_TunnelOption.md) objects
Required: No

## See Also
<a name="API_VpnConnectionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnConnectionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnConnectionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnConnectionOptions)
