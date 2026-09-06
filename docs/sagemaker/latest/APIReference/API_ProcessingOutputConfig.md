---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingOutputConfig.html
---

# ProcessingOutputConfig
<a name="API_ProcessingOutputConfig"></a>

Configuration for uploading output from the processing container.

## Contents
<a name="API_ProcessingOutputConfig_Contents"></a>

 ** Outputs **   <a name="sagemaker-Type-ProcessingOutputConfig-Outputs"></a>
An array of outputs configuring the data to upload from the processing container.
Type: Array of [ProcessingOutput](API_ProcessingOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-ProcessingOutputConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the processing job output. `KmsKeyId` can be an ID of a KMS key, ARN of a KMS key, or alias of a KMS key. The `KmsKeyId` is applied to all outputs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_ProcessingOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingOutputConfig)
