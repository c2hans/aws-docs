---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinterface-instanceipv6address.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterface InstanceIpv6Address
<a name="aws-properties-ec2-networkinterface-instanceipv6address"></a>

Describes the IPv6 addresses to associate with the network interface.

## Syntax
<a name="aws-properties-ec2-networkinterface-instanceipv6address-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinterface-instanceipv6address-syntax.json"></a>

```
{
  "[Ipv6Address](#cfn-ec2-networkinterface-instanceipv6address-ipv6address)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinterface-instanceipv6address-syntax.yaml"></a>

```
  [Ipv6Address](#cfn-ec2-networkinterface-instanceipv6address-ipv6address): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinterface-instanceipv6address-properties"></a>

`Ipv6Address`  <a name="cfn-ec2-networkinterface-instanceipv6address-ipv6address"></a>
An IPv6 address to associate with the network interface.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
