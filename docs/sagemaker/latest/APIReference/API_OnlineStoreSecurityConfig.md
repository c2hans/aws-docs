---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreSecurityConfig.html
---

# OnlineStoreSecurityConfig
<a name="API_OnlineStoreSecurityConfig"></a>

The security configuration for `OnlineStore`.

## Contents
<a name="API_OnlineStoreSecurityConfig_Contents"></a>

 ** KmsKeyId **   <a name="sagemaker-Type-OnlineStoreSecurityConfig-KmsKeyId"></a>
The AWS Key Management Service (KMS) key ARN that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.
The caller (either user or IAM role) of `CreateFeatureGroup` must have below permissions to the `OnlineStore` `KmsKeyId`:
+  `"kms:Encrypt"`
+  `"kms:Decrypt"`
+  `"kms:DescribeKey"`
+  `"kms:CreateGrant"`
+  `"kms:RetireGrant"`
+  `"kms:ReEncryptFrom"`
+  `"kms:ReEncryptTo"`
+  `"kms:GenerateDataKey"`
+  `"kms:ListAliases"`
+  `"kms:ListGrants"`
+  `"kms:RevokeGrant"`
The caller (either user or IAM role) to all DataPlane operations (`PutRecord`, `GetRecord`, `DeleteRecord`) must have the following permissions to the `KmsKeyId`:
+  `"kms:Decrypt"`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_OnlineStoreSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OnlineStoreSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OnlineStoreSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OnlineStoreSecurityConfig)
