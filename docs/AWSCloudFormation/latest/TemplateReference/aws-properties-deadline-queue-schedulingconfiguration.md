---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-schedulingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue SchedulingConfiguration
<a name="aws-properties-deadline-queue-schedulingconfiguration"></a>

The scheduling configuration for a queue. Defines the strategy used to assign workers to jobs.

## Syntax
<a name="aws-properties-deadline-queue-schedulingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-schedulingconfiguration-syntax.json"></a>

```
{
  "[PriorityBalanced](#cfn-deadline-queue-schedulingconfiguration-prioritybalanced)" : {{PriorityBalancedSchedulingConfiguration}},
  "[PriorityFifo](#cfn-deadline-queue-schedulingconfiguration-priorityfifo)" : {{Json}},
  "[WeightedBalanced](#cfn-deadline-queue-schedulingconfiguration-weightedbalanced)" : {{WeightedBalancedSchedulingConfiguration}}
}
```

### YAML
<a name="aws-properties-deadline-queue-schedulingconfiguration-syntax.yaml"></a>

```
  [PriorityBalanced](#cfn-deadline-queue-schedulingconfiguration-prioritybalanced): {{
    PriorityBalancedSchedulingConfiguration}}
  [PriorityFifo](#cfn-deadline-queue-schedulingconfiguration-priorityfifo): {{Json}}
  [WeightedBalanced](#cfn-deadline-queue-schedulingconfiguration-weightedbalanced): {{
    WeightedBalancedSchedulingConfiguration}}
```

## Properties
<a name="aws-properties-deadline-queue-schedulingconfiguration-properties"></a>

`PriorityBalanced`  <a name="cfn-deadline-queue-schedulingconfiguration-prioritybalanced"></a>
Workers are distributed evenly across all jobs at the highest priority level. When workers cannot be evenly divided, the extra workers are assigned to the jobs submitted earliest. If a job has fewer remaining tasks than its share of workers, the surplus workers are redistributed to other jobs at the same priority level.
*Required*: No
*Type*: [PriorityBalancedSchedulingConfiguration](aws-properties-deadline-queue-prioritybalancedschedulingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PriorityFifo`  <a name="cfn-deadline-queue-schedulingconfiguration-priorityfifo"></a>
Workers are assigned to the highest-priority job first. When multiple jobs share the same priority, the job submitted earliest receives workers first. This is the default scheduling configuration for new queues.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightedBalanced`  <a name="cfn-deadline-queue-schedulingconfiguration-weightedbalanced"></a>
Workers are assigned to jobs based on a weighted formula that considers job priority, error count, submission time, and the number of tasks currently rendering. Each factor has a configurable weight that determines its influence on scheduling decisions.
*Required*: No
*Type*: [WeightedBalancedSchedulingConfiguration](aws-properties-deadline-queue-weightedbalancedschedulingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
