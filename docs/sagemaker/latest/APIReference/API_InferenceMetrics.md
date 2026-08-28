---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceMetrics.html
---

# InferenceMetrics
<a name="API_InferenceMetrics"></a>

The metrics for an existing endpoint compared in an Inference Recommender job.

## Contents
<a name="API_InferenceMetrics_Contents"></a>

 ** MaxInvocations **   <a name="sagemaker-Type-InferenceMetrics-MaxInvocations"></a>
The expected maximum number of requests per minute for the instance.
Type: Integer
Required: Yes

 ** ModelLatency **   <a name="sagemaker-Type-InferenceMetrics-ModelLatency"></a>
The expected model latency at maximum invocations per minute for the instance.
Type: Integer
Required: Yes

## See Also
<a name="API_InferenceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
