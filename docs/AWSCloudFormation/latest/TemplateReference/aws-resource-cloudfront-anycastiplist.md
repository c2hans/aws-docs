---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-anycastiplist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::AnycastIpList
<a name="aws-resource-cloudfront-anycastiplist"></a>

An Anycast static IP list. For more information, see [Request Anycast static IPs to use for allowlisting](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/request-static-ips.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-resource-cloudfront-anycastiplist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-anycastiplist-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::AnycastIpList",
  "Properties" : {
      "[IpAddressType](#cfn-cloudfront-anycastiplist-ipaddresstype)" : {{String}},
      "[IpamCidrConfigs](#cfn-cloudfront-anycastiplist-ipamcidrconfigs)" : {{[ IpamCidrConfig, ... ]}},
      "[IpCount](#cfn-cloudfront-anycastiplist-ipcount)" : {{Integer}},
      "[Name](#cfn-cloudfront-anycastiplist-name)" : {{String}},
      "[Tags](#cfn-cloudfront-anycastiplist-tags)" : {{Tags}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-anycastiplist-syntax.yaml"></a>

```
Type: AWS::CloudFront::AnycastIpList
Properties:
  [IpAddressType](#cfn-cloudfront-anycastiplist-ipaddresstype): {{String}}
  [IpamCidrConfigs](#cfn-cloudfront-anycastiplist-ipamcidrconfigs): {{
    - IpamCidrConfig}}
  [IpCount](#cfn-cloudfront-anycastiplist-ipcount): {{Integer}}
  [Name](#cfn-cloudfront-anycastiplist-name): {{String}}
  [Tags](#cfn-cloudfront-anycastiplist-tags): {{
    Tags}}
```

## Properties
<a name="aws-resource-cloudfront-anycastiplist-properties"></a>

`IpAddressType`  <a name="cfn-cloudfront-anycastiplist-ipaddresstype"></a>
The IP address type for the Anycast static IP list.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamCidrConfigs`  <a name="cfn-cloudfront-anycastiplist-ipamcidrconfigs"></a>
A list of IPAM CIDR configurations that define the IP address ranges, IPAM pools, and associated Anycast IP addresses.
*Required*: No
*Type*: Array of [IpamCidrConfig](aws-properties-cloudfront-anycastiplist-ipamcidrconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpCount`  <a name="cfn-cloudfront-anycastiplist-ipcount"></a>
The number of IP addresses in the Anycast static IP list.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudfront-anycastiplist-name"></a>
The name of the Anycast static IP list.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]{1,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-anycastiplist-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: [Tags](aws-properties-cloudfront-anycastiplist-tags.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudfront-anycastiplist-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-anycastiplist-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Anycast IP list. For example: `aip_7XdPQUqEXAMPLE283z455j`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudfront-anycastiplist-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-anycastiplist-return-values-fn--getatt-fn--getatt"></a>

`ETag`  <a name="ETag-fn::getatt"></a>
A complex type that contains `Tag` key and `Tag` value.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the Anycast static IP list.

`IpamCidrConfigResults`  <a name="IpamCidrConfigResults-fn::getatt"></a>
The results for the IPAM CIDRs that defines a specific IP address range, IPAM pool, and associated Anycast IP address.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
