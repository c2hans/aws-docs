---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentDataCacheConfig.html
---

# InferenceComponentDataCacheConfig
<a name="API_InferenceComponentDataCacheConfig"></a>

Settings that affect how the inference component caches data.

## Contents
<a name="API_InferenceComponentDataCacheConfig_Contents"></a>

 ** EnableCaching **   <a name="sagemaker-Type-InferenceComponentDataCacheConfig-EnableCaching"></a>
Sets whether the endpoint that hosts the inference component caches the model artifacts and container image.
With caching enabled, the endpoint caches this data in each instance that it provisions for the inference component. That way, the inference component deploys faster during the auto scaling process. If caching isn't enabled, the inference component takes longer to deploy because of the time it spends downloading the data.
Type: Boolean
Required: Yes

## See Also
<a name="API_InferenceComponentDataCacheConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentDataCacheConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentDataCacheConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentDataCacheConfig)
