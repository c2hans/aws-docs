---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-connectpeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectPeer
<a name="aws-resource-networkmanager-connectpeer"></a>

Creates a core network Connect peer for a specified core network connect attachment between a core network and an appliance. The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).

## Syntax
<a name="aws-resource-networkmanager-connectpeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-connectpeer-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkManager::ConnectPeer",
  "Properties" : {
      "[BgpOptions](#cfn-networkmanager-connectpeer-bgpoptions)" : {{BgpOptions}},
      "[ConnectAttachmentId](#cfn-networkmanager-connectpeer-connectattachmentid)" : {{String}},
      "[CoreNetworkAddress](#cfn-networkmanager-connectpeer-corenetworkaddress)" : {{String}},
      "[InsideCidrBlocks](#cfn-networkmanager-connectpeer-insidecidrblocks)" : {{[ String, ... ]}},
      "[PeerAddress](#cfn-networkmanager-connectpeer-peeraddress)" : {{String}},
      "[SubnetArn](#cfn-networkmanager-connectpeer-subnetarn)" : {{String}},
      "[Tags](#cfn-networkmanager-connectpeer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-connectpeer-syntax.yaml"></a>

```
Type: AWS::NetworkManager::ConnectPeer
Properties:
  [BgpOptions](#cfn-networkmanager-connectpeer-bgpoptions): {{
    BgpOptions}}
  [ConnectAttachmentId](#cfn-networkmanager-connectpeer-connectattachmentid): {{String}}
  [CoreNetworkAddress](#cfn-networkmanager-connectpeer-corenetworkaddress): {{String}}
  [InsideCidrBlocks](#cfn-networkmanager-connectpeer-insidecidrblocks): {{
    - String}}
  [PeerAddress](#cfn-networkmanager-connectpeer-peeraddress): {{String}}
  [SubnetArn](#cfn-networkmanager-connectpeer-subnetarn): {{String}}
  [Tags](#cfn-networkmanager-connectpeer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networkmanager-connectpeer-properties"></a>

`BgpOptions`  <a name="cfn-networkmanager-connectpeer-bgpoptions"></a>
Describes the BGP options.
*Required*: No
*Type*: [BgpOptions](aws-properties-networkmanager-connectpeer-bgpoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectAttachmentId`  <a name="cfn-networkmanager-connectpeer-connectattachmentid"></a>
The ID of the attachment to connect.
*Required*: Yes
*Type*: String
*Pattern*: `^attachment-([0-9a-f]{8,17})$`
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CoreNetworkAddress`  <a name="cfn-networkmanager-connectpeer-corenetworkaddress"></a>
The IP address of a core network.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InsideCidrBlocks`  <a name="cfn-networkmanager-connectpeer-insidecidrblocks"></a>
The inside IP addresses used for a Connect peer configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddress`  <a name="cfn-networkmanager-connectpeer-peeraddress"></a>
The IP address of the Connect peer.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetArn`  <a name="cfn-networkmanager-connectpeer-subnetarn"></a>
The subnet ARN of the Connect peer.
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networkmanager-connectpeer-tags"></a>
The list of key-value tags associated with the Connect peer.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-connectpeer-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkmanager-connectpeer-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-connectpeer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ConnectPeerId`. For example, `{ "Ref: "connect-peer--041e25dbc928d7e61" }`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networkmanager-connectpeer-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networkmanager-connectpeer-return-values-fn--getatt-fn--getatt"></a>

`ConnectPeerId`  <a name="ConnectPeerId-fn::getatt"></a>
The ID of the Connect peer.

`CoreNetworkId`  <a name="CoreNetworkId-fn::getatt"></a>
The core network ID.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the Connect peer was created.

`EdgeLocation`  <a name="EdgeLocation-fn::getatt"></a>
The Connect peer Regions where edges are located.

`LastModificationErrors`  <a name="LastModificationErrors-fn::getatt"></a>
Describes the error associated with the attachment request.

`State`  <a name="State-fn::getatt"></a>
The state of the Connect peer. This will be: `REJECTED` \| `PENDING_ATTACHMENT_ACCEPTANCE` \| `CREATING` \| `FAILED` \| `AVAILABLE` \| `UPDATING` \| ` PENDING_NETWORK_UPDATE` \| `PENDING_TAG_ACCEPTANCE` \| `DELETING`.
