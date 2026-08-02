---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ipamprefixlistresolver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMPrefixListResolver
<a name="aws-resource-ec2-ipamprefixlistresolver"></a>

An IPAM prefix list resolver is a component that manages the synchronization between IPAM's CIDR selection rules and customer-managed prefix lists. It automates connectivity configurations by selecting CIDRs from IPAM's database based on your business logic and synchronizing them with prefix lists used in resources such as VPC route tables and security groups.

## Syntax
<a name="aws-resource-ec2-ipamprefixlistresolver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ipamprefixlistresolver-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IPAMPrefixListResolver",
  "Properties" : {
      "[AddressFamily](#cfn-ec2-ipamprefixlistresolver-addressfamily)" : {{String}},
      "[Description](#cfn-ec2-ipamprefixlistresolver-description)" : {{String}},
      "[IpamId](#cfn-ec2-ipamprefixlistresolver-ipamid)" : {{String}},
      "[Rules](#cfn-ec2-ipamprefixlistresolver-rules)" : {{[ IpamPrefixListResolverRule, ... ]}},
      "[Tags](#cfn-ec2-ipamprefixlistresolver-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ipamprefixlistresolver-syntax.yaml"></a>

```
Type: AWS::EC2::IPAMPrefixListResolver
Properties:
  [AddressFamily](#cfn-ec2-ipamprefixlistresolver-addressfamily): {{String}}
  [Description](#cfn-ec2-ipamprefixlistresolver-description): {{String}}
  [IpamId](#cfn-ec2-ipamprefixlistresolver-ipamid): {{String}}
  [Rules](#cfn-ec2-ipamprefixlistresolver-rules): {{
    - IpamPrefixListResolverRule}}
  [Tags](#cfn-ec2-ipamprefixlistresolver-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-ipamprefixlistresolver-properties"></a>

`AddressFamily`  <a name="cfn-ec2-ipamprefixlistresolver-addressfamily"></a>
The address family (IPv4 or IPv6) for the IPAM prefix list resolver.
*Required*: Yes
*Type*: String
*Allowed values*: `ipv4 | ipv6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ec2-ipamprefixlistresolver-description"></a>
The description of the IPAM prefix list resolver.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamId`  <a name="cfn-ec2-ipamprefixlistresolver-ipamid"></a>
The ID of the IPAM associated with this resolver.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Rules`  <a name="cfn-ec2-ipamprefixlistresolver-rules"></a>
CIDR selection rules for this resolver.
*Required*: No
*Type*: Array of [IpamPrefixListResolverRule](aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-ipamprefixlistresolver-tags"></a>
The tags assigned to the IPAM prefix list resolver.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-ipamprefixlistresolver-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-ipamprefixlistresolver-return-values"></a>

### Ref
<a name="aws-resource-ec2-ipamprefixlistresolver-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the prefix list resolver ID. For example: `ipam-plr-111122223333`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-ipamprefixlistresolver-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-ipamprefixlistresolver-return-values-fn--getatt-fn--getatt"></a>

`IpamArn`  <a name="IpamArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IPAM associated with this resolver.

`IpamPrefixListResolverArn`  <a name="IpamPrefixListResolverArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IPAM prefix list resolver.

`IpamPrefixListResolverId`  <a name="IpamPrefixListResolverId-fn::getatt"></a>
The ID of the IPAM prefix list resolver.
