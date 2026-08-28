---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-schedulingminpriorityoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue SchedulingMinPriorityOverride
<a name="aws-properties-deadline-queue-schedulingminpriorityoverride"></a>

Defines the override behavior for jobs at the minimum priority (0) in weighted balanced scheduling.

## Syntax
<a name="aws-properties-deadline-queue-schedulingminpriorityoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-schedulingminpriorityoverride-syntax.json"></a>

```
{
  "[AlwaysScheduleLast](#cfn-deadline-queue-schedulingminpriorityoverride-alwaysschedulelast)" : {{Json}}
}
```

### YAML
<a name="aws-properties-deadline-queue-schedulingminpriorityoverride-syntax.yaml"></a>

```
  [AlwaysScheduleLast](#cfn-deadline-queue-schedulingminpriorityoverride-alwaysschedulelast): {{Json}}
```

## Properties
<a name="aws-properties-deadline-queue-schedulingminpriorityoverride-properties"></a>

`AlwaysScheduleLast`  <a name="cfn-deadline-queue-schedulingminpriorityoverride-alwaysschedulelast"></a>
Jobs at the minimum priority (0) are always scheduled after all other jobs, regardless of the weighted scheduling formula. If multiple jobs have priority 0, ties are broken using the standard weighted formula.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
