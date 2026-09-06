---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EncryptionConfigurationForRepositoryCreationTemplate.html
---

# EncryptionConfigurationForRepositoryCreationTemplate
<a name="API_EncryptionConfigurationForRepositoryCreationTemplate"></a>

The encryption configuration to associate with the repository creation template.

## Contents
<a name="API_EncryptionConfigurationForRepositoryCreationTemplate_Contents"></a>

 ** encryptionType **   <a name="ECR-Type-EncryptionConfigurationForRepositoryCreationTemplate-encryptionType"></a>
The encryption type to use.
If you use the `KMS` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS. When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. For more information, see [Protecting data using server-side encryption with an AWS KMS key stored in AWS Key Management Service (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Console Developer Guide*.
If you use the `AES256` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm. For more information, see [Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in the *Amazon Simple Storage Service Console Developer Guide*.
Type: String
Valid Values: `AES256 | KMS | KMS_DSSE`
Required: Yes

 ** kmsKey **   <a name="ECR-Type-EncryptionConfigurationForRepositoryCreationTemplate-kmsKey"></a>
If you use the `KMS` encryption type, specify the AWS KMS key to use for encryption. The full ARN of the AWS KMS key must be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^$|arn:aws[a-z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key\/[a-z0-9-]+`
Required: No

## See Also
<a name="API_EncryptionConfigurationForRepositoryCreationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/EncryptionConfigurationForRepositoryCreationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/EncryptionConfigurationForRepositoryCreationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/EncryptionConfigurationForRepositoryCreationTemplate)
