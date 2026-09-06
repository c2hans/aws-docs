---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringOutputConfig.html
---

# MonitoringOutputConfig
<a name="API_MonitoringOutputConfig"></a>

The output configuration for monitoring jobs.

## Contents
<a name="API_MonitoringOutputConfig_Contents"></a>

 ** MonitoringOutputs **   <a name="sagemaker-Type-MonitoringOutputConfig-MonitoringOutputs"></a>
Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.
Type: Array of [MonitoringOutput](API_MonitoringOutput.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-MonitoringOutputConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker AI uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_MonitoringOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringOutputConfig)
