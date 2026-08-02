---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnetcidrblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SubnetCidrBlock
<a name="aws-resource-ec2-subnetcidrblock"></a>

Associates a CIDR block with your subnet. You can associate a single IPv6 CIDR block with your subnet.

## Syntax
<a name="aws-resource-ec2-subnetcidrblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-subnetcidrblock-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SubnetCidrBlock",
  "Properties" : {
      "[Ipv6CidrBlock](#cfn-ec2-subnetcidrblock-ipv6cidrblock)" : {{String}},
      "[Ipv6IpamPoolId](#cfn-ec2-subnetcidrblock-ipv6ipampoolid)" : {{String}},
      "[Ipv6NetmaskLength](#cfn-ec2-subnetcidrblock-ipv6netmasklength)" : {{Integer}},
      "[SubnetId](#cfn-ec2-subnetcidrblock-subnetid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-subnetcidrblock-syntax.yaml"></a>

```
Type: AWS::EC2::SubnetCidrBlock
Properties:
  [Ipv6CidrBlock](#cfn-ec2-subnetcidrblock-ipv6cidrblock): {{String}}
  [Ipv6IpamPoolId](#cfn-ec2-subnetcidrblock-ipv6ipampoolid): {{String}}
  [Ipv6NetmaskLength](#cfn-ec2-subnetcidrblock-ipv6netmasklength): {{Integer}}
  [SubnetId](#cfn-ec2-subnetcidrblock-subnetid): {{String}}
```

## Properties
<a name="aws-resource-ec2-subnetcidrblock-properties"></a>

`Ipv6CidrBlock`  <a name="cfn-ec2-subnetcidrblock-ipv6cidrblock"></a>
The IPv6 network range for the subnet, in CIDR notation.
*Required*: Conditional
*Type*: String
*Maximum*: `42`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6IpamPoolId`  <a name="cfn-ec2-subnetcidrblock-ipv6ipampoolid"></a>
An IPv6 IPAM pool ID for the subnet.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6NetmaskLength`  <a name="cfn-ec2-subnetcidrblock-ipv6netmasklength"></a>
An IPv6 netmask length for the subnet.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-subnetcidrblock-subnetid"></a>
The ID of the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-subnetcidrblock-return-values"></a>

### Ref
<a name="aws-resource-ec2-subnetcidrblock-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the association ID for the subnet’s IPv6 CIDR block.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-subnetcidrblock-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-subnetcidrblock-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the association.

`IpSource`  <a name="IpSource-fn::getatt"></a>
The source that allocated the IP address space. `byoip` or `amazon` indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). `none` indicates private space.

`Ipv6AddressAttribute`  <a name="Ipv6AddressAttribute-fn::getatt"></a>
Public IPv6 addresses are those advertised on the internet from AWS. Private IP addresses are not and cannot be advertised on the internet from AWS.
