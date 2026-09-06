---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Subnet PrivateDnsNameOptionsOnLaunch
<a name="aws-properties-ec2-subnet-privatednsnameoptionsonlaunch"></a>

Specifies the options for instance hostnames.

## Syntax
<a name="aws-properties-ec2-subnet-privatednsnameoptionsonlaunch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-subnet-privatednsnameoptionsonlaunch-syntax.json"></a>

```
{
  "[EnableResourceNameDnsAAAARecord](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsaaaarecord)" : {{Boolean}},
  "[EnableResourceNameDnsARecord](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsarecord)" : {{Boolean}},
  "[HostnameType](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-hostnametype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-subnet-privatednsnameoptionsonlaunch-syntax.yaml"></a>

```
  [EnableResourceNameDnsAAAARecord](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsaaaarecord): {{Boolean}}
  [EnableResourceNameDnsARecord](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsarecord): {{Boolean}}
  [HostnameType](#cfn-ec2-subnet-privatednsnameoptionsonlaunch-hostnametype): {{String}}
```

## Properties
<a name="aws-properties-ec2-subnet-privatednsnameoptionsonlaunch-properties"></a>

`EnableResourceNameDnsAAAARecord`  <a name="cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsaaaarecord"></a>
Indicates whether to respond to DNS queries for instance hostname with DNS AAAA records.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableResourceNameDnsARecord`  <a name="cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsarecord"></a>
Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostnameType`  <a name="cfn-ec2-subnet-privatednsnameoptionsonlaunch-hostnametype"></a>
The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.
*Required*: No
*Type*: String
*Allowed values*: `ip-name | resource-name`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
