---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIBenchmarkOutputResult.html
---

# AIBenchmarkOutputResult
<a name="API_AIBenchmarkOutputResult"></a>

The output result of an AI benchmark job, including the Amazon S3 location and CloudWatch log information.

## Contents
<a name="API_AIBenchmarkOutputResult_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-AIBenchmarkOutputResult-S3OutputLocation"></a>
The Amazon S3 URI where benchmark results are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** CloudWatchLogs **   <a name="sagemaker-Type-AIBenchmarkOutputResult-CloudWatchLogs"></a>
The CloudWatch log information for the benchmark job.
Type: Array of [AICloudWatchLogs](API_AICloudWatchLogs.md) objects
Required: No

 ** MlflowConfig **   <a name="sagemaker-Type-AIBenchmarkOutputResult-MlflowConfig"></a>
The MLflow tracking configuration for the job.
Type: [AIMlflowConfig](API_AIMlflowConfig.md) object
Required: No

## See Also
<a name="API_AIBenchmarkOutputResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIBenchmarkOutputResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIBenchmarkOutputResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIBenchmarkOutputResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
