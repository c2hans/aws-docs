---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-memorymibrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet MemoryMiBRequest
<a name="aws-properties-ec2-spotfleet-memorymibrequest"></a>

The minimum and maximum amount of memory, in MiB.

## Syntax
<a name="aws-properties-ec2-spotfleet-memorymibrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-memorymibrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-spotfleet-memorymibrequest-max)" : {{Integer}},
  "[Min](#cfn-ec2-spotfleet-memorymibrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-memorymibrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-spotfleet-memorymibrequest-max): {{Integer}}
  [Min](#cfn-ec2-spotfleet-memorymibrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-memorymibrequest-properties"></a>

`Max`  <a name="cfn-ec2-spotfleet-memorymibrequest-max"></a>
The maximum amount of memory, in MiB. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-spotfleet-memorymibrequest-min"></a>
The minimum amount of memory, in MiB. To specify no minimum limit, specify `0`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
