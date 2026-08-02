---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationMetrics.html
---

# RecommendationMetrics
<a name="API_RecommendationMetrics"></a>

The metrics of recommendations.

## Contents
<a name="API_RecommendationMetrics_Contents"></a>

 ** CostPerHour **   <a name="sagemaker-Type-RecommendationMetrics-CostPerHour"></a>
Defines the cost per hour for the instance.
Type: Float
Required: No

 ** CostPerInference **   <a name="sagemaker-Type-RecommendationMetrics-CostPerInference"></a>
Defines the cost per inference for the instance .
Type: Float
Required: No

 ** CpuUtilization **   <a name="sagemaker-Type-RecommendationMetrics-CpuUtilization"></a>
The expected CPU utilization at maximum invocations per minute for the instance.
 `NaN` indicates that the value is not available.
Type: Float
Valid Range: Minimum value of 0.0.
Required: No

 ** MaxInvocations **   <a name="sagemaker-Type-RecommendationMetrics-MaxInvocations"></a>
The expected maximum number of requests per minute for the instance.
Type: Integer
Required: No

 ** MemoryUtilization **   <a name="sagemaker-Type-RecommendationMetrics-MemoryUtilization"></a>
The expected memory utilization at maximum invocations per minute for the instance.
 `NaN` indicates that the value is not available.
Type: Float
Valid Range: Minimum value of 0.0.
Required: No

 ** ModelLatency **   <a name="sagemaker-Type-RecommendationMetrics-ModelLatency"></a>
The expected model latency at maximum invocation per minute for the instance.
Type: Integer
Required: No

 ** ModelSetupTime **   <a name="sagemaker-Type-RecommendationMetrics-ModelSetupTime"></a>
The time it takes to launch new compute resources for a serverless endpoint. The time can vary depending on the model size, how long it takes to download the model, and the start-up time of the container.
 `NaN` indicates that the value is not available.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RecommendationMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationMetrics)
