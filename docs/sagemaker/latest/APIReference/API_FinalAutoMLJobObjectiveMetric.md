---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalAutoMLJobObjectiveMetric.html
---

# FinalAutoMLJobObjectiveMetric
<a name="API_FinalAutoMLJobObjectiveMetric"></a>

The best candidate result from an AutoML training job.

## Contents
<a name="API_FinalAutoMLJobObjectiveMetric_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-FinalAutoMLJobObjectiveMetric-MetricName"></a>
The name of the metric with the best result. For a description of the possible objective metrics, see [AutoMLJobObjective$MetricName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html).
Type: String
Valid Values: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | BalancedAccuracy | R2 | Recall | RecallMacro | Precision | PrecisionMacro | MAE | MAPE | MASE | WAPE | AverageWeightedQuantileLoss`
Required: Yes

 ** Value **   <a name="sagemaker-Type-FinalAutoMLJobObjectiveMetric-Value"></a>
The value of the metric with the best result.
Type: Float
Required: Yes

 ** StandardMetricName **   <a name="sagemaker-Type-FinalAutoMLJobObjectiveMetric-StandardMetricName"></a>
The name of the standard metric. For a description of the standard metrics, see [Autopilot candidate metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics).
Type: String
Valid Values: `Accuracy | MSE | F1 | F1macro | AUC | RMSE | BalancedAccuracy | R2 | Recall | RecallMacro | Precision | PrecisionMacro | MAE | MAPE | MASE | WAPE | AverageWeightedQuantileLoss`
Required: No

 ** Type **   <a name="sagemaker-Type-FinalAutoMLJobObjectiveMetric-Type"></a>
The type of metric with the best result.
Type: String
Valid Values: `Maximize | Minimize`
Required: No

## See Also
<a name="API_FinalAutoMLJobObjectiveMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FinalAutoMLJobObjectiveMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FinalAutoMLJobObjectiveMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FinalAutoMLJobObjectiveMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
