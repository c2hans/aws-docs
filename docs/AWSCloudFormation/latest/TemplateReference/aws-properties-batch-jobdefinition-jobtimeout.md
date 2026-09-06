---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-jobtimeout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition JobTimeout
<a name="aws-properties-batch-jobdefinition-jobtimeout"></a>

An object that represents a job timeout configuration.

## Syntax
<a name="aws-properties-batch-jobdefinition-jobtimeout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-jobtimeout-syntax.json"></a>

```
{
  "[AttemptDurationSeconds](#cfn-batch-jobdefinition-jobtimeout-attemptdurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-jobtimeout-syntax.yaml"></a>

```
  [AttemptDurationSeconds](#cfn-batch-jobdefinition-jobtimeout-attemptdurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-jobtimeout-properties"></a>

`AttemptDurationSeconds`  <a name="cfn-batch-jobdefinition-jobtimeout-attemptdurationseconds"></a>
The job timeout time (in seconds) that's measured from the job attempt's `startedAt` timestamp. After this time passes, AWS Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds.
For array jobs, the timeout applies to the child jobs, not to the parent array job.
For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
