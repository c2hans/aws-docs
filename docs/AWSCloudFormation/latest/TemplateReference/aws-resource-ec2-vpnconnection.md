---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpnconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection
<a name="aws-resource-ec2-vpnconnection"></a>

Specifies a VPN connection between a virtual private gateway and a VPN customer gateway or a transit gateway and a VPN customer gateway.

To specify a VPN connection between a transit gateway and customer gateway, use the `TransitGatewayId` and `CustomerGatewayId` properties.

To specify a VPN connection between a virtual private gateway and customer gateway, use the `VpnGatewayId` and `CustomerGatewayId` properties.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *AWS Site-to-Site VPN User Guide*.

## Syntax
<a name="aws-resource-ec2-vpnconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpnconnection-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPNConnection",
  "Properties" : {
      "[CustomerGatewayId](#cfn-ec2-vpnconnection-customergatewayid)" : {{String}},
      "[EnableAcceleration](#cfn-ec2-vpnconnection-enableacceleration)" : {{Boolean}},
      "[LocalIpv4NetworkCidr](#cfn-ec2-vpnconnection-localipv4networkcidr)" : {{String}},
      "[LocalIpv6NetworkCidr](#cfn-ec2-vpnconnection-localipv6networkcidr)" : {{String}},
      "[OutsideIpAddressType](#cfn-ec2-vpnconnection-outsideipaddresstype)" : {{String}},
      "[PreSharedKeyStorage](#cfn-ec2-vpnconnection-presharedkeystorage)" : {{String}},
      "[RemoteIpv4NetworkCidr](#cfn-ec2-vpnconnection-remoteipv4networkcidr)" : {{String}},
      "[RemoteIpv6NetworkCidr](#cfn-ec2-vpnconnection-remoteipv6networkcidr)" : {{String}},
      "[StaticRoutesOnly](#cfn-ec2-vpnconnection-staticroutesonly)" : {{Boolean}},
      "[Tags](#cfn-ec2-vpnconnection-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-vpnconnection-transitgatewayid)" : {{String}},
      "[TransportTransitGatewayAttachmentId](#cfn-ec2-vpnconnection-transporttransitgatewayattachmentid)" : {{String}},
      "[TunnelBandwidth](#cfn-ec2-vpnconnection-tunnelbandwidth)" : {{String}},
      "[TunnelInsideIpVersion](#cfn-ec2-vpnconnection-tunnelinsideipversion)" : {{String}},
      "[Type](#cfn-ec2-vpnconnection-type)" : {{String}},
      "[VpnConcentratorId](#cfn-ec2-vpnconnection-vpnconcentratorid)" : {{String}},
      "[VpnGatewayId](#cfn-ec2-vpnconnection-vpngatewayid)" : {{String}},
      "[VpnTunnelOptionsSpecifications](#cfn-ec2-vpnconnection-vpntunneloptionsspecifications)" : {{[ VpnTunnelOptionsSpecification, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpnconnection-syntax.yaml"></a>

```
Type: AWS::EC2::VPNConnection
Properties:
  [CustomerGatewayId](#cfn-ec2-vpnconnection-customergatewayid): {{String}}
  [EnableAcceleration](#cfn-ec2-vpnconnection-enableacceleration): {{Boolean}}
  [LocalIpv4NetworkCidr](#cfn-ec2-vpnconnection-localipv4networkcidr): {{String}}
  [LocalIpv6NetworkCidr](#cfn-ec2-vpnconnection-localipv6networkcidr): {{String}}
  [OutsideIpAddressType](#cfn-ec2-vpnconnection-outsideipaddresstype): {{String}}
  [PreSharedKeyStorage](#cfn-ec2-vpnconnection-presharedkeystorage): {{String}}
  [RemoteIpv4NetworkCidr](#cfn-ec2-vpnconnection-remoteipv4networkcidr): {{String}}
  [RemoteIpv6NetworkCidr](#cfn-ec2-vpnconnection-remoteipv6networkcidr): {{String}}
  [StaticRoutesOnly](#cfn-ec2-vpnconnection-staticroutesonly): {{Boolean}}
  [Tags](#cfn-ec2-vpnconnection-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-vpnconnection-transitgatewayid): {{String}}
  [TransportTransitGatewayAttachmentId](#cfn-ec2-vpnconnection-transporttransitgatewayattachmentid): {{String}}
  [TunnelBandwidth](#cfn-ec2-vpnconnection-tunnelbandwidth): {{String}}
  [TunnelInsideIpVersion](#cfn-ec2-vpnconnection-tunnelinsideipversion): {{String}}
  [Type](#cfn-ec2-vpnconnection-type): {{String}}
  [VpnConcentratorId](#cfn-ec2-vpnconnection-vpnconcentratorid): {{String}}
  [VpnGatewayId](#cfn-ec2-vpnconnection-vpngatewayid): {{String}}
  [VpnTunnelOptionsSpecifications](#cfn-ec2-vpnconnection-vpntunneloptionsspecifications): {{
    - VpnTunnelOptionsSpecification}}
```

## Properties
<a name="aws-resource-ec2-vpnconnection-properties"></a>

`CustomerGatewayId`  <a name="cfn-ec2-vpnconnection-customergatewayid"></a>
The ID of the customer gateway at your end of the VPN connection.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAcceleration`  <a name="cfn-ec2-vpnconnection-enableacceleration"></a>
Indicate whether to enable acceleration for the VPN connection.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalIpv4NetworkCidr`  <a name="cfn-ec2-vpnconnection-localipv4networkcidr"></a>
The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.
Default: `0.0.0.0/0`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalIpv6NetworkCidr`  <a name="cfn-ec2-vpnconnection-localipv6networkcidr"></a>
The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.
Default: `::/0`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutsideIpAddressType`  <a name="cfn-ec2-vpnconnection-outsideipaddresstype"></a>
The type of IP address assigned to the outside interface of the customer gateway device.
Valid values: `PrivateIpv4` \| `PublicIpv4` \| `Ipv6`
Default: `PublicIpv4`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreSharedKeyStorage`  <a name="cfn-ec2-vpnconnection-presharedkeystorage"></a>
Specifies the storage mode for the pre-shared key (PSK). Valid values are `Standard` (stored in the AWS Site-to-Site VPN service) or `SecretsManager` (stored in AWS Secrets Manager).
*Required*: No
*Type*: String
*Allowed values*: `Standard | SecretsManager`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RemoteIpv4NetworkCidr`  <a name="cfn-ec2-vpnconnection-remoteipv4networkcidr"></a>
The IPv4 CIDR on the AWS side of the VPN connection.
Default: `0.0.0.0/0`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RemoteIpv6NetworkCidr`  <a name="cfn-ec2-vpnconnection-remoteipv6networkcidr"></a>
The IPv6 CIDR on the AWS side of the VPN connection.
Default: `::/0`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StaticRoutesOnly`  <a name="cfn-ec2-vpnconnection-staticroutesonly"></a>
Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.
If you are creating a VPN connection for a device that does not support Border Gateway Protocol (BGP), you must specify `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-vpnconnection-tags"></a>
Any tags assigned to the VPN connection.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-vpnconnection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-vpnconnection-transitgatewayid"></a>
The ID of the transit gateway associated with the VPN connection.
You must specify either `TransitGatewayId` or `VpnGatewayId`, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransportTransitGatewayAttachmentId`  <a name="cfn-ec2-vpnconnection-transporttransitgatewayattachmentid"></a>
The transit gateway attachment ID to use for the VPN tunnel.
Required if `OutsideIpAddressType` is set to `PrivateIpv4`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TunnelBandwidth`  <a name="cfn-ec2-vpnconnection-tunnelbandwidth"></a>
 The desired bandwidth specification for the VPN tunnel, used when creating or modifying VPN connection options to set the tunnel's throughput capacity. `standard` supports up to 1.25 Gbps per tunnel, while `large` supports up to 5 Gbps per tunnel. The default value is `standard`. Existing VPN connections without a bandwidth setting will automatically default to `standard`.
*Required*: No
*Type*: String
*Allowed values*: `standard | large`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TunnelInsideIpVersion`  <a name="cfn-ec2-vpnconnection-tunnelinsideipversion"></a>
Indicate whether the VPN tunnels process IPv4 or IPv6 traffic.
Default: `ipv4`
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-ec2-vpnconnection-type"></a>
The type of VPN connection.
*Required*: Yes
*Type*: String
*Allowed values*: `ipsec.1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpnConcentratorId`  <a name="cfn-ec2-vpnconnection-vpnconcentratorid"></a>
The ID of the VPN concentrator to associate with the VPN connection.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpnGatewayId`  <a name="cfn-ec2-vpnconnection-vpngatewayid"></a>
The ID of the virtual private gateway at the AWS side of the VPN connection.
You must specify either `TransitGatewayId` or `VpnGatewayId`, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpnTunnelOptionsSpecifications`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecifications"></a>
The tunnel options for the VPN connection.
*Required*: No
*Type*: Array of [VpnTunnelOptionsSpecification](aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-vpnconnection-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpnconnection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the VPN connection.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-vpnconnection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-vpnconnection-return-values-fn--getatt-fn--getatt"></a>

`VpnConnectionId`  <a name="VpnConnectionId-fn::getatt"></a>
The ID of the VPN connection.

## Examples
<a name="aws-resource-ec2-vpnconnection--examples"></a>

### VPN connection
<a name="aws-resource-ec2-vpnconnection--examples--VPN_connection"></a>

The following example specifies a VPN connection between myVPNGateway and MyCustomerGateway.

#### JSON
<a name="aws-resource-ec2-vpnconnection--examples--VPN_connection--json"></a>

```
"myVPNConnection" : {
   "Type" : "AWS::EC2::VPNConnection",
   "Properties" : {
      "Type" : "ipsec.1",
      "StaticRoutesOnly" : "true",
      "CustomerGatewayId" : {"Ref" : "myCustomerGateway"},
      "VpnGatewayId" : {"Ref" : "myVPNGateway"}
   }
}
```

#### YAML
<a name="aws-resource-ec2-vpnconnection--examples--VPN_connection--yaml"></a>

```
   myVPNConnection:
      Type: AWS::EC2::VPNConnection
      Properties:
        Type: ipsec.1
        StaticRoutesOnly: true
        CustomerGatewayId:
          !Ref myCustomerGateway
        VpnGatewayId:
          !Ref myVPNGateway
```

## See also
<a name="aws-resource-ec2-vpnconnection--seealso"></a>
+ [VPNConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnConnection.html) in the *Amazon EC2 API Reference*
