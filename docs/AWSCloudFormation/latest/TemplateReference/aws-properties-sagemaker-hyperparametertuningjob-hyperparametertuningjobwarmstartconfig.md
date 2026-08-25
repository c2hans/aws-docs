---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob HyperParameterTuningJobWarmStartConfig
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig"></a>

Specifies the configuration for a hyperparameter tuning job that uses one or more previous hyperparameter tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.

All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric, and the training job that performs the best is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.

**Note**
All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-syntax.json"></a>

```
{
  "[ParentHyperParameterTuningJobs](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-parenthyperparametertuningjobs)" : {{[ ParentHyperParameterTuningJobsItems, ... ]}},
  "[WarmStartType](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-warmstarttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-syntax.yaml"></a>

```
  [ParentHyperParameterTuningJobs](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-parenthyperparametertuningjobs): {{
    - ParentHyperParameterTuningJobsItems}}
  [WarmStartType](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-warmstarttype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-properties"></a>

`ParentHyperParameterTuningJobs`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-parenthyperparametertuningjobs"></a>
An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see [Using a Previous Hyperparameter Tuning Job as a Starting Point](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html).
Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.
*Required*: Yes
*Type*: Array of [ParentHyperParameterTuningJobsItems](aws-properties-sagemaker-hyperparametertuningjob-parenthyperparametertuningjobsitems.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WarmStartType`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig-warmstarttype"></a>
Specifies one of the following:
IDENTICAL\_DATA\_AND\_ALGORITHM
The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
TRANSFER\_LEARNING
The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
*Required*: Yes
*Type*: String
*Allowed values*: `IdenticalDataAndAlgorithm | TransferLearning`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
