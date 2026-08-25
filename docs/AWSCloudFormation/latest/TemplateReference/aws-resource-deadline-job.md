---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-job.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Job
<a name="aws-resource-deadline-job"></a>

Creates a job. A job is a set of instructions that Deadline Cloud uses to schedule and run work on available workers. For more information, see [Deadline Cloud jobs](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-jobs.html).

## Syntax
<a name="aws-resource-deadline-job-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-job-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Job",
  "Properties" : {
      "[FarmId](#cfn-deadline-job-farmid)" : {{String}},
      "[MaxFailedTasksCount](#cfn-deadline-job-maxfailedtaskscount)" : {{Integer}},
      "[MaxRetriesPerTask](#cfn-deadline-job-maxretriespertask)" : {{Integer}},
      "[MaxWorkerCount](#cfn-deadline-job-maxworkercount)" : {{Integer}},
      "[Priority](#cfn-deadline-job-priority)" : {{Integer}},
      "[QueueId](#cfn-deadline-job-queueid)" : {{String}},
      "[Tags](#cfn-deadline-job-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-job-syntax.yaml"></a>

```
Type: AWS::Deadline::Job
Properties:
  [FarmId](#cfn-deadline-job-farmid): {{String}}
  [MaxFailedTasksCount](#cfn-deadline-job-maxfailedtaskscount): {{Integer}}
  [MaxRetriesPerTask](#cfn-deadline-job-maxretriespertask): {{Integer}}
  [MaxWorkerCount](#cfn-deadline-job-maxworkercount): {{Integer}}
  [Priority](#cfn-deadline-job-priority): {{Integer}}
  [QueueId](#cfn-deadline-job-queueid): {{String}}
  [Tags](#cfn-deadline-job-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-deadline-job-properties"></a>

`FarmId`  <a name="cfn-deadline-job-farmid"></a>
The farm ID of the job.
*Required*: No
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxFailedTasksCount`  <a name="cfn-deadline-job-maxfailedtaskscount"></a>
The number of task failures before the job stops running and is marked as `FAILED`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxRetriesPerTask`  <a name="cfn-deadline-job-maxretriespertask"></a>
The maximum number of retries per failed tasks.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxWorkerCount`  <a name="cfn-deadline-job-maxworkercount"></a>
The maximum number of worker hosts that can concurrently process a job.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-deadline-job-priority"></a>
The job priority.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueueId`  <a name="cfn-deadline-job-queueid"></a>
The queue ID of the job.
*Required*: No
*Type*: String
*Pattern*: `^queue-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-deadline-job-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-job-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-job-return-values"></a>

### Ref
<a name="aws-resource-deadline-job-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-deadline-job-return-values-fn--getatt"></a>

####
<a name="aws-resource-deadline-job-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the resource was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user or system that created this resource.

`JobId`  <a name="JobId-fn::getatt"></a>
The job ID.

`LifecycleStatus`  <a name="LifecycleStatus-fn::getatt"></a>
The life cycle status of the job.

`LifecycleStatusMessage`  <a name="LifecycleStatusMessage-fn::getatt"></a>
A message that communicates the status of the life cycle.

`Name`  <a name="Name-fn::getatt"></a>
The name of the job.

`TaskRunStatus`  <a name="TaskRunStatus-fn::getatt"></a>
The task run status for the job.
