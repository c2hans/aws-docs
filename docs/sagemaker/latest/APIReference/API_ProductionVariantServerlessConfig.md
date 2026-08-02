---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantServerlessConfig.html
---

# ProductionVariantServerlessConfig
<a name="API_ProductionVariantServerlessConfig"></a>

Specifies the serverless configuration for an endpoint variant.

## Contents
<a name="API_ProductionVariantServerlessConfig_Contents"></a>

 ** MaxConcurrency **   <a name="sagemaker-Type-ProductionVariantServerlessConfig-MaxConcurrency"></a>
The maximum number of concurrent invocations your serverless endpoint can process.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: Yes

 ** MemorySizeInMB **   <a name="sagemaker-Type-ProductionVariantServerlessConfig-MemorySizeInMB"></a>
The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 6144.
Required: Yes

 ** ProvisionedConcurrency **   <a name="sagemaker-Type-ProductionVariantServerlessConfig-ProvisionedConcurrency"></a>
The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency`.
This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

## See Also
<a name="API_ProductionVariantServerlessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantServerlessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantServerlessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantServerlessConfig)
