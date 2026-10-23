---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayAttachmentNatConfiguration NatRule
<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule"></a>

<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule-description"></a>The `NatRule` property type specifies Property description not available. for an [AWS::EC2::TransitGatewayAttachmentNatConfiguration](aws-resource-ec2-transitgatewayattachmentnatconfiguration.md).

## Syntax
<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule-syntax.json"></a>

```
{
  "[MatchSourceCidr](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-matchsourcecidr)" : {{String}},
  "[NatCidr](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-natcidr)" : {{String}},
  "[RuleNumber](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-rulenumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule-syntax.yaml"></a>

```
  [MatchSourceCidr](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-matchsourcecidr): {{String}}
  [NatCidr](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-natcidr): {{String}}
  [RuleNumber](#cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-rulenumber): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-transitgatewayattachmentnatconfiguration-natrule-properties"></a>

`MatchSourceCidr`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-matchsourcecidr"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatCidr`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-natcidr"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleNumber`  <a name="cfn-ec2-transitgatewayattachmentnatconfiguration-natrule-rulenumber"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `32766`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
