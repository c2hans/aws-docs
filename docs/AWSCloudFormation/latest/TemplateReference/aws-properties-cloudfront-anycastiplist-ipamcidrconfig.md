---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-anycastiplist-ipamcidrconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::AnycastIpList IpamCidrConfig
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfig"></a>

Configuration for an IPAM CIDR that defines a specific IP address range, IPAM pool, and associated Anycast IP address.

## Syntax
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfig-syntax.json"></a>

```
{
  "[Cidr](#cfn-cloudfront-anycastiplist-ipamcidrconfig-cidr)" : {{String}},
  "[IpamPoolArn](#cfn-cloudfront-anycastiplist-ipamcidrconfig-ipampoolarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfig-syntax.yaml"></a>

```
  [Cidr](#cfn-cloudfront-anycastiplist-ipamcidrconfig-cidr): {{String}}
  [IpamPoolArn](#cfn-cloudfront-anycastiplist-ipamcidrconfig-ipampoolarn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfig-properties"></a>

`Cidr`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfig-cidr"></a>
The CIDR that specifies the IP address range for this IPAM configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamPoolArn`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfig-ipampoolarn"></a>
The Amazon Resource Name (ARN) of the IPAM pool that the CIDR block is assigned to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
