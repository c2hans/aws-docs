---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationJobOutputConfig.html
---

# OptimizationJobOutputConfig
<a name="API_OptimizationJobOutputConfig"></a>

Details for where to store the optimized model that you create with the optimization job.

## Contents
<a name="API_OptimizationJobOutputConfig_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-OptimizationJobOutputConfig-S3OutputLocation"></a>
The Amazon S3 URI for where to store the optimized model that you create with an optimization job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-OptimizationJobOutputConfig-KmsKeyId"></a>
The Amazon Resource Name (ARN) of a key in AWS KMS. SageMaker uses they key to encrypt the artifacts of the optimized model when SageMaker uploads the model to Amazon S3.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** SageMakerModel **   <a name="sagemaker-Type-OptimizationJobOutputConfig-SageMakerModel"></a>
The name of a SageMaker model to use as the output destination for an optimization job.
Type: [OptimizationSageMakerModel](API_OptimizationSageMakerModel.md) object
Required: No

## See Also
<a name="API_OptimizationJobOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OptimizationJobOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OptimizationJobOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OptimizationJobOutputConfig)
