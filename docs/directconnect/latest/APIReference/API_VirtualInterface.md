---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterface.html
---

# VirtualInterface
<a name="API_VirtualInterface"></a>

Information about a virtual interface.

## Contents
<a name="API_VirtualInterface_Contents"></a>

 ** addressFamily **   <a name="DX-Type-VirtualInterface-addressFamily"></a>
The address family for the BGP peer.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** amazonAddress **   <a name="DX-Type-VirtualInterface-amazonAddress"></a>
The IP address assigned to the Amazon interface.
Type: String
Required: No

 ** amazonSideAsn **   <a name="DX-Type-VirtualInterface-amazonSideAsn"></a>
The autonomous system number (AS) for the Amazon side of the connection.
Type: Long
Required: No

 ** asn **   <a name="DX-Type-VirtualInterface-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
+ If you enter a 4-byte ASN for the `asn` parameter, the API returns an error.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
Type: Integer
Required: No

 ** asnLong **   <a name="DX-Type-VirtualInterface-asnLong"></a>
The long ASN for the virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.
Note the following limitations when using `asnLong`:
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+  `asnLong` accepts any valid ASN value, regardless if it's 2-byte or 4-byte.
+ When using a 4-byte `asnLong`, the API response returns `0` for the legacy `asn` attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
Type: Long
Required: No

 ** authKey **   <a name="DX-Type-VirtualInterface-authKey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
Type: String
Required: No

 ** awsDeviceV2 **   <a name="DX-Type-VirtualInterface-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-VirtualInterface-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** bgpPeers **   <a name="DX-Type-VirtualInterface-bgpPeers"></a>
The BGP peers configured on this virtual interface.
Type: Array of [BGPPeer](API_BGPPeer.md) objects
Required: No

 ** connectionId **   <a name="DX-Type-VirtualInterface-connectionId"></a>
The ID of the connection.
Type: String
Required: No

 ** customerAddress **   <a name="DX-Type-VirtualInterface-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String
Required: No

 ** customerRouterConfig **   <a name="DX-Type-VirtualInterface-customerRouterConfig"></a>
The customer router configuration.
Type: String
Required: No

 ** directConnectGatewayId **   <a name="DX-Type-VirtualInterface-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** jumboFrameCapable **   <a name="DX-Type-VirtualInterface-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean
Required: No

 ** location **   <a name="DX-Type-VirtualInterface-location"></a>
The location of the connection.
Type: String
Required: No

 ** mtu **   <a name="DX-Type-VirtualInterface-mtu"></a>
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500
Type: Integer
Required: No

 ** ownerAccount **   <a name="DX-Type-VirtualInterface-ownerAccount"></a>
The ID of the AWS account that owns the virtual interface.
Type: String
Required: No

 ** prefixPoolAllocatedCountIpv4 **   <a name="DX-Type-VirtualInterface-prefixPoolAllocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolAllocatedCountIpv6 **   <a name="DX-Type-VirtualInterface-prefixPoolAllocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** rateLimit **   <a name="DX-Type-VirtualInterface-rateLimit"></a>
The rate limit (bandwidth allocation) applied to the virtual interface. The value must be one of the supported bandwidth values and cannot exceed the bandwidth of the parent connection or LAG. Supported values: `50Mbps`, `100Mbps`, `200Mbps`, `300Mbps`, `400Mbps`, `500Mbps`, `600Mbps`, `700Mbps`, `800Mbps`, `900Mbps`, `1Gbps`, `1.2Gbps`, `1.5Gbps`, `1.8Gbps`, `2Gbps`, `2.1Gbps`, `2.4Gbps`, `2.7Gbps`, `3Gbps`, `3.2Gbps`, `3.6Gbps`, `4Gbps`, `5Gbps`, `6Gbps`, `7Gbps`, `8Gbps`, `9Gbps`, `10Gbps`, `12Gbps`, `15Gbps`, `18Gbps`, `20Gbps`, `21Gbps`, `24Gbps`, `27Gbps`, `30Gbps`, `32Gbps`, `36Gbps`, `40Gbps`, `50Gbps`, `60Gbps`, `70Gbps`, `80Gbps`, `100Gbps`, `120Gbps`, `150Gbps`, `180Gbps`, `200Gbps`, `210Gbps`, `240Gbps`, `270Gbps`, `300Gbps`, `320Gbps`, `360Gbps`, `400Gbps`, `450Gbps`, `480Gbps`, `500Gbps`, `540Gbps`, `600Gbps`, `700Gbps`, `800Gbps`, `900Gbps`, `1Tbps`, `1.1Tbps`, `1.2Tbps`, `1.3Tbps`, `1.4Tbps`, `1.5Tbps`, `1.6Tbps`.
Type: String
Required: No

 ** region **   <a name="DX-Type-VirtualInterface-region"></a>
The AWS Region where the virtual interface is located.
Type: String
Required: No

 ** routeFilterPrefixes **   <a name="DX-Type-VirtualInterface-routeFilterPrefixes"></a>
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** siteLinkEnabled **   <a name="DX-Type-VirtualInterface-siteLinkEnabled"></a>
Indicates whether SiteLink is enabled.
Type: Boolean
Required: No

 ** tags **   <a name="DX-Type-VirtualInterface-tags"></a>
The tags associated with the virtual interface.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** virtualGatewayId **   <a name="DX-Type-VirtualInterface-virtualGatewayId"></a>
The ID of the virtual private gateway. Applies only to private virtual interfaces.
Type: String
Required: No

 ** virtualInterfaceId **   <a name="DX-Type-VirtualInterface-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

 ** virtualInterfaceName **   <a name="DX-Type-VirtualInterface-virtualInterfaceName"></a>
The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
Type: String
Required: No

 ** virtualInterfaceState **   <a name="DX-Type-VirtualInterface-virtualInterfaceState"></a>
The state of the virtual interface. The following are the possible values:
+  `confirming`: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
+  `verifying`: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
+  `pending`: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
+  `available`: A virtual interface that is able to forward traffic.
+  `down`: A virtual interface that is BGP down.
+  `testing`: A virtual interface is in this state immediately after calling [StartBgpFailoverTest](API_StartBgpFailoverTest.md) and remains in this state during the duration of the test.
+  `deleting`: A virtual interface is in this state immediately after calling [DeleteVirtualInterface](API_DeleteVirtualInterface.md) until it can no longer forward traffic.
+  `deleted`: A virtual interface that cannot forward traffic.
+  `rejected`: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the `Confirming` state is deleted by the virtual interface owner, the virtual interface enters the `Rejected` state.
+  `unknown`: The state of the virtual interface is not available.
Type: String
Valid Values: `confirming | verifying | pending | available | down | testing | deleting | deleted | rejected | unknown`
Required: No

 ** virtualInterfaceType **   <a name="DX-Type-VirtualInterface-virtualInterfaceType"></a>
The type of virtual interface. The possible values are `private`, `public` and `transit`.
Type: String
Required: No

 ** vlan **   <a name="DX-Type-VirtualInterface-vlan"></a>
The ID of the VLAN.
Type: Integer
Required: No

## See Also
<a name="API_VirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/VirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/VirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/VirtualInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
