---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-schedulingmaxpriorityoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue SchedulingMaxPriorityOverride
<a name="aws-properties-deadline-queue-schedulingmaxpriorityoverride"></a>

Defines the override behavior for jobs at the maximum priority (100) in weighted balanced scheduling.

## Syntax
<a name="aws-properties-deadline-queue-schedulingmaxpriorityoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-schedulingmaxpriorityoverride-syntax.json"></a>

```
{
  "[AlwaysScheduleFirst](#cfn-deadline-queue-schedulingmaxpriorityoverride-alwaysschedulefirst)" : {{Json}}
}
```

### YAML
<a name="aws-properties-deadline-queue-schedulingmaxpriorityoverride-syntax.yaml"></a>

```
  [AlwaysScheduleFirst](#cfn-deadline-queue-schedulingmaxpriorityoverride-alwaysschedulefirst): {{Json}}
```

## Properties
<a name="aws-properties-deadline-queue-schedulingmaxpriorityoverride-properties"></a>

`AlwaysScheduleFirst`  <a name="cfn-deadline-queue-schedulingmaxpriorityoverride-alwaysschedulefirst"></a>
Jobs at the maximum priority (100) are always scheduled before other jobs, regardless of the weighted scheduling formula. If multiple jobs have priority 100, ties are broken using the standard weighted formula.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
