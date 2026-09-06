---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::AnycastIpList IpamCidrConfigResult
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult"></a>

The result for the IPAM CIDR that defines a specific IP address range, IPAM pool, and associated Anycast IP address.

## Syntax
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult-syntax.json"></a>

```
{
  "[AnycastIp](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-anycastip)" : {{String}},
  "[Cidr](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-cidr)" : {{String}},
  "[IpamPoolArn](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-ipampoolarn)" : {{String}},
  "[Status](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult-syntax.yaml"></a>

```
  [AnycastIp](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-anycastip): {{String}}
  [Cidr](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-cidr): {{String}}
  [IpamPoolArn](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-ipampoolarn): {{String}}
  [Status](#cfn-cloudfront-anycastiplist-ipamcidrconfigresult-status): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult-properties"></a>

`AnycastIp`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfigresult-anycastip"></a>
The specified Anycast IP address allocated from the IPAM pool for this CIDR configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Cidr`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfigresult-cidr"></a>
The CIDR that specifies the IP address range for this IPAM configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamPoolArn`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfigresult-ipampoolarn"></a>
The Amazon Resource Name (ARN) of the IPAM pool that the CIDR block is assigned to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfigresult-status"></a>
The current status of the IPAM CIDR configuration.
*Required*: No
*Type*: String
*Allowed values*: `provisioned | failed-provision | provisioning | deprovisioned | failed-deprovision | deprovisioning | advertised | failed-advertise | advertising | withdrawn | failed-withdraw | withdrawing`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
