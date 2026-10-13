---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceCatalog.html
---

# ResourceCatalog
<a name="API_ResourceCatalog"></a>

 A resource catalog containing all of the resources of a specific resource type within a resource owner account. For an example on sharing the Amazon SageMaker Feature Store `DefaultFeatureGroupCatalog`, see [Share Amazon SageMaker Catalog resource type](https://docs.aws.amazon.com/sagemaker/latest/APIReference/feature-store-cross-account-discoverability-share-sagemaker-catalog.html) in the Amazon SageMaker Developer Guide.

## Contents
<a name="API_ResourceCatalog_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ResourceCatalog-CreationTime"></a>
 The time the `ResourceCatalog` was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="sagemaker-Type-ResourceCatalog-Description"></a>
 A free form description of the `ResourceCatalog`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** ResourceCatalogArn **   <a name="sagemaker-Type-ResourceCatalog-ResourceCatalogArn"></a>
 The Amazon Resource Name (ARN) of the `ResourceCatalog`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:sagemaker-catalog/.*`
Required: Yes

 ** ResourceCatalogName **   <a name="sagemaker-Type-ResourceCatalog-ResourceCatalogName"></a>
 The name of the `ResourceCatalog`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_ResourceCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResourceCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResourceCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResourceCatalog)
