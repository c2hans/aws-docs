---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SourceAlgorithm.html
---

# SourceAlgorithm
<a name="API_SourceAlgorithm"></a>

Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.

## Contents
<a name="API_SourceAlgorithm_Contents"></a>

 ** AlgorithmName **   <a name="sagemaker-Type-SourceAlgorithm-AlgorithmName"></a>
The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: Yes

 ** ModelDataETag **   <a name="sagemaker-Type-SourceAlgorithm-ModelDataETag"></a>
The ETag associated with Model Data URL.
Type: String
Required: No

 ** ModelDataSource **   <a name="sagemaker-Type-SourceAlgorithm-ModelDataSource"></a>
Specifies the location of ML model data to deploy during endpoint creation.
Type: [ModelDataSource](API_ModelDataSource.md) object
Required: No

 ** ModelDataUrl **   <a name="sagemaker-Type-SourceAlgorithm-ModelDataUrl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).
The model artifacts must be in an S3 bucket that is in the same AWS region as the algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_SourceAlgorithm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SourceAlgorithm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SourceAlgorithm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SourceAlgorithm)
