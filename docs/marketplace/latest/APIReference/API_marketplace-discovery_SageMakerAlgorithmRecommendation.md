---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SageMakerAlgorithmRecommendation.html
---

# SageMakerAlgorithmRecommendation

The recommended instance types for training and inference with a SageMaker algorithm.

## Contents
<a name="API_marketplace-discovery_SageMakerAlgorithmRecommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** recommendedBatchTransformInstanceType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerAlgorithmRecommendation-recommendedBatchTransformInstanceType"></a>
The instance type that the seller recommends for batch transform jobs with this algorithm.
Type: String
Required: Yes

 ** recommendedTrainingInstanceType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerAlgorithmRecommendation-recommendedTrainingInstanceType"></a>
The recommended instance type for training.
Type: String
Required: Yes

 ** recommendedRealtimeInferenceInstanceType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerAlgorithmRecommendation-recommendedRealtimeInferenceInstanceType"></a>
The instance type that the seller recommends for real-time inference endpoints with this algorithm.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_SageMakerAlgorithmRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SageMakerAlgorithmRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SageMakerAlgorithmRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SageMakerAlgorithmRecommendation)
