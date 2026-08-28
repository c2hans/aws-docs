---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-anycastiplist-anycastiplist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::AnycastIpList AnycastIpList
<a name="aws-properties-cloudfront-anycastiplist-anycastiplist"></a>

An Anycast static IP list. For more information, see [Request Anycast static IPs to use for allowlisting](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/request-static-ips.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-properties-cloudfront-anycastiplist-anycastiplist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-anycastiplist-anycastiplist-syntax.json"></a>

```
{
  "[AnycastIps](#cfn-cloudfront-anycastiplist-anycastiplist-anycastips)" : {{[ String, ... ]}},
  "[Arn](#cfn-cloudfront-anycastiplist-anycastiplist-arn)" : {{String}},
  "[Id](#cfn-cloudfront-anycastiplist-anycastiplist-id)" : {{String}},
  "[IpAddressType](#cfn-cloudfront-anycastiplist-anycastiplist-ipaddresstype)" : {{String}},
  "[IpamCidrConfigResults](#cfn-cloudfront-anycastiplist-anycastiplist-ipamcidrconfigresults)" : {{[ IpamCidrConfigResult, ... ]}},
  "[IpCount](#cfn-cloudfront-anycastiplist-anycastiplist-ipcount)" : {{Integer}},
  "[LastModifiedTime](#cfn-cloudfront-anycastiplist-anycastiplist-lastmodifiedtime)" : {{String}},
  "[Name](#cfn-cloudfront-anycastiplist-anycastiplist-name)" : {{String}},
  "[Status](#cfn-cloudfront-anycastiplist-anycastiplist-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-anycastiplist-anycastiplist-syntax.yaml"></a>

```
  [AnycastIps](#cfn-cloudfront-anycastiplist-anycastiplist-anycastips): {{
    - String}}
  [Arn](#cfn-cloudfront-anycastiplist-anycastiplist-arn): {{String}}
  [Id](#cfn-cloudfront-anycastiplist-anycastiplist-id): {{String}}
  [IpAddressType](#cfn-cloudfront-anycastiplist-anycastiplist-ipaddresstype): {{String}}
  [IpamCidrConfigResults](#cfn-cloudfront-anycastiplist-anycastiplist-ipamcidrconfigresults): {{
    - IpamCidrConfigResult}}
  [IpCount](#cfn-cloudfront-anycastiplist-anycastiplist-ipcount): {{Integer}}
  [LastModifiedTime](#cfn-cloudfront-anycastiplist-anycastiplist-lastmodifiedtime): {{String}}
  [Name](#cfn-cloudfront-anycastiplist-anycastiplist-name): {{String}}
  [Status](#cfn-cloudfront-anycastiplist-anycastiplist-status): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-anycastiplist-anycastiplist-properties"></a>

`AnycastIps`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-anycastips"></a>
The static IP addresses that are allocated to the Anycast static IP list.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arn`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-arn"></a>
The Amazon Resource Name (ARN) of the Anycast static IP list.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-id"></a>
The ID of the Anycast static IP list.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-ipaddresstype"></a>
The IP address type for the Anycast static IP list.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamCidrConfigResults`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-ipamcidrconfigresults"></a>
The results for the IPAM CIDRs that defines a specific IP address range, IPAM pool, and associated Anycast IP address.
*Required*: No
*Type*: Array of [IpamCidrConfigResult](aws-properties-cloudfront-anycastiplist-ipamcidrconfigresult.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpCount`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-ipcount"></a>
The number of IP addresses in the Anycast static IP list.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastModifiedTime`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-lastmodifiedtime"></a>
The last time the Anycast static IP list was modified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-name"></a>
The name of the Anycast static IP list.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]{1,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cloudfront-anycastiplist-anycastiplist-status"></a>
The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
