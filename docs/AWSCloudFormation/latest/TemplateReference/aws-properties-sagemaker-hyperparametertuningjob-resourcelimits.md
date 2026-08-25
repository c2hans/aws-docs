---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-resourcelimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob ResourceLimits
<a name="aws-properties-sagemaker-hyperparametertuningjob-resourcelimits"></a>

Specifies the maximum number of training jobs and parallel training jobs that a hyperparameter tuning job can launch.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-resourcelimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-resourcelimits-syntax.json"></a>

```
{
  "[MaxNumberOfTrainingJobs](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxnumberoftrainingjobs)" : {{Integer}},
  "[MaxParallelTrainingJobs](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxparalleltrainingjobs)" : {{Integer}},
  "[MaxRuntimeInSeconds](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxruntimeinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-resourcelimits-syntax.yaml"></a>

```
  [MaxNumberOfTrainingJobs](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxnumberoftrainingjobs): {{Integer}}
  [MaxParallelTrainingJobs](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxparalleltrainingjobs): {{Integer}}
  [MaxRuntimeInSeconds](#cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxruntimeinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-resourcelimits-properties"></a>

`MaxNumberOfTrainingJobs`  <a name="cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxnumberoftrainingjobs"></a>
The maximum number of training jobs that a hyperparameter tuning job can launch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxParallelTrainingJobs`  <a name="cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxparalleltrainingjobs"></a>
The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxRuntimeInSeconds`  <a name="cfn-sagemaker-hyperparametertuningjob-resourcelimits-maxruntimeinseconds"></a>
The maximum time in seconds that a hyperparameter tuning job can run.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `15768000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
