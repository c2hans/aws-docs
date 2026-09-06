---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageSecurityConfig.html
---

# ModelPackageSecurityConfig
<a name="API_ModelPackageSecurityConfig"></a>

An optional AWS Key Management Service key to encrypt, decrypt, and re-encrypt model package information for regulated workloads with highly sensitive data.

## Contents
<a name="API_ModelPackageSecurityConfig_Contents"></a>

 ** KmsKeyId **   <a name="sagemaker-Type-ModelPackageSecurityConfig-KmsKeyId"></a>
The AWS KMS Key ID (`KMSKeyId`) used for encryption of model package information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: Yes

## See Also
<a name="API_ModelPackageSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageSecurityConfig)
