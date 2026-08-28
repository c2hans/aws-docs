---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-privatednsnameoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate PrivateDnsNameOptions
<a name="aws-properties-ec2-launchtemplate-privatednsnameoptions"></a>

The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Syntax
<a name="aws-properties-ec2-launchtemplate-privatednsnameoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-privatednsnameoptions-syntax.json"></a>

```
{
  "[EnableResourceNameDnsAAAARecord](#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsaaaarecord)" : {{Boolean}},
  "[EnableResourceNameDnsARecord](#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsarecord)" : {{Boolean}},
  "[HostnameType](#cfn-ec2-launchtemplate-privatednsnameoptions-hostnametype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-privatednsnameoptions-syntax.yaml"></a>

```
  [EnableResourceNameDnsAAAARecord](#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsaaaarecord): {{Boolean}}
  [EnableResourceNameDnsARecord](#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsarecord): {{Boolean}}
  [HostnameType](#cfn-ec2-launchtemplate-privatednsnameoptions-hostnametype): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-privatednsnameoptions-properties"></a>

`EnableResourceNameDnsAAAARecord`  <a name="cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsaaaarecord"></a>
Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableResourceNameDnsARecord`  <a name="cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsarecord"></a>
Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostnameType`  <a name="cfn-ec2-launchtemplate-privatednsnameoptions-hostnametype"></a>
The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon Elastic Compute Cloud User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `ip-name | resource-name`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
