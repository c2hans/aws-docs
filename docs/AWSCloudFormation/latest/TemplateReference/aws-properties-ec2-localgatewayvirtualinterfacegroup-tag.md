---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-localgatewayvirtualinterfacegroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LocalGatewayVirtualInterfaceGroup Tag
<a name="aws-properties-ec2-localgatewayvirtualinterfacegroup-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-ec2-localgatewayvirtualinterfacegroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-localgatewayvirtualinterfacegroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-localgatewayvirtualinterfacegroup-tag-key)" : {{String}},
  "[Value](#cfn-ec2-localgatewayvirtualinterfacegroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-localgatewayvirtualinterfacegroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-localgatewayvirtualinterfacegroup-tag-key): {{String}}
  [Value](#cfn-ec2-localgatewayvirtualinterfacegroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-localgatewayvirtualinterfacegroup-tag-properties"></a>

`Key`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-tag-key"></a>
The key of the tag.
Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:`.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:.*)`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-tag-value"></a>
The value of the tag.
Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:.*)`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
