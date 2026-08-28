---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalHyperParameterTuningJobObjectiveMetric.html
---

# FinalHyperParameterTuningJobObjectiveMetric
<a name="API_FinalHyperParameterTuningJobObjectiveMetric"></a>

Shows the latest objective metric emitted by a training job that was launched by a hyperparameter tuning job. You define the objective metric in the `HyperParameterTuningJobObjective` parameter of [HyperParameterTuningJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html).

## Contents
<a name="API_FinalHyperParameterTuningJobObjectiveMetric_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-FinalHyperParameterTuningJobObjectiveMetric-MetricName"></a>
The name of the objective metric. For SageMaker built-in algorithms, metrics are defined per algorithm. See the [metrics for XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html) as an example. You can also use a custom algorithm for training and define your own metrics. For more information, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Value **   <a name="sagemaker-Type-FinalHyperParameterTuningJobObjectiveMetric-Value"></a>
The value of the objective metric.
Type: Float
Required: Yes

 ** Type **   <a name="sagemaker-Type-FinalHyperParameterTuningJobObjectiveMetric-Type"></a>
Select if you want to minimize or maximize the objective metric during hyperparameter tuning.
Type: String
Valid Values: `Maximize | Minimize`
Required: No

## See Also
<a name="API_FinalHyperParameterTuningJobObjectiveMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FinalHyperParameterTuningJobObjectiveMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FinalHyperParameterTuningJobObjectiveMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FinalHyperParameterTuningJobObjectiveMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
