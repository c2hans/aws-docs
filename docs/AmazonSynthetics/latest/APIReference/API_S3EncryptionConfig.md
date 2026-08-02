---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_S3EncryptionConfig.html
---

# S3EncryptionConfig
<a name="API_S3EncryptionConfig"></a>

A structure that contains the configuration of encryption-at-rest settings for canary artifacts that the canary uploads to Amazon S3.

For more information, see [Encrypting canary artifacts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html)

## Contents
<a name="API_S3EncryptionConfig_Contents"></a>

 ** EncryptionMode **   <a name="synthetics-Type-S3EncryptionConfig-EncryptionMode"></a>
 The encryption method to use for artifacts created by this canary. Specify `SSE_S3` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify `SSE-KMS` to use server-side encryption with a customer-managed AWS KMS key.
If you omit this parameter, an AWS-managed AWS KMS key is used.
Type: String
Valid Values: `SSE_S3 | SSE_KMS`
Required: No

 ** KmsKeyArn **   <a name="synthetics-Type-S3EncryptionConfig-KmsKeyArn"></a>
The ARN of the customer-managed AWS KMS key to use, if you specify `SSE-KMS` for `EncryptionMode`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:kms:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:key/[\w\-\/]+`
Required: No

## See Also
<a name="API_S3EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/S3EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/S3EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/S3EncryptionConfig)
