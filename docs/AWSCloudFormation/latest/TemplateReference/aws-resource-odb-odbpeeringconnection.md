---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-odb-odbpeeringconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbPeeringConnection
<a name="aws-resource-odb-odbpeeringconnection"></a>

Creates a peering connection between an ODB network and a VPC.

A peering connection enables private connectivity between the networks for application-tier communication.

## Syntax
<a name="aws-resource-odb-odbpeeringconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-odb-odbpeeringconnection-syntax.json"></a>

```
{
  "Type" : "AWS::ODB::OdbPeeringConnection",
  "Properties" : {
      "[AdditionalPeerNetworkCidrs](#cfn-odb-odbpeeringconnection-additionalpeernetworkcidrs)" : {{[ String, ... ]}},
      "[DisplayName](#cfn-odb-odbpeeringconnection-displayname)" : {{String}},
      "[OdbNetworkId](#cfn-odb-odbpeeringconnection-odbnetworkid)" : {{String}},
      "[PeerNetworkId](#cfn-odb-odbpeeringconnection-peernetworkid)" : {{String}},
      "[PeerNetworkRouteTableIds](#cfn-odb-odbpeeringconnection-peernetworkroutetableids)" : {{[ String, ... ]}},
      "[Tags](#cfn-odb-odbpeeringconnection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-odb-odbpeeringconnection-syntax.yaml"></a>

```
Type: AWS::ODB::OdbPeeringConnection
Properties:
  [AdditionalPeerNetworkCidrs](#cfn-odb-odbpeeringconnection-additionalpeernetworkcidrs): {{
    - String}}
  [DisplayName](#cfn-odb-odbpeeringconnection-displayname): {{String}}
  [OdbNetworkId](#cfn-odb-odbpeeringconnection-odbnetworkid): {{String}}
  [PeerNetworkId](#cfn-odb-odbpeeringconnection-peernetworkid): {{String}}
  [PeerNetworkRouteTableIds](#cfn-odb-odbpeeringconnection-peernetworkroutetableids): {{
    - String}}
  [Tags](#cfn-odb-odbpeeringconnection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-odb-odbpeeringconnection-properties"></a>

`AdditionalPeerNetworkCidrs`  <a name="cfn-odb-odbpeeringconnection-additionalpeernetworkcidrs"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-odb-odbpeeringconnection-displayname"></a>
The display name of the ODB peering connection.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OdbNetworkId`  <a name="cfn-odb-odbpeeringconnection-odbnetworkid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})$`
*Minimum*: `6`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerNetworkId`  <a name="cfn-odb-odbpeeringconnection-peernetworkid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})$`
*Minimum*: `6`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerNetworkRouteTableIds`  <a name="cfn-odb-odbpeeringconnection-peernetworkroutetableids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-odb-odbpeeringconnection-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-odbpeeringconnection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-odb-odbpeeringconnection-return-values"></a>

### Ref
<a name="aws-resource-odb-odbpeeringconnection-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-odb-odbpeeringconnection-return-values-fn--getatt"></a>

####
<a name="aws-resource-odb-odbpeeringconnection-return-values-fn--getatt-fn--getatt"></a>

`OdbNetworkArn`  <a name="OdbNetworkArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ODB network that initiated the peering connection.

`OdbPeeringConnectionArn`  <a name="OdbPeeringConnectionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ODB peering connection.

`OdbPeeringConnectionId`  <a name="OdbPeeringConnectionId-fn::getatt"></a>
The unique identifier of the ODB peering connection. A sample ID is `odbpcx-abcdefgh12345678`.

`PeerNetworkArn`  <a name="PeerNetworkArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the peer network.

`PeerNetworkCidrs`  <a name="PeerNetworkCidrs-fn::getatt"></a>
The CIDR blocks associated with the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.
