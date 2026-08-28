---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet AcceleratorTotalMemoryMiBRequest
<a name="aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest"></a>

The minimum and maximum amount of total accelerator memory, in MiB.

## Syntax
<a name="aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-max)" : {{Integer}},
  "[Min](#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-max): {{Integer}}
  [Min](#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest-properties"></a>

`Max`  <a name="cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-max"></a>
The maximum amount of accelerator memory, in MiB. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Min`  <a name="cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-min"></a>
The minimum amount of accelerator memory, in MiB. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
