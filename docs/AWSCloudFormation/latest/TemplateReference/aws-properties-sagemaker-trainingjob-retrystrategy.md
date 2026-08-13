---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-retrystrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob RetryStrategy
<a name="aws-properties-sagemaker-trainingjob-retrystrategy"></a>

The retry strategy to use when a training job fails due to an `InternalServerError`. `RetryStrategy` is specified as part of the `CreateTrainingJob` and `CreateHyperParameterTuningJob` requests. You can add the `StoppingCondition` parameter to the request to limit the training time for the complete job.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-retrystrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-retrystrategy-syntax.json"></a>

```
{
  "[MaximumRetryAttempts](#cfn-sagemaker-trainingjob-retrystrategy-maximumretryattempts)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-retrystrategy-syntax.yaml"></a>

```
  [MaximumRetryAttempts](#cfn-sagemaker-trainingjob-retrystrategy-maximumretryattempts): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-retrystrategy-properties"></a>

`MaximumRetryAttempts`  <a name="cfn-sagemaker-trainingjob-retrystrategy-maximumretryattempts"></a>
The number of times to retry the job. When the job is retried, it's `SecondaryStatus` is changed to `STARTING`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
