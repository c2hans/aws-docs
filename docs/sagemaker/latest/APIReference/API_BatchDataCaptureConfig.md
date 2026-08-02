---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDataCaptureConfig.html
---

# BatchDataCaptureConfig
<a name="API_BatchDataCaptureConfig"></a>

Configuration to control how SageMaker captures inference data for batch transform jobs.

## Contents
<a name="API_BatchDataCaptureConfig_Contents"></a>

 ** DestinationS3Uri **   <a name="sagemaker-Type-BatchDataCaptureConfig-DestinationS3Uri"></a>
The Amazon S3 location being used to capture the data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** GenerateInferenceId **   <a name="sagemaker-Type-BatchDataCaptureConfig-GenerateInferenceId"></a>
Flag that indicates whether to append inference id to the output.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="sagemaker-Type-BatchDataCaptureConfig-KmsKeyId"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the batch transform job.
The KmsKeyId can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_BatchDataCaptureConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDataCaptureConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDataCaptureConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDataCaptureConfig)
