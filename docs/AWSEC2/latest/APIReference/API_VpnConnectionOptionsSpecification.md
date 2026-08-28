---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnConnectionOptionsSpecification.html
---

# VpnConnectionOptionsSpecification
<a name="API_VpnConnectionOptionsSpecification"></a>

Describes VPN connection options.

## Contents
<a name="API_VpnConnectionOptionsSpecification_Contents"></a>

 ** EnableAcceleration **
Indicate whether to enable acceleration for the VPN connection.
Default: `false`
Type: Boolean
Required: No

 ** LocalIpv4NetworkCidr **
The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.
Default: `0.0.0.0/0`
Type: String
Required: No

 ** LocalIpv6NetworkCidr **
The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.
Default: `::/0`
Type: String
Required: No

 ** OutsideIpAddressType **
The type of IP address assigned to the outside interface of the customer gateway device.
Valid values: `PrivateIpv4` \| `PublicIpv4` \| `Ipv6`
Default: `PublicIpv4`
Type: String
Required: No

 ** RemoteIpv4NetworkCidr **
The IPv4 CIDR on the AWS side of the VPN connection.
Default: `0.0.0.0/0`
Type: String
Required: No

 ** RemoteIpv6NetworkCidr **
The IPv6 CIDR on the AWS side of the VPN connection.
Default: `::/0`
Type: String
Required: No

 ** StaticRoutesOnly **
Indicate whether the VPN connection uses static routes only. If you are creating a VPN connection for a device that does not support BGP, you must specify `true`. Use [CreateVpnConnectionRoute](API_CreateVpnConnectionRoute.md) to create a static route.
Default: `false`
Type: Boolean
Required: No

 ** TransportTransitGatewayAttachmentId **
The transit gateway attachment ID to use for the VPN tunnel.
Required if `OutsideIpAddressType` is set to `PrivateIpv4`.
Type: String
Required: No

 ** TunnelBandwidth **
 The desired bandwidth specification for the VPN tunnel, used when creating or modifying VPN connection options to set the tunnel's throughput capacity. `standard` supports up to 1.25 Gbps per tunnel, while `large` supports up to 5 Gbps per tunnel. The default value is `standard`. Existing VPN connections without a bandwidth setting will automatically default to `standard`.
Type: String
Valid Values: `standard | large`
Required: No

 ** TunnelInsideIpVersion **
Indicate whether the VPN tunnels process IPv4 or IPv6 traffic.
Default: `ipv4`
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** TunnelOptions.N **
The tunnel options for the VPN connection.
Type: Array of [VpnTunnelOptionsSpecification](API_VpnTunnelOptionsSpecification.md) objects
Required: No

## See Also
<a name="API_VpnConnectionOptionsSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnConnectionOptionsSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnConnectionOptionsSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnConnectionOptionsSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
