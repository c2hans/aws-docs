---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobqueue-jobstatetimelimitaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobQueue JobStateTimeLimitAction
<a name="aws-properties-batch-jobqueue-jobstatetimelimitaction"></a>

Specifies an action that AWS Batch will take after the job has remained at the head of the queue in the specified state for longer than the specified time.

## Syntax
<a name="aws-properties-batch-jobqueue-jobstatetimelimitaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobqueue-jobstatetimelimitaction-syntax.json"></a>

```
{
  "[Action](#cfn-batch-jobqueue-jobstatetimelimitaction-action)" : {{String}},
  "[MaxTimeSeconds](#cfn-batch-jobqueue-jobstatetimelimitaction-maxtimeseconds)" : {{Integer}},
  "[Reason](#cfn-batch-jobqueue-jobstatetimelimitaction-reason)" : {{String}},
  "[State](#cfn-batch-jobqueue-jobstatetimelimitaction-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobqueue-jobstatetimelimitaction-syntax.yaml"></a>

```
  [Action](#cfn-batch-jobqueue-jobstatetimelimitaction-action): {{String}}
  [MaxTimeSeconds](#cfn-batch-jobqueue-jobstatetimelimitaction-maxtimeseconds): {{Integer}}
  [Reason](#cfn-batch-jobqueue-jobstatetimelimitaction-reason): {{String}}
  [State](#cfn-batch-jobqueue-jobstatetimelimitaction-state): {{String}}
```

## Properties
<a name="aws-properties-batch-jobqueue-jobstatetimelimitaction-properties"></a>

`Action`  <a name="cfn-batch-jobqueue-jobstatetimelimitaction-action"></a>
The action to take when a job is at the head of the job queue in the specified state for the specified period of time. For job queues connected to a `ECS`, `FARGATE` or `EKS` compute environment, the only supported value is `CANCEL`, which will cancel the job. For job queues connected to a `SAGEMAKER_TRAINING` service environment, the only supported value is `TERMINATE`, which will terminate the job.
*Required*: Yes
*Type*: String
*Allowed values*: `CANCEL | TERMINATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTimeSeconds`  <a name="cfn-batch-jobqueue-jobstatetimelimitaction-maxtimeseconds"></a>
The approximate amount of time, in seconds, that must pass with the job in the specified state before the action is taken. The minimum value is 600 (10 minutes) and the maximum value is 86,400 (24 hours).
*Required*: Yes
*Type*: Integer
*Minimum*: `600`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Reason`  <a name="cfn-batch-jobqueue-jobstatetimelimitaction-reason"></a>
The reason to log for the action being taken.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-batch-jobqueue-jobstatetimelimitaction-state"></a>
The state of the job needed to trigger the action. The only supported value is `RUNNABLE`.
*Required*: Yes
*Type*: String
*Allowed values*: `RUNNABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
