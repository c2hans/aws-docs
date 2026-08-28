---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-localgatewayvirtualinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LocalGatewayVirtualInterface
<a name="aws-resource-ec2-localgatewayvirtualinterface"></a>

Describes a local gateway virtual interface.

## Syntax
<a name="aws-resource-ec2-localgatewayvirtualinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-localgatewayvirtualinterface-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::LocalGatewayVirtualInterface",
  "Properties" : {
      "[LocalAddress](#cfn-ec2-localgatewayvirtualinterface-localaddress)" : {{String}},
      "[LocalGatewayVirtualInterfaceGroupId](#cfn-ec2-localgatewayvirtualinterface-localgatewayvirtualinterfacegroupid)" : {{String}},
      "[OutpostLagId](#cfn-ec2-localgatewayvirtualinterface-outpostlagid)" : {{String}},
      "[PeerAddress](#cfn-ec2-localgatewayvirtualinterface-peeraddress)" : {{String}},
      "[PeerBgpAsn](#cfn-ec2-localgatewayvirtualinterface-peerbgpasn)" : {{Integer}},
      "[PeerBgpAsnExtended](#cfn-ec2-localgatewayvirtualinterface-peerbgpasnextended)" : {{Integer}},
      "[Tags](#cfn-ec2-localgatewayvirtualinterface-tags)" : {{[ Tag, ... ]}},
      "[Vlan](#cfn-ec2-localgatewayvirtualinterface-vlan)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-ec2-localgatewayvirtualinterface-syntax.yaml"></a>

```
Type: AWS::EC2::LocalGatewayVirtualInterface
Properties:
  [LocalAddress](#cfn-ec2-localgatewayvirtualinterface-localaddress): {{String}}
  [LocalGatewayVirtualInterfaceGroupId](#cfn-ec2-localgatewayvirtualinterface-localgatewayvirtualinterfacegroupid): {{String}}
  [OutpostLagId](#cfn-ec2-localgatewayvirtualinterface-outpostlagid): {{String}}
  [PeerAddress](#cfn-ec2-localgatewayvirtualinterface-peeraddress): {{String}}
  [PeerBgpAsn](#cfn-ec2-localgatewayvirtualinterface-peerbgpasn): {{Integer}}
  [PeerBgpAsnExtended](#cfn-ec2-localgatewayvirtualinterface-peerbgpasnextended): {{Integer}}
  [Tags](#cfn-ec2-localgatewayvirtualinterface-tags): {{
    - Tag}}
  [Vlan](#cfn-ec2-localgatewayvirtualinterface-vlan): {{Integer}}
```

## Properties
<a name="aws-resource-ec2-localgatewayvirtualinterface-properties"></a>

`LocalAddress`  <a name="cfn-ec2-localgatewayvirtualinterface-localaddress"></a>
The local address.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalGatewayVirtualInterfaceGroupId`  <a name="cfn-ec2-localgatewayvirtualinterface-localgatewayvirtualinterfacegroupid"></a>
The ID of the local gateway virtual interface group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutpostLagId`  <a name="cfn-ec2-localgatewayvirtualinterface-outpostlagid"></a>
The Outpost LAG ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddress`  <a name="cfn-ec2-localgatewayvirtualinterface-peeraddress"></a>
The peer address.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerBgpAsn`  <a name="cfn-ec2-localgatewayvirtualinterface-peerbgpasn"></a>
The peer BGP ASN.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerBgpAsnExtended`  <a name="cfn-ec2-localgatewayvirtualinterface-peerbgpasnextended"></a>
The extended 32-bit ASN of the BGP peer for use with larger ASN values.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-localgatewayvirtualinterface-tags"></a>
The tags assigned to the virtual interface.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-localgatewayvirtualinterface-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vlan`  <a name="cfn-ec2-localgatewayvirtualinterface-vlan"></a>
The ID of the VLAN.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-localgatewayvirtualinterface-return-values"></a>

### Ref
<a name="aws-resource-ec2-localgatewayvirtualinterface-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the local gateway virtual interface. For example:

 `{ "Ref": "lgw-vif-07145b276bEXAMPLE" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-localgatewayvirtualinterface-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-localgatewayvirtualinterface-return-values-fn--getatt-fn--getatt"></a>

`ConfigurationState`  <a name="ConfigurationState-fn::getatt"></a>
The current state of the local gateway virtual interface.

`LocalBgpAsn`  <a name="LocalBgpAsn-fn::getatt"></a>
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.

`LocalGatewayId`  <a name="LocalGatewayId-fn::getatt"></a>
The ID of the local gateway.

`LocalGatewayVirtualInterfaceId`  <a name="LocalGatewayVirtualInterfaceId-fn::getatt"></a>
The ID of the virtual interface.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the local gateway virtual interface.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
