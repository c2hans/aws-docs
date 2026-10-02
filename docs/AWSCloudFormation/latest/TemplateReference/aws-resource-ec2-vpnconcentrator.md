---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpnconcentrator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConcentrator
<a name="aws-resource-ec2-vpnconcentrator"></a>

Describes a VPN concentrator.

## Syntax
<a name="aws-resource-ec2-vpnconcentrator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpnconcentrator-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPNConcentrator",
  "Properties" : {
      "[Tags](#cfn-ec2-vpnconcentrator-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-vpnconcentrator-transitgatewayid)" : {{String}},
      "[Type](#cfn-ec2-vpnconcentrator-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpnconcentrator-syntax.yaml"></a>

```
Type: AWS::EC2::VPNConcentrator
Properties:
  [Tags](#cfn-ec2-vpnconcentrator-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-vpnconcentrator-transitgatewayid): {{String}}
  [Type](#cfn-ec2-vpnconcentrator-type): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpnconcentrator-properties"></a>

`Tags`  <a name="cfn-ec2-vpnconcentrator-tags"></a>
Any tags assigned to the VPN concentrator.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-vpnconcentrator-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-vpnconcentrator-transitgatewayid"></a>
The ID of the transit gateway associated with the VPN concentrator.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-ec2-vpnconcentrator-type"></a>
The type of VPN concentrator.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-vpnconcentrator-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpnconcentrator-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-vpnconcentrator-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-vpnconcentrator-return-values-fn--getatt-fn--getatt"></a>

`TransitGatewayAttachmentId`  <a name="TransitGatewayAttachmentId-fn::getatt"></a>
The ID of the transit gateway attachment for the VPN concentrator.

`VpnConcentratorId`  <a name="VpnConcentratorId-fn::getatt"></a>
The ID of the VPN concentrator to associate with the VPN connection.
