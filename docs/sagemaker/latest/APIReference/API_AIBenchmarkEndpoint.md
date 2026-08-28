---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIBenchmarkEndpoint.html
---

# AIBenchmarkEndpoint
<a name="API_AIBenchmarkEndpoint"></a>

The SageMaker endpoint configuration for benchmarking.

## Contents
<a name="API_AIBenchmarkEndpoint_Contents"></a>

 ** Identifier **   <a name="sagemaker-Type-AIBenchmarkEndpoint-Identifier"></a>
The name or Amazon Resource Name (ARN) of the SageMaker endpoint to benchmark.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`
Required: Yes

 ** InferenceComponents **   <a name="sagemaker-Type-AIBenchmarkEndpoint-InferenceComponents"></a>
The list of inference components to benchmark on the endpoint.
Type: Array of [AIBenchmarkInferenceComponent](API_AIBenchmarkInferenceComponent.md) objects
Required: No

 ** TargetContainerHostname **   <a name="sagemaker-Type-AIBenchmarkEndpoint-TargetContainerHostname"></a>
The hostname of the specific container to target within a multi-container endpoint.
Type: String
Required: No

## See Also
<a name="API_AIBenchmarkEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIBenchmarkEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIBenchmarkEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIBenchmarkEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
