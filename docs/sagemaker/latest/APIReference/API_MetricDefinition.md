---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html
---

# MetricDefinition
<a name="API_MetricDefinition"></a>

Specifies a metric that the training algorithm writes to `stderr` or `stdout`. You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

## Contents
<a name="API_MetricDefinition_Contents"></a>

 ** Name **   <a name="sagemaker-Type-MetricDefinition-Name"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Regex **   <a name="sagemaker-Type-MetricDefinition-Regex"></a>
A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.+`
Required: Yes

## See Also
<a name="API_MetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricDefinition)
