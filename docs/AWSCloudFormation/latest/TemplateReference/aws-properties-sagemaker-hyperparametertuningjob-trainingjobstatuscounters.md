---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob TrainingJobStatusCounters
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters"></a>

The numbers of training jobs launched by a hyperparameter tuning job, categorized by status.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-syntax.json"></a>

```
{
  "[Completed](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-completed)" : {{Integer}},
  "[InProgress](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-inprogress)" : {{Integer}},
  "[NonRetryableError](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-nonretryableerror)" : {{Integer}},
  "[RetryableError](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-retryableerror)" : {{Integer}},
  "[Stopped](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-stopped)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-syntax.yaml"></a>

```
  [Completed](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-completed): {{Integer}}
  [InProgress](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-inprogress): {{Integer}}
  [NonRetryableError](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-nonretryableerror): {{Integer}}
  [RetryableError](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-retryableerror): {{Integer}}
  [Stopped](#cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-stopped): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-properties"></a>

`Completed`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-completed"></a>
The number of completed training jobs launched by the hyperparameter tuning job.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InProgress`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-inprogress"></a>
The number of in-progress training jobs launched by a hyperparameter tuning job.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NonRetryableError`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-nonretryableerror"></a>
The number of training jobs that failed and can't be retried. A failed training job can't be retried if it failed because a client error occurred.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryableError`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-retryableerror"></a>
The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stopped`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobstatuscounters-stopped"></a>
The number of training jobs launched by a hyperparameter tuning job that were manually stopped.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
