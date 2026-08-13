---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automljobobjective.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLJobObjective
<a name="aws-properties-sagemaker-automljob-automljobobjective"></a>

Specifies a metric to minimize or maximize as the objective of an AutoML job.

## Syntax
<a name="aws-properties-sagemaker-automljob-automljobobjective-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automljobobjective-syntax.json"></a>

```
{
  "[MetricName](#cfn-sagemaker-automljob-automljobobjective-metricname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automljobobjective-syntax.yaml"></a>

```
  [MetricName](#cfn-sagemaker-automljob-automljobobjective-metricname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automljobobjective-properties"></a>

`MetricName`  <a name="cfn-sagemaker-automljob-automljobobjective-metricname"></a>
The name of the objective metric used to measure the predictive quality of a machine learning system. During training, the model's parameters are updated iteratively to optimize its performance based on the feedback provided by the objective metric when evaluating the model on the validation dataset.
The list of available metrics supported by Autopilot and the default metric applied when you do not specify a metric name explicitly depend on the problem type.
+ For tabular problem types:
  + List of available metrics:
    +  Regression: `MAE`, `MSE`, `R2`, `RMSE`
    +  Binary classification: `Accuracy`, `AUC`, `BalancedAccuracy`, `F1`, `Precision`, `Recall`
    +  Multiclass classification: `Accuracy`, `BalancedAccuracy`, `F1macro`, `PrecisionMacro`, `RecallMacro`

    For a description of each metric, see [Autopilot metrics for classification and regression](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics).
  + Default objective metrics:
    + Regression: `MSE`.
    + Binary classification: `F1`.
    + Multiclass classification: `Accuracy`.
+ For image or text classification problem types:
  + List of available metrics: `Accuracy`

    For a description of each metric, see [Autopilot metrics for text and image classification](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-data-format-and-metric.html).
  + Default objective metrics: `Accuracy`
+ For time-series forecasting problem types:
  + List of available metrics: `RMSE`, `wQL`, `Average wQL`, `MASE`, `MAPE`, `WAPE`

    For a description of each metric, see [Autopilot metrics for time-series forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-objective-metric.html).
  + Default objective metrics: `AverageWeightedQuantileLoss`
+ For text generation problem types (LLMs fine-tuning): Fine-tuning language models in Autopilot does not require setting the `AutoMLJobObjective` field. Autopilot fine-tunes LLMs without requiring multiple candidates to be trained and evaluated. Instead, using your dataset, Autopilot directly fine-tunes your target model to enhance a default objective metric, the cross-entropy loss. After fine-tuning a language model, you can evaluate the quality of its generated text using different metrics. For a list of the available metrics, see [Metrics for fine-tuning LLMs in Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html).
*Required*: Yes
*Type*: String
*Allowed values*: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | BalancedAccuracy | R2 | Recall | RecallMacro | Precision | PrecisionMacro | MAE | MAPE | MASE | WAPE | AverageWeightedQuantileLoss`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
