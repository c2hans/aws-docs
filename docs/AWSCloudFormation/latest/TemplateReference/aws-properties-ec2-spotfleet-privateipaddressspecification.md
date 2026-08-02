---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-privateipaddressspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet PrivateIpAddressSpecification
<a name="aws-properties-ec2-spotfleet-privateipaddressspecification"></a>

Describes a secondary private IPv4 address for a network interface.

## Syntax
<a name="aws-properties-ec2-spotfleet-privateipaddressspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-privateipaddressspecification-syntax.json"></a>

```
{
  "[Primary](#cfn-ec2-spotfleet-privateipaddressspecification-primary)" : {{Boolean}},
  "[PrivateIpAddress](#cfn-ec2-spotfleet-privateipaddressspecification-privateipaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-privateipaddressspecification-syntax.yaml"></a>

```
  [Primary](#cfn-ec2-spotfleet-privateipaddressspecification-primary): {{Boolean}}
  [PrivateIpAddress](#cfn-ec2-spotfleet-privateipaddressspecification-privateipaddress): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-privateipaddressspecification-properties"></a>

`Primary`  <a name="cfn-ec2-spotfleet-privateipaddressspecification-primary"></a>
Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddress`  <a name="cfn-ec2-spotfleet-privateipaddressspecification-privateipaddress"></a>
The private IPv4 address.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
