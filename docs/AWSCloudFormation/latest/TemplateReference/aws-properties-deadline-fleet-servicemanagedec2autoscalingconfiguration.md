---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet ServiceManagedEc2AutoScalingConfiguration
<a name="aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration"></a>

The auto scaling configuration settings for a service managed EC2 fleet.

## Syntax
<a name="aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration-syntax.json"></a>

```
{
  "[ScaleOutWorkersPerMinute](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-scaleoutworkersperminute)" : {{Integer}},
  "[StandbyWorkerCount](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-standbyworkercount)" : {{Integer}},
  "[WorkerIdleDurationSeconds](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-workeridledurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration-syntax.yaml"></a>

```
  [ScaleOutWorkersPerMinute](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-scaleoutworkersperminute): {{Integer}}
  [StandbyWorkerCount](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-standbyworkercount): {{Integer}}
  [WorkerIdleDurationSeconds](#cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-workeridledurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-servicemanagedec2autoscalingconfiguration-properties"></a>

`ScaleOutWorkersPerMinute`  <a name="cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-scaleoutworkersperminute"></a>
The number of workers that can be added per minute to the fleet. The default is 10 workers per minute.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StandbyWorkerCount`  <a name="cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-standbyworkercount"></a>
The number of idle workers maintained and ready to process incoming tasks. The default is 0.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerIdleDurationSeconds`  <a name="cfn-deadline-fleet-servicemanagedec2autoscalingconfiguration-workeridledurationseconds"></a>
The number of seconds that a worker can remain idle before it is shut down. The default is 300 seconds (5 minutes).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
