---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-networkinterfacecount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate NetworkInterfaceCount
<a name="aws-properties-ec2-launchtemplate-networkinterfacecount"></a>

The minimum and maximum number of network interfaces.

## Syntax
<a name="aws-properties-ec2-launchtemplate-networkinterfacecount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-networkinterfacecount-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-launchtemplate-networkinterfacecount-max)" : {{Integer}},
  "[Min](#cfn-ec2-launchtemplate-networkinterfacecount-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-networkinterfacecount-syntax.yaml"></a>

```
  [Max](#cfn-ec2-launchtemplate-networkinterfacecount-max): {{Integer}}
  [Min](#cfn-ec2-launchtemplate-networkinterfacecount-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-networkinterfacecount-properties"></a>

`Max`  <a name="cfn-ec2-launchtemplate-networkinterfacecount-max"></a>
The maximum number of network interfaces. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-launchtemplate-networkinterfacecount-min"></a>
The minimum number of network interfaces. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
