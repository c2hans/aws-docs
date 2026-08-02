---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationOptimizationDetail.html
---

# AIRecommendationOptimizationDetail
<a name="API_AIRecommendationOptimizationDetail"></a>

Details about an optimization technique applied in a recommendation.

## Contents
<a name="API_AIRecommendationOptimizationDetail_Contents"></a>

 ** OptimizationType **   <a name="sagemaker-Type-AIRecommendationOptimizationDetail-OptimizationType"></a>
The type of optimization. Valid values are `SpeculativeDecoding` and `KernelTuning`.
Type: String
Valid Values: `SpeculativeDecoding | KernelTuning`
Required: Yes

 ** OptimizationConfig **   <a name="sagemaker-Type-AIRecommendationOptimizationDetail-OptimizationConfig"></a>
A map of configuration parameters for the optimization technique.
Type: String to string map
Required: No

## See Also
<a name="API_AIRecommendationOptimizationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationOptimizationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationOptimizationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationOptimizationDetail)
