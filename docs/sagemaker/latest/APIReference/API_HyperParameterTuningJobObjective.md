---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html
---

# HyperParameterTuningJobObjective
<a name="API_HyperParameterTuningJobObjective"></a>

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).

## Contents
<a name="API_HyperParameterTuningJobObjective_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-HyperParameterTuningJobObjective-MetricName"></a>
The name of the metric to use for the objective metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Type **   <a name="sagemaker-Type-HyperParameterTuningJobObjective-Type"></a>
Whether to minimize or maximize the objective metric.
Type: String
Valid Values: `Maximize | Minimize`
Required: Yes

## See Also
<a name="API_HyperParameterTuningJobObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobObjective)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
