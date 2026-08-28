---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-acceleratorcount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate AcceleratorCount
<a name="aws-properties-ec2-launchtemplate-acceleratorcount"></a>

The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance.

## Syntax
<a name="aws-properties-ec2-launchtemplate-acceleratorcount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-acceleratorcount-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-launchtemplate-acceleratorcount-max)" : {{Integer}},
  "[Min](#cfn-ec2-launchtemplate-acceleratorcount-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-acceleratorcount-syntax.yaml"></a>

```
  [Max](#cfn-ec2-launchtemplate-acceleratorcount-max): {{Integer}}
  [Min](#cfn-ec2-launchtemplate-acceleratorcount-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-acceleratorcount-properties"></a>

`Max`  <a name="cfn-ec2-launchtemplate-acceleratorcount-max"></a>
The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set `Max` to `0`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-launchtemplate-acceleratorcount-min"></a>
The minimum number of accelerators. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
