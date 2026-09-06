---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationModelDetails.html
---

# AIRecommendationModelDetails
<a name="API_AIRecommendationModelDetails"></a>

Details about the model package in a recommendation.

## Contents
<a name="API_AIRecommendationModelDetails_Contents"></a>

 ** InferenceSpecificationName **   <a name="sagemaker-Type-AIRecommendationModelDetails-InferenceSpecificationName"></a>
The name of the inference specification within the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** InstanceDetails **   <a name="sagemaker-Type-AIRecommendationModelDetails-InstanceDetails"></a>
The instance details for this recommendation, including instance type, count, and model copies per instance.
Type: Array of [AIRecommendationInstanceDetail](API_AIRecommendationInstanceDetail.md) objects
Required: No

 ** ModelPackageArn **   <a name="sagemaker-Type-AIRecommendationModelDetails-ModelPackageArn"></a>
The Amazon Resource Name (ARN) of the model package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

## See Also
<a name="API_AIRecommendationModelDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationModelDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationModelDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationModelDetails)
