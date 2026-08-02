---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::InputSecurityGroup InputWhitelistRuleCidr
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr"></a>

An IPv4 CIDR range to include in this input security group.

The parent of this entity is InputSecurityGroup.

## Syntax
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr-syntax.json"></a>

```
{
  "[Cidr](#cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr-syntax.yaml"></a>

```
  [Cidr](#cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr): {{String}}
```

## Properties
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr-properties"></a>

`Cidr`  <a name="cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr"></a>
An IPv4 CIDR range to include in this input security group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
