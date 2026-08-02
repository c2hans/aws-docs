---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-privatevirtualinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::PrivateVirtualInterface
<a name="aws-resource-directconnect-privatevirtualinterface"></a>

Creates a private virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A private virtual interface can be connected to either a Direct Connect gateway or a Virtual Private Gateway (VGW). Connecting the private virtual interface to a Direct Connect gateway enables the possibility for connecting to multiple VPCs, including VPCs in different AWS Regions. Connecting the private virtual interface to a VGW only provides access to a single VPC within the same Region.

Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html). To check whether your virtual interface supports jumbo frames, call [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html).

For more information, see [Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) in the * Direct Connect User Guide *.

Hosted virtual interfaces are supported by the CloudFormation resource for private virtual interfaces. The CloudFormation stack account will own the virtual interface, allowing usage of a connection or LAG in another AWS account. The connection or LAG owner account must have a role allowing the stack account to allocate private virtual interfaces.

For more information about hosted virtual interfaces, see [Hosted Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-privatevirtualinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-privatevirtualinterface-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::PrivateVirtualInterface",
  "Properties" : {
      "[AllocatePrivateVirtualInterfaceRoleArn](#cfn-directconnect-privatevirtualinterface-allocateprivatevirtualinterfacerolearn)" : {{String}},
      "[BgpPeers](#cfn-directconnect-privatevirtualinterface-bgppeers)" : {{[ BgpPeer, ... ]}},
      "[ConnectionId](#cfn-directconnect-privatevirtualinterface-connectionid)" : {{String}},
      "[DirectConnectGatewayId](#cfn-directconnect-privatevirtualinterface-directconnectgatewayid)" : {{String}},
      "[EnableSiteLink](#cfn-directconnect-privatevirtualinterface-enablesitelink)" : {{Boolean}},
      "[Mtu](#cfn-directconnect-privatevirtualinterface-mtu)" : {{Integer}},
      "[Tags](#cfn-directconnect-privatevirtualinterface-tags)" : {{[ Tag, ... ]}},
      "[VirtualGatewayId](#cfn-directconnect-privatevirtualinterface-virtualgatewayid)" : {{String}},
      "[VirtualInterfaceName](#cfn-directconnect-privatevirtualinterface-virtualinterfacename)" : {{String}},
      "[Vlan](#cfn-directconnect-privatevirtualinterface-vlan)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-privatevirtualinterface-syntax.yaml"></a>

```
Type: AWS::DirectConnect::PrivateVirtualInterface
Properties:
  [AllocatePrivateVirtualInterfaceRoleArn](#cfn-directconnect-privatevirtualinterface-allocateprivatevirtualinterfacerolearn): {{String}}
  [BgpPeers](#cfn-directconnect-privatevirtualinterface-bgppeers): {{
    - BgpPeer}}
  [ConnectionId](#cfn-directconnect-privatevirtualinterface-connectionid): {{String}}
  [DirectConnectGatewayId](#cfn-directconnect-privatevirtualinterface-directconnectgatewayid): {{String}}
  [EnableSiteLink](#cfn-directconnect-privatevirtualinterface-enablesitelink): {{Boolean}}
  [Mtu](#cfn-directconnect-privatevirtualinterface-mtu): {{Integer}}
  [Tags](#cfn-directconnect-privatevirtualinterface-tags): {{
    - Tag}}
  [VirtualGatewayId](#cfn-directconnect-privatevirtualinterface-virtualgatewayid): {{String}}
  [VirtualInterfaceName](#cfn-directconnect-privatevirtualinterface-virtualinterfacename): {{String}}
  [Vlan](#cfn-directconnect-privatevirtualinterface-vlan): {{Integer}}
```

## Properties
<a name="aws-resource-directconnect-privatevirtualinterface-properties"></a>

`AllocatePrivateVirtualInterfaceRoleArn`  <a name="cfn-directconnect-privatevirtualinterface-allocateprivatevirtualinterfacerolearn"></a>
The Amazon Resource Name (ARN) of the role to allocate the private virtual interface. The role needs to be in the account which owns the connection or LAG, and must have `directconnect:AllocatePrivateVirtualInterface` permissions. If there are tags on the virtual interface, `directconnect:TagResource` permissions are also required.
This should only be used when creating hosted virtual interfaces.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BgpPeers`  <a name="cfn-directconnect-privatevirtualinterface-bgppeers"></a>
The BGP peers configured on this virtual interface.
Modifying the BGP peers on a virtual interface will cause interruptions.
*Required*: Yes
*Type*: Array of [BgpPeer](aws-properties-directconnect-privatevirtualinterface-bgppeer.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ConnectionId`  <a name="cfn-directconnect-privatevirtualinterface-connectionid"></a>
The ID or ARN of the connection or LAG.
Connectivity over the virtual interface will be interrupted while associating to a new connection or LAG.
*Required*: Yes
*Type*: String
*Pattern*: `^((arn:aws[a-z-]*:directconnect:[a-z0-9-]+:[0-9]{12}:(dxcon/dxcon|dxlag/dxlag))|dx(con|lag))-[a-z0-9A-Z]{8,21}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DirectConnectGatewayId`  <a name="cfn-directconnect-privatevirtualinterface-directconnectgatewayid"></a>
The ID or ARN of the Direct Connect gateway.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z-]*:directconnect::[0-9]{12}:dx-gateway/)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableSiteLink`  <a name="cfn-directconnect-privatevirtualinterface-enablesitelink"></a>
Indicates whether to enable or disable SiteLink.
Connectivity over the virtual interface will be interrupted while enabling or disabling SiteLink.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Mtu`  <a name="cfn-directconnect-privatevirtualinterface-mtu"></a>
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.
Connectivity over the virtual interface will be interrupted while the MTU update is completed.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-directconnect-privatevirtualinterface-tags"></a>
The tags associated with the private virtual interface.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-privatevirtualinterface-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualGatewayId`  <a name="cfn-directconnect-privatevirtualinterface-virtualgatewayid"></a>
The ID or ARN of the virtual private gateway.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z-]*:ec2:[a-z0-9-]+:[0-9]{12}:vpn-gateway/)?vgw-[a-zA-Z0-9]{8,32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualInterfaceName`  <a name="cfn-directconnect-privatevirtualinterface-virtualinterfacename"></a>
The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \-_,\/]{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vlan`  <a name="cfn-directconnect-privatevirtualinterface-vlan"></a>
The ID of the VLAN.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `4095`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-directconnect-privatevirtualinterface-return-values"></a>

### Ref
<a name="aws-resource-directconnect-privatevirtualinterface-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the private virtual interface.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-privatevirtualinterface-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-privatevirtualinterface-return-values-fn--getatt-fn--getatt"></a>

`VirtualInterfaceArn`  <a name="VirtualInterfaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the private virtual interface.

`VirtualInterfaceId`  <a name="VirtualInterfaceId-fn::getatt"></a>
The ID of the private virtual interface.

## Examples
<a name="aws-resource-directconnect-privatevirtualinterface--examples"></a>

### Create a private virtual interface using resources in the same account
<a name="aws-resource-directconnect-privatevirtualinterface--examples--Create_a_private_virtual_interface_using_resources_in_the_same_account"></a>

This example shows a basic private virtual interface setup using a pre-existing connection and virtual private gateway in the same account.

#### JSON
<a name="aws-resource-directconnect-privatevirtualinterface--examples--Create_a_private_virtual_interface_using_resources_in_the_same_account--json"></a>

```
{
  "Resources": {
    "myPrivateVirtualInterface": {
      "Type": "AWS::DirectConnect::PrivateVirtualInterface",
      "Properties": {
        "ConnectionId": "dxcon-fgsdqeuv",
        "VirtualGatewayId": "vgw-aba37db6",
        "VirtualInterfaceName": "cfn-privatevirtualinterface-example",
        "Vlan": 101,
        "BgpPeers": [
          {
            "AddressFamily": "ipv4",
            "AmazonAddress": "192.168.1.1/30",
            "CustomerAddress": "192.168.1.2/30",
            "Asn": "65000",
            "AuthKey": "example-auth-key"
          },
          {
            "AddressFamily": "ipv6",
            "Asn": "65000"
          }
        ],
        "Tags": [
          {
            "Key": "example-key",
            "Value": "example-value"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-directconnect-privatevirtualinterface--examples--Create_a_private_virtual_interface_using_resources_in_the_same_account--yaml"></a>

```
Resources:
  myPrivateVirtualInterface:
    Type: AWS::DirectConnect::PrivateVirtualInterface
    Properties:
      ConnectionId: dxcon-fgsdqeuv
      VirtualGatewayId: vgw-aba37db6
      VirtualInterfaceName: cfn-privatevirtualinterface-example
      Vlan: 101
      BgpPeers:
      - AddressFamily: ipv4
        AmazonAddress: 192.168.1.1/30
        CustomerAddress: 192.168.1.2/30
        Asn: '65000'
        AuthKey: example-auth-key
      - AddressFamily: ipv6
        Asn: '65000'
      Tags:
      - Key: example-key
        Value: example-value
```
