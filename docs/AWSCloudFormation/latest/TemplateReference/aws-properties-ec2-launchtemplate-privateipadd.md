---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-privateipadd.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate PrivateIpAdd
<a name="aws-properties-ec2-launchtemplate-privateipadd"></a>

Specifies a secondary private IPv4 address for a network interface.

`PrivateIpAdd` is a property of [AWS::EC2::LaunchTemplate NetworkInterface](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-privateipadd-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-privateipadd-syntax.json"></a>

```
{
  "[Primary](#cfn-ec2-launchtemplate-privateipadd-primary)" : {{Boolean}},
  "[PrivateIpAddress](#cfn-ec2-launchtemplate-privateipadd-privateipaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-privateipadd-syntax.yaml"></a>

```
  [Primary](#cfn-ec2-launchtemplate-privateipadd-primary): {{Boolean}}
  [PrivateIpAddress](#cfn-ec2-launchtemplate-privateipadd-privateipaddress): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-privateipadd-properties"></a>

`Primary`  <a name="cfn-ec2-launchtemplate-privateipadd-primary"></a>
Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddress`  <a name="cfn-ec2-launchtemplate-privateipadd-privateipaddress"></a>
The private IPv4 address.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-privateipadd--seealso"></a>
+ [ PrivateIpAddressSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PrivateIpAddressSpecification.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
