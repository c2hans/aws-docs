---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointInput.html
---

# EndpointInput
<a name="API_EndpointInput"></a>

Input object for the endpoint

## Contents
<a name="API_EndpointInput_Contents"></a>

 ** EndpointName **   <a name="sagemaker-Type-EndpointInput-EndpointName"></a>
An endpoint in customer's account which has enabled `DataCaptureConfig` enabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** LocalPath **   <a name="sagemaker-Type-EndpointInput-LocalPath"></a>
Path to the filesystem where the endpoint data is available to the container.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** EndTimeOffset **   <a name="sagemaker-Type-EndpointInput-EndTimeOffset"></a>
If specified, monitoring jobs substract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `.?P.*`
Required: No

 ** ExcludeFeaturesAttribute **   <a name="sagemaker-Type-EndpointInput-ExcludeFeaturesAttribute"></a>
The attributes of the input data to exclude from the analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** FeaturesAttribute **   <a name="sagemaker-Type-EndpointInput-FeaturesAttribute"></a>
The attributes of the input data that are the input features.
Type: String
Required: No

 ** InferenceAttribute **   <a name="sagemaker-Type-EndpointInput-InferenceAttribute"></a>
The attribute of the input data that represents the ground truth label.
Type: String
Required: No

 ** ProbabilityAttribute **   <a name="sagemaker-Type-EndpointInput-ProbabilityAttribute"></a>
In a classification problem, the attribute that represents the class probability.
Type: String
Required: No

 ** ProbabilityThresholdAttribute **   <a name="sagemaker-Type-EndpointInput-ProbabilityThresholdAttribute"></a>
The threshold for the class probability to be evaluated as a positive result.
Type: Double
Required: No

 ** S3DataDistributionType **   <a name="sagemaker-Type-EndpointInput-S3DataDistributionType"></a>
Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`
Type: String
Valid Values: `FullyReplicated | ShardedByS3Key`
Required: No

 ** S3InputMode **   <a name="sagemaker-Type-EndpointInput-S3InputMode"></a>
Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File`.
Type: String
Valid Values: `Pipe | File`
Required: No

 ** StartTimeOffset **   <a name="sagemaker-Type-EndpointInput-StartTimeOffset"></a>
If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `.?P.*`
Required: No

## See Also
<a name="API_EndpointInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EndpointInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EndpointInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EndpointInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
