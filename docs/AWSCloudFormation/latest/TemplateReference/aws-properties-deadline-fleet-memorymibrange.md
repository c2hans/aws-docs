---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-memorymibrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet MemoryMiBRange
<a name="aws-properties-deadline-fleet-memorymibrange"></a>

The range of memory in MiB.

## Syntax
<a name="aws-properties-deadline-fleet-memorymibrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-memorymibrange-syntax.json"></a>

```
{
  "[Max](#cfn-deadline-fleet-memorymibrange-max)" : {{Integer}},
  "[Min](#cfn-deadline-fleet-memorymibrange-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-memorymibrange-syntax.yaml"></a>

```
  [Max](#cfn-deadline-fleet-memorymibrange-max): {{Integer}}
  [Min](#cfn-deadline-fleet-memorymibrange-min): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-memorymibrange-properties"></a>

`Max`  <a name="cfn-deadline-fleet-memorymibrange-max"></a>
The maximum amount of memory (in MiB).
*Required*: No
*Type*: Integer
*Minimum*: `512`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-deadline-fleet-memorymibrange-min"></a>
The minimum amount of memory (in MiB).
*Required*: Yes
*Type*: Integer
*Minimum*: `512`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
