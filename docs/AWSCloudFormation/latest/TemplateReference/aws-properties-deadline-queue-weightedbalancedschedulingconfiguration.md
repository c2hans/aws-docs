---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-weightedbalancedschedulingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue WeightedBalancedSchedulingConfiguration
<a name="aws-properties-deadline-queue-weightedbalancedschedulingconfiguration"></a>

Configuration for weighted balanced scheduling. Workers are assigned to jobs based on a weighted formula:

 `weight = (priority * priorityWeight) + (errors * errorWeight) + ((currentTime - submissionTime) * submissionTimeWeight) + ((renderingTasks - renderingTaskBuffer) * renderingTaskWeight)`

The job with the highest calculated weight is scheduled first. Workers are distributed evenly amongst jobs with the same weight.

## Syntax
<a name="aws-properties-deadline-queue-weightedbalancedschedulingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-weightedbalancedschedulingconfiguration-syntax.json"></a>

```
{
  "[ErrorWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-errorweight)" : {{Number}},
  "[MaxPriorityOverride](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-maxpriorityoverride)" : {{SchedulingMaxPriorityOverride}},
  "[MinPriorityOverride](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-minpriorityoverride)" : {{SchedulingMinPriorityOverride}},
  "[PriorityWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-priorityweight)" : {{Number}},
  "[RenderingTaskBuffer](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskbuffer)" : {{Integer}},
  "[RenderingTaskWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskweight)" : {{Number}},
  "[SubmissionTimeWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-submissiontimeweight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-deadline-queue-weightedbalancedschedulingconfiguration-syntax.yaml"></a>

```
  [ErrorWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-errorweight): {{Number}}
  [MaxPriorityOverride](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-maxpriorityoverride): {{
    SchedulingMaxPriorityOverride}}
  [MinPriorityOverride](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-minpriorityoverride): {{
    SchedulingMinPriorityOverride}}
  [PriorityWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-priorityweight): {{Number}}
  [RenderingTaskBuffer](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskbuffer): {{Integer}}
  [RenderingTaskWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskweight): {{Number}}
  [SubmissionTimeWeight](#cfn-deadline-queue-weightedbalancedschedulingconfiguration-submissiontimeweight): {{Number}}
```

## Properties
<a name="aws-properties-deadline-queue-weightedbalancedschedulingconfiguration-properties"></a>

`ErrorWeight`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-errorweight"></a>
The weight applied to the number of errors on a job. A negative value means jobs without errors are scheduled first. A value of `0` means errors are ignored. The default value is `-10.0`.
*Required*: No
*Type*: Number
*Minimum*: `-10000`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxPriorityOverride`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-maxpriorityoverride"></a>
Overrides the weighted scheduling formula for jobs at the maximum priority (100). When set, jobs with priority 100 are always scheduled first regardless of their calculated weight. When absent, maximum priority jobs use the standard weighted formula.
*Required*: No
*Type*: [SchedulingMaxPriorityOverride](aws-properties-deadline-queue-schedulingmaxpriorityoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinPriorityOverride`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-minpriorityoverride"></a>
Overrides the weighted scheduling formula for jobs at the minimum priority (0). When set, jobs with priority 0 are always scheduled last regardless of their calculated weight. When absent, minimum priority jobs use the standard weighted formula.
*Required*: No
*Type*: [SchedulingMinPriorityOverride](aws-properties-deadline-queue-schedulingminpriorityoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PriorityWeight`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-priorityweight"></a>
The weight applied to job priority in the scheduling formula. Higher values give more influence to job priority. A value of `0` means priority is ignored. The default value is `100.0`.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenderingTaskBuffer`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskbuffer"></a>
The rendering task buffer is subtracted from the number of rendering tasks before applying the rendering task weight. This creates a stickiness effect where workers prefer to stay with their current job. Higher values make workers stickier. The default value is `1`. The buffer is only applied in the weight calculation for a job if the worker is currently assigned to that job.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenderingTaskWeight`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-renderingtaskweight"></a>
The weight applied to the number of tasks currently rendering on a job. A negative value means jobs that are not already rendering are scheduled next. A value of `0` means the rendering state is ignored. The default value is `-100.0`.
*Required*: No
*Type*: Number
*Minimum*: `-10000`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubmissionTimeWeight`  <a name="cfn-deadline-queue-weightedbalancedschedulingconfiguration-submissiontimeweight"></a>
The weight applied to job submission time. A positive value means earlier jobs are scheduled first. A value of `0` means submission time is ignored. The default value is `3.0`.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
