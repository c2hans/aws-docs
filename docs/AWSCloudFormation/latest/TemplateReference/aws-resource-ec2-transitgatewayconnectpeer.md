---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewayconnectpeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayConnectPeer
<a name="aws-resource-ec2-transitgatewayconnectpeer"></a>

Describes a transit gateway Connect peer.

## Syntax
<a name="aws-resource-ec2-transitgatewayconnectpeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewayconnectpeer-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayConnectPeer",
  "Properties" : {
      "[ConnectPeerConfiguration](#cfn-ec2-transitgatewayconnectpeer-connectpeerconfiguration)" : {{TransitGatewayConnectPeerConfiguration}},
      "[Tags](#cfn-ec2-transitgatewayconnectpeer-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayAttachmentId](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewayconnectpeer-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayConnectPeer
Properties:
  [ConnectPeerConfiguration](#cfn-ec2-transitgatewayconnectpeer-connectpeerconfiguration): {{
    TransitGatewayConnectPeerConfiguration}}
  [Tags](#cfn-ec2-transitgatewayconnectpeer-tags): {{
    - Tag}}
  [TransitGatewayAttachmentId](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewayconnectpeer-properties"></a>

`ConnectPeerConfiguration`  <a name="cfn-ec2-transitgatewayconnectpeer-connectpeerconfiguration"></a>
The Connect peer details.
*Required*: Yes
*Type*: [TransitGatewayConnectPeerConfiguration](aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-transitgatewayconnectpeer-tags"></a>
The tags for the Connect peer.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewayconnectpeer-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentid"></a>
The ID of the Connect attachment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewayconnectpeer-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewayconnectpeer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Connect peer.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewayconnectpeer-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewayconnectpeer-return-values-fn--getatt-fn--getatt"></a>

`ConnectPeerConfiguration.BgpConfigurations`  <a name="ConnectPeerConfiguration.BgpConfigurations-fn::getatt"></a>
The BGP configuration details.

`ConnectPeerConfiguration.Protocol`  <a name="ConnectPeerConfiguration.Protocol-fn::getatt"></a>
The tunnel protocol.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time.

`State`  <a name="State-fn::getatt"></a>
The state of the Connect peer.

`TransitGatewayConnectPeerId`  <a name="TransitGatewayConnectPeerId-fn::getatt"></a>
The ID of the Connect peer.
