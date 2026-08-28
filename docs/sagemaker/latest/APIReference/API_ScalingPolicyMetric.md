---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ScalingPolicyMetric.html
---

# ScalingPolicyMetric
<a name="API_ScalingPolicyMetric"></a>

The metric for a scaling policy.

## Contents
<a name="API_ScalingPolicyMetric_Contents"></a>

 ** InvocationsPerInstance **   <a name="sagemaker-Type-ScalingPolicyMetric-InvocationsPerInstance"></a>
The number of invocations sent to a model, normalized by `InstanceCount` in each ProductionVariant. `1/numberOfInstances` is sent as the value on each request, where `numberOfInstances` is the number of active instances for the ProductionVariant behind the endpoint at the time of the request.
Type: Integer
Required: No

 ** ModelLatency **   <a name="sagemaker-Type-ScalingPolicyMetric-ModelLatency"></a>
The interval of time taken by a model to respond as viewed from SageMaker. This interval includes the local communication times taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.
Type: Integer
Required: No

## See Also
<a name="API_ScalingPolicyMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ScalingPolicyMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ScalingPolicyMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ScalingPolicyMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
