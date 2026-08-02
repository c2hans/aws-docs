---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm HyperParameterTuningJobObjective
<a name="aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective"></a>

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).

## Syntax
<a name="aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective-syntax.json"></a>

```
{
  "[MetricName](#cfn-sagemaker-algorithm-hyperparametertuningjobobjective-metricname)" : {{String}},
  "[Type](#cfn-sagemaker-algorithm-hyperparametertuningjobobjective-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective-syntax.yaml"></a>

```
  [MetricName](#cfn-sagemaker-algorithm-hyperparametertuningjobobjective-metricname): {{String}}
  [Type](#cfn-sagemaker-algorithm-hyperparametertuningjobobjective-type): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-hyperparametertuningjobobjective-properties"></a>

`MetricName`  <a name="cfn-sagemaker-algorithm-hyperparametertuningjobobjective-metricname"></a>
The name of the metric to use for the objective metric.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-sagemaker-algorithm-hyperparametertuningjobobjective-type"></a>
Whether to minimize or maximize the objective metric.
*Required*: Yes
*Type*: String
*Allowed values*: `Maximize | Minimize`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
