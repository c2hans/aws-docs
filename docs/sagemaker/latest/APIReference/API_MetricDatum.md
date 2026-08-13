---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDatum.html
---

# MetricDatum
<a name="API_MetricDatum"></a>

Information about the metric for a candidate produced by an AutoML job.

## Contents
<a name="API_MetricDatum_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-MetricDatum-MetricName"></a>
The name of the metric.
Type: String
Valid Values: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | BalancedAccuracy | R2 | Recall | RecallMacro | Precision | PrecisionMacro | MAE | MAPE | MASE | WAPE | AverageWeightedQuantileLoss`
Required: No

 ** Set **   <a name="sagemaker-Type-MetricDatum-Set"></a>
The dataset split from which the AutoML job produced the metric.
Type: String
Valid Values: `Train | Validation | Test`
Required: No

 ** StandardMetricName **   <a name="sagemaker-Type-MetricDatum-StandardMetricName"></a>
The name of the standard metric.
For definitions of the standard metrics, see [`Autopilot candidate metrics`](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-metrics).
Type: String
Valid Values: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | MAE | R2 | BalancedAccuracy | Precision | PrecisionMacro | Recall | RecallMacro | LogLoss | InferenceLatency | MAPE | MASE | WAPE | AverageWeightedQuantileLoss | Rouge1 | Rouge2 | RougeL | RougeLSum | Perplexity | ValidationLoss | TrainingLoss`
Required: No

 ** Value **   <a name="sagemaker-Type-MetricDatum-Value"></a>
The value of the metric.
Type: Float
Required: No

## See Also
<a name="API_MetricDatum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricDatum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricDatum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricDatum)
