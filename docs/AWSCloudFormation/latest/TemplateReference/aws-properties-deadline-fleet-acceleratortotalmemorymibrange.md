---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-acceleratortotalmemorymibrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet AcceleratorTotalMemoryMiBRange
<a name="aws-properties-deadline-fleet-acceleratortotalmemorymibrange"></a>

Defines the maximum and minimum amount of memory, in MiB, to use for the accelerator.

## Syntax
<a name="aws-properties-deadline-fleet-acceleratortotalmemorymibrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-acceleratortotalmemorymibrange-syntax.json"></a>

```
{
  "[Max](#cfn-deadline-fleet-acceleratortotalmemorymibrange-max)" : {{Integer}},
  "[Min](#cfn-deadline-fleet-acceleratortotalmemorymibrange-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-acceleratortotalmemorymibrange-syntax.yaml"></a>

```
  [Max](#cfn-deadline-fleet-acceleratortotalmemorymibrange-max): {{Integer}}
  [Min](#cfn-deadline-fleet-acceleratortotalmemorymibrange-min): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-acceleratortotalmemorymibrange-properties"></a>

`Max`  <a name="cfn-deadline-fleet-acceleratortotalmemorymibrange-max"></a>
The maximum amount of memory to use for the accelerator, measured in MiB.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-deadline-fleet-acceleratortotalmemorymibrange-min"></a>
The minimum amount of memory to use for the accelerator, measured in MiB.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
