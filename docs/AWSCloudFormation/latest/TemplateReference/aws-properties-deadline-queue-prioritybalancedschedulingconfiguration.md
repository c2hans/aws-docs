---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-prioritybalancedschedulingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue PriorityBalancedSchedulingConfiguration
<a name="aws-properties-deadline-queue-prioritybalancedschedulingconfiguration"></a>

Configuration for priority balanced scheduling. Workers are distributed evenly across all jobs at the highest priority level.

## Syntax
<a name="aws-properties-deadline-queue-prioritybalancedschedulingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-prioritybalancedschedulingconfiguration-syntax.json"></a>

```
{
  "[RenderingTaskBuffer](#cfn-deadline-queue-prioritybalancedschedulingconfiguration-renderingtaskbuffer)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-queue-prioritybalancedschedulingconfiguration-syntax.yaml"></a>

```
  [RenderingTaskBuffer](#cfn-deadline-queue-prioritybalancedschedulingconfiguration-renderingtaskbuffer): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-queue-prioritybalancedschedulingconfiguration-properties"></a>

`RenderingTaskBuffer`  <a name="cfn-deadline-queue-prioritybalancedschedulingconfiguration-renderingtaskbuffer"></a>
The rendering task buffer controls worker stickiness. A worker only switches from its current job to another job at the same priority if the other job has fewer rendering tasks by more than this buffer value. Higher values make workers stickier to their current jobs. The default value is `1`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
