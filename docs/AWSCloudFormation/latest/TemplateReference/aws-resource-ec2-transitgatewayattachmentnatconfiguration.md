---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewayattachmentnatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayAttachmentNatConfiguration
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration"></a>

<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-description"></a>The `AWS::EC2::TransitGatewayAttachmentNatConfiguration` resource Property description not available. for EC2.

## Syntax
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayAttachmentNatConfiguration",
  "Properties" : {
      "[NatGatewayRules](#cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewayrules)" : {{[ NatRule, ... ]}},
      "[NatGatewaySupport](#cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewaysupport)" : {{String}},
      "[NatSystemRouteSupport](#cfn-ec2-transitgatewayattachmentnatconfiguration-natsystemroutesupport)" : {{String}},
      "[TransitGatewayAttachmentId](#cfn-ec2-transitgatewayattachmentnatconfiguration-transitgatewayattachmentid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayAttachmentNatConfiguration
Properties:
  [NatGatewayRules](#cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewayrules): {{
    - NatRule}}
  [NatGatewaySupport](#cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewaysupport): {{String}}
  [NatSystemRouteSupport](#cfn-ec2-transitgatewayattachmentnatconfiguration-natsystemroutesupport): {{String}}
  [TransitGatewayAttachmentId](#cfn-ec2-transitgatewayattachmentnatconfiguration-transitgatewayattachmentid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-properties"></a>

`NatGatewayRules`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewayrules"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [NatRule](aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatGatewaySupport`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natgatewaysupport"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatSystemRouteSupport`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natsystemroutesupport"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-transitgatewayattachmentid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^tgw-attach-[0-9a-f]{8,34}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewayattachmentnatconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.
