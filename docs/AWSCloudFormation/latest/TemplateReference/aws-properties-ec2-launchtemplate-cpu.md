---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-cpu.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate Cpu
<a name="aws-properties-ec2-launchtemplate-cpu"></a>

Specifies the CPU performance to consider when using an instance family as the baseline reference.

## Syntax
<a name="aws-properties-ec2-launchtemplate-cpu-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-cpu-syntax.json"></a>

```
{
  "[References](#cfn-ec2-launchtemplate-cpu-references)" : {{[ Reference, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-cpu-syntax.yaml"></a>

```
  [References](#cfn-ec2-launchtemplate-cpu-references): {{
    - Reference}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-cpu-properties"></a>

`References`  <a name="cfn-ec2-launchtemplate-cpu-references"></a>
The instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes are compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.
*Required*: No
*Type*: Array of [Reference](aws-properties-ec2-launchtemplate-reference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
