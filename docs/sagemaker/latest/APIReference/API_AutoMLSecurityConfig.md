---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLSecurityConfig.html
---

# AutoMLSecurityConfig
<a name="API_AutoMLSecurityConfig"></a>

Security options.

## Contents
<a name="API_AutoMLSecurityConfig_Contents"></a>

 ** EnableInterContainerTrafficEncryption **   <a name="sagemaker-Type-AutoMLSecurityConfig-EnableInterContainerTrafficEncryption"></a>
Whether to use traffic encryption between the container layers.
Type: Boolean
Required: No

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-AutoMLSecurityConfig-VolumeKmsKeyId"></a>
The key used to encrypt stored data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-AutoMLSecurityConfig-VpcConfig"></a>
The VPC configuration.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_AutoMLSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLSecurityConfig)
