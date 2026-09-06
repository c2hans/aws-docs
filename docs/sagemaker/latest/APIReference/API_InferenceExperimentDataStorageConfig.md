---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceExperimentDataStorageConfig.html
---

# InferenceExperimentDataStorageConfig
<a name="API_InferenceExperimentDataStorageConfig"></a>

The Amazon S3 location and configuration for storing inference request and response data.

## Contents
<a name="API_InferenceExperimentDataStorageConfig_Contents"></a>

 ** Destination **   <a name="sagemaker-Type-InferenceExperimentDataStorageConfig-Destination"></a>
The Amazon S3 bucket where the inference request and response data is stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** ContentType **   <a name="sagemaker-Type-InferenceExperimentDataStorageConfig-ContentType"></a>
Configuration specifying how to treat different headers. If no headers are specified Amazon SageMaker AI will by default base64 encode when capturing the data.
Type: [CaptureContentTypeHeader](API_CaptureContentTypeHeader.md) object
Required: No

 ** KmsKey **   <a name="sagemaker-Type-InferenceExperimentDataStorageConfig-KmsKey"></a>
 The AWS Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_InferenceExperimentDataStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceExperimentDataStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceExperimentDataStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceExperimentDataStorageConfig)
