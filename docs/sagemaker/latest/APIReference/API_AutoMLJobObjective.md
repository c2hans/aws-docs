---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html
---

# AutoMLJobObjective
<a name="API_AutoMLJobObjective"></a>

Specifies a metric to minimize or maximize as the objective of an AutoML job.

## Contents
<a name="API_AutoMLJobObjective_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-AutoMLJobObjective-MetricName"></a>
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
Type: String
Valid Values: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | BalancedAccuracy | R2 | Recall | RecallMacro | Precision | PrecisionMacro | MAE | MAPE | MASE | WAPE | AverageWeightedQuantileLoss`
Required: Yes

## See Also
<a name="API_AutoMLJobObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLJobObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLJobObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLJobObjective)
