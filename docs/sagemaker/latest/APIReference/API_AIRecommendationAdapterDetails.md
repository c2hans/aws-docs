---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationAdapterDetails.html
---

# AIRecommendationAdapterDetails
<a name="API_AIRecommendationAdapterDetails"></a>

The per-recommendation LoRA adapter details. Contains both the model package ARNs and Amazon S3 URIs for each adapter, regardless of which form was originally supplied in the request. When you supply only Amazon S3 URIs, Amazon SageMaker AI creates model packages on your behalf.

## Contents
<a name="API_AIRecommendationAdapterDetails_Contents"></a>

 ** ModelPackageArns **   <a name="sagemaker-Type-AIRecommendationAdapterDetails-ModelPackageArns"></a>
The list of LoRA adapters with their model package ARNs.
Type: Array of [AIAdapterModelPackageEntry](API_AIAdapterModelPackageEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** S3Uris **   <a name="sagemaker-Type-AIRecommendationAdapterDetails-S3Uris"></a>
The list of LoRA adapters with their Amazon S3 URIs.
Type: Array of [AIAdapterS3Entry](API_AIAdapterS3Entry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_AIRecommendationAdapterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationAdapterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationAdapterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationAdapterDetails)
