---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobStoppingConditions.html
---

# RecommendationJobStoppingConditions
<a name="API_RecommendationJobStoppingConditions"></a>

Specifies conditions for stopping a job. When a job reaches a stopping condition limit, SageMaker ends the job.

## Contents
<a name="API_RecommendationJobStoppingConditions_Contents"></a>

 ** FlatInvocations **   <a name="sagemaker-Type-RecommendationJobStoppingConditions-FlatInvocations"></a>
Stops a load test when the number of invocations (TPS) peaks and flattens, which means that the instance has reached capacity. The default value is `Stop`. If you want the load test to continue after invocations have flattened, set the value to `Continue`.
Type: String
Valid Values: `Continue | Stop`
Required: No

 ** MaxInvocations **   <a name="sagemaker-Type-RecommendationJobStoppingConditions-MaxInvocations"></a>
The maximum number of requests per minute expected for the endpoint.
Type: Integer
Required: No

 ** ModelLatencyThresholds **   <a name="sagemaker-Type-RecommendationJobStoppingConditions-ModelLatencyThresholds"></a>
The interval of time taken by a model to respond as viewed from SageMaker. The interval includes the local communication time taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.
Type: Array of [ModelLatencyThreshold](API_ModelLatencyThreshold.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_RecommendationJobStoppingConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobStoppingConditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobStoppingConditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobStoppingConditions)
