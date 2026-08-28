---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-publicvirtualinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::PublicVirtualInterface
<a name="aws-resource-directconnect-publicvirtualinterface"></a>

Creates a public virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A public virtual interface supports sending traffic to public services of AWS such as Amazon S3.

When creating an IPv6 public virtual interface (`addressFamily` is `ipv6`), leave the `customer` and `amazon` address fields blank to use auto-assigned IPv6 space. Custom IPv6 addresses are not supported.

For more information, see [Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) in the * Direct Connect User Guide *.

Hosted virtual interfaces are supported by the CloudFormation resource for public virtual interfaces. The CloudFormation stack account will own the virtual interface, allowing usage of a connection or LAG in another AWS account. The connection or LAG owner account must have a role allowing the stack account to allocate public virtual interfaces.

For more information about hosted virtual interfaces, see [Hosted Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted-vif.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-publicvirtualinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-publicvirtualinterface-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::PublicVirtualInterface",
  "Properties" : {
      "[AllocatePublicVirtualInterfaceRoleArn](#cfn-directconnect-publicvirtualinterface-allocatepublicvirtualinterfacerolearn)" : {{String}},
      "[BgpPeers](#cfn-directconnect-publicvirtualinterface-bgppeers)" : {{[ BgpPeer, ... ]}},
      "[ConnectionId](#cfn-directconnect-publicvirtualinterface-connectionid)" : {{String}},
      "[RateLimit](#cfn-directconnect-publicvirtualinterface-ratelimit)" : {{String}},
      "[RouteFilterPrefixes](#cfn-directconnect-publicvirtualinterface-routefilterprefixes)" : {{[ String, ... ]}},
      "[Tags](#cfn-directconnect-publicvirtualinterface-tags)" : {{[ Tag, ... ]}},
      "[VirtualInterfaceName](#cfn-directconnect-publicvirtualinterface-virtualinterfacename)" : {{String}},
      "[Vlan](#cfn-directconnect-publicvirtualinterface-vlan)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-publicvirtualinterface-syntax.yaml"></a>

```
Type: AWS::DirectConnect::PublicVirtualInterface
Properties:
  [AllocatePublicVirtualInterfaceRoleArn](#cfn-directconnect-publicvirtualinterface-allocatepublicvirtualinterfacerolearn): {{String}}
  [BgpPeers](#cfn-directconnect-publicvirtualinterface-bgppeers): {{
    - BgpPeer}}
  [ConnectionId](#cfn-directconnect-publicvirtualinterface-connectionid): {{String}}
  [RateLimit](#cfn-directconnect-publicvirtualinterface-ratelimit): {{String}}
  [RouteFilterPrefixes](#cfn-directconnect-publicvirtualinterface-routefilterprefixes): {{
    - String}}
  [Tags](#cfn-directconnect-publicvirtualinterface-tags): {{
    - Tag}}
  [VirtualInterfaceName](#cfn-directconnect-publicvirtualinterface-virtualinterfacename): {{String}}
  [Vlan](#cfn-directconnect-publicvirtualinterface-vlan): {{Integer}}
```

## Properties
<a name="aws-resource-directconnect-publicvirtualinterface-properties"></a>

`AllocatePublicVirtualInterfaceRoleArn`  <a name="cfn-directconnect-publicvirtualinterface-allocatepublicvirtualinterfacerolearn"></a>
The Amazon Resource Name (ARN) of the role to allocate the public virtual interface. The role needs to be in the account which owns the connection or LAG, and must have `directconnect:AllocatePublicVirtualInterface` permissions. If there are tags on the virtual interface, `directconnect:TagResource` permissions are also required.
This should only be used when creating hosted virtual interfaces.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BgpPeers`  <a name="cfn-directconnect-publicvirtualinterface-bgppeers"></a>
The BGP peers configured on this virtual interface.
Modifying the BGP peers on a virtual interface may cause interruptions.
*Required*: Yes
*Type*: Array of [BgpPeer](aws-properties-directconnect-publicvirtualinterface-bgppeer.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ConnectionId`  <a name="cfn-directconnect-publicvirtualinterface-connectionid"></a>
The ID or ARN of the connection or LAG.
Connectivity over the virtual interface will be interrupted while associating to a new connection or LAG.
*Required*: Yes
*Type*: String
*Pattern*: `^((arn:aws[a-z-]*:directconnect:[a-z0-9-]+:[0-9]{12}:(dxcon/dxcon|dxlag/dxlag))|dx(con|lag))-[a-z0-9A-Z]{8,21}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RateLimit`  <a name="cfn-directconnect-publicvirtualinterface-ratelimit"></a>
The rate limit (bandwidth allocation) to apply to the virtual interface. The rate limit restricts the maximum bandwidth that the virtual interface can use on the parent connection.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+\.?[0-9]*(Mbps|Gbps|Tbps)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RouteFilterPrefixes`  <a name="cfn-directconnect-publicvirtualinterface-routefilterprefixes"></a>
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-directconnect-publicvirtualinterface-tags"></a>
The tags associated with the public virtual interface.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-publicvirtualinterface-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualInterfaceName`  <a name="cfn-directconnect-publicvirtualinterface-virtualinterfacename"></a>
The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \-_,\/]{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vlan`  <a name="cfn-directconnect-publicvirtualinterface-vlan"></a>
The ID of the VLAN.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `4095`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-directconnect-publicvirtualinterface-return-values"></a>

### Ref
<a name="aws-resource-directconnect-publicvirtualinterface-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the public virtual interface.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-publicvirtualinterface-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-publicvirtualinterface-return-values-fn--getatt-fn--getatt"></a>

`VirtualInterfaceArn`  <a name="VirtualInterfaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the public virtual interface.

`VirtualInterfaceId`  <a name="VirtualInterfaceId-fn::getatt"></a>
The ID of the public virtual interface.

## Examples
<a name="aws-resource-directconnect-publicvirtualinterface--examples"></a>

### Create a public virtual interface using resources in the same account
<a name="aws-resource-directconnect-publicvirtualinterface--examples--Create_a_public_virtual_interface_using_resources_in_the_same_account"></a>

This example shows a basic public virtual interface setup using a pre-existing connection in the same account.

#### JSON
<a name="aws-resource-directconnect-publicvirtualinterface--examples--Create_a_public_virtual_interface_using_resources_in_the_same_account--json"></a>

```
{
  "Resources": {
    "myPublicVirtualInterface": {
      "Type": "AWS::DirectConnect::PublicVirtualInterface",
      "Properties": {
        "ConnectionId": "dxcon-fgsdqeuv",
        "VirtualInterfaceName": "cfn-publicvirtualinterface-example",
        "Vlan": 101,
        "RouteFilterPrefixes": [
          "50.0.0.0/30"
        ],
        "BgpPeers": [
          {
            "AddressFamily": "ipv4",
            "AmazonAddress": "50.0.0.1/30",
            "CustomerAddress": "50.0.0.2/30",
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
<a name="aws-resource-directconnect-publicvirtualinterface--examples--Create_a_public_virtual_interface_using_resources_in_the_same_account--yaml"></a>

```
Resources:
  myPublicVirtualInterface:
    Type: AWS::DirectConnect::PublicVirtualInterface
    Properties:
      ConnectionId: dxcon-fgsdqeuv
      VirtualInterfaceName: cfn-publicvirtualinterface-example
      Vlan: 101
      RouteFilterPrefixes:
      - 50.0.0.0/30
      BgpPeers:
      - AddressFamily: ipv4
        AmazonAddress: 50.0.0.1/30
        CustomerAddress: 50.0.0.2/30
        Asn: '65000'
        AuthKey: example-auth-key
      - AddressFamily: ipv6
        Asn: '65000'
      Tags:
      - Key: example-key
        Value: example-value
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
