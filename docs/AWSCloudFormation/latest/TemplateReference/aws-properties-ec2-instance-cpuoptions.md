---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-cpuoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance CpuOptions
<a name="aws-properties-ec2-instance-cpuoptions"></a>

Specifies the CPU options for the instance. When you specify CPU options, you must specify both the number of CPU cores and threads per core.

Modifying the CPU options for an instance results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).

For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Syntax
<a name="aws-properties-ec2-instance-cpuoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-cpuoptions-syntax.json"></a>

```
{
  "[CoreCount](#cfn-ec2-instance-cpuoptions-corecount)" : {{Integer}},
  "[ThreadsPerCore](#cfn-ec2-instance-cpuoptions-threadspercore)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-instance-cpuoptions-syntax.yaml"></a>

```
  [CoreCount](#cfn-ec2-instance-cpuoptions-corecount): {{Integer}}
  [ThreadsPerCore](#cfn-ec2-instance-cpuoptions-threadspercore): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-instance-cpuoptions-properties"></a>

`CoreCount`  <a name="cfn-ec2-instance-cpuoptions-corecount"></a>
The number of CPU cores for the instance.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThreadsPerCore`  <a name="cfn-ec2-instance-cpuoptions-threadspercore"></a>
The number of threads per CPU core.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
